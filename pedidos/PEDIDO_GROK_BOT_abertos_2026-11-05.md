# Pedido ao Grok Bot — o que continua em aberto (05/11/2026)

Substitui o pedido de 03/11, que já foi respondido e integrado (obrigado). Aqui fica só o que falta, por ordem de prioridade.

## 0. Regras (iguais)
- Só leitura pública. Nunca contactar vendedores, preencher formulários ou pedir dados por email ou chat em nome do Pedro.
- Não contornar anti-bot. Proibido usar proxy, mudar o user-agent ou usar o PC do Pedro. Se bloquear, marcar `sem_leitura`.
- Pausas de 20–30 s; um site de cada vez.
- Segredos só pelo COFRE; sem dados pessoais de particulares.
- O Grok não pontua nem dá veredictos; o v8 é do Claude Code.
- Estados: só a **ficha** diz `ativo`, `reservado` ou `vendido`. Um carro visto só na lista é `na_lista`.

## 1. As 7 berlinas ★ (prioridade máxima)
São as que cumprem tudo o que o Pedro prefere: berlina, InnoDrive, 4+1, eixo traseiro direcional, PCM novo e estacionamento assistido.

| # | Código | Carro | Onde |
|---|---|---|---|
| 1 | `L68W39` | 4S 02/2026 | PZ Bielefeld |
| 2 | `M4EGLE` | 4S 03/2026 | PZ Wettenberg |
| 3 | `08NZ42` | 4 Black Edition 08/2026 | PZ Trier |
| 4 | AS24 `f7cafc67` | 4 05/2026, Preto Jet | Kaarst (Düsseldorf) |
| 5 | `7N04NW` | GTS 07/2026 | PZ Bonn |
| 6 | `20P2V5` | 4 07/2026 | PZ Bonn |
| 7 | `EXDW85` | 4S 08/2026 ("Verfügbar ab 4.11.2026") | PZ Bergisch Gladbach |

Para cada um, devolver:
- **Estado e preço lidos na ficha, todos os dias.**
- **VIN completo**, se aparecer em qualquer lado: ficha, fotos (OCR do para-brisas ou do pilar B), PDF ou descrição. Na 03/11 só o M73KGO e o 24D5M5 tinham VIN.
  - Serve para confirmar o ano-modelo pela 10.ª posição (T = MY2026, V = MY2027).
- **SoH da bateria** (`sohPercentage` ou certificado nas fotos). Nenhum dos 7 o tem.
- **Galeria:**
  - **L68W39:** as fotos continuam a ser do configurador? Avisar se aparecerem fotos reais.
  - **Todos:** número de fotos e se há imagens novas desde 03/11.
- **"Verfügbar ab"** e descidas de preço (com a data).

**Caso especial: AS24 `f7cafc67` (Kaarst).** Ainda não tem ficha completa. Preciso:
- de saber se o vendedor é um stand (empresa) e que garantia dá;
- da **1.ª matrícula com dia exato**: estimámos 31/05/2026, e a regra dos 6 meses depende disso;
- de confirmar InnoDrive (P4S), 4+1 (5KA), eixo traseiro direcional (0N5), ângulo morto (7Y8), Surround View (FT3) ou Remote ParkAssist (FT1), e se o carro tem acidentes;
- do **registo completo no formato excel v7** (`justo_v7`, `pen_v7`, `os`, `eq`, `opts`, `novo_origem` e `posto_v7`, pelo `build_excel_v8.py`), como fizeram com o Diez.

## 2. Anúncios AutoScout24 com dúvidas por fechar (prioridade alta)
- **Diez `68f10d6f`** (Black Edition berlina 08/2026, 99.900 €, Bach Sportwagen):
  - A AS24 diz **4 lugares** e o InnoDrive "não indicado". Procurar 5KA e P4S na descrição completa e nas fotos (por exemplo, o banco traseiro do meio ou o ecrã do InnoDrive).
  - Confirmar o estado e o preço de hoje.
  - Ver se a garantia aparece agora em algum lado (a 03/11 dizia `warrantyExists: false`).

## 3. Vigilância diária (continua)
- **Formato:** `finder_estado_<data>.json`, lido na ficha, para todos os Excelente e Bom disponíveis e reservados.
- **Reservados a acompanhar:**

  | Código | Onde |
  |---|---|
  | `WZVRQM` | Leipzig ("Verfügbar ab 31.12.2026") |
  | `ON3PM9` | Essen |
  | `NKOZ7L` | Hamburg |
  | `KP920D` | Hamburg |
  | `M27W88` | München |

  Devolver `nota: "reserva caiu"` quando o selo desaparecer.
- **Reservas que caíram a 05/11** (confirmar que continuam livres):
  - `3K674M` Soest;
  - `4W3QKZ` Willich;
  - `D4NK4K` Braunschweig;
  - `EKKZQ5` Göttingen.
- **Vendidos que reaparecem com outro código:** comparar com os vendidos recentes. A lista anterior continua a valer, mais:
  - `K5KV2X` Berlin, vendido a 05/11;
  - `4GE07Q`/`L6RX2N` Bonn.
- **Descidas de preço:** em qualquer berlina facelift com InnoDrive, mesmo acima de 115.000 €. Prioridade às que tenham 0N5, 7Y8 e FT3 ou FT1.

## 4. Dúvidas antigas que ainda ficam (prioridade média)
| Código | O que confirmar |
|---|---|
| `V3MP6K` (Amsterdam, berlina) | Estado de acidentes. A descrição está vazia; ver as fotos (OCR) à procura de "schadevrij", "ongevalvrij" ou de um relatório de danos |
| `T60K3YK2` (Turbo, FR) | Ficha completa no formato `carros`, com `registo_v7` |
| `MEQJ9XWM` (4S, BG) | Ficha completa no formato `carros`, com `registo_v7` |

## 5. Fonte nova (prioridade baixa)
- **willhaben.at:** berlinas Taycan facelift (1.ª matrícula a partir de 03/2024), só de stands, com InnoDrive e 4+1.
  - Se a página tiver anti-bot ou pedir login, marcar `sem_leitura` e parar.
  - Devolver no formato `carros`.

## 6. Entrega
- Um zip por lote, com um `LEIA-ME.md` curto.
- Ficheiros:
  - `fichas_berlinas_<data>.json` para as secções 1, 2 e 4;
  - `finder_estado_<data>.json` para a secção 3;
  - `willhaben_<data>.json` para a secção 5.
- Sem páginas em bruto com dados pessoais.
