# Pedido ao Grok Bot: pré-teste de negociação com vendedores (06/11/2026)

O Pedro aprovou a estratégia. Antes de abordar os carros que lhe interessam mais, vamos testar a conversa com os vendedores, começando pelos carros classificados **Caro** e passando depois aos **Justo**. Queremos perceber:
- se negoceiam e quanto descem;
- o que oferecem em vez de desconto;
- como tratam a venda a um particular de Portugal.

O Grok gere esta parte com o Pedro, porque é o mais interativo com ele. O Claude Code integra as respostas no dossier: a coluna "Negociação", as notas de cada carro e a pontuação.

## 0. Regras (obrigatórias)
- **Nenhuma mensagem sai sem o "ok" explícito do Pedro, mensagem a mensagem.** O Grok redige e mostra ao Pedro. Ou o Pedro envia ele próprio, ou o Grok envia só depois desse "ok". Nunca enviar nada em nome do Pedro por iniciativa própria.
- **Verdade sempre:**
  - Não inventar propostas da concorrência. Só se podem citar anúncios reais e públicos (com o link), e só se o Pedro aprovar.
  - Não prometer compra nem datas que o Pedro não confirmou.
- **Sem dinheiro:** nada de sinais, reservas pagas, transferências ou assinaturas. Isso é decidido só pelo Pedro, caso a caso. Avisar o Pedro de imediato se alguém pedir pagamento antecipado ou dados bancários, porque pode ser burla, sobretudo num vendedor independente.
- **Dados pessoais:** usar só o nome e o contacto que o Pedro indicar. Nada de NIF, morada, documentos ou IBAN.
- **Segredos e logins** (email, portais) só pelo COFRE, como sempre.
- **Não contornar anti-bot.** Proibido usar proxies ou o PC do Pedro para isso.
- **Uma conversa por stand.** Se o mesmo stand tiver dois carros da lista, perguntar pelos dois na mesma mensagem e manter a mesma história.
- **O Grok não dá veredictos v8.** Devolve factos e citações exatas das respostas.

## 1. Primeiro: pesquisa extensa (antes de qualquer mensagem)
Procurar relatos de quem já comprou Porsche (de preferência Taycan, ou elétricos premium) usados em concessionários alemães a partir do estrangeiro, sobretudo de Portugal ou Espanha. Queremos saber o que resultou e o que não resultou.

**Fontes sugeridas:**
- **Fóruns:**
  - Rennlist (Taycan);
  - taycanforum.com;
  - PFF.de (Porsche Fan Forum);
  - motor-talk.de;
  - Reddit (r/Taycan, r/Porsche, r/germany, r/portugal);
  - autopt.com / Fórum Autohoje.
- **Experiências de importação:**
  - grupos de importação PT (fóruns, blogues e vídeos de importadores);
  - ForoCoches e Forocoches/Motor (ES).

Se uma fonte tiver anti-bot ou pedir login, marcar `sem_leitura` e passar à seguinte.

**Perguntas a responder** (com fonte e data de cada afirmação):
1. **Margem de desconto.** Quanto descem normalmente os Porsche Zentren em usados, Approved e "Junge Gebrauchte"? E os vendedores independentes? O que muda em novembro e dezembro, com os objetivos de fim de ano (Jahresendgeschäft)?
2. **Contrapartidas em vez de desconto:**
   - rodas de inverno;
   - prolongar a Approved;
   - cabo ou carregador;
   - Überführung ou Zulassung incluídas;
   - pneus novos;
   - revisão feita.

   O que costuma ser aceite?
3. **Canal e tom.** Email, telefone ou formulário do Finder? Alemão ou inglês? Mensagem curta ou detalhada? Mencionar a data da visita ajuda ou prejudica?
4. **Tempo do anúncio.** Os carros há muito tempo à venda descem mais? Há relatos com números?
5. **Venda a particular de outro país da UE:**
   - Há Porsche Zentren que se recusam ou exigem condições?
   - Matrícula de transporte: Kurzzeitkennzeichen ou Überführungskennzeichen.
   - Documentos: Zulassungsbescheinigung Teil I/II e COC.
   - Garantia Approved em Portugal.
6. **IVA:**
   - "Novo meio de transporte" (até 6 meses ou até 6.000 km): IVA pago em PT e fatura sem IVA alemão. Que provas pedem (Gelangensbestätigung)?
   - Usados: IVA alemão incluído, sem dedução.
