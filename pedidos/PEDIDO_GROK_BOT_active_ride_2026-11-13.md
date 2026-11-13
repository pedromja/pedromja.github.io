# Pedido ao Grok Bot: procurar Taycan J1.2 com Porsche Active Ride (13/11/2026)

O Pedro quer alargar a procura a carros com **Porsche Active Ride** (código de opção **1P8**). Hoje o site só tem 2 berlinas 4/4S com Active Ride em 189. É uma opção rara: não existe no Taycan base, vem de série no Turbo GT e aparece sobretudo em GTS, Turbo e Turbo S. Regras de sempre: só leitura pública, sem login, sem contornar anti-bot, sem contactar vendedores, sem dados pessoais, sem veredictos.

## O que procurar
- Taycan J1.2, 1.ª matrícula ≥ 03/2024, só stands (sem particulares), sem acidente.
- **Versões:** 4, 4S, GTS, Turbo e Turbo S. O Turbo GT fica de fora.
- **Carroçarias:** berlina primeiro, depois Sport Turismo e Cross Turismo.
- **Preço:** até **135.000 €** de anúncio.
- **Prioridade:** berlinas 4S e GTS com InnoDrive (P4S) e 4+1 (5KA).

## Onde
1. **Porsche Finder (DE, AT, BE, NL, LU, FR, IT, ES, PL, CZ, SK, SI, HR, SE):** usar o filtro público de equipamento "Porsche Active Ride", se a pesquisa o tiver. Se não tiver, abrir as fichas das versões GTS/Turbo/Turbo S e procurar "Porsche Active Ride" na lista de equipamento.
2. **Sites dos Porsche Zentren** (a lista `lista_pz.json`): nos 42 carros J1.2 que hoje só aparecem no site do stand, ver se a ficha tem Active Ride.
3. **AutoScout24:** pesquisa por texto "Active Ride" nos Taycan ≥ 03/2024.
4. **Berlinas de 2024:** incluir, porque a lista de berlinas do Finder começa em 2025.

## Confirmar onde as fontes discordam
- **Ingelmunster GTS L6683Z:** o anúncio diz Active Ride, mas a lista de opções do configurador que o Pedro guardou não tem o 1P8. Confirmar na ficha.
- **Os 6 Taycan 4 marcados com Active Ride:** confirmar na ficha, porque é raro nessa versão.

## Entrega
No zip diário, um `active_ride_<data>.json` com um registo por carro, no formato `carros` com `registo_v7`. Campos: código, URL, versão, carroçaria, 1.ª matrícula exata, km, preço, país, stand, tipo de vendedor, InnoDrive, 5KA, eixo traseiro (0N5), FT3/FT1, 7Y8, cor, VIN se aparecer, e onde se leu o Active Ride (lista de equipamento da ficha, texto ou filtro). Incluir também os carros já conhecidos que forem confirmados ou desmentidos.
