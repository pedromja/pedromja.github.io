# Pedido ao Grok Bot — VIN em falta dos candidatos Taycan (31/10/2026)

## Objetivo
Ler o **VIN (número de quadro)** de cada carro abaixo, a partir do próprio anúncio (Porsche Finder, site do Porsche Zentrum ou AutoScout24), para:
1. confirmar o **ano-modelo** pelo 10.º carácter (S = MY2025 · T = MY2026 · V = MY2027 · R/P = pré-facelift);
2. saber se tem o **PCM antigo (MY2025) ou novo (MY2026)** — já vimos que carros de demonstração matriculados em 10/2025–02/2026 podem ser MY2025;
3. cruzar com a lista **TI 48/26** dos módulos de bateria (o cruzamento faço eu no Claude Code; não é preciso o Grok o fazer).

Já temos o VIN de: Ljubljana 4XK4Z5 e 7WOZLW, Innsbruck 9ZPDNO, Szczecin 6OOQPP e K55WOM, Wien EKX7D5, Sevilha 8O82R3. **Não repetir.**

## Regras (iguais às de sempre)
- **Só leitura pública.** Nunca contactar vendedores, preencher formulários, pedir o VIN por email/chat ou enviar mensagens em nome do Pedro.
- Não contornar anti-bot (Cloudflare, Vercel, mobile.de, Bilbasen, La Centrale, Gaspedaal, AutoUncle, dasparking): sem proxies, sem mudar o user-agent, sem o PC do Pedro. Se bloquear → `sem_leitura`.
- Pausas de 20–30 s entre pedidos ao mesmo site.
- Copiar o VIN **exatamente** como aparece (17 caracteres). Não inventar nem completar VIN parciais: se só aparecer parte, copiar a parte e marcar `vin_parcial: true`.
- Se o anúncio não mostrar VIN, procurar o campo **"Modelljahr" / "Model year" / "Modelno leto"** (às vezes aparece sem VIN) e registá-lo à parte.
- Onde procurar no Porsche Finder: secção "Fahrzeugdetails / Technische Daten" (campo "FIN" / "Fahrgestellnummer" / "VIN"), PDF da ficha do carro se houver link, e fotos do certificado de bateria (SoH), que muitas vezes mostram o VIN no cabeçalho. Nas fotos, só copiar se estiver legível sem ambiguidade.
- Aproveitar para registar o **estado** do anúncio (ativo / reservado / vendido / desaparecido) e o **preço** atual.

