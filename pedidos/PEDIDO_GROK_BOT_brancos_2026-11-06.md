# Pedido ao Grok Bot: passar a recolher os Taycan brancos (06/11/2026)

## Regra nova do Pedro
Os carros **brancos** deixam de estar excluídos. Em Portugal, um wrap noutra cor custa cerca de **4.000 €**. Por isso:
- um branco entra no dossier **só se, somando 4.000 € ao "posto em PT", continuar a ser Bom ou Excelente** no v8;
- a pontuação é feita pelo Claude Code. O Grok **só recolhe**.

Chalk/Kreide (cinzento-giz) continua a ser tratado como **não branco**, como até aqui.

## O que muda na recolha
1. **Recolher os brancos** em todas as fontes e pesquisas habituais:
   - Porsche Finder, AutoScout24, Autotrack, viaBOVAG, Blocket/Wayke, sauto.cz e as outras;
   - cores como Weiß, Carraraweiß, Carrara White, Blanc, Bianco, Blanco, Wit, Biały, Bílá.
2. **Não aplicar** o filtro "branco" que hoje os exclui (o `motivo_fora_filtros: branco`). Todos os outros filtros continuam: 4+1, facelift (a partir de 03/2024), só stands, sem acidentes graves, InnoDrive, e o resto.
3. **No `excel_data_*_v8.json`:** incluir os brancos com o registo completo, como os outros carros:
   - `justo_v7`, `posto_v7`, `pen_v7`, `verd_v7`, `os`;
   - `eq`, `opts`, `novo_origem`;
   - `primeira_matricula_exata`.
4. **Campo `cor`:** escrever a cor exata do anúncio (por exemplo, "Carraraweiß metallic"). É por esse campo que o Claude Code os identifica.
5. **Prioridade:** berlinas brancas com InnoDrive e 4+1, de preferência com:
   - eixo traseiro direcional (0N5);
   - PCM novo (MY2026+);
   - aviso de ângulo morto (7Y8);
   - Surround View (FT3) ou Remote ParkAssist (FT1).

## Do lado do Claude Code (já feito)
- No `add_novos.py`, o "posto em PT" de cada branco passa a incluir +4.000 € de wrap.
- Um branco só entra no site se, com esse custo, ficar **Bom ou Excelente**.
- Na cor aparece "branco: posto inclui wrap 4000 €".
