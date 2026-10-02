# SNT Studios — Website Oficial

Landing page moderna, responsiva e de alta conversão para o **SNT Studios** em Guarulhos - SP (próximo ao Aeroporto Internacional GRU).

- **Domínio canônico:** `www.sntstudios.com`
- **Domínio alternativo:** `www.sntstudios.com.br`
- **WhatsApp Oficial:** `(11) 5444-3110`
- **Gestão Operacional:** Integrado ao SNT Command Center

## Tecnologias
- HTML5 Semântico
- Tailwind CSS
- Design System Dark Boutique Hospitality
- Integração direta com WhatsApp e Google Maps

## Publicação
Pronto para hospedagem com 0 custo no **GitHub Pages**, **Cloudflare Pages** ou **Vercel**.
O arquivo `CNAME` aponta para `www.sntstudios.com`. Os domínios sem `www` e o domínio `.com.br` devem redirecionar para o canônico na plataforma de hospedagem.

## Fotos do site

Os JPEGs em `assets/fotos` são os originais e não são enviados pela Vercel.
Antes de incluir ou trocar fotos, gere novamente as versões leves e o HTML:

```bash
python optimize_images.py
python build_site.py
npm ci
npm run build:css
python validate_site.py
```

O otimizador corrige a orientação, limita a maior dimensão a 1.920 px, gera
WebP e recria a capa social. O site e as galerias devem sempre apontar para as
versões WebP.

O Tailwind também é compilado em `assets/site.css`: o navegador não executa
o compilador via CDN. A CI recria esse arquivo e falha se alguém alterar o HTML
sem versionar o CSS correspondente.
