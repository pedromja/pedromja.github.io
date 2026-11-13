# Pedido ao Grok Bot: mercados que as regras de importação podem tornar favoráveis (13/11/2026)

O Pedro pediu para ler este artigo e ver que mercados podemos estar a desvalorizar:
https://impostosobreveiculos.info/importacao/importar-um-automovel-electrico-para-portugal/

Regras de sempre: só leitura pública, sem login, sem contornar anti-bot (Bilbasen, mobile.de e afins continuam fora), sem contactar vendedores, sem dados pessoais, sem veredictos.

## 1. O que o artigo diz (lido pelo Claude Code a 13/11)
- Um elétrico comprado na UE não paga ISV nem IUC. Também não paga IVA em Portugal se for **usado**, isto é, se tiver mais de 6 meses **e** mais de 6.000 km. O site já aplica esta regra.
- Fora da UE paga-se o IVA português de 23 % à entrada, seja o carro novo ou usado, sobre o preço mais o transporte e os direitos aduaneiros.
- Os direitos aduaneiros são de 10 %, mas a Suíça e a Noruega pagam **0 %** num carro fabricado na UE, com certificado ou declaração de origem. Um Porsche alemão cabe aqui.
- O IVA suíço pode ser descontado na exportação. A Noruega quase não cobra IVA nos elétricos, por isso o preço sobe mais com o IVA português.
- O transporte até Portugal custa **500–750 €** a partir de Espanha, França e Itália, e **750–1.500 €** a partir da Alemanha, Bélgica, Países Baixos e Dinamarca. A legalização custa cerca de 200 €.

O site usa hoje 1.300 € de importação para qualquer país da UE. Os países próximos ficam um pouco penalizados (cerca de 500–700 €) e os distantes ficam com o custo subestimado.

## 2. Mercados a investigar
O site já cobre a UE continental, a Suíça e a Noruega. Hoje, todos os anúncios suíços e noruegueses dão Caro, porque fora da UE se paga o IVA português (23 %) à entrada, mesmo num carro usado. As hipóteses abaixo são do Claude Code e **têm de ser confirmadas**: quero factos e fontes, não conclusões.

| Mercado | Porque pode compensar | O que confirmar |
|---|---|---|
| **Canárias** (Las Palmas, Santa Cruz de Tenerife) | Fora do IVA da UE; imposto local (IGIC) baixo. Os anúncios espanhóis das Canárias podem estar a ser tratados no site como Espanha (IVA 21 %). | Se o stand vende para exportação sem IGIC; custos de envio por barco até Portugal; IVA 23 % e despacho à chegada; lista dos Taycan J1.2 à venda nas Canárias (Finder ES e AutoScout24 ES) com cidade. |
| **Andorra** | Imposto local (IGI) de 4,5 %; união aduaneira com a UE para carros. | Se há Porsche Centre com Taycan J1.2 usados e preços; se o IGI não se cobra na exportação; papéis e custos de despacho. |
| **Dinamarca** | IVA de 25 % (arbitragem para carros "novos") e imposto de registo com devolução na exportação. Hoje não há nenhum anúncio dinamarquês no site. | Taycan J1.2 no Finder DK; como funciona a devolução do imposto de registo para elétricos; se os stands vendem para exportação. Não usar Bilbasen. |
| **Finlândia** | IVA de 25,5 % e devolução do imposto automóvel na exportação. Hoje não há nenhum anúncio finlandês no site. | Taycan J1.2 no Finder FI; regras da devolução na exportação. |
| **San Marino e Liechtenstein** | Fora do IVA da UE, mas dentro da união aduaneira (San Marino) ou do território aduaneiro suíço (Liechtenstein). Já há um anúncio de San Marino no site. | Como se fatura para um particular português; IVA à chegada; papéis. |
| **Suíça e Noruega** (confirmar o modelo) | O site tira o IVA local, soma o IVA português de 23 % e cerca de 2.100 €. | Direitos aduaneiros a 0 % para um Porsche de origem UE (que prova de origem é precisa); devolução do IVA suíço de 8,1 % na exportação; IVA norueguês dos elétricos na exportação; custo de despachante e transporte. |

Ficam fora, pela regra do volante à esquerda: Reino Unido, Irlanda, Malta e Chipre.

## 3. Custo de transporte por origem
Para afinar o custo de importação por país, recolher **3 cotações públicas** (sites de transporte de automóveis em camião, sem pedir orçamento com dados do Pedro) para levar um carro até Lisboa a partir de: Madrid, Barcelona, Lyon, Milão, Munique, Hamburgo, Bruxelas, Viena, Varsóvia, Bratislava, Zagreb, Estocolmo e Zurique. Indicar se o camião é aberto ou fechado, o prazo e o seguro.

## 4. Entrega
Num zip:
- `mercados_importacao_<data>.md`, com o resumo do artigo e, por mercado, o regime fiscal à saída e à chegada, os custos e as fontes (links);
- `anuncios_mercados_novos_<data>.json`, com os Taycan J1.2 encontrados nesses mercados, no formato `carros` com `registo_v7`, e com cidade e país corretos (Canárias e Andorra à parte).
