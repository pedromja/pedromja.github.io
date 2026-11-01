# Pedido ao Grok Bot — trabalho pendente (01/11/2026)

Este ficheiro junta **tudo o que está pendente** para o Grok. Substitui os pedidos anteriores ainda abertos. Por ordem de prioridade.

## 0. Regras (não mudam)
- **Só leitura pública.** Nunca contactar vendedores, preencher formulários, pedir VIN/SoH por email/chat, nem enviar mensagens em nome do Pedro.
- Não contornar anti-bot (Cloudflare, Vercel; mobile.de, Bilbasen, La Centrale, Gaspedaal, AutoUncle, dasparking): sem proxies, sem mudar o user-agent, sem o PC do Pedro. Bloqueou → `sem_leitura` e seguir.
- Pausas de 20–30 s entre pedidos ao mesmo site; parar ao primeiro código ≠ 200 repetido.
- Segredos e logins: nunca em texto; só através do bot COFRE. Bancos, pagamentos e serviços do Estado: perguntar sempre antes.
- Sem dados pessoais de particulares. Copiar textos e números tal como aparecem; nada inventado.
- O modelo de pontuação (v8) é do Claude Code: o Grok **não** pontua nem propõe veredictos, só recolhe dados.

## 1. Atualização de regra: 6 meses contados a 10/12/2026
O carro tem de estar em casa a 15/12/2026. Com margem para a viagem desde a Alemanha (≈ 2.300 km, 3–4 dias), a **entrega conta-se a 10/12/2026**.
- Um carro só paga IVA PT se, **a 10/12/2026**, tiver ≤ 6 meses desde a 1.ª matrícula **ou** ≤ 6.000 km.
- Usar sempre a **data exata** da 1.ª matrícula (`primeira_matricula_exata`); 6 meses a 10/12 = matrícula até **09/06/2026**.
- Nos resumos, o filtro "<6 meses" passa a "<6 meses a 10/12/2026". O `posto_v7` pode continuar pelo método antigo: o Claude Code recalcula.

## 2. Listas do Finder de Cross Turismo e Sport Turismo (prioridade alta)
As listas de 31/10–01/11 foram só de **berlinas** (DE, AT, NL, BE, LU, FR). Mas **46 dos 68 finalistas disponíveis são CT ou ST**. Fazer as mesmas listas, no mesmo formato JSON (`carros`, `ignorados`, `lista_bruta`, com `flags`, `modelYear`, `primeira_matricula_exata`, `vin`, `preco_eur`, `equipamento_opcional`, SoH, acidente, demo, reserva):
- **Carroçarias:** Cross Turismo e Sport Turismo (no Finder: `body-type` correspondente; se o filtro não existir, ler tudo e separar pelo `bodyType`).
- **Países:** DE, AT, NL, BE, LU, FR (como as berlinas) e também IT, ES, SI, HR, PL, CZ, HU, SE, DK. Fora: CH e NO (alfândega), PT só para referência.
- **Condição:** usados + Porsche Approved; até 140.000 €.
- **1.ª matrícula:** de **03/2024** a 06/2026 (nos CT/ST os melhores negócios atuais são de 2024–2025: Lüneburg 06/2025, Leipzig 11/2024, Holzwickede 05/2024). Se o Pedro quiser a janela das berlinas (06/2025–06/2026), ele diz.
- Ficheiros: `finder_<PAÍS>_CTST_<data>.json` + `_resumo.md`, como nas berlinas.
- Depois, **berlinas** nos países que faltam (IT, ES, SI, HR, PL, CZ, HU, SE, DK), mesma janela das berlinas (06/2025–06/2026).

## 3. Galeria completa: certificado de bateria (SoH) e VIN nas fotos (prioridade alta)
Na recolha de VIN de 31/10 a galeria não foi aberta (só 5 fotos). Nos anúncios alemães o VIN não é publicado, mas costuma aparecer **no cabeçalho do certificado SoH** ou numa foto da placa/talão. Para cada carro abaixo: abrir a galeria completa (sem login), procurar o certificado de bateria e fotos com o VIN.
- Copiar o SoH (%), a data e os km da medição, e o VIN só se estiver **legível sem ambiguidade** (senão `vin_parcial` com o que se lê).
- Se não houver certificado nem VIN nas fotos: `sem_certificado` / `sem_vin`, com o nº de fotos vistas.