7. **Erros a evitar:**
   - pedir desconto antes de ver o carro;
   - dizer o orçamento;
   - viajar sem uma proposta escrita.
8. **Pedir proposta vinculativa por escrito.** Como pedir um "verbindliches Angebot" antes de viajar, e se os stands o costumam dar.

**Entrega da pesquisa:** `pesquisa_negociacao_<data>.md`, com um resumo de 1 página e os detalhes por pergunta, com links. Só depois de o Pedro e o Claude Code lerem é que se passa à secção 2.

## 2. Carros do pré-teste
Dados do dossier a 06/11: preço do anúncio, posto em PT, veredicto v8 e dias à venda. Antes de escrever a cada stand, confirmar na ficha que o carro continua **ativo**. Se estiver reservado ou vendido, saltar.

### Fase 1: Caro (para calibrar). Começar por aqui.
| Código | Carro | Stand | Preço | Posto PT | v8 | Dias à venda | Ficha |
|---|---|---|---|---|---|---|---|
| `454OWZ` | 4 01/2026, 16.900 km | PZ Hannover (Approved) | 116.990 € | 118.290 € | Caro 58 | até 294 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-454OWZ |
| `56750V` | 4S 04/2026, 15.900 km | PZ Braunschweig | 127.930 € | 129.230 € | Caro 68 | até 188 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-gebraucht-56750V |
| `4560KQ` | 4 06/2026, 4.990 km | PZ Siegen | 125.500 € | 131.018 € | Caro 57 | até 140 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-4560KQ |
| `PLGE5G` | 4S 07/2026, 18.900 km | PZ Reutlingen (Approved) | 125.450 € | 130.966 € | Caro 62 | até 125 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-black-edition-gebraucht-PLGE5G |
| `PV0N2R` | 4S 10/2026, 9.900 km | PZ Magdeburg | 131.000 € | 136.703 € | Caro 66 | até 13 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-black-edition-gebraucht-PV0N2R |

**Notas:**
- **`454OWZ`:** o PZ Hannover também tem `NQV3RV` e `6476R5`, que o Pedro pode querer mais tarde. Usar a mesma história e não queimar o stand: tom cordial e sem ultimatos.
- **`56750V`:**
  - É Frozen Berry (rosa); a cor pode não agradar ao Pedro, mas serve para testar.
  - Com a 1.ª matrícula a 30/04/2026, a entrega em dezembro já é como usado, com IVA alemão.
- **`PV0N2R`:** o anúncio é recente. Serve para comparar com os antigos: os novos descem menos?

### Fase 2: Justo (só depois de a fase 1 ter respostas e o guião estar afinado)
| Código | Carro | Stand | Preço | Posto PT | v8 | Ficha |
|---|---|---|---|---|---|---|
| `7N04NW` + `20P2V5` | GTS 07/2026 e 4 07/2026 | PZ Bonn (o mesmo stand: **uma só mensagem**) | 137.950 € e 103.950 € | 143.887 € e 108.744 € | Justo 73 e 72 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-gts-gebraucht-7N04NW · https://finder.porsche.com/de/de-DE/details/porsche-taycan-4-black-edition-gebraucht-20P2V5 |
| `EXDW85` | 4S 08/2026 ("Verfügbar ab 4.11.2026") | PZ Bergisch Gladbach | 128.900 € | 134.533 € | Justo 69 | https://finder.porsche.com/de/de-DE/details/porsche-taycan-4s-black-edition-gebraucht-EXDW85 |
| AS24 `f7cafc67` | 4 05/2026, 23.123 km | independente, Kaarst | 98.990 € | 100.290 € | Justo 74 | https://www.autoscout24.com/offers/porsche-taycan-4-black-edition-pano-hud-hal-softclose-18w-electric-black-cat_ma57mo75273-f7cafc67-4bba-4004-bc95-60d24aea793b |

**Nota sobre o Kaarst:** é um vendedor independente, por isso o cuidado com pagamentos é redobrado. Perguntar também:
- a data exata da 1.ª matrícula;
- a garantia;
- o InnoDrive e os 4+1.

### Fase 3: os melhores. NÃO contactar sem ordem expressa do Pedro.
- `L68W39` (Bielefeld, Excelente 90);
- `M4EGLE` (Wettenberg, Bom 79).

