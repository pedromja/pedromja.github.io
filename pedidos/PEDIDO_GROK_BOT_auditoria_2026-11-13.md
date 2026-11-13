# Pedido ao Grok Bot: correções da auditoria à recolha (13/11/2026)

O Claude Code auditou o site e os ficheiros de 11 e 12/11 (`finder_estado`, `anuncios`). A recolha está estável e as "reservas caídas" repetidas baixaram de 5 para 1 por dia. Faltam estas correções, por ordem de prioridade. Regras de sempre: só leitura pública, sem login, sem contornar anti-bot, sem contactar vendedores, sem dados pessoais, sem veredictos.

## 1. Abrir a ficha dos carros em alerta (não só a lista)
Em 12/11, metade das linhas do `finder_estado` (40 de 78) eram `na_lista`: a ficha não foi aberta. Entre elas estavam 5 dos carros em alerta: `EXR720`, `9PERGW`, `L6683Z`, `4XK4Z5`, `3K674M`. O Zagreb `Z52DNE` não apareceu.
- Para os carros do alerta, `na_lista` não chega: abrir sempre a ficha.
- Preencher, quando a ficha mostrar: `primeira_matricula_exata`, `innodrive_P4S`, `lugares_5KA`, `acidente`, `disponivel_a_partir_de`, `soh_bateria_pct` e `garantia_texto`. Hoje faltam em 57 de 78 linhas.

## 2. Campo `uso` (demo, carro de serviço)
O pedido de 12/11 (eixo 7) ainda não chegou: `uso` vem vazio em 1.902 de 1.929 anúncios. Começar pelos carros de 2026 com menos de 8.000 km. Valores: `Vorführwagen`, `Firmenwagen`, `Dienstwagen`, `Tageszulassung`, `Mietwagen`, `Leasingrückläufer` ou `n/d`.

## 3. Anúncios repetidos
O campo `possivel_duplicado_de` vem vazio em quase todos. O site encontrou 49 pares com a mesma matrícula, versão, km (±150) e preço (±1,2 %). Agora já os conta uma vez só, mas convém confirmar.
- Para cada par, dizer se é o **mesmo carro** (mesmo VIN ou mesmas fotos) e qual é o anúncio original (o do stand).
- Os pares entre países diferentes podem ser revendedores a anunciar o carro de um stand: indicar quem é o vendedor real.

**Mesmo país (39)**

