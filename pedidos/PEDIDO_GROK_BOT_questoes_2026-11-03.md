# Pedido ao Grok Bot — questões em aberto (03/11/2026)

Junta tudo o que o Claude Code ainda precisa do Grok. Substitui as partes abertas dos pedidos de 31/10 e 01/11. Por ordem de prioridade.

## 0. Regras (iguais)
- Só leitura pública. Nunca contactar vendedores, preencher formulários ou pedir dados por email ou chat em nome do Pedro.
- Não contornar anti-bot. Proibido usar proxy, mudar o user-agent ou usar o PC do Pedro. Se bloquear, marcar `sem_leitura`.
- Pausas de 20–30 s; um site de cada vez.
- Segredos só pelo COFRE; sem dados pessoais de particulares.
- O Grok não pontua nem dá veredictos; o v8 é do Claude Code.

## 1. Foco novo do Pedro: berlina, PCM novo, eixo traseiro (prioridade alta)
O Pedro está a dar preferência a:
- berlina, com InnoDrive (P4S) e 4+1 (5KA), que continuam obrigatórios;
- **PCM novo** (MY2026: software 4578, VIN com T na 10.ª posição);
- **eixo traseiro direcional (0N5)**;
- **aviso de ângulo morto (7Y8)**;
- **Surround View com estacionamento ativo (FT3)**, e de preferência **Remote ParkAssist (FT1)**.

O orçamento passa para segundo plano.

Para cada carro da tabela, abrir a ficha completa e devolver:
- os códigos acima (sim, não ou não indicado) e também QK3 (pré-instalação de dashcam);
- o ano-modelo:
  - `modelYear`;
  - o VIN, se aparecer em qualquer lado;
  - a data de produção;
  - "Modelljahr 2027" ou algo equivalente;
  - qualquer menção a "PCM 4578", "App Center", ou a um sistema Android ou de nova geração;
- a disponibilidade ("Verfügbar ab"), o SoH, as garantias, se é carro de demonstração e o estado (ativo, reservado ou vendido, lido **na ficha**);
- se as fotos são reais ou geradas pelo configurador (rendered).

| Código | Carro | Onde |
|---|---|---|
| `08NZ42` | 4 Black Edition 08/2026 | PZ Trier |
| `NQV3RV` | 4 10/2025 (baixou para 104.900 €) | PZ Hannover |
| `6476R5` | Taycan 12/2025 | PZ Hannover |
| `M4EGLE` | 4S 03/2026 | PZ Wettenberg |
| `L68W39` | 4S 02/2026, 2.868 km | PZ Bielefeld |
| `20P2V5` | 4 07/2026 | PZ Bonn |
| `EXDW85` | 4S 08/2026 | PZ Bergisch Gladbach |
| `7N04NW` | GTS 07/2026 | PZ Bonn |
| `56837M` | 4 05/2026 | PZ Leipzig |
| `7K8X47` | Taycan 05/2026 | PZ Leipzig |
| `ENLX0K` | Taycan 05/2026 | PZ Kleinmachnow |
| `45ZNP9` | 4 04/2026 | PZ Estenfeld/Würzburg |
| `3K674M` | GTS 07/2025 (galeria só com imagens do configurador) | PZ Soest |
| `4556XQ` | Taycan 05/2026 (tem FT1) | PZ Soest |
| `M73KGO` | 4S 03/2026 | PZ Howald (LU) |
| `K5KV2X` | 4S 06/2025 (a reserva caiu a 03/11) | PZ Berlin-Adlershof |

**MY2027:** as berlinas matriculadas entre 07/2026 e 10/2026 podem ser MY2027, com um sistema novo baseado em Android. Se a ficha disser "Modelljahr 2027", ou o VIN tiver V na 10.ª posição, assinalar `my2027: true`.

## 2. Fichas completas de anúncios que ainda não estão no ranking (prioridade alta)
Para estes carros, além do equipamento da secção 1, preciso do **registo completo no formato excel v7** para os poder pontuar: `justo_v7`, `pen_v7`, `os`, `eq`, `opts`, `novo_origem` e `posto_v7`, calculados pelo `build_excel_v8.py`.

