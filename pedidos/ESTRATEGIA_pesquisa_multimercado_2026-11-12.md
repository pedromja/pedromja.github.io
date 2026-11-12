# Estratégia de pesquisa de bons negócios · Taycan J1.2 · mercados europeus (12/11/2026)

Prazo: carro em casa a 15/12/2026, entrega até 10/12. Faltam 4 semanas. A estratégia assenta no que os dados de duas semanas (1.300 anúncios, 29/10–12/11) já mostram, e divide o trabalho entre o Claude Code (modelo e site), o Grok Bot (recolha) e o Pedro (contactos e decisão).

## O que os dados já provam
| Facto | Número | Consequência |
|---|---|---|
| Os Excelente saem em dias | 59 % vendidos ou reservados em 2 semanas; mediana **8 dias** à venda | Um Excelente novo tem de ser decidido em 48 h |
| Os Bom saem ao mês | 24 %, mediana 14 dias | Há tempo para negociar, não para esperar descidas |
| Os Caro não saem | 5 % | É neles que os stands baixam o preço (−2 % de cada vez) |
| Os stands alemães cortam preço no anúncio, não à mesa | Hannover, Leipzig, Bonn, Papendorf: 1,2 cortes por anúncio, 2–3 % cada; à mesa 0–1,3 % | Comprar logo a seguir a um corte, não antes |
| Há 230 carros de 2026 com menos de 8.000 km | demos e carros de serviço dos PZ, mediana 132.000 € postos | Vão ser escoados até ao fim do ano: é o segmento onde o preço mais vai descer |
| Fora da Alemanha quase não há Excelente/Bom | DE 69 em 527; FR 0 em 110; ES 0; NL 3; BE 2; IT 2; AT 3 | A Alemanha é o mercado; os outros servem para exceções (Ljubljana, Ingelmunster) |
| Polónia e Eslováquia: preço fixo | 0 % de desconto nas duas respostas | Só valem se o preço de tabela já for bom |

## Os 8 eixos da estratégia

### 1. Alerta de 48 horas para Excelente novos (o eixo mais importante)
Um Excelente dura 8 dias. A rotina passa a ter um **alerta imediato** quando entra um anúncio Excelente ou Bom ≥ 80 com o equipamento do Pedro (berlina, InnoDrive, 4+1, eixo traseiro ou estacionamento assistido). O alerta sai na manhã da recolha, com o email de contacto já preparado, para o Pedro o enviar nesse dia.
- Claude: regra no `build_all` que compara o ranking de hoje com o de ontem e destaca entradas novas no topo da página e no resumo diário.
- Grok: abrir a **ficha** desses carros no próprio dia (estado, VIN, SoH, "Verfügbar ab").

### 2. Probabilidade de sobrevivência por carro
Com as datas de entrada e saída de 1.300 anúncios, calcula-se para cada carro **a probabilidade de ainda estar à venda daqui a 7 dias**, em função do veredicto, do preço face ao justo, dos dias à venda e do país. Aparece no ranking como "risco de perder": alto, médio, baixo. Serve para ordenar os contactos: primeiro os bons com risco alto.
- Claude: modelo de sobrevivência simples (taxas por classe), atualizado todos os dias.

### 3. Cadência de cortes por stand ("quando é que este stand baixa outra vez?")
Cada Porsche Zentrum tem um ritmo: Hannover e Leipzig cortam 2–3 % de cada vez, a cada 2–3 semanas; Diez e Porsche Inter Auto (AT) cortam 5–6 % de uma vez. Com o histórico, estima-se para cada anúncio Caro/Justo parado **a data provável do próximo corte** e o preço a que deve chegar até 10/12.
- Claude: coluna "próximo corte" no ranking e no mapa, com data e valor previstos.
- Uso: para os carros que o Pedro quer mas estão caros, esperar o corte em vez de pedir desconto; pedir desconto só depois do corte, quando o stand já decidiu baixar.

### 4. Reservas que caem e anúncios que reaparecem
Uma reserva que cai (D4NK4K, NK804N, L85WP9) ou um anúncio que volta (EXR720) quer dizer financiamento falhado ou comprador desistente. O stand já perdeu semanas e está mais aberto. Estes carros passam a ter um selo **"reserva caiu"** com a data, e entram no alerta do eixo 1.
- Grok: já marca; passa a abrir sempre a ficha desses carros no dia seguinte, para confirmar que continuam livres.

### 5. Inventário sombra: os sites dos próprios Porsche Zentren
Os anúncios do Bamberg vieram de `bamberg.porsche.de/inventory`, com códigos que o Finder também tem, mas por vezes com preços e fotos diferentes e carros que ainda não estão no Finder. Há cerca de 90 Porsche Zentren alemães com a mesma estrutura de página pública.
- Grok: ler, uma vez por dia, os inventários públicos dos PZ alemães e austríacos (lista de domínios `*.porsche.de/de/inventory`), sem login e sem contornar bloqueios; cruzar por código e assinalar **carros que só aparecem no site do stand** e **diferenças de preço** entre o site do stand, o Finder e a AutoScout24. Compra-se pelo canal mais barato.

