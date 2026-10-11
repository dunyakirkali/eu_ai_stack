# ETF coverage of the European AI stack

Which few ETFs hold the most of the 451 companies in [`companies.json`](companies.json)? Holdings are the iShares CSV files dated 8 Oct 2026, matched to our companies by name. This is research, not investment advice.

## Answer

**Two ETFs hold 98 of the 99 listed companies we could match. Three hold all 99.**

| ETFs | Companies held | Share of the listed ones |
|---|---|---|
| EXSA | 72 | 73% |
| ESCE + IWDA | 98 | 99% |
| ESCE + EXSA + IWDA | 99 | 100% |

- **IWDA** supplies the large caps and the European companies that list in the US (Nebius, Spotify, NXP, Linde).
- **ESCE** supplies the European small and mid caps that the large-cap funds skip (Siltronic, Wacker, SUSS, Jenoptik, Renishaw, Elmos, X-FAB, ams OSRAM, Melexis and others). 22 companies are held by no other fund we checked.
- **EXSA** adds only KGHM Polska Miedz on top of those two. On its own it holds 72 of the 99, which makes it the best single fund.

## The ETFs we checked

| Ticker | Fund | ISIN | TER | Equity holdings | Our companies in it | Their share of the fund |
|---|---|---|---|---|---|---|
| IWDA | iShares Core MSCI World UCITS ETF (Acc) | IE00B4L5Y983 | 0.20% | 1249 | 58 | 4.4% |
| ESCE | iShares MSCI Europe Small Cap UCITS ETF (Acc) | IE0000N55FP4 | 0.25% | 832 | 41 | 7.7% |
| EXSA | iShares STOXX Europe 600 UCITS ETF (DE) | DE0002635307 | n/a | 602 | 72 | 25.8% |
| EXSM | iShares EURO STOXX Small UCITS ETF | n/a | n/a | 87 | 10 | 14.4% |
| EXV3 | iShares STOXX Europe 600 Technology UCITS ETF (DE) | DE000A0H08Q4 | 0.46% | 35 | 14 | 72.9% |
| EXH4 | iShares STOXX Europe 600 Industrial Goods & Services UCITS ETF (DE) | DE000A0H08J9 | 0.46% | 104 | 13 | 38.5% |
| EXH9 | iShares STOXX Europe 600 Utilities UCITS ETF (DE) | DE000A0Q4R02 | 0.46% | 29 | 11 | 78.1% |

The last column matters. Holding a company is not the same as having exposure to it. Our companies are only **about 4% of IWDA** and **about 8% of ESCE**, so buying either for this theme means mostly buying everything else. The sector funds are far more concentrated: our companies are about 78% of the Utilities fund (EXH9) and 73% of the Technology fund (EXV3), but each holds only 11 to 14 of them.

## Caveats

- **ESCE is brand new and tiny.** It launched on 25 March 2026 and had about EUR 9M in net assets on 1 Oct 2026, so it could be thinly traded or closed. A longer-running small-cap fund (for example from SPDR, Amundi or Xtrackers) might be a safer way to get the same coverage. I haven't tested those, and their holdings would need downloading and matching the same way.
- **Only listed companies can be held.** Of the 451 companies, 237 are private, 26 are non-profits and 42 are subsidiaries. Layer L7 (frontier labs) has no listed company at all, and L6 (data and talent) has one. No ETF gives exposure to Mistral, Black Forest Labs or DeepL.
- **Matching was by name and partly by hand.** I reviewed the ambiguous matches and rejected false ones (for example AT&S first matched AT&T, and Hitachi Energy matched its parent Hitachi). A few could still be wrong or missing.
- **Our own data is unverified**, so the list of listed companies is too. Several agent labels were wrong or missing (Infineon, ASML and others had no status).
- **Holdings change.** These are a single snapshot from 8 Oct 2026.

## Coverage by layer

| Layer | Companies in our list | Held by the ETFs above |
|---|---|---|
| L0 · Raw materials | 36 | 18 |
| L1 · Materials processing | 51 | 14 |
| L2 · Machine subsystems | 38 | 4 |
| L3 · Chip machines and design tools | 48 | 9 |
| L4 · Chip design and manufacturing | 45 | 9 |
| L5 · Systems and infrastructure | 108 | 37 |
| L6 · Data and talent | 39 | 1 |
| L7 · Frontier labs | 28 | 0 |
| L8 · Delivery and applications | 58 | 7 |

## Listed companies no checked ETF holds

These are listed (or were) but did not appear in any of the seven funds, probably because many are micro caps or list outside the indices these funds track (I did not check each one): Ferroglobe, Nordic Mining, Savannah Resources, Constellium, IQE, REC Silicon, Gooch & Housego, Lumibird, Obducat, Riber, EnSilica, Schweizer Electronic, EDF, Ekinops, Eurotech, Northern Data, ParTec, RWS Holdings, Almawave, LightOn, SOPHiA GENETICS.
EDF was delisted after its 2023 nationalisation. Constellium, Ferroglobe, SOPHiA GENETICS and Northern Data list mainly outside the indices covered here. A micro-cap or country-specific fund would be needed for the rest.

## Who is in which fund

The per-company mapping is in [`etf_coverage.json`](etf_coverage.json).