- **AutoScout24 `68f10d6f-3d96-41c8-a62c-183ffb0165c5`:** Taycan Black Edition **berlina** 08/2026, 6.900 km, com "HA-Lenkung" e Soft-Close. Bach Sportwagen, em Diez. Baixou de 114.900 € para **99.900 €** a 03/11.
  - Confirmar InnoDrive, 5KA, FT3, 7Y8 e FT1.
  - Confirmar se o vendedor é um stand (empresa) e que garantia dá.
  - https://www.autoscout24.com/offers/porsche-taycan-black-edition-ha-lenkung-soft-close-electric-black-cat_ma57mo75273-68f10d6f-3d96-41c8-a62c-183ffb0165c5
- **Finder `24D5M5`:** 4 Cross Turismo 06/2024, 94.900 €, Centro Porsche Bergamo. Passa todos os filtros.
- **Blocket `24906109`:** 4S 06/2024, 999.000 SEK, com película preta mate. Confirmar:
  - se o vendedor (Bilarvet) é um stand;
  - se os "5 lugares" são 4+1 (5KA);
  - a cor original;
  - se o InnoDrive (P4S) vem na lista de opções.

## 3. Regra para os estados do Finder (correção)
- **A lista de resultados não mostra reservas.** Num carro que só foi visto na lista, devolver `estado: "na_lista"` (ou `sem_ficha`) e **não** `ativo`.
- Só a ficha pode dizer `ativo`, `reservado` ou `vendido`. A 03/11, o 5675EW veio como `ativo` só por estar na lista, quando a ficha de 02/11 dizia reservado.
- Quando uma reserva cai, devolver `estado: "ativo"` e `nota: "reserva caiu"`, como fizeram a 03/11. Isso está certo.

## 4. Rotina diária do Grok (decisão do Pedro)
O diagnóstico de 03/11 propõe:
- dividir a rotina em duas fases, uma às 07:30 e outra às 08:20;
- usar um só `diario.py` que calcula as datas sozinho, com retoma pelos passos já feitos;
- baixar o `maximum-price` das pesquisas para 125.000 €;
- avisar o Pedro se, às 09:00, não existir `alerta_<hoje>.json`.

**O Claude Code concorda com a proposta.** Se o Pedro a aprovar, aplicar. Corrigir já os erros de data fixa no código (`alerta_build.py`, `final_estado.py`, `montar_estado.py`) e a frase polaca de vendido.

## 5. Dúvidas antigas ainda sem resposta (prioridade média)
| Código | O que confirmar |
|---|---|
| `V3MP6K` (Amsterdam, Taycan berlina, Bom 66) | Estado de acidentes: procurar "schadevrij" ou "ongevalvrij" na descrição e nas fotos |
| `QOZG8Z` (Oisterwijk 4S CT) | "Approved 35 meses": copiar o texto exato |
| `QOWVKW` (Frankfurt 4S ST) | HD-Matrix (8IU) e BOSE (9VL) na lista completa |
| `4WZ5L5` (Frankfurt 4 CT) | Se os 2.025 € de transferência e matrícula alemã continuam no preço |
| `L6LK9X`, `EXR720` | Repetir a galeria completa (falhou a 01/11) à procura do certificado SoH e do VIN |

## 6. Vigilância diária (continua)
- **Estado e preço de todos os Excelente e Bom disponíveis e reservados**, lidos na **ficha** e no formato `finder_estado_<data>.json`.
- **Prioridade:** as berlinas da secção 1 e os reservados recentes:
  - Lüneburg NK804N, reservado a 03/11;
  - Essen ON3PM9, reservado a 03/11;
  - Leipzig WZVRQM;
  - Hamburg NKOZ7L e KP920D.

  Ver se as reservas caem.
- **Carros vendidos que reaparecem com outro código:** comparar a 1.ª matrícula exata, os km, a cor e o concessionário com a lista de vendidos recentes:
  - Bonn 4GE07Q/L6RX2N;
  - Böblingen L66QRN, Bielefeld D458PN e Dresden XWKENP;
  - Trier L8M4WN, 5 Seen RNW5NL, Milano NKP7ZL e Szczecin 440L9Q.
- Assinalar descidas de preço em qualquer berlina facelift com InnoDrive, mesmo acima de 115.000 €.

## 7. Entrega
- Um zip por lote, com um `LEIA-ME.md` curto.
- Ficheiros:
  - `fichas_berlinas_<data>.json` para as secções 1 e 2, no formato `carros` das listas do Finder, com `flags`, `equipamento_opcional` completo, `modelYear`, `vin` e `primeira_matricula_exata`;
  - `finder_estado_<data>.json` para a secção 6.
- Sem páginas em bruto com dados pessoais.
