# Pedido ao Grok Bot: correção das entregas diárias (06/11/2026)

A entrega `taycan_claude_2026-11-06` foi integrada, mas tive de corrigir duas coisas à mão. Para as próximas entregas, por favor ajustar o seguinte.

## 1. O filtro de privacidade está a apagar dados que não são pessoais
Nas entregas de 05/11 e 06/11 apareceu `[vendedor omitido]` ou `[contacto omitido]` em campos que são dados de **empresas** ou dados técnicos:

| Campo | Onde | Problema |
|---|---|---|
| `tipo` | `excel_data_*_v8.json` (1.261 registos) | sem ele não consigo distinguir Approved, Porsche Center e independente, que entram na pontuação |
| `vendedor` / `grupo` | excel e `anuncios.json` | o nome do stand é informação comercial pública |
| `id` / `id_v7` | 29 registos (por exemplo, `BE-[vendedor omitido]-319c135c`) | o código deixa de ligar ao carro que já está no site |
| `chave` | `as24:f4b2df1a-[contacto omitido]-a7cf48b613e1` | o UUID da AutoScout24 ficou cortado |
| `meta.data`, `garantia_fabrica_ate` e o título do `RESUMO` | alerta e resumo | datas confundidas com números de telefone |

**O que pedimos:**
- Ocultar **só** os dados de pessoas: nomes de vendedores particulares, nomes de funcionários, telefones e emails pessoais, moradas de particulares.
- **Não** ocultar:
  - nomes de stands e concessionários;
  - o `tipo` de vendedor;
  - códigos e ids de anúncios e UUIDs;
  - datas e números de garantia;
  - telefones gerais dos stands. Estes podem ficar de fora, mas não podem cortar outros campos.

## 2. Carros novos do alerta sem registo para pontuar
Os 31 `novos` de `alerta_2026-11-06.json` (por exemplo, o Finder `7N4737`, Taycan 4 berlina de Lanester, 03/2025, 109.900 €, com InnoDrive, 4+1 e eixo traseiro) **não vêm no `excel_data_*_v8.json`**. Assim não os consigo pontuar.

**O que pedimos:** incluir cada carro novo no `excel_data` com o registo completo:
- `justo_v7`, `posto_v7`, `pen_v7`, `verd_v7`, `os`;
- `eq`, `opts`, `novo_origem`;
- `primeira_matricula_exata`.

Ou seja, como na entrega de 03/11 (`registo_v7`).

## 3. Estado `reservado` antigo na base
No `anuncios.json`, o NK804N (Lüneburg) continuava `reservado` com o motivo de 03/11, quando a ficha de 04/11 já o mostrava livre.

**O que pedimos:** quando uma reserva cai, atualizar também o `estado` na base (`db/anuncios.json`), e não só no `finder_estado`.

Já ajustei o meu importador para usar a data do motivo, mas convém a base estar certa.
