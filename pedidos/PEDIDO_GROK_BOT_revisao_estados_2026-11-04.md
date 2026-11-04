# Pedido ao Grok Bot — revisão completa de vendidos e reservados (04/11/2026)

O Pedro reparou que várias mudanças de estado (vendidos, reservas novas, reservas que caíram) ainda não estão no site. Preciso de uma **revisão completa, carro a carro, lida na ficha de cada anúncio**, de todos os carros abaixo.

## Regras
- Só leitura pública. Nunca contactar vendedores nem preencher formulários.
- Não contornar anti-bot: sem proxies, sem mudar o user-agent, sem o PC do Pedro. Se bloquear, `sem_leitura`.
- Pausas de 20–30 s; um pedido de cada vez.
- **Estado só pela ficha:**
  - `reservado` quando o selo «Reserviert durch einen Kunden» (ou o equivalente na língua local) aparece como selo, e não só no dicionário de traduções da página. É a regra das 3 ocorrências que usaram a 03/11.
  - `vendido` quando a ficha diz «Dieser Porsche wurde verkauft», «reeds verkocht», «è stata venduta», etc.
  - `desaparecido` quando o anúncio já não existe (404 ou redireciona para a pesquisa).
  - `ativo` quando a ficha abre normalmente, sem selo.
  - **Não usar `na_lista` neste pedido.**
- Para AutoScout24 e outros portais: `ativo` se o anúncio está online, `desaparecido` se saiu. Se houver texto de vendido ou reservado, copiá-lo.
- Registar também o **preço atual** (e a moeda) e os **km**, se mudaram.
- Assinalar `possivel_reaparecido` se encontrar, na mesma pesquisa, um anúncio novo com a mesma 1.ª matrícula exata, os mesmos km, a mesma cor e o mesmo concessionário de um carro vendido.

## Carros a rever (226)
Estão aqui:
- todos os Excelente e Bom;
- os Justo com InnoDrive e 4+1;
- as berlinas da secção «Berlinas ★»;
- todos os que o site tem como reservados;
- os vendidos recentes de Excelente, Bom ou Justo, para confirmar que não voltaram.

A coluna «estado no site» é o que temos hoje. Se a ficha disser outra coisa, é isso que tem de vir.

Contagem por estado no site: {'ativo': 182, 'vendido': 18, 'reservado': 25, 'desaparecido': 1}. Por portal: {'Finder': 217, 'AutoScout24': 7, 'outro': 2}.

