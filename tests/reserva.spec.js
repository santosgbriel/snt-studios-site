// Reserva direta com pagamento (STU-021/022): o botão na cotação, o
// formulário de /reserva/ e a volta do pagamento. A API do bot é simulada; a
// Pagar.me também (o "checkout" é uma página falsa deste servidor).
"use strict";
const { test, expect } = require("@playwright/test");

const COTACAO = {
  ok: true, entrada: "2030-03-10", saida: "2030-03-12", noites: 2,
  studios: [{ numero: "12", disponivel: true, noites: 2, totalDireta: 520, totalCartao: 546, parcelasCartao: 3, valorParcela: 182 }],
};
const VENDA_LIGADA = { ok: true, disponivel: true, teste: false, valorTeste: null, politica: "Cancelamento grátis até 7 dias antes da entrada.", minutosParaPagar: 30 };

async function simular(page, { venda = VENDA_LIGADA, cotacao = COTACAO, aoPagar = null, situacao = null } = {}) {
  const pedidos = [];
  await page.route("**/api/studios/public/venda**", async (route) => {
    if (route.request().method() === "POST") {
      const corpo = JSON.parse(route.request().postData() || "{}");
      pedidos.push(corpo);
      return route.fulfill(aoPagar ? aoPagar(corpo) : { json: { ok: true, codigo: "STABC123", url: "http://localhost:4173/checkout-falso.html" } });
    }
    return route.fulfill({ json: venda });
  });
  await page.route("**/api/studios/public/cotacao**", (route) => route.fulfill({ json: cotacao }));
  await page.route("**/api/studios/public/reserva**", (route) => route.fulfill(situacao ? situacao() : { status: 404, json: { ok: false } }));
  await page.route("**/checkout-falso.html", (route) => route.fulfill({ contentType: "text/html", body: "<h1>Checkout da Pagar.me</h1>" }));
  return pedidos;
}

const FORM = "/reserva/?studio=master&entrada=2030-03-10&saida=2030-03-12&hospedes=2&lang=pt";

test("formulário mostra a estadia com Pix e cartão, cobra campos e segue para o pagamento", async ({ page }) => {
  const pedidos = await simular(page, {
    aoPagar: (c) => (c.nome.trim().split(" ").length < 2
      ? { status: 422, json: { ok: false, erros: { nome: "nome e sobrenome", aceite: "aceite" } } }
      : { json: { ok: true, codigo: "STABC123", url: "http://localhost:4173/checkout-falso.html" } }),
  });
  await page.goto(FORM);
  await expect(page.getByRole("heading", { name: "Reserve e pague agora" })).toBeVisible();
  await expect(page.locator("#f-resumo")).toContainText("Studio Amplo A");
  await expect(page.locator("#f-resumo")).toContainText("10/03/2030");
  await expect(page.locator("#f-resumo")).toContainText("R$ 520,00");
  await expect(page.locator("#f-resumo")).toContainText("R$ 546,00");
  await expect(page.locator("#politica")).toHaveText("Cancelamento grátis até 7 dias antes da entrada.");

  await page.fill("[name=nome]", "Maria");
  await page.click("button.enviar");
  await expect(page.locator('[data-campo="nome"] .msg-erro')).toHaveText("Escreva nome e sobrenome.");
  await expect(page.locator("#erro-aceite")).toContainText("aceitar");

  await page.fill("[name=nome]", "Maria Souza");
  await page.fill("[name=email]", "maria@example.com");
  await page.fill("[name=telefone]", "+55 11 98765-4321");
  await page.fill("[name=documento]", "529.982.247-25");
  await page.check("[name=aceite]");
  await page.click("button.enviar");
  await expect(page.getByRole("heading", { name: "Checkout da Pagar.me" })).toBeVisible();
  const ultimo = pedidos[pedidos.length - 1];
  expect(ultimo).toMatchObject({ studio: "12", entrada: "2030-03-10", saida: "2030-03-12", hospedes: 2, documentoTipo: "cpf", aceite: true, idioma: "pt" });
  expect(ultimo.preco).toBeUndefined();
});

test("política no idioma escolhido, e a em português quando falta a tradução", async ({ page }) => {
  await simular(page, { venda: { ...VENDA_LIGADA, politica: "Grátis até 7 dias.", politicas: { pt: "Grátis até 7 dias.", en: "Free up to 7 days.", es: "" } } });
  await page.goto(FORM);
  await expect(page.locator("#politica")).toHaveText("Grátis até 7 dias.");
  await page.click('[data-lang="en"]');
  await expect(page.locator("#politica")).toHaveText("Free up to 7 days.");
  await page.click('[data-lang="es"]');
  await expect(page.locator("#politica")).toHaveText("Grátis até 7 dias.");
});

test("venda desligada: não mostra formulário e leva ao WhatsApp", async ({ page }) => {
  await simular(page, { venda: { ok: true, disponivel: false } });
  await page.goto(FORM);
  await expect(page.getByRole("heading", { name: "Pagamento pelo site indisponível" })).toBeVisible();
  await expect(page.locator("#form")).toBeHidden();
  await expect(page.locator("#problema-whats")).toHaveAttribute("href", /api\.whatsapp\.com/);
});

