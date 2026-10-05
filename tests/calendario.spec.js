// O calendário e a cotação, no navegador (fila do bot, item 160).
//
// A API do bot é simulada: o teste prova a página, não a produção. Datas
// relativas a hoje, calculadas DENTRO do navegador (o fuso dele é o que a
// página usa).
"use strict";
const { test, expect } = require("@playwright/test");

async function hojeMais(page, dias) {
  return page.evaluate((n) => {
    const d = new Date(); d.setDate(d.getDate() + n);
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
  }, dias);
}

test.beforeEach(async ({ page }) => {
  // window.open do WhatsApp vira registro, sem abrir nada.
  await page.addInitScript(() => {
    window.__abertos = [];
    window.open = (url) => { window.__abertos.push(String(url)); return null; };
  });
  // O navegador do teste roda no fuso desta máquina, o mesmo do Node.
  const d = new Date(); d.setDate(d.getDate() + 12);
  const ocupada = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
  await page.route("**/api/studios/public/ocupacao**", (route) =>
    route.fulfill({ json: { ok: true, totalmenteOcupadas: [ocupada] } }));
  await page.route("**/api/studios/public/cotacao**", async (route) => {
    const u = new URL(route.request().url());
    await route.fulfill({
      json: {
        ok: true, entrada: u.searchParams.get("entrada"), saida: u.searchParams.get("saida"),
        studios: [
          { numero: 12, disponivel: true, totalDireta: 870, economia: 97, noites: 3, porNoite: 290 },
          { numero: 11, disponivel: false },
        ],
      },
    });
  });
  await page.goto("/");
});

test("abre como sobreposição na tela, fica aberto na primeira data, fecha na segunda e cota", async ({ page }) => {
  const entrada = await hojeMais(page, 5);
  const saida = await hojeMais(page, 8);
  const ocupada = await hojeMais(page, 12);

  await page.locator("#airbnbDateBox button").first().click();
  const cal = page.locator("#calendarioAirbnb");
  await expect(cal).toBeVisible();
  // Sobreposição: filho do body e inteiro dentro da tela (o defeito de 03/10
  // abria o seletor fora da área visível).
  expect(await cal.evaluate((el) => el.parentElement === document.body)).toBe(true);
  const caixa = await cal.boundingBox();
  const tela = page.viewportSize();
  expect(caixa.y).toBeGreaterThanOrEqual(0);
  expect(caixa.x).toBeGreaterThanOrEqual(0);
  expect(caixa.x + caixa.width).toBeLessThanOrEqual(tela.width + 1);
  expect(caixa.y).toBeLessThan(tela.height);

  // Data totalmente ocupada não se escolhe.
  await expect(page.locator(`#calendarioAirbnb button[data-date="${ocupada}"]`).first()).toBeDisabled();

  // Primeira data: o calendário continua aberto (o outro defeito de 03/10).
  await page.locator(`#calendarioAirbnb button[data-date="${entrada}"]`).first().click();
  await page.waitForTimeout(400);
  await expect(cal).toBeVisible();
  await expect(page.locator("#inputCheckIn")).toHaveValue(entrada);

  // Segunda data: fecha e cota sozinho.
  await page.locator(`#calendarioAirbnb button[data-date="${saida}"]`).first().click();
  await expect(cal).toBeHidden();
  await expect(page.locator("#inputCheckOut")).toHaveValue(saida);
  const resultado = page.locator("#resultadoCotacao");
  await expect(resultado).toContainText("Studio Amplo A");
  await expect(resultado).toContainText("870");
});

test("o botão do WhatsApp leva as datas e o studio da cotação", async ({ page }) => {
  const entrada = await hojeMais(page, 5);
  const saida = await hojeMais(page, 8);
  await page.locator("#airbnbDateBox button").first().click();
  await page.locator(`#calendarioAirbnb button[data-date="${entrada}"]`).first().click();
  await page.locator(`#calendarioAirbnb button[data-date="${saida}"]`).first().click();
  await expect(page.locator("#resultadoCotacao")).toContainText("Studio Amplo A");

  await page.locator("#resultadoCotacao button[onclick*='abrirWhatsAppCotacao']").first().click();
  const abertos = await page.evaluate(() => window.__abertos);
  expect(abertos.length).toBe(1);
  const url = new URL(abertos[0]);
  expect(url.hostname).toBe("api.whatsapp.com");
  expect(url.searchParams.get("phone")).toBe("551154443110");
  const texto = url.searchParams.get("text");
  expect(texto).toContain("Studio Amplo A");
  const br = (iso) => iso.split("-").reverse().join("/");
  expect(texto.includes(br(entrada)) || texto.includes(entrada)).toBe(true);
  // 05/10/2026: a mensagem leva só o valor, sem desconto nem comparação com as plataformas.
  expect(texto).not.toMatch(/desconto|economia|plataformas/i);
});

test("trocar o idioma traduz o calendário e fica guardado", async ({ page }) => {
  await page.locator("#btnLangEn").click();
  expect(await page.evaluate(() => localStorage.getItem("snt_studios_lang"))).toBe("en");
  await page.locator("#airbnbDateBox button").first().click();
  const dia = page.locator("#calendarioAirbnb button[data-date]:not([disabled])").first();
  await expect(dia).toHaveAttribute("aria-label", /(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)/);
  await page.reload();
  expect(await page.evaluate(() => localStorage.getItem("snt_studios_lang"))).toBe("en");
});

test("o site não fala em 10% de desconto em nenhum idioma (05/10/2026)", async ({ page }) => {
  for (const idioma of ["pt", "en", "es"]) {
    await page.evaluate((i) => window.trocarIdioma(i), idioma);
    const texto = await page.locator("body").innerText();
    expect(texto, idioma).not.toMatch(/10\s?%/);
  }
  const html = await page.content();
  expect(html).not.toMatch(/10\s?%|10%25/);
});