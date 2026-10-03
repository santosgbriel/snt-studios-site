# -*- coding: utf-8 -*-
from pathlib import Path

"""
Site oficial do SNT Studios com experiência Airbnb (Listing Reserve Widget).
Mantém: Fotos reais WebP, Galeria Lightbox, Google Maps, 600mb internet,
especificações de tipologia (cortinas vs janela superior), tabela comparativa,
e consulta direta de disponibilidade em tempo real no Smoobu com handoff limpo para o WhatsApp.
"""

site_code = '''<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SNT Studios · Hospitalidade & Hospedagem Próximo ao Aeroporto de Guarulhos (GRU)</title>
  
  <!-- SEO & Social Sharing -->
  <meta name="description" content="Studios modernos, privativos e confortáveis em Guarulhos, a apenas 10-15 min do Aeroporto GRU. Internet fibra 600MB, fechadura eletrônica 24h, cozinha compacta e reserva direta com 10% de desconto.">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="https://www.sntstudios.com/">
  <meta property="og:title" content="SNT Studios · Hospedagem Moderna ao Lado do Aeroporto GRU">
  <meta property="og:description" content="Reserve direto com 10% de desconto no WhatsApp oficial. Studios privativos com Wi-Fi 600MB, fechadura digital 24h e cozinha completa.">
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
      background: rgba(7, 11, 20, 0.88);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }
    .glass-card {
      background: rgba(15, 23, 42, 0.78);
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
    input[type="date"]::-webkit-calendar-picker-indicator {
      filter: invert(1);
      opacity: 0.65;
      cursor: pointer;
    }
    input[type="date"]::-webkit-calendar-picker-indicator:hover {
      opacity: 1;
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
      <a href="#" class="flex items-center gap-3 group">
        <img src="assets/snt-empreendimentos-horizontal-branco.png" alt="SNT Studios" class="h-9 sm:h-11 w-auto object-contain transition transform group-hover:scale-[1.02]">
        <span class="hidden md:inline-block bg-emerald-500/10 text-emerald-400 text-[11px] font-bold px-2.5 py-0.5 rounded-full border border-emerald-500/20">
          STUDIOS BOUTIQUE
        </span>
      </a>

      <!-- MENU DESKTOP -->
      <div class="hidden lg:flex items-center gap-8 text-sm font-medium text-slate-300">
        <a href="#inicio" class="hover:text-emerald-400 transition">Início</a>
        <a href="#cotador" class="hover:text-emerald-400 transition">Disponibilidade</a>
        <a href="#studios" class="hover:text-emerald-400 transition">Nossos Studios</a>
        <a href="#comodidades" class="hover:text-emerald-400 transition">Comodidades</a>
        <a href="#localizacao" class="hover:text-emerald-400 transition">Localização</a>
        <a href="#faq" class="hover:text-emerald-400 transition">Dúvidas</a>
      </div>

      <!-- BOTÃO DIRETO WHATSAPP -->
      <div class="flex items-center gap-3">
        <a href="https://api.whatsapp.com/send?phone=551154443110" target="_blank" rel="noopener noreferrer" class="hidden sm:inline-flex items-center gap-2 text-xs font-semibold text-slate-300 hover:text-emerald-400 transition px-3 py-2 rounded-lg bg-slate-900 border border-slate-800">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>(11) 5444-3110</span>
        </a>
        <a href="https://api.whatsapp.com/send?phone=551154443110&text=Ola%21%20Gostaria%20de%20consultar%20uma%20reserva%20direta%20no%20SNT%20Studios%20com%2010%25%20de%20desconto." target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold px-4 sm:px-5 py-2.5 rounded-xl text-xs sm:text-sm shadow-lg shadow-emerald-500/20 transition transform hover:-translate-y-0.5">
          <span>Reservar no WhatsApp</span>
          <span class="bg-slate-950/20 text-slate-950 text-[10px] px-1.5 py-0.5 rounded font-black">-10%</span>
        </a>
      </div>

    </div>
  </nav>

  <!-- LISTING AIRBNB SHOWCASE (O MODELO DE QUANDO O HÓSPEDE JÁ ESTÁ DENTRO DO IMÓVEL) -->
  <section id="inicio" class="relative pt-28 pb-16 lg:pt-36 lg:pb-24 hero-glow overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

      <!-- CABEÇALHO DO ANÚNCIO (ESTILO LISTING AIRBNB) -->
      <div class="mb-6 space-y-2.5">
        <div class="flex flex-wrap items-center gap-2">
          <span class="inline-flex items-center gap-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 px-3 py-1 text-xs font-bold text-emerald-400">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            Hospedagem Privativa em Guarulhos · Aeroporto GRU
          </span>
          <span class="inline-flex items-center gap-1 rounded-full bg-amber-400/10 border border-amber-400/30 px-3 py-1 text-xs font-bold text-amber-300">
            ★ 4.98 · Preferido dos hóspedes
          </span>
          <span class="inline-flex items-center gap-1 rounded-full bg-slate-800 border border-slate-700 px-3 py-1 text-xs font-semibold text-slate-300">
            🛡️ 10% OFF Reserva Direta Garantida
          </span>
        </div>

        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white tracking-tight leading-tight">
          SNT Studios · Studios Privativos a 10 min do Aeroporto GRU
        </h1>

        <!-- BARRA SUB-HEADER AIRBNB -->
        <div class="flex flex-wrap items-center justify-between gap-3 text-xs sm:text-sm text-slate-300 pt-1 pb-4 border-b border-slate-800/80">
          <div class="flex flex-wrap items-center gap-2">
            <span class="font-black text-amber-400 flex items-center gap-1">★ 4.98</span>
            <span class="text-slate-500">·</span>
            <a href="#studios" class="underline underline-offset-4 hover:text-white font-medium">42 avaliações reais de hóspedes</a>
            <span class="text-slate-500">·</span>
            <span class="text-slate-300 font-semibold">🏆 Superhost SNT</span>
            <span class="text-slate-500">·</span>
            <a href="#localizacao" class="underline underline-offset-4 hover:text-emerald-400 text-slate-400">Avenida Aguanil, 51 · Seródio, Guarulhos - SP</a>
          </div>
          <div class="flex items-center gap-3">
            <button type="button" onclick="compartilharSite()" class="flex items-center gap-1.5 text-xs text-slate-400 hover:text-white transition">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/></svg>
              <span id="btnShareText">Compartilhar</span>
            </button>
          </div>
        </div>
      </div>

      <!-- GRADE DE FOTOS AIRBNB (5 FOTOS COM A PRINCIPAL EM DESTAQUE) -->
      <div class="relative rounded-3xl overflow-hidden border border-slate-800 shadow-2xl mb-12 group">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-2 h-[340px] sm:h-[420px] lg:h-[480px]">
          <!-- Foto Principal Grande (Esquerda: 2 colunas no desktop) -->
          <div class="md:col-span-2 relative overflow-hidden bg-slate-950 cursor-pointer" onclick="abrirGaleria('12')">
            <img src="assets/fotos/20251030_162521(1).webp" alt="Studio 12 - Master King" class="w-full h-full object-cover group-hover:scale-[1.02] transition duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent flex flex-col justify-end p-5">
              <span class="bg-amber-400 text-slate-950 text-[10px] font-black px-2.5 py-0.5 rounded shadow w-max mb-1">🏆 STUDIO 12 · MASTER KING</span>
              <span class="text-white text-sm font-bold">O maior studio · Ampla iluminação e cortinas elegantes</span>
            </div>
          </div>
          <!-- Coluna 2 (2 fotos empilhadas) -->
          <div class="hidden md:grid grid-rows-2 gap-2">
            <div class="relative overflow-hidden bg-slate-950 cursor-pointer" onclick="abrirGaleria('14')">
              <img src="assets/fotos/20251030_164004.webp" alt="Studio 14 - Executivo" class="w-full h-full object-cover hover:scale-105 transition duration-500">
              <div class="absolute bottom-2 left-2 bg-slate-950/80 backdrop-blur px-2 py-0.5 rounded text-[10px] font-bold text-teal-300 border border-slate-700">Studio 14 Executivo</div>
            </div>
            <div class="relative overflow-hidden bg-slate-950 cursor-pointer" onclick="abrirGaleria('12')">
              <img src="assets/fotos/20251030_144616.webp" alt="Cozinha Compacta Completa" class="w-full h-full object-cover hover:scale-105 transition duration-500">
              <div class="absolute bottom-2 left-2 bg-slate-950/80 backdrop-blur px-2 py-0.5 rounded text-[10px] font-bold text-emerald-300 border border-slate-700">Cozinha Compacta</div>
            </div>
          </div>
          <!-- Coluna 3 (2 fotos empilhadas) -->
          <div class="hidden md:grid grid-rows-2 gap-2">
            <div class="relative overflow-hidden bg-slate-950 cursor-pointer" onclick="abrirGaleria('11')">
              <img src="assets/fotos/20251030_143554.webp" alt="Studio 11 - Standard Smart" class="w-full h-full object-cover hover:scale-105 transition duration-500">
              <div class="absolute bottom-2 left-2 bg-slate-950/80 backdrop-blur px-2 py-0.5 rounded text-[10px] font-bold text-slate-300 border border-slate-700">Studio 11 Smart</div>
            </div>
            <div class="relative overflow-hidden bg-slate-950 cursor-pointer" onclick="abrirGaleria('13')">
              <img src="assets/fotos/20251030_144024.webp" alt="Studio 13 - Standard Cozy" class="w-full h-full object-cover hover:scale-105 transition duration-500">
              <div class="absolute bottom-2 left-2 bg-slate-950/80 backdrop-blur px-2 py-0.5 rounded text-[10px] font-bold text-slate-300 border border-slate-700">Studio 13 Cozy</div>
            </div>
          </div>
        </div>
        <!-- Botão no Canto Inferior Direito: Mostrar todas as fotos -->
        <button type="button" onclick="abrirGaleria('12')" class="absolute bottom-4 right-4 bg-slate-950/90 hover:bg-white hover:text-slate-950 backdrop-blur text-white text-xs font-extrabold px-4 py-2.5 rounded-xl border border-slate-700 transition flex items-center gap-2 shadow-2xl">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
          <span>Mostrar todas as 20 fotos</span>
        </button>
      </div>

      <!-- GRID PRINCIPAL (COLUNA ESQUERDA: DETALHES | COLUNA DIREITA: STICKY AIRBNB RESERVE BOX) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start">
        
        <!-- COLUNA ESQUERDA: DETALHES DO ESPAÇO (7 COLUNAS) -->
        <div class="lg:col-span-7 space-y-8">
          
          <!-- RESUMO DO ESPAÇO -->
          <div class="flex items-start justify-between pb-6 border-b border-slate-800">
            <div>
              <h2 class="text-xl sm:text-2xl font-bold text-white">Studio privativo inteiro · Hospedagem SNT</h2>
              <p class="text-xs sm:text-sm text-slate-400 mt-1">Até 2 hóspedes · 1 cama queen ou casal · 1 banheiro privativo · Cozinha privativa compacta</p>
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
                <h3 class="text-sm font-bold text-white">Auto check-in 24h via fechadura digital</h3>
                <p class="text-xs text-slate-400 mt-0.5">Acesse o complexo e seu studio com senha individual a qualquer hora da noite ou madrugada, sem precisar de chaves físicas.</p>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-6 text-xl text-emerald-400 shrink-0">⚡</div>
              <div>
                <h3 class="text-sm font-bold text-white">Wi-Fi fibra de 600 Mbps dedicado</h3>
                <p class="text-xs text-slate-400 mt-0.5">Internet ultra-veloz testada para chamadas de vídeo, reuniões executivas e streaming 4K sem interrupções.</p>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-6 text-xl text-emerald-400 shrink-0">🍳</div>
              <div>
                <h3 class="text-sm font-bold text-white">Cozinha privativa equipada</h3>
                <p class="text-xs text-slate-400 mt-0.5">Equipada com frigobar, micro-ondas, cooktop, cafeteira Dolce Gusto, louças e talheres para sua conveniência.</p>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-6 text-xl text-emerald-400 shrink-0">✈️</div>
              <div>
                <h3 class="text-sm font-bold text-white">10 a 15 minutos do Aeroporto de Guarulhos (GRU)</h3>
                <p class="text-xs text-slate-400 mt-0.5">Localização estratégica com rota rápida para os Terminais 1, 2 e 3 por aplicativo, ideal para conexões e escalas.</p>
              </div>
            </div>
          </div>

          <!-- DESCRIÇÃO DO ESPAÇO E AS DUAS TIPOLOGIAS -->
          <div class="space-y-4 pb-6 border-b border-slate-800">
            <h3 class="text-base font-bold text-white">Sobre o espaço</h3>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              O <strong>SNT Studios</strong> foi projetado para oferecer o máximo em privacidade, silêncio e praticidade. Cada uma das 4 unidades é inteiramente privativa, com banheiro exclusivo, bancada e ambiente climatizado.
            </p>
            
            <div class="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 space-y-3">
              <h4 class="text-xs font-bold uppercase tracking-wider text-emerald-400">Nossas 2 Tipologias de Studios</h4>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div class="p-3 rounded-xl bg-slate-800/60 border border-slate-700/60">
                  <span class="font-bold text-white block mb-1">Studios Maiores (12 e 14)</span>
                  <p class="text-slate-400 text-[11px]">Janela ampla com cortinas elegantes, mais espaço de circulação e bancada ampla de trabalho.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-800/60 border border-slate-700/60">
                  <span class="font-bold text-white block mb-1">Studios Compactos (11 e 13)</span>
                  <p class="text-slate-400 text-[11px]">Janelinha superior voltada para silêncio e discrição máxima. Planta inteligente e econômica.</p>
                </div>
              </div>
              <p class="text-[11px] text-slate-400">
                <em>Ao selecionar suas datas ao lado, o sistema aloca e garante automaticamente a melhor acomodação disponível no calendário oficial.</em>
              </p>
            </div>
          </div>

          <!-- O QUE ESSE LUGAR OFERECE (COMODIDADES AIRBNB) -->
          <div class="space-y-4 pb-6 border-b border-slate-800">
            <h3 class="text-base font-bold text-white">O que esse lugar oferece</h3>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 text-xs text-slate-300">
              <div class="flex items-center gap-2.5"><span>⚡</span><span>Wi-Fi Fibra 600 Mbps</span></div>
              <div class="flex items-center gap-2.5"><span>🔑</span><span>Fechadura digital 24h</span></div>
              <div class="flex items-center gap-2.5"><span>📺</span><span>Smart TV com Streaming</span></div>
              <div class="flex items-center gap-2.5"><span>🍳</span><span>Cozinha com Cooktop</span></div>
              <div class="flex items-center gap-2.5"><span>❄️</span><span>Ar-condicionado / Ventilador</span></div>
              <div class="flex items-center gap-2.5"><span>☕</span><span>Cafeteira Dolce Gusto</span></div>
              <div class="flex items-center gap-2.5"><span>🚿</span><span>Banho quente pressurizado</span></div>
              <div class="flex items-center gap-2.5"><span>🧺</span><span>Enxoval higienizado</span></div>
              <div class="flex items-center gap-2.5"><span>💻</span><span>Bancada para notebook</span></div>
              <div class="flex items-center gap-2.5"><span>🛡️</span><span>Câmeras nas áreas comuns</span></div>
              <div class="flex items-center gap-2.5"><span>🚗</span><span>Fácil acesso para Uber/99</span></div>
              <div class="flex items-center gap-2.5"><span>🧊</span><span>Frigobar e Micro-ondas</span></div>
            </div>
          </div>

          <!-- REGRAS DA CASA RÁPIDAS -->
          <div class="space-y-2 text-xs text-slate-400">
            <div class="flex items-center gap-3">
              <span class="font-bold text-white">Check-in:</span>
              <span>A partir das 15:00 (Acesso autônomo 24h via código)</span>
            </div>
            <div class="flex items-center gap-3">
              <span class="font-bold text-white">Check-out:</span>
              <span>Até as 11:00</span>
            </div>
            <div class="flex items-center gap-3">
              <span class="font-bold text-white">Política de Silêncio:</span>
              <span>Respeito ao descanso dos demais hóspedes a partir das 22h</span>
            </div>
          </div>

        </div>

        <!-- COLUNA DIREITA: WIDGET DE RESERVA AIRBNB STICKY (5 COLUNAS) -->
        <div class="lg:col-span-5">
          <div class="lg:sticky lg:top-28">
            <div id="cotador" class="glass-card rounded-3xl p-6 sm:p-7 shadow-2xl border border-slate-700/80 hover:border-emerald-500/30 transition duration-300 relative">
              
              <!-- CABEÇALHO DO CARD: PREÇO POR NOITE E AVALIAÇÕES -->
              <div class="flex items-baseline justify-between mb-5">
                <div>
                  <span class="text-2xl sm:text-3xl font-black text-white" id="headerPrecoNoite">R$ 159</span>
                  <span class="text-xs sm:text-sm text-slate-400 font-medium"> / noite</span>
                  <span class="ml-2 inline-flex items-center gap-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 px-2 py-0.5 text-[10px] font-bold text-emerald-400">10% OFF DIRETO</span>
                </div>
                <div class="flex items-center gap-1.5 text-xs">
                  <span class="text-amber-400 font-bold">★ 4.98</span>
                  <span class="text-slate-500">·</span>
                  <span class="text-slate-300 font-medium underline underline-offset-2">Hóspedes reais</span>
                </div>
              </div>

              <!-- O BOXED SELECTOR AIRBNB (CHECK-IN / CHECKOUT / HÓSPEDES) -->
              <form id="formCotador" onsubmit="event.preventDefault(); consultarDisponibilidade();">
                <div class="border border-slate-700 rounded-2xl bg-slate-900/90 overflow-hidden shadow-inner focus-within:ring-2 focus-within:ring-emerald-500/60 focus-within:border-emerald-500/60 transition">
                  
                  <!-- LINHA SUPERIOR: CHECK-IN E CHECKOUT DIVIDIDOS AO MEIO -->
                  <div class="grid grid-cols-2 divide-x divide-slate-700">
                    <label for="inputCheckIn" class="block p-3 sm:p-3.5 hover:bg-slate-800/40 cursor-pointer transition">
                      <span class="block text-[10px] font-black uppercase tracking-wider text-slate-400">CHECK-IN</span>
                      <input type="date" id="inputCheckIn" class="w-full bg-transparent text-xs sm:text-sm font-semibold text-white focus:outline-none cursor-pointer mt-0.5" required>
                    </label>
                    <label for="inputCheckOut" class="block p-3 sm:p-3.5 hover:bg-slate-800/40 cursor-pointer transition">
                      <span class="block text-[10px] font-black uppercase tracking-wider text-slate-400">CHECKOUT</span>
                      <input type="date" id="inputCheckOut" class="w-full bg-transparent text-xs sm:text-sm font-semibold text-white focus:outline-none cursor-pointer mt-0.5" required>
                    </label>
                  </div>

                  <!-- LINHA INFERIOR: HÓSPEDES LARGURA TOTAL -->
                  <div class="border-t border-slate-700 p-3 sm:p-3.5 hover:bg-slate-800/40 transition">
                    <label for="selectGuests" class="block text-[10px] font-black uppercase tracking-wider text-slate-400 cursor-pointer">HÓSPEDES</label>
                    <div class="relative mt-0.5">
                      <select id="selectGuests" class="w-full bg-transparent text-xs sm:text-sm font-semibold text-white focus:outline-none cursor-pointer appearance-none pr-8">
                        <option value="1" class="bg-slate-900 text-white">1 hóspede</option>
                        <option value="2" class="bg-slate-900 text-white" selected>2 hóspedes (Casal)</option>
                      </select>
                      <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center text-slate-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                      </div>
                    </div>
                  </div>

                </div>

                <!-- BOTÃO DE AÇÃO PRINCIPAL AIRBNB -->
                <button id="btnConsultar" type="submit" class="w-full mt-4 bg-emerald-500 hover:bg-emerald-400 active:scale-[0.99] text-slate-950 font-black py-3.5 px-4 rounded-xl text-xs sm:text-sm uppercase tracking-wider transition-all duration-200 shadow-xl shadow-emerald-500/20 flex items-center justify-center gap-2">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="m21 21-4.35-4.35m2.1-5.4a7.5 7.5 0 1 1-15 0 7.5 7.5 0 0 1 15 0Z"/></svg>
                  <span id="btnConsultarTexto">Conferir disponibilidade</span>
                </button>

                <!-- FRASE CLÁSSICA DO AIRBNB -->
                <p class="text-center text-[11px] sm:text-xs text-slate-400 mt-2.5 font-medium">
                  Você ainda não será cobrado
                </p>

              </form>

              <!-- RESULTADO DA COTAÇÃO & DETALHAMENTO DE PREÇO (AIRBNB STYLE) -->
              <div id="resultadoCotacao" class="hidden mt-4 pt-4 border-t border-slate-800" aria-live="polite"></div>

              <!-- DIFERENCIAIS DA RESERVA DIRETA NO CARD -->
              <div class="mt-5 pt-4 border-t border-slate-800/80 space-y-2 text-xs text-slate-400">
                <div class="flex items-center justify-between text-emerald-400 font-medium">
                  <span class="flex items-center gap-1.5">
                    <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                    Desconto Direto de 10%
                  </span>
                  <span class="font-bold">Garantido</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="flex items-center gap-1.5">
                    <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                    Sem taxas de serviço de terceiros
                  </span>
                  <span class="text-slate-300">Economia real</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="flex items-center gap-1.5">
                    <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                    Sincronização ao vivo Smoobu
                  </span>
                  <span class="text-slate-300">24 horas</span>
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
          <h4 class="text-xs font-bold text-white">Wi-Fi 600 Mbps</h4>
          <p class="text-[11px] text-slate-400">Fibra óptica dedicada ultra-rápida</p>
        </div>

        <div class="glass-card p-3.5 rounded-xl text-center space-y-1">
          <div class="text-xl">🔑</div>
          <h4 class="text-xs font-bold text-white">Self Check-in 24h</h4>
          <p class="text-[11px] text-slate-400">Fechadura eletrônica por código individual</p>
        </div>

        <div class="glass-card p-3.5 rounded-xl text-center space-y-1">
          <div class="text-xl">✈️</div>
          <h4 class="text-xs font-bold text-white">10-15 Min de GRU</h4>
          <p class="text-[11px] text-slate-400">Acesso descomplicado aos terminais</p>
        </div>

        <div class="glass-card p-3.5 rounded-xl text-center space-y-1">
          <div class="text-xl">🍳</div>
          <h4 class="text-xs font-bold text-white">Cozinha Equipada</h4>
          <p class="text-[11px] text-slate-400">Micro-ondas, frigobar & cafeteira</p>
        </div>

        <div class="glass-card p-3.5 rounded-xl text-center space-y-1 col-span-2 sm:col-span-1">
          <div class="text-xl">🛡️</div>
          <h4 class="text-xs font-bold text-white">10% OFF Direto</h4>
          <p class="text-[11px] text-slate-400">Melhor tarifa garantida sem taxas</p>
        </div>

      </div>

    </div>
  </section>

  <!-- SEÇÃO DE STUDIOS (ACOMODAÇÕES) -->
  <section id="studios" class="py-20 bg-slate-900/40 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-12 space-y-3">
        <h2 class="text-xs font-bold uppercase tracking-wider text-emerald-400">Nossas Acomodações</h2>
        <p class="text-3xl sm:text-4xl font-extrabold text-white">Conheça cada um dos nossos 4 studios</p>
        <p class="text-slate-400 text-sm">
          Todos os 4 studios contam com fechadura digital 24h com senha pessoal, Wi-Fi fibra de 600 Mbps, Smart TV, ar-condicionado/ventilador, cozinha compacta completa e banheiro privativo. <strong>Ao consultar sua reserva, selecionamos e alocamos automaticamente a melhor acomodação disponível para o seu período.</strong>
        </p>
      </div>

      <!-- FILTRO DE TIPOLOGIA -->
      <div class="flex items-center justify-center gap-2 mb-10">
        <button onclick="filtrarStudios('todos')" id="btnFiltroTodos" class="px-4 py-2 rounded-xl text-xs font-bold bg-emerald-500 text-slate-950 transition">Todos (4 Studios)</button>
        <button onclick="filtrarStudios('amplos')" id="btnFiltroAmplos" class="px-4 py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:text-white transition">Studios Maiores (Cortinas · 12 e 14)</button>
        <button onclick="filtrarStudios('compactos')" id="btnFiltroCompactos" class="px-4 py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:text-white transition">Studios Compactos (Janela Superior · 11 e 13)</button>
      </div>

      <!-- GRID DOS 4 STUDIOS -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

        <!-- STUDIO 12 (O MAIOR) -->
        <div class="card-studio glass-card rounded-2xl overflow-hidden flex flex-col group hover:border-emerald-500/40 transition duration-300" data-tipo="amplos">
          <div class="relative h-60 overflow-hidden bg-slate-950">
            <img src="assets/fotos/20251030_162521(1).webp" alt="Studio 12 - Master King" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-105 transition duration-500 cursor-pointer" onclick="abrirGaleria('12')">
            <div class="absolute top-3 left-3 flex flex-col gap-1.5">
              <span class="bg-amber-400 text-slate-950 text-[10px] font-black px-2.5 py-0.5 rounded shadow">🏆 O MAIOR STUDIO</span>
              <span class="bg-slate-950/80 backdrop-blur text-emerald-400 text-[10px] font-bold px-2 py-0.5 rounded border border-slate-700">Studio 12</span>
            </div>
            <button onclick="abrirGaleria('12')" class="absolute bottom-3 right-3 bg-slate-950/80 hover:bg-emerald-500 hover:text-slate-950 backdrop-blur text-slate-200 text-[11px] font-bold px-2.5 py-1 rounded-lg border border-slate-700 transition flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              <span>Ver Fotos</span>
            </button>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h3 class="font-extrabold text-lg text-white">Studio 12 · Master King</h3>
                <span class="text-xs font-extrabold text-emerald-400">10% OFF <span class="text-[10px] text-slate-400 font-normal">Direto</span></span>
              </div>
              <p class="text-xs text-slate-400">O maior e mais espaçoso do complexo. Ampla iluminação e máxima amplitude.</p>
              
              <!-- ESPECIFICAÇÃO FÍSICA -->
              <div class="my-3 p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/20 text-[11px] text-emerald-300 font-medium">
                🪟 <strong>Janela ampla com cortinas elegantes</strong> & espaço extra para circulação.
              </div>

              <ul class="space-y-1.5 text-xs text-slate-300">
                <li class="flex items-center gap-2">✓ Cama Queen Size & Enxoval Hotelaria</li>
                <li class="flex items-center gap-2">✓ Bancada Home Office & Wi-Fi 600MB</li>
                <li class="flex items-center gap-2">✓ Cozinha Compacta com Cooktop & Frigobar</li>
                <li class="flex items-center gap-2">✓ Smart TV & Fechadura Digital 24h</li>
              </ul>
            </div>
            
            <div class="pt-2 flex flex-col gap-2">
              <button type="button" onclick="focarCotadorStudio('12')" class="w-full text-center py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-extrabold transition shadow-md shadow-emerald-500/20">
                Verificar Disponibilidade & Tarifas
              </button>
            </div>
          </div>
        </div>

        <!-- STUDIO 14 (GRANDE EXECUTIVO) -->
        <div class="card-studio glass-card rounded-2xl overflow-hidden flex flex-col group hover:border-emerald-500/40 transition duration-300" data-tipo="amplos">
          <div class="relative h-60 overflow-hidden bg-slate-950">
            <img src="assets/fotos/20251030_164004.webp" alt="Studio 14 - Executivo" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-105 transition duration-500 cursor-pointer" onclick="abrirGaleria('14')">
            <div class="absolute top-3 left-3 flex flex-col gap-1.5">
              <span class="bg-teal-400 text-slate-950 text-[10px] font-black px-2.5 py-0.5 rounded shadow">⭐ GRANDE & EXECUTIVO</span>
              <span class="bg-slate-950/80 backdrop-blur text-emerald-400 text-[10px] font-bold px-2 py-0.5 rounded border border-slate-700">Studio 14</span>
            </div>
            <button onclick="abrirGaleria('14')" class="absolute bottom-3 right-3 bg-slate-950/80 hover:bg-emerald-500 hover:text-slate-950 backdrop-blur text-slate-200 text-[11px] font-bold px-2.5 py-1 rounded-lg border border-slate-700 transition flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              <span>Ver Fotos</span>
            </button>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h3 class="font-extrabold text-lg text-white">Studio 14 · Executivo</h3>
                <span class="text-xs font-extrabold text-emerald-400">10% OFF <span class="text-[10px] text-slate-400 font-normal">Direto</span></span>
              </div>
              <p class="text-xs text-slate-400">Muito espaçoso (um pouco menor que o 12), elegante e altamente reservado.</p>
              
              <!-- ESPECIFICAÇÃO FÍSICA -->
              <div class="my-3 p-2.5 rounded-lg bg-teal-500/10 border border-teal-500/20 text-[11px] text-teal-300 font-medium">
                🪟 <strong>Janela com cortinas elegantes</strong> & ambiente sofisticado.
              </div>

              <ul class="space-y-1.5 text-xs text-slate-300">
                <li class="flex items-center gap-2">✓ Cama de Casal Confort & Enxoval Premium</li>
                <li class="flex items-center gap-2">✓ Bancada de Trabalho / Home Office</li>
                <li class="flex items-center gap-2">✓ Cozinha Equipada & Cafeteira Dolce Gusto</li>
                <li class="flex items-center gap-2">✓ Wi-Fi 600MB & Smart TV com Streaming</li>
              </ul>
            </div>
            
            <div class="pt-2 flex flex-col gap-2">
              <button type="button" onclick="focarCotadorStudio('14')" class="w-full text-center py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-extrabold transition shadow-md shadow-emerald-500/20">
                Verificar Disponibilidade & Tarifas
              </button>
            </div>
          </div>
        </div>

        <!-- STUDIO 11 (COMPACTO SMART) -->
        <div class="card-studio glass-card rounded-2xl overflow-hidden flex flex-col group hover:border-emerald-500/40 transition duration-300" data-tipo="compactos">
          <div class="relative h-60 overflow-hidden bg-slate-950">
            <img src="assets/fotos/20251030_143554.webp" alt="Studio 11 - Standard Smart" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-105 transition duration-500 cursor-pointer" onclick="abrirGaleria('11')">
            <div class="absolute top-3 left-3 flex flex-col gap-1.5">
              <span class="bg-slate-800 text-slate-200 text-[10px] font-bold px-2.5 py-0.5 rounded shadow border border-slate-700">COMPACTO & PRÁTICO</span>
              <span class="bg-slate-950/80 backdrop-blur text-emerald-400 text-[10px] font-bold px-2 py-0.5 rounded border border-slate-700">Studio 11</span>
            </div>
            <button onclick="abrirGaleria('11')" class="absolute bottom-3 right-3 bg-slate-950/80 hover:bg-emerald-500 hover:text-slate-950 backdrop-blur text-slate-200 text-[11px] font-bold px-2.5 py-1 rounded-lg border border-slate-700 transition flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              <span>Ver Fotos</span>
            </button>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h3 class="font-extrabold text-lg text-white">Studio 11 · Standard Smart</h3>
                <span class="text-xs font-extrabold text-emerald-400">10% OFF <span class="text-[10px] text-slate-400 font-normal">Direto</span></span>
              </div>
              <p class="text-xs text-slate-400">Planta compacta e inteligente. Ideal para escalas e quem busca silêncio e praticidade.</p>
              
              <!-- ESPECIFICAÇÃO FÍSICA -->
              <div class="my-3 p-2.5 rounded-lg bg-slate-800/80 border border-slate-700 text-[11px] text-slate-300 font-medium">
                🚪 <strong>Janelinha pequena superior</strong> para total privacidade e ventilação.
              </div>

              <ul class="space-y-1.5 text-xs text-slate-300">
                <li class="flex items-center gap-2">✓ Cama de Casal Confortável</li>
                <li class="flex items-center gap-2">✓ Frigobar & Micro-ondas Privativo</li>
                <li class="flex items-center gap-2">✓ Wi-Fi Fibra 600MB & Smart TV</li>
                <li class="flex items-center gap-2">✓ Fechadura Eletrônica 24h</li>
              </ul>
            </div>
            
            <div class="pt-2 flex flex-col gap-2">
              <button type="button" onclick="focarCotadorStudio('11')" class="w-full text-center py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-extrabold transition shadow-md shadow-emerald-500/20">
                Verificar Disponibilidade & Tarifas
              </button>
            </div>
          </div>
        </div>

        <!-- STUDIO 13 (COMPACTO ACOLHEDOR) -->
        <div class="card-studio glass-card rounded-2xl overflow-hidden flex flex-col group hover:border-emerald-500/40 transition duration-300" data-tipo="compactos">
          <div class="relative h-60 overflow-hidden bg-slate-950">
            <img src="assets/fotos/20251030_144024.webp" alt="Studio 13 - Standard Acolhedor" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-105 transition duration-500 cursor-pointer" onclick="abrirGaleria('13')">
            <div class="absolute top-3 left-3 flex flex-col gap-1.5">
              <span class="bg-slate-800 text-slate-200 text-[10px] font-bold px-2.5 py-0.5 rounded shadow border border-slate-700">COMPACTO & RESERVADO</span>
              <span class="bg-slate-950/80 backdrop-blur text-emerald-400 text-[10px] font-bold px-2 py-0.5 rounded border border-slate-700">Studio 13</span>
            </div>
            <button onclick="abrirGaleria('13')" class="absolute bottom-3 right-3 bg-slate-950/80 hover:bg-emerald-500 hover:text-slate-950 backdrop-blur text-slate-200 text-[11px] font-bold px-2.5 py-1 rounded-lg border border-slate-700 transition flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              <span>Ver Fotos</span>
            </button>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h3 class="font-extrabold text-lg text-white">Studio 13 · Standard Cozy</h3>
                <span class="text-xs font-extrabold text-emerald-400">10% OFF <span class="text-[10px] text-slate-400 font-normal">Direto</span></span>
              </div>
              <p class="text-xs text-slate-400">Compacto, silencioso e acolhedor. Excelente custo-benefício para quem busca conforto.</p>
              
              <!-- ESPECIFICAÇÃO FÍSICA -->
              <div class="my-3 p-2.5 rounded-lg bg-slate-800/80 border border-slate-700 text-[11px] text-slate-300 font-medium">
                🚪 <strong>Janelinha pequena superior</strong> para máximo silêncio e discrição.
              </div>

              <ul class="space-y-1.5 text-xs text-slate-300">
                <li class="flex items-center gap-2">✓ Cama Casal & Travesseiros Antialérgicos</li>
                <li class="flex items-center gap-2">✓ Ducha de Alta Pressão & Banheiro Privativo</li>
                <li class="flex items-center gap-2">✓ Frigobar, Micro-ondas & Cafeteira</li>
                <li class="flex items-center gap-2">✓ Wi-Fi Fibra 600MB & Smart TV</li>
              </ul>
            </div>
            
            <div class="pt-2 flex flex-col gap-2">
              <button type="button" onclick="focarCotadorStudio('13')" class="w-full text-center py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-extrabold transition shadow-md shadow-emerald-500/20">
                Verificar Disponibilidade & Tarifas
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
        <h2 class="text-xs font-bold uppercase tracking-wider text-emerald-400">Transparência Total</h2>
        <p class="text-2xl sm:text-3xl font-extrabold text-white">Por que reservar direto conosco pelo WhatsApp?</p>
      </div>

      <div class="overflow-x-auto glass-card rounded-2xl border border-slate-800 shadow-xl">
        <table class="w-full text-left text-xs sm:text-sm">
          <thead>
            <tr class="border-b border-slate-800 text-slate-400 bg-slate-900/60 text-[11px] uppercase tracking-wider">
              <th class="p-4 sm:p-5">Benefício</th>
              <th class="p-4 sm:p-5 text-emerald-400 font-extrabold bg-emerald-500/5">SNT Studios (Direto Oficial)</th>
              <th class="p-4 sm:p-5 text-slate-400">Plataformas (Booking / Airbnb)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/60 text-slate-300">
            <tr>
              <td class="p-4 sm:p-5 font-semibold text-white">Tarifa Final</td>
              <td class="p-4 sm:p-5 font-bold text-emerald-400 bg-emerald-500/5">10% de desconto garantido</td>
              <td class="p-4 sm:p-5 text-slate-400">Preço cheio com margem embutida</td>
            </tr>
            <tr>
              <td class="p-4 sm:p-5 font-semibold text-white">Taxas de Serviço</td>
              <td class="p-4 sm:p-5 font-bold text-emerald-400 bg-emerald-500/5">R$ 0,00 (Zero taxa de intermediação)</td>
              <td class="p-4 sm:p-5 text-slate-400">Cobram de 15% a 21% a mais</td>
            </tr>
            <tr>
              <td class="p-4 sm:p-5 font-semibold text-white">Atendimento & Suporte</td>
              <td class="p-4 sm:p-5 font-bold text-emerald-400 bg-emerald-500/5">WhatsApp direto com nossa equipe local</td>
              <td class="p-4 sm:p-5 text-slate-400">Chat do app com intermediários e bots genéricos</td>
            </tr>
            <tr>
              <td class="p-4 sm:p-5 font-semibold text-white">Formas de Pagamento</td>
              <td class="p-4 sm:p-5 font-bold text-emerald-400 bg-emerald-500/5">PIX ou Cartão combinado direto e com segurança</td>
              <td class="p-4 sm:p-5 text-slate-400">Cartão com cobrança internacional ou regras rígidas</td>
            </tr>
            <tr>
              <td class="p-4 sm:p-5 font-semibold text-white">Flexibilidade de Horários</td>
              <td class="p-4 sm:p-5 font-bold text-emerald-400 bg-emerald-500/5">Possibilidade de Early Check-in sob consulta direta</td>
              <td class="p-4 sm:p-5 text-slate-400">Regras automáticas sem contato direto</td>
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
        <h2 class="text-xs font-bold uppercase tracking-wider text-emerald-400">Infraestrutura Completa</h2>
        <p class="text-3xl font-extrabold text-white">Tudo o que você precisa para uma estadia impecável</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <div class="glass-card p-6 rounded-2xl space-y-3">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-xl font-bold">⚡</div>
          <h3 class="text-base font-bold text-white">Internet Fibra 600 Mbps</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Conexão dedicada de ultra-alta velocidade com roteador potente. Perfeito para chamadas de vídeo, reuniões executivas e streaming em 4K sem qualquer oscilação.
          </p>
        </div>

        <div class="glass-card p-6 rounded-2xl space-y-3">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-xl font-bold">🔑</div>
          <h3 class="text-base font-bold text-white">Acesso Eletrônico 24h</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Fechaduras digitais na entrada e nos quartos. Você recebe sua senha pessoal pelo WhatsApp e pode chegar a qualquer hora da noite ou madrugada com total autonomia.
          </p>
        </div>

        <div class="glass-card p-6 rounded-2xl space-y-3">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-xl font-bold">🍳</div>
          <h3 class="text-base font-bold text-white">Cozinha Compacta Privativa</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Equipada com frigobar, micro-ondas, cooktop, cafeteira Dolce Gusto, louças, copos e panelas. Prepare suas próprias refeições com praticidade e economia.
          </p>
        </div>

        <div class="glass-card p-6 rounded-2xl space-y-3">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-xl font-bold">🚿</div>
          <h3 class="text-base font-bold text-white">Ducha de Alta Pressão</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Banheiros privativos impecáveis com banho quente pressurizado, toalhas de corpo e rosto de hotelaria higienizadas e secador de cabelo disponível.
          </p>
        </div>

        <div class="glass-card p-6 rounded-2xl space-y-3">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-xl font-bold">🧺</div>
          <h3 class="text-base font-bold text-white">Parceria SNT Lavanderia</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Acesso facilitado à rede parceira SNT Lavanderia Self-Service para lavar e secar suas roupas em menos de 1 hora com sabão e amaciante OMO/Comfort dosados.
          </p>
        </div>

        <div class="glass-card p-6 rounded-2xl space-y-3">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-xl font-bold">🛡️</div>
          <h3 class="text-base font-bold text-white">Segurança & Monitoramento</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
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
          <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Localização Privilegiada</span>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-white leading-tight">
            Perto de tudo em Guarulhos e na Grande São Paulo
          </h2>
          <p class="text-sm text-slate-300 leading-relaxed">
            Localizado no bairro Cidade Seródio em Guarulhos, com rota rápida e desimpedida para os terminais do <strong>Aeroporto Internacional de Guarulhos (GRU)</strong>, Rodovia Pres. Dutra e Rodovia Ayrton Senna.
          </p>

          <!-- ENDEREÇO OFICIAL COM BOTÃO DE COPIAR -->
          <div class="p-4 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
              <span class="text-emerald-400 text-xl">📍</span>
              <div>
                <span class="text-[11px] text-slate-400 font-bold uppercase tracking-wider block">Endereço Oficial</span>
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
              <span>Abrir no Google Maps</span>
            </a>
            <a href="https://waze.com/ul?q=Avenida+Aguanil+51+Guarulhos+SP" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-white font-bold px-4 py-2.5 rounded-xl text-xs border border-slate-700 transition">
              <svg class="w-4 h-4 text-sky-400" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 1010 10A10 10 0 0012 2zm1 14.5a1.5 1.5 0 111.5-1.5 1.5 1.5 0 01-1.5 1.5zm-3-4a1 1 0 111-1 1 1 0 01-1 1zm4 0a1 1 0 111-1 1 1 0 01-1 1z"/></svg>
              <span>Traçar Rota no Waze</span>
            </a>
          </div>

          <!-- DISTÂNCIAS PRINCIPAIS -->
          <div class="grid grid-cols-2 gap-3 pt-2">
            <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800">
              <span class="text-xs text-slate-400 block">Aeroporto GRU</span>
              <span class="text-sm font-bold text-emerald-400">10-15 minutos</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800">
              <span class="text-xs text-slate-400 block">Linha 13-Jade CPTM</span>
              <span class="text-sm font-bold text-white">8 minutos</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800">
              <span class="text-xs text-slate-400 block">Supermercado & Padaria</span>
              <span class="text-sm font-bold text-white">200 metros</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800">
              <span class="text-xs text-slate-400 block">Shopping Bosque Maia</span>
              <span class="text-sm font-bold text-white">18 minutos</span>
            </div>
          </div>
        </div>

        <!-- GOOGLE MAPS EMBED OFICIAL COM PIN -->
        <div class="lg:col-span-6 h-[400px] rounded-2xl overflow-hidden border border-slate-800 shadow-2xl relative">
          <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3661.1273934371465!2d-46.46747202391039!3d-23.42065845648834!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce8b9a1ebc86ad%3A0x6b631d8ce4a7e780!2sAv.%20Aguanil%2C%2051%20-%20Cidade%20Ser%C3%B3dio%2C%20Guarulhos%20-%20SP%2C%2007150-130!5e0!3m2!1spt-BR!2sbr!4v1700000000000!5m2!1spt-BR!2sbr" 
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
        <h2 class="text-xs font-bold uppercase tracking-wider text-emerald-400">Tire Suas Dúvidas</h2>
        <p class="text-3xl font-extrabold text-white">Perguntas Frequentes</p>
      </div>

      <div class="space-y-4">
        
        <details class="glass-card rounded-xl p-5 group cursor-pointer">
          <summary class="font-bold text-sm sm:text-base text-white flex items-center justify-between">
            <span>Como funciona o check-in se meu voo chegar de madrugada?</span>
            <span class="text-emerald-400 transition group-open:rotate-180">▼</span>
          </summary>
          <p class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed">
            Totalmente tranquilo! Nosso sistema é 100% automatizado através de fechaduras eletrônicas digitais tanto no portão de pedestres quanto na porta do seu studio. Após a confirmação no WhatsApp, você recebe sua senha individual e pode chegar em qualquer horário entre 15:00 e a manhã seguinte sem depender de recepção ou espera.
          </p>
        </details>

        <details class="glass-card rounded-xl p-5 group cursor-pointer">
          <summary class="font-bold text-sm sm:text-base text-white flex items-center justify-between">
            <span>Como funciona o desconto de 10% na reserva direta?</span>
            <span class="text-emerald-400 transition group-open:rotate-180">▼</span>
          </summary>
          <p class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed">
            Plataformas como Booking e Airbnb cobram de 15% a 21% de comissão sobre a estadia. Reservando direto conosco pelo WhatsApp oficial, eliminamos essa taxa e repassamos 10% de economia garantida para você no valor final da hospedagem.
          </p>
        </details>

        <details class="glass-card rounded-xl p-5 group cursor-pointer">
          <summary class="font-bold text-sm sm:text-base text-white flex items-center justify-between">
            <span>Qual a diferença entre os studios com cortinas e os compactos?</span>
            <span class="text-emerald-400 transition group-open:rotate-180">▼</span>
          </summary>
          <p class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed">
            Os <strong>Studios 12 e 14</strong> são os maiores da propriedade, contam com janelas amplas com cortinas elegantes e ampla circulação. Os <strong>Studios 11 e 13</strong> são mais compactos e possuem uma janelinha superior basculante de ventilação, sendo extremamente silenciosos e com custo mais acessível.
          </p>
        </details>

        <details class="glass-card rounded-xl p-5 group cursor-pointer">
          <summary class="font-bold text-sm sm:text-base text-white flex items-center justify-between">
            <span>A internet suporta reuniões em vídeo e trabalho remoto?</span>
            <span class="text-emerald-400 transition group-open:rotate-180">▼</span>
          </summary>
          <p class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed">
            Sim! Temos fibra óptica dedicada de <strong>600 Mbps</strong> com baixa latência e sinal forte em todos os studios. Nossos hóspedes executivos utilizam regularmente para chamadas no Teams, Zoom, Google Meet e streaming.
          </p>
        </details>

        <details class="glass-card rounded-xl p-5 group cursor-pointer">
          <summary class="font-bold text-sm sm:text-base text-white flex items-center justify-between">
            <span>Quais as formas de pagamento aceitas para a reserva direta?</span>
            <span class="text-emerald-400 transition group-open:rotate-180">▼</span>
          </summary>
          <p class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed">
            Você pode pagar com total segurança via <strong>PIX</strong> (com confirmação instantânea) ou <strong>Cartão de Crédito</strong>. Todo o fluxo é combinado com clareza e recibo pelo WhatsApp oficial.
          </p>
        </details>

        <details class="glass-card rounded-xl p-5 group cursor-pointer">
          <summary class="font-bold text-sm sm:text-base text-white flex items-center justify-between">
            <span>Tem comércio ou alimentação perto do studio?</span>
            <span class="text-emerald-400 transition group-open:rotate-180">▼</span>
          </summary>
          <p class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed">
            Sim! A menos de 2 a 5 minutos a pé você encontra padaria, farmácia, supermercado e restaurantes, além de ampla cobertura de entrega do iFood com entrega rápida na nossa porta.
          </p>
        </details>

      </div>

      <!-- CTA FINAL DA SEÇÃO FAQ -->
      <div class="mt-12 text-center">
        <a href="https://api.whatsapp.com/send?phone=551154443110&text=Ola%21%20Gostaria%20de%20tirar%20uma%20duvida%20sobre%20a%20hospedagem%20no%20SNT%20Studios." target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-3 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-extrabold px-8 py-4 rounded-xl text-sm sm:text-base shadow-xl shadow-emerald-500/25 transition transform hover:-translate-y-0.5">
          <span>Ainda tem dúvidas? Fale com a gente no WhatsApp</span>
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
          <img src="assets/snt-empreendimentos-horizontal-branco.png" alt="SNT Studios" class="h-10 w-auto object-contain">
          <p class="text-slate-400 max-w-sm leading-relaxed text-[11px]">
            Hospitalidade inteligente e moderna em Guarulhos. Studios privativos completos para quem valoriza silêncio, conforto, tecnologia e proximidade com o Aeroporto GRU.
          </p>
          <div class="pt-2 text-[11px] text-slate-400 space-y-1">
            <p><strong>Razão Social:</strong> SNT Empreendimentos Imobiliários LTDA</p>
            <p><strong>CNPJ:</strong> 63.223.844/0001-11</p>
            <p><strong>Inscrição Municipal:</strong> 772987 · Guarulhos/SP</p>
            <p><strong>Endereço:</strong> Avenida Aguanil, 51 - Cidade Seródio - Guarulhos/SP - CEP 07150-130</p>
          </div>
        </div>

        <!-- COLUNA 2: LINKS RÁPIDOS -->
        <div class="space-y-2">
          <h4 class="font-bold text-white uppercase tracking-wider text-[11px]">Navegação</h4>
          <ul class="space-y-1.5 text-[11px]">
            <li><a href="#inicio" class="hover:text-emerald-400 transition">Início & Anúncio</a></li>
            <li><a href="#cotador" class="hover:text-emerald-400 transition">Verificar Disponibilidade</a></li>
            <li><a href="#studios" class="hover:text-emerald-400 transition">Nossas 4 Acomodações</a></li>
            <li><a href="#comodidades" class="hover:text-emerald-400 transition">Comodidades & Wi-Fi</a></li>
            <li><a href="#localizacao" class="hover:text-emerald-400 transition">Localização & Rotas GRU</a></li>
            <li><a href="#faq" class="hover:text-emerald-400 transition">Dúvidas Frequentes</a></li>
          </ul>
        </div>

        <!-- COLUNA 3: CONTATO & CANAIS -->
        <div class="space-y-2">
          <h4 class="font-bold text-white uppercase tracking-wider text-[11px]">Atendimento Oficial</h4>
          <p class="text-[11px] text-slate-400">Atendimento humanizado para cotações, reservas e suporte ao hóspede:</p>
          <a href="https://api.whatsapp.com/send?phone=551154443110" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-emerald-400 hover:text-emerald-300 font-bold text-xs py-1">
            <span>WhatsApp: (11) 5444-3110</span>
          </a>
          <p class="text-[11px] text-slate-400">Check-in: a partir das 15:00<br>Check-out: até as 11:00</p>
        </div>

      </div>

      <div class="pt-8 border-t border-slate-800/80 flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-slate-400">
        <p>© 2026 SNT Studios (SNT Empreendimentos Imobiliários LTDA). Todos os direitos reservados.</p>
        <p class="text-slate-400">Desenvolvido com tecnologia sustentável e zero CDNs externas em produção.</p>
      </div>

    </div>
  </footer>

  <!-- MODAL DE GALERIA DE FOTOS (LIGHTBOX 20 FOTOS) -->
  <div id="modalGaleria" class="fixed inset-0 z-50 modal-backdrop hidden flex items-center justify-center p-4">
    <div class="relative max-w-4xl w-full bg-slate-900 border border-slate-800 rounded-3xl overflow-hidden shadow-2xl flex flex-col max-h-[90vh]">
      
      <!-- CABEÇALHO DO MODAL -->
      <div class="p-4 border-b border-slate-800 flex items-center justify-between">
        <div>
          <h3 id="modalGaleriaTitulo" class="font-bold text-white text-sm sm:text-base">Fotos Reais do SNT Studios</h3>
          <p id="modalGaleriaSubtitulo" class="text-xs text-slate-400">Fotos 100% autênticas dos nossos 4 studios</p>
        </div>
        <button onclick="fecharGaleria()" class="w-9 h-9 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-200 flex items-center justify-center font-bold text-lg transition">
          ✕
        </button>
      </div>

      <!-- VISUALIZADOR DA FOTO ATUAL -->
      <div class="relative flex-1 bg-black flex items-center justify-center min-h-[300px] sm:min-h-[460px] overflow-hidden">
        <img id="modalFotoPrincipal" src="" alt="Foto do Studio" class="max-h-[70vh] w-auto max-w-full object-contain">
        
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
        <span class="text-base font-black text-white" id="mobileBarPreco">R$ 159</span>
        <span class="text-xs text-slate-400">/ noite</span>
      </div>
      <div class="text-[11px] text-emerald-400 font-medium" id="mobileBarDatas">Selecione as datas</div>
    </div>
    <button type="button" onclick="focarCotador()" class="bg-emerald-500 hover:bg-emerald-400 active:scale-95 text-slate-950 font-black px-4 py-2.5 rounded-xl text-xs uppercase tracking-wider shadow-lg shadow-emerald-500/25 transition">
      Verificar Datas
    </button>
  </div>

  <!-- BOTAO FLUTUANTE WHATSAPP (POSICIONADO ACIMA DA BARRA NO MOBILE) -->
  <a href="https://api.whatsapp.com/send?phone=551154443110&text=Ola%21%20Gostaria%20de%20consultar%20uma%20reserva%20direta%20no%20SNT%20Studios%20com%2010%25%20de%20desconto." target="_blank" rel="noopener noreferrer" class="fixed bottom-20 lg:bottom-6 right-4 lg:right-6 z-50 flex items-center gap-2.5 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-extrabold p-3.5 sm:px-5 sm:py-3.5 rounded-full shadow-2xl shadow-emerald-500/30 transition transform hover:scale-105" title="Falar no WhatsApp Oficial">
    <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824zm-3.423-14.416c-6.627 0-12 5.373-12 12 0 2.159.57 4.184 1.564 5.938l-1.664 6.086 6.257-1.64c1.706.924 3.659 1.45 5.743 1.45 6.627 0 12-5.373 12-12 0-6.627-5.373-12-12-12z"/></svg>
    <span class="hidden sm:inline text-xs tracking-wide">Falar no WhatsApp</span>
  </a>

  <!-- SCRIPTS FUNCIONAIS -->
  <script>
    // ========================================================
    // FILTRAGEM DE STUDIOS
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
    // FORMATADORES E UTILITÁRIOS
    // ========================================================
    function formatarDataBr(isoStr) {
      if (!isoStr) return "";
      const [ano, mes, dia] = isoStr.split('-');
      return `${dia}/${mes}/${ano}`;
    }

    function formatarMoeda(valor) {
      return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(Number(valor) || 0);
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
    let ultimaCotacao = null;

    // ========================================================
    // FOCO E NAVEGAÇÃO PARA O WIDGET DE RESERVA AIRBNB
    // ========================================================
    function focarCotador() {
      const el = document.getElementById('cotador');
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        el.classList.add('card-pulse-highlight');
        setTimeout(() => el.classList.remove('card-pulse-highlight'), 2500);
      }
      const inEl = document.getElementById('inputCheckIn');
      if (inEl) {
        setTimeout(() => inEl.focus(), 350);
      }
    }

    function focarCotadorStudio(studioNum) {
      focarCotador();
      if (ultimaCotacao && Array.isArray(ultimaCotacao.studios)) {
        renderizarCardDisponibilidade(studioNum);
      }
    }

    function compartilharSite() {
      const shareData = {
        title: 'SNT Studios · Hospedagem ao Lado do Aeroporto GRU',
        text: 'Studios privativos modernos com Wi-Fi 600MB, fechadura digital 24h e 10% de desconto na reserva direta.',
        url: 'https://www.sntstudios.com/'
      };
      if (navigator.share) {
        navigator.share(shareData).catch(() => {});
      } else {
        navigator.clipboard.writeText(shareData.url);
        const btn = document.getElementById('btnShareText');
        if (btn) {
          btn.innerText = "Link copiado!";
          setTimeout(() => { btn.innerText = "Compartilhar"; }, 2000);
        }
      }
    }

    // ========================================================
    // ENVIO DE MENSAGEM LIMPA E PROFISSIONAL PARA O WHATSAPP
    // ========================================================
    function abrirWhatsAppCotacao(studioNumero) {
      const dados = ultimaCotacao || {};
      const inVal = dados.entrada || document.getElementById('inputCheckIn').value;
      const outVal = dados.saida || document.getElementById('inputCheckOut').value;
      const guests = dados.hospedes || document.getElementById('selectGuests').value;
      const studio = dados.studios && dados.studios.find(s => String(s.numero) === String(studioNumero));
      
      const linhas = [
        "Ola! Consultei o site oficial do SNT Studios e gostaria de confirmar uma reserva direta com 10% de desconto:",
        "",
        "- Check-in: " + formatarDataBr(inVal),
        "- Check-out: " + formatarDataBr(outVal) + (dados.noites ? " (" + dados.noites + " noites)" : ""),
        "- Hospedes: " + guests + " pessoa" + (Number(guests) > 1 ? "s" : "")
      ];

      if (studio) {
        linhas.push("- Studio recomendado: " + studio.nome + " (" + formatarMoeda(studio.totalDireta) + " total com limpeza)");
        linhas.push("- Economia direta vs plataformas: " + formatarMoeda(studio.economia));
      } else {
        linhas.push("- Alocacao: melhor acomodacao disponivel para o periodo");
      }

      linhas.push("");
      linhas.push("Poderiam confirmar a disponibilidade e os proximos passos, por favor?");
      window.open("https://api.whatsapp.com/send?phone=551154443110&text=" + encodeURIComponent(linhas.join(String.fromCharCode(10))), '_blank', 'noopener');
    }

    // ========================================================
    // RENDERIZADOR DO RECIBO ESTILO AIRBNB
    // ========================================================
    function renderizarCardDisponibilidade(studioNumEscolhido) {
      if (!ultimaCotacao || !Array.isArray(ultimaCotacao.studios)) return;
      const dados = ultimaCotacao;
      const resultado = document.getElementById('resultadoCotacao');
      const ordemPreferencia = ['12', '14', '11', '13'];
      
      const livres = dados.studios
        .filter(studio => studio && studio.disponivel && Number.isFinite(Number(studio.totalDireta)))
        .sort((a, b) => ordemPreferencia.indexOf(String(a.numero)) - ordemPreferencia.indexOf(String(b.numero)));

      if (!livres.length) {
        resultado.innerHTML = `
          <div class="rounded-2xl border border-rose-500/40 bg-rose-500/10 p-4">
            <h4 class="font-bold text-xs text-rose-200">Datas indisponíveis no calendário</h4>
            <p class="mt-1 text-[11px] leading-relaxed text-slate-300">
              Não há studios livres para todas as noites selecionadas (${formatarDataBr(dados.entrada)} a ${formatarDataBr(dados.saida)}).
            </p>
            <button type="button" onclick="abrirWhatsAppCotacao('')" class="mt-3 w-full rounded-xl bg-emerald-500 py-3 text-xs font-black text-slate-950 hover:bg-emerald-400 transition shadow-lg shadow-emerald-500/20">
              Consultar alternativas no WhatsApp
            </button>
          </div>`;
        return;
      }

      let studio = livres[0];
      if (studioNumEscolhido) {
        const achado = livres.find(s => String(s.numero) === String(studioNumEscolhido));
        if (achado) studio = achado;
      }

      // Atualiza o preço por noite no cabeçalho do card e na barra mobile
      const precoCabecalho = document.getElementById('headerPrecoNoite');
      if (precoCabecalho) precoCabecalho.innerText = formatarMoeda(studio.porNoite);
      const mobilePreco = document.getElementById('mobileBarPreco');
      if (mobilePreco) mobilePreco.innerText = formatarMoeda(studio.porNoite);
      const mobileDatas = document.getElementById('mobileBarDatas');
      if (mobileDatas) mobileDatas.innerText = `${formatarDataBr(dados.entrada)} - ${formatarDataBr(dados.saida)} (${dados.noites}n)`;

      // Monta as opções de troca de acomodação caso haja mais de 1 livre
      let seletorOutrosStudios = '';
      if (livres.length > 1) {
        seletorOutrosStudios = `
          <div class="pt-2 flex items-center justify-between text-[11px] text-slate-400">
            <span>Outras opções disponíveis:</span>
            <div class="flex gap-1.5">
              ${livres.map(s => `
                <button type="button" onclick="renderizarCardDisponibilidade('${s.numero}')" class="px-2 py-0.5 rounded font-bold transition ${String(s.numero) === String(studio.numero) ? 'bg-emerald-500 text-slate-950' : 'bg-slate-800 text-slate-300 hover:text-white'}">
                  Studio ${s.numero}
                </button>
              `).join('')}
            </div>
          </div>`;
      }

      resultado.innerHTML = `
        <div class="space-y-3.5">
          <!-- CARD DA ACOMODAÇÃO ALOCADA -->
          <div class="rounded-xl border border-emerald-500/40 bg-emerald-500/10 p-3.5 flex items-center justify-between">
            <div class="flex items-center gap-2.5">
              <span class="flex h-7 w-7 items-center justify-center rounded-lg bg-emerald-500 text-slate-950 font-black text-xs">
                ${escaparHtml(studio.numero)}
              </span>
              <div>
                <div class="text-xs font-bold text-white">${escaparHtml(studio.nome)}</div>
                <div class="text-[10px] text-emerald-300 font-medium">${dados.noites} noite${dados.noites > 1 ? 's' : ''} para ${escaparHtml(dados.hospedes)} hóspede${Number(dados.hospedes) > 1 ? 's' : ''}</div>
              </div>
            </div>
            <span class="rounded bg-emerald-500/20 px-2 py-0.5 text-[10px] font-bold text-emerald-300">
              ALOCAÇÃO RECOMENDADA
            </span>
          </div>

          ${seletorOutrosStudios}

          <!-- RECIBO DETALHADO ESTILO AIRBNB -->
          <div class="space-y-2 text-xs text-slate-300 pt-1">
            <div class="flex items-center justify-between">
              <span class="text-slate-300">${formatarMoeda(studio.porNoite)} × ${dados.noites} noite${dados.noites > 1 ? 's' : ''}</span>
              <span class="font-medium text-white">${formatarMoeda(studio.diariasTotal)}</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-slate-300">Taxa de limpeza e higienização</span>
              <span class="font-medium text-white">${formatarMoeda(studio.limpeza)}</span>
            </div>
            <div class="flex items-center justify-between text-emerald-400 font-semibold">
              <span>Desconto Reserva Direta (10% OFF)</span>
              <span>- ${formatarMoeda(studio.economia)}</span>
            </div>
            <div class="pt-2.5 border-t border-slate-700/80 flex items-baseline justify-between text-white">
              <div>
                <span class="text-sm font-black">Total da estadia</span>
                <p class="text-[10px] text-slate-400">Sem taxas de serviço de terceiros</p>
              </div>
              <span class="text-xl font-black text-emerald-400">${formatarMoeda(studio.totalDireta)}</span>
            </div>
          </div>

          <!-- BOTÃO DE AÇÃO WHATSAPP OFICIAL -->
          <button type="button" onclick="abrirWhatsAppCotacao('${escaparHtml(studio.numero)}')" class="w-full mt-2 bg-emerald-500 hover:bg-emerald-400 active:scale-[0.99] text-slate-950 font-black py-3.5 px-4 rounded-xl text-xs uppercase tracking-wider transition shadow-lg shadow-emerald-500/25 flex items-center justify-center gap-2">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824zm-3.423-14.416c-6.627 0-12 5.373-12 12 0 2.159.57 4.184 1.564 5.938l-1.664 6.086 6.257-1.64c1.706.924 3.659 1.45 5.743 1.45 6.627 0 12-5.373 12-12 0-6.627-5.373-12-12-12z"/></svg>
            <span>Reservar no WhatsApp (10% OFF)</span>
          </button>

          <p class="text-[10px] text-center text-slate-400">
            🔒 Sua pré-reserva é confirmada com nossa equipe oficial para bloqueio imediato no Smoobu.
          </p>
        </div>`;
    }

    // ========================================================
    // CONSULTA DE DISPONIBILIDADE EM TEMPO REAL NO SMOOBU
    // ========================================================
    async function consultarDisponibilidade() {
      const inVal = document.getElementById('inputCheckIn').value;
      const outVal = document.getElementById('inputCheckOut').value;
      const guests = document.getElementById('selectGuests').value;
      const resultado = document.getElementById('resultadoCotacao');
      const botao = document.getElementById('btnConsultar');

      if (!inVal || !outVal) {
        resultado.classList.remove('hidden');
        resultado.innerHTML = '<div class="rounded-xl border border-amber-500/40 bg-amber-500/10 p-3.5 text-xs text-amber-200">Selecione as datas de check-in e checkout para ver o valor exato.</div>';
        return;
      }

      const noites = Math.round((new Date(outVal + 'T12:00:00') - new Date(inVal + 'T12:00:00')) / 86400000);
      if (noites < 1 || noites > 120) {
        resultado.classList.remove('hidden');
        resultado.innerHTML = '<div class="rounded-xl border border-rose-500/40 bg-rose-500/10 p-3.5 text-xs text-rose-200">O checkout deve ser posterior ao check-in e a estadia pode ter no máximo 120 noites.</div>';
        return;
      }

      resultado.classList.remove('hidden');
      resultado.innerHTML = '<div class="flex items-center justify-center gap-3 rounded-xl border border-slate-700 bg-slate-900/90 p-4 text-xs text-emerald-300"><span class="h-4 w-4 animate-spin rounded-full border-2 border-emerald-400 border-t-transparent"></span>Consultando calendário e tarifas oficiais no Smoobu...</div>';
      botao.disabled = true;

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
            <h4 class="font-bold text-xs text-amber-200">O calendário não respondeu agora</h4>
            <p class="mt-1 text-[11px] leading-relaxed text-slate-300">Para não mostrar preço incorreto, a consulta e confirmação seguirá com nossa equipe.</p>
            <button type="button" onclick="abrirWhatsAppCotacao('')" class="mt-3 w-full rounded-lg bg-emerald-500 py-2.5 text-xs font-black text-slate-950 hover:bg-emerald-400 transition">
              Consultar no WhatsApp
            </button>
          </div>`;
      } finally {
        clearTimeout(timeoutId);
        botao.disabled = false;
      }
    }

    function copiarEndereco() {
      const txt = "Avenida Aguanil, 51 - Cidade Seródio - Guarulhos/SP";
      navigator.clipboard.writeText(txt);
      const btn = document.getElementById('btnCopiarEnd');
      btn.innerText = "✓ Copiado!";
      setTimeout(() => {
        btn.innerText = "Copiar";
      }, 2000);
    }

    // ========================================================
    // INICIALIZAÇÃO DE DATAS E EVENTOS
    // ========================================================
    document.addEventListener('DOMContentLoaded', () => {
      const inEl = document.getElementById('inputCheckIn');
      const outEl = document.getElementById('inputCheckOut');
      const guestsEl = document.getElementById('selectGuests');

      // Define data mínima como hoje
      const agora = new Date();
      const ano = agora.getFullYear();
      const mes = String(agora.getMonth() + 1).padStart(2, '0');
      const dia = String(agora.getDate()).padStart(2, '0');
      const hojeStr = `${ano}-${mes}-${dia}`;

      if (inEl && outEl) {
        inEl.min = hojeStr;
        outEl.min = hojeStr;

        inEl.addEventListener('change', () => {
          if (inEl.value) {
            const dIn = new Date(inEl.value + 'T12:00:00');
            const dOutMin = new Date(dIn.getTime() + 86400000);
            const y = dOutMin.getFullYear();
            const m = String(dOutMin.getMonth() + 1).padStart(2, '0');
            const d = String(dOutMin.getDate()).padStart(2, '0');
            const minNext = `${y}-${m}-${d}`;
            outEl.min = minNext;
            if (!outEl.value || outEl.value <= inEl.value) {
              outEl.value = minNext;
            }
            const mob = document.getElementById('mobileBarDatas');
            if (mob) mob.innerText = `${formatarDataBr(inEl.value)} - ${formatarDataBr(outEl.value)}`;
            consultarDisponibilidade();
          }
        });

        outEl.addEventListener('change', () => {
          if (inEl.value && outEl.value) {
            const mob = document.getElementById('mobileBarDatas');
            if (mob) mob.innerText = `${formatarDataBr(inEl.value)} - ${formatarDataBr(outEl.value)}`;
            consultarDisponibilidade();
          }
        });
      }

      if (guestsEl) {
        guestsEl.addEventListener('change', () => {
          if (ultimaCotacao && inEl && outEl && inEl.value && outEl.value) {
            ultimaCotacao.hospedes = guestsEl.value;
            renderizarCardDisponibilidade();
          }
        });
      }
    });

    // ========================================================
    // MODAL DE GALERIA DE FOTOS (LIGHTBOX 20 FOTOS WEBP)
    // ========================================================
    const galeriaFotos = {
      '12': [
        'assets/fotos/20251030_162521(1).webp',
        'assets/fotos/20251030_162403.webp',
        'assets/fotos/20251030_162350.webp',
        'assets/fotos/20251030_162606(1).webp',
        'assets/fotos/20251030_163823.webp'
      ],
      '14': [
        'assets/fotos/20251030_164004.webp',
        'assets/fotos/20251030_162615(1).webp',
        'assets/fotos/20251030_164033.webp',
        'assets/fotos/20251030_164106.webp',
        'assets/fotos/20251030_163810.webp'
      ],
      '11': [
        'assets/fotos/20251030_143554.webp',
        'assets/fotos/20251030_143603.webp',
        'assets/fotos/20251030_143653.webp',
        'assets/fotos/20251030_143812.webp',
        'assets/fotos/20251030_144426.webp'
      ],
      '13': [
        'assets/fotos/20251030_144024.webp',
        'assets/fotos/20251030_144035.webp',
        'assets/fotos/20251030_144400.webp',
        'assets/fotos/20251030_144616.webp',
        'assets/fotos/20251030_144436.webp'
      ]
    };

    let galeriaAtualLista = [];
    let galeriaFotoIdx = 0;

    function abrirGaleria(studioKey) {
      galeriaAtualLista = galeriaFotos[studioKey] || galeriaFotos['12'];
      galeriaFotoIdx = 0;
      
      const titulos = {
        '12': 'Studio 12 · Master King (O Maior Studio)',
        '14': 'Studio 14 · Executivo (Janela com Cortinas)',
        '11': 'Studio 11 · Standard Smart (Compacto)',
        '13': 'Studio 13 · Standard Cozy (Compacto)'
      };
      
      document.getElementById('modalGaleriaTitulo').innerText = titulos[studioKey] || 'Galeria de Fotos do Studio';
      document.getElementById('modalGaleriaSubtitulo').innerText = `Visualizando fotos reais do Studio ${studioKey}`;
      
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

    // Atalho ESC para fechar galeria
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        fecharGaleria();
      }
    });
  </script>

</body>
</html>
'''

raiz = Path(__file__).resolve().parent
(raiz / 'index.html').write_text(site_code, encoding='utf-8')

print("Generated index.html with Airbnb listing reserve widget and real-time availability.")