| Anúncio | Também em |
|---|---|
| NL-Leusden-6f77c232 | NL-Leusden-G7PR3N |
| AT-PorscheLeopold-a66e90d2 | AT-Wien-45NQWQ |
| AT-PorscheInterAu-138c7b95 | AT-Wien-XG228E |
| NL-Gelderland-45c248e7 | NL-Heteren-OPLQ93 |
| AT-PorscheLeopold-73bac471 | AT-Wien-32W7WV |
| AT-PorscheLeopold-73bac471 | wh:889709824 |
| NL-Brabant-60197373 | NL-Gelderland-59374237 |
| AT-Salzburg-P0070K | AT-Salzburg-af7583b1 |
| IT-Bologna-8973N6 | IT-Modena-a540a4f9 |
| NL-Deventer-70PLV4 | NL-Deventer-9P5EVW |
| DE-Pforzheim-0845MN | DE-Wuppertal-2XQELK |
| DE-Bielefeld-2436V5 | DE-Leipzig-6GP92X |
| DE-Bielefeld-56VKKW | DE-Bielefeld-OLMMMM |
| DE-Gttingen-90RD0W | DE-Leipzig-V334OE |
| DE-Hamburg-EX24P0 | DE-mobile-462326266 |
| DE-Magdeburg-K7LPMX | DE-Mnchen-W36O4L |
| DE-Bielefeld-K7QRNX | DE-Bielefeld-NQ6K4N |
| DE-Hagen-MEEW98 | DE-Pforzheim-0845MN |
| DE-Hagen-MEEW98 | DE-Wuppertal-2XQELK |
| DE-BergischGladba-NQOROV | DE-Hagen-XWO99O |
| DE-BergischGladba-NQOROV | DE-Moers-7KL9G7 |
| DE-Aschaffenburg-QKEGV6 | DE-Nrnberg-G2XGQ0 |
| DE-Hagen-XWO99O | DE-Moers-7KL9G7 |
| DE-ndOOYYOnomostr-85631517 | DE-ndOOYYOnomostr-85860429 |
| DE-Leipzig-39ab3245 | DE-Leipzig-ME4Z0W |
| FR-Poissy-O6W703 | FR-Poissy-V30PVK |
| DE-Lrrach-m21070698 | GRQ2RN |
| AT-DWASalzburg-55500397 | AT-Salzburg-af7583b1 |
| AT-DWASalzburg-55500397 | AT-Salzburg-P0070K |
| AT-DWALinzLeondi-30104884 | AT-PorscheLinzLeo-0afda4e5 |
| AT-DWAWien-11101643 | wh:970121051 |
| AT-DWAWienLiesin-15004780 | wh:903660996 |
| DE-Hamburg-XGRVVG | DE-Hamburg-XGWRQN |
| DE-Plattling-0489353d | as24:0489353d-bd52-4d3c-b68e-48c3af07d6cc |
| DE-Gersthofen-5475e30a | as24:5475e30a-1957-4294-a961-82ab333564e8 |
| DE-Osnabrck-83857c1c | as24:83857c1c-b67f-46a5-b0be-87a82715e858 |
| DE-Leipzig-883aec73 | DE-Leipzig-95V9QO |
| DE-Kempten-ad42dff7 | as24:ad42dff7-6769-4992-b68c-e02449651458 |
| DE-BergischGladba-076cabb7 | DE-BergischGladba-XGRM3G |

**Países diferentes (10)**

| Anúncio | Também em |
|---|---|
| NL-Groningen-59656349 | PL-Warszawa-GEGM6N |
| BE-DCT-24538403 | FR-DCTWielsbekeMa-624826bd |
| FR-AutoScout24Lux-7054cf20 | LU-Howald-ON53LM |
| BG-Sofia-8GWO0L | SK-Bratislava-WZ7OL4 |
| CH-Frenkendorf-WK3L8D | FR-ARIANESWISSMOT-6d6fe258 |
| DE-Wuppertal-WXR5P4 | NL-Twente-b8297d9f |
| DE-ndOOYYOnomostr-85631517 | PL-Wroclaw-V3O495 |
| DE-ndOOYYOnomostr-85860429 | PL-Wroclaw-V3O495 |
| DE-mobile-m53532863 | NL-MaastrichtAirp-ONL22L |
| DE-ndoveonomostra-5749ffcd | FR-Rouen-X8XO8N |

## 4. Quilometragens suspeitas
23 anúncios têm menos de 500 km com mais de 6 meses de matrícula. Pode ser verdade (carro de stock), mas também pode ser um erro de leitura, como nos ooyyo. Confirmar o km na ficha.

