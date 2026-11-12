# Pedido ao Grok Bot: tarefas da estratégia multimercado (12/11/2026)

O Pedro aprovou a estratégia (`ESTRATEGIA_pesquisa_multimercado_2026-11-12.md`). Estas são as tarefas do lado do Grok, por ordem de prioridade. Regras de sempre: só leitura pública, sem login, sem contornar anti-bot, sem contactar vendedores, sem dados pessoais, sem veredictos.

## 1. Fichas no próprio dia para os carros em alerta (eixo 1 e 4)
A rotina do Claude Code passa a assinalar, de manhã, os carros em **alerta de 48 h**. A lista de hoje:
`EXR720`, `9PERGW`, `L6683Z`, `4XK4Z5`, `3K674M`, `EXGVO6`, `3KDW90`, `NP93G9`, `QOLVR2`, `Z52DNE` (Zagreb), `4317baae` (AS24 Helmstedt).

Para estes, **todos os dias**, abrir a **ficha** (não a lista) e devolver no `finder_estado`: estado, preço, "Verfügbar ab", SoH se aparecer, e `nota: "reserva caiu"` quando for o caso. Os carros que entrarem no alerta nos dias seguintes vêm no resumo diário do Claude Code; o Pedro reencaminha.

## 2. Inventários públicos dos Porsche Zentren (eixo 5)
Os sites dos PZ alemães têm uma página pública de stock com a mesma estrutura, por exemplo:
- `https://hannover.porsche.de/de/inventory/porsche/454OWZ`
- `https://bamberg.porsche.de/de/inventory/porsche/porsche-taycan-4s-gebraucht-64L54W`

Pedido:
1. Construir a lista dos domínios `*.porsche.de` (e `*.porsche.at`) dos Porsche Zentren e ler, **uma vez por dia**, a página de stock de Taycan de cada um (sem login; se bloquear, `sem_leitura`).
2. Cruzar por código (o mesmo do Finder) e devolver `inventario_pz_<data>.json` com, por carro: código, stand, preço no site do stand, preço no Finder, preço na AutoScout24 (quando existir), km, 1.ª matrícula, "Vorführwagen / Firmenwagen / Tageszulassung / Dienstwagen" se aparecer, e URL.
3. Assinalar à parte:
   - **carros que só estão no site do stand** e ainda não no Finder;
   - **diferenças de preço** entre canais (≥ 500 €).

## 3. Carros "novos" para efeitos de IVA em países com IVA > 23 % (eixo 6)
Hoje há 21 Taycan na Suécia (14), Croácia (4) e Hungria (3). Para os que tiverem **menos de 6 meses ou menos de 6.000 km a 10/12/2026**, devolver a ficha completa no formato `carros` com `registo_v7` (InnoDrive, 5KA, 0N5, FT3/FT1, 7Y8, VIN, matrícula exata, km, preço bruto e **preço sem IVA** se o anúncio o mostrar). Prioridade ao **Zagreb 4S Z52DNE** (Excelente 89).

## 4. Demos e carros de serviço (eixo 7)
Nas fichas do Finder e da AutoScout24, passar a devolver o campo `uso_anterior` com o que a ficha disser: `Vorführwagen`, `Firmenwagen`, `Dienstwagen`, `Tageszulassung`, `Mietwagen`, `Leasingrückläufer`, ou `n/d`. Começar pelos carros de 2026 com menos de 8.000 km.

## 5. Correção pedida de novo
As "reservas caídas" repetem-se todos os dias (Willich, Hamburg, Essen…). Comparar com a **leitura do dia anterior**, não com a lista do pedido de 03/11. Só é "reserva caiu" se ontem estava reservado e hoje não.

## Entrega
Um zip por dia com o `finder_estado_<data>.json` habitual, mais `inventario_pz_<data>.json` quando houver, e as fichas do ponto 3 num `fichas_iva_<data>.json`.
