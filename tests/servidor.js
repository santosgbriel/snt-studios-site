// Servidor estático mínimo para a suíte do navegador: serve a pasta do site
// como o Vercel serviria (index.html na raiz), sem dependência nenhuma.
"use strict";
const http = require("http");
const fs = require("fs");
const path = require("path");

const RAIZ = path.join(__dirname, "..");
const PORTA = Number(process.env.PORTA || 4173);
const TIPOS = {
  ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript",
  ".json": "application/json", ".webmanifest": "application/manifest+json",
  ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp",
  ".svg": "image/svg+xml", ".ico": "image/x-icon", ".avif": "image/avif",
};

http.createServer((req, res) => {
  let caminho = decodeURIComponent(new URL(req.url, "http://x").pathname);
  if (caminho.endsWith("/")) caminho += "index.html";
  const arquivo = path.normalize(path.join(RAIZ, caminho));
  if (!arquivo.startsWith(RAIZ)) { res.writeHead(403); return res.end(); }
  fs.readFile(arquivo, (err, dados) => {
    if (err) { res.writeHead(404); return res.end("não encontrado"); }
    res.writeHead(200, { "Content-Type": TIPOS[path.extname(arquivo).toLowerCase()] || "application/octet-stream" });
    res.end(dados);
  });
}).listen(PORTA, () => console.log("site em http://localhost:" + PORTA));