Ficam para o fim, com o guião já testado.

## 3. A mensagem: base a adaptar com a pesquisa
**Linhas gerais:**
- em alemão, curta e cordial;
- o Pedro é de Portugal e pensa visitar o stand **no fim de novembro ou início de dezembro**, para eventualmente fechar negócio e levar o carro;
- **não dizer o orçamento.**

**Perguntas a incluir:**
1. Se o carro continua disponível.
2. Se vendem a um particular de Portugal e como tratam a matrícula de transporte e os documentos.
3. O VIN, a versão do PCM e o ano-modelo, o certificado de SoH da bateria, se o carro tem acidentes ("unfallfrei?"), o histórico de manutenção e as campanhas ou recalls feitos.
4. A garantia Approved: até quando vale e se vale em Portugal.
5. O **melhor preço final** para um negócio em dezembro, ou o que podem incluir: rodas de inverno, prolongar a Approved, Überführung.
6. Se podem enviar uma **proposta por escrito** (verbindliches Angebot) antes da viagem.

**Rascunho base** (o Grok melhora-o com o que a pesquisa disser e mostra a versão final ao Pedro):

> Sehr geehrte Damen und Herren,
>
> ich interessiere mich für Ihren Porsche Taycan [Version], Fahrzeugnummer [Code] ([Link]). Ich wohne in Portugal und plane, Ende November / Anfang Dezember zu Ihnen zu kommen, um das Fahrzeug anzusehen und es bei Einigung direkt mitzunehmen.
>
> Vorab hätte ich einige Fragen:
> 1. Ist das Fahrzeug noch verfügbar?
> 2. Verkaufen Sie an Privatkunden aus Portugal, und wie läuft die Überführung (Kurzzeit-/Überführungskennzeichen, Unterlagen)?
> 3. Könnten Sie mir die FIN, die PCM-Version/das Modelljahr sowie, falls vorhanden, ein Batterie-Zertifikat (SoH) nennen? Ist das Fahrzeug unfallfrei, und wurden alle Rückrufe/Kampagnen durchgeführt?
> 4. Bis wann läuft die Porsche Approved Garantie, und gilt sie auch in Portugal?
> 5. Was wäre Ihr bester Endpreis bei einem Abschluss im Dezember, bzw. welche Leistungen (z. B. Winterräder, Approved-Verlängerung, Überführung) könnten Sie einschließen?
> 6. Wäre ein verbindliches schriftliches Angebot vor meiner Anreise möglich?
>
> Vielen Dank und freundliche Grüße
> [Nome do Pedro]

## 4. Acompanhamento
- **Ritmo:** 2 a 3 stands por dia, para comparar respostas e afinar o texto.
- **Insistência:** se não houver resposta em 3 dias úteis, um lembrete curto, e só com o "ok" do Pedro.
- **Respostas:** mostrar cada resposta ao Pedro com tradução e uma sugestão de resposta. Também esta sai só com o "ok" dele.
- **Chamadas telefónicas:** se o stand quiser falar ao telefone, o Grok prepara um guião em português e alemão para o Pedro.

## 5. Entrega ao Claude Code
Um zip por lote, com um `LEIA-ME.md` curto e os ficheiros:
- `pesquisa_negociacao_<data>.md` (secção 1);
- `negociacao_<data>.json`, uma entrada por contacto, com os campos:
  - `codigo`, `stand`, `canal` e `data_envio`;
  - `mensagem_enviada` (texto exato);
  - `data_resposta` e `resposta` (texto exato, sem dados pessoais do vendedor além do nome do stand);
  - `disponivel`;
  - `vende_particular_estrangeiro`;
  - `preco_final_oferecido` e `desconto_pct`;
  - `extras_oferecidos` (lista);
  - `proposta_escrita` (sim, não ou pendente);
  - `vin`, `pcm_my`, `soh` e `unfallfrei`;
  - `approved_ate` e `approved_em_PT`;
  - `transporte_docs`;
  - `notas`.
- Não incluir emails nem telefones de pessoas. Basta o nome do stand.

O Claude Code usa isto para:
- calibrar a coluna "Negociação" (descontos reais vs. a estimativa de 0–8 %);
- atualizar os dados de cada carro (VIN, SoH, PCM);
- decidir com o Pedro quando avançar para a fase 3.