### 6. Arbitragem de IVA nos carros "novos" para efeitos fiscais
Um carro com menos de 6 meses ou menos de 6.000 km à entrega paga IVA em Portugal (23 %) e é faturado sem o IVA de origem. Em países com IVA acima de 23 % isso **baixa** o preço: Hungria (27 %), Dinamarca, Suécia, Croácia (25 %). Hoje há 21 anúncios nesses países (14 na Suécia, 4 na Croácia, 3 na Hungria). Também joga ao contrário: um carro alemão de 19 % fica 3,4 % mais caro quando é "novo", por isso, na Alemanha, preferir carros que em 10/12 já contem como usados (matrícula até 09/06/2026 e mais de 6.000 km).
- Claude: já calcula o regime à entrega; passa a mostrar a **"vantagem de IVA"** em euros por carro, positiva ou negativa.
- Grok: fichas completas dos candidatos suecos, croatas e húngaros com InnoDrive e 4+1 (os que hoje faltam).

### 7. Demos e carros de serviço dos stands no fim do ano
Os 230 carros de 2026 com poucos quilómetros são, em grande parte, demos (Vorführwagen) e carros de serviço (Firmenwagen) dos próprios stands, como o Hannover 454OWZ. Têm de sair dos balanços até 31/12, e os PZ têm objetivos trimestrais. É o grupo onde o preço mais vai descer entre 20/11 e 10/12.
- Grok: marcar nas fichas "Vorführwagen", "Firmenwagen", "Tageszulassung" e "Dienstwagen".
- Claude: segmento próprio no mercado, com a curva de preço desta semana contra a semana passada, para apanhar o momento em que começam a baixar.
- Pedro: nos contactos com estes carros, a data de visita entre 1 e 10/12 é um argumento, porque o stand quer fechar antes do fim do ano.

### 8. Leilão silencioso de propostas escritas
Em vez de negociar carro a carro, o Pedro pede a 4–6 stands, no mesmo dia e com o mesmo texto, uma **proposta escrita vinculativa com validade até 5/12**, para carros equivalentes. Depois escolhe. Os stands alemães respondem a isto com mais do que à pergunta "qual é o melhor preço?", porque percebem que há concorrência real sem que ninguém tenha de inventar nada. As propostas de Hannover e Bratislava já estão a caminho; faltam Kassel, Bielefeld, Bonn e Wettenberg.
- Claude: um só texto, em alemão e inglês, com o prazo e os pontos a incluir (preço, matrículas de exportação, SoH, reparações, validade).
- Pedro: envia; responde só depois de ter 3 propostas na mão.

## Mercados: onde procurar e o que esperar
| Mercado | Papel | Nota |
|---|---|---|
| Alemanha | principal: 90 % dos bons negócios | cortes no anúncio, 1–1,5 % à mesa; demos no fim do ano |
| Áustria | segundo mercado, mesma língua | preços 5–10 % acima dos alemães; Porsche Inter Auto corta 5 % de uma vez |
| Eslovénia, Bélgica, Luxemburgo | exceções pontuais | Ljubljana e Ingelmunster são dos melhores do ranking |
| Polónia, Eslováquia, Chéquia | preço fixo | só se a tabela já for boa (Bratislava RG77M4); confirmar sempre exportação |
| Suécia, Croácia, Hungria | arbitragem de IVA | só carros "novos" para efeitos fiscais; poucos anúncios, mas com margem |
| França, Espanha, Itália | fracos | sem Excelente/Bom; Itália pode recusar exportação |
| Suíça, Noruega | fora | alfândega e IVA à entrada: não compensa |

## Calendário até 10/12
| Semana | O que acontece |
|---|---|
| 13–19/11 | eixos 1–4 no site; Grok começa os inventários dos PZ (eixo 5) e as fichas SE/HR/HU (eixo 6); Pedro envia o pedido de propostas escritas (eixo 8) |
| 20–26/11 | propostas na mão; escolha dos 2 finalistas; marcar visita; primeira vaga de cortes nos demos |
| 27/11–3/12 | visita e contrato; sinal só depois da minuta revista; matrículas de exportação |
| 4–10/12 | levantamento e viagem; margem de 5 dias para imprevistos |

## O que precisa de aprovação do Pedro
1. O alerta de 48 h e a probabilidade de sobrevivência entram no site: sim ou não.
2. O Grok passa a ler os sites dos Porsche Zentren (público, sem login): sim ou não.
3. O "leilão silencioso": a lista de stands a quem pedir proposta escrita e a data-limite (sugestão: 5/12).
