# Pedido ao Grok Bot: registo v7 dos J1.2 excluídos e dos brancos (07/11/2026)

Obrigado pela entrega `entrega_j12_todos_2026-11-07` (32 carros). Para os poder pontuar, o `add_novos.py` do Claude Code precisa dos campos do **modelo v7**, os mesmos que o `v7_registo.py` / `build_excel_v8.py` calculam do teu lado:

`justo_v7`, `posto_v7`, `pen_v7`, `verd_v7`, `os`, `novo_origem` e `meses`

Estes campos são dados do modelo base, não um veredicto teu. O v8 é aplicado pelo Claude Code.

## Pedido
1. **Correr o `v7_registo.py` sobre:**
   - os **32** carros de `excel_data_j12_excluidos_preco_innodrive_2026-11-07.json`;
   - os **4 brancos** de 06/11: `ZL8VO4`, `GRQ2RN`, `57R6VM` e `GEDWDQ`.

   O preço e o InnoDrive não excluem nenhum carro. O InnoDrive fica `Não` ou `Desconhecido` no campo `eq`, e o v8 trata disso.
2. **Abrir as 4 fichas do Finder que não foram lidas** e preencher o equipamento:
   - `G7VNR8`, `0OE47L`, `RNM80Q` e `N227ML`.
3. **Prioridade às berlinas:**

   | Código | Carro | Preço | Ponto a confirmar |
   |---|---|---|---|
   | `T60K3YK2` | Turbo, FR, 07/2025 | 114.900 € | — |
   | `RNM80Q` | Black Edition, ES, 10/2026 | 121.900 € | — |
   | `N227ML` | GTS, FR, 06/2025 | 124.800 € | — |
   | `9819fc5f` | 4, IT, 03/2025, 48.000 km | 95.000 € | — |
   | `2266c8cb` | 4S, DE, 12/2024 | 99.800 € | tem eixo traseiro e Surround View; diz 4 lugares: confirmar 5KA |
   | `MEQJ9XWM` | 4S, BG, 05/2025 | 79.998 € | confirmar 5KA e equipamento |
4. **sauto.cz e willhaben:**
   - confirmar a 1.ª matrícula (mês e ano), a carroçaria e o InnoDrive, quando a ficha o mostrar;
   - **não pôr "Berlina" por suposição**: se a carroçaria não for clara, usar `null`.

## Entrega
`excel_data_j12_registo_<data>.json`, no formato `excel_data` (como em `registos_novos_2026-11-06.json`), com um `LEIA-ME` curto.

## Adenda (07/11, noite): fichas do Das WeltAuto
Obrigado pelas 22 fichas do Das WeltAuto. Revelaram que **8 registos da base vindos do agregador ooyyo estavam errados**: versão "Taycan", carroçaria "Sedan" e km de 1 a 45. O Claude Code retirou-os do site até haver registo correto.

**Pedido:**
1. **Refazer o `registo_v7` destes carros com os dados das fichas** (versão, carroçaria, km, 1.ª matrícula exata, preço de hoje e equipamento):
   - `55500397`, `60103266`, `30105296` (é berlina: 4 Black Edition 08/2026), `30104884`, `11101643`, `15004780`.
   - Sobre os outros dois:
     - `15005346` é o mesmo carro que `AT-Wien-e93e3041` e já está no site.
     - `40008678` deu 404.
2. **Registo v7 para os que ainda não estão no site:**
   - `30105058` (Taycan Black Edition **berlina** 05/2026, 109.900 €, Approved, 4+1);
   - `15005131` (4S Sport Turismo 04/2024);
   - `30104127` (Taycan Sport Turismo 08/2025).
3. **Confirmar três aliases que parecem errados.** Nestes casos o código do Finder aponta para outro país:
   - `11102045` → `finder:QVV5MW` (no site é um carro de Madrid);
   - `60102686` → `finder:KP287P` (no site é um carro da Noruega);
   - `15002213` → `finder:P4E37O` (no site é de Hilzingen, DE).
4. **Corrigir o parser do ooyyo/dasweltauto na rotina**: os km vêm em milhares cortados.
