# Pedido ao Grok Bot: registo v7 dos 4 brancos (06/11/2026)

Obrigado pela recolha dos brancos (`entrega_brancos_2026-11-06`), que está muito bem documentada.

## Falta uma coisa para os poder pontuar
Os 4 registos vieram com `justo_v7`, `posto_v7`, `pen_v7`, `verd_v7`, `os` e `novo_origem` a `null`. O `add_novos.py` do Claude Code **precisa destes campos** para calcular o v8. São os mesmos que o `build_excel_v8.py` calcula para os outros carros. São dados do modelo v7, não uma pontuação nova.

**Pedido:** correr o `build_excel_v8.py` sobre os 4 brancos e devolver o registo completo no formato do `excel_data` (como em `registos_novos_2026-11-06.json`):

| Código | Carro |
|---|---|
| `ZL8VO4` | 4S Black Edition berlina 12/2025, Friedrichshafen, 119.870 € |
| `GRQ2RN` | Taycan Sport Turismo 03/2025, Lörrach, 87.499 € |
| `57R6VM` | Taycan Sport Turismo 03/2025, Wuppertal, 89.900 € |
| `GEDWDQ` | 4 Cross Turismo 07/2024, Innsbruck, 87.990 € |

Por registo, devolver:
- `justo_v7`, `posto_v7`, `pen_v7`, `verd_v7`, `os`;
- `novo_origem` e `meses`;
- `primeira_matricula_exata`.

**Sem** somar o wrap: o Claude Code soma os 4.000 € no `add_novos.py` e decide se o carro fica (só entra se ainda for Bom ou Excelente).

O `posto_v7` deve ser o normal, sem o wrap.