## Prioridade 1 — posto em PT ≤ 115.000 € (38 carros)
| # | Código | Versão | Cidade | 1.ª matr. | km | Posto PT | v8 | Anúncio |
|---|---|---|---|---|---|---|---|---|
| 1 | `NK804N` | 4S CT | Lüneburg | 06/2025 | 41.250 km | 89.200 € | Excelente 92 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-NK804N |
| 2 | `240VN9` | 4S ST | Stuttgart | 09/2024 | 54.200 km | 91.200 € | Excelente 87 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-240VN9 |
| 3 | `447RV5` | 4S CT | Leipzig | 11/2024 | 20.435 km | 92.100 € | Excelente 86 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-447RV5 |
| 4 | `DOV2XK` | 4S CT | Düsseldorf | 10/2025 | 24.900 km | 98.900 € | Excelente 81 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-DOV2XK |
| 5 | `GE8O8Q` | 4 CT | Regensburg | 01/2026 | 9.400 km | 99.200 € | Excelente 81 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-GE8O8Q |
| 6 | `QOOV28` | 4S CT | Berlin | 08/2025 | 26.554 km | 105.200 € | Excelente 77 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-QOOV28 |
| 7 | `RN9LOL` | 4S CT | Holzwickede | 05/2024 | 3.155 km | 105.592 € | Excelente 76 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-RN9LOL |
| 8 | `P0ZMZO` | 4 CT | Diez | 08/2025 | 15.885 km | 85.090 € | Excelente 75 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-P0ZMZO |
| 9 | `EXR720` | 4S | Bielefeld | 03/2025 | 4.967 km | 114.894 € | Bom 82 | https://bielefeld.porsche.de/de/inventory/porsche/porsche-taycan-4s-gebraucht-EXR720 |
| 10 | `9PERGW` | 4S | Kassel | 09/2025 | 23.900 km | 114.200 € | Bom 80 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-9PERGW |
| 11 | `08NZ42` | 4 | Trier | 08/2026 | 7.000 km | 109.406 € | Bom 77 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-08NZ42 |
| 12 | `0DQ4LD` | 4 | Recklinghausen | 07/2025 | 26.960 km | 91.190 € | Bom 74 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-gebraucht-0DQ4LD |
| 13 | `L6L9QX` | Taycan ST | Köln | 06/2025 | 8.443 km | 90.200 € | Bom 74 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-L6L9QX |
| 14 | `L85WP9` | Taycan | Bremen | 12/2024 | 12.500 km | 94.280 € | Bom 74 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gebraucht-L85WP9 |
| 15 | `WKEEVM` | 4S | Holzwickede | 03/2025 | 20.281 km | 99.190 € | Bom 74 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-WKEEVM |
| 16 | `ZE9KKV` | 4S CT | Ettlingen | 07/2025 | 23.900 km | 112.989 € | Bom 74 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-ZE9KKV |
| 17 | `ON3PM9` | 4S ST | Essen | 05/2025 | 15.276 km | 109.200 € | Bom 73 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-ON3PM9 |
| 18 | `G7PR3N` | 4S CT | Leusden | 10/2024 | 35.916 km | 98.800 € | Bom 72 | https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-4s-cross-turismo-occasion-G7PR3N |
| 19 | `L6LK9X` | 4 CT | Ljubljana | 05/2024 | 77.009 km | 84.290 € | Bom 72 | https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4-cross-turismo-rabljeno-vozilo-L6LK9X |
| 20 | `M27W88` | 4 CT | München | 11/2025 | 15.000 km | 103.800 € | Bom 72 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-M27W88 |
| 21 | `QOZG8Z` | 4S CT | Oisterwijk | 07/2024 | 25.615 km | 106.050 € | Bom 71 | https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-4s-cross-turismo-occasion-QOZG8Z |
| 22 | `4G4RMZ` | Taycan | Winhöring | 07/2025 | 28.100 km | 86.200 € | Bom 71 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gebraucht-4G4RMZ |
| 23 | `4W3QKZ` | 4S ST | Willich | 03/2025 | 45.900 km | 111.200 € | Bom 71 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-4W3QKZ |
| 24 | `9NR67P` | 4 CT | Gilching-Argelsried | 12/2025 | 9.900 km | 98.200 € | Bom 71 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-9NR67P |
| 25 | `440L9Q` | Taycan ST | Szczecin | 09/2024 | 26.774 km | 83.012 € | Bom 70 | https://finder.porsche.com/pl/pl-PL/details/porsche-taycan-sport-turismo-uzywany-440L9Q |
| 26 | `NKP7ZL` | 4S CT | Milano | 05/2024 | 22.693 km | 101.200 € | Bom 69 | https://finder.porsche.com/it/it-IT/details/porsche-taycan-4s-cross-turismo-usata-NKP7ZL |
| 27 | `4W8ZV9` | 4 CT | Offenburg | 10/2025 | 9.911 km | 101.170 € | Bom 69 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-4W8ZV9 |
| 28 | `NK2E7V` | GTS ST | Leipzig | 05/2025 | 59.146 km | 110.100 € | Bom 69 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-NK2E7V |
| 29 | `89NVDM` | 4 CT | Ljubljana | 12/2025 | 4.561 km | 102.110 € | Bom 68 | https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4-cross-turismo-rabljeno-vozilo-89NVDM |
| 30 | `4WZ5L5` | 4 CT | Frankfurt/Main | 01/2026 | 9.999 km | 107.960 € | Bom 68 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-4WZ5L5 |
| 31 | `L9KVZZ` | 4 CT | Frankfurt am Main | 04/2025 | 14.952 km | 95.960 € | Bom 67 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-L9KVZZ |
| 32 | `WZ7NZ4` | Taycan ST | Graz-Liebenau | 06/2025 | 20.698 km | 99.250 € | Bom 66 | https://finder.porsche.com/at/de-AT/details/porsche-taycan-sport-turismo-gebraucht-WZ7NZ4 |
| 33 | `36P53Z` | 4S | Stuttgart | 10/2024 | 8.400 km | 109.200 € | Bom 65 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-36P53Z |
| 34 | `3K8R6M` | Taycan ST | Bonn | 05/2025 | 34.590 km | 81.250 € | Bom 65 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-3K8R6M |
| 35 | `36MEXV` | 4 CT | Hamburg | 04/2025 | 19.765 km | 84.270 € | Bom 64 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-36MEXV |
| 36 | `PV25WO` | Taycan ST | Holzwickede | 10/2024 | 33.608 km | 78.990 € | Bom 64 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-PV25WO |
| 37 | `08R6GN` | 4 CT | Leipzig | 05/2026 | 8.900 km | 109.623 € | Bom 63 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-08R6GN |
| 38 | `XG828E` | Taycan ST | Estenfeld | 07/2024 | 25.500 km | 81.190 € | Bom 63 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-XG828E |

