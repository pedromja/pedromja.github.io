# Ordem ao Grok Bot — Plano B: alternativas ao Taycan (21/11/2026)

O Pedro quer um plano B caso não compre um Taycan até 10/12. O Grok **só recolhe factos com fonte**. Não pontua nem dá veredicto: o Claude faz a pontuação e o Pedro decide. Ninguém é contactado.

## Âmbito
- Só **100 % elétricos**, com **5 lugares** e versão de **4 rodas motrizes**. Berlina, fastback, carrinha ou SUV.
- Mercado de usados com **até 18 meses** (1.ª matrícula a partir de 05/2025).
- Orçamento: posto em Portugal até cerca de 115.000 €.
- Modelos (acrescentar outros que encaixem):
  - Audi: e-tron GT, A6/S6 e-tron (Sportback e Avant), Q6/SQ6 e-tron
  - BMW: i5 (berlina e Touring), iX, iX3 Neue Klasse
  - Mercedes: CLA elétrico, EQE (berlina e SUV), GLC elétrico
  - Porsche Macan Electric
  - Lotus: Emeya, Eletre
  - Hyundai: Ioniq 6, Ioniq 5; Kia EV6; Genesis GV60 / Electrified GV70
  - Tesla Model 3 e Model Y (Long Range AWD e Performance)
  - Polestar 2, 3 e 4
  - Volvo: ES90, EX90, EX40
  - BYD Seal; Zeekr 001 e 7X; XPeng G6, G9 e P7+; NIO ET5/ET7
  - Lexus RZ

## O que recolher, por modelo (e por versão AWD quando mudar)
1. **Design:** prémios de 2024–2026 com link (World Car Design of the Year, Car Design Award, Red Dot, iF, Goldenes Lenkrad, Autobest, What Car?, Top Gear…) e o ano.
2. **Tecnologia**, com fonte:
   - arquitetura (400 V ou 800 V);
   - carga DC máxima (kW) e tempo de 10 a 80 %;
   - autonomia WLTP e consumo real (testes ADAC, Bjørn Nyland, Autobild);
   - bomba de calor de série;
   - atualizações remotas (OTA);
   - assistentes de condução (equivalentes a ACC, manutenção ativa na faixa, ângulo morto, câmara 360°, estacionamento remoto): de série ou opcional;
   - suspensão pneumática e eixo traseiro direcional.
3. **Fiabilidade:**
   - ADAC Pannenstatistik (2025/2026), TÜV Report, DEKRA, Consumer Reports e J.D. Power;
   - campanhas e recalls (KBA, Safety Gate/RAPEX, NHTSA) desde 2024;
   - garantia do carro e da bateria;
   - queixas recorrentes em fóruns de donos (resumo com link, sem dados pessoais).
4. **Valor residual:** valores residuais publicados aos 12, 24 e 36 meses (Autovista/Schwacke, DAT, Leaseplan/ALD, Autobild), com a fonte e o país.
5. **Portugal (Standvirtual e stands oficiais):**
   - para cada modelo, número de anúncios e preços pedidos de carros com 1 a 3 anos (mínimo, mediana, máximo), com km e versão;
   - quanto tempo ficam à venda, se der para ver;
   - se há rede oficial de assistência em Portugal (marca e cidades).
6. **Para o Taycan** (berlina J1.2, de 2024 a 2026), a mesma recolha em Portugal: Standvirtual, Porsche Approved PT e stands. Serve para a análise de revenda após 1 ou 2 anos.

## Formato a devolver (zip `alternativas_claude_<data>.zip`)
- `alternativas_modelos.json`: um registo por modelo/versão, com os campos acima; cada valor com `fonte` (URL) e `data`.
- `pt_precos_usados.json` / `.csv`: anúncios portugueses (modelo, versão, ano/mês, km, preço, vendedor, cidade, URL).
- `LEIA-ME.md`: o que foi lido, o que falhou e as limitações.

## Regras
- Não contornar bloqueios (Cloudflare, captcha, login). O que estiver bloqueado fica registado como bloqueado.
- Sem dados pessoais de vendedores particulares.
- Não contactar ninguém. Nada de pontuações.
