# Ordem ao Grok Bot · 16/11/2026 (tarde) — tudo o que o Claude Code recomenda, aprovado pelo Pedro

Completa a `ORDEM_GROK_BOT_negociacao_2026-11-16.md` (regras e grupos continuam válidos) e aprova a `ADENDA_ORDEM_GROK_primeiros_contactos_2026-11-16.md`.

**Regras:** não aceitar negócio, não reservar, não pagar nem assinar. Não enviar passaporte nem telefone. A **morada postal** pode ser dada só quando o stand a pede para a oferta (pedir ao Pedro; nunca guardar em ficheiros, zips ou repositórios). Não pedir rodas de inverno (se o stand as oferecer, não recusar). Validade pedida: **5/12/2026**. Entrega: **até 10/12/2026**. Nota do Google Translate e inglês por baixo nos emails noutra língua.

**Envio:** primeiros contactos e insistências com texto pré-definido → validar o email com o Pedro, guardar, **enviar**. Respostas em conversas abertas com texto novo → **rascunho** para o Pedro rever e enviar.

## A. Hoje (rascunhos para o Pedro rever) — textos em `pedidos/RESPOSTAS_stands_2026-11-16.md`
1. **PZ Siegen · 4560KQ:** texto 1 (link e preço; não receberam o email de 06/11).
2. **Centro Porsche Alicante · QVPW4Z:** texto 2 (é um usado Approved; link e preço).
3. **PZ Bonn · 20P2V5 + GTS 7N04NW:** texto 3 (continuar por escrito; pedir a proposta dos dois).
4. **Porsche Centrum Sopot · 08W58N:** texto 4 (custo e prazo da entrega em Portugal; validade).
5. **Porsche Zenter Lëtzebuerg · M73KGO:** texto 5a, com a morada que o Pedro te der.
6. **Centre Porsche Lorient · 7N4737:** texto 5b, com a morada, sem telefone.
7. **PZ Bratislava · RG77M4:** responder ao email da proposta em eslovaco com este texto:
```
Dear Sir or Madam,

Thank you for your email and for arranging a new battery health check.

A written offer in Slovak is fine for me. If possible, please state clearly the validity date (I would ask for 5 December 2026), the deposit amount and the payment terms.

Regarding my travel dates: I plan to travel in the first days of December and to complete the purchase and handover by 10 December 2026 at the latest. I will confirm the exact date once I have reviewed all the details.

I am not confirming the purchase or paying a deposit at this stage.

Kind regards,
Pedro Andrade
```

## B. Hoje (primeiros contactos aprovados, da adenda) — validar email, guardar, enviar o texto B
8. **PZ Landau · 4 V4X3Z9** — https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-gebraucht-V4X3Z9
9. **PZ Ulm-Neu-Ulm · Turbo EXGVO6** — https://finder.porsche.com/de/de-DE/details/porsche-taycan-turbo-gebraucht-EXGVO6
10. **PZ Holzwickede/Dortmund · 4S WKEEVM** — https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-WKEEVM
11. **PZ Hannover:** quando o stand responder ao C4 enviado às 10:37, criar um rascunho na mesma conversa a perguntar também pelo Taycan 4 **NQV3RV** (104.900 €) e pelo Taycan **6476R5** (101.850 €), como alternativas no mesmo stand.

## C. Esperar e insistir (texto D da secção D de `PEDIDO_GROK_BOT_rascunhos_negociacao_2026-11-16.md`, adaptando a data do primeiro email)
| Stand · carro | Se não houver resposta humana até | Ação |
|---|---|---|
| Porsche Centre Ingelmunster · L6683Z ("um colega vai contactá-lo") | 18/11 | insistência D em NL + EN, a perguntar pela proposta escrita |
| PZ Kassel · 9PERGW | 18/11 | insistência D-DE |
| PZ Wettenberg · M4EGLE (só automática) | 19/11 | insistência D-DE |
| PZ Pforzheim · DNDG5P (só automática) | 19/11 | insistência D-DE |
| PZ Reutlingen · PLGE5G (só automática) | 19/11 | segunda insistência D-DE |
| Porsche Centrum Rotterdam · 9094KD | 19/11 | segunda insistência D-NL |
| PZ Hannover · 454OWZ (C4 enviado 16/11) | 19/11 | lembrete curto em inglês |
| PZ Tirol · QL47PW (pergunta do IVA) | 19/11 | lembrete curto em inglês |
| PZ Braunschweig · 56750V | hoje | rascunho C7 (continuar por escrito, sem telefone) |

As insistências com texto D: validar o email (já guardado) e **enviar**. Os lembretes curtos: **rascunho**.

**Não escrever:** Bielefeld EXR720 (reservado a 16/11; avisar se a reserva cair), Bologna 20OE7P (não exporta), Magdeburg PV0N2R (só disponível a 20/01/2027).

## D. Recolha diária (no zip habitual)
1. Em todas as fichas abertas: **FT1, FT3, KA6, P4S, 0N5, 7Y8, 1P8, 5KA** com `sim` / `não` / `n/d` (como já fizeste a 15 e 16/11).
2. Incluir no `excel_data`, com `registo_v7` completo, os 6 anúncios novos ainda sem veredicto: Dortmund 326XVZ, Barcelona XZR4KX, Bonn 44R7QZ, Gießen 56PQEV, Louvain-la-Neuve QORRN8, Madrid Norte NOMRGV.
3. Abrir todos os dias a ficha dos carros em negociação e dos da adenda (estado, preço, reserva, "Verfügbar ab").
4. `negociacao_<data>.json` só com factos (o que foi enviado, sem endereços; respostas; preço, validade, SoH, VIN, matrícula, km, garantia, exportação, pagamento, o que o stand pede). Anexos técnicos sem dados pessoais à parte; PDFs com dados pessoais ficam fora.

## E. Avisar o Pedro de imediato se
- algum stand mandar uma **proposta escrita com validade**;
- algum carro em negociação ficar **reservado ou vendido**;
- a reserva do **Bielefeld EXR720** cair;
- algum stand pedir **sinal, assinatura ou dados pessoais** além da morada.
