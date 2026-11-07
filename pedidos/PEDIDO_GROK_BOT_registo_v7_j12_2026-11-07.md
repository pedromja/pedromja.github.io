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