| # | Código | Versão | v8 | Posto PT | Anúncio |
|---|---|---|---|---|---|
| 1 | `240VN9` | 4S ST | Excelente 87 | 91.200 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-240VN9 |
| 2 | `4XK4Z5` | 4S | Excelente 86 | 111.270 € | https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4s-rabljeno-vozilo-4XK4Z5 |
| 3 | `447RV5` | 4S CT | Excelente 86 | 92.100 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-447RV5 |
| 4 | `DOV2XK` | 4S CT | Excelente 82 | 98.900 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-DOV2XK |
| 5 | `GE8O8Q` | 4 CT | Excelente 81 | 99.200 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-GE8O8Q |
| 6 | `QOOV28` | 4S CT | Excelente 77 | 105.200 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-QOOV28 |
| 7 | `RN9LOL` | 4S CT | Excelente 77 | 105.592 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-RN9LOL |
| 8 | `P0ZMZO` | 4 CT | Excelente 75 | 85.090 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-P0ZMZO |
| 9 | `EXR720` | 4S | Bom 82 | 114.894 € | https://bielefeld.porsche.de/de/inventory/porsche/porsche-taycan-4s-gebraucht-EXR720 |
| 10 | `3K674M` | GTS | Bom 80 | 116.200 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-3K674M |
| 11 | `9PERGW` | 4S | Bom 80 | 114.200 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-9PERGW |
| 12 | `P4E37O` | 4S CT | Bom 78 | 116.200 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-P4E37O |
| 13 | `08NZ42` | 4 | Bom 77 | 109.406 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-08NZ42 |
| 14 | `0DQ4LD` | 4 | Bom 74 | 91.190 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-gebraucht-0DQ4LD |
| 15 | `L6L9QX` | Taycan ST | Bom 74 | 90.200 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-L6L9QX |
| 16 | `L85WP9` | Taycan | Bom 74 | 94.280 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gebraucht-L85WP9 |
| 17 | `ZE9KKV` | 4S CT | Bom 74 | 112.989 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-ZE9KKV |
| 18 | `NKP7ZL` | 4S CT | Bom 72 | 99.200 € | https://finder.porsche.com/it/it-IT/details/porsche-taycan-4s-cross-turismo-usata-NKP7ZL |
| 19 | `G7PR3N` | 4S CT | Bom 72 | 98.800 € | https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-4s-cross-turismo-occasion-G7PR3N |
| 20 | `L6LK9X` | 4 CT | Bom 72 | 84.290 € | https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4-cross-turismo-rabljeno-vozilo-L6LK9X |
| 21 | `M27W88` | 4 CT | Bom 72 | 103.800 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-M27W88 |
| 22 | `QOZG8Z` | 4S CT | Bom 71 | 106.050 € | https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-4s-cross-turismo-occasion-QOZG8Z |
| 23 | `9ZPDNO` | 4 CT | Bom 71 | 101.290 € | https://finder.porsche.com/at/de-AT/details/porsche-taycan-4-cross-turismo-gebraucht-9ZPDNO |
| 24 | `4G4RMZ` | Taycan | Bom 71 | 86.200 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gebraucht-4G4RMZ |
| 25 | `56837M` | 4 | Bom 71 | 106.100 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-56837M |
| 26 | `9NR67P` | 4 CT | Bom 71 | 98.200 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-9NR67P |
| 27 | `440L9Q` | Taycan ST | Bom 70 | 83.012 € | https://finder.porsche.com/pl/pl-PL/details/porsche-taycan-sport-turismo-uzywany-440L9Q |
| 28 | `4W8ZV9` | 4 CT | Bom 69 | 101.170 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-4W8ZV9 |
| 29 | `64K0VD` | 4 | Bom 69 | 104.100 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-64K0VD |
| 30 | `NK2E7V` | GTS ST | Bom 69 | 110.100 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-NK2E7V |
| 31 | `89NVDM` | 4 CT | Bom 68 | 102.110 € | https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4-cross-turismo-rabljeno-vozilo-89NVDM |
| 32 | `08R6GN` | 4 CT | Bom 68 | 106.100 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-08R6GN |
| 33 | `4WZ5L5` | 4 CT | Bom 68 | 107.960 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-4WZ5L5 |
| 34 | `7K8X47` | Taycan | Bom 68 | 101.100 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-black-edition-gebraucht-7K8X47 |
| 35 | `9N3DOW` | 4S ST | Bom 67 | 116.836 € | https://finder.porsche.com/lu/fr-LU/details/porsche-taycan-4s-sport-turismo-doccasion-9N3DOW |
| 36 | `ENLX0K` | Taycan | Bom 67 | 102.800 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-black-edition-gebraucht-ENLX0K |
| 37 | `WZ7NZ4` | Taycan ST | Bom 66 | 99.250 € | https://finder.porsche.com/at/de-AT/details/porsche-taycan-sport-turismo-gebraucht-WZ7NZ4 |
| 38 | `V3MP6K` | Taycan | Bom 66 | 101.250 € | https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-occasion-V3MP6K |
| 39 | `36P53Z` | 4S | Bom 65 | 109.200 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-36P53Z |
| 40 | `3K8R6M` | Taycan ST | Bom 65 | 81.250 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-3K8R6M |
| 41 | `36MEXV` | 4 CT | Bom 64 | 84.270 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-36MEXV |
| 42 | `7WOZLW` | 4 CT | Bom 63 | 101.290 € | https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4-cross-turismo-rabljeno-vozilo-7WOZLW |
| 43 | `XG828E` | Taycan ST | Bom 63 | 81.190 € | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-XG828E |

