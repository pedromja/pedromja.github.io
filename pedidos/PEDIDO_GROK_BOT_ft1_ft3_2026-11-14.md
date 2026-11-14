# Pedido ao Grok Bot: 3D Park Assist (FT3) e Remote ParkAssist (FT1) em todos os anúncios (14/11/2026)

O site passou a mostrar em todo o lado se cada carro tem:
- **3D Park Assist (FT3):** Surround View 3D com estacionamento ativo. O carro estaciona sozinho com o condutor dentro.
- **Remote ParkAssist (FT1):** estaciona sozinho com o condutor fora, comandado pelo telemóvel. Inclui o 3D Park Assist.

Quando não se sabe, o site mostra "?". Hoje, nos carros à venda:

| | Sabemos o código | Só "Surround View", sem código | Sem informação |
|---|---|---|---|
| Todos | 160 (75 FT1, 85 FT3) | 858 | 182 |
| Berlinas de 5 lugares | 74 (30 FT1, 44 FT3) | 264 | 34 |

Regras de sempre: só leitura pública, sem login, sem contornar anti-bot, sem contactar vendedores, sem dados pessoais, sem veredictos.

## Pedido
1. Em **todas as fichas que abrires** (Finder, sites dos PZ, AutoScout24), devolver dois campos no `finder_estado` e no `enriquecimento`:
   - `FT1`: `sim` / `não`. Textos: "Remote ParkAssist", "Remote Park Assist", "Parken per App", código FT1.
   - `FT3`: `sim` / `não`. Textos: "ParkAssist inkl. Surround View", "Aktiver Parkassistent", "3D-Surround View", código FT3.
   - Se só disser "Surround View", sem estacionamento ativo nem Remote: `FT3: "provável"`. Se tiver o código antigo KA6: `KA6: sim`.
   - Se a ficha não tiver lista de equipamento: `n/d` (não `não`).
2. **Prioridade:**
   1. berlinas de 5 lugares (4+1) e carros do alerta de 48 h;
   2. os carros de "Surround View" sem código;
   3. os restantes, à medida que as fichas forem abertas.
3. **Os mesmos campos para os opcionais importantes que o site mostra com "?":** InnoDrive (P4S), eixo traseiro (0N5), ângulo morto (7Y8), Active Ride (1P8) e 5 lugares (5KA). Nesses, devolver `sim` / `não` / `n/d`, e `não` só quando a ficha tem a lista completa de equipamento.

## Entrega
No zip diário habitual, nos ficheiros `finder_estado_<data>.json` e `enriquecimento_<data>.json`. Não é preciso uma passagem à parte.