test("datas tomadas na hora de pagar: avisa sem sair da página", async ({ page }) => {
  await simular(page, { aoPagar: () => ({ status: 409, json: { ok: false, erro: "indisponivel" } }) });
  await page.goto(FORM);
  await page.fill("[name=nome]", "Maria Souza");
  await page.fill("[name=email]", "maria@example.com");
  await page.fill("[name=telefone]", "11987654321");
  await page.fill("[name=documento]", "52998224725");
  await page.check("[name=aceite]");
  await page.click("button.enviar");
  await expect(page.getByRole("heading", { name: "Datas indisponíveis" })).toBeVisible();
});

test("volta do pagamento: confirmada mostra o número da reserva e o check-in", async ({ page }) => {
  await simular(page, {
    situacao: () => ({ json: { ok: true, status: "confirmada", teste: false, studio: "12", entrada: "2030-03-10", saida: "2030-03-12", noites: 2, hospedes: 2,
      valores: { pix: 520, cartao: 546, parcelas: 3 }, pagamento: { metodo: "pix", valor: 520, parcelas: 1 }, reservaId: "95200001",
      checkin: "https://checkin.sntstudios.com/?t=c1.abc", pagarEm: null, expiraEm: 0 } }),
  });
  await page.goto("/reserva/?c=STABC123&lang=pt");
  await expect(page.getByRole("heading", { name: "Reserva confirmada!" })).toBeVisible();
  await expect(page.locator("#s-resumo")).toContainText("#95200001");
  await expect(page.locator("#s-resumo")).toContainText("R$ 520,00");
  await expect(page.getByRole("link", { name: "Fazer o check-in online" })).toHaveAttribute("href", "https://checkin.sntstudios.com/?t=c1.abc");
});

test("volta do pagamento: aguardando vira confirmada sozinha", async ({ page }) => {
  let n = 0;
  await simular(page, {
    situacao: () => {
      n += 1;
      const base = { ok: true, teste: false, studio: "12", entrada: "2030-03-10", saida: "2030-03-12", noites: 2, hospedes: 2, valores: { pix: 520, cartao: 546, parcelas: 3 }, expiraEm: Date.now() + 600000 };
      return { json: n < 2 ? { ...base, status: "aguardando", pagamento: null, pagarEm: "http://localhost:4173/checkout-falso.html" }
        : { ...base, status: "confirmada", pagamento: { metodo: "cartao", valor: 546, parcelas: 3 }, reservaId: "1", checkin: "https://checkin.sntstudios.com/?t=x" } };
    },
  });
  await page.goto("/reserva/?c=STABC123&lang=pt");
  await expect(page.getByRole("heading", { name: "Aguardando o pagamento" })).toBeVisible();
  await expect(page.getByRole("link", { name: "Voltar para o pagamento" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Reserva confirmada!" })).toBeVisible({ timeout: 8000 });
});

test("cotação do site: botão Reservar e pagar só com a venda ligada, e leva ao formulário", async ({ page }) => {
  await simular(page);
  await page.route("**/api/studios/public/ocupacao**", (route) => route.fulfill({ json: { ok: true, totalmenteOcupadas: [], diasSemCheckout: [] } }));
  await page.route("**/reserva/?**", (route) => route.fulfill({ contentType: "text/html", body: "<h1>formulário</h1>" }));
  await page.goto("/");
  await page.evaluate(() => {
    ultimaCotacao = { ok: true, entrada: "2030-03-10", saida: "2030-03-12", noites: 2, hospedes: "2", studios: [{ numero: "12", disponivel: true, totalDireta: 520, totalCartao: 546, parcelasCartao: 3, valorParcela: 182 }] };
    renderizarCardDisponibilidade('');
  });
  const pagar = page.locator('#resultadoCotacao [data-acao="pagar"]');
  await expect(pagar).toBeVisible();
  await expect(page.locator("#resultadoCotacao")).toContainText("Reservar no WhatsApp");
  await pagar.click();
  await expect(page).toHaveURL(/\/reserva\/\?studio=master&entrada=2030-03-10&saida=2030-03-12&hospedes=2&lang=pt/);
});

test("cotação do site: com a venda desligada, só o WhatsApp", async ({ page }) => {
  await simular(page, { venda: { ok: true, disponivel: false } });
  await page.route("**/api/studios/public/ocupacao**", (route) => route.fulfill({ json: { ok: true, totalmenteOcupadas: [], diasSemCheckout: [] } }));
  await page.goto("/");
  await page.evaluate(() => {
    ultimaCotacao = { ok: true, entrada: "2030-03-10", saida: "2030-03-12", noites: 2, hospedes: "2", studios: [{ numero: "12", disponivel: true, totalDireta: 520, totalCartao: 546, parcelasCartao: 3, valorParcela: 182 }] };
    renderizarCardDisponibilidade('');
  });
  await expect(page.locator("#resultadoCotacao")).toContainText("Reservar no WhatsApp");
  await expect(page.locator('#resultadoCotacao [data-acao="pagar"]')).toHaveCount(0);
});
