# Pedido ao Grok / Apify — fichas completas (26/11/2026)

Objetivo: ler a **ficha completa** de cada anúncio abaixo e devolver a lista de equipamento, idealmente com os **códigos de opção Porsche** (P4S, P5T, P67, 1P8, 0N5, FT3, FT1, KA6, 7Y8, 5KA, KS1, 8IU/8JU, 3FG, VW1/VW6, Q1J/Q2J, 4D3, 4A4, KH5, J9Q, 9VL/9VJ, 4X4, GH3…).
Se a ficha tiver ligação ao configurador («Konfiguration ansehen» / PDF), devolver também esse link completo (com `options=`) e o preço em novo indicado.

Para cada carro: código, estado (ativo / reservado / vendido / desaparecido, com o texto da ficha), preço, km, 1.ª matrícula exata, uso anterior (Vorführwagen, Dienstwagen…), garantia (Approved / fábrica até…), SoH se indicado, disponibilidade («verfügbar ab»), cor exterior.

Formato de saída: JSON no formato de `finder_estado_*.json` (campos `codigo`, `url`, `verificado_em`, `estado`, `texto_estado`, `preco`, `km`, `primeira_matricula_exata`, `uso`, `garantia`, `soh_bateria_pct`, `disponivel_a_partir_de`, `cor`) mais `opcoes_codigos` (lista) e `link_configurador`.

Regras: sem proxies, sem login, sem contornar bloqueios (parar no 429/403 e indicar quais ficaram por ler); 20–30 s entre pedidos ao mesmo sítio; sem dados pessoais de vendedores ou consultores.

## Porsche Finder (21 fichas, por ordem de preço posto em PT)

- **NKEKQP** · 4 · FrankfurtamMai · 10/2025 · 21650 km · 79.960 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-gebraucht-NKEKQP
- **44WKP5** · 4 · Regensburg · 06/2025 · 15500 km · 89.900 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-gebraucht-44WKP5
- **6OZRXW** · 4 · Wommelgem · 02/2025 · 18791 km · 92.999 € · https://finder.porsche.com/be/nl-BE/details/porsche-taycan-4-occasie-6OZRXW
- **M44EK8** · 4S · Berlin · 07/2024 · 39744 km · 98.930 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-M44EK8
- **D42E0L** · 4 · Bonn · 07/2026 · 8000 km · 99.950 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-D42E0L
- **QORRN8** · 4 · MontSaintGuibe · 03/2026 · 10659 km · 104.999 € · https://finder.porsche.com/be/nl-BE/details/porsche-taycan-4-occasie-QORRN8
- **K7L62X** · 4 · HegauBodensee · 11/2026 · 9900 km · 121.890 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-K7L62X
- **6OR74W** · GTS · Bielefeld · 02/2025 · 3710 km · 127.800 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-6OR74W
- **7039LD** · 4 · München · 11/2026 · 6000 km · 128.309 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-7039LD
- **058Q2N** · Turbo · Stuttgart · 10/2024 · 20400 km · 128.900 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-gebraucht-058Q2N
- **EN807W** · 4S · BerlinAdlershof · 11/2026 · 3900 km · 130.900 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-black-edition-gebraucht-EN807W
- **258NO5** · Turbo · Leipzig · 11/2024 · 17139 km · 132.800 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-gebraucht-258NO5
- **45O2XE** · GTS · Hamburg · 11/2026 · 3100 km · 134.900 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-45O2XE
- **56QL6W** · GTS · Moers · 10/2026 · 9000 km · 139.890 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-56QL6W
- **W3EPQQ** · 4S · SchwarzwaldBaar · 11/2026 · 9900 km · 140.840 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-black-edition-gebraucht-W3EPQQ
- **82KWP3** · Turbo S · Freiburg · 05/2024 · 4900 km · 142.890 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-s-gebraucht-82KWP3
- **2598G2** · GTS · Kassel · 11/2026 · 4400 km · 151.176 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-2598G2
- **RN38RZ** · GTS · Wiesbaden · 06/2026 · 1400 km · 154.400 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-RN38RZ
- **3257QW** · GTS · Rosenheim · 09/2026 · 9900 km · 153.690 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-3257QW
- **56N579** · GTS · Willich · 08/2026 · 9900 km · 152.500 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-56N579
- **WZ8XRZ** · GTS · Willich · 10/2026 · 9900 km · 158.900 € · https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-WZ8XRZ

## Outros portais (19 anúncios: ler a página do anúncio; procurar se o mesmo carro está no Finder e, se estiver, ler a ficha do Finder)

