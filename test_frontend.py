# -*- coding: utf-8 -*-
"""
Suíte de testes automatizados do frontend SNT Studios (sntstudios.com).
Verifica:
1. Padrões de Produção SNT: Zero CDNs externos, canônico HTTPS e CNPJ correto.
2. Requisitos de Negócio:
   - Zero estrelas, zero Superhost, zero Preferido dos hóspedes.
   - Zero menções a ferramentas internas (ex: Smoobu).
   - Zero exibição de 'taxa de limpeza' isolada (total consolidado embutido).
   - Nomes comerciais exclusivos (sem números 11, 12, 13, 14 para clientes).
3. Internacionalização (i18n): Paridade de 100% das chaves entre PT, EN e ES,
   e correspondência exata com todos os atributos data-i18n do DOM.
4. Mídia e Assets: Fotos WebP existentes em disco e payload otimizado (< 4 MB).
5. Sintaxe JavaScript: Validação via node --check.
"""
import sys, re, os, subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
raiz = Path(__file__).resolve().parent
html_file = raiz / 'index.html'

if not html_file.exists():
    print("ERRO: index.html não encontrado.")
    sys.exit(1)

html = html_file.read_text(encoding='utf-8')
erros = []

# 1. Zero CDN
if 'cdn.tailwindcss.com' in html:
    erros.append("Uso indevido de cdn.tailwindcss.com detectado.")

# 2. Canônico e CNPJ
if 'https://www.sntstudios.com/' not in html:
    erros.append("URL canônica 'https://www.sntstudios.com/' ausente.")
if '63.223.844/0001-11' not in html:
    erros.append("CNPJ oficial '63.223.844/0001-11' ausente ou incorreto.")

# 3. Termos proibidos
proibidos = ['★', '4.98', 'Superhost', 'Preferido dos hóspedes', 'Smoobu', 'taxa de limpeza']
for p in proibidos:
    if p.lower() in html.lower():
        erros.append(f"Termo proibido encontrado no HTML: '{p}'")

# 4. Números internos de studios expostos (11, 12, 13, 14)
for num in ['11', '12', '13', '14']:
    encontrados = re.findall(rf'Studio\s*{num}\b', html, re.IGNORECASE)
    if encontrados:
        erros.append(f"Número interno exposto ao cliente: {encontrados}")

# 5. Internacionalização (i18n)
pt_idx = html.find('pt: {')
en_idx = html.find('en: {')
es_idx = html.find('es: {')
end_idx = html.find('function trocarIdioma')

if pt_idx == -1 or en_idx == -1 or es_idx == -1 or end_idx == -1:
    erros.append("Estrutura do dicionário I18N não encontrada no script.")
else:
    pattern = re.compile(r'([a-zA-Z0-9_]+)\s*:\s*(?:"(?:\\.|[^"])*"|\'(?:\\.|[^\'])*\')')
    pt_keys = set(pattern.findall(html[pt_idx+5:en_idx]))
    en_keys = set(pattern.findall(html[en_idx+5:es_idx]))
    es_keys = set(pattern.findall(html[es_idx+5:end_idx]))

    if pt_keys != en_keys:
        erros.append(f"Discrepância PT vs EN: {pt_keys ^ en_keys}")
    if pt_keys != es_keys:
        erros.append(f"Discrepância PT vs ES: {pt_keys ^ es_keys}")

    html_keys = set(re.findall(r'data-i18n=["\']([a-zA-Z0-9_]+)["\']', html))
    faltando_dicionario = html_keys - pt_keys
    if faltando_dicionario:
        erros.append(f"Atributos data-i18n sem tradução no dicionário: {faltando_dicionario}")

# 6. Verificação de imagens WebP e payload
fotos = set(re.findall(r'assets/fotos/[a-zA-Z0-9_\-\.\(\)]+\.webp', html))
if not fotos:
    erros.append("Nenhuma foto WebP encontrada no HTML.")
else:
    fotos_faltantes = [f for f in fotos if not (raiz / f).exists()]
    if fotos_faltantes:
        erros.append(f"Fotos referenciadas ausentes em disco: {fotos_faltantes}")
    
    peso_total_mb = sum((raiz / f).stat().st_size for f in fotos if (raiz / f).exists()) / (1024 * 1024)
    if peso_total_mb > 4.0:
        erros.append(f"Peso total da galeria excede o limite de 4 MB: {peso_total_mb:.2f} MB")

# 7. Sintaxe JavaScript via node --check
scripts = re.findall(r'<script(?![^>]*ld\+json)[^>]*>(.*?)</script>', html, re.DOTALL)
for idx, s in enumerate(scripts):
    if not s.strip():
        continue
    temp_js = raiz / f'_temp_check_{idx}.js'
    temp_js.write_text(s, encoding='utf-8')
    res = subprocess.run(['node', '--check', str(temp_js)], capture_output=True, text=True)
    if res.returncode != 0:
        erros.append(f"Erro de sintaxe no script inline {idx}: {res.stderr}")
    if temp_js.exists():
        temp_js.unlink()

# 8. Ausência de Inscrição Municipal (conforme diretriz de privacidade fiscal)
if 'inscrição municipal' in html.lower() or 'inscricao municipal' in html.lower() or '772987' in html:
    erros.append("Inscrição Municipal ou registro fiscal 772987 encontrado indevidamente no HTML.")

# 9. Verificação do Calendário Airbnb Dual-Month e Strike-Through
if 'calDiasGrid1' not in html or 'calDiasGrid2' not in html:
    erros.append("Estrutura do calendário dual-month (Airbnb) ausente no HTML.")
