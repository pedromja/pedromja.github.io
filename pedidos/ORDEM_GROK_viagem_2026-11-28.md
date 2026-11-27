# Ordem ao Grok Bot — preços reais da viagem (28/11/2026)

Objetivo: preços **reais e atuais** (pesquisa ao vivo nos sites, não médias de rota) para uma viagem **só de ida, 2 adultos**, a reservar até **sábado 28/11 às 18h (Lisboa)**. Não reservar nada, não fazer login, não usar proxies nem contornar bloqueios; parar e indicar o site quando houver bloqueio. Sem dados pessoais.

## 1. Voos — segunda 30/11/2026, partida de Lisboa (LIS) às 13:00 ou depois

Para cada destino, todos os voos (diretos primeiro, depois com 1 escala até 7 h de viagem total):
- **LIS → Frankfurt (FRA)** — destino principal
- LIS → Estugarda (STR), LIS → Munique (MUC), LIS → Düsseldorf (DUS) — alternativas

Por voo: companhia, número do voo, hora de partida e chegada (hora local), duração, escalas, **preço total para 2 adultos em EUR** na tarifa mais barata com **bagagem de mão** e, à parte, o preço com **1 mala de porão de 23 kg** por pessoa; site onde o preço foi visto e hora da consulta. Fontes: TAP, Lufthansa, Eurowings, Ryanair/easyJet se houver, Google Flights/Skyscanner/Kayak.

## 2. Alojamento — quarto duplo, 2 adultos, preço total com taxas

| Noite | Onde | Pedido |
|---|---|---|
| 30/11 → 1/12 | junto ao aeroporto de Frankfurt (máx. 15 min) | 3 opções: a mais barata com nota ≥ 8, uma média, uma com estacionamento grátis |
| 1/12 → 2/12 | Pforzheim ou Estugarda | 3 opções, idem |
| 2/12 → 3/12 | Friedrichshafen (lago de Constança) | 3 opções, idem |
| 3/12 → 4/12 (alternativa) | Innsbruck (Áustria) | 2 opções |

Por hotel: nome, distância ao ponto indicado, preço total da noite para 2 com taxas (incluindo taxa turística quando existir), se o cancelamento é grátis e até quando, link e hora da consulta. Fontes: Booking.com, site do hotel, Expedia.

## 3. Carro de aluguer só de ida

- Levantamento: aeroporto de Frankfurt, segunda 30/11 às 18:00.
- Entrega (preço para cada uma): **Friedrichshafen** a 3/12 · **Estugarda (aeroporto)** a 3/12 · **Innsbruck** a 4/12 (indicar a taxa de entrega noutro país).
- Categoria compacta ou média, automático se possível, quilometragem ilimitada.
- Por oferta: empresa (Sixt, Europcar, Hertz, Avis, Enterprise…), preço total com a taxa de entrega noutra cidade/país, seguro incluído, link e hora da consulta.
- Comparar com **comboio** (Deutsche Bahn, Sparpreis, 2 pessoas): FRA → Aschaffenburg, Aschaffenburg → Pforzheim, Pforzheim → Friedrichshafen, Friedrichshafen → Innsbruck, com o preço total.

## Formato da resposta

Um zip `viagem_precos_2026-11-28.zip` com:
- `viagem_precos.json` — listas `voos`, `hoteis`, `aluguer`, `comboio`, com os campos acima e `fonte_url` + `consultado_em` em cada linha;
- `RESUMO.md` — a opção mais barata de cada bloco e o total da ida (voo + 3 noites + aluguer), em EUR.
