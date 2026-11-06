# Pedido ao Grok Bot: negociação, fase 1 (luz verde, 06/11/2026)

O Pedro e o Claude Code leram a pesquisa (`pesquisa_negociacao_2026-11-06.md`). Obrigado, está muito útil.

**O Pedro aprovou a fase 1.** Continuam a valer todas as regras do pedido `PEDIDO_GROK_BOT_negociacao_pre_teste_2026-11-06.md`, e esta é a principal:

> **Nenhuma mensagem sai sem o "ok" explícito do Pedro, mensagem a mensagem.** Nada de pagamentos, sinais, IBAN ou assinaturas.

## 1. Correções ao rascunho, a partir da pesquisa
1. **Matrícula de transporte.** Pedir a **Ausfuhrkennzeichen** (exportação, faixa vermelha) ou que o stand indique um transporte em camião. **Não** propor Kurzzeitkennzeichen: não serve para atravessar França e Espanha.
2. **IVA em carros que em dezembro ainda contam como "novos"** (até 6 meses desde a 1.ª matrícula **ou** até 6.000 km). Perguntar:
   - se faturam sem IVA alemão;
   - se pedem um **depósito do IVA** (Kaution) até receberem a prova de chegada (Gelangensbestätigung ou matrícula PT);
   - em quanto tempo o devolvem.
3. **Desconto ou extras.** Não pedir uma percentagem. Pedir o melhor preço final **ou** o que podem incluir: prolongar a Approved, revisão, matrícula de exportação.
4. **Proposta escrita com prazo.** Pedir um "verbindliches Angebot" com o preço, o que inclui e até quando é válido.
5. **Não dizer o orçamento.**
6. **Expectativa (só para o Grok, não escrever na mensagem):** o habitual nos PZ é cerca de 1.000 € ou mais 1 ano de Approved. Se oferecerem mais do que isso, é sinal de que o stand está flexível.

## 2. Carros da fase 1
Antes de cada mensagem, confirmar na ficha que o carro continua **ativo**.

| Código | Carro | Stand | Preço | Regime em dezembro (entrega a 10/12) | Notas |
|---|---|---|---|---|---|
| `454OWZ` | 4 01/2026, 16.900 km | PZ Hannover | 116.990 € | usado: IVA alemão incluído | Até 294 dias à venda. Ser cordial: o mesmo stand tem `NQV3RV` e `6476R5` |
| `56750V` | 4S 04/2026, 15.900 km | PZ Braunschweig | 127.930 € | usado: IVA alemão incluído | Até 188 dias à venda |
| `4560KQ` | 4 06/2026, 4.990 km | PZ Siegen | 125.500 € | **novo**: menos de 6.000 km | Fazer as perguntas do IVA e do depósito |
| `PLGE5G` | 4S 07/2026, 18.900 km | PZ Reutlingen | 125.450 € | **novo** se a 1.ª matrícula for depois de 10/06/2026: confirmar o dia exato | Fazer as perguntas do IVA e do depósito |
| `PV0N2R` | 4S 10/2026, 9.900 km | PZ Magdeburg | 131.000 € | **novo**: menos de 6 meses | Anúncio recente: serve para comparar com os antigos. Fazer as perguntas do IVA |

**Ritmo:**
- 2 a 3 stands por dia, sempre com o "ok" do Pedro.
- Sugestão de ordem: primeiro `454OWZ` e `56750V`, que estão há mais tempo à venda; depois `4560KQ`, `PLGE5G` e `PV0N2R`.

## 3. Rascunho corrigido (base)
O Grok adapta-o a cada carro e mostra a versão final ao Pedro. A pergunta 5 só entra nos carros "novos" (`4560KQ`, `PLGE5G` e `PV0N2R`).

> Betreff: Anfrage Porsche Taycan [Version], Fahrzeugnummer [Code]
>
> Sehr geehrte Damen und Herren,
>
> ich interessiere mich für Ihren Porsche Taycan [Version] ([Link]). Ich wohne in Portugal und plane, Ende November / Anfang Dezember zu Ihnen zu kommen, um das Fahrzeug zu besichtigen und es bei Einigung direkt zu übernehmen.
>
> Vorab hätte ich folgende Fragen:
> 1. Ist das Fahrzeug noch verfügbar?
> 2. Verkaufen Sie an Privatkunden aus Portugal? Unterstützen Sie bei der Ausfuhr (Ausfuhrkennzeichen) oder können Sie einen Transport nach Portugal vermitteln? Welche Unterlagen erhalte ich (Zulassungsbescheinigung Teil I und II, COC)?
> 3. Können Sie mir die FIN, das Modelljahr bzw. die PCM-Version sowie, falls vorhanden, ein Batteriezertifikat (SoH) nennen? Ist das Fahrzeug unfallfrei, und wurden alle Rückrufe/Kampagnen durchgeführt?
> 4. Bis wann läuft die Porsche Approved Garantie?
> 5. *(nur bei Neufahrzeug im Sinne des UStG)* Da das Fahrzeug bei Übergabe als neues Fahrzeug gilt, würde ich die Mehrwertsteuer in Portugal entrichten. Stellen Sie die Rechnung ohne deutsche MwSt. aus, und verlangen Sie bis zum Nachweis der Verbringung eine Kaution in Höhe der MwSt.? Wie schnell wird sie erstattet?
> 6. Was wäre Ihr bester Endpreis bei einem Abschluss im Dezember, bzw. welche Leistungen könnten Sie einschließen (z. B. Verlängerung der Approved Garantie, Service, Ausfuhrkennzeichen)?
> 7. Wäre ein verbindliches schriftliches Angebot mit Gültigkeitsdatum vor meiner Anreise möglich?
>
> Vielen Dank im Voraus und freundliche Grüße
> [Nome do Pedro]

## 4. Entrega
- **Ficheiro:** `negociacao_<data>.json`, no formato da secção 5 do pedido de pré-teste, com mais estes campos:
  - `iva_regime` e `iva_deposito`;
  - `ausfuhr_kennzeichen` (sim, não ou transporte).
- **Quando:** um zip sempre que houver respostas novas, e um resumo curto ao fim da fase 1.
- **Fase 2:** só depois de o Pedro e o Claude Code revermos as respostas da fase 1.
