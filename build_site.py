# -*- coding: utf-8 -*-
from pathlib import Path

"""
Site oficial do SNT Studios com experiência Airbnb (Listing Reserve Widget).
Totalmente multilíngue (PT / EN / ES), com calendário interativo de seleção de datas por dois cliques,
nomes comerciais exclusivos (sem números internos), total com diárias e limpeza embutidas (sem taxas extras),
e zero menções a ferramentas internas.
"""

site_code = '''<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SNT Studios · Hospitalidade & Hospedagem Próximo ao Aeroporto de Guarulhos (GRU)</title>
  
  <!-- SEO & Social Sharing -->
  <meta name="description" content="Studios privativos modernos e confortáveis em Guarulhos, a cerca de 20 minutos de carro do Aeroporto GRU. Internet fibra 600MB, fechadura eletrônica 24h, cozinha compacta e reserva direta pelo WhatsApp oficial.">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="https://www.sntstudios.com/">
  <meta property="og:title" content="SNT Studios · Hospedagem Moderna perto do Aeroporto GRU">
  <meta property="og:description" content="Reserve direto no WhatsApp oficial. Studios privativos com Wi-Fi 600MB, fechadura digital 24h e cozinha completa.">
  <meta property="og:image" content="https://www.sntstudios.com/assets/og-cover.jpg">
  <meta property="og:url" content="https://www.sntstudios.com/">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="SNT Studios">
  <meta name="twitter:card" content="summary_large_image">

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LodgingBusiness",
    "name": "SNT Studios",
    "legalName": "SNT Empreendimentos Imobiliários LTDA",
    "identifier": "63.223.844/0001-11",
    "url": "https://www.sntstudios.com/",
    "telephone": "+55 11 5444-3110",
    "image": "https://www.sntstudios.com/assets/og-cover.jpg",
    "priceRange": "$$",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Avenida Aguanil, 51",
      "addressLocality": "Guarulhos",
      "addressRegion": "SP",
      "addressCountry": "BR"
    }
  }
  </script>

  <!-- Favicon & Icons -->
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="assets/apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">
  <meta name="theme-color" content="#070b14">

  <!-- CSS compilado e purgado via Tailwind CLI (Zero CDN em produção) -->
  <link rel="stylesheet" href="assets/site.css">

  <!-- Google Fonts: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .glass-nav {
      background: rgba(7, 11, 20, 0.90);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
    }
    .glass-card {
      background: rgba(15, 23, 42, 0.80);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .glass-card:hover {
      border-color: rgba(16, 185, 129, 0.35);
    }
    .hero-glow {
      background: radial-gradient(circle at 50% 15%, rgba(16, 185, 129, 0.16) 0%, rgba(7, 11, 20, 0) 70%);
    }
    .modal-backdrop {
      background: rgba(2, 6, 23, 0.88);
      backdrop-filter: blur(8px);
    }
    @keyframes pulseFocus {
      0%, 100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
      50% { box-shadow: 0 0 0 6px rgba(16, 185, 129, 0.4); }
    }
    .card-pulse-highlight {
      animation: pulseFocus 1.2s ease-in-out 2;
    }
  </style>
</head>
<body class="bg-[#070b14] text-slate-100 antialiased selection:bg-emerald-500 selection:text-black">

  <!-- NAVBAR FIXA -->
  <nav class="fixed top-0 left-0 right-0 z-40 glass-nav border-b border-slate-800/80 transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- LOGO SNT STUDIOS -->
      <!-- Os prédios da SNT em vetor, no verde do site, colados ao nome (05/10/2026):
           o PNG da SNT Empreendimentos tinha fundo branco e parecia colado no cabeçalho. -->
      <a href="#inicio" class="flex items-center gap-2 group shrink-0 whitespace-nowrap" aria-label="SNT Studios · voltar ao início">
        <svg class="h-8 w-[23px] sm:h-10 sm:w-[29px] shrink-0 text-emerald-500 transition group-hover:text-emerald-400" viewBox="240 135 545 755" fill="none" stroke="currentColor" stroke-width="34" aria-hidden="true" focusable="false"><path d="M384.5 458V318L547 171V287L630 345V528"/><path d="M247 869H384.5V520"/><path d="M298 869V566L462 416V881"/><path d="M555 881V510L719 617V869"/><path d="M631 592V869H776"/></svg>
        <span class="flex flex-col leading-none">
          <span class="text-lg sm:text-xl font-extrabold tracking-tight text-white">SNT <span class="font-bold text-emerald-400">Studios</span></span>
          <span class="hidden sm:block mt-1 text-[10px] font-semibold uppercase tracking-[0.16em] text-slate-400">Guarulhos · GRU</span>
        </span>
      </a>

      <!-- MENU DESKTOP -->
      <div class="hidden lg:flex flex-1 justify-center items-center gap-5 xl:gap-7 ml-12 mr-8 xl:mx-16 text-sm font-medium text-slate-300 whitespace-nowrap">
        <a href="#cotador" class="hover:text-emerald-400 transition" data-i18n="nav_disponibilidade">Disponibilidade</a>
        <a href="#studios" class="hover:text-emerald-400 transition" data-i18n="nav_studios">Acomodações</a>
        <a href="#comodidades" class="hover:text-emerald-400 transition" data-i18n="nav_comodidades">Comodidades</a>
        <a href="#localizacao" class="hover:text-emerald-400 transition" data-i18n="nav_localizacao">Localização</a>
        <a href="#faq" class="hover:text-emerald-400 transition" data-i18n="nav_faq">Dúvidas</a>
      </div>

      <!-- SELETOR DE IDIOMAS & BOTAO WHATSAPP -->
      <div class="flex items-center gap-3">
        
        <!-- SELETOR MULTILÍNGUE (PT / EN / ES) -->
        <div class="flex items-center bg-slate-900 border border-slate-700/80 rounded-xl p-1 text-xs whitespace-nowrap shrink-0">
          <button type="button" onclick="trocarIdioma('pt')" id="btnLangPt" class="px-2 py-1 rounded-lg font-bold transition bg-emerald-500 text-slate-950" title="Português">
            PT
          </button>
          <button type="button" onclick="trocarIdioma('en')" id="btnLangEn" class="px-2 py-1 rounded-lg font-bold transition text-slate-400 hover:text-white" title="English">
            EN
          </button>
          <button type="button" onclick="trocarIdioma('es')" id="btnLangEs" class="px-2 py-1 rounded-lg font-bold transition text-slate-400 hover:text-white" title="Español">
            ES
          </button>
        </div>

        <a href="https://api.whatsapp.com/send?phone=551154443110" target="_blank" rel="noopener noreferrer" class="hidden 2xl:inline-flex items-center gap-2 text-xs font-semibold text-slate-300 hover:text-emerald-400 transition px-3 py-2 rounded-lg bg-slate-900 border border-slate-800 whitespace-nowrap">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>(11) 5444-3110</span>
        </a>
        <a href="https://api.whatsapp.com/send?phone=551154443110&text=Ola%21%20Gostaria%20de%20consultar%20uma%20reserva%20direta%20no%20SNT%20Studios." target="_blank" rel="noopener noreferrer" class="hidden sm:inline-flex items-center gap-2 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold px-5 py-2.5 rounded-xl text-sm shadow-lg shadow-emerald-500/20 transition transform hover:-translate-y-0.5 whitespace-nowrap shrink-0">
          <span data-i18n="btn_nav_reserva">Reservar no WhatsApp</span>
        </a>
      </div>

    </div>
  </nav>

  <!-- LISTING SHOWCASE (MODELO DE QUANDO O HÓSPEDE JÁ ESTÁ DENTRO DO IMÓVEL) -->
  <section id="inicio" class="relative pt-28 pb-16 lg:pt-36 lg:pb-24 hero-glow overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

      <!-- CABEÇALHO DO ANÚNCIO (SEM ESTRELAS / FOCO EM VALOR E LOCALIZAÇÃO) -->
      <div class="mb-6 space-y-2.5">
        <div class="flex flex-wrap items-center gap-2">
          <span class="inline-flex items-center gap-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 px-3 py-1 text-xs font-bold text-emerald-400" data-i18n="badge_topo_local">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            Hospedagem Privativa em Guarulhos · Aeroporto GRU
          </span>
          <span class="inline-flex items-center gap-1 rounded-full bg-slate-800 border border-slate-700 px-3 py-1 text-xs font-semibold text-slate-300" data-i18n="badge_topo_desconto">
            🛡️ Reserva direta pelo WhatsApp oficial
          </span>
          <span class="inline-flex items-center gap-1 rounded-full bg-slate-800 border border-slate-700 px-3 py-1 text-xs font-semibold text-slate-300" data-i18n="badge_topo_checkin">
            🔑 Auto Check-in 24h
          </span>
        </div>

        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white tracking-tight leading-tight" data-i18n="hero_title">SNT Studios · Studios Privativos em Guarulhos, perto do Aeroporto GRU</h1>

        <!-- BARRA SUB-HEADER -->
        <div class="flex flex-wrap items-center justify-between gap-3 text-xs sm:text-sm text-slate-300 pt-1 pb-4 border-b border-slate-800/80">
          <div class="flex flex-col sm:flex-row sm:flex-wrap sm:items-center gap-1 sm:gap-2">
            <span class="text-slate-300 font-semibold" data-i18n="sub_hospitalidade">Hospitalidade Independente</span>
            <span class="hidden sm:inline text-slate-500">·</span>
            <span class="text-slate-400" data-i18n="sub_gru_dist">Cerca de 20 minutos de carro dos Terminais 1, 2 e 3</span>
            <span class="hidden sm:inline text-slate-500">·</span>
            <a href="#localizacao" class="underline underline-offset-4 hover:text-emerald-400 text-slate-400">Avenida Aguanil, 51 · Seródio, Guarulhos - SP</a>
          </div>
          <div class="flex items-center gap-3">
            <button type="button" onclick="compartilharSite()" class="flex items-center gap-1.5 text-xs text-slate-400 hover:text-white transition">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/></svg>
              <span id="btnShareText" data-i18n="btn_compartilhar">Compartilhar</span>
            </button>
          </div>
        </div>
      </div>

      <!-- GRADE DE FOTOS AIRBNB (5 FOTOS COM A PRINCIPAL EM DESTAQUE) -->
      <div class="relative rounded-3xl overflow-hidden border border-slate-800 shadow-2xl mb-12 group">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-2 h-[340px] sm:h-[420px] lg:h-[480px]">
          <!-- Foto Principal Grande (Esquerda: 2 colunas no desktop) -->
          <div class="md:col-span-2 relative overflow-hidden bg-slate-950 cursor-pointer" onclick="abrirGaleria('master')">
            <img src="assets/fotos/20251030_162521(1).webp" alt="Studio Amplo A" class="w-full h-full object-cover group-hover:scale-[1.02] transition duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent flex flex-col justify-end p-5">
              <span class="bg-emerald-500 text-slate-950 text-[10px] font-black px-2.5 py-0.5 rounded shadow w-max mb-1 uppercase tracking-wider" data-i18n="tag_master_king">STUDIO AMPLO</span>
              <span class="text-white text-sm font-bold" data-i18n="desc_master_king_curta">Cama queen, bancada de trabalho e cortinas blackout</span>
            </div>
          </div>
          <!-- Coluna 2 (2 fotos empilhadas) -->
          <div class="hidden md:grid grid-rows-2 gap-2">
            <div class="relative overflow-hidden bg-slate-950 cursor-pointer" onclick="abrirGaleria('executivo')">
              <img src="assets/fotos/20251030_164004.webp" alt="Studio Amplo B" class="w-full h-full object-cover hover:scale-105 transition duration-500">
              <div class="absolute bottom-2 left-2 bg-slate-950/80 backdrop-blur px-2 py-0.5 rounded text-[10px] font-bold text-teal-300 border border-slate-700" data-i18n="tag_executivo_premium">Studio Amplo</div>
            </div>
            <div class="relative overflow-hidden bg-slate-950 cursor-pointer" onclick="abrirGaleria('master')">
              <img src="assets/fotos/20251030_144616.webp" alt="Cozinha Compacta Completa" class="w-full h-full object-cover hover:scale-105 transition duration-500">
              <div class="absolute bottom-2 left-2 bg-slate-950/80 backdrop-blur px-2 py-0.5 rounded text-[10px] font-bold text-emerald-300 border border-slate-700" data-i18n="tag_cozinha_priv">Cozinha Compacta</div>
            </div>
          </div>
          <!-- Coluna 3 (2 fotos empilhadas) -->
          <div class="hidden md:grid grid-rows-2 gap-2">
            <div class="relative overflow-hidden bg-slate-950 cursor-pointer" onclick="abrirGaleria('smart')">
              <img src="assets/fotos/20251030_143554.webp" alt="Studio Compacto A" class="w-full h-full object-cover hover:scale-105 transition duration-500">
              <div class="absolute bottom-2 left-2 bg-slate-950/80 backdrop-blur px-2 py-0.5 rounded text-[10px] font-bold text-slate-300 border border-slate-700" data-i18n="tag_standard_smart">Studio Compacto</div>
            </div>
            <div class="relative overflow-hidden bg-slate-950 cursor-pointer" onclick="abrirGaleria('cozy')">
              <img src="assets/fotos/20251030_144024.webp" alt="Studio Compacto B" class="w-full h-full object-cover hover:scale-105 transition duration-500">
              <div class="absolute bottom-2 left-2 bg-slate-950/80 backdrop-blur px-2 py-0.5 rounded text-[10px] font-bold text-slate-300 border border-slate-700" data-i18n="tag_standard_cozy">Studio Compacto</div>
            </div>
          </div>
        </div>
        <!-- Botão no Canto Inferior Direito: Mostrar todas as fotos -->
        <button type="button" onclick="abrirGaleria('todas')" class="absolute top-4 md:top-auto md:bottom-4 right-4 bg-slate-950/90 hover:bg-white hover:text-slate-950 backdrop-blur text-white text-xs font-extrabold px-4 py-2.5 rounded-xl border border-slate-700 transition flex items-center gap-2 shadow-2xl">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
          <span data-i18n="btn_todas_fotos">Mostrar todas as 20 fotos</span>
        </button>
      </div>

      <!-- GRID PRINCIPAL (COLUNA ESQUERDA: DETALHES | COLUNA DIREITA: STICKY AIRBNB RESERVE BOX) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start">
        
        <!-- COLUNA ESQUERDA: DETALHES DO ESPAÇO (7 COLUNAS) -->
        <div class="lg:col-span-7 space-y-8">
          
          <!-- RESUMO DO ESPAÇO -->
          <div class="flex items-start justify-between pb-6 border-b border-slate-800">
            <div>
              <h2 class="text-xl sm:text-2xl font-bold text-white" data-i18n="detalhe_tipo_espaco">Studio privativo inteiro · Hospedagem SNT</h2>
              <p class="text-xs sm:text-sm text-slate-400 mt-1" data-i18n="detalhe_capacidade">Até 2 hóspedes · 1 cama queen · 1 banheiro privativo · Cozinha compacta equipada</p>
            </div>
            <div class="w-12 h-12 rounded-full bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 font-extrabold text-sm shrink-0">
              SNT
            </div>
          </div>

          <!-- DESTAQUES NO ESTILO AIRBNB COM ÍCONES -->
          <div class="space-y-5 pb-6 border-b border-slate-800">
            <div class="flex items-start gap-4">
              <div class="w-6 text-xl text-emerald-400 shrink-0">🔑</div>
              <div>
                <h3 class="text-sm font-bold text-white" data-i18n="feature_checkin_tit">Auto check-in 24h via fechadura digital</h3>
                <p class="text-xs text-slate-400 mt-0.5" data-i18n="feature_checkin_desc">O portão abre por QR code e a porta do studio por uma senha só sua: chegue a qualquer hora da noite ou madrugada, sem chave física.</p>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-6 text-xl text-emerald-400 shrink-0">⚡</div>
              <div>
                <h3 class="text-sm font-bold text-white" data-i18n="feature_wifi_tit">Wi-Fi fibra de 600 Mbps dedicado</h3>
                <p class="text-xs text-slate-400 mt-0.5" data-i18n="feature_wifi_desc">Internet ultra-veloz testada para chamadas de vídeo, reuniões executivas e streaming 4K sem interrupções.</p>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-6 text-xl text-emerald-400 shrink-0">🍳</div>
              <div>
                <h3 class="text-sm font-bold text-white" data-i18n="feature_cozinha_tit">Cozinha privativa equipada</h3>
                <p class="text-xs text-slate-400 mt-0.5" data-i18n="feature_cozinha_desc">Geladeira com freezer, micro-ondas, cooktop, cafeteira elétrica, sanduicheira, panelas, louças e talheres.</p>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-6 text-xl text-emerald-400 shrink-0">✈️</div>
              <div>
                <h3 class="text-sm font-bold text-white" data-i18n="feature_gru_tit">Cerca de 20 min de carro do Aeroporto de Guarulhos (GRU)</h3>
                <p class="text-xs text-slate-400 mt-0.5" data-i18n="feature_gru_desc">São 12 a 14 km até os terminais, uns 21 a 22 minutos de carro ou aplicativo sem trânsito. A pé não dá: o caminho contorna o aeroporto.</p>
              </div>
            </div>
          </div>

          <!-- DESCRIÇÃO DO ESPAÇO E AS DUAS TIPOLOGIAS COMERCIAIS -->
          <div class="space-y-4 pb-6 border-b border-slate-800">
            <h3 class="text-base font-bold text-white" data-i18n="sobre_espaco_tit">Sobre o espaço</h3>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed" data-i18n="sobre_espaco_p1">
              O <strong>SNT Studios</strong> oferece uma proposta inteligente de hospitalidade autônoma: privacidade completa, acabamento refinado e excelente localização próxima ao Aeroporto GRU. Todas as acomodações são 100% privativas com banheiro exclusivo, bancada e ambiente climatizado.
            </p>
            
            <div class="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 space-y-3">
              <h4 class="text-xs font-bold uppercase tracking-wider text-emerald-400" data-i18n="tipologias_tit">Dois tamanhos, os mesmos itens</h4>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div class="p-3.5 rounded-xl bg-slate-800/60 border border-slate-700/60">
                  <span class="font-bold text-white block mb-1" data-i18n="cat_ampla_tit">Studios Amplos (2 unidades)</span>
                  <p class="text-slate-400 text-[11px]" data-i18n="cat_ampla_desc">Os dois maiores: mais área livre para circular e organizar a bagagem.</p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-800/60 border border-slate-700/60">
                  <span class="font-bold text-white block mb-1" data-i18n="cat_compacta_tit">Studios Compactos (2 unidades)</span>
                  <p class="text-slate-400 text-[11px]" data-i18n="cat_compacta_desc">Os dois menores: a mesma cama queen, cozinha e comodidades, numa planta mais enxuta.</p>
                </div>
              </div>
              <p class="text-[11px] text-slate-400" data-i18n="tipologias_nota">
                <em>Ao selecionar suas datas ao lado, o sistema verifica a disponibilidade em tempo real e calcula o valor total consolidado.</em>
              </p>
            </div>
          </div>

          <!-- O QUE ESSE LUGAR OFERECE (COMODIDADES AIRBNB) -->
          <div class="space-y-4 pb-6 border-b border-slate-800">
            <h3 class="text-base font-bold text-white" data-i18n="comodidades_grid_tit">O que esse lugar oferece</h3>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 text-xs text-slate-300">
              <div class="flex items-center gap-2.5"><span>⚡</span><span data-i18n="comod_wifi">Wi-Fi Fibra 600 Mbps</span></div>
              <div class="flex items-center gap-2.5"><span>🔑</span><span data-i18n="comod_fechadura">Fechadura digital 24h</span></div>
              <div class="flex items-center gap-2.5"><span>📺</span><span data-i18n="comod_tv">Smart TV com Streaming</span></div>
              <div class="flex items-center gap-2.5"><span>🍳</span><span data-i18n="comod_cooktop">Cozinha com Cooktop</span></div>
              <div class="flex items-center gap-2.5"><span>❄️</span><span data-i18n="comod_ar">Ar-condicionado split e aquecedor</span></div>
              <div class="flex items-center gap-2.5"><span>☕</span><span data-i18n="comod_cafe">Cafeteira elétrica</span></div>
              <div class="flex items-center gap-2.5"><span>🚿</span><span data-i18n="comod_ducha">Ducha quente</span></div>
              <div class="flex items-center gap-2.5"><span>🧺</span><span data-i18n="comod_enxoval">Enxoval higienizado</span></div>
              <div class="flex items-center gap-2.5"><span>💻</span><span data-i18n="comod_bancada">Bancada para notebook</span></div>
              <div class="flex items-center gap-2.5"><span>🛡️</span><span data-i18n="comod_cameras">Câmeras nas áreas comuns</span></div>
              <div class="flex items-center gap-2.5"><span>🚗</span><span data-i18n="comod_transporte">Fácil acesso para Uber/99</span></div>
              <div class="flex items-center gap-2.5"><span>🧊</span><span data-i18n="comod_frigobar">Geladeira e micro-ondas</span></div>
            </div>
          </div>

          <!-- REGRAS DA CASA RÁPIDAS -->
          <div class="space-y-2 text-xs text-slate-400">
            <div class="flex items-center gap-3">
              <span class="font-bold text-white" data-i18n="regra_checkin_tit">Check-in:</span>
              <span data-i18n="regra_checkin_val">A partir das 15:00 (Acesso autônomo 24h via código)</span>
            </div>
            <div class="flex items-center gap-3">
              <span class="font-bold text-white" data-i18n="regra_checkout_tit">Check-out:</span>
              <span data-i18n="regra_checkout_val">Até as 11:00</span>
            </div>
            <div class="flex items-center gap-3">
              <span class="font-bold text-white" data-i18n="regra_silencio_tit">Política de Silêncio:</span>
              <span data-i18n="regra_silencio_val">Respeito ao descanso dos demais hóspedes a partir das 22h</span>
            </div>
          </div>

        </div>

        <!-- COLUNA DIREITA: WIDGET DE RESERVA AIRBNB STICKY (5 COLUNAS) -->
        <div class="lg:col-span-5">
          <div class="lg:sticky lg:top-28">
            <div id="cotador" class="glass-card rounded-3xl p-6 sm:p-7 shadow-2xl border border-slate-700/80 hover:border-emerald-500/30 transition duration-300 relative">
              
              <!-- CABEÇALHO DO CARD: PREÇO POR NOITE E RESERVA DIRETA -->
              <div class="flex items-baseline justify-between mb-5">
                <div>
                  <span class="text-2xl sm:text-3xl font-black text-white" id="headerPrecoNoite" data-i18n="card_ver_valor">Ver valor</span>
                  <span id="headerPrecoSufixo" class="hidden text-xs sm:text-sm text-slate-400 font-medium" data-i18n="card_por_noite"> / noite</span>
                </div>
                <div class="text-xs text-slate-400 font-medium" data-i18n="card_tarifa_oficial">
                  Tarifa Oficial
                </div>
              </div>

              <!-- O BOXED SELECTOR AIRBNB COM CALENDÁRIO INTERATIVO POR CLIQUES -->
              <form id="formCotador" onsubmit="event.preventDefault(); consultarDisponibilidade();">
                
                <!-- CAMPOS OCULTOS PARA INTEGRAÇÃO -->
                <input type="hidden" id="inputCheckIn" value="">
                <input type="hidden" id="inputCheckOut" value="">

                <!-- CAIXA PRINCIPAL DE DATAS & HÓSPEDES (AIRBNB SIGNATURE BOX) -->
                <div id="airbnbDateBox" class="border border-slate-700 rounded-2xl bg-slate-900/90 overflow-hidden shadow-inner focus-within:ring-2 focus-within:ring-emerald-500/60 transition cursor-pointer">
                  
                  <!-- LINHA SUPERIOR: CHECK-IN E CHECKOUT DIVIDIDOS AO MEIO -->
                  <div class="grid grid-cols-2 divide-x divide-slate-700">
                    <button type="button" class="w-full p-3 sm:p-3.5 hover:bg-slate-800/40 transition cursor-pointer text-left" onclick="clicarBoxCheckIn()" aria-controls="calendarioAirbnb" aria-expanded="false" aria-label="Selecionar data de check-in">
                      <span class="block text-[10px] font-black uppercase tracking-wider text-slate-400" data-i18n="lbl_checkin">CHECK-IN</span>
                      <span id="displayCheckIn" class="block text-xs sm:text-sm font-semibold text-white mt-0.5" data-i18n="txt_inserir_data">Adicionar data</span>
                    </button>
                    <button type="button" class="w-full p-3 sm:p-3.5 hover:bg-slate-800/40 transition cursor-pointer text-left" onclick="clicarBoxCheckOut()" aria-controls="calendarioAirbnb" aria-expanded="false" aria-label="Selecionar data de checkout">
                      <span class="block text-[10px] font-black uppercase tracking-wider text-slate-400" data-i18n="lbl_checkout">CHECKOUT</span>
                      <span id="displayCheckOut" class="block text-xs sm:text-sm font-semibold text-white mt-0.5" data-i18n="txt_inserir_data">Adicionar data</span>
                    </button>
                  </div>

                  <!-- LINHA INFERIOR: HÓSPEDES LARGURA TOTAL -->
                  <div class="border-t border-slate-700 p-3 sm:p-3.5 hover:bg-slate-800/40 transition" onclick="event.stopPropagation()">
                    <label for="selectGuests" class="block text-[10px] font-black uppercase tracking-wider text-slate-400 cursor-pointer" data-i18n="lbl_hospedes">HÓSPEDES</label>
                    <div class="relative mt-0.5">
                      <select id="selectGuests" onchange="atualizarHospedes()" class="w-full bg-transparent text-xs sm:text-sm font-semibold text-white focus:outline-none cursor-pointer appearance-none pr-8">
                        <option value="1" class="bg-slate-900 text-white" data-i18n="opt_1_hospede">1 hóspede</option>
                        <option value="2" class="bg-slate-900 text-white" selected data-i18n="opt_2_hospedes">2 hóspedes (Casal)</option>
                      </select>
                      <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center text-slate-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                      </div>
                    </div>
                  </div>

                </div>

                <!-- CALENDÁRIO INTERATIVO AIRBNB (SELEÇÃO DE 2 CLIQUES + DUAL-MONTH) -->
                <div id="calendarioBackdrop" class="hidden fixed inset-0 z-[60] bg-slate-950/75 backdrop-blur-sm" aria-hidden="true" onclick="fecharCalendario()"></div>
                <div id="calendarioAirbnb" role="dialog" aria-modal="true" aria-label="Selecionar datas de check-in e checkout" onclick="event.stopPropagation()" class="hidden fixed inset-x-3 top-4 bottom-4 z-[70] overflow-y-auto overscroll-contain p-4 sm:inset-auto sm:left-1/2 sm:top-1/2 sm:w-[min(660px,calc(100vw-2rem))] sm:max-h-[calc(100vh-2rem)] sm:-translate-x-1/2 sm:-translate-y-1/2 sm:p-6 rounded-3xl bg-slate-950 border border-slate-700/80 shadow-2xl transition">
                  
                  <!-- CABEÇALHO DO CALENDÁRIO COM MINI-BOX DE DATAS (ESTILO AIRBNB OFICIAL) -->
                  <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 mb-3 border-b border-slate-800">
                    <div>
                      <h3 class="text-sm sm:text-base font-extrabold text-white" data-i18n="cal_titulo">Selecionar datas</h3>
                      <p class="text-[11px] text-slate-400 mt-0.5" data-i18n="cal_subtitulo">Adicione suas datas de viagem para ver os preços exatos</p>
                    </div>
                    
                    <div class="flex items-center rounded-xl border border-slate-700 bg-slate-900/90 divide-x divide-slate-700 text-left text-xs self-start sm:self-auto">
                      <button type="button" id="calMiniBoxIn" class="px-3 py-1.5 min-w-[105px] rounded-l-xl transition border-2 border-emerald-500 bg-emerald-500/10 cursor-pointer text-left" onclick="clicarBoxCheckIn()" aria-label="Alterar data de check-in">
                        <span class="block text-[9px] font-black tracking-wider text-slate-400 uppercase" data-i18n="lbl_checkin">CHECK-IN</span>
                        <span id="calMiniCheckIn" class="block text-xs font-bold text-white mt-0.5">DD/MM/AAAA</span>
                      </button>
                      <button type="button" id="calMiniBoxOut" class="px-3 py-1.5 min-w-[105px] rounded-r-xl transition border-2 border-transparent cursor-pointer text-left" onclick="clicarBoxCheckOut()" aria-label="Alterar data de checkout">
                        <span class="block text-[9px] font-black tracking-wider text-slate-400 uppercase" data-i18n="lbl_checkout">CHECKOUT</span>
                        <span id="calMiniCheckOut" class="block text-xs font-bold text-slate-400 mt-0.5" data-i18n="txt_inserir_data">Adicionar data</span>
                      </button>
                    </div>
                  </div>

                  <!-- CONTAINER DOS MESES: 1 MÊS NO MOBILE, 2 MESES LADO A LADO EM SM+ -->
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-5" onmouseleave="limparHover()">
                    
                    <!-- MÊS 1 -->
                    <div class="space-y-2">
                      <div class="flex items-center justify-between px-1 h-8">
                        <button type="button" id="calBtnPrevMes" onclick="mudarMes(-1)" class="w-8 h-8 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center font-bold text-base transition shadow-sm" aria-label="Mês anterior">‹</button>
                        <span id="calMesAno1" class="text-xs sm:text-sm font-black text-white capitalize"></span>
                        <div class="w-8 h-8 sm:hidden flex items-center justify-center">
                          <button type="button" onclick="mudarMes(1)" class="w-8 h-8 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center font-bold text-base transition shadow-sm" aria-label="Próximo mês">›</button>
                        </div>
                        <div class="w-8 hidden sm:block"></div>
                      </div>
                      <div id="calDiasSemana1" class="grid grid-cols-7 gap-1 text-center text-[10px] font-bold text-slate-400 uppercase"></div>
                      <div id="calDiasGrid1" class="grid grid-cols-7 gap-1 text-center text-xs font-semibold"></div>
                    </div>

                    <!-- MÊS 2 -->
                    <div class="hidden sm:block space-y-2">
                      <div class="flex items-center justify-between px-1 h-8">
                        <div class="w-8"></div>
                        <span id="calMesAno2" class="text-xs sm:text-sm font-black text-white capitalize"></span>
                        <button type="button" onclick="mudarMes(1)" class="w-8 h-8 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center font-bold text-base transition shadow-sm" aria-label="Próximo mês">›</button>
                      </div>
                      <div id="calDiasSemana2" class="grid grid-cols-7 gap-1 text-center text-[10px] font-bold text-slate-400 uppercase"></div>
                      <div id="calDiasGrid2" class="grid grid-cols-7 gap-1 text-center text-xs font-semibold"></div>
                    </div>

                  </div>

                  <!-- RODAPÉ DO CALENDÁRIO: RESUMO, LIMPAR DATAS E BOTÃO FECHAR -->
                  <div class="mt-4 pt-3 border-t border-slate-800 flex items-center justify-between text-xs">
                    <div class="flex items-center gap-2">
                      <span class="text-slate-400 text-xs">⌨️</span>
                      <span id="calResumoNoites" class="text-slate-300 font-medium text-[11px]" data-i18n="txt_sem_datas">Nenhuma data selecionada</span>
                    </div>
                    <div class="flex items-center gap-3">
                      <button type="button" onclick="limparDatas()" class="text-[11px] font-bold text-slate-400 hover:text-white underline transition" data-i18n="btn_limpar_datas">
                        Limpar datas
                      </button>
                      <button type="button" onclick="fecharCalendario()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs transition shadow-md" data-i18n="cal_btn_fechar">
                        Fechar
                      </button>
                    </div>
                  </div>

                </div>

                <!-- BOTÃO DE AÇÃO PRINCIPAL AIRBNB -->
                <button id="btnConsultar" type="submit" class="w-full mt-4 bg-emerald-500 hover:bg-emerald-400 active:scale-[0.99] text-slate-950 font-black py-3.5 px-4 rounded-xl text-xs sm:text-sm uppercase tracking-wider transition-all duration-200 shadow-xl shadow-emerald-500/20 flex items-center justify-center gap-2">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="m21 21-4.35-4.35m2.1-5.4a7.5 7.5 0 1 1-15 0 7.5 7.5 0 0 1 15 0Z"/></svg>
                  <span id="btnConsultarTexto" data-i18n="btn_conferir_disp">Conferir disponibilidade</span>
                </button>

                <!-- FRASE CLÁSSICA DO AIRBNB -->
                <p class="text-center text-[11px] sm:text-xs text-slate-400 mt-2.5 font-medium" data-i18n="txt_nao_cobrado">
                  Você ainda não será cobrado
                </p>

              </form>

              <!-- RESULTADO DA COTAÇÃO & DETALHAMENTO DE PREÇO (VALOR CONSOLIDADO SEM TAXAS EXTRAS) -->
              <div id="resultadoCotacao" class="hidden mt-4 pt-4 border-t border-slate-800" aria-live="polite"></div>

              <!-- DIFERENCIAIS DA RESERVA DIRETA NO CARD -->
              <div class="mt-5 pt-4 border-t border-slate-800/80 space-y-2 text-xs text-slate-400">
                <div class="flex items-center justify-between">
                  <span class="flex items-center gap-1.5">
                    <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                    <span data-i18n="vantagem_zero_taxas">Sem taxas de serviço de terceiros</span>
                  </span>
                  <span class="text-slate-300" data-i18n="txt_economia_real">Sem surpresas</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="flex items-center gap-1.5">
                    <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                    <span data-i18n="vantagem_tempo_real">Disponibilidade em tempo real</span>
                  </span>
                  <span class="text-slate-300">24h</span>
                </div>
              </div>

            </div>
          </div>
        </div>

      </div>

      <!-- FAIXA DE DIFERENCIAIS RÁPIDOS -->
      <div class="mt-14 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3 max-w-7xl mx-auto">
        
        <div class="glass-card p-3.5 rounded-xl text-center space-y-1">
          <div class="text-xl">⚡</div>
          <h4 class="text-xs font-bold text-white" data-i18n="diff_wifi_tit">Wi-Fi 600 Mbps</h4>
          <p class="text-[11px] text-slate-400" data-i18n="diff_wifi_sub">Fibra óptica dedicada ultra-rápida</p>
        </div>

        <div class="glass-card p-3.5 rounded-xl text-center space-y-1">
          <div class="text-xl">🔑</div>
          <h4 class="text-xs font-bold text-white" data-i18n="diff_checkin_tit">Self Check-in 24h</h4>
          <p class="text-[11px] text-slate-400" data-i18n="diff_checkin_sub">Fechadura eletrônica por código individual</p>
        </div>

        <div class="glass-card p-3.5 rounded-xl text-center space-y-1">
          <div class="text-xl">✈️</div>
          <h4 class="text-xs font-bold text-white" data-i18n="diff_gru_tit">~20 min de GRU</h4>
          <p class="text-[11px] text-slate-400" data-i18n="diff_gru_sub">12 a 14 km de carro até os terminais</p>
        </div>

        <div class="glass-card p-3.5 rounded-xl text-center space-y-1">
          <div class="text-xl">🍳</div>
          <h4 class="text-xs font-bold text-white" data-i18n="diff_cozinha_tit">Cozinha Equipada</h4>
          <p class="text-[11px] text-slate-400" data-i18n="diff_cozinha_sub">Geladeira, micro-ondas & cafeteira</p>
        </div>

        <div class="glass-card p-3.5 rounded-xl text-center space-y-1 col-span-2 sm:col-span-1">
          <div class="text-xl">🛡️</div>
          <h4 class="text-xs font-bold text-white" data-i18n="diff_desconto_tit">Reserva Direta</h4>
          <p class="text-[11px] text-slate-400" data-i18n="diff_desconto_sub">WhatsApp oficial, Pix ou cartão</p>
        </div>

      </div>

    </div>
  </section>

  <!-- SEÇÃO DE STUDIOS (ACOMODAÇÕES COM NOMES COMERCIAIS) -->
  <section id="studios" class="py-20 bg-slate-900/40 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-12 space-y-3">
        <h2 class="text-xs font-bold uppercase tracking-wider text-emerald-400" data-i18n="sec_studios_tag">Nossas Acomodações</h2>
        <p class="text-3xl sm:text-4xl font-extrabold text-white" data-i18n="sec_studios_tit">Conheça nossas opções privativas</p>
        <p class="text-slate-400 text-sm" data-i18n="sec_studios_sub">Os quatro studios têm os mesmos itens — muda só o tamanho: fechadura eletrônica com senha da estadia, Wi-Fi fibra de 600 Mbps, Smart TV, ar-condicionado split, cozinha compacta e banheiro privativo.</p>
      </div>

      <!-- FILTRO DE CATEGORIA -->
      <div class="flex items-center justify-center gap-2 mb-10">
        <button onclick="filtrarStudios('todos')" id="btnFiltroTodos" class="px-4 py-2 rounded-xl text-xs font-bold bg-emerald-500 text-slate-950 transition" data-i18n="btn_filtro_todos">Todos os Studios</button>
        <button onclick="filtrarStudios('amplos')" id="btnFiltroAmplos" class="px-4 py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:text-white transition" data-i18n="btn_filtro_amplos">Studios Amplos</button>
        <button onclick="filtrarStudios('compactos')" id="btnFiltroCompactos" class="px-4 py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:text-white transition" data-i18n="btn_filtro_compactos">Studios Compactos</button>
      </div>

      <!-- GRID DOS STUDIOS COM NOMES COMERCIAIS -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

        <!-- STUDIO MASTER KING -->
        <div class="card-studio glass-card rounded-2xl overflow-hidden flex flex-col group hover:border-emerald-500/40 transition duration-300" data-tipo="amplos">
          <div class="relative h-60 overflow-hidden bg-slate-950">
            <img src="assets/fotos/20251030_162521(1).webp" alt="Studio Amplo A" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-105 transition duration-500 cursor-pointer" onclick="abrirGaleria('master')">
            <div class="absolute top-3 left-3 flex flex-col gap-1.5">
              <span class="bg-amber-400 text-slate-950 text-[10px] font-black px-2.5 py-0.5 rounded shadow" data-i18n="badge_maior_studio">AMPLO</span>
              <span class="bg-slate-950/80 backdrop-blur text-emerald-400 text-[10px] font-bold px-2 py-0.5 rounded border border-slate-700">Amplo A</span>
            </div>
            <button onclick="abrirGaleria('master')" class="absolute bottom-3 right-3 bg-slate-950/80 hover:bg-emerald-500 hover:text-slate-950 backdrop-blur text-slate-200 text-[11px] font-bold px-2.5 py-1 rounded-lg border border-slate-700 transition flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              <span data-i18n="btn_ver_fotos">Ver Fotos</span>
            </button>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h3 class="font-extrabold text-lg text-white">Studio Amplo A</h3>
              </div>
              <p class="text-xs text-slate-400" data-i18n="card_master_desc">Um dos dois studios maiores: mais espaço para circular e para a bagagem.</p>
              
              <div class="my-3 p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/20 text-[11px] text-emerald-300 font-medium" data-i18n="card_master_esp">📐 Mesmos itens de todos os studios, com mais área livre.</div>

              <ul class="space-y-1.5 text-xs text-slate-300">
                <li class="flex items-center gap-2">✓ <span data-i18n="item_cama_queen">Cama queen com enxoval</span></li>
                <li class="flex items-center gap-2">✓ <span data-i18n="item_home_office">Bancada de trabalho & Wi-Fi 600 Mbps</span></li>
                <li class="flex items-center gap-2">✓ <span data-i18n="item_cozinha_cooktop">Cozinha: geladeira, micro-ondas, cooktop e cafeteira</span></li>
                <li class="flex items-center gap-2">✓ <span data-i18n="item_fechadura_tv">Smart TV, ar-condicionado & fechadura eletrônica</span></li>
              </ul>
            </div>
            
            <div class="pt-2 flex flex-col gap-2">
              <button type="button" onclick="focarCotador()" class="w-full text-center py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-extrabold transition shadow-md shadow-emerald-500/20" data-i18n="btn_verificar_datas">
                Verificar Datas & Disponibilidade
              </button>
            </div>
          </div>
        </div>

        <!-- STUDIO EXECUTIVO PREMIUM -->
        <div class="card-studio glass-card rounded-2xl overflow-hidden flex flex-col group hover:border-emerald-500/40 transition duration-300" data-tipo="amplos">
          <div class="relative h-60 overflow-hidden bg-slate-950">
            <img src="assets/fotos/20251030_164004.webp" alt="Studio Amplo B" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-105 transition duration-500 cursor-pointer" onclick="abrirGaleria('executivo')">
            <div class="absolute top-3 left-3 flex flex-col gap-1.5">
              <span class="bg-teal-400 text-slate-950 text-[10px] font-black px-2.5 py-0.5 rounded shadow" data-i18n="badge_executivo">AMPLO</span>
              <span class="bg-slate-950/80 backdrop-blur text-emerald-400 text-[10px] font-bold px-2 py-0.5 rounded border border-slate-700">Amplo B</span>
            </div>
            <button onclick="abrirGaleria('executivo')" class="absolute bottom-3 right-3 bg-slate-950/80 hover:bg-emerald-500 hover:text-slate-950 backdrop-blur text-slate-200 text-[11px] font-bold px-2.5 py-1 rounded-lg border border-slate-700 transition flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              <span data-i18n="btn_ver_fotos">Ver Fotos</span>
            </button>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h3 class="font-extrabold text-lg text-white">Studio Amplo B</h3>
              </div>
              <p class="text-xs text-slate-400" data-i18n="card_executivo_desc">Um dos dois studios maiores: bom para estadias longas e a trabalho.</p>
              
              <div class="my-3 p-2.5 rounded-lg bg-teal-500/10 border border-teal-500/20 text-[11px] text-teal-300 font-medium" data-i18n="card_executivo_esp">📐 Mesmos itens de todos os studios, com mais área livre.</div>

              <ul class="space-y-1.5 text-xs text-slate-300">
                <li class="flex items-center gap-2">✓ <span data-i18n="item_cama_casal_premium">Cama queen com enxoval</span></li>
                <li class="flex items-center gap-2">✓ <span data-i18n="item_home_office">Bancada de trabalho & Wi-Fi 600 Mbps</span></li>
                <li class="flex items-center gap-2">✓ <span data-i18n="item_cozinha_cafeteira">Cozinha: geladeira, micro-ondas, cooktop e cafeteira</span></li>
                <li class="flex items-center gap-2">✓ <span data-i18n="item_fechadura_tv">Smart TV, ar-condicionado & fechadura eletrônica</span></li>
              </ul>
            </div>
            
            <div class="pt-2 flex flex-col gap-2">
              <button type="button" onclick="focarCotador()" class="w-full text-center py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-extrabold transition shadow-md shadow-emerald-500/20" data-i18n="btn_verificar_datas">
                Verificar Datas & Disponibilidade
              </button>
            </div>
          </div>
        </div>

        <!-- STUDIO STANDARD SMART -->
        <div class="card-studio glass-card rounded-2xl overflow-hidden flex flex-col group hover:border-emerald-500/40 transition duration-300" data-tipo="compactos">
          <div class="relative h-60 overflow-hidden bg-slate-950">
            <img src="assets/fotos/20251030_143554.webp" alt="Studio Compacto A" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-105 transition duration-500 cursor-pointer" onclick="abrirGaleria('smart')">
            <div class="absolute top-3 left-3 flex flex-col gap-1.5">
              <span class="bg-slate-800 text-slate-200 text-[10px] font-bold px-2.5 py-0.5 rounded shadow border border-slate-700" data-i18n="badge_smart">COMPACTO</span>
              <span class="bg-slate-950/80 backdrop-blur text-emerald-400 text-[10px] font-bold px-2 py-0.5 rounded border border-slate-700">Compacto A</span>
            </div>
            <button onclick="abrirGaleria('smart')" class="absolute bottom-3 right-3 bg-slate-950/80 hover:bg-emerald-500 hover:text-slate-950 backdrop-blur text-slate-200 text-[11px] font-bold px-2.5 py-1 rounded-lg border border-slate-700 transition flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              <span data-i18n="btn_ver_fotos">Ver Fotos</span>
            </button>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h3 class="font-extrabold text-lg text-white">Studio Compacto A</h3>
              </div>
              <p class="text-xs text-slate-400" data-i18n="card_smart_desc">Um dos dois studios compactos: prático para escalas e estadias curtas.</p>
              
              <div class="my-3 p-2.5 rounded-lg bg-slate-800/80 border border-slate-700 text-[11px] text-slate-300 font-medium" data-i18n="card_smart_esp">📐 Mesmos itens de todos os studios, numa planta compacta.</div>

              <ul class="space-y-1.5 text-xs text-slate-300">
                <li class="flex items-center gap-2">✓ <span data-i18n="item_cama_casal">Cama queen com enxoval</span></li>
                <li class="flex items-center gap-2">✓ <span data-i18n="item_frigobar_micro">Cozinha: geladeira, micro-ondas, cooktop e cafeteira</span></li>
                <li class="flex items-center gap-2">✓ <span data-i18n="item_wifi_tv">Wi-Fi 600 Mbps & Smart TV</span></li>
                <li class="flex items-center gap-2">✓ <span data-i18n="item_fechadura_24h">Ar-condicionado & fechadura eletrônica</span></li>
              </ul>
            </div>
            
            <div class="pt-2 flex flex-col gap-2">
              <button type="button" onclick="focarCotador()" class="w-full text-center py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-extrabold transition shadow-md shadow-emerald-500/20" data-i18n="btn_verificar_datas">
                Verificar Datas & Disponibilidade
              </button>
            </div>
          </div>
        </div>

        <!-- STUDIO STANDARD COZY -->
        <div class="card-studio glass-card rounded-2xl overflow-hidden flex flex-col group hover:border-emerald-500/40 transition duration-300" data-tipo="compactos">
          <div class="relative h-60 overflow-hidden bg-slate-950">
            <img src="assets/fotos/20251030_144024.webp" alt="Studio Compacto B" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-105 transition duration-500 cursor-pointer" onclick="abrirGaleria('cozy')">
            <div class="absolute top-3 left-3 flex flex-col gap-1.5">
              <span class="bg-slate-800 text-slate-200 text-[10px] font-bold px-2.5 py-0.5 rounded shadow border border-slate-700" data-i18n="badge_cozy">COMPACTO</span>
              <span class="bg-slate-950/80 backdrop-blur text-emerald-400 text-[10px] font-bold px-2 py-0.5 rounded border border-slate-700">Compacto B</span>
            </div>
            <button onclick="abrirGaleria('cozy')" class="absolute bottom-3 right-3 bg-slate-950/80 hover:bg-emerald-500 hover:text-slate-950 backdrop-blur text-slate-200 text-[11px] font-bold px-2.5 py-1 rounded-lg border border-slate-700 transition flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              <span data-i18n="btn_ver_fotos">Ver Fotos</span>
            </button>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h3 class="font-extrabold text-lg text-white">Studio Compacto B</h3>
              </div>
              <p class="text-xs text-slate-400" data-i18n="card_cozy_desc">Um dos dois studios compactos: tudo o que os maiores têm, com melhor custo-benefício.</p>
              
              <div class="my-3 p-2.5 rounded-lg bg-slate-800/80 border border-slate-700 text-[11px] text-slate-300 font-medium" data-i18n="card_cozy_esp">📐 Mesmos itens de todos os studios, numa planta compacta.</div>

              <ul class="space-y-1.5 text-xs text-slate-300">
                <li class="flex items-center gap-2">✓ <span data-i18n="item_cama_casal_travesseiro">Cama queen com enxoval</span></li>
                <li class="flex items-center gap-2">✓ <span data-i18n="item_ducha_press">Banheiro privativo com ducha e secador</span></li>
                <li class="flex items-center gap-2">✓ <span data-i18n="item_frigobar_cafe">Cozinha: geladeira, micro-ondas, cooktop e cafeteira</span></li>
                <li class="flex items-center gap-2">✓ <span data-i18n="item_wifi_tv">Wi-Fi 600 Mbps & Smart TV</span></li>
              </ul>
            </div>
            
            <div class="pt-2 flex flex-col gap-2">
              <button type="button" onclick="focarCotador()" class="w-full text-center py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-extrabold transition shadow-md shadow-emerald-500/20" data-i18n="btn_verificar_datas">
                Verificar Datas & Disponibilidade
              </button>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- TABELA COMPARATIVA: RESERVA DIRETA VS AIRBNB/BOOKING -->
  <section class="py-16 border-t border-slate-800 bg-[#090d16]">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-2xl mx-auto mb-10 space-y-2">
        <h2 class="text-xs font-bold uppercase tracking-wider text-emerald-400" data-i18n="comp_tag">Transparência Total</h2>
        <p class="text-2xl sm:text-3xl font-extrabold text-white" data-i18n="comp_tit">Por que reservar direto conosco pelo WhatsApp?</p>
      </div>

      <div class="overflow-x-auto glass-card rounded-2xl border border-slate-800 shadow-xl">
        <table class="w-full text-left text-xs sm:text-sm">
          <thead>
            <tr class="border-b border-slate-800 text-slate-400 bg-slate-900/60 text-[11px] uppercase tracking-wider">
              <th class="p-4 sm:p-5" data-i18n="th_beneficio">Benefício</th>
              <th class="p-4 sm:p-5 text-emerald-400 font-extrabold bg-emerald-500/5" data-i18n="th_direto">SNT Studios (Direto Oficial)</th>
              <th class="p-4 sm:p-5 text-slate-400" data-i18n="th_plataformas">Plataformas (Booking / Airbnb)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/60 text-slate-300">
            <tr>
              <td class="p-4 sm:p-5 font-semibold text-white" data-i18n="td_atendimento">Atendimento & Suporte</td>
              <td class="p-4 sm:p-5 font-bold text-emerald-400 bg-emerald-500/5" data-i18n="td_atend_direto">WhatsApp direto com nossa equipe local</td>
              <td class="p-4 sm:p-5 text-slate-400" data-i18n="td_atend_plat">Chat do app com intermediários e bots genéricos</td>
            </tr>
            <tr>
              <td class="p-4 sm:p-5 font-semibold text-white" data-i18n="td_pagamento">Formas de Pagamento</td>
              <td class="p-4 sm:p-5 font-bold text-emerald-400 bg-emerald-500/5" data-i18n="td_pag_direto">PIX ou Cartão combinado direto e com segurança</td>
              <td class="p-4 sm:p-5 text-slate-400" data-i18n="td_pag_plat">Pagamento pelas regras de cada plataforma</td>
            </tr>
            <tr>
              <td class="p-4 sm:p-5 font-semibold text-white" data-i18n="td_flexibilidade">Flexibilidade de Horários</td>
              <td class="p-4 sm:p-5 font-bold text-emerald-400 bg-emerald-500/5" data-i18n="td_flex_direto">Possibilidade de Early Check-in sob consulta direta</td>
              <td class="p-4 sm:p-5 text-slate-400" data-i18n="td_flex_plat">Regras automáticas sem contato direto</td>
            </tr>
          </tbody>
        </table>
      </div>

    </div>
  </section>

  <!-- COMODIDADES COMPLETAS -->
  <section id="comodidades" class="py-20 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-3">
        <h2 class="text-xs font-bold uppercase tracking-wider text-emerald-400" data-i18n="sec_infra_tag">Infraestrutura Completa</h2>
        <p class="text-3xl font-extrabold text-white" data-i18n="sec_infra_tit">Tudo o que você precisa para uma estadia impecável</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <div class="glass-card p-6 rounded-2xl space-y-3">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-xl font-bold">⚡</div>
          <h3 class="text-base font-bold text-white" data-i18n="infra_wifi_tit">Internet Fibra 600 Mbps</h3>
          <p class="text-xs text-slate-400 leading-relaxed" data-i18n="infra_wifi_desc">
            Conexão dedicada de ultra-alta velocidade com roteador potente. Perfeito para chamadas de vídeo, reuniões executivas e streaming em 4K sem qualquer oscilação.
          </p>
        </div>

        <div class="glass-card p-6 rounded-2xl space-y-3">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-xl font-bold">🔑</div>
          <h3 class="text-base font-bold text-white" data-i18n="infra_checkin_tit">Acesso Eletrônico 24h</h3>
          <p class="text-xs text-slate-400 leading-relaxed" data-i18n="infra_checkin_desc">O portão abre por QR code e a porta do studio por uma senha exclusiva da sua estadia. As instruções chegam automaticamente minutos depois de você preencher o formulário de check-in online — dá para chegar a qualquer hora, sem recepção.</p>
        </div>

        <div class="glass-card p-6 rounded-2xl space-y-3">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-xl font-bold">🍳</div>
          <h3 class="text-base font-bold text-white" data-i18n="infra_cozinha_tit">Cozinha Compacta Privativa</h3>
          <p class="text-xs text-slate-400 leading-relaxed" data-i18n="infra_cozinha_desc">Geladeira com freezer, micro-ondas, cooktop, cafeteira elétrica, sanduicheira, panelas, louças e talheres. Prepare suas refeições com praticidade.</p>
        </div>

        <div class="glass-card p-6 rounded-2xl space-y-3">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-xl font-bold">🚿</div>
          <h3 class="text-base font-bold text-white" data-i18n="infra_ducha_tit">Banheiro Privativo</h3>
          <p class="text-xs text-slate-400 leading-relaxed" data-i18n="infra_ducha_desc">Box de vidro, ducha quente, bidê, secador de cabelo e toalhas para a estadia.</p>
        </div>

        <div class="glass-card p-6 rounded-2xl space-y-3">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-xl font-bold">🧺</div>
          <h3 class="text-base font-bold text-white" data-i18n="infra_lav_tit">SNT Lavanderia no prédio</h3>
          <p class="text-xs text-slate-400 leading-relaxed" data-i18n="infra_lav_desc">A SNT Lavanderia Self-Service funciona no andar de baixo, 24 horas, para lavar e secar suas roupas. É um serviço à parte, pago direto no totem.</p>
        </div>

        <div class="glass-card p-6 rounded-2xl space-y-3">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-xl font-bold">🛡️</div>
          <h3 class="text-base font-bold text-white" data-i18n="infra_seg_tit">Segurança & Monitoramento</h3>
          <p class="text-xs text-slate-400 leading-relaxed" data-i18n="infra_seg_desc">
            Circuito interno de câmeras nas áreas comuns e iluminação inteligente para garantir a máxima tranquilidade para você e suas bagagens.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- LOCALIZAÇÃO COM GOOGLE MAPS PIN EXATO -->
  <section id="localizacao" class="py-20 border-t border-slate-800 bg-[#090d16]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        
        <div class="lg:col-span-6 space-y-6">
          <span class="text-xs font-bold uppercase tracking-wider text-emerald-400" data-i18n="loc_tag">Localização Privilegiada</span>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-white leading-tight" data-i18n="loc_tit">
            Perto de tudo em Guarulhos e na Grande São Paulo
          </h2>
          <p class="text-sm text-slate-300 leading-relaxed" data-i18n="loc_desc">No bairro Cidade Seródio, em Guarulhos, com acesso de carro ou aplicativo aos terminais do Aeroporto Internacional de Guarulhos (GRU), à Rodovia Presidente Dutra e à Rodovia Ayrton Senna.</p>

          <!-- ENDEREÇO OFICIAL COM BOTÃO DE COPIAR -->
          <div class="p-4 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
              <span class="text-emerald-400 text-xl">📍</span>
              <div>
                <span class="text-[11px] text-slate-400 font-bold uppercase tracking-wider block" data-i18n="loc_endereco_oficial">Endereço Oficial</span>
                <span class="text-xs sm:text-sm font-bold text-white">Avenida Aguanil, 51 - Cidade Seródio - Guarulhos/SP</span>
              </div>
            </div>
            <button onclick="copiarEndereco()" id="btnCopiarEnd" class="shrink-0 px-3 py-2 rounded-lg bg-slate-800 hover:bg-emerald-500 hover:text-slate-950 text-slate-300 text-xs font-bold transition">
              Copiar
            </button>
          </div>

          <!-- BOTÕES DE ROTAS (GOOGLE MAPS & WAZE) -->
          <div class="flex flex-wrap gap-3">
            <a href="https://www.google.com/maps/search/?api=1&query=Avenida+Aguanil,+51+-+Cidade+Ser%C3%B3dio,+Guarulhos+-+SP" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-white font-bold px-4 py-2.5 rounded-xl text-xs border border-slate-700 transition">
              <svg class="w-4 h-4 text-emerald-400" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
              <span>Google Maps</span>
            </a>
            <a href="https://waze.com/ul?q=Avenida+Aguanil+51+Guarulhos+SP" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-white font-bold px-4 py-2.5 rounded-xl text-xs border border-slate-700 transition">
              <svg class="w-4 h-4 text-sky-400" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 1010 10A10 10 0 0012 2zm1 14.5a1.5 1.5 0 111.5-1.5 1.5 1.5 0 01-1.5 1.5zm-3-4a1 1 0 111-1 1 1 0 01-1 1zm4 0a1 1 0 111-1 1 1 0 01-1 1z"/></svg>
              <span>Waze</span>
            </a>
          </div>

          <!-- DISTÂNCIAS PRINCIPAIS -->
          <div class="grid grid-cols-2 gap-3 pt-2">
            <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800">
              <span class="text-xs text-slate-400 block" data-i18n="dist_gru_tit">Aeroporto GRU</span>
              <span class="text-sm font-bold text-emerald-400" data-i18n="dist_gru_val">21-22 min de carro</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800">
              <span class="text-xs text-slate-400 block" data-i18n="dist_cptm_tit">Estação Aeroporto-Guarulhos (CPTM)</span>
              <span class="text-sm font-bold text-white" data-i18n="dist_cptm_val">20 min de carro</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800">
              <span class="text-xs text-slate-400 block" data-i18n="dist_comercio_tit">Comércio & Padaria</span>
              <span class="text-sm font-bold text-white" data-i18n="dist_comercio_val">Logo ao lado</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800">
              <span class="text-xs text-slate-400 block" data-i18n="dist_shopping_tit">Shopping Bosque Maia</span>
              <span class="text-sm font-bold text-white" data-i18n="dist_shopping_val">18 minutos</span>
            </div>
          </div>
        </div>

        <!-- GOOGLE MAPS EMBED OFICIAL COM PIN -->
        <div class="lg:col-span-6 h-[400px] rounded-2xl overflow-hidden border border-slate-800 shadow-2xl relative">
          <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3661.1273934371465!2d-46.46747202391039!3d-23.42065845648834!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce8b9a1ebc86ad%3A0x6b631d8ce4a7e780!2sAv.%20Aguanil%2C%2051%20-%20Cidade%20Ser%C3%B3dio%2C%20Guarulhos%20-%20SP%2C%2007150-060!5e0!3m2!1spt-BR!2sbr!4v1700000000000!5m2!1spt-BR!2sbr" 
            width="100%" 
            height="100%" 
            style="border:0; filter: invert(90%) hue-rotate(180deg);" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade"
            title="Localização SNT Studios no Google Maps">
          </iframe>
        </div>

      </div>

    </div>
  </section>

  <!-- PERGUNTAS FREQUENTES (FAQ) -->
  <section id="faq" class="py-20 border-t border-slate-800">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center mb-14 space-y-2">
        <h2 class="text-xs font-bold uppercase tracking-wider text-emerald-400" data-i18n="faq_tag">Tire Suas Dúvidas</h2>
        <p class="text-3xl font-extrabold text-white" data-i18n="faq_tit">Perguntas Frequentes</p>
      </div>

      <div class="space-y-4">
        
        <details class="glass-card rounded-xl p-5 group cursor-pointer">
          <summary class="font-bold text-sm sm:text-base text-white flex items-center justify-between">
            <span data-i18n="faq_q1">Como funciona o check-in se meu voo chegar de madrugada?</span>
            <span class="text-emerald-400 transition group-open:rotate-180">▼</span>
          </summary>
          <p class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed" data-i18n="faq_a1">Tranquilo: o portão abre por QR code e a porta do studio por uma senha só sua, então você entra sozinho a qualquer hora a partir das 15h, inclusive de madrugada. As instruções chegam uns 5 minutos depois que você preenche o formulário de check-in online.</p>
        </details>


        <details class="glass-card rounded-xl p-5 group cursor-pointer">
          <summary class="font-bold text-sm sm:text-base text-white flex items-center justify-between">
            <span data-i18n="faq_q3">Qual a diferença entre os studios?</span>
            <span class="text-emerald-400 transition group-open:rotate-180">▼</span>
          </summary>
          <p class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed" data-i18n="faq_a3">Só o tamanho: dois são maiores e dois mais compactos. Cama queen, cozinha, ar-condicionado, Smart TV, Wi-Fi de 600 Mbps e banheiro privativo são iguais em todos.</p>
        </details>

        <details class="glass-card rounded-xl p-5 group cursor-pointer">
          <summary class="font-bold text-sm sm:text-base text-white flex items-center justify-between">
            <span data-i18n="faq_q4">A internet suporta reuniões em vídeo e trabalho remoto?</span>
            <span class="text-emerald-400 transition group-open:rotate-180">▼</span>
          </summary>
          <p class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed" data-i18n="faq_a4">
            Sim! Temos fibra óptica dedicada de <strong>600 Mbps</strong> com baixa latência e sinal forte em todos os studios. Nossos hóspedes executivos utilizam regularmente para chamadas no Teams, Zoom, Google Meet e streaming.
          </p>
        </details>

        <details class="glass-card rounded-xl p-5 group cursor-pointer">
          <summary class="font-bold text-sm sm:text-base text-white flex items-center justify-between">
            <span data-i18n="faq_q5">Quais as formas de pagamento aceitas para a reserva direta?</span>
            <span class="text-emerald-400 transition group-open:rotate-180">▼</span>
          </summary>
          <p class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed" data-i18n="faq_a5">
            Você pode pagar com total segurança via <strong>PIX</strong> (com confirmação instantânea) ou <strong>Cartão de Crédito</strong>. Todo o fluxo é combinado com clareza e recibo pelo WhatsApp oficial.
          </p>
        </details>

        <details class="glass-card rounded-xl p-5 group cursor-pointer">
          <summary class="font-bold text-sm sm:text-base text-white flex items-center justify-between">
            <span data-i18n="faq_q6">Tem comércio ou alimentação perto do studio?</span>
            <span class="text-emerald-400 transition group-open:rotate-180">▼</span>
          </summary>
          <p class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed" data-i18n="faq_a6">
            Sim! A menos de 2 a 5 minutos a pé você encontra padaria, farmácia, supermercado e restaurantes, além de ampla cobertura de entrega do iFood com entrega rápida na nossa porta.
          </p>
        </details>

      </div>

      <!-- CTA FINAL DA SEÇÃO FAQ -->
      <div class="mt-12 text-center">
        <a href="https://api.whatsapp.com/send?phone=551154443110&text=Ola%21%20Gostaria%20de%20tirar%20uma%20duvida%20sobre%20a%20hospedagem%20no%20SNT%20Studios." target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-3 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-extrabold px-8 py-4 rounded-xl text-sm sm:text-base shadow-xl shadow-emerald-500/25 transition transform hover:-translate-y-0.5">
          <span data-i18n="btn_faq_whatsapp">Ainda tem dúvidas? Fale com a gente no WhatsApp</span>
          <span>→</span>
        </a>
      </div>

    </div>
  </section>

  <!-- FOOTER OFICIAL -->
  <footer id="contato" class="py-12 border-t border-slate-800 bg-[#050810] text-slate-400 text-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-10">
        
        <!-- COLUNA 1: MARCA & IDENTIDADE -->
        <div class="space-y-3 md:col-span-2">
          <div class="flex items-center gap-2.5" aria-label="SNT Studios">
            <svg class="h-11 w-[32px] shrink-0 text-emerald-500" viewBox="240 135 545 755" fill="none" stroke="currentColor" stroke-width="34" aria-hidden="true" focusable="false"><path d="M384.5 458V318L547 171V287L630 345V528"/><path d="M247 869H384.5V520"/><path d="M298 869V566L462 416V881"/><path d="M555 881V510L719 617V869"/><path d="M631 592V869H776"/></svg>
            <span class="flex flex-col leading-none">
              <span class="text-xl font-extrabold tracking-tight text-white">SNT <span class="font-bold text-emerald-400">Studios</span></span>
              <span class="mt-1 text-[10px] font-semibold uppercase tracking-[0.16em] text-slate-400">uma empresa SNT Empreendimentos</span>
            </span>
          </div>
          <p class="text-slate-400 max-w-sm leading-relaxed text-[11px]" data-i18n="footer_desc">
            Hospitalidade inteligente e moderna em Guarulhos. Studios privativos completos para quem valoriza silêncio, conforto, tecnologia e proximidade com o Aeroporto GRU.
          </p>
          <div class="pt-2 text-[11px] text-slate-400 space-y-1">
            <p><strong>Razão Social:</strong> SNT Empreendimentos Imobiliários LTDA</p>
            <p><strong>CNPJ:</strong> 63.223.844/0001-11</p>
            <p><strong>Endereço:</strong> Avenida Aguanil, 51 - Cidade Seródio - Guarulhos/SP - CEP 07150-060</p>
          </div>
        </div>

        <!-- COLUNA 2: LINKS RÁPIDOS -->
        <div class="space-y-2">
          <h4 class="font-bold text-white uppercase tracking-wider text-[11px]" data-i18n="footer_nav_tit">Navegação</h4>
          <ul class="space-y-1.5 text-[11px]">
            <li><a href="#inicio" class="hover:text-emerald-400 transition" data-i18n="nav_inicio">Início & Anúncio</a></li>
            <li><a href="#cotador" class="hover:text-emerald-400 transition" data-i18n="nav_disponibilidade">Verificar Disponibilidade</a></li>
            <li><a href="#studios" class="hover:text-emerald-400 transition" data-i18n="nav_studios">Nossas Acomodações</a></li>
            <li><a href="#comodidades" class="hover:text-emerald-400 transition" data-i18n="nav_comodidades">Comodidades & Wi-Fi</a></li>
            <li><a href="#localizacao" class="hover:text-emerald-400 transition" data-i18n="nav_localizacao">Localização & Rotas GRU</a></li>
            <li><a href="#faq" class="hover:text-emerald-400 transition" data-i18n="nav_faq">Dúvidas Frequentes</a></li>
          </ul>
        </div>

        <!-- COLUNA 3: CONTATO & CANAIS -->
        <div class="space-y-2">
          <h4 class="font-bold text-white uppercase tracking-wider text-[11px]" data-i18n="footer_atend_tit">Atendimento Oficial</h4>
          <p class="text-[11px] text-slate-400" data-i18n="footer_atend_desc">Atendimento humanizado para cotações, reservas e suporte ao hóspede:</p>
          <a href="https://api.whatsapp.com/send?phone=551154443110" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-emerald-400 hover:text-emerald-300 font-bold text-xs py-1">
            <span>WhatsApp: (11) 5444-3110</span>
          </a>
          <p class="text-[11px] text-slate-400" data-i18n="footer_horarios">Check-in: a partir das 15:00<br>Check-out: até as 11:00</p>
        </div>

      </div>

      <div class="pt-8 border-t border-slate-800/80 flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-slate-400">
        <p>© 2026 SNT Studios (SNT Empreendimentos Imobiliários LTDA). Todos os direitos reservados. · <a href="/privacidade.html" class="text-emerald-400 hover:text-emerald-300 underline underline-offset-2">Política de Privacidade</a></p>
        <p class="text-slate-400" data-i18n="footer_sustentavel">Desenvolvido com tecnologia sustentável e zero CDNs externas em produção.</p>
      </div>

    </div>
  </footer>

  <!-- MODAL DE GALERIA DE FOTOS (LIGHTBOX 20 FOTOS WEBP) -->
  <div id="modalGaleria" class="fixed inset-0 z-50 modal-backdrop hidden flex items-center justify-center p-4">
    <div class="relative max-w-4xl w-full bg-slate-900 border border-slate-800 rounded-3xl overflow-hidden shadow-2xl flex flex-col max-h-[90vh]">
      
      <!-- CABEÇALHO DO MODAL -->
      <div class="p-4 border-b border-slate-800 flex items-center justify-between">
        <div>
          <h3 id="modalGaleriaTitulo" class="font-bold text-white text-sm sm:text-base">Fotos Reais do SNT Studios</h3>
          <p id="modalGaleriaSubtitulo" class="text-xs text-slate-400">Fotos 100% autênticas das nossas acomodações</p>
        </div>
        <button onclick="fecharGaleria()" class="w-9 h-9 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-200 flex items-center justify-center font-bold text-lg transition">
          ✕
        </button>
      </div>

      <!-- VISUALIZADOR DA FOTO ATUAL -->
      <div class="relative flex-1 bg-black flex items-center justify-center min-h-[300px] sm:min-h-[460px] overflow-hidden">
        <img id="modalFotoPrincipal" src="" alt="Foto da Acomodação" class="max-h-[70vh] w-auto max-w-full object-contain">
        
        <!-- BOTOES DE NAVEGAÇÃO -->
        <button onclick="anteriorFotoGaleria()" class="absolute left-3 top-1/2 -translate-y-1/2 w-11 h-11 rounded-full bg-slate-950/80 hover:bg-emerald-500 hover:text-slate-950 text-white flex items-center justify-center font-black text-xl transition border border-slate-800 shadow-xl">
          ‹
        </button>
        <button onclick="proximaFotoGaleria()" class="absolute right-3 top-1/2 -translate-y-1/2 w-11 h-11 rounded-full bg-slate-950/80 hover:bg-emerald-500 hover:text-slate-950 text-white flex items-center justify-center font-black text-xl transition border border-slate-800 shadow-xl">
          ›
        </button>

        <!-- CONTADOR DE FOTOS -->
        <div id="modalContadorFoto" class="absolute bottom-3 left-1/2 -translate-x-1/2 bg-slate-950/85 backdrop-blur px-3 py-1 rounded-full text-xs font-bold text-slate-200 border border-slate-800">
          1 / 20
        </div>
      </div>

      <!-- MINIATURAS INFERIORES -->
      <div id="modalMiniaturas" class="p-3 bg-slate-950 border-t border-slate-800 flex gap-2 overflow-x-auto">
        <!-- Renderizado dinamicamente via JS -->
      </div>

    </div>
  </div>

  <!-- BARRA FIXA MOBILE ESTILO AIRBNB (DOCKADA NA PARTE INFERIOR EM TELAS PEQUENAS) -->
  <div id="airbnbMobileBar" class="lg:hidden fixed bottom-0 left-0 right-0 z-40 bg-slate-950/95 backdrop-blur-md border-t border-slate-800 px-4 py-3 flex items-center justify-between shadow-2xl transition duration-300">
    <div>
      <div class="flex items-baseline gap-1">
        <span class="text-base font-black text-white" id="mobileBarPreco" data-i18n="card_ver_valor">Ver valor</span>
        <span id="mobilePrecoSufixo" class="hidden text-xs text-slate-400" data-i18n="card_por_noite">/ noite</span>
      </div>
      <div class="text-[11px] text-emerald-400 font-medium" id="mobileBarDatas" data-i18n="txt_inserir_data">Selecione as datas</div>
    </div>
    <button type="button" onclick="focarCotador()" class="bg-emerald-500 hover:bg-emerald-400 active:scale-95 text-slate-950 font-black px-4 py-2.5 rounded-xl text-xs uppercase tracking-wider shadow-lg shadow-emerald-500/25 transition" data-i18n="btn_verificar_datas_curto">
      Verificar Datas
    </button>
  </div>

  <!-- BOTAO FLUTUANTE WHATSAPP (POSICIONADO ACIMA DA BARRA NO MOBILE) -->
  <a href="https://api.whatsapp.com/send?phone=551154443110&text=Ola%21%20Gostaria%20de%20consultar%20uma%20reserva%20direta%20no%20SNT%20Studios." target="_blank" rel="noopener noreferrer" class="fixed bottom-20 lg:bottom-6 right-4 lg:right-6 z-50 flex items-center gap-2.5 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-extrabold p-3.5 sm:px-5 sm:py-3.5 rounded-full shadow-2xl shadow-emerald-500/30 transition transform hover:scale-105" title="Falar no WhatsApp Oficial">
    <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824zm-3.423-14.416c-6.627 0-12 5.373-12 12 0 2.159.57 4.184 1.564 5.938l-1.664 6.086 6.257-1.64c1.706.924 3.659 1.45 5.743 1.45 6.627 0 12-5.373 12-12 0-6.627-5.373-12-12-12z"/></svg>
    <span class="hidden sm:inline text-xs tracking-wide">Falar no WhatsApp</span>
  </a>

  <!-- SCRIPTS FUNCIONAIS: I18N, CALENDÁRIO RANGE AIRBNB E COTAÇÃO -->
  <script>
    // ========================================================
    // INTERNACIONALIZAÇÃO (PT / EN / ES)
    // ========================================================
    let idiomaAtual = localStorage.getItem('snt_studios_lang') || 'pt';

    const I18N = {
      pt: {
        nav_inicio: "Início",
        nav_disponibilidade: "Disponibilidade",
        nav_studios: "Acomodações",
        nav_comodidades: "Comodidades",
        nav_localizacao: "Localização",
        nav_faq: "Dúvidas",
        btn_nav_reserva: "Reservar no WhatsApp",
        badge_topo_local: "Hospedagem Privativa em Guarulhos · Aeroporto GRU",
        badge_topo_desconto: "🛡️ Reserva direta pelo WhatsApp oficial",
        badge_topo_checkin: "🔑 Auto Check-in 24h",
        hero_title: "SNT Studios · Studios Privativos em Guarulhos, perto do Aeroporto GRU",
        sub_hospitalidade: "Hospitalidade Independente",
        sub_gru_dist: "Cerca de 20 minutos de carro dos Terminais 1, 2 e 3",
        btn_compartilhar: "Compartilhar",
        tag_master_king: "STUDIO AMPLO",
        desc_master_king_curta: "Cama queen, bancada de trabalho e cortinas blackout",
        tag_executivo_premium: "Studio Amplo",
        tag_cozinha_priv: "Cozinha Compacta",
        tag_standard_smart: "Studio Compacto",
        tag_standard_cozy: "Studio Compacto",
        btn_todas_fotos: "Mostrar todas as 20 fotos",
        detalhe_tipo_espaco: "Studio privativo inteiro · Hospedagem SNT",
        detalhe_capacidade: "Até 2 hóspedes · 1 cama queen · 1 banheiro privativo · Cozinha compacta equipada",
        feature_checkin_tit: "Auto check-in 24h via fechadura digital",
        feature_checkin_desc: "O portão abre por QR code e a porta do studio por uma senha só sua: chegue a qualquer hora da noite ou madrugada, sem chave física.",
        feature_wifi_tit: "Wi-Fi fibra de 600 Mbps dedicado",
        feature_wifi_desc: "Internet ultra-veloz testada para chamadas de vídeo, reuniões executivas e streaming 4K sem interrupções.",
        feature_cozinha_tit: "Cozinha privativa equipada",
        feature_cozinha_desc: "Geladeira com freezer, micro-ondas, cooktop, cafeteira elétrica, sanduicheira, panelas, louças e talheres.",
        feature_gru_tit: "Cerca de 20 min de carro do Aeroporto de Guarulhos (GRU)",
        feature_gru_desc: "São 12 a 14 km até os terminais, uns 21 a 22 minutos de carro ou aplicativo sem trânsito. A pé não dá: o caminho contorna o aeroporto.",
        sobre_espaco_tit: "Sobre o espaço",
        sobre_espaco_p1: "O SNT Studios oferece uma proposta inteligente de hospitalidade autônoma: privacidade completa, acabamento refinado e excelente localização próxima ao Aeroporto GRU. Todas as acomodações são 100% privativas com banheiro exclusivo, bancada e ambiente climatizado.",
        tipologias_tit: "Dois tamanhos, os mesmos itens",
        cat_ampla_tit: "Studios Amplos (2 unidades)",
        cat_ampla_desc: "Os dois maiores: mais área livre para circular e organizar a bagagem.",
        cat_compacta_tit: "Studios Compactos (2 unidades)",
        cat_compacta_desc: "Os dois menores: a mesma cama queen, cozinha e comodidades, numa planta mais enxuta.",
        tipologias_nota: "Ao selecionar suas datas ao lado, o sistema verifica a disponibilidade em tempo real e calcula o valor total consolidado.",
        comodidades_grid_tit: "O que esse lugar oferece",
        comod_wifi: "Wi-Fi Fibra 600 Mbps",
        comod_fechadura: "Fechadura digital 24h",
        comod_tv: "Smart TV com Streaming",
        comod_cooktop: "Cozinha com Cooktop",
        comod_ar: "Ar-condicionado split e aquecedor",
        comod_cafe: "Cafeteira elétrica",
        comod_ducha: "Ducha quente",
        comod_enxoval: "Enxoval higienizado",
        comod_bancada: "Bancada para notebook",
        comod_cameras: "Câmeras nas áreas comuns",
        comod_transporte: "Fácil acesso para Uber/99",
        comod_frigobar: "Geladeira e micro-ondas",
        regra_checkin_tit: "Check-in:",
        regra_checkin_val: "A partir das 15:00 (Acesso autônomo 24h via código)",
        regra_checkout_tit: "Check-out:",
        regra_checkout_val: "Até as 11:00",
        regra_silencio_tit: "Política de Silêncio:",
        regra_silencio_val: "Respeito ao descanso dos demais hóspedes a partir das 22h",
        card_por_noite: " / noite", card_ver_valor: "Ver valor",
        card_tarifa_oficial: "Tarifa Oficial",
        lbl_checkin: "CHECK-IN",
        lbl_checkout: "CHECKOUT",
        lbl_hospedes: "HÓSPEDES",
        txt_inserir_data: "Adicionar data",
        opt_1_hospede: "1 hóspede",
        opt_2_hospedes: "2 hóspedes (Casal)",
        cal_escolha_checkin: "Selecione a data de check-in",
        cal_escolha_checkout: "Selecione a data de checkout",
        cal_sub_instrucao: "1º clique: entrada · 2º clique: saída",
        cal_titulo: "Selecionar datas",
        cal_subtitulo: "Adicione suas datas de viagem para ver os preços exatos",
        cal_btn_fechar: "Fechar",
        txt_noite_sing: "noite",
        txt_noites_plur: "noites",
        btn_limpar_datas: "Limpar datas",
        dia_dom: "Dom", dia_seg: "Seg", dia_ter: "Ter", dia_qua: "Qua", dia_qui: "Qui", dia_sex: "Sex", dia_sab: "Sáb",
        txt_sem_datas: "Nenhuma data selecionada",
        btn_concluir: "Concluir",
        btn_conferir_disp: "Conferir disponibilidade",
        btn_verificar_datas_curto: "Verificar Datas",
        txt_nao_cobrado: "Você ainda não será cobrado",
        txt_garantido: "Garantido",
        vantagem_zero_taxas: "Sem taxas de serviço de terceiros",
        txt_economia_real: "Sem surpresas",
        vantagem_tempo_real: "Disponibilidade em tempo real",
        diff_wifi_tit: "Wi-Fi 600 Mbps", diff_wifi_sub: "Fibra óptica dedicada ultra-rápida",
        diff_checkin_tit: "Self Check-in 24h", diff_checkin_sub: "Fechadura eletrônica por código individual",
        diff_gru_tit: "~20 min de GRU", diff_gru_sub: "12 a 14 km de carro até os terminais",
        diff_cozinha_tit: "Cozinha Equipada", diff_cozinha_sub: "Geladeira, micro-ondas & cafeteira",
        diff_desconto_tit: "Reserva Direta", diff_desconto_sub: "WhatsApp oficial, Pix ou cartão",
        sec_studios_tag: "Nossas Acomodações", sec_studios_tit: "Conheça nossas opções privativas",
        sec_studios_sub: "Os quatro studios têm os mesmos itens — muda só o tamanho: fechadura eletrônica com senha da estadia, Wi-Fi fibra de 600 Mbps, Smart TV, ar-condicionado split, cozinha compacta e banheiro privativo.",
        btn_filtro_todos: "Todos os Studios", btn_filtro_amplos: "Studios Amplos", btn_filtro_compactos: "Studios Compactos",
        badge_maior_studio: "AMPLO", badge_executivo: "AMPLO", badge_smart: "COMPACTO", badge_cozy: "COMPACTO",
        btn_ver_fotos: "Ver Fotos", btn_verificar_datas: "Verificar Datas & Disponibilidade",
        card_master_desc: "Um dos dois studios maiores: mais espaço para circular e para a bagagem.",
        card_master_esp: "📐 Mesmos itens de todos os studios, com mais área livre.",
        item_cama_queen: "Cama queen com enxoval", item_home_office: "Bancada de trabalho & Wi-Fi 600 Mbps",
        item_cozinha_cooktop: "Cozinha: geladeira, micro-ondas, cooktop e cafeteira", item_fechadura_tv: "Smart TV, ar-condicionado & fechadura eletrônica",
        card_executivo_desc: "Um dos dois studios maiores: bom para estadias longas e a trabalho.",
        card_executivo_esp: "📐 Mesmos itens de todos os studios, com mais área livre.",
        item_cama_casal_premium: "Cama queen com enxoval", item_cozinha_cafeteira: "Cozinha: geladeira, micro-ondas, cooktop e cafeteira",
        card_smart_desc: "Um dos dois studios compactos: prático para escalas e estadias curtas.",
        card_smart_esp: "📐 Mesmos itens de todos os studios, numa planta compacta.",
        item_cama_casal: "Cama queen com enxoval", item_frigobar_micro: "Cozinha: geladeira, micro-ondas, cooktop e cafeteira", item_wifi_tv: "Wi-Fi 600 Mbps & Smart TV", item_fechadura_24h: "Ar-condicionado & fechadura eletrônica",
        card_cozy_desc: "Um dos dois studios compactos: tudo o que os maiores têm, com melhor custo-benefício.",
        card_cozy_esp: "📐 Mesmos itens de todos os studios, numa planta compacta.",
        item_cama_casal_travesseiro: "Cama queen com enxoval", item_ducha_press: "Banheiro privativo com ducha e secador", item_frigobar_cafe: "Cozinha: geladeira, micro-ondas, cooktop e cafeteira",
        comp_tag: "Transparência Total", comp_tit: "Por que reservar direto conosco pelo WhatsApp?",
        th_beneficio: "Benefício", th_direto: "SNT Studios (Direto Oficial)", th_plataformas: "Plataformas (Booking / Airbnb)",
        td_atendimento: "Atendimento & Suporte", td_atend_direto: "WhatsApp direto com nossa equipe local", td_atend_plat: "Chat do app com intermediários e bots genéricos",
        td_pagamento: "Formas de Pagamento", td_pag_direto: "PIX ou Cartão combinado direto e com segurança", td_pag_plat: "Pagamento pelas regras de cada plataforma",
        td_flexibilidade: "Flexibilidade de Horários", td_flex_direto: "Possibilidade de Early Check-in sob consulta direta", td_flex_plat: "Regras automáticas sem contato direto",
        sec_infra_tag: "Infraestrutura Completa", sec_infra_tit: "Tudo o que você precisa para uma estadia impecável",
        infra_wifi_tit: "Internet Fibra 600 Mbps", infra_wifi_desc: "Conexão dedicada de ultra-alta velocidade com roteador potente. Perfeito para chamadas de vídeo, reuniões executivas e streaming em 4K sem qualquer oscilação.",
        infra_checkin_tit: "Acesso Eletrônico 24h", infra_checkin_desc: "O portão abre por QR code e a porta do studio por uma senha exclusiva da sua estadia. As instruções chegam automaticamente minutos depois de você preencher o formulário de check-in online — dá para chegar a qualquer hora, sem recepção.",
        infra_cozinha_tit: "Cozinha Compacta Privativa", infra_cozinha_desc: "Geladeira com freezer, micro-ondas, cooktop, cafeteira elétrica, sanduicheira, panelas, louças e talheres. Prepare suas refeições com praticidade.",
        infra_ducha_tit: "Banheiro Privativo", infra_ducha_desc: "Box de vidro, ducha quente, bidê, secador de cabelo e toalhas para a estadia.",
        infra_lav_tit: "SNT Lavanderia no prédio", infra_lav_desc: "A SNT Lavanderia Self-Service funciona no andar de baixo, 24 horas, para lavar e secar suas roupas. É um serviço à parte, pago direto no totem.",
        infra_seg_tit: "Segurança & Monitoramento", infra_seg_desc: "Circuito interno de câmeras nas áreas comuns e iluminação inteligente para garantir a máxima tranquilidade para você e suas bagagens.",
        loc_tag: "Localização Privilegiada", loc_tit: "Perto de tudo em Guarulhos e na Grande São Paulo",
        loc_desc: "No bairro Cidade Seródio, em Guarulhos, com acesso de carro ou aplicativo aos terminais do Aeroporto Internacional de Guarulhos (GRU), à Rodovia Presidente Dutra e à Rodovia Ayrton Senna.",
        loc_endereco_oficial: "Endereço Oficial",
        dist_gru_tit: "Aeroporto GRU", dist_gru_val: "21-22 min de carro",
        dist_cptm_tit: "Estação Aeroporto-Guarulhos (CPTM)", dist_cptm_val: "20 min de carro",
        dist_comercio_tit: "Comércio & Padaria", dist_comercio_val: "Logo ao lado",
        dist_shopping_tit: "Shopping Bosque Maia", dist_shopping_val: "18 minutos",
        faq_tag: "Tire Suas Dúvidas", faq_tit: "Perguntas Frequentes",
        faq_q1: "Como funciona o check-in se meu voo chegar de madrugada?",
        faq_a1: "Tranquilo: o portão abre por QR code e a porta do studio por uma senha só sua, então você entra sozinho a qualquer hora a partir das 15h, inclusive de madrugada. As instruções chegam uns 5 minutos depois que você preenche o formulário de check-in online.",
        faq_q3: "Qual a diferença entre os studios?",
        faq_a3: "Só o tamanho: dois são maiores e dois mais compactos. Cama queen, cozinha, ar-condicionado, Smart TV, Wi-Fi de 600 Mbps e banheiro privativo são iguais em todos.",
        faq_q4: "A internet suporta reuniões em vídeo e trabalho remoto?",
        faq_a4: "Sim! Temos fibra óptica dedicada de 600 Mbps com baixa latência e sinal forte em todos os studios. Nossos hóspedes executivos utilizam regularmente para chamadas no Teams, Zoom, Google Meet e streaming.",
        faq_q5: "Quais as formas de pagamento aceitas para a reserva direta?",
        faq_a5: "Você pode pagar com total segurança via PIX (com confirmação instantânea) ou Cartão de Crédito. Todo o fluxo é combinado com clareza e recibo pelo WhatsApp oficial.",
        faq_q6: "Tem comércio ou alimentação perto do studio?",
        faq_a6: "Sim! A menos de 2 a 5 minutos a pé você encontra padaria, farmácia, supermercado e restaurantes, além de ampla cobertura de entrega do iFood com entrega rápida na nossa porta.",
        btn_faq_whatsapp: "Ainda tem dúvidas? Fale com a gente no WhatsApp",
        footer_desc: "Hospitalidade inteligente e moderna em Guarulhos. Studios privativos completos para quem valoriza silêncio, conforto, tecnologia e proximidade com o Aeroporto GRU.",
        footer_nav_tit: "Navegação", footer_atend_tit: "Atendimento Oficial",
        footer_atend_desc: "Atendimento humanizado para cotações, reservas e suporte ao hóspede:",
        footer_horarios: "Check-in: a partir das 15:00<br>Check-out: até as 11:00",
        footer_sustentavel: "Desenvolvido com tecnologia sustentável e zero CDNs externas em produção."
      },
      en: {
        nav_inicio: "Home",
        nav_disponibilidade: "Availability",
        nav_studios: "Accommodations",
        nav_comodidades: "Amenities",
        nav_localizacao: "Location",
        nav_faq: "FAQ",
        btn_nav_reserva: "Book on WhatsApp",
        badge_topo_local: "Private Stay in Guarulhos · GRU Airport",
        badge_topo_desconto: "🛡️ Book direct on our official WhatsApp",
        badge_topo_checkin: "🔑 24/7 Digital Self Check-in",
        hero_title: "SNT Studios · Private Studios in Guarulhos, near GRU Airport",
        sub_hospitalidade: "Independent Hospitality",
        sub_gru_dist: "About 20 minutes by car from Terminals 1, 2 and 3",
        btn_compartilhar: "Share",
        tag_master_king: "LARGER STUDIO",
        desc_master_king_curta: "Queen bed, work desk and blackout curtains",
        tag_executivo_premium: "Larger Studio",
        tag_cozinha_priv: "Compact Kitchen",
        tag_standard_smart: "Compact Studio",
        tag_standard_cozy: "Compact Studio",
        btn_todas_fotos: "Show all 20 photos",
        detalhe_tipo_espaco: "Entire private studio · Hosted by SNT Studios",
        detalhe_capacidade: "Up to 2 guests · 1 queen bed · 1 private bathroom · Equipped kitchenette",
        feature_checkin_tit: "24/7 self check-in via electronic lock",
        feature_checkin_desc: "The building gate opens with a QR code and your studio door with your own passcode: arrive any time of night, no physical keys.",
        feature_wifi_tit: "Dedicated 600 Mbps fiber Wi-Fi",
        feature_wifi_desc: "Ultra-fast, reliable internet tested for video calls, remote work, and uninterrupted 4K streaming.",
        feature_cozinha_tit: "Fully equipped private kitchenette",
        feature_cozinha_desc: "Fridge with freezer, microwave, stovetop, electric coffee maker, sandwich maker, cookware and tableware.",
        feature_gru_tit: "About 20 min by car from Guarulhos Airport (GRU)",
        feature_gru_desc: "It is 12 to 14 km to the terminals, about 21 to 22 minutes by car or ride app without traffic. Not walkable: the road goes around the airport.",
        sobre_espaco_tit: "About the space",
        sobre_espaco_p1: "SNT Studios offers an autonomous hospitality concept: full privacy, modern finish, and unbeatable proximity to GRU Airport. Every unit is completely private with dedicated bathroom, workspace, and air conditioning/fan.",
        tipologias_tit: "Two sizes, the same amenities",
        cat_ampla_tit: "Larger Studios (2 units)",
        cat_ampla_desc: "The two larger ones: more free space to move around and unpack.",
        cat_compacta_tit: "Compact Studios (2 units)",
        cat_compacta_desc: "The two smaller ones: the same queen bed, kitchenette and amenities in a tighter layout.",
        tipologias_nota: "Select your dates to verify live availability and calculate the final bundled rate.",
        comodidades_grid_tit: "What this place offers",
        comod_wifi: "600 Mbps Fiber Wi-Fi",
        comod_fechadura: "24/7 Keyless digital entry",
        comod_tv: "Smart TV with Streaming",
        comod_cooktop: "Kitchenette with Cooktop",
        comod_ar: "Split air conditioning and heater",
        comod_cafe: "Electric coffee maker",
        comod_ducha: "Hot shower",
        comod_enxoval: "Sanitized hotel linen",
        comod_bancada: "Laptop work desk",
        comod_cameras: "Security cameras in common areas",
        comod_transporte: "Easy pickup for Uber/99",
        comod_frigobar: "Fridge and microwave",
        regra_checkin_tit: "Check-in:",
        regra_checkin_val: "From 3:00 PM (24/7 autonomous digital access)",
        regra_checkout_tit: "Check-out:",
        regra_checkout_val: "Until 11:00 AM",
        regra_silencio_tit: "Quiet Hours:",
        regra_silencio_val: "Please respect other guests' rest after 10:00 PM",
        card_por_noite: " / night", card_ver_valor: "See price",
        card_tarifa_oficial: "Official Rate",
        lbl_checkin: "CHECK-IN",
        lbl_checkout: "CHECKOUT",
        lbl_hospedes: "GUESTS",
        txt_inserir_data: "Add date",
        opt_1_hospede: "1 guest",
        opt_2_hospedes: "2 guests (Couple)",
        cal_escolha_checkin: "Select check-in date",
        cal_escolha_checkout: "Select checkout date",
        cal_sub_instrucao: "1st tap: check-in · 2nd tap: checkout",
        cal_titulo: "Select dates",
        cal_subtitulo: "Add your travel dates for exact pricing",
        cal_btn_fechar: "Close",
        txt_noite_sing: "night",
        txt_noites_plur: "nights",
        btn_limpar_datas: "Clear dates",
        dia_dom: "Sun", dia_seg: "Mon", dia_ter: "Tue", dia_qua: "Wed", dia_qui: "Thu", dia_sex: "Fri", dia_sab: "Sat",
        txt_sem_datas: "No dates selected",
        btn_concluir: "Done",
        btn_conferir_disp: "Check availability",
        btn_verificar_datas_curto: "Check Dates",
        txt_nao_cobrado: "You won't be charged yet",
        txt_garantido: "Guaranteed",
        vantagem_zero_taxas: "Zero third-party service fees",
        txt_economia_real: "No surprises",
        vantagem_tempo_real: "Real-time calendar availability",
        diff_wifi_tit: "600 Mbps Wi-Fi", diff_wifi_sub: "Dedicated ultra-fast fiber",
        diff_checkin_tit: "24/7 Self Check-in", diff_checkin_sub: "Electronic passcode lock",
        diff_gru_tit: "~20 min to GRU", diff_gru_sub: "12 to 14 km by car to the terminals",
        diff_cozinha_tit: "Equipped Kitchen", diff_cozinha_sub: "Fridge, microwave & coffee maker",
        diff_desconto_tit: "Direct Booking", diff_desconto_sub: "Official WhatsApp, Pix or card",
        sec_studios_tag: "Our Accommodations", sec_studios_tit: "Explore our private studios",
        sec_studios_sub: "All four studios have the same amenities — only the size changes: electronic lock with a stay passcode, 600 Mbps fiber Wi-Fi, Smart TV, split air conditioning, kitchenette and private bathroom.",
        btn_filtro_todos: "All Studios", btn_filtro_amplos: "Larger Studios", btn_filtro_compactos: "Compact Studios",
        badge_maior_studio: "LARGER", badge_executivo: "LARGER", badge_smart: "COMPACT", badge_cozy: "COMPACT",
        btn_ver_fotos: "View Photos", btn_verificar_datas: "Check Dates & Availability",
        card_master_desc: "One of the two larger studios: more room to move around and for luggage.",
        card_master_esp: "📐 Same amenities as every studio, with more free space.",
        item_cama_queen: "Queen bed with linens", item_home_office: "Work desk & 600 Mbps Wi-Fi",
        item_cozinha_cooktop: "Kitchenette: fridge, microwave, stovetop, coffee maker", item_fechadura_tv: "Smart TV, air conditioning & electronic lock",
        card_executivo_desc: "One of the two larger studios: good for longer and business stays.",
        card_executivo_esp: "📐 Same amenities as every studio, with more free space.",
        item_cama_casal_premium: "Queen bed with linens", item_cozinha_cafeteira: "Kitchenette: fridge, microwave, stovetop, coffee maker",
        card_smart_desc: "One of the two compact studios: practical for layovers and short stays.",
        card_smart_esp: "📐 Same amenities as every studio, in a compact layout.",
        item_cama_casal: "Queen bed with linens", item_frigobar_micro: "Kitchenette: fridge, microwave, stovetop, coffee maker", item_wifi_tv: "600 Mbps Wi-Fi & Smart TV", item_fechadura_24h: "Air conditioning & electronic lock",
        card_cozy_desc: "One of the two compact studios: everything the larger ones have, at better value.",
        card_cozy_esp: "📐 Same amenities as every studio, in a compact layout.",
        item_cama_casal_travesseiro: "Queen bed with linens", item_ducha_press: "Private bathroom with shower and hair dryer", item_frigobar_cafe: "Kitchenette: fridge, microwave, stovetop, coffee maker",
        comp_tag: "Total Transparency", comp_tit: "Why book directly with us on WhatsApp?",
        th_beneficio: "Benefit", th_direto: "SNT Studios (Official Direct)", th_plataformas: "OTAs (Booking / Airbnb)",
        td_atendimento: "Customer Support", td_atend_direto: "Direct WhatsApp with our local team", td_atend_plat: "Generic chatbots and app intermediaries",
        td_pagamento: "Payment Methods", td_pag_direto: "PIX or Credit Card safely arranged", td_pag_plat: "Payment under each platform's rules",
        td_flexibilidade: "Schedule Flexibility", td_flex_direto: "Early check-in option upon direct inquiry", td_flex_plat: "Automated, inflexible rules",
        sec_infra_tag: "Full Amenities", sec_infra_tit: "Everything you need for a seamless stay",
        infra_wifi_tit: "600 Mbps Fiber Wi-Fi", infra_wifi_desc: "High-speed dedicated Wi-Fi with strong coverage across all studios for streaming and business calls.",
        infra_checkin_tit: "24/7 Digital Access", infra_checkin_desc: "The gate opens with a QR code and your studio door with a passcode unique to your stay. Instructions arrive automatically minutes after you fill in the online check-in form — arrive any time, no front desk.",
        infra_cozinha_tit: "Private Kitchenette", infra_cozinha_desc: "Fridge with freezer, microwave, stovetop, electric coffee maker, sandwich maker, cookware and tableware. Cook your own meals with ease.",
        infra_ducha_tit: "Private Bathroom", infra_ducha_desc: "Glass shower, hot shower, bidet, hair dryer and towels for your stay.",
        infra_lav_tit: "SNT Laundromat in the building", infra_lav_desc: "SNT self-service laundromat runs downstairs, 24 hours, to wash and dry your clothes. It is a separate service, paid at the kiosk.",
        infra_seg_tit: "Security & Monitoring", infra_seg_desc: "CCTV in common areas and smart lighting for peace of mind.",
        loc_tag: "Strategic Location", loc_tit: "Close to GRU Airport and Greater São Paulo",
        loc_desc: "In Cidade Seródio, Guarulhos, with car or ride-app access to the Guarulhos International Airport (GRU) terminals and the Dutra and Ayrton Senna highways.",
        loc_endereco_oficial: "Official Address",
        dist_gru_tit: "GRU Airport", dist_gru_val: "21-22 min by car",
        dist_cptm_tit: "Aeroporto-Guarulhos train station (CPTM)", dist_cptm_val: "20 min by car",
        dist_comercio_tit: "Supermarket & Bakery", dist_comercio_val: "Right next door",
        dist_shopping_tit: "Bosque Maia Mall", dist_shopping_val: "18 minutes",
        faq_tag: "Got Questions?", faq_tit: "Frequently Asked Questions",
        faq_q1: "How does check-in work if my flight lands late at night or early morning?",
        faq_a1: "No problem: the gate opens with a QR code and your studio door with your own passcode, so you can let yourself in any time from 3 PM, even in the middle of the night. Instructions arrive about 5 minutes after you fill in the online check-in form.",
        faq_q3: "What is the difference between the studios?",
        faq_a3: "Only the size: two are larger and two are more compact. Queen bed, kitchenette, air conditioning, Smart TV, 600 Mbps Wi-Fi and private bathroom are the same in all of them.",
        faq_q4: "Is the Wi-Fi fast enough for remote work and video meetings?",
        faq_a4: "Yes! We provide dedicated 600 Mbps fiber internet with low latency and strong coverage, extensively tested for Zoom, Google Meet, and 4K streaming.",
        faq_q5: "Which payment methods are accepted?",
        faq_a5: "You can pay securely via instant PIX or credit card. Everything is arranged transparently with a receipt on our official WhatsApp.",
        faq_q6: "Are there restaurants and grocery stores nearby?",
        faq_a6: "Yes, bakeries, pharmacies, grocery stores, and restaurants are within a 2 to 5-minute walk, with fast iFood delivery straight to our door.",
        btn_faq_whatsapp: "Still have questions? Chat with us on WhatsApp",
        footer_desc: "Smart and modern hospitality in Guarulhos. Full private studios designed for travelers seeking quiet rest and quick GRU Airport access.",
        footer_nav_tit: "Navigation", footer_atend_tit: "Official Support",
        footer_atend_desc: "Direct support for quotes, bookings, and guest assistance:",
        footer_horarios: "Check-in: from 3:00 PM<br>Check-out: until 11:00 AM",
        footer_sustentavel: "Engineered with sustainable technology and zero external CDNs in production."
      },
      es: {
        nav_inicio: "Inicio",
        nav_disponibilidade: "Disponibilidad",
        nav_studios: "Alojamientos",
        nav_comodidades: "Comodidades",
        nav_localizacao: "Ubicación",
        nav_faq: "Preguntas",
        btn_nav_reserva: "Reservar por WhatsApp",
        badge_topo_local: "Alojamiento Privado en Guarulhos · Aeropuerto GRU",
        badge_topo_desconto: "🛡️ Reserva directa por WhatsApp oficial",
        badge_topo_checkin: "🔑 Auto Check-in 24h",
        hero_title: "SNT Studios · Estudios Privados en Guarulhos, cerca del Aeropuerto GRU",
        sub_hospitalidade: "Hospitalidad Independiente",
        sub_gru_dist: "A unos 20 minutos en auto de las Terminales 1, 2 y 3",
        btn_compartilhar: "Compartir",
        tag_master_king: "ESTUDIO AMPLIO",
        desc_master_king_curta: "Cama queen, escritorio y cortinas blackout",
        tag_executivo_premium: "Estudio Amplio",
        tag_cozinha_priv: "Cocina Compacta",
        tag_standard_smart: "Estudio Compacto",
        tag_standard_cozy: "Estudio Compacto",
        btn_todas_fotos: "Ver las 20 fotos",
        detalhe_tipo_espaco: "Estudio privado completo · Alojamiento SNT",
        detalhe_capacidade: "Hasta 2 huéspedes · 1 cama queen · 1 baño privado · Cocina compacta equipada",
        feature_checkin_tit: "Auto check-in 24h con cerradura electrónica",
        feature_checkin_desc: "El portón abre con código QR y la puerta del estudio con una clave solo suya: llegue a cualquier hora de la noche, sin llaves físicas.",
        feature_wifi_tit: "Wi-Fi fibra de 600 Mbps dedicado",
        feature_wifi_desc: "Conexión de alta velocidad probada para videollamadas, trabajo remoto y streaming en 4K sin cortes.",
        feature_cozinha_tit: "Cocina privada equipada",
        feature_cozinha_desc: "Heladera con freezer, microondas, anafe, cafetera eléctrica, sandwichera, ollas, vajilla y cubiertos.",
        feature_gru_tit: "A unos 20 min en auto del Aeropuerto de Guarulhos (GRU)",
        feature_gru_desc: "Son 12 a 14 km hasta las terminales, unos 21 a 22 minutos en auto o aplicación sin tráfico. No se puede ir a pie: el camino rodea el aeropuerto.",
        sobre_espaco_tit: "Sobre el espacio",
        sobre_espaco_p1: "SNT Studios brinda una propuesta moderna de hospitalidad autónoma: privacidad total, excelente confort y ubicación inmejorable junto a GRU. Todas las unidades son 100% privadas con baño propio y cocina equipada.",
        tipologias_tit: "Dos tamaños, el mismo equipamiento",
        cat_ampla_tit: "Estudios Amplios (2 unidades)",
        cat_ampla_desc: "Los dos más grandes: más espacio libre para circular y acomodar el equipaje.",
        cat_compacta_tit: "Estudios Compactos (2 unidades)",
        cat_compacta_desc: "Los dos más pequeños: la misma cama queen, cocina y comodidades, en una planta más compacta.",
        tipologias_nota: "Seleccione sus fechas para verificar disponibilidad en tiempo real con el precio final consolidado.",
        comodidades_grid_tit: "Qué ofrece este lugar",
        comod_wifi: "Wi-Fi Fibra 600 Mbps",
        comod_fechadura: "Cerradura digital 24h",
        comod_tv: "Smart TV con Streaming",
        comod_cooktop: "Cocina con Anafe",
        comod_ar: "Aire acondicionado split y calefactor",
        comod_cafe: "Cafetera eléctrica",
        comod_ducha: "Ducha caliente",
        comod_enxoval: "Ropa de cama y toallas de hotel",
        comod_bancada: "Escritorio para notebook",
        comod_cameras: "Cámaras en áreas comunes",
        comod_transporte: "Acceso fácil para Uber/99",
        comod_frigobar: "Heladera y microondas",
        regra_checkin_tit: "Check-in:",
        regra_checkin_val: "A partir de las 15:00 (Acceso autónomo 24h con código)",
        regra_checkout_tit: "Check-out:",
        regra_checkout_val: "Hasta las 11:00",
        regra_silencio_tit: "Política de Silencio:",
        regra_silencio_val: "Respeto al descanso de los demás huéspedes a partir de las 22:00",
        card_por_noite: " / noche", card_ver_valor: "Ver precio",
        card_tarifa_oficial: "Tarifa Oficial",
        lbl_checkin: "CHECK-IN",
        lbl_checkout: "CHECKOUT",
        lbl_hospedes: "HUÉSPEDES",
        txt_inserir_data: "Añadir fecha",
        opt_1_hospede: "1 huésped",
        opt_2_hospedes: "2 huéspedes (Pareja)",
        cal_escolha_checkin: "Seleccione fecha de check-in",
        cal_escolha_checkout: "Seleccione fecha de checkout",
        cal_sub_instrucao: "1º clic: entrada · 2º clic: salida",
        cal_titulo: "Seleccionar fechas",
        cal_subtitulo: "Agregue las fechas de su viaje para ver los precios exactos",
        cal_btn_fechar: "Cerrar",
        txt_noite_sing: "noche",
        txt_noites_plur: "noches",
        btn_limpar_datas: "Borrar fechas",
        dia_dom: "Dom", dia_seg: "Lun", dia_ter: "Mar", dia_qua: "Mié", dia_qui: "Jue", dia_sex: "Vie", dia_sab: "Sáb",
        txt_sem_datas: "Ninguna fecha seleccionada",
        btn_concluir: "Listo",
        btn_conferir_disp: "Comprobar disponibilidad",
        btn_verificar_datas_curto: "Verificar Fechas",
        txt_nao_cobrado: "Aún no se te cobrará nada",
        txt_garantido: "Garantizado",
        vantagem_zero_taxas: "Sin comisiones de intermediarios",
        txt_economia_real: "Sin sorpresas",
        vantagem_tempo_real: "Disponibilidad en tiempo real",
        diff_wifi_tit: "Wi-Fi 600 Mbps", diff_wifi_sub: "Fibra óptica dedicada ultra rápida",
        diff_checkin_tit: "Self Check-in 24h", diff_checkin_sub: "Cerradura electrónica con código personal",
        diff_gru_tit: "~20 min de GRU", diff_gru_sub: "12 a 14 km en auto hasta las terminales",
        diff_cozinha_tit: "Cocina Equipada", diff_cozinha_sub: "Heladera, microondas y cafetera",
        diff_desconto_tit: "Reserva Directa", diff_desconto_sub: "WhatsApp oficial, Pix o tarjeta",
        sec_studios_tag: "Nuestros Alojamientos", sec_studios_tit: "Descubra nuestras opciones privadas",
        sec_studios_sub: "Los cuatro estudios tienen el mismo equipamiento — solo cambia el tamaño: cerradura electrónica con clave de la estadía, Wi-Fi de fibra 600 Mbps, Smart TV, aire split, cocina compacta y baño privado.",
        btn_filtro_todos: "Todos los Estudios", btn_filtro_amplos: "Estudios Amplios", btn_filtro_compactos: "Estudios Compactos",
        badge_maior_studio: "AMPLIO", badge_executivo: "AMPLIO", badge_smart: "COMPACTO", badge_cozy: "COMPACTO",
        btn_ver_fotos: "Ver Fotos", btn_verificar_datas: "Verificar Fechas y Disponibilidad",
        card_master_desc: "Uno de los dos estudios más grandes: más espacio para circular y para el equipaje.",
        card_master_esp: "📐 El mismo equipamiento de todos los estudios, con más espacio libre.",
        item_cama_queen: "Cama queen con ropa de cama", item_home_office: "Escritorio y Wi-Fi 600 Mbps",
        item_cozinha_cooktop: "Cocina: heladera, microondas, anafe y cafetera", item_fechadura_tv: "Smart TV, aire acondicionado y cerradura electrónica",
        card_executivo_desc: "Uno de los dos estudios más grandes: ideal para estadías largas y de trabajo.",
        card_executivo_esp: "📐 El mismo equipamiento de todos los estudios, con más espacio libre.",
        item_cama_casal_premium: "Cama queen con ropa de cama", item_cozinha_cafeteira: "Cocina: heladera, microondas, anafe y cafetera",
        card_smart_desc: "Uno de los dos estudios compactos: práctico para escalas y estadías cortas.",
        card_smart_esp: "📐 El mismo equipamiento de todos los estudios, en una planta compacta.",
        item_cama_casal: "Cama queen con ropa de cama", item_frigobar_micro: "Cocina: heladera, microondas, anafe y cafetera", item_wifi_tv: "Wi-Fi 600 Mbps y Smart TV", item_fechadura_24h: "Aire acondicionado y cerradura electrónica",
        card_cozy_desc: "Uno de los dos estudios compactos: todo lo que tienen los grandes, con mejor precio.",
        card_cozy_esp: "📐 El mismo equipamiento de todos los estudios, en una planta compacta.",
        item_cama_casal_travesseiro: "Cama queen con ropa de cama", item_ducha_press: "Baño privado con ducha y secador", item_frigobar_cafe: "Cocina: heladera, microondas, anafe y cafetera",
        comp_tag: "Total Transparencia", comp_tit: "¿Por qué reservar directo con nosotros por WhatsApp?",
        th_beneficio: "Beneficio", th_direto: "SNT Studios (Directo Oficial)", th_plataformas: "Plataformas (Booking / Airbnb)",
        td_atendimento: "Atención al Cliente", td_atend_direto: "WhatsApp directo con nuestro equipo local", td_atend_plat: "Chat de app con bots e intermediarios",
        td_pagamento: "Medios de Pago", td_pag_direto: "PIX o Tarjeta acordado de forma segura", td_pag_plat: "Pago según las reglas de cada plataforma",
        td_flexibilidade: "Flexibilidad Horaria", td_flex_direto: "Early check-in disponible bajo consulta directa", td_flex_plat: "Normas automáticas sin contacto humano",
        sec_infra_tag: "Infraestructura Completa", sec_infra_tit: "Todo lo que necesita para una estancia impecable",
        infra_wifi_tit: "Internet Fibra 600 Mbps", infra_wifi_desc: "Conexión dedicada de alta velocidad para videollamadas, trabajo y streaming 4K.",
        infra_checkin_tit: "Acceso Electrónico 24h", infra_checkin_desc: "El portón abre con código QR y la puerta del estudio con una clave exclusiva de su estadía. Las instrucciones llegan automáticamente minutos después de completar el formulario de check-in online — llegue a cualquier hora, sin recepción.",
        infra_cozinha_tit: "Cocina Compacta Privada", infra_cozinha_desc: "Heladera con freezer, microondas, anafe, cafetera eléctrica, sandwichera, ollas, vajilla y cubiertos. Prepare sus comidas con practicidad.",
        infra_ducha_tit: "Baño Privado", infra_ducha_desc: "Box de vidrio, ducha caliente, bidé, secador de pelo y toallas para la estadía.",
        infra_lav_tit: "SNT Lavandería en el edificio", infra_lav_desc: "La SNT Lavandería Self-Service funciona en la planta baja, las 24 horas, para lavar y secar su ropa. Es un servicio aparte, pagado en el tótem.",
        infra_seg_tit: "Seguridad y Monitoreo", infra_seg_desc: "Cámaras en áreas comunes e iluminación inteligente para su tranquilidad.",
        loc_tag: "Ubicación Estratégica", loc_tit: "Cerca de todo en Guarulhos y Gran São Paulo",
        loc_desc: "En el barrio Cidade Seródio, Guarulhos, con acceso en auto o aplicación a las terminales del Aeropuerto Internacional de Guarulhos (GRU) y a las autopistas Dutra y Ayrton Senna.",
        loc_endereco_oficial: "Dirección Oficial",
        dist_gru_tit: "Aeropuerto GRU", dist_gru_val: "21-22 min en auto",
        dist_cptm_tit: "Estación Aeroporto-Guarulhos (CPTM)", dist_cptm_val: "20 min en auto",
        dist_comercio_tit: "Comercio y Panadería", dist_comercio_val: "Al lado",
        dist_shopping_tit: "Shopping Bosque Maia", dist_shopping_val: "18 minutos",
        faq_tag: "Preguntas Frecuentes", faq_tit: "Dudas Habituales",
        faq_q1: "¿Cómo funciona el check-in si mi vuelo llega de madrugada?",
        faq_a1: "Sin problema: el portón abre con código QR y la puerta del estudio con una clave solo suya, así que entra solo a cualquier hora desde las 15:00, incluso de madrugada. Las instrucciones llegan unos 5 minutos después de completar el formulario de check-in online.",
        faq_q3: "¿Cuál es la diferencia entre los estudios?",
        faq_a3: "Solo el tamaño: dos son más grandes y dos más compactos. Cama queen, cocina, aire acondicionado, Smart TV, Wi-Fi de 600 Mbps y baño privado son iguales en todos.",
        faq_q4: "¿El Wi-Fi es apto para videollamadas y trabajo remoto?",
        faq_a4: "¡Sí! Disponemos de fibra óptica dedicada de 600 Mbps con baja latencia y excelente señal para Zoom, Google Meet y streaming 4K.",
        faq_q5: "¿Qué formas de pago se aceptan?",
        faq_a5: "Puede pagar con total seguridad mediante PIX o Tarjeta de Crédito, todo coordinado de forma transparente por WhatsApp.",
        faq_q6: "¿Hay comercios o restaurantes cerca?",
        faq_a6: "Sí, a 2-5 minutos a pie encontrará panadería, farmacia, supermercado y restaurantes, además de entrega rápida de iFood.",
        btn_faq_whatsapp: "¿Tiene dudas? Escríbanos por WhatsApp",
        footer_desc: "Hospitalidad moderna e inteligente en Guarulhos. Estudios privados completos para quienes valoran silencio, confort y cercanía a GRU.",
        footer_nav_tit: "Navegación", footer_atend_tit: "Atención Oficial",
        footer_atend_desc: "Atención directa para cotizaciones, reservas y soporte al huésped:",
        footer_horarios: "Check-in: a partir de las 15:00<br>Check-out: hasta las 11:00",
        footer_sustentavel: "Desarrollado con tecnología sustentable y sin CDNs externas en producción."
      }
    };

    function trocarIdioma(lang) {
      if (!I18N[lang]) return;
      idiomaAtual = lang;
      localStorage.setItem('snt_studios_lang', lang);

      // Atualiza botões do seletor
      ['pt', 'en', 'es'].forEach(l => {
        const b = document.getElementById('btnLang' + l.charAt(0).toUpperCase() + l.slice(1));
        if (b) {
          if (l === lang) {
            b.className = "px-2 py-1 rounded-lg font-bold transition bg-emerald-500 text-slate-950";
          } else {
            b.className = "px-2 py-1 rounded-lg font-bold transition text-slate-400 hover:text-white";
          }
        }
      });

      // Aplica traduções em todos os elementos com data-i18n
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const chave = el.getAttribute('data-i18n');
        if (I18N[lang][chave]) {
          el.innerHTML = I18N[lang][chave];
        }
      });

      // Atualiza textos do calendário e cotação caso estejam visíveis
      renderizarMeses();
      atualizarDisplayDatas();
      if (ultimaCotacao && Array.isArray(ultimaCotacao.studios)) {
        renderizarCardDisponibilidade();
      }
    }

    // ========================================================
    // FORMATADORES E UTILITÁRIOS
    // ========================================================
    function formatarDataBr(isoStr) {
      if (!isoStr) return "";
      const [ano, mes, dia] = isoStr.split('-');
      if (idiomaAtual === 'en') return `${mes}/${dia}/${ano}`;
      return `${dia}/${mes}/${ano}`;
    }

    function formatarMoeda(valor) {
      return new Intl.NumberFormat(idiomaAtual === 'en' ? 'en-US' : (idiomaAtual === 'es' ? 'es-ES' : 'pt-BR'), { 
        style: 'currency', 
        currency: 'BRL' 
      }).format(Number(valor) || 0);
    }

    function escaparHtml(valor) {
      return String(valor == null ? '' : valor)
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#039;');
    }

    const API_COTACAO = "https://snt-lavanderia-bot-production.up.railway.app/api/studios/public/cotacao";
    const API_OCUPACAO = "https://snt-lavanderia-bot-production.up.railway.app/api/studios/public/ocupacao";
    let ultimaCotacao = null;

    // ========================================================
    // MAPEAMENTO DE NOMES COMERCIAIS (ZERO NÚMEROS DE STUDIOS)
    // ========================================================
    const STUDIOS_COMERCIAIS = {
      '12': {
        chave: 'master',
        nome: 'Studio Amplo A',
        categoria: 'amplos',
        tituloExibicao: 'Studio Amplo A',
        destaque: 'Um dos dois studios maiores · Cama queen',
        subtitulo: 'Mais área livre, os mesmos itens de todos os studios'
      },
      '14': {
        chave: 'executivo',
        nome: 'Studio Amplo B',
        categoria: 'amplos',
        tituloExibicao: 'Studio Amplo B',
        destaque: 'Um dos dois studios maiores · Cama queen',
        subtitulo: 'Mais área livre, os mesmos itens de todos os studios'
      },
      '11': {
        chave: 'smart',
        nome: 'Studio Compacto A',
        categoria: 'compactos',
        tituloExibicao: 'Studio Compacto A',
        destaque: 'Um dos dois studios compactos · Cama queen',
        subtitulo: 'Planta compacta, os mesmos itens de todos os studios'
      },
      '13': {
        chave: 'cozy',
        nome: 'Studio Compacto B',
        categoria: 'compactos',
        tituloExibicao: 'Studio Compacto B',
        destaque: 'Um dos dois studios compactos · Cama queen',
        subtitulo: 'Planta compacta, os mesmos itens de todos os studios'
      }
    };

    // ========================================================
    // CALENDÁRIO RANGE AIRBNB (SELEÇÃO DE 2 CLIQUES + DUAL-MONTH)
    // ========================================================
    let dataCheckIn = "";
    let dataCheckOut = "";
    let dataHover = "";
    let calAno = new Date().getFullYear();
    let calMes = new Date().getMonth(); // 0-11
    let datasTotalmenteOcupadas = new Set();
    let carregandoDisponibilidadeGeral = false;
    let overflowAntesDoCalendario = "";
    let calendarioBloqueouRolagem = false;

    const NOMES_MESES = {
      pt: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
      en: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      es: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    };

    const DIAS_SEMANA_SIGLAS = {
      pt: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'],
      en: ['S', 'M', 'T', 'W', 'T', 'F', 'S'],
      es: ['D', 'L', 'M', 'M', 'J', 'V', 'S']
    };

    function clicarBoxCheckIn() {
      abrirCalendario();
      dataCheckIn = "";
      dataCheckOut = "";
      dataHover = "";
      document.getElementById('inputCheckIn').value = "";
      document.getElementById('inputCheckOut').value = "";
      atualizarDisplayDatas();
      renderizarMeses();
    }

    function clicarBoxCheckOut() {
      abrirCalendario();
      if (dataCheckIn) {
        dataCheckOut = "";
        dataHover = "";
        document.getElementById('inputCheckOut').value = "";
        atualizarDisplayDatas();
        renderizarMeses();
      }
    }

    function alternarCalendario() {
      const el = document.getElementById('calendarioAirbnb');
      if (!el) return;
      if (el.classList.contains('hidden')) {
        abrirCalendario();
      } else {
        fecharCalendario();
      }
    }

    function abrirCalendario() {
      const el = document.getElementById('calendarioAirbnb');
      const backdrop = document.getElementById('calendarioBackdrop');
      if (el) {
        // O calendário nasce dentro do card por organização do HTML, mas vira
        // filho do body ao abrir. Assim `position: fixed` usa a tela inteira,
        // mesmo com backdrop-filter/transform nos ancestrais do card.
        if (backdrop && backdrop.parentElement !== document.body) document.body.appendChild(backdrop);
        if (el.parentElement !== document.body) document.body.appendChild(el);
        if (backdrop) backdrop.classList.remove('hidden');
        el.classList.remove('hidden');
        document.querySelectorAll('[aria-controls="calendarioAirbnb"]').forEach((controle) => {
          controle.setAttribute('aria-expanded', 'true');
        });
        if (!calendarioBloqueouRolagem) {
          overflowAntesDoCalendario = document.body.style.overflow;
          document.body.style.overflow = 'hidden';
          calendarioBloqueouRolagem = true;
        }
        renderizarMeses();
        if (datasTotalmenteOcupadas.size === 0) {
          carregarDisponibilidadeGeral();
        }
      }
    }

    function fecharCalendario() {
      const el = document.getElementById('calendarioAirbnb');
      const backdrop = document.getElementById('calendarioBackdrop');
      if (el) el.classList.add('hidden');
      if (backdrop) backdrop.classList.add('hidden');
      document.querySelectorAll('[aria-controls="calendarioAirbnb"]').forEach((controle) => {
        controle.setAttribute('aria-expanded', 'false');
      });
      if (calendarioBloqueouRolagem) {
        document.body.style.overflow = overflowAntesDoCalendario;
        calendarioBloqueouRolagem = false;
      }
    }

    function mudarMes(delta) {
      calMes += delta;
      if (calMes < 0) {
        calMes = 11;
        calAno--;
      } else if (calMes > 11) {
        calMes = 0;
        calAno++;
      }
      // Não permite voltar para meses anteriores ao mês atual
      const agora = new Date();
      if (calAno < agora.getFullYear() || (calAno === agora.getFullYear() && calMes < agora.getMonth())) {
        calAno = agora.getFullYear();
        calMes = agora.getMonth();
      }
      renderizarMeses();
    }

    function formatarTituloMes(ano, mes) {
      const lista = NOMES_MESES[idiomaAtual] || NOMES_MESES['pt'];
      const nomeMes = lista[mes];
      if (idiomaAtual === 'pt' || idiomaAtual === 'es') {
        return `${nomeMes.toLowerCase()} de ${ano}`;
      }
      return `${nomeMes} ${ano}`;
    }

    function renderizarCabecalhoSemana(elContainer) {
      if (!elContainer) return;
      const siglas = DIAS_SEMANA_SIGLAS[idiomaAtual] || DIAS_SEMANA_SIGLAS['pt'];
      elContainer.innerHTML = siglas.map(s => `<span>${s}</span>`).join('');
    }

    function renderizarGradeDiasMes(ano, mes, elGrid) {
      if (!elGrid) return;
      elGrid.innerHTML = '';

      const agora = new Date();
      const hojeIso = `${agora.getFullYear()}-${String(agora.getMonth() + 1).padStart(2, '0')}-${String(agora.getDate()).padStart(2, '0')}`;

      const primeiroDiaSemana = new Date(ano, mes, 1).getDay();
      const totalDiasMes = new Date(ano, mes + 1, 0).getDate();

      // Células em branco antes do dia 1
      for (let i = 0; i < primeiroDiaSemana; i++) {
        const vazio = document.createElement('div');
        vazio.className = "h-9";
        elGrid.appendChild(vazio);
      }

      // Se Check-in já foi definido e estamos aguardando Checkout,
      // qualquer noite após a primeira noite indisponível não pode ser estendida
      let primeiroBloqueioAposCheckIn = null;
      if (dataCheckIn && !dataCheckOut) {
        const bloqueiosOrdenados = Array.from(datasTotalmenteOcupadas).sort();
        for (const bloq of bloqueiosOrdenados) {
          if (bloq > dataCheckIn) {
            primeiroBloqueioAposCheckIn = bloq;
            break;
          }
        }
      }

      for (let dia = 1; dia <= totalDiasMes; dia++) {
        const diaIso = `${ano}-${String(mes + 1).padStart(2, '0')}-${String(dia).padStart(2, '0')}`;
        const ehPassado = diaIso < hojeIso;
        const ehTotalmenteOcupado = datasTotalmenteOcupadas.has(diaIso);
        let ehIndisponivel = false;
        if (ehPassado) {
          ehIndisponivel = true;
        } else if (dataCheckIn && !dataCheckOut) {
          // Fase 2: Seleção de checkout
          if (diaIso > dataCheckIn) {
            // Checkout válido até o primeiro dia de bloqueio (inclusive, manhã da saída)
            if (primeiroBloqueioAposCheckIn && diaIso > primeiroBloqueioAposCheckIn) {
              ehIndisponivel = true;
            }
          } else if (diaIso < dataCheckIn) {
            // Se clicar antes do check-in atual, vira novo check-in (logo a noite deve estar livre)
            if (ehTotalmenteOcupado) {
              ehIndisponivel = true;
            }
          }
        } else {
          // Fase 1: Seleção de check-in (ou reinício após seleção completa)
          if (ehTotalmenteOcupado) {
            ehIndisponivel = true;
          }
        }

        const btn = document.createElement('button');
        btn.type = "button";
        btn.innerText = String(dia);
        btn.setAttribute('data-date', diaIso);
        const localeCalendario = idiomaAtual === 'en' ? 'en-US' : (idiomaAtual === 'es' ? 'es-ES' : 'pt-BR');
        btn.setAttribute('aria-label', new Intl.DateTimeFormat(localeCalendario, {
          weekday: 'long', day: 'numeric', month: 'long', year: 'numeric'
        }).format(new Date(diaIso + 'T12:00:00')));

        if (ehIndisponivel) {
          btn.className = "h-9 w-full flex items-center justify-center rounded-full text-xs font-normal text-slate-600 line-through cursor-not-allowed opacity-35";
          btn.disabled = true;
        } else {
          btn.onclick = () => selecionarDiaCalendario(diaIso);
          btn.onmouseenter = () => hoverDiaCalendario(diaIso);

          const ehCheckIn = dataCheckIn === diaIso;
          const ehCheckOut = dataCheckOut === diaIso;
          const emIntervalo = dataCheckIn && dataCheckOut && diaIso > dataCheckIn && diaIso < dataCheckOut;

          let classes = "h-9 w-full flex items-center justify-center text-xs font-semibold transition ";

          if (ehCheckIn || ehCheckOut) {
            classes += "bg-emerald-500 text-slate-950 font-black shadow-md shadow-emerald-500/30 scale-105 rounded-full z-10";
          } else if (emIntervalo) {
            classes += "bg-emerald-500/20 text-emerald-300 rounded-none";
          } else {
            classes += "text-white font-bold hover:bg-slate-800 rounded-full";
          }
          btn.className = classes;
        }

        elGrid.appendChild(btn);
      }
    }

    function renderizarMeses() {
      // Mês 1
      const mes1 = calMes;
      const ano1 = calAno;
      const tit1 = document.getElementById('calMesAno1');
      if (tit1) tit1.innerText = formatarTituloMes(ano1, mes1);
      renderizarCabecalhoSemana(document.getElementById('calDiasSemana1'));
      renderizarGradeDiasMes(ano1, mes1, document.getElementById('calDiasGrid1'));

      // Mês 2
      let mes2 = calMes + 1;
      let ano2 = calAno;
      if (mes2 > 11) {
        mes2 = 0;
        ano2++;
      }
      const tit2 = document.getElementById('calMesAno2');
      if (tit2) tit2.innerText = formatarTituloMes(ano2, mes2);
      renderizarCabecalhoSemana(document.getElementById('calDiasSemana2'));
      renderizarGradeDiasMes(ano2, mes2, document.getElementById('calDiasGrid2'));

      // Desabilita navegação para meses passados
      const agora = new Date();
      const ehMesAtual = (calAno === agora.getFullYear() && calMes === agora.getMonth());
      const btnPrev = document.getElementById('calBtnPrevMes');
      if (btnPrev) {
        btnPrev.disabled = ehMesAtual;
        if (ehMesAtual) {
          btnPrev.className = "w-8 h-8 rounded-full bg-slate-800/40 text-slate-600 flex items-center justify-center font-bold text-base cursor-not-allowed";
        } else {
          btnPrev.className = "w-8 h-8 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center font-bold text-base transition shadow-sm cursor-pointer";
        }
      }

      atualizarDisplayDatas();
    }

    function hoverDiaCalendario(diaIso) {
      if (!dataCheckIn || dataCheckOut || diaIso <= dataCheckIn) return;
      dataHover = diaIso;

      const cal = document.getElementById('calendarioAirbnb');
      if (!cal) return;
      const botoes = cal.querySelectorAll('button[data-date]');
      botoes.forEach(b => {
        const d = b.getAttribute('data-date');
        if (!d || b.disabled || d === dataCheckIn) return;
        if (d > dataCheckIn && d <= diaIso) {
          b.classList.add('bg-emerald-500/20', 'text-emerald-300', 'rounded-none');
          b.classList.remove('rounded-full', 'hover:bg-slate-800');
        } else {
          b.classList.remove('bg-emerald-500/20', 'text-emerald-300', 'rounded-none');
          b.classList.add('rounded-full');
        }
      });

      const diffDias = Math.round((new Date(diaIso + 'T12:00:00') - new Date(dataCheckIn + 'T12:00:00')) / 86400000);
      const resumo = document.getElementById('calResumoNoites');
      if (resumo) {
        const txtNoite = diffDias > 1 ? (I18N[idiomaAtual].txt_noites_plur || 'noites') : (I18N[idiomaAtual].txt_noite_sing || 'noite');
        resumo.innerText = `${diffDias} ${txtNoite}`;
      }
    }

    function limparHover() {
      if (dataCheckOut) return;
      dataHover = "";
      const cal = document.getElementById('calendarioAirbnb');
      if (!cal) return;
      const botoes = cal.querySelectorAll('button[data-date]');
      botoes.forEach(b => {
        const d = b.getAttribute('data-date');
        if (d !== dataCheckIn && !b.disabled) {
          b.classList.remove('bg-emerald-500/20', 'text-emerald-300', 'rounded-none');
          b.classList.add('rounded-full');
        }
      });
      atualizarDisplayDatas();
    }

    function selecionarDiaCalendario(diaIso) {
      if (!dataCheckIn || (dataCheckIn && dataCheckOut)) {
        // 1º Clique: define data de entrada
        dataCheckIn = diaIso;
        dataCheckOut = "";
        dataHover = "";
        document.getElementById('inputCheckIn').value = diaIso;
        document.getElementById('inputCheckOut').value = "";
        
        atualizarDisplayDatas();
        renderizarMeses();
      } else if (dataCheckIn && !dataCheckOut) {
        // 2º Clique: define data de saída
        if (diaIso > dataCheckIn) {
          dataCheckOut = diaIso;
          dataHover = "";
          document.getElementById('inputCheckOut').value = diaIso;
          
          atualizarDisplayDatas();
          renderizarMeses();
          
          // Fecha o calendário suavemente e já calcula em tempo real
          setTimeout(() => {
            fecharCalendario();
            consultarDisponibilidade();
          }, 250);
        } else {
          // Se clicou em data anterior ou igual, vira o novo check-in
          dataCheckIn = diaIso;
          dataCheckOut = "";
          dataHover = "";
          document.getElementById('inputCheckIn').value = diaIso;
          document.getElementById('inputCheckOut').value = "";
          atualizarDisplayDatas();
          renderizarMeses();
        }
      }
    }

    function limparDatas() {
      dataCheckIn = "";
      dataCheckOut = "";
      dataHover = "";
      document.getElementById('inputCheckIn').value = "";
      document.getElementById('inputCheckOut').value = "";
      atualizarDisplayDatas();
      renderizarMeses();
      const resultado = document.getElementById('resultadoCotacao');
      if (resultado) resultado.classList.add('hidden');
      const precoCabecalho = document.getElementById('headerPrecoNoite');
      const precoMobile = document.getElementById('mobileBarPreco');
      if (precoCabecalho) {
        precoCabecalho.setAttribute('data-i18n', 'card_ver_valor');
        precoCabecalho.innerText = I18N[idiomaAtual].card_ver_valor;
      }
      if (precoMobile) {
        precoMobile.setAttribute('data-i18n', 'card_ver_valor');
        precoMobile.innerText = I18N[idiomaAtual].card_ver_valor;
      }
      document.getElementById('headerPrecoSufixo')?.classList.add('hidden');
      document.getElementById('mobilePrecoSufixo')?.classList.add('hidden');
    }

    function atualizarDisplayDatas() {
      const inEl = document.getElementById('displayCheckIn');
      const outEl = document.getElementById('displayCheckOut');
      const miniIn = document.getElementById('calMiniCheckIn');
      const miniOut = document.getElementById('calMiniCheckOut');
      const boxIn = document.getElementById('calMiniBoxIn');
      const boxOut = document.getElementById('calMiniBoxOut');
      const mob = document.getElementById('mobileBarDatas');
      const placeholder = I18N[idiomaAtual].txt_inserir_data || "Adicionar data";

      const placeholderDataIn = idiomaAtual === 'en' ? "MM/DD/YYYY" : "DD/MM/AAAA";

      if (inEl) inEl.innerText = dataCheckIn ? formatarDataBr(dataCheckIn) : placeholder;
      if (outEl) outEl.innerText = dataCheckOut ? formatarDataBr(dataCheckOut) : placeholder;
      
      if (miniIn) miniIn.innerText = dataCheckIn ? formatarDataBr(dataCheckIn) : placeholderDataIn;
      if (miniOut) miniOut.innerText = dataCheckOut ? formatarDataBr(dataCheckOut) : placeholder;

      // Realce visual da mini-caixa ativa
      if (boxIn && boxOut) {
        if (!dataCheckIn || (dataCheckIn && dataCheckOut)) {
          boxIn.className = "px-3 py-1.5 min-w-[105px] rounded-l-xl transition border-2 border-emerald-500 bg-emerald-500/10 cursor-pointer";
          boxOut.className = "px-3 py-1.5 min-w-[105px] rounded-r-xl transition border-2 border-transparent cursor-pointer";
        } else {
          boxIn.className = "px-3 py-1.5 min-w-[105px] rounded-l-xl transition border-2 border-transparent cursor-pointer";
          boxOut.className = "px-3 py-1.5 min-w-[105px] rounded-r-xl transition border-2 border-emerald-500 bg-emerald-500/10 cursor-pointer";
        }
      }

      if (mob) {
        if (dataCheckIn && dataCheckOut) {
          const noites = Math.round((new Date(dataCheckOut + 'T12:00:00') - new Date(dataCheckIn + 'T12:00:00')) / 86400000);
          mob.innerText = `${formatarDataBr(dataCheckIn)} - ${formatarDataBr(dataCheckOut)} (${noites}n)`;
        } else if (dataCheckIn) {
          mob.innerText = `${formatarDataBr(dataCheckIn)} - ...`;
        } else {
          mob.innerText = placeholder;
        }
      }

      const resumo = document.getElementById('calResumoNoites');
      if (resumo) {
        if (dataCheckIn && dataCheckOut) {
          const noites = Math.round((new Date(dataCheckOut + 'T12:00:00') - new Date(dataCheckIn + 'T12:00:00')) / 86400000);
          const txtNoite = noites > 1 ? (I18N[idiomaAtual].txt_noites_plur || 'noites') : (I18N[idiomaAtual].txt_noite_sing || 'noite');
          resumo.innerText = `${noites} ${txtNoite} (${formatarDataBr(dataCheckIn)} a ${formatarDataBr(dataCheckOut)})`;
        } else if (dataCheckIn) {
          resumo.innerText = `Check-in: ${formatarDataBr(dataCheckIn)}`;
        } else {
          resumo.innerText = I18N[idiomaAtual].txt_sem_datas || "Nenhuma data selecionada";
        }
      }
    }

    async function carregarDisponibilidadeGeral() {
      if (carregandoDisponibilidadeGeral) return;
      carregandoDisponibilidadeGeral = true;
      try {
        const agora = new Date();
        const ano = agora.getFullYear();
        const mes = String(agora.getMonth() + 1).padStart(2, '0');
        const dia = String(agora.getDate()).padStart(2, '0');
        const hojeIso = `${ano}-${mes}-${dia}`;

        const url = new URL(API_OCUPACAO);
        url.searchParams.set('de', hojeIso);
        url.searchParams.set('dias', '120');

        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 8000);
        const res = await fetch(url.toString(), {
          signal: controller.signal,
          headers: { Accept: 'application/json' }
        });
        clearTimeout(timeoutId);

        if (res.ok) {
          const dados = await res.json().catch(() => ({}));
          if (dados && dados.ok) {
            let totalmenteOcupadas = Array.isArray(dados.totalmenteOcupadas)
              ? dados.totalmenteOcupadas
              : [];
            // Compatibilidade durante a publicação conjunta com o backend antigo.
            if (!totalmenteOcupadas.length && dados.ocupacao && typeof dados.ocupacao === 'object') {
              const listas = Object.values(dados.ocupacao).filter(Array.isArray);
              const contagem = {};
              listas.forEach(lista => lista.forEach(d => { contagem[d] = (contagem[d] || 0) + 1; }));
              totalmenteOcupadas = Object.keys(contagem).filter(d => contagem[d] >= listas.length);
            }
            datasTotalmenteOcupadas = new Set(totalmenteOcupadas);
            renderizarMeses();
          }
        }
      } catch (e) {
        // Falha tolerante: calendário continua navegável
      } finally {
        carregandoDisponibilidadeGeral = false;
      }
    }

    function atualizarHospedes() {
      if (ultimaCotacao && dataCheckIn && dataCheckOut) {
        ultimaCotacao.hospedes = document.getElementById('selectGuests').value;
        renderizarCardDisponibilidade();
      }
    }

    // ========================================================
    // FOCO E NAVEGAÇÃO
    // ========================================================
    function focarCotador() {
      const el = document.getElementById('cotador');
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        el.classList.add('card-pulse-highlight');
        setTimeout(() => el.classList.remove('card-pulse-highlight'), 2500);
      }
      setTimeout(() => abrirCalendario(), 350);
    }

    function compartilharSite() {
      const shareData = {
        title: 'SNT Studios · Hospedagem perto do Aeroporto GRU',
        text: 'Studios privativos modernos com Wi-Fi 600MB, fechadura digital 24h e reserva direta pelo WhatsApp oficial.',
        url: 'https://www.sntstudios.com/'
      };
      if (navigator.share) {
        navigator.share(shareData).catch(() => {});
      } else {
        navigator.clipboard.writeText(shareData.url);
        const btn = document.getElementById('btnShareText');
        if (btn) {
          btn.innerText = idiomaAtual === 'en' ? "Link copied!" : (idiomaAtual === 'es' ? "¡Copiado!" : "Link copiado!");
          setTimeout(() => { btn.innerText = I18N[idiomaAtual].btn_compartilhar || "Compartilhar"; }, 2000);
        }
      }
    }

    // ========================================================
    // ENVIO DE MENSAGEM LIMPA E PROFISSIONAL PARA O WHATSAPP
    // (ADAPTA AO IDIOMA SELECIONADO SEM EMOJIS CORROMPIDOS)
    // ========================================================
    function abrirWhatsAppCotacao(studioChave) {
      const dados = ultimaCotacao || {};
      const inVal = dados.entrada || dataCheckIn;
      const outVal = dados.saida || dataCheckOut;
      const guests = dados.hospedes || document.getElementById('selectGuests').value;
      
      let studioInfo = null;
      if (dados.studios) {
        studioInfo = dados.studios.find(s => {
          const com = STUDIOS_COMERCIAIS[String(s.numero)];
          return com && com.chave === studioChave;
        }) || dados.studios[0];
      }

      const nomeStudio = (studioInfo && STUDIOS_COMERCIAIS[String(studioInfo.numero)]) 
        ? STUDIOS_COMERCIAIS[String(studioInfo.numero)].nome 
        : "Studio Privativo";

      const totalFormatado = studioInfo ? formatarMoeda(studioInfo.totalDireta) : "";

      let linhas = [];

      if (idiomaAtual === 'en') {
        linhas = [
          "Hello! I checked the official SNT Studios website and would like to confirm a direct booking:",
          "",
          "- Check-in: " + formatarDataBr(inVal),
          "- Check-out: " + formatarDataBr(outVal) + (dados.noites ? " (" + dados.noites + " nights)" : ""),
          "- Guests: " + guests + " person" + (Number(guests) > 1 ? "s" : "")
        ];
        if (studioInfo) {
          linhas.push("- Accommodation: " + nomeStudio + " (" + totalFormatado + " total bundled rate)");
        }
        linhas.push("");
        linhas.push("Could you please confirm availability and provide payment details?");
      } else if (idiomaAtual === 'es') {
        linhas = [
          "Hola! Consulte el sitio oficial de SNT Studios y me gustaria confirmar una reserva directa:",
          "",
          "- Check-in: " + formatarDataBr(inVal),
          "- Check-out: " + formatarDataBr(outVal) + (dados.noites ? " (" + dados.noites + " noches)" : ""),
          "- Huespedes: " + guests + " persona" + (Number(guests) > 1 ? "s" : "")
        ];
        if (studioInfo) {
          linhas.push("- Alojamiento: " + nomeStudio + " (" + totalFormatado + " tarifa total consolidada)");
        }
        linhas.push("");
        linhas.push("Podrian confirmar la disponibilidad y los pasos a seguir, por favor?");
      } else {
        linhas = [
          "Ola! Consultei o site oficial do SNT Studios e gostaria de confirmar uma reserva direta:",
          "",
          "- Check-in: " + formatarDataBr(inVal),
          "- Check-out: " + formatarDataBr(outVal) + (dados.noites ? " (" + dados.noites + " noites)" : ""),
          "- Hospedes: " + guests + " pessoa" + (Number(guests) > 1 ? "s" : "")
        ];
        if (studioInfo) {
          linhas.push("- Acomodacao: " + nomeStudio + " (" + totalFormatado + " total da estadia)");
        }
        linhas.push("");
        linhas.push("Poderiam confirmar a disponibilidade e os proximos passos, por favor?");
      }

      window.open("https://api.whatsapp.com/send?phone=551154443110&text=" + encodeURIComponent(linhas.join(String.fromCharCode(10))), '_blank', 'noopener');
    }

    // ========================================================
    // RENDERIZADOR DO RECIBO (VALOR TOTAL EMBUTIDO, NOMES COMERCIAIS)
    // ========================================================
    function renderizarCardDisponibilidade(studioChaveEscolhida) {
      if (!ultimaCotacao || !Array.isArray(ultimaCotacao.studios)) return;
      const dados = ultimaCotacao;
      const resultado = document.getElementById('resultadoCotacao');
      const ordemPreferencia = ['12', '14', '11', '13'];
      
      const livres = dados.studios
        .filter(studio => studio && studio.disponivel && Number.isFinite(Number(studio.totalDireta)))
        .sort((a, b) => ordemPreferencia.indexOf(String(a.numero)) - ordemPreferencia.indexOf(String(b.numero)));

      if (!livres.length) {
        resultado.classList.remove('hidden');
        resultado.innerHTML = `
          <div class="rounded-2xl border border-rose-500/40 bg-rose-500/10 p-4">
            <h4 class="font-bold text-xs text-rose-200">${idiomaAtual === 'en' ? 'Dates not available on calendar' : (idiomaAtual === 'es' ? 'Fechas no disponibles en el calendario' : 'Datas indisponíveis no calendário')}</h4>
            <p class="mt-1 text-[11px] leading-relaxed text-slate-300">
              ${idiomaAtual === 'en' ? 'There are no accommodations free for the selected dates.' : (idiomaAtual === 'es' ? 'No hay estudios disponibles para el período seleccionado.' : 'Não há studios livres para todas as noites selecionadas.')} (${formatarDataBr(dados.entrada)} a ${formatarDataBr(dados.saida)}).
            </p>
            <button type="button" onclick="abrirWhatsAppCotacao('')" class="mt-3 w-full rounded-xl bg-emerald-500 py-3 text-xs font-black text-slate-950 hover:bg-emerald-400 transition shadow-lg shadow-emerald-500/20">
              ${idiomaAtual === 'en' ? 'Inquire alternative dates on WhatsApp' : (idiomaAtual === 'es' ? 'Consultar alternativas por WhatsApp' : 'Consultar alternativas no WhatsApp')}
            </button>
          </div>`;
        return;
      }

      // Se o usuário selecionou uma chave comercial específica, procura ela
      let studio = livres[0];
      if (studioChaveEscolhida) {
        const achado = livres.find(s => {
          const com = STUDIOS_COMERCIAIS[String(s.numero)];
          return com && com.chave === studioChaveEscolhida;
        });
        if (achado) studio = achado;
      }

      const infoComercial = STUDIOS_COMERCIAIS[String(studio.numero)] || {
        chave: 'master',
        nome: 'Studio Amplo A',
        categoria: 'amplos',
        destaque: 'Acomodação privativa completa',
        subtitulo: 'Conforto e privacidade'
      };

      // Atualiza o preço por noite no cabeçalho do card e na barra mobile
      const diariaEfetiva = studio.totalDireta / dados.noites;
      const precoCabecalho = document.getElementById('headerPrecoNoite');
      if (precoCabecalho) {
        precoCabecalho.removeAttribute('data-i18n');
        precoCabecalho.innerText = formatarMoeda(diariaEfetiva);
      }
      const mobilePreco = document.getElementById('mobileBarPreco');
      if (mobilePreco) {
        mobilePreco.removeAttribute('data-i18n');
        mobilePreco.innerText = formatarMoeda(diariaEfetiva);
      }
      document.getElementById('headerPrecoSufixo')?.classList.remove('hidden');
      document.getElementById('mobilePrecoSufixo')?.classList.remove('hidden');

      // Agrupa studios disponíveis por categoria comercial para oferecer escolha de preço
      let cardsOpcoesPreco = '';
      if (livres.length > 1) {
        // Encontra opções distintas (por exemplo se tiver um Amplo e um Standard disponíveis)
        const categoriasVistas = new Set();
        const opcoesDistintas = [];
        livres.forEach(s => {
          const com = STUDIOS_COMERCIAIS[String(s.numero)];
          if (com && !categoriasVistas.has(com.chave)) {
            categoriasVistas.add(com.chave);
            opcoesDistintas.push({ studio: s, info: com });
          }
        });

        if (opcoesDistintas.length > 1) {
          cardsOpcoesPreco = `
            <div class="space-y-1.5 pt-2">
              <span class="text-[11px] text-slate-400 font-bold uppercase tracking-wider block">
                ${idiomaAtual === 'en' ? 'Available Category Options:' : (idiomaAtual === 'es' ? 'Opciones de categoría disponibles:' : 'Opções de categorias disponíveis:')}
              </span>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                ${opcoesDistintas.map(item => `
                  <button type="button" onclick="renderizarCardDisponibilidade('${item.info.chave}')" class="p-2.5 rounded-xl border text-left transition ${item.info.chave === infoComercial.chave ? 'border-emerald-500 bg-emerald-500/15' : 'border-slate-700 bg-slate-800/60 hover:border-slate-600'}">
                    <div class="text-xs font-bold text-white">${item.info.nome}</div>
                    <div class="text-[11px] text-emerald-400 font-extrabold mt-0.5">${formatarMoeda(item.studio.totalDireta)} <span class="text-[10px] text-slate-400 font-normal">total</span></div>
                  </button>
                `).join('')}
              </div>
            </div>`;
        }
      }

      resultado.classList.remove('hidden');
      resultado.innerHTML = `
        <div class="space-y-3.5">
          <!-- CARD DA ACOMODAÇÃO COMERCIALMENTE ALOCADA -->
          <div class="rounded-xl border border-emerald-500/40 bg-emerald-500/10 p-3.5 flex items-center justify-between">
            <div>
              <div class="text-xs font-bold text-white">${escaparHtml(infoComercial.nome)}</div>
              <div class="text-[10px] text-emerald-300 font-medium">${dados.noites} ${dados.noites > 1 ? (idiomaAtual === 'en' ? 'nights' : (idiomaAtual === 'es' ? 'noches' : 'noites')) : (idiomaAtual === 'en' ? 'night' : (idiomaAtual === 'es' ? 'noche' : 'noite'))} · ${dados.hospedes} ${Number(dados.hospedes) > 1 ? (idiomaAtual === 'en' ? 'guests' : (idiomaAtual === 'es' ? 'huéspedes' : 'hóspedes')) : (idiomaAtual === 'en' ? 'guest' : (idiomaAtual === 'es' ? 'huésped' : 'hóspede'))}</div>
            </div>
            <span class="rounded bg-emerald-500/20 px-2 py-0.5 text-[10px] font-bold text-emerald-300 uppercase tracking-wider">
              ${idiomaAtual === 'en' ? 'AVAILABLE' : (idiomaAtual === 'es' ? 'DISPONIBLE' : 'DISPONÍVEL')}
            </span>
          </div>

          ${cardsOpcoesPreco}

          <!-- RECIBO CONSOLIDADO (TOTAL EMBUTIDO, SEM TAXAS SEPARADAS) -->
          <div class="space-y-2 text-xs text-slate-300 pt-1">
            <div class="flex items-center justify-between">
              <span>${dados.noites} ${dados.noites > 1 ? (idiomaAtual === 'en' ? 'nights' : (idiomaAtual === 'es' ? 'noches' : 'noites')) : (idiomaAtual === 'en' ? 'night' : (idiomaAtual === 'es' ? 'noche' : 'noite'))} (${idiomaAtual === 'en' ? 'average' : (idiomaAtual === 'es' ? 'promedio' : 'média')} ${formatarMoeda(diariaEfetiva)}/${idiomaAtual === 'en' ? 'night' : (idiomaAtual === 'es' ? 'noche' : 'noite')})</span>
              <span class="font-medium text-white">${formatarMoeda(studio.totalDireta)}</span>
            </div>
            <div class="pt-2.5 border-t border-slate-700/80 flex items-baseline justify-between text-white">
              <div>
                <span class="text-sm font-black">${idiomaAtual === 'en' ? 'Total Price' : (idiomaAtual === 'es' ? 'Precio Total Final' : 'Valor Total da Estadia')}</span>
                <p class="text-[10px] text-slate-400">${idiomaAtual === 'en' ? 'Bundled price, zero extra fees' : (idiomaAtual === 'es' ? 'Precio final sin costos ocultos' : 'Valor final consolidado sem taxas ocultas')}</p>
              </div>
              <span class="text-xl font-black text-emerald-400">${formatarMoeda(studio.totalDireta)}</span>
            </div>
          </div>

          <!-- BOTÃO DE AÇÃO WHATSAPP OFICIAL -->
          <button type="button" onclick="abrirWhatsAppCotacao('${infoComercial.chave}')" class="w-full mt-2 bg-emerald-500 hover:bg-emerald-400 active:scale-[0.99] text-slate-950 font-black py-3.5 px-4 rounded-xl text-xs uppercase tracking-wider transition shadow-lg shadow-emerald-500/25 flex items-center justify-center gap-2">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824zm-3.423-14.416c-6.627 0-12 5.373-12 12 0 2.159.57 4.184 1.564 5.938l-1.664 6.086 6.257-1.64c1.706.924 3.659 1.45 5.743 1.45 6.627 0 12-5.373 12-12 0-6.627-5.373-12-12-12z"/></svg>
            <span>${idiomaAtual === 'en' ? 'Reserve via WhatsApp' : (idiomaAtual === 'es' ? 'Reservar por WhatsApp' : 'Reservar no WhatsApp')}</span>
          </button>

          <p class="text-[10px] text-center text-slate-400">
            🔒 ${idiomaAtual === 'en' ? 'Your dates are locked directly with our team upon message confirmation.' : (idiomaAtual === 'es' ? 'Su reserva se bloquea directamente con nuestro equipo al confirmar.' : 'Sua reserva é bloqueada diretamente com nossa equipe no atendimento oficial.')}
          </p>
        </div>`;
    }

    // ========================================================
    // CONSULTA DE DISPONIBILIDADE EM TEMPO REAL
    // ========================================================
    async function consultarDisponibilidade() {
      const inVal = document.getElementById('inputCheckIn').value || dataCheckIn;
      const outVal = document.getElementById('inputCheckOut').value || dataCheckOut;
      const guests = document.getElementById('selectGuests').value;
      const resultado = document.getElementById('resultadoCotacao');
      const botao = document.getElementById('btnConsultar');

      if (!inVal || !outVal) {
        resultado.classList.remove('hidden');
        resultado.innerHTML = `<div class="rounded-xl border border-amber-500/40 bg-amber-500/10 p-3.5 text-xs text-amber-200">${idiomaAtual === 'en' ? 'Please select check-in and checkout dates above.' : (idiomaAtual === 'es' ? 'Por favor, seleccione las fechas de entrada y salida arriba.' : 'Selecione as datas de check-in e checkout para ver o valor consolidado.')}</div>`;
        abrirCalendario();
        return;
      }

      const noites = Math.round((new Date(outVal + 'T12:00:00') - new Date(inVal + 'T12:00:00')) / 86400000);
      if (noites < 1 || noites > 120) {
        resultado.classList.remove('hidden');
        resultado.innerHTML = `<div class="rounded-xl border border-rose-500/40 bg-rose-500/10 p-3.5 text-xs text-rose-200">${idiomaAtual === 'en' ? 'Checkout date must be after check-in.' : (idiomaAtual === 'es' ? 'La fecha de salida debe ser posterior a la de entrada.' : 'O checkout deve ser posterior ao check-in e a estadia pode ter no máximo 120 noites.')}</div>`;
        return;
      }

      resultado.classList.remove('hidden');
      resultado.innerHTML = `<div class="flex items-center justify-center gap-3 rounded-xl border border-slate-700 bg-slate-900/90 p-4 text-xs text-emerald-300"><span class="h-4 w-4 animate-spin rounded-full border-2 border-emerald-400 border-t-transparent"></span>${idiomaAtual === 'en' ? 'Checking real-time calendar availability...' : (idiomaAtual === 'es' ? 'Consultando disponibilidad en tiempo real...' : 'Consultando disponibilidade e tarifas em tempo real...')}</div>`;
      if (botao) botao.disabled = true;

      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 10000);

      try {
        const url = new URL(API_COTACAO);
        url.searchParams.set('entrada', inVal);
        url.searchParams.set('saida', outVal);
        const resposta = await fetch(url.toString(), {
          signal: controller.signal,
          headers: { Accept: 'application/json' }
        });
        const dados = await resposta.json().catch(() => ({}));
        if (!resposta.ok || !dados.ok || !Array.isArray(dados.studios)) {
          throw new Error(dados.erro || 'Não foi possível consultar o calendário.');
        }

        ultimaCotacao = { ...dados, hospedes: guests };
        renderizarCardDisponibilidade();
      } catch (erro) {
        ultimaCotacao = { entrada: inVal, saida: outVal, hospedes: guests, studios: [] };
        resultado.innerHTML = `
          <div class="rounded-xl border border-amber-500/40 bg-amber-500/10 p-4">
            <h4 class="font-bold text-xs text-amber-200">${idiomaAtual === 'en' ? 'Direct inquiry available' : (idiomaAtual === 'es' ? 'Consulta directa disponible' : 'Consulta direta disponível')}</h4>
            <p class="mt-1 text-[11px] leading-relaxed text-slate-300">${idiomaAtual === 'en' ? 'To verify instant dates and rates, continue directly on WhatsApp.' : (idiomaAtual === 'es' ? 'Para confirmar disponibilidad exacta, continúe directamente en WhatsApp.' : 'Para não mostrar valor desatualizado, a confirmação segue diretamente com nossa equipe.')}</p>
            <button type="button" onclick="abrirWhatsAppCotacao('')" class="mt-3 w-full rounded-lg bg-emerald-500 py-2.5 text-xs font-black text-slate-950 hover:bg-emerald-400 transition">
              ${idiomaAtual === 'en' ? 'Check on WhatsApp' : (idiomaAtual === 'es' ? 'Consultar en WhatsApp' : 'Consultar no WhatsApp')}
            </button>
          </div>`;
      } finally {
        clearTimeout(timeoutId);
        if (botao) botao.disabled = false;
      }
    }

    function copiarEndereco() {
      const txt = "Avenida Aguanil, 51 - Cidade Seródio - Guarulhos/SP";
      navigator.clipboard.writeText(txt);
      const btn = document.getElementById('btnCopiarEnd');
      btn.innerText = idiomaAtual === 'en' ? "✓ Copied!" : (idiomaAtual === 'es' ? "✓ ¡Copiado!" : "✓ Copiado!");
      setTimeout(() => {
        btn.innerText = idiomaAtual === 'en' ? "Copy" : (idiomaAtual === 'es' ? "Copiar" : "Copiar");
      }, 2000);
    }

    // ========================================================
    // FILTRAGEM DE CATEGORIAS
    // ========================================================
    function filtrarStudios(tipo) {
      const cards = document.querySelectorAll('.card-studio');
      const btnTodos = document.getElementById('btnFiltroTodos');
      const btnAmplos = document.getElementById('btnFiltroAmplos');
      const btnCompactos = document.getElementById('btnFiltroCompactos');

      [btnTodos, btnAmplos, btnCompactos].forEach(b => {
        b.className = "px-4 py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:text-white transition";
      });

      if (tipo === 'todos') {
        btnTodos.className = "px-4 py-2 rounded-xl text-xs font-bold bg-emerald-500 text-slate-950 transition";
      } else if (tipo === 'amplos') {
        btnAmplos.className = "px-4 py-2 rounded-xl text-xs font-bold bg-emerald-500 text-slate-950 transition";
      } else {
        btnCompactos.className = "px-4 py-2 rounded-xl text-xs font-bold bg-emerald-500 text-slate-950 transition";
      }

      cards.forEach(c => {
        if (tipo === 'todos' || c.getAttribute('data-tipo') === tipo) {
          c.classList.remove('hidden');
        } else {
          c.classList.add('hidden');
        }
      });
    }

    // ========================================================
    // MODAL DE GALERIA DE FOTOS (LIGHTBOX COM NOMES COMERCIAIS)
    // ========================================================
    const galeriaFotos = {
      'master': [
        'assets/fotos/20251030_162521(1).webp',
        'assets/fotos/20251030_162403.webp',
        'assets/fotos/20251030_162350.webp',
        'assets/fotos/20251030_162606(1).webp',
        'assets/fotos/20251030_163823.webp'
      ],
      'executivo': [
        'assets/fotos/20251030_164004.webp',
        'assets/fotos/20251030_162615(1).webp',
        'assets/fotos/20251030_164033.webp',
        'assets/fotos/20251030_164106.webp',
        'assets/fotos/20251030_163810.webp'
      ],
      'smart': [
        'assets/fotos/20251030_143554.webp',
        'assets/fotos/20251030_143603.webp',
        'assets/fotos/20251030_143653.webp',
        'assets/fotos/20251030_143812.webp',
        'assets/fotos/20251030_144426.webp'
      ],
      'cozy': [
        'assets/fotos/20251030_144024.webp',
        'assets/fotos/20251030_144035.webp',
        'assets/fotos/20251030_144400.webp',
        'assets/fotos/20251030_144616.webp',
        'assets/fotos/20251030_144436.webp'
      ],
      'todas': [
        'assets/fotos/20251030_162521(1).webp',
        'assets/fotos/20251030_162403.webp',
        'assets/fotos/20251030_162350.webp',
        'assets/fotos/20251030_162606(1).webp',
        'assets/fotos/20251030_163823.webp',
        'assets/fotos/20251030_164004.webp',
        'assets/fotos/20251030_162615(1).webp',
        'assets/fotos/20251030_164033.webp',
        'assets/fotos/20251030_164106.webp',
        'assets/fotos/20251030_163810.webp',
        'assets/fotos/20251030_143554.webp',
        'assets/fotos/20251030_143603.webp',
        'assets/fotos/20251030_143653.webp',
        'assets/fotos/20251030_143812.webp',
        'assets/fotos/20251030_144426.webp',
        'assets/fotos/20251030_144024.webp',
        'assets/fotos/20251030_144035.webp',
        'assets/fotos/20251030_144400.webp',
        'assets/fotos/20251030_144616.webp',
        'assets/fotos/20251030_144436.webp'
      ]
    };

    let galeriaAtualLista = [];
    let galeriaFotoIdx = 0;

    function abrirGaleria(categoriaChave) {
      galeriaAtualLista = galeriaFotos[categoriaChave] || galeriaFotos['todas'] || galeriaFotos['master'];
      galeriaFotoIdx = 0;
      
      const titulos = {
        'master': 'Studio Amplo A (O Maior Studio · Cama Queen & Cortinas)',
        'executivo': 'Studio Amplo B (Grande & Sofisticado)',
        'smart': 'Studio Compacto A (Compacto & Silencioso)',
        'cozy': 'Studio Compacto B (Compacto & Acolhedor)',
        'todas': (idiomaAtual === 'en' ? 'SNT Studios · All 20 Authentic Photos' : (idiomaAtual === 'es' ? 'SNT Studios · Las 20 Fotos Reales' : 'SNT Studios · Todas as 20 Fotos Reais'))
      };
      
      document.getElementById('modalGaleriaTitulo').innerText = titulos[categoriaChave] || 'Fotos Reais das Acomodações';
      document.getElementById('modalGaleriaSubtitulo').innerText = "Fotos 100% autênticas do SNT Studios";
      
      atualizarFotoGaleria();
      renderizarMiniaturasGaleria();
      document.getElementById('modalGaleria').classList.remove('hidden');
      document.body.classList.add('overflow-hidden');
    }

    function fecharGaleria() {
      document.getElementById('modalGaleria').classList.add('hidden');
      document.body.classList.remove('overflow-hidden');
    }

    function atualizarFotoGaleria() {
      const img = document.getElementById('modalFotoPrincipal');
      img.src = galeriaAtualLista[galeriaFotoIdx];
      document.getElementById('modalContadorFoto').innerText = `${galeriaFotoIdx + 1} / ${galeriaAtualLista.length}`;
      renderizarMiniaturasGaleria();
    }

    function proximaFotoGaleria() {
      galeriaFotoIdx = (galeriaFotoIdx + 1) % galeriaAtualLista.length;
      atualizarFotoGaleria();
    }

    function anteriorFotoGaleria() {
      galeriaFotoIdx = (galeriaFotoIdx - 1 + galeriaAtualLista.length) % galeriaAtualLista.length;
      atualizarFotoGaleria();
    }

    function renderizarMiniaturasGaleria() {
      const container = document.getElementById('modalMiniaturas');
      container.innerHTML = '';
      galeriaAtualLista.forEach((f, idx) => {
        const img = document.createElement('img');
        img.src = f;
        img.className = `w-14 h-14 object-cover rounded-lg cursor-pointer border-2 transition ${idx === galeriaFotoIdx ? 'border-emerald-500 scale-105' : 'border-transparent opacity-60 hover:opacity-100'}`;
        img.onclick = () => {
          galeriaFotoIdx = idx;
          atualizarFotoGaleria();
        };
        container.appendChild(img);
      });
    }

    // Atalho ESC para fechar galeria e calendário
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        fecharGaleria();
        fecharCalendario();
      }
    });

    // Fecha calendário ao clicar fora
    document.addEventListener('click', (e) => {
      const cal = document.getElementById('calendarioAirbnb');
      const box = document.getElementById('airbnbDateBox');
      if (cal && !cal.classList.contains('hidden')) {
        if (!cal.contains(e.target) && !box.contains(e.target)) {
          fecharCalendario();
        }
      }
    });

    // Inicialização ao carregar página
    document.addEventListener('DOMContentLoaded', () => {
      carregarDisponibilidadeGeral();
      if (idiomaAtual !== 'pt') {
        trocarIdioma(idiomaAtual);
      } else {
        renderizarMeses();
        atualizarDisplayDatas();
      }
    });
  </script>

</body>
</html>
'''

raiz = Path(__file__).resolve().parent
(raiz / 'index.html').write_text(site_code, encoding='utf-8')

print("Generated index.html with Airbnb 2-tap range picker, commercial studio names, bundled rates, and multi-language support (PT/EN/ES).")