Formato: `galeria_soh_vin_<data>.json`, um objeto por carro: `codigo, url, verificado_em, n_fotos_vistas, soh_pct, soh_data, soh_km, soh_texto, vin, vin_parcial, vin_fonte (ex.: "foto 14, certificado SoH"), notas`.

## 4. Dúvidas concretas por anúncio (prioridade média)
| Código | O que confirmar (só pelo anúncio público) |
|---|---|
| `V3MP6K` (Amsterdam, Taycan, Bom 66) | Estado de acidente: o Finder NL não mostra o campo. Procurar "schadevrij" / "ongevalvrij" / historial na descrição e nas fotos. |
| `QOZG8Z` (Oisterwijk 4S CT) | "Approved 35 meses" lido a 31/10: é garantia restante, duração do contrato ou erro de leitura? Copiar o texto exato. |
| `QOWVKW` (Frankfurt 4S ST Black Edition) | HD-Matrix (8IU) e BOSE (9VL): o AS24 destaca-os, a lista do Finder não. Ver a lista completa e os destaques. |
| `4WZ5L5` (Frankfurt 4 CT) | Os 2.025 € de "Überführung und Zulassung" continuam no preço? |
| Todos da secção 3 | Data de disponibilidade (`disponibilidade` / "verfügbar ab"): se for depois de 10/12/2026, dizer. |
| Todos da secção 3 | A lista de opções tem **QK3** (pré-instalação de dashcam)? Tem Porsche Dashcam montada? |

## 5. Rotina diária (continua)
Todos os dias de manhã, estado e preço dos finalistas disponíveis (Excelente/Bom no v8) e dos reservados, no formato `finder_estado_<data>.json` (`codigo, url, verificado_em, estado: ativo|reservado|vendido|desaparecido|sem_leitura, texto_estado, preco, moeda`).