| Anúncio | km | 1.ª matrícula |
|---|---|---|
| IT-Treviso-648b05d1 | 10 | 12/2024 |
| NL-Brabant-57289618 | 15 | 06/2025 |
| BE-LTFnv-23102965 | 0 | 06/2025 |
| FR-AutoScout24Lux-ae565a56 | 289 | 03/2025 |
| AT-Salzburg-55500397 | 45 | 11/2024 |
| AT-Klagenfurt-M2E87O | 263 | 12/2025 |
| CH-Oftringen-67KM4D | 250 | 01/2026 |
| FR-LABEGE-25Q4P2 | 10 | 06/2025 |
| FR-Marseille-G2XEGQ | 10 | 01/2026 |
| IT-ModugnoBA-56E8DW | 20 | 09/2025 |
| IT-Firenze-LGR5PX | 15 | 03/2026 |
| PL-Wroclaw-V3O495 | 11 | 02/2026 |
| DE-Bielefeld-6G0GNW | 21 | 08/2024 |
| DE-Bielefeld-G7X858 | 30 | 03/2025 |
| IT-Bergamo-M702LW | 20 | 12/2025 |
| DE-ndOOYYOnomostr-85631517 | 100 | 02/2026 |
| DE-ndOOYYOnomostr-85860429 | 100 | 02/2026 |
| AT-ndOOYYOnomostr-40008678 | 34 | 06/2024 |
| AT-ndOOYYOnomostr-60103266 | 3 | 02/2026 |
| AT-ndOOYYOnomostr-15005346 | 2 | 05/2025 |
| AT-ndOOYYOnomostr-11101643 | 9 | 11/2025 |
| AT-ndOOYYOnomostr-15004780 | 9 | 11/2025 |
| DE-Bielefeld-d70dc0e9 | 21 | 08/2024 |

## 5. Tipo de vendedor em falta
41 anúncios ativos não têm `tipo` (Approved, Porsche Center ou independente). Lista: `LT-ndoveonomostra-32859006`, `DE-ndoveonomostra-8832af28`, `DE-ndoveonomostra-5051f330`, `LV-ndoveonomostra-x`, `DE-ndoveonomostra-ae1de59d`, `AT-ndoveonomostra-19674971`, `DE-ndoveonomostra-f5c84e9e`, `SK-ndoveonomostra-x`, `DE-ndoveonomostra-4c0bab11`, `DE-ndoveonomostra-0e63cc00`, `DE-ndoveonomostra-6afcc8a4`, `DE-ndoveonomostra-183fc85a`, `IT-ndOOYYOnomostr-69582281`, `IT-ndOOYYOnomostr-x`, `IT-ndOOYYOnomostr-07619095`, `IT-ndOOYYOnomostr-8783319`, `FR-ndOOYYOnomostr-34852424`, `FR-ndOOYYOnomostr-31811871`, `FR-ndOOYYOnomostr-73812778`, `FR-ndOOYYOnomostr-73860553`, `FR-ndOOYYOnomostr-90541305`, `FR-ndOOYYOnomostr-90554764`, `FR-ndOOYYOnomostr-18772565`, `DE-ndOOYYOnomostr-86734326`, `DE-ndOOYYOnomostr-85631517`, `DE-ndOOYYOnomostr-x`, `DE-ndOOYYOnomostr-85860429`, `BE-ndOOYYOnomostr-11527846`, `BE-ndOOYYOnomostr-11561521`, `BE-ndOOYYOnomostr-11562682`, `AT-ndOOYYOnomostr-40008678`, `AT-ndOOYYOnomostr-60103266`, `AT-ndOOYYOnomostr-30105296`, `AT-ndOOYYOnomostr-30104884`, `AT-ndOOYYOnomostr-15005346`, `AT-ndOOYYOnomostr-11101643`, `AT-ndOOYYOnomostr-15004780`, `DE-ndoveonomostra-bc2cca7d`, `DE-ndoveonomostra-c65ca711`, `DE-ndoveonomostra-565454ad`, `DE-ndoveonomostra-5749ffcd`.

## 6. Equipamento por preencher
Cerca de 555 anúncios vêm com todos os campos `eq_*` vazios e sem `fonte_equipamento`. Nenhum é Excelente ou Bom, por isso a prioridade é baixa: preencher só quando a ficha for aberta por outro motivo.

## 7. Ficheiros pedidos a 12/11 que ainda não chegaram
- `inventario_pz_<data>.json` (inventários públicos dos Porsche Zentren);
- `fichas_iva_<data>.json` (Suécia, Croácia e Hungria, prioridade ao Zagreb `Z52DNE`).

## Entrega
O zip diário habitual. Basta acrescentar o que estiver pronto; não é preciso esperar por tudo.