| Company | Layer | Held by |
|---|---|---|
| AMG Critical Materials | L0 | ESCE |
| Anglo American | L0 | EXSA, IWDA |
| Antofagasta plc | L0 | EXSA, IWDA |
| Aurubis | L0 | ESCE, EXSA, EXSM |
| Boliden | L0 | EXSA, IWDA |
| Elkem | L0 | ESCE |
| Equinor | L0 | EXSA, IWDA |
| Eramet | L0 | ESCE |
| Glencore | L0 | EXSA, IWDA |
| Imerys | L0 | ESCE |
| KGHM Polska Miedz | L0 | EXSA |
| Linde plc | L0 | IWDA |
| Metlen Energy & Metals | L0 | ESCE, EXH9, EXSA, EXSM |
| Norsk Hydro | L0 | EXSA, IWDA |
| Rio Tinto | L0 | EXSA, IWDA |
| TotalEnergies | L0 | EXSA, IWDA |
| Umicore | L0 | ESCE, EXSA |
| Veolia | L0 | EXH9, EXSA, IWDA |
| Air Liquide | L1 | EXSA, IWDA |
| Arkema | L1 | ESCE, EXSA, EXSM |
| AT&S | L1 | ESCE, EXSA, EXSM, EXV3 |
| BASF | L1 | EXSA, IWDA |
| Evonik | L1 | EXSA, EXSM, IWDA |
| Henkel | L1 | IWDA |
| Johnson Matthey | L1 | ESCE, EXSA |
| Merck KGaA | L1 | EXSA, IWDA |
| Siltronic | L1 | ESCE |
| Soitec | L1 | ESCE, EXSA, EXSM, EXV3 |
| SOL Group | L1 | ESCE |
| Solvay | L1 | ESCE |
| Syensqo | L1 | EXSA, IWDA |
| Wacker Chemie | L1 | ESCE |
| COMET Group | L2 | ESCE, EXSA, EXV3 |
| Jenoptik | L2 | ESCE |
| Renishaw | L2 | ESCE |
| VAT Group | L2 | EXH4, EXSA, IWDA |
| Aixtron | L3 | ESCE, EXSA, EXSM, EXV3 |
| ASM International | L3 | EXSA, EXV3, IWDA |
| ASML | L3 | EXSA, EXV3, IWDA |
| BE Semiconductor Industries (Besi) | L3 | EXSA, EXV3, IWDA |
| INFICON | L3 | ESCE, EXH4, EXSA |
| Mycronic | L3 | ESCE, EXSA, EXV3 |
| Oxford Instruments | L3 | ESCE |
| PVA TePla | L3 | ESCE |
| SUSS MicroTec | L3 | ESCE |
| ams OSRAM | L4 | ESCE |
| Elmos Semiconductor | L4 | ESCE |
| Infineon | L4 | EXSA, EXV3, IWDA |
| Melexis | L4 | ESCE |
| Nordic Semiconductor | L4 | ESCE, EXSA, EXV3 |
| NXP | L4 | IWDA |
| Sivers Semiconductors | L4 | ESCE |
| STMicroelectronics | L4 | EXSA, EXV3, IWDA |
| X-FAB Silicon Foundries | L4 | ESCE |
| ABB | L5 | EXH4, EXSA, IWDA |
| ACS Group | L5 | EXSA, IWDA |
| Alfa Laval | L5 | EXH4, EXSA, IWDA |
| Bouygues | L5 | EXSA, IWDA |
| Deutsche Telekom (T-Systems) | L5 | EXSA, IWDA |
| E.ON | L5 | EXH9, EXSA, IWDA |
| Enel | L5 | EXH9, EXSA, IWDA |
| ENGIE | L5 | EXH9, EXSA, IWDA |
| Ferrovial | L5 | EXSA, IWDA |
| Fortum | L5 | EXH9, EXSA, IWDA |
| HUBER+SUHNER | L5 | ESCE, EXSA |
| Iberdrola | L5 | EXH9, EXSA, IWDA |
| IONOS | L5 | ESCE |
| Legrand | L5 | EXH4, EXSA, IWDA |
| Merlin Properties | L5 | ESCE, EXSA |
| Munters | L5 | ESCE |
| National Grid | L5 | EXH9, EXSA, IWDA |
| Nebius | L5 | IWDA |
| Nexans | L5 | ESCE, EXH4, EXSA |
| NKT | L5 | ESCE, EXH4, EXSA |
| Nokia | L5 | EXSA, IWDA |
| Nordex | L5 | ESCE, EXSA, EXSM |
| Orsted | L5 | EXH9, EXSA, IWDA |
| OVHcloud | L5 | ESCE |
| Prysmian | L5 | EXH4, EXSA, IWDA |
| Rolls-Royce (mtu power systems) | L5 | EXH4, EXSA, IWDA |
| Royal BAM Group | L5 | ESCE, EXSA, EXSM |
| RWE | L5 | EXH9, EXSA, IWDA |
| Schneider Electric | L5 | EXH4, EXSA, IWDA |
| Siemens Energy | L5 | EXSA, IWDA |
| Skanska | L5 | EXSA, IWDA |
| SSE | L5 | EXH9, EXSA, IWDA |
| Swisscom | L5 | EXSA, IWDA |
| Telenor | L5 | EXSA, IWDA |
| Vestas | L5 | EXSA, IWDA |
| Vinci | L5 | EXSA, IWDA |
| Waertsilae | L5 | EXH4, EXSA, IWDA |
| Teleperformance | L6 | ESCE, EXH4, EXSA, EXSM |
| Capgemini | L8 | EXSA, EXV3, IWDA |
| Dassault Systemes | L8 | EXSA, EXV3, IWDA |
| Klarna | L8 | ESCE |
| Philips | L8 | EXSA, IWDA |
| SAP | L8 | EXSA, EXV3, IWDA |
| Siemens | L8 | EXH4, EXSA, IWDA |
| Spotify | L8 | IWDA |