| # | Código | Versão | Cidade | v8 | Estado no site | Portal | Anúncio |
|---|---|---|---|---|---|---|---|
| 1 | `EXGVO6` | Turbo | Ulm (DE) | Excelente 100 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-gebraucht-EXGVO6 |
| 2 | `D458PN` | 4S | Bielefeld (DE) | Excelente 98 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-D458PN |
| 3 | `XWKENP` | 4S CT | Dresden (DE) | Excelente 95 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-XWKENP |
| 4 | `L66QRN` | Taycan | Böblingen (DE) | Excelente 94 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gebraucht-L66QRN |
| 5 | `NK804N` | 4S CT | Lüneburg (DE) | Excelente 92 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-NK804N |
| 6 | `QVWE26` | 4S | Recklinghausen (DE) | Excelente 92 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-QVWE26 |
| 7 | `4GE07Q` | 4S ST | Bonn (DE) | Excelente 90 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-L6RX2N |
| 8 | `f512a3a2` | Turbo S CT | Stuhr-Seckenhausen (DE) | Excelente 90 | **ativo** | AutoScout24 | https://www.autoscout24.com/offers/porsche-taycan-cross-turismo-turbo-s-pccb-offrod-carbon-electric-red-cat_ma57mo75273-f512a3a2-9411-41eb-ac1b-3f66d948411d |
| 9 | `D4NK4K` | 4 CT | Braunschweig (DE) | Excelente 90 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-D4NK4K |
| 10 | `Z52DNE` | 4S | Zagreb (HR) | Excelente 89 | **ativo** | Finder | https://finder.porsche.com/hr/hr-HR/details/porsche-taycan-4s-black-edition-rabljeno-Z52DNE |
| 11 | `240VN9` | 4S ST | Stuttgart (DE) | Excelente 87 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-240VN9 |
| 12 | `RNW5NL` | 4 CT | Gilching-Argelsried (DE) | Excelente 87 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-RNW5NL |
| 13 | `4XK4Z5` | 4S | Ljubljana (SI) | Excelente 86 | **ativo** | Finder | https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4s-rabljeno-vozilo-4XK4Z5 |
| 14 | `447RV5` | 4S CT | Leipzig (DE) | Excelente 86 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-447RV5 |
| 15 | `245PW9` | 4S | Aschaffenburg (DE) | Excelente 85 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-245PW9 |
| 16 | `K5PRPG` | GTS ST | Regensburg (DE) | Excelente 85 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-K5PRPG |
| 17 | `0O5KN2` | 4S ST | Dresden (DE) | Excelente 84 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-0O5KN2 |
| 18 | `DOV2XK` | 4S CT | Düsseldorf (DE) | Excelente 82 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-DOV2XK |
| 19 | `EKKZQ5` | 4S ST | Göttingen (DE) | Excelente 81 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-EKKZQ5 |
| 20 | `GE8O8Q` | 4 CT | Regensburg (DE) | Excelente 81 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-GE8O8Q |
| 21 | `V334OE` | 4 | Leipzig (DE) | Excelente 79 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-V334OE |
| 22 | `O6E7Q9` | 4 CT | Zagreb (HR) | Excelente 78 | **ativo** | Finder | https://finder.porsche.com/hr/hr-HR/details/porsche-taycan-4-cross-turismo-rabljeno-O6E7Q9 |
| 23 | `QOOV28` | 4S CT | Berlin (DE) | Excelente 77 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-QOOV28 |
| 24 | `RN9LOL` | 4S CT | Holzwickede (DE) | Excelente 77 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-RN9LOL |
| 25 | `RN949Z` | 4S CT | Rotterdam (NL) | Excelente 76 | **vendido** | Finder | https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-4s-cross-turismo-occasion-RN949Z |
| 26 | `G7QR2Q` | Taycan ST | Freiburg (DE) | Excelente 76 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-G7QR2Q |
| 27 | `NKOZ7L` | 4S CT | Hamburg (DE) | Excelente 76 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-NKOZ7L |
| 28 | `P0ZMZO` | 4 CT | Diez (DE) | Excelente 75 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-P0ZMZO |
| 29 | `QOLVR2` | Turbo S | Leipzig (DE) | Bom 97 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-s-gebraucht-QOLVR2 |
| 30 | `3KDW90` | Turbo S | Bielefeld (DE) | Bom 91 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-s-gebraucht-3KDW90 |
| 31 | `4317baae` | Turbo S | Helmstedt (DE) | Bom 86 | **ativo** | AutoScout24 | https://www.autoscout24.com/offers/porsche-taycan-turbo-s-951-ps-approved-np-240k-abs-vollaus-electric-silver-cat_ma57mo75273-4317baae-2008-45a5-8d95-9d0f589ebe9f |
| 32 | `L6683Z` | GTS | Ingelmunster (BE) | Bom 84 | **ativo** | Finder | https://finder.porsche.com/be/nl-BE/details/porsche-taycan-gts-occasie-L6683Z |
| 33 | `8299NL` | Turbo S CT | Milano (MI) (IT) | Bom 84 | **ativo** | Finder | https://finder.porsche.com/it/it-IT/details/porsche-taycan-turbo-s-cross-turismo-usata-8299NL |
| 34 | `NP93G9` | Turbo | Leipzig (DE) | Bom 84 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-gebraucht-NP93G9 |
| 35 | `K5KZDP` | Turbo ST | Saarbrücken (DE) | Bom 83 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-sport-turismo-gebraucht-K5KZDP |
| 36 | `L68W39` | 4S | Bielefeld (DE) | Bom 83 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-L68W39 |
| 37 | `EXR720` | 4S | Bielefeld (DE) | Bom 82 | **vendido** | outro | https://bielefeld.porsche.de/de/inventory/porsche/porsche-taycan-4s-gebraucht-EXR720 |
| 38 | `K5KV2X` | 4S | Berlin (DE) | Bom 82 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-K5KV2X |
| 39 | `PVRZW4` | Turbo ST | Leipzig (DE) | Bom 82 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-sport-turismo-gebraucht-PVRZW4 |
| 40 | `3K674M` | GTS | Soest (DE) | Bom 80 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-3K674M |
| 41 | `9PERGW` | 4S | Kassel (DE) | Bom 80 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-9PERGW |
| 42 | `RNR8XL` | Turbo CT | Leipzig (DE) | Bom 80 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-cross-turismo-gebraucht-RNR8XL |
| 43 | `4XNV25` | GTS ST | Winhöring (DE) | Bom 79 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-4XNV25 |
| 44 | `KP920D` | GTS ST | Hamburg (DE) | Bom 79 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-KP920D |
| 45 | `D4NE7E` | Turbo ST | Leipzig (DE) | Bom 78 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-sport-turismo-gebraucht-D4NE7E |
| 46 | `EXVW46` | GTS ST | Leipzig (DE) | Bom 78 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-EXVW46 |
| 47 | `P4E37O` | 4S CT | Hilzingen (DE) | Bom 78 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-P4E37O |
| 48 | `829P4Q` | Turbo CT | Ingelmunster (BE) | Bom 77 | **vendido** | Finder | https://finder.porsche.com/be/nl-BE/details/porsche-taycan-turbo-cross-turismo-occasie-829P4Q |
| 49 | `08NZ42` | 4 | Trier (DE) | Bom 77 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-08NZ42 |
| 50 | `4G5ZPZ` | GTS ST | Ingelmunster (BE) | Bom 76 | **ativo** | Finder | https://finder.porsche.com/be/nl-BE/details/porsche-taycan-gts-sport-turismo-occasie-4G5ZPZ |
| 51 | `V97W6K` | Turbo CT | Gersthofen (DE) | Bom 76 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-cross-turismo-gebraucht-V97W6K |
| 52 | `ON3PM9` | 4S ST | Essen (DE) | Bom 75 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-ON3PM9 |
| 53 | `0DQ4LD` | 4 | Recklinghausen (DE) | Bom 74 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-gebraucht-0DQ4LD |
| 54 | `K7Q3WM` | 4S CT | Sinzheim (DE) | Bom 74 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-K7Q3WM |
| 55 | `L6L9QX` | Taycan ST | Köln (DE) | Bom 74 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-L6L9QX |
| 56 | `L85WP9` | Taycan | Bremen (DE) | Bom 74 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gebraucht-L85WP9 |
| 57 | `WKEEVM` | 4S | Holzwickede (DE) | Bom 74 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-WKEEVM |
| 58 | `ZE9KKV` | 4S CT | Ettlingen (DE) | Bom 74 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-ZE9KKV |
| 59 | `8GV2MM` | GTS ST | Mannheim (DE) | Bom 73 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-8GV2MM |
| 60 | `NQV3RV` | 4 | Hannover (DE) | Bom 73 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-gebraucht-NQV3RV |
| 61 | `CWA60M` | Turbo ST | Helsingborg (SE) | Bom 73 | **desaparecido** | outro | https://www.bytbil.com/skane-lan/personbil-taycan-turbo-sport-turismo-9214-19435636 |
| 62 | `NKP7ZL` | 4S CT | Milano (IT) | Bom 72 | **vendido** | Finder | https://finder.porsche.com/it/it-IT/details/porsche-taycan-4s-cross-turismo-usata-NKP7ZL |
| 63 | `G7PR3N` | 4S CT | Leusden (NL) | Bom 72 | **ativo** | Finder | https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-4s-cross-turismo-occasion-G7PR3N |
| 64 | `L6LK9X` | 4 CT | Ljubljana (SI) | Bom 72 | **ativo** | Finder | https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4-cross-turismo-rabljeno-vozilo-L6LK9X |
| 65 | `M27W88` | 4 CT | München (DE) | Bom 72 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-M27W88 |
| 66 | `WZVRQM` | 4 | Leipzig (DE) | Bom 72 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-WZVRQM |
| 67 | `ZO5ORE` | GTS ST | Münster (DE) | Bom 72 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-ZO5ORE |
| 68 | `24D5M5` | 4 CT | Bergamo (IT) | Bom 72 | **ativo** | Finder | https://finder.porsche.com/it/it-IT/details/porsche-taycan-4-cross-turismo-usata-24D5M5 |
| 69 | `QOZG8Z` | 4S CT | Oisterwijk (NL) | Bom 71 | **ativo** | Finder | https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-4s-cross-turismo-occasion-QOZG8Z |
| 70 | `9ZPDNO` | 4 CT | Innsbruck (AT) | Bom 71 | **ativo** | Finder | https://finder.porsche.com/at/de-AT/details/porsche-taycan-4-cross-turismo-gebraucht-9ZPDNO |
| 71 | `4G4RMZ` | Taycan | Winhöring (DE) | Bom 71 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gebraucht-4G4RMZ |
| 72 | `4W3QKZ` | 4S ST | Willich (DE) | Bom 71 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-4W3QKZ |
| 73 | `56837M` | 4 | Leipzig (DE) | Bom 71 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-56837M |
| 74 | `9NR67P` | 4 CT | Gilching-Argelsried (DE) | Bom 71 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-9NR67P |
| 75 | `440L9Q` | Taycan ST | Szczecin (PL) | Bom 70 | **vendido** | Finder | https://finder.porsche.com/pl/pl-PL/details/porsche-taycan-sport-turismo-uzywany-440L9Q |
| 76 | `7K4Q76` | 4S ST | Raubling (DE) | Bom 70 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-black-edition-gebraucht-7K4Q76 |
| 77 | `V49VX9` | Taycan | Siegen (DE) | Bom 70 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gebraucht-V49VX9 |
| 78 | `4W8ZV9` | 4 CT | Offenburg (DE) | Bom 69 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-4W8ZV9 |
| 79 | `64K0VD` | 4 | Leipzig (DE) | Bom 69 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-64K0VD |
| 80 | `NK2E7V` | GTS ST | Leipzig (DE) | Bom 69 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-NK2E7V |
| 81 | `9N3DOW` | 4S ST | Roost (LU) | Bom 68 | **ativo** | Finder | https://finder.porsche.com/lu/fr-LU/details/porsche-taycan-4s-sport-turismo-doccasion-9N3DOW |
| 82 | `89NVDM` | 4 CT | Ljubljana (SI) | Bom 68 | **ativo** | Finder | https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4-cross-turismo-rabljeno-vozilo-89NVDM |
| 83 | `08R6GN` | 4 CT | Leipzig (DE) | Bom 68 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-08R6GN |
| 84 | `4WZ5L5` | 4 CT | Frankfurt/Main (DE) | Bom 68 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-4WZ5L5 |
| 85 | `7K8X47` | Taycan | Leipzig (DE) | Bom 68 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-black-edition-gebraucht-7K8X47 |
| 86 | `L8M4WN` | Taycan ST | Trier (DE) | Bom 68 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-black-edition-gebraucht-L8M4WN |
| 87 | `WZ7NZ4` | Taycan ST | Graz-Liebenau (AT) | Bom 67 | **ativo** | Finder | https://finder.porsche.com/at/de-AT/details/porsche-taycan-sport-turismo-gebraucht-WZ7NZ4 |
| 88 | `ENLX0K` | Taycan | Kleinmachnow (DE) | Bom 67 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-black-edition-gebraucht-ENLX0K |
| 89 | `L9KVZZ` | 4 CT | Frankfurt am Main (DE) | Bom 67 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-L9KVZZ |
| 90 | `G076Q0` | Turbo CT | Riga (LV) | Bom 66 | **ativo** | Finder | https://finder.porsche.com/lv/lv-LV/details/porsche-taycan-turbo-cross-turismo-lietota-G076Q0 |
| 91 | `V3MP6K` | Taycan | Amsterdam (NL) | Bom 66 | **ativo** | Finder | https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-occasion-V3MP6K |
| 92 | `0DK364` | GTS ST | Papendorf (DE) | Bom 66 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-0DK364 |
| 93 | `36P53Z` | 4S | Stuttgart (DE) | Bom 65 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-36P53Z |
| 94 | `3K8R6M` | Taycan ST | Bonn (DE) | Bom 65 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-3K8R6M |
| 95 | `PV25WO` | Taycan ST | Holzwickede (DE) | Bom 65 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-PV25WO |
| 96 | `XL768G` | Taycan ST | Hannover (DE) | Bom 65 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-XL768G |
| 97 | `WX3RL4` | Taycan ST | Linz-Leonding (AT) | Bom 64 | **ativo** | Finder | https://finder.porsche.com/at/de-AT/details/porsche-taycan-sport-turismo-gebraucht-WX3RL4 |
| 98 | `36MEXV` | 4 CT | Hamburg (DE) | Bom 64 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-36MEXV |
| 99 | `64P8WP` | 4 CT | Soest (DE) | Bom 64 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-64P8WP |
| 100 | `7WOZLW` | 4 CT | Ljubljana (SI) | Bom 63 | **ativo** | Finder | https://finder.porsche.com/si/sl-SI/details/porsche-taycan-4-cross-turismo-rabljeno-vozilo-7WOZLW |
| 101 | `XG828E` | Taycan ST | Estenfeld (DE) | Bom 63 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-XG828E |
| 102 | `67PV56` | 4 CT | Hannover (DE) | Bom 62 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-67PV56 |
| 103 | `XZ699X` | Turbo S | Leipzig (DE) | Justo 97 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-s-gebraucht-XZ699X |
| 104 | `DRG84P` | 4S ST | Leipzig (DE) | Justo 92 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-DRG84P |
| 105 | `9N9WN7` | 4S CT | Düsseldorf (DE) | Justo 88 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-9N9WN7 |
| 106 | `G05454` | Turbo S CT | Stuttgart (DE) | Justo 79 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-s-cross-turismo-gebraucht-G05454 |
| 107 | `L66WZQ` | Turbo ST | Leipzig (DE) | Justo 78 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-sport-turismo-gebraucht-L66WZQ |
| 108 | `G0ED4W` | Turbo ST | Friedrichshafen (DE) | Justo 77 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-sport-turismo-gebraucht-G0ED4W |
| 109 | `M44G7E` | GTS ST | Berlin (DE) | Justo 77 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-M44G7E |
| 110 | `OP4MG9` | GTS | Aschaffenburg (DE) | Justo 77 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-OP4MG9 |
| 111 | `e9dc1a45` | Turbo | Stuhr-Seckenhausen (DE) | Justo 76 | **ativo** | AutoScout24 | https://www.autoscout24.com/offers/porsche-taycan-turbo-panorama-headup-innodrive-21-electric-black-cat_ma57mo75273-e9dc1a45-1f90-4157-8798-effc68d37e36 |
| 112 | `f7cafc67` | 4 | Kaarst (bei Düsseldorf) (DE) | Justo 74 | **ativo** | AutoScout24 | https://www.autoscout24.com/offers/porsche-taycan-4-black-edition-pano-hud-hal-softclose-18w-electric-black-cat_ma57mo75273-f7cafc67-4bba-4004-bc95-60d24aea793b |
| 113 | `3K2MXZ` | GTS | Regensburg (DE) | Justo 74 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-3K2MXZ |
| 114 | `70KPG4` | Turbo | Bielefeld (DE) | Justo 74 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-gebraucht-70KPG4 |
| 115 | `M4EGLE` | 4S | Wettenberg (DE) | Justo 74 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-black-edition-gebraucht-M4EGLE |
| 116 | `V4N4RR` | 4 CT | Holzwickede (DE) | Justo 74 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-V4N4RR |
| 117 | `Z5PZ9E` | 4 CT | Hamburg (DE) | Justo 74 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-Z5PZ9E |
| 118 | `D4RW2P` | Turbo S ST | Prague (CZ) | Justo 73 | **ativo** | Finder | https://finder.porsche.com/cz/cs-CZ/details/porsche-taycan-turbo-s-sport-turismo-ojete-D4RW2P |
| 119 | `3K4ZEM` | Turbo ST | Leipzig (DE) | Justo 73 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-sport-turismo-gebraucht-3K4ZEM |
| 120 | `DR8KME` | GTS ST | Leipzig (DE) | Justo 73 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-DR8KME |
| 121 | `OGPER7` | 4S ST | Bielefeld (DE) | Justo 73 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-OGPER7 |
| 122 | `20P2V5` | 4 | Bonn (DE) | Justo 72 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-20P2V5 |
| 123 | `4G5VXE` | Turbo CT | Bielefeld (DE) | Justo 72 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-cross-turismo-gebraucht-4G5VXE |
| 124 | `L8O4VZ` | 4S ST | Leipzig (DE) | Justo 72 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-L8O4VZ |
| 125 | `45ZNP9` | 4 | Estenfeld (DE) | Justo 71 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-45ZNP9 |
| 126 | `7N04NW` | GTS | Bonn (DE) | Justo 71 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-7N04NW |
| 127 | `VZMMM2` | 4S CT | Milano (IT) | Justo 70 | **ativo** | Finder | https://finder.porsche.com/it/it-IT/details/porsche-taycan-4s-cross-turismo-usata-VZMMM2 |
| 128 | `5Z0QGW` | Taycan | Villingen-Schwenningen (DE) | Justo 70 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gebraucht-5Z0QGW |
| 129 | `6OOG45` | 4S ST | Frankfurt/Main (DE) | Justo 70 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-6OOG45 |
| 130 | `70P85W` | 4S ST | Bergisch Gladbach (DE) | Justo 70 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-black-edition-gebraucht-70P85W |
| 131 | `4W34XE` | 4S | Tallinn (EE) | Justo 69 | **ativo** | Finder | https://finder.porsche.com/ee/et-EE/details/porsche-taycan-4s-kasutatud-4W34XE |
| 132 | `EXDW85` | 4S | Bergisch Gladbach (DE) | Justo 69 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-black-edition-gebraucht-EXDW85 |
| 133 | `XGWRQN` | Taycan ST | Hamburg (DE) | Justo 69 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-XGWRQN |
| 134 | `W36ODZ` | 4S CT | Milano (IT) | Justo 68 | **ativo** | Finder | https://finder.porsche.com/it/it-IT/details/porsche-taycan-4s-cross-turismo-usata-W36ODZ |
| 135 | `DO6NMK` | GTS | Bergisch Gladbach (DE) | Justo 68 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-DO6NMK |
| 136 | `K78DMM` | GTS ST | Chemnitz (DE) | Justo 68 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-K78DMM |
| 137 | `QOWVKW` | 4S ST | Frankfurt/Main (DE) | Justo 68 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-black-edition-gebraucht-QOWVKW |
| 138 | `V4X3Z9` | 4 | Landau i.d. Pfalz (DE) | Justo 68 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-gebraucht-V4X3Z9 |
| 139 | `XPVRZX` | 4S ST | Kiel (DE) | Justo 68 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-XPVRZX |
| 140 | `Z5RD72` | 4S ST | Gersthofen (DE) | Justo 68 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-Z5RD72 |
| 141 | `6476R5` | Taycan | Hannover (DE) | Justo 67 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-black-edition-gebraucht-6476R5 |
| 142 | `EKE6D5` | 4 CT | Koblenz (DE) | Justo 67 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-EKE6D5 |
| 143 | `OGGQZ3` | Taycan | Zagreb (HR) | Justo 67 | **ativo** | Finder | https://finder.porsche.com/hr/hr-HR/details/porsche-taycan-OGGQZ3 |
| 144 | `25Q26K` | 4S ST | Willich (DE) | Justo 66 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-25Q26K |
| 145 | `EPR2E5` | 4S CT | Lübeck (DE) | Justo 66 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-EPR2E5 |
| 146 | `XWZ4LG` | Taycan | Lüneburg (DE) | Justo 66 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-black-edition-gebraucht-XWZ4LG |
| 147 | `Z5PQM2` | GTS ST | Aschaffenburg (DE) | Justo 66 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-Z5PQM2 |
| 148 | `WKK75L` | 4 CT | Livorno (IT) | Justo 65 | **ativo** | Finder | https://finder.porsche.com/it/it-IT/details/porsche-taycan-4-cross-turismo-usata-WKK75L |
| 149 | `45NQWQ` | 4S CT | Wien (AT) | Justo 64 | **ativo** | Finder | https://finder.porsche.com/at/de-AT/details/porsche-taycan-4s-cross-turismo-gebraucht-45NQWQ |
| 150 | `084EG4` | GTS ST | Düsseldorf (DE) | Justo 64 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-084EG4 |
| 151 | `2OQX42` | 4S ST | Dresden (DE) | Justo 64 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-2OQX42 |
| 152 | `DNDEZE` | 4 CT | Reutlingen (DE) | Justo 64 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-DNDEZE |
| 153 | `KP9RZD` | Turbo | Leipzig (DE) | Justo 63 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-gebraucht-KP9RZD |
| 154 | `6WG8QD` | 4S CT | Wien (AT) | Justo 63 | **ativo** | Finder | https://finder.porsche.com/at/de-AT/details/porsche-taycan-4s-cross-turismo-gebraucht-6WG8QD |
| 155 | `EKXDNK` | 4S CT | Knokke-Heist (BE) | Justo 63 | **ativo** | Finder | https://finder.porsche.com/be/nl-BE/details/porsche-taycan-4s-cross-turismo-occasie-EKXDNK |
| 156 | `458453` | Taycan | Zagreb (HR) | Justo 63 | **ativo** | Finder | https://finder.porsche.com/hr/hr-HR/details/porsche-taycan-black-edition-rabljeno-458453 |
| 157 | `M73KGO` | 4S | Howald (LU) | Justo 63 | **ativo** | Finder | https://finder.porsche.com/lu/fr-LU/details/porsche-taycan-4s-black-edition-doccasion-M73KGO |
| 158 | `2OLGD9` | 4S ST | Schwäbisch Gmünd (DE) | Justo 63 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-2OLGD9 |
| 159 | `7K949L` | Taycan | Kleinmachnow (DE) | Justo 63 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-black-edition-gebraucht-7K949L |
| 160 | `LV08VN` | GTS ST | Offenburg (DE) | Justo 62 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-LV08VN |
| 161 | `LV9R6Q` | 4 CT | Saarbrücken (DE) | Justo 62 | **vendido** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-LV9R6Q |
| 162 | `PVQXRO` | 4S ST | Bielefeld (DE) | Justo 62 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-sport-turismo-gebraucht-PVQXRO |
| 163 | `QKZKX6` | Taycan ST | Lüneburg (DE) | Justo 62 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-QKZKX6 |
| 164 | `4556XQ` | Taycan | Soest (DE) | Justo 61 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-black-edition-gebraucht-4556XQ |
| 165 | `Z849WD` | 4 CT | Nürnberg (DE) | Justo 61 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-Z849WD |
| 166 | `DNNRGL` | 4 | Leipzig (DE) | Justo 61 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-DNNRGL |
| 167 | `QVPW4Z` | 4S | Alicante (ES) | Justo 60 | **ativo** | Finder | https://finder.porsche.com/es/es-ES/details/porsche-taycan-4s-usado-QVPW4Z |
| 168 | `QL47PW` | 4 | Innsbruck (AT) | Justo 60 | **ativo** | Finder | https://finder.porsche.com/at/de-AT/details/porsche-taycan-4-gebraucht-QL47PW |
| 169 | `7KO487` | 4S CT | Klaipedos raj. (LT) | Justo 60 | **ativo** | Finder | https://finder.porsche.com/lt/lt-LT/details/porsche-taycan-4s-cross-turismo-naudoti-7KO487 |
| 170 | `6428RP` | 4 CT | Saarbrücken (DE) | Justo 60 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-6428RP |
| 171 | `EN8REE` | 4 CT | Darmstadt (DE) | Justo 60 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-EN8REE |
| 172 | `LV88VZ` | Taycan | Paderborn (DE) | Justo 60 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-black-edition-gebraucht-LV88VZ |
| 173 | `2XWKW9` | 4 | Milano (IT) | Justo 60 | **ativo** | Finder | https://finder.porsche.com/it/it-IT/details/porsche-taycan-4-usata-2XWKW9 |
| 174 | `36VE6V` | Taycan | Roost (LU) | Justo 59 | **ativo** | Finder | https://finder.porsche.com/lu/fr-LU/details/porsche-taycan-black-edition-doccasion-36VE6V |
| 175 | `4578L3` | Taycan ST | Soest (DE) | Justo 59 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-black-edition-gebraucht-4578L3 |
| 176 | `M0W42O` | Taycan ST | Offenburg (DE) | Justo 59 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-M0W42O |
| 177 | `OLQVQM` | Taycan ST | Estenfeld (DE) | Justo 59 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-black-edition-gebraucht-OLQVQM |
| 178 | `M2K6R8` | Taycan | Praha Prosek (CZ) | Justo 58 | **ativo** | Finder | https://finder.porsche.com/cz/cs-CZ/details/porsche-taycan-ojete-M2K6R8 |
| 179 | `2492M2` | 4 CT | Stuttgart (DE) | Justo 58 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-2492M2 |
| 180 | `32OD78` | Taycan ST | Ulm (DE) | Justo 58 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-32OD78 |
| 181 | `9N4Z5D` | Taycan ST | Wuppertal (DE) | Justo 58 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-9N4Z5D |
| 182 | `G08XN8` | Taycan ST | Hamburg (DE) | Justo 58 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-gebraucht-G08XN8 |
| 183 | `05ODZE` | Taycan | Aubière (FR) | Justo 57 | **ativo** | Finder | https://finder.porsche.com/fr/fr-FR/details/porsche-taycan-doccasion-05ODZE |
| 184 | `45OO4E` | 4S CT | Köln (DE) | Justo 57 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-cross-turismo-gebraucht-45OO4E |
| 185 | `7K4DL6` | Taycan ST | Landau i.d. Pfalz (DE) | Justo 57 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-black-edition-gebraucht-7K4DL6 |
| 186 | `M2VLV8` | 4 CT | Bergisch Gladbach (DE) | Justo 57 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-M2VLV8 |
| 187 | `PLWGOO` | GTS ST | Kleinmachnow (DE) | Justo 57 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-sport-turismo-gebraucht-PLWGOO |
| 188 | `56D8N9` | 4 | Rotterdam (NL) | Justo 56 | **ativo** | Finder | https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-4-occasion-56D8N9 |
| 189 | `PVZ2WE` | Taycan ST | Münster (DE) | Justo 56 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-black-edition-gebraucht-PVZ2WE |
| 190 | `EX63O6` | Taycan ST | Leusden (NL) | Justo 54 | **ativo** | Finder | https://finder.porsche.com/nl/nl-NL/details/porsche-taycan-sport-turismo-black-edition-occasion-EX63O6 |
| 191 | `aa54abcf` | 4 ST | Leipzig (DE) | Justo 54 | **ativo** | AutoScout24 | https://www.autoscout24.com/offers/porsche-taycan-4-black-edition-sportchrono-innodrive-sport-electric-silver-cat_ma57mo75273-aa54abcf-a2e0-4827-b40f-32ef183484c8 |
| 192 | `f2d6783f` | 4S CT | Maldegem (BE) | Justo 52 | **ativo** | AutoScout24 | https://www.autoscout24.com/offers/porsche-taycan-4s-cross-turismo-105-kwh-perf-batt+-chrono-air-susp-hd-matrix-bose-18-way-inno-zetel-verw-ventil-pano-electric-grey-cat_ma57mo75273-f2d6783f-d1d6-412d-8fa7-32a56f7d0857 |
| 193 | `624826bd` | 4 CT | Belgique (FR) | Justo 51 | **ativo** | AutoScout24 | https://www.autoscout24.fr/offres/porsche-taycan-crossturismo-4-pano-inno-21-bose-14-wayseats-electrique-gris-cat_ma57mo75273-624826bd-2146-45bb-8d65-2346cc8769cc |
| 194 | `5Z6PP9` | Taycan ST | Graz-Liebenau (AT) | Justo 51 | **ativo** | Finder | https://finder.porsche.com/at/de-AT/details/porsche-taycan-sport-turismo-gebraucht-5Z6PP9 |
| 195 | `PLO384` | Taycan ST | Braunschweig (DE) | Justo 51 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-sport-turismo-black-edition-gebraucht-PLO384 |
| 196 | `RRO02L` | 4 CT | München (DE) | Justo 50 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-cross-turismo-gebraucht-RRO02L |
| 197 | `XPMZON` | Turbo S | Aschaffenburg (DE) | Caro 75 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-s-gebraucht-XPMZON |
| 198 | `WKLLEL` | GTS | Landau (DE) | Caro 73 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-WKLLEL |
| 199 | `56750V` | 4S | Braunschweig (DE) | Caro 68 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-56750V |
| 200 | `2XR58K` | Turbo S | Wroclaw (PL) | Caro 67 | **ativo** | Finder | https://finder.porsche.com/pl/pl-PL/details/porsche-taycan-turbo-s-uzywany-2XR58K |
| 201 | `4GWMN5` | 4S | Poznan (PL) | Caro 67 | **ativo** | Finder | https://finder.porsche.com/pl/pl-PL/details/porsche-taycan-4s-uzywany-4GWMN5 |
| 202 | `PV0N2R` | 4S | Magdeburg (DE) | Caro 66 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-black-edition-gebraucht-PV0N2R |
| 203 | `ENGK2K` | GTS | Filderstadt-Bernhausen (DE) | Caro 64 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-ENGK2K |
| 204 | `9PXKXP` | 4S | Desenzano (BS) (IT) | Caro 62 | **ativo** | Finder | https://finder.porsche.com/it/it-IT/details/porsche-taycan-4s-black-edition-usata-9PXKXP |
| 205 | `PLGE5G` | 4S | Reutlingen (DE) | Caro 62 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-black-edition-gebraucht-PLGE5G |
| 206 | `08W58N` | 4S | Sopot (PL) | Caro 61 | **ativo** | Finder | https://finder.porsche.com/pl/pl-PL/details/porsche-taycan-4s-black-edition-uzywany-08W58N |
| 207 | `5675EW` | 4 | Hamburg (DE) | Caro 61 | **reservado** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-5675EW |
| 208 | `90WEVP` | 4S | Hannover (DE) | Caro 60 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-black-edition-gebraucht-90WEVP |
| 209 | `XWPOMP` | GTS | Hilzingen (DE) | Caro 60 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-XWPOMP |
| 210 | `PLEVV4` | 4 | 821 04 Bratislava (SK) | Caro 59 | **ativo** | Finder | https://finder.porsche.com/sk/sk-SK/details/porsche-taycan-4-black-edition-jazdene-PLEVV4 |
| 211 | `DN8V2K` | GTS | München (DE) | Caro 59 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-DN8V2K |
| 212 | `NKQ4LV` | GTS | Recklinghausen (DE) | Caro 58 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-NKQ4LV |
| 213 | `32767V` | 4 | Ettlingen (DE) | Caro 57 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-32767V |
| 214 | `4560KQ` | 4 | Siegen (DE) | Caro 57 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-4560KQ |
| 215 | `45MK2Z` | 4S | Köln (DE) | Caro 57 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-black-edition-gebraucht-45MK2Z |
| 216 | `OPD8WL` | 4 | Siegen (DE) | Caro 57 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-OPD8WL |
| 217 | `QL9LR6` | 4 | München (DE) | Caro 57 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-QL9LR6 |
| 218 | `V3O495` | 4S | Wroclaw (PL) | Caro 56 | **ativo** | Finder | https://finder.porsche.com/pl/pl-PL/details/porsche-taycan-4s-black-edition-uzywany-V3O495 |
| 219 | `454OWZ` | 4 | Hannover (DE) | Caro 56 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-454OWZ |
| 220 | `W3EK6Q` | 4 | Darmstadt (DE) | Caro 56 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-W3EK6Q |
| 221 | `20OE7P` | 4 | Bologna (IT) | Caro 55 | **ativo** | Finder | https://finder.porsche.com/it/it-IT/details/porsche-taycan-4-black-edition-usata-20OE7P |
| 222 | `G2XEGQ` | 4 | Marseille (FR) | Caro 54 | **ativo** | Finder | https://finder.porsche.com/fr/fr-FR/details/porsche-taycan-4-doccasion-G2XEGQ |
| 223 | `QV40ZO` | GTS | Kempten (DE) | Caro 51 | **ativo** | Finder | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-QV40ZO |
| 224 | `7NQKO6` | 4S | L'Hospitalet del Llobregat - Barcelona (ES) | Caro 48 | **ativo** | Finder | https://finder.porsche.com/es/es-ES/details/porsche-taycan-4s-usado-7NQKO6 |
| 225 | `7090WL` | 4 | Mechelen (BE) | Caro 44 | **reservado** | Finder | https://finder.porsche.com/be/nl-BE/details/porsche-taycan-4-occasie-7090WL |
| 226 | `6G45KP` | Taycan | S. Paio D’Arcos - Braga (PT) | Caro 35 | **reservado** | Finder | https://finder.porsche.com/pt/pt-PT/details/porsche-taycan-usado-6G45KP |

## Entrega
- `finder_estado_2026-11-04_revisao.json`, no formato 3.3, com um registo por carro:
  - `codigo`, `url`, `verificado_em`, `estado` (ativo, reservado, vendido, desaparecido ou sem_leitura) e `texto_estado` (a frase exata);
  - `preco`, `moeda` e `km`;
  - `estado_site` (copiado da tabela) e `mudou` (true ou false);
  - `nota`.
- `revisao_resumo.md`, só com as **mudanças** face à tabela: vendidos novos, reservas novas, reservas que caíram, desaparecidos, preços alterados e possíveis reaparecidos.
- Um zip, sem páginas em bruto, emails nem telefones.
