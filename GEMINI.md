# Diretrizes de Engenharia e Performance — snt-studios-site

1. **Zero CDNs em Produção**:
   - É terminantemente proibido o uso de `cdn.tailwindcss.com` ou scripts de estilo externos em produção.
   - Todo CSS deve ser compilado e minificado via Tailwind CLI em `assets/site.css` (`npm run build:css`).
   - A esteira de CI (`.github/workflows/verify.yml`) valida `npm run verify:css` e bloqueia deploys se o CSS estiver desatualizado.
2. **Otimização de Mídia e Imagens**:
   - Proibido subir fotos brutas de câmera (2 MB a 5 MB).
   - Todas as fotos da galeria e capas devem ser mantidas em **WebP** com peso unitário inferior a 150 KB.
   - O payload total da página inicial deve permanecer abaixo de 4 MB.
3. **Consistência de Domínio, Canônico e SEO**:
   - O domínio canônico oficial é `https://www.sntstudios.com/`.
   - Manter tags canônicas, OpenGraph, Twitter Cards e schema estruturado (`LodgingBusiness` com CNPJ `63.223.844/0001-11`) 100% alinhados.
4. **Higiene Pública de Links e Rotas**:
   - NUNCA expor URLs de painéis internos, links de gestão ou rotas administrativas em rodapés ou menus públicos.
   - Formulários e CTAs do WhatsApp devem usar o endpoint direto `https://api.whatsapp.com/send?phone=...` com codificação limpa, sem emojis ou caracteres especiais de 4 bytes que causem corrupção de texto no redirecionamento.
5. **Definição de Pronto**:
   - Executar `python validate_site.py` antes de qualquer commit (validar integridade de todos os recursos e scripts).
