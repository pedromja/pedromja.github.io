# Pedido ao Grok Bot: distinguir FT1 de FT3 em todos os anúncios (14/11/2026)

O Pedro quer ver em todo o site se cada carro tem **FT1** ou **FT3**:
- **FT1 · Remote ParkAssist:** o carro estaciona sozinho com o condutor fora, comandado pelo telemóvel. Inclui o FT3.
- **FT3 · ParkAssist com Surround View e estacionamento ativo:** câmaras 360°, e o carro estaciona sozinho com o condutor dentro.

Hoje o site sabe o código em 160 carros à venda (75 FT1 e 85 FT3). Há **865** em que o anúncio só diz "Surround View" sem se saber qual dos dois. Regras de sempre: só leitura pública, sem login, sem contornar anti-bot, sem contactar vendedores, sem dados pessoais, sem veredictos.

## Pedido
1. Em **todas as fichas que abrires** (Finder, sites dos PZ, AutoScout24), devolver dois campos novos no `finder_estado` e no `enriquecimento`:
   - `FT1`: `sim` / `não`, conforme a lista de equipamento ("Remote ParkAssist", "Remote Park Assist", "Parken per App" ou o código FT1);
   - `FT3`: `sim` / `não` ("ParkAssist inkl. Surround View", "Aktiver Parkassistent", "Surround View" com estacionamento ativo, ou o código FT3).
2. **Prioridade:** primeiro as berlinas de 5 lugares (4+1) e os carros do alerta de 48 h; depois os restantes, à medida que as fichas forem abertas por outro motivo.
3. Se a ficha só disser "Surround View" sem estacionamento ativo nem Remote, devolver `FT3: "provável"`. Se tiver o código antigo KA6, indicar `KA6: sim`.

## Entrega
No zip diário habitual. Não é preciso uma passagem à parte.