- **a45a2472** · 4 · Lyra · 10/2025 · 20134 km · 79.880 € · https://www.autoscout24.com/offers/porsche-taycan-4-led-pano-bose-kamera-waermepumpe-dab-electric-black-cat_ma57mo75273-a45a2472-2a5b-4882-a2ff-c2facfb67e57
- **f7cafc67** · 4 · Astoria · 05/2026 · 23123 km · 98.990 € · https://www.autoscout24.com/offers/porsche-taycan-4-black-edition-pano-hud-hal-softclose-18w-electric-black-cat_ma57mo75273-f7cafc67-4bba-4004-bc95-60d24aea793b
- **28e7b942** · 4S · BielefeldGlini · 12/2024 · 23790 km · 99.800 € · https://www.carzilla.de/Porsche-Zentrum-Bielefeld-Glinicke-Sportwagen-GmbH/Porsche/Taycan/Gebrauchtfahrzeug/Elektro/Automatik/28e7b942054943b696739dedf8391861/20753
- **a00525fe** · 4S · GaiaAutoItalia · 08/2024 · 22000 km · 99.950 € · https://www.autoscout24.com/offers/porsche-taycan-4s-598cv-restyling-electric-black-cat_ma57mo75273-a00525fe-9e3c-482a-81ea-e1690af16e3b
- **f11483cb** · 4S · Project911sasd · 09/2024 · 13500 km · 100.000 € · https://www.autoscout24.com/offers/porsche-taycan-taycan-2024-4s-performance-battery-plus-5p-ti-electric-silver-cat_ma57mo75273-f11483cb-2c30-4757-aa7b-afd1d34b59e9
- **564cf511** · 4S · Sfrmotors · 04/2024 · 20500 km · 100.990 € · https://www.autoscout24.com/offers/porsche-taycan-4s-598cv-promo-iva-esp-electric-cat_ma57mo75273-564cf511-7964-4f74-8cb2-031513170082
- **8e168fac** · 4S · AutocentriGius · 07/2024 · 29590 km · 103.900 € · https://www.autoscout24.com/offers/porsche-taycan-4s-5p-ti-electric-green-cat_ma57mo75273-8e168fac-a9fa-4daf-a1ea-6f994284d0e5
- **23265289** · 4S · TR · 09/2025 · 6478 km · 109.850 € · https://www.autoscout24.com/offers/porsche-taycan-4s-perfomance-sportdesign-headup-21-electric-green-cat_ma57mo75273-23265289-2d5c-438b-8ea0-ac6fb151e26e
- **e9dc1a45** · Turbo · TR · 09/2024 · 29501 km · 117.850 € · https://www.autoscout24.com/offers/porsche-taycan-turbo-panorama-headup-innodrive-21-electric-black-cat_ma57mo75273-e9dc1a45-1f90-4157-8798-effc68d37e36
- **2df23716** · 4 · PorscheGrazLie · 06/2026 · 7772 km · 118.950 € · https://www.autoscout24.com/offers/porsche-taycan-4-black-edition-electric-grey-cat_ma57mo75273-2df23716-7373-437f-80cf-4d0fc86b1fe8
- **30105296** · 4 · DWALinzLeondi · 08/2026 · 4248 km · 124.900 € · https://www.dasweltauto.at/vehicle/30105296
- **4c7b6dcd** · 4 · PorscheLinzLeo · 08/2026 · 3938 km · 124.900 € · https://www.autoscout24.com/offers/porsche-taycan-4-black-edition-electric-black-cat_ma57mo75273-4c7b6dcd-c8d0-428f-852b-eaab8ca51ae4
- **adb03f1a** · 4S · AutocentriGius · 12/2025 · 8300 km · 129.900 € · https://www.autoscout24.com/offers/porsche-taycan-4s-5p-ti-electric-black-cat_ma57mo75273-adb03f1a-1163-4dc0-a9cd-d3794ddc4340
- **50aad5f0** · 4 · Gesicar · 08/2026 · 190 km · 130.026 € · https://www.autoscout24.com/offers/porsche-taycan-4-black-edition-iva-esposta-electric-black-cat_ma57mo75273-50aad5f0-af0c-4549-8b9e-077b741af44d
- **534366d7** · 4S · BergischGladba · 08/2026 · 5900 km · 126.900 € · https://www.autoscout24.com/offers/porsche-taycan-4s-black-edition-electric-grey-cat_ma57mo75273-534366d7-0a16-416c-a145-a94a5f671a0c
- **f5c9c630** · GTS · Amsterdam · 12/2025 · 12666 km · 136.950 € · https://www.autoscout24.com/offers/porsche-taycan-gts-electric-grey-cat_ma57mo75273-f5c9c630-4b6d-435b-ac3f-87eb18c8bf2e
- **4317baae** · Turbo S · AutozentrumNie · 09/2024 · 9054 km · 144.444 € · https://www.autoscout24.com/offers/porsche-taycan-turbo-s-951-ps-approved-np-240k-abs-vollaus-electric-silver-cat_ma57mo75273-4317baae-2008-45a5-8d95-9d0f589ebe9f
- **aa8e08f4** · 4 · LEUSDEN · 11/2026 · 5000 km · 143.400 € · https://www.autoscout24.com/offers/porsche-taycan-4-black-edition-105-kwh-electric-green-cat_ma57mo75273-aa8e08f4-0d65-4c34-b89d-45d111ecb1e4
- **59629278** · 4S · Amsterdam · 06/2026 · 15 km · 158.320 € · https://www.autotrack.nl/a/porsche-taycan-elektriciteit-2026-59629278

Nota: o Astoria (f7cafc67, stand independente) não está no Finder; o Pedro pede o PDF/VIN diretamente ao stand.
