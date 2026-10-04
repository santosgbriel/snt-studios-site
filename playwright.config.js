// Suíte do navegador (fila do bot, item 160, 04/10/2026): o calendário e a
// cotação provados de verdade, em desktop e celular. Os testes estáticos
// (validate_site.py, test_frontend.py) passavam com o calendário abrindo fora
// da tela e fechando depois da primeira data.
//
// Local: `npm run test:navegador` usa o Google Chrome instalado (PW_CHANNEL=chrome
// por padrão no Windows). No CI, o Chromium do Playwright.
"use strict";
const { defineConfig, devices } = require("@playwright/test");

const canal = process.env.PW_CHANNEL || (process.platform === "win32" ? "chrome" : undefined);
const comCanal = (d) => (canal ? { ...d, channel: canal } : d);

module.exports = defineConfig({
  testDir: "./tests",
  timeout: 30000,
  retries: process.env.CI ? 1 : 0,
  reporter: process.env.CI ? [["list"], ["github"]] : "list",
  use: { baseURL: "http://localhost:4173", trace: "retain-on-failure" },
  webServer: { command: "node tests/servidor.js", url: "http://localhost:4173", reuseExistingServer: !process.env.CI },
  projects: [
    { name: "desktop", use: comCanal({ ...devices["Desktop Chrome"] }) },
    { name: "celular", use: comCanal({ ...devices["Pixel 7"] }) },
  ],
});
