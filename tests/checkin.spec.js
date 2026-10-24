// O check-in online próprio (item 166), no navegador. A API do bot é
// simulada: o teste prova a página, não a produção.
"use strict";
const { test, expect } = require("@playwright/test");

const RESERVA = { ok: true, studio: "Studio 14 - Guarulhos", entrada: "2026-10-10", saida: "2026-10-13", noites: 3, hospedes: 2, preenchido: false, acessoEnviado: false, horario: "14:00" };
const TOKEN = "c1.token-opaco-assinado";

async function simular(page, { get = RESERVA, post } = {}) {
  const enviados = [];
  await page.route("**/api/studios/public/checkin**", async (route) => {
    const req = route.request();
    if (req.method() === "GET") return route.fulfill({ status: get.ok ? 200 : 404, json: get });
    const corpo = JSON.parse(req.postData() || "{}");
    enviados.push(corpo);
    return route.fulfill(post ? post(corpo) : { json: { ...RESERVA, preenchido: true } });
  });
  return enviados;
}

test("mostra studio e datas, e um acompanhante para reserva de 2 pessoas", async ({ page }) => {
  await simular(page);
  await page.goto("/checkin/?t=" + encodeURIComponent(TOKEN));
  await expect(page.locator("#r-studio")).toHaveText("Studio 14");
  await expect(page.locator("#r-entrada")).toHaveText("10/10/2026");
  await expect(page.locator(".acomp")).toHaveCount(1);
  await expect(page.locator(".sub")).toContainText(/14h|2 PM|14:00/);
});

test("envia a ficha com o link e mostra quando o acesso chega", async ({ page }) => {
  await page.clock.setFixedTime(new Date("2026-10-08T12:00:00-03:00"));
  const enviados = await simular(page);
  await page.goto("/checkin/?t=" + encodeURIComponent(TOKEN));
  await page.fill("[name=nome]", "Fulana Exemplo");
  await page.selectOption("[name=genero]", "feminino");
  await page.fill("[name=nascimento]", "1990-05-20");
  await page.fill("[name=documento]", "12345678900");
  await page.fill(".acomp [data-a=nome]", "Beltrano Exemplo");
  await page.selectOption(".acomp [data-a=genero]", "masculino");
  await page.fill(".acomp [data-a=nascimento]", "1988-01-02");
  await page.fill("[name=email]", "fulana@exemplo.com");
  await page.fill("[name=whatsapp]", "+55 11 91234-5678");
  await page.fill("[name=chegada]", "18:30");
  await page.check("[name=aceite]");
  await page.click(".enviar");
  await expect(page.locator("#pronto")).toBeVisible();
  await expect(page.locator("#pronto-txt")).toContainText("10/10/2026");
  expect(enviados).toHaveLength(1);
  const c = enviados[0];
  expect(c.t).toBe(TOKEN);
  expect(c.r).toBeUndefined();
  expect(c.d).toBeUndefined();
  expect(c.titular.nome).toBe("Fulana Exemplo");
  expect(c.acompanhantes).toHaveLength(1);
  expect(c.aceite).toBe(true);
  expect(c.idioma).toMatch(/^(pt|en|es)$/);
});

test("os erros da API voltam marcados no campo certo", async ({ page }) => {
  await simular(page, { post: () => ({ status: 422, json: { ok: false, erros: ["email", "aceite"] } }) });
  await page.goto("/checkin/?t=" + encodeURIComponent(TOKEN));
  await page.click(".enviar");
  await expect(page.locator("[data-campo=email]")).toHaveClass(/invalido/);
  await expect(page.locator("#erro-aceite")).not.toBeEmpty();
  await expect(page.locator("#pronto")).toBeHidden();
});

test("link sem reserva ou que não confere mostra o aviso, sem formulário", async ({ page }) => {
  await simular(page, { get: { ok: false, erro: "link_invalido" } });
  await page.goto("/checkin/?t=invalido");
  await expect(page.locator("#problema")).toBeVisible();
  await expect(page.locator("#form")).toBeHidden();
  await page.goto("/checkin/");
  await expect(page.locator("#problema")).toBeVisible();
});

test("token expirado orienta pedir um novo link", async ({ page }) => {
  await simular(page, { get: { ok: false, erro: "link_expirado" } });
  await page.goto("/checkin/?t=expirado&lang=pt");
  await expect(page.locator("#problema-tit")).toHaveText("Link expirado");
  await expect(page.locator("#problema-txt")).toContainText("novo link");
});

test("troca de idioma traduz a página", async ({ page }) => {
  await simular(page);
  await page.goto("/checkin/?t=" + encodeURIComponent(TOKEN) + "&lang=en");
  await expect(page.locator("h1")).toHaveText("Online check-in");
  await page.click("[data-lang=es]");
  await expect(page.locator(".enviar")).toHaveText("Enviar check-in");
  await expect(page.locator("legend").first()).toHaveText("Huésped responsable");
});

test("o horário do acesso sai no formato de cada idioma", async ({ page }) => {
  await simular(page);
  await page.goto("/checkin/?t=" + encodeURIComponent(TOKEN) + "&lang=pt");
  await expect(page.locator(".sub")).toContainText("a partir das 14h");
  await page.click("[data-lang=en]");
  await expect(page.locator(".sub")).toContainText("from 2 PM");
  await page.click("[data-lang=es]");
  await expect(page.locator(".sub")).toContainText("desde las 14:00");
});

test("check-in feito depois de a estadia começar diz que o acesso chega em minutos (22/10/2026)", async ({ page }) => {
  // Perdeu a noite de 10/10 e preencheu de madrugada no dia 11.
  await page.clock.setFixedTime(new Date("2026-10-11T05:50:00-03:00"));
  await simular(page);
  await page.goto("/checkin/?t=" + encodeURIComponent(TOKEN));
  await page.fill("[name=nome]", "Fulana Exemplo");
  await page.selectOption("[name=genero]", "feminino");
  await page.fill("[name=nascimento]", "1990-05-20");
  await page.fill("[name=documento]", "12345678900");
  await page.fill(".acomp [data-a=nome]", "Beltrano Exemplo");
  await page.selectOption(".acomp [data-a=genero]", "masculino");
  await page.fill(".acomp [data-a=nascimento]", "1988-01-02");
  await page.fill("[name=email]", "fulana@exemplo.com");
  await page.fill("[name=whatsapp]", "+55 11 91234-5678");
  await page.fill("[name=chegada]", "07:00");
  await page.check("[name=aceite]");
  await page.click(".enviar");
  await expect(page.locator("#pronto")).toBeVisible();
  await expect(page.locator("#pronto-txt")).toContainText(/poucos minutos|few minutes|pocos minutos/);
  await expect(page.locator("#pronto-txt")).not.toContainText("10/10/2026");
});