**Disponíveis (68):** [`EXGVO6`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-gebraucht-EXGVO6), [`NK804N`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-NK804N), [`f512a3a2`](https://www.autoscout24.com/offers/porsche-taycan-cross-turismo-turbo-s-pccb-offrod-carbon-electric-red-cat_ma57mo75273-f512a3a2-9411-41eb-ac1b-3f66d948411d), [`240VN9`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-240VN9), [`4XK4Z5`](https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4s-rabljeno-vozilo-4XK4Z5), [`447RV5`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-447RV5), [`K5PRPG`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-K5PRPG), [`DOV2XK`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-DOV2XK), [`GE8O8Q`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-GE8O8Q), [`QOOV28`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-QOOV28), [`RN9LOL`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-RN9LOL), [`P0ZMZO`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-P0ZMZO), [`QOLVR2`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-s-gebraucht-QOLVR2), [`3KDW90`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-s-gebraucht-3KDW90), [`4317baae`](https://www.autoscout24.com/offers/porsche-taycan-turbo-s-951-ps-approved-np-240k-abs-vollaus-electric-silver-cat_ma57mo75273-4317baae-2008-45a5-8d95-9d0f589ebe9f), [`L6683Z`](https://finder.porsche.com/be/nl-BE/details/porsche-taycan-gts-occasie-L6683Z), [`8299NL`](https://finder.porsche.com/it/it-IT/details/porsche-taycan-turbo-s-cross-turismo-usata-8299NL), [`NP93G9`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-gebraucht-NP93G9), [`L68W39`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-L68W39), [`EXR720`](https://bielefeld.porsche.de/de/inventory/porsche/porsche-taycan-4s-gebraucht-EXR720), [`PVRZW4`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-sport-turismo-gebraucht-PVRZW4), [`3K674M`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-3K674M), [`9PERGW`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-9PERGW), [`D4NE7E`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-sport-turismo-gebraucht-D4NE7E), [`EXVW46`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-EXVW46), [`P4E37O`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-P4E37O), [`RNR8XL`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-cross-turismo-gebraucht-RNR8XL), [`829P4Q`](https://finder.porsche.com/be/nl-BE/details/porsche-taycan-turbo-cross-turismo-occasie-829P4Q), [`08NZ42`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-08NZ42), [`V97W6K`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-cross-turismo-gebraucht-V97W6K), [`4G5ZPZ`](https://finder.porsche.com/be/nl-BE/details/porsche-taycan-gts-sport-turismo-occasie-4G5ZPZ), [`0DQ4LD`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-gebraucht-0DQ4LD), [`K7Q3WM`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-K7Q3WM), [`L6L9QX`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-L6L9QX), [`L85WP9`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-gebraucht-L85WP9), [`WKEEVM`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-WKEEVM), [`ZE9KKV`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-ZE9KKV), [`NKP7ZL`](https://finder.porsche.com/it/it-IT/details/porsche-taycan-4s-cross-turismo-usata-NKP7ZL), [`G7PR3N`](https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-4s-cross-turismo-occasion-G7PR3N), [`L6LK9X`](https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4-cross-turismo-rabljeno-vozilo-L6LK9X), [`M27W88`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-M27W88), [`ZO5ORE`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-ZO5ORE), [`QOZG8Z`](https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-4s-cross-turismo-occasion-QOZG8Z), [`9ZPDNO`](https://finder.porsche.com/at/de-AT/details/porsche-taycan-4-cross-turismo-gebraucht-9ZPDNO), [`4G4RMZ`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-gebraucht-4G4RMZ), [`56837M`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-56837M), [`9NR67P`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-9NR67P), [`440L9Q`](https://finder.porsche.com/pl/pl-PL/details/porsche-taycan-sport-turismo-uzywany-440L9Q), [`4W8ZV9`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-4W8ZV9), [`64K0VD`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-64K0VD), [`NK2E7V`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-NK2E7V), [`89NVDM`](https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4-cross-turismo-rabljeno-vozilo-89NVDM), [`08R6GN`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-08R6GN), [`4WZ5L5`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-4WZ5L5), [`7K8X47`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-black-edition-gebraucht-7K8X47), [`9N3DOW`](https://finder.porsche.com/lu/fr-LU/details/porsche-taycan-4s-sport-turismo-doccasion-9N3DOW), [`ENLX0K`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-black-edition-gebraucht-ENLX0K), [`L9KVZZ`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-L9KVZZ), [`WZ7NZ4`](https://finder.porsche.com/at/de-AT/details/porsche-taycan-sport-turismo-gebraucht-WZ7NZ4), [`G076Q0`](https://finder.porsche.com/lv/lv-LV/details/porsche-taycan-turbo-cross-turismo-lietota-G076Q0), [`V3MP6K`](https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-occasion-V3MP6K), [`36P53Z`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-36P53Z), [`3K8R6M`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-3K8R6M), [`0DK364`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-0DK364), [`36MEXV`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-36MEXV), [`64P8WP`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-64P8WP), [`7WOZLW`](https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4-cross-turismo-rabljeno-vozilo-7WOZLW), [`XG828E`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-XG828E)

**Reservados (11) — ver se a reserva cai:** [`4W3QKZ`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-4W3QKZ), [`D4NK4K`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-D4NK4K), [`EKKZQ5`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-EKKZQ5), [`K5KV2X`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-K5KV2X), [`KP920D`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-KP920D), [`NKOZ7L`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-NKOZ7L), [`ON3PM9`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-ON3PM9), [`PV25WO`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-PV25WO), [`RNW5NL`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-RNW5NL), [`WZVRQM`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-WZVRQM), [`XWKENP`](https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-XWKENP)

Assinalar logo no resumo: qualquer **descida de preço**, reserva nova, vendido, ou reserva que caiu.

## 6. Entrega
- Um zip por lote com os JSON + um `LEIA-ME.md` curto (o que foi lido, quando, quantos bloqueados).
- Nada de páginas brutas com dados pessoais; tokens e emails removidos, como até aqui.
- Ordem sugerida: secção 1 (só ajustar), 5 (diária), 3, 2, 4.
