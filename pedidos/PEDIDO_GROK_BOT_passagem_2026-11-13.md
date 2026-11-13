# Pedido ao Grok Bot: seguimento da passagem de 13/11/2026

Obrigado pela entrega de hoje. Os eixos 5–7 já estão no site: os inventários dos Porsche Zentren, o uso anterior e as fichas de IVA. Seguem as correções e os próximos passos, por ordem de prioridade. Regras de sempre: só leitura pública, sem login, sem contornar anti-bot, sem contactar vendedores, sem dados pessoais, sem veredictos nem cálculo de posto.

## 1. Berlinas de 2024: alargar a lista do Finder
O inventário mostrou que a lista de berlinas do Finder começa em 2025. Por isso faltavam no site berlinas J1.2 de 2024, entre 03/2024 e 12/2024. São precisamente as que o Pedro prefere.
- Passar a lista de berlinas do Finder a **1.ª matrícula ≥ 03/2024**, como as Sport e Cross Turismo.
- Abrir hoje a ficha destas berlinas, que só aparecem no site do stand, com InnoDrive (P4S), 5KA, 0N5, FT3/FT1, 7Y8, VIN, 1.ª matrícula exata e SoH se aparecer:

| Código | Stand | Versão | Preço | km |
|---|---|---|---|---|
| M44EK8 | PZ Berlin | 4S | 84.930 € | 39.744 |
| OP37EO | PZ Düsseldorf | Taycan | 69.900 € | 24.293 |
| OGR9W7 | PZ Berlin | Taycan (Kreide) | 75.600 € | 31.334 |
| 3KZ4Q8 | PZ Freiburg | Taycan | 82.870 € | 26.071 |
| EKG405 | PZ 5 Seen | Turbo | 115.900 € | 49.700 |
| OGRR3L | PZ Garmisch-Partenkirchen | Taycan | 59.490 € | 94.373 |

## 2. Preços do Finder: enviar todos, não só os das fichas
Hoje, 61 carros tinham no site um preço antigo. O Finder e o site do stand já mostravam o mesmo preço mais baixo. O `finder_estado` só trouxe 15 preços.
- Nas linhas `na_lista`, preencher também `preco` com o valor que a lista mostra hoje. A lista basta para o preço; a ficha só é precisa para o estado.

## 3. Comparação com a AutoScout24: ligar só por código ou VIN
Das 95 "diferenças de preço", as que envolvem a AutoScout24 não são fiáveis. Dois exemplos:
- **Hannover 454OWZ:** 116.990 € no stand e 96.880 € na AS24. Os 96.880 € são o preço **sem IVA** de um anúncio de 115.290 €.
- **323D90:** 104.600 € no stand e 147.900 € na AS24. É outro carro com os mesmos km e o mesmo mês de matrícula.

Pedido:
- ligar à AS24 só quando o anúncio mostrar o mesmo código do stand ou o mesmo VIN;
- guardar sempre o preço **com IVA** (o "Brutto") e indicar se o anúncio o mostra sem IVA (`iva_texto`);
- as diferenças entre o **site do stand e o Finder** (mesmo código) estão certas. São essas que o site usa.

## 4. Posto em Portugal: não calcular
O resumo de hoje deu dois postos para o mesmo carro: 7K8X47 com 104.455 € e com 103.155 €, e QOLVR2 com 160.100 € e com 158.800 €. O posto é calculado pelo site, com a regra dos 6 meses a 10/12. O 7K8X47 conta como usado e fica a 99.100 € postos. Basta mandar o preço do anúncio.

## 5. Fichas de IVA: completar dois suecos
A Suécia tem dois candidatos com bom preço sem IVA, mas o equipamento-chave está "Desconhecido":
- **Danderyd 4S** (blocket 641a9406f1), 04/2026, 4.730 km, 1.020.000 SEK sem IVA, com eixo traseiro e Surround View;
- **Halmstad 4** (blocket db68507a84), 06/2026, 500 km, 956.000 SEK sem IVA.

Pedido: InnoDrive, 5 lugares (4+1), Active Ride e VIN, se a ficha ou a descrição os mostrarem. Indicar também se o vendedor aceita vender para exportação, se a ficha o disser.

## 6. Estados de hoje já aplicados no site
- **3K674M (Soest):** voltou a estar reservado. O site já o mostra assim.
- **NKOZ7L (Hamburg):** a reserva caiu. Abrir a ficha amanhã para confirmar que continua livre.
- **56837M e 64K0VD (Leipzig):** reservados, com "Verfügbar ab" a 30/11 e a 04/01/2027.

## 7. Pendentes da tua lista
Os 4 sites dos PZ por ler (St. Pölten, Allgäu, Bad Homburg, Stuttgart), quando for possível sem contornar bloqueios.

## Entrega
O zip diário habitual. Os pontos 1 e 2 são os mais úteis para amanhã.