## Prioridade 2 — posto entre 115.000 e 122.000 € (negociáveis) (8 carros)
| # | Código | Versão | Cidade | 1.ª matr. | km | Posto PT | v8 | Anúncio |
|---|---|---|---|---|---|---|---|---|
| 1 | `EXGVO6` | Turbo | Ulm | 04/2024 | 73.900 km | 116.290 € | Excelente 99 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-gebraucht-EXGVO6 |
| 2 | `K5PRPG` | GTS ST | Regensburg | 07/2025 | 52.800 km | 118.200 € | Excelente 84 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-K5PRPG |
| 3 | `3K674M` | GTS | Soest | 07/2025 | 28.100 km | 116.200 € | Bom 80 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-3K674M |
| 4 | `EXVW46` | GTS ST | Leipzig | 02/2025 | 31.885 km | 121.100 € | Bom 78 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-EXVW46 |
| 5 | `P4E37O` | 4S CT | Hilzingen | 07/2025 | 21.500 km | 116.200 € | Bom 78 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-P4E37O |
| 6 | `ZO5ORE` | GTS ST | Münster | 02/2025 | 30.600 km | 118.100 € | Bom 71 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-ZO5ORE |
| 7 | `9N3DOW` | 4S ST | Roost | 09/2025 | 4.996 km | 116.836 € | Bom 67 | https://finder.porsche.com/lu/fr-LU/details/porsche-taycan-4s-sport-turismo-doccasion-9N3DOW |
| 8 | `64P8WP` | 4 CT | Soest | 06/2026 | 6.990 km | 118.367 € | Bom 64 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-64P8WP |

(Excluídos de propósito: carros vendidos/reservados/retirados, os disponíveis só depois de 15/12/2026 — Zagreb Z52DNE e O6E7Q9, Winhöring 4XNV25 — e os acima de 122.000 €.)

## Formato da resposta
Um ficheiro `vin_candidatos_2026-MM-DD.json` (lista), um objeto por carro:
```json
{
  "codigo": "NK804N",
  "url": "https://finder.porsche.com/...",
  "verificado_em": "2026-11-01T10:15",
  "estado": "ativo | reservado | vendido | desaparecido | sem_leitura",
  "preco": 87900,
  "vin": "WP0ZZZY1....... (17 caracteres) ou null",
  "vin_parcial": false,
  "vin_fonte": "Finder Fahrzeugdetails | PDF ficha | foto certificado SoH | AutoScout24 | site PZ",
  "modelljahr_texto": "Modelljahr 2025 (se aparecer; senão null)",
  "pcm_texto": "qualquer menção ao PCM / ecrã / software, copiada tal como aparece (ou null)",
  "notas": "texto livre; se sem_leitura, dizer porquê (desafio Cloudflare, time-out, campo inexistente…)"
}
```
Mais um resumo curto em `.md`: quantos VIN lidos, quantos sem VIN no anúncio, quantos bloqueados.
