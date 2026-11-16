# Ordem ao Grok Bot: negociação a partir de 16/11/2026

**Substitui** o pedido `PEDIDO_GROK_BOT_rascunhos_negociacao_2026-11-16.md`. Os textos continuam nos mesmos ficheiros (indicados abaixo).

Regras de sempre: não aceitar negócio, não reservar, não pagar nem assinar; não enviar passaporte, morada nem telefone do Pedro; não pedir rodas de inverno; nota do Google Translate e inglês por baixo em todos os emails que não sejam em inglês; validade pedida até **5 de dezembro de 2026**; entrega até **10 de dezembro de 2026**.

## Grupo 1 · stands que já responderam → mesmo email, texto adaptado, RASCUNHO para o Pedro rever
Usar o **endereço da conversa anterior** e responder **dentro do mesmo fio** (Re:). Como o texto foi adaptado às últimas informações, fica em **rascunho**: o Pedro lê e envia.

| Stand · carro | Texto (em `pedidos/RESPOSTAS_stands_revistas_2026-11-13.md`) | Adaptação às últimas informações |
|---|---|---|
| PZ Hannover · 454OWZ | 4 (C4, versão ajustada a 16/11) | responde à pergunta de hoje às 08:30: ainda a analisar, sem negócio nem depósito; o anúncio subiu para 120.990 € mas a minuta de 09/11 diz 115.490 €: pedir que confirmem os 115.490 €; manter PIWIS, reparações no contrato, SoH e validade até 5/12 |
| Porsche Zenter Lëtzebuerg · M73KGO | 1 (C1) | responde à mensagem de 13/11; SoH, versão do PCM, fim da garantia, oferta escrita até 5/12 |
| PZ Tirol · QL47PW | 2 (C2) | a pergunta do IVA (carro usado em dezembro, particular: IVA austríaco de 20 % ou regime da margem); VIN e SoH continuam em falta |
| PZ Bratislava · RG77M4 | 3 (C3) | data da 1.ª matrícula (27 ou 29/11/2025), valor da reserva, validade até 5/12 |
| Porsche Centrum Sopot · 08W58N | 5 (C5) | SoH prometido para 09/11 continua em falta; particular; fatura sem IVA polaco |
| Centre Porsche Lorient · 7N4737 | 6 (C6) | SoH prometido continua em falta; COC; datas da garantia |
| PZ Braunschweig · 56750V | 7 (C7) | só pediram um número para ligar: continuar por escrito, sem dar o número |

O Centro Porsche Bologna (20OE7P) está fechado: não exporta. Não escrever.

## Grupo 2 · stands que nunca responderam → validar o email com o Pedro, guardar, ENVIAR a insistência
| Stand · carro | Texto (em `pedidos/PEDIDO_GROK_BOT_rascunhos_negociacao_2026-11-16.md`, secção D) |
|---|---|
| PZ Siegen · 4560KQ | D-DE |
| PZ Reutlingen · PLGE5G | D-DE (só veio a confirmação automática) |
| Porsche Centrum Rotterdam · 9094KD | D-NL |
| Centro Porsche Alicante · QVPW4Z | D-ES |

## Grupo 3 · primeiros contactos → validar o email com o Pedro, guardar, ENVIAR o email pré-definido
| Stand · carro | Texto |
|---|---|
| Porsche Centre Ingelmunster · GTS L6683Z | A: `pedidos/LEILAO_Ingelmunster_L6683Z_2026-11-16.md` |
| PZ Kassel · 4S 9PERGW | B: `pedidos/LEILAO_proposta_escrita_2026-11-12.md` (primeiro contacto) |
| PZ Bonn · 4 Black Edition 20P2V5 + GTS 7N04NW | B, com os dois carros na mesma mensagem e a pergunta do IVA (o 20P2V5 conta como novo) |
| PZ Wettenberg · 4S Black Edition M4EGLE | B |
| PZ Pforzheim · 4 Black Edition DNDG5P | B (o email de 06/11 nunca saiu) |

**Bielefeld EXR720:** reservado a 16/11. Não escrever. Se a reserva cair, avisar o Pedro e preparar o texto B com o pedido do SoH.

## Como validar e guardar os emails (grupos 2 e 3)
1. Para cada stand, mostrar ao Pedro o endereço que encontraste (no anúncio ou no site do stand) e o link do anúncio, e **esperar o "sim" do Pedro** a esse endereço.
2. Guardar o endereço validado na tua configuração local (por exemplo `contactos_stands.json`), por stand. **Não pôr os endereços nos zips nem em ficheiros públicos.**
3. Usar sempre esse endereço nas mensagens seguintes ao mesmo stand.
4. Só depois do "sim": enviar o email pré-definido (grupo 3) ou a insistência (grupo 2), sem mudar o texto.

## Ordem de trabalho
1. Grupo 3 (os melhores carros, com prazo apertado): Ingelmunster, Kassel, Bonn, Wettenberg, Pforzheim.
2. Grupo 1: rascunhos para o Pedro rever, começando por Hannover (perguntou hoje) e Luxemburgo.
3. Grupo 2: insistências.

## Depois
- Ler as respostas no Gmail, só em leitura.
- No zip diário, um `negociacao_<data>.json` só com factos: o que foi enviado (data, hora, stand, assunto, sem endereços), as respostas, preço, validade, SoH, VIN, 1.ª matrícula, km, garantia, custos de exportação, pagamento e o que o stand pede. Os PDFs com dados pessoais não entram no zip.