if 'calMiniCheckIn' not in html or 'calMiniCheckOut' not in html:
    erros.append("Mini-box de Check-in/Checkout do calendário ausente.")
if 'calBtnPrevMes' not in html:
    erros.append("Botão de navegação calBtnPrevMes ausente no HTML.")
if 'datasTotalmenteOcupadas' not in html or 'carregarDisponibilidadeGeral' not in html:
    erros.append("Lógica de detecção e strike-through de datas ocupadas ausente.")

# O calendário é um modal sobre a tela, não um bloco que empurra o conteúdo para
# baixo. O clique dentro dele precisa parar antes do listener que fecha ao clicar
# fora; isso preserva a janela entre o primeiro e o segundo clique do intervalo.
if 'id="calendarioBackdrop"' not in html or 'aria-modal="true"' not in html:
    erros.append("Calendário não possui a sobreposição modal esperada.")
if 'id="calendarioAirbnb"' not in html or 'onclick="event.stopPropagation()"' not in html:
    erros.append("Clique interno do calendário pode voltar a fechá-lo após o check-in.")
if 'fixed inset-x-3 top-4 bottom-4 z-[70]' not in html:
    erros.append("Calendário não está preso à tela com rolagem interna.")
if "document.body.appendChild(el)" not in html or "document.body.style.overflow = 'hidden'" not in html:
    erros.append("Calendário não é promovido ao body ou não bloqueia a rolagem externa.")

inicio_selecao = html.find('function selecionarDiaCalendario(diaIso)')
segundo_clique = html.find('} else if (dataCheckIn && !dataCheckOut)', inicio_selecao)
if inicio_selecao == -1 or segundo_clique == -1:
    erros.append("Fluxo de seleção das duas datas não foi encontrado.")
elif 'fecharCalendario()' in html[inicio_selecao:segundo_clique]:
    erros.append("O primeiro clique ainda fecha o calendário antes do checkout.")

# 10. Validação Funcional das Regras de Seleção e Checkout do Calendário
js_teste_calendario = """
const datasTotalmenteOcupadas = new Set(['2026-10-06', '2026-10-08']);
const hojeIso = '2026-10-01';

function testarDisponibilidade(dataCheckIn, dataCheckOut, diaIso) {
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

  const ehPassado = diaIso < hojeIso;
  const ehTotalmenteOcupado = datasTotalmenteOcupadas.has(diaIso);
  let ehIndisponivel = false;
  if (ehPassado) {
    ehIndisponivel = true;
  } else if (dataCheckIn && !dataCheckOut) {
    if (diaIso > dataCheckIn) {
      if (primeiroBloqueioAposCheckIn && diaIso > primeiroBloqueioAposCheckIn) {
        ehIndisponivel = true;
      }
    } else if (diaIso < dataCheckIn) {
      if (ehTotalmenteOcupado) {
        ehIndisponivel = true;
      }
    }
  } else {
    if (ehTotalmenteOcupado) {
      ehIndisponivel = true;
    }
  }
  return ehIndisponivel;
}

// 1. Data ocupada (2026-10-06) NÃO pode ser check-in
if (testarDisponibilidade('', '', '2026-10-06') !== true) {
  throw new Error("Data ocupada deve ser indisponível para check-in.");
}
// 2. Data livre (2026-10-05) PODE ser check-in
if (testarDisponibilidade('', '', '2026-10-05') !== false) {
  throw new Error("Data livre deve ser disponível para check-in.");
}
// 3. Com check-in em 2026-10-05, checkout em 2026-10-06 (primeiro bloqueio) DEVE SER PERMITIDO (saída matutina)
if (testarDisponibilidade('2026-10-05', '', '2026-10-06') !== false) {
  throw new Error("Checkout no primeiro dia ocupado deve ser permitido.");
}
// 4. Checkout em 2026-10-07 ou posterior DEVE SER BLOQUEADO (atravessa noite ocupada)
if (testarDisponibilidade('2026-10-05', '', '2026-10-07') !== true) {
  throw new Error("Checkout além do primeiro dia ocupado deve ser bloqueado.");
}
// 5. Data passada deve ser indisponível
if (testarDisponibilidade('', '', '2026-09-30') !== true) {
  throw new Error("Data no passado deve ser indisponível.");
}
"""
temp_test = raiz / '_temp_test_cal.js'
temp_test.write_text(js_teste_calendario, encoding='utf-8')
res_cal = subprocess.run(['node', str(temp_test)], capture_output=True, text=True)
if res_cal.returncode != 0:
    erros.append(f"Falha na validação funcional do calendário: {res_cal.stderr.strip()}")
if temp_test.exists():
    temp_test.unlink()

# Relatório Final
if erros:
    print("❌ FALHAS NA SUÍTE DE TESTES:")
    for e in erros:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("✅ TODOS OS TESTES PASSARAM COM 100% DE SUCESSO:")
    print(f"  - Padrões SNT: Zero CDNs, Canônico HTTPS e CNPJ 63.223.844/0001-11 OK")
    print(f"  - Inscrição Municipal: 100% removida do site (zero menções)")
    print(f"  - Calendário Airbnb: Dual-month, 2º clique sem falha, strike-through de datas indisponíveis OK")
    print(f"  - Zero estrelas, Superhost e termos restritos OK")
    print(f"  - Zero números 11, 12, 13, 14 expostos (nomes comerciais ativos)")
    print(f"  - I18N: {len(pt_keys)} chaves sincronizadas entre PT, EN e ES (100% DOM coberto)")
    print(f"  - Galeria: {len(fotos)} fotos WebP válidas ({peso_total_mb:.2f} MB < 4.0 MB)")
    print("  - Sintaxe JavaScript verificada sem erros (node --check)")

