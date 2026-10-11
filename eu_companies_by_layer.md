# European companies by layer of the AI stack

451 European companies across the nine layers of [the stack](ai_stack_tech_tree.md). "European" includes the UK, Norway and Switzerland, not only EU members. The country and city are the headquarters.

**Read this first.** The list was compiled by research agents, and most entries come from their own knowledge, not from live sources (agents reported only about 50 live checks in total). Each entry has the agent's confidence rating, which is a judgement, not proof:

- **high** (108): the research agent was confident, and some of these were checked live.
- **medium** (299): believed correct, mostly not checked live.
- **low** (44): uncertain about the headquarters, ownership, whether it still operates, or both. Verify before relying on it.

Ownership and headquarters change often (acquisitions, relocations), so the Note column matters. Source: [`companies.json`](companies.json). Regenerate this file, the map and the GeoJSON with `python3 build.py`.

| Layer | Companies |
|---|---|
| [L0 · Raw materials](#l0--raw-materials) | 36 |
| [L1 · Materials processing](#l1--materials-processing) | 51 |
| [L2 · Machine subsystems](#l2--machine-subsystems) | 38 |
| [L3 · Chip machines and design tools](#l3--chip-machines-and-design-tools) | 48 |
| [L4 · Chip design and manufacturing](#l4--chip-design-and-manufacturing) | 45 |
| [L5 · Systems and infrastructure](#l5--systems-and-infrastructure) | 108 |
| [L6 · Data and talent](#l6--data-and-talent) | 39 |
| [L7 · Frontier labs](#l7--frontier-labs) | 28 |
| [L8 · Delivery and applications](#l8--delivery-and-applications) | 58 |

By country: DE 122, UK 75, FR 69, NL 36, CH 26, SE 25, FI 15, IT 15, ES 13, NO 12, BE 10, AT 8, DK 5, PT 4, LU 3, IE 3, PL 1, GR 1, SI 1, EE 1, LT 1, HU 1, IS 1, LV 1, CZ 1, UA 1

## L0 · Raw materials

| Company | Country | City | Role | Confidence | Note |
|---|---|---|---|---|---|
| [Aluminium Dunkerque](https://www.aluminiumdunkerque.com) | FR | Dunkirk | Primary aluminium smelter | medium | Owned by GFG Alliance (Liberty) |
| [AMG Critical Materials](https://www.amg-nv.com) | NL | Amsterdam | Lithium, vanadium, graphite, critical metals | high |  |
| [Anglo American](https://www.angloamerican.com) | UK | London | Copper and diversified mining | high |  |
| [Antofagasta plc](https://www.antofagasta.co.uk) | UK | London | Copper mining (Chile) | high | Mines are in Chile; HQ London |
| Aurubis | DE | Hamburg | Copper smelting and recycling | medium |  |
| Boliden | SE | Stockholm | Copper, zinc and other metals | medium |  |
| [Cornish Lithium](https://cornishlithium.com) | UK | Truro | Lithium from geothermal brine and hard rock | medium | Pre-production |
| [Elkem](https://www.elkem.com) | NO | Oslo | Silicon metal and quartz-based silicon materials | high | Majority owned by China National Bluestar |
| [Equinor](https://www.equinor.com) | NO | Stavanger | Natural gas and oil supplier | high | State majority |
| [Eramet](https://www.eramet.com) | FR | Paris | Manganese, nickel and lithium mining | high |  |
| [Ferroglobe](https://www.ferroglobe.com) | UK | London | Silicon metal and ferroalloys, quartz | high | Nasdaq-listed; plants in France, Spain, Norway |
| [Glencore](https://www.glencore.com) | CH | Baar | Copper and cobalt mining and trading | high | Jersey-incorporated, operational HQ Baar |
| [Imerys](https://www.imerys.com) | FR | Paris | Industrial minerals, quartz and graphite | high |  |
| [Keliber](https://www.mining-technology.com/news/sibanye-lithium-refinery-finland) | FI | Kokkola | Lithium hydroxide from spodumene | medium | Majority owned by Sibanye-Stillwater, minority Finnish Minerals Group |
| [KGHM Polska Miedz](https://kghm.com) | PL | Lubin | Copper and silver mining and smelting | high | State-controlled |
| [Linde plc](https://www.linde.com) | UK | Woking | Helium, neon and noble gases | low | Registered in Ireland, executive office Woking per company; NYSE-listed; HQ ambiguous |
| LKAB | SE | Luleå | Iron ore, developing a rare-earth deposit | medium |  |
| [Messer](https://www.messergroup.com) | DE | Bad Soden | Helium, neon and rare gases supply | medium |  |
| [Metlen Energy & Metals](https://www.metlen.com/news/press-releases/metlen-signs-landmark-gallium-supply-agreement/) | GR | Athens | Alumina, aluminium and new gallium production | medium | Parent plc registered/listed in London since 2025; operational HQ Athens (sources differ). Gallium plant under construction |
| [Nordic Mining](https://www.nordicmining.com) | NO | Oslo | Rutile and rare earth deposits (Engebo, Fen) | medium | Pre-production |
| [Norsk Hydro](https://www.hydro.com) | NO | Oslo | Aluminium smelting and primary metal | high |  |
| [Nyrstar](https://www.nyrstar.com) | CH | Zurich | Zinc and germanium/gallium by-product metals | medium | Owned by Trafigura; smelters in Belgium, Netherlands, Australia |
| [Orano](https://www.orano.group) | FR | Chatillon | Uranium mining and nuclear fuel cycle | high | State-owned |
| [Quarzwerke](https://www.quarzwerke.com) | DE | Frechen | Quartz sands and silica minerals | medium |  |
| [Rare Earths Norway](https://www.rareearthsnorway.com) | NO | Ulefoss | Fen rare earth deposit developer | medium | Pre-production |
| [Rio Tinto](https://www.riotinto.com) | UK | London | Copper, aluminium and lithium mining | medium | Dual-listed with Australia; plc HQ London |
| [Savannah Resources](https://www.ajbell.co.uk/news/articles/savannah-resources-moves-towards-construction-portugal-lithium-mine) | UK | London | Barroso lithium project, Portugal | medium | Pre-production; FID expected 2027 |
| Sibelco | BE | Antwerp | High-purity quartz and silica | medium |  |
| [Suez](https://www.suez.com) | FR | Paris | Ultra-pure water and water treatment | medium | Owned by Veolia, Meridiam and others since 2022 |
| [Terrafame](https://www.terrafame.com) | FI | Sotkamo | Nickel and cobalt sulphate for batteries | medium | State-owned (Finnish Minerals Group majority) |
| [TotalEnergies](https://totalenergies.com) | FR | Courbevoie | Oil, gas and LNG supply | high |  |
| [Trimet Aluminium](https://www.trimet.eu) | DE | Essen | Primary aluminium smelting | medium |  |
| Umicore | BE | Brussels | Metals recycling, germanium, speciality materials | medium |  |
| [Urenco](https://www.urenco.com) | UK | Stoke Poges | Uranium enrichment for nuclear fuel | high | Owned by UK, Dutch governments and German utilities |
| [Veolia](https://www.veolia.com) | FR | Paris | Ultra-pure water systems for fabs | medium | Veolia Water Technologies unit |
| [Wolfram Bergbau und Huetten](https://www.wolfram.at) | AT | St. Martin im Sulmtal | Tungsten mining and processing | medium | Owned by Sandvik (Sweden) |

## L1 · Materials processing

| Company | Country | City | Role | Confidence | Note |
|---|---|---|---|---|---|
| Air Liquide | FR | Paris | Industrial and electronic gases | medium |  |
| [Allresist](https://www.allresist.com) | DE | Strausberg | Photoresists and e-beam resists | medium |  |
| [Arkema](https://www.arkema.com) | FR | Colombes | Specialty chemicals and electronic materials | high |  |
| [AT&S](https://www.ats.net) | AT | Leoben | IC substrates and advanced PCBs | high |  |
| [Atotech](https://www.atotech.com) | DE | Berlin | Plating chemistry for chip packages and PCBs | medium | Owned by MKS Instruments (US) |
| [BASF](https://www.basf.com) | DE | Ludwigshafen | Electronic chemicals and battery materials | high |  |
| [Carester (Caremag)](https://fastmarkets.com/insights/caremag-raises-216-million-to-build-rare-earths-plant-in-france) | FR | Lyon | Rare earth refining and magnet recycling, Lacq | medium | Plant under construction, start-up targeted end 2026 |
| [Ceratizit](https://www.ceratizit.com) | LU | Mamer | Tungsten carbide hard materials | medium |  |
| [Constellium](https://www.constellium.com) | FR | Paris | Rolled and extruded aluminium products | medium | NYSE-listed, Dutch-incorporated |
| [DELO Industrial Adhesives](https://www.delo-adhesives.com) | DE | Windach | Adhesives for semiconductor packaging | medium |  |
| [Evonik](https://www.evonik.com) | DE | Essen | Silanes, specialty chemicals for semiconductors | high |  |
| [Freiberger Compound Materials](https://www.freiberger.com) | DE | Freiberg | GaAs and compound semiconductor substrates | medium |  |
| [H.C. Starck Solutions](https://www.hcstarck.com) | DE | Munich | Tungsten and refractory metal powders | low | Owned by Masan High-Tech Materials; verify current name |
| [Henkel](https://www.henkel.com) | DE | Duesseldorf | Semiconductor packaging adhesives and materials | high |  |
| [Heraeus](https://www.heraeus.com) | DE | Hanau | Quartz glass, precious metals, bonding wire | high |  |
| [HyProMag](https://source.benchmarkminerals.com/article/site-visit-hypromag-opens-uks-first-rare-earth-magnet-recycling-facility) | UK | Birmingham | Magnet-to-magnet recycling (Tyseley) | medium | Owned by Mkango/CoTec via Maginito |
| [IQE](https://www.iqep.com) | UK | Cardiff | Compound semiconductor epitaxial wafers | high |  |
| [Irresistible Materials](https://www.eenewseurope.com/en/chemistry-startup-claims-euv-resist-breakthrough/) | UK | Birmingham | EUV photoresist developer | medium | University of Birmingham spin-out; small, pre-scale |
| [Johnson Matthey](https://matthey.com) | UK | London | Platinum group metals and chemicals | high |  |
| [JSR Micro NV](https://www.jsrmicro.be/semiconductor) | BE | Leuven | Photoresists produced in Belgium | medium | Owned by JSR Corp (Japan) |
| [KME](https://www.kme.com) | DE | Osnabrueck | Copper and copper-alloy products | medium |  |
| [Less Common Metals](https://www.metal-powder.tech/?p=284480) | UK | Ellesmere Port | Rare earth metals and magnet alloys | medium | Acquisition by USA Rare Earth reported 2025; ownership may now be US |
| [Magneti Ljubljana](https://www.magneti.si) | SI | Ljubljana | Permanent magnets and magnetic systems | medium |  |
| Merck KGaA | DE | Darmstadt | Electronic materials and chemicals | medium |  |
| [Metallo Group](https://www.metallo.com) | BE | Beerse | Copper, tin and e-waste metals recycling | medium |  |
| [Metalor Technologies](https://metalor.com) | CH | Neuchatel | Precious metals, bonding and sputtering materials | medium |  |
| [micro resist technology](https://www.microresist.de) | DE | Berlin | Photoresists for lithography and nanoimprint | medium |  |
| [MicroChemicals](https://www.microchemicals.com) | DE | Ulm | Photoresists and process chemicals | medium |  |
| [Neo Performance Materials Silmet](https://www.neomaterials.com) | EE | Sillamae | Rare earth separation | medium | Parent Neo Performance Materials is Toronto-based |
| [Neorem Magnets](https://www.neorem.fi) | FI | Pori | Sintered NdFeB magnets | low | Ownership and plant status not verified |
| [Nippon Gases Europe](https://www.nippongases.com) | ES | Madrid | Industrial and electronic gases | medium | Owned by Taiyo Nippon Sanso (Japan) |
| [Okmetic](https://www.okmetic.com/about-us/the-history-of-okmetic) | FI | Vantaa | Silicon wafers for sensors and power | high | Owned by NSIG (China) since 2016 |
| [Plansee Group](https://www.plansee.com) | AT | Reutte | Tungsten and molybdenum materials | high |  |
| [REC Silicon](https://www.recsilicon.com) | NO | Lysaker | Polysilicon and silane gas | medium | Main plants in US; owned by Hanwha |
| [REEtec](https://www.scatecinnovation.no/artikler/reetec-raises-nok-1200-million) | NO | Porsgrunn | Rare earth oxide separation (NdPr) | medium | LKAB largest owner; plant ramp-up status unconfirmed |
| [Remondis](https://www.remondis.com) | DE | Luenen | Recycling of electronics and metals | medium |  |
| [ROSI Solar](https://eitrawmaterials.eu/supportedstartups/rosi/) | FR | Grenoble | Silicon and metals recycling from PV | medium | Plant status unverified |
| [SCHOTT](https://www.schott.com) | DE | Mainz | Specialty glass and glass wafers | high | Foundation-owned |
| [SiCrystal](https://www.sicrystal.de) | DE | Nuremberg | Silicon carbide substrates | medium | Owned by ROHM (Japan) |
| Siltronic | DE | Munich | Silicon wafers | medium |  |
| Soitec | FR | Bernin | Engineered substrates (SOI) | medium |  |
| [SOL Group](https://www.solgroup.com) | IT | Monza | Industrial and specialty gases | medium |  |
| [Solvay](https://www.solvay.com) | BE | Brussels | Rare earth separation (La Rochelle), soda ash | high |  |
| [Speira](https://www.speira.com) | DE | Grevenbroich | Aluminium rolling and recycling | medium | Owned by Strategic Equity Capital |
| [Stena Recycling](https://www.stenarecycling.com) | SE | Gothenburg | Electronics scrap and metals recycling | medium |  |
| [SweGaN](https://www.swegan.se) | SE | Linkoping | GaN-on-SiC epitaxial wafers | medium |  |
| [Syensqo](https://www.syensqo.com) | BE | Brussels | Fluoropolymers and electronic specialty chemicals | high | Spun off from Solvay 2023 |
| [Vacuumschmelze](https://www.vacuumschmelze.com) | DE | Hanau | Rare earth permanent magnets | high | Owned by Apollo funds |
| Wacker Chemie | DE | Munich | Polysilicon | medium |  |
| [Westfalen](https://www.westfalen.com) | DE | Muenster | Industrial and specialty gases | medium |  |
| [Wieland-Werke](https://www.wieland.com) | DE | Ulm | Copper alloys for connectors and lead frames | medium |  |

## L2 · Machine subsystems

| Company | Country | City | Role | Confidence | Note |
|---|---|---|---|---|---|
| [attocube systems](https://www.attocube.com) | DE | Munich | Nanopositioners and interferometers | medium | Owned by Bruker (US) |
| [Bronkhorst](https://www.bronkhorst.com) | NL | Ruurlo | Mass flow controllers for process gases | medium |  |
| [Busch Vacuum Solutions](https://www.buschvacuum.com) | DE | Maulburg | Vacuum pumps; owner of Pfeiffer Vacuum | medium | Family-owned; Pfeiffer Vacuum (existing entry) is now a Busch subsidiary |
| [Camfil](https://www.camfil.com) | SE | Stockholm | Cleanroom air filtration | medium |  |
| Carl Zeiss SMT | DE | Oberkochen | Optics for EUV and DUV lithography | medium |  |
| [COMET Group](https://www.comet.tech) | CH | Flamatt | RF generators and matching networks for plasma | high |  |
| [Demcon](https://demcon.com) | NL | Enschede | Mechatronic systems for chip equipment | medium |  |
| [Edwards Vacuum](https://www.edwardsvacuum.com) | UK | Crawley | Dry vacuum pumps, abatement for fabs | high | Owned by Atlas Copco (Sweden) |
| [ETEL](https://www.etel.ch) | CH | Motiers | Direct-drive motors and motion controllers | medium | Part of HEIDENHAIN (Germany) |
| [Excillum](https://www.excillum.com) | SE | Kista | Liquid-metal-jet X-ray sources for metrology | medium |  |
| [Exyte](https://www.exyte.net) | DE | Stuttgart | Cleanroom and semiconductor fab engineering | medium | Owned by Ardian-led investors |
| [Gooch & Housego](https://goochandhousego.com) | UK | Ilminster | Photonic components, acousto-optics | medium |  |
| [HEIDENHAIN](https://www.heidenhain.com) | DE | Traunreut | Optical encoders for wafer stages | medium |  |
| [Hittech Group](https://www.hittech.nl) | NL | Bergschenhoek | Precision frames and modules for chip tools | low |  |
| [Jenoptik](https://www.jenoptik.com) | DE | Jena | Optics and laser modules for lithography | high |  |
| [LASER COMPONENTS](https://www.lasercomponents.com) | DE | Olching | Laser optics and detectors | low |  |
| [LAUDA](https://www.lauda.de) | DE | Lauda-Koenigshofen | Process chillers and thermal control | medium |  |
| [Layertec](https://www.layertec.de) | DE | Mellingen | Precision laser optics and coatings | medium |  |
| [Leybold](https://www.leybold.com) | DE | Cologne | Vacuum pumps and systems | medium | Owned by Atlas Copco (Sweden) |
| [Light Conversion](https://lightcon.com) | LT | Vilnius | Ultrafast lasers | medium |  |
| [Lumibird](https://www.lumibird.com) | FR | Lannion | Solid-state and fibre lasers | medium |  |
| [MI-Partners](https://www.mi-partners.nl) | NL | Eindhoven | Mechatronics development for lithography | medium |  |
| [Micro-Epsilon](https://www.micro-epsilon.com) | DE | Ortenburg | Precision displacement sensors | medium |  |
| [Neways Electronics](https://www.neways.com) | NL | Son | Electronics modules for chip equipment | medium |  |
| [NTS Group](https://www.nts-group.nl) | NL | Eindhoven | Mechatronic modules for ASML and others | medium |  |
| Pfeiffer Vacuum | DE | Aßlar | Vacuum pumps and systems | medium | Owned by Busch |
| [Physik Instrumente (PI)](https://www.pi.ws) | DE | Karlsruhe | Piezo and precision motion stages | medium |  |
| Prodrive Technologies | NL | Eindhoven | Power and control electronics | medium |  |
| [Renishaw](https://www.renishaw.com) | UK | Wotton-under-Edge | Encoders and position metrology | high |  |
| [Settels Savenije](https://www.settels-savenije.nl) | NL | Eindhoven | Cleanroom modules and precision parts | medium |  |
| [Sioux Technologies](https://www.sioux.eu) | NL | Eindhoven | Embedded software and mechatronics for tools | medium |  |
| [SmarAct](https://www.smaract.com) | DE | Oldenburg | Nanopositioning and piezo stages | medium |  |
| [Stäubli](https://www.staubli.com) | CH | Pfaeffikon | Cleanroom robots | low | Robotics division is one of several |
| [TOPTICA Photonics](https://www.toptica.com) | DE | Graefelfing | Diode and ultrafast lasers | medium |  |
| Trumpf | DE | Ditzingen | Lasers, including the EUV light source | medium |  |
| [TRUMPF Hüttinger](https://www.trumpf.com) | DE | Freiburg | RF/plasma power supplies | medium | Part of TRUMPF (existing entry) |
| [VAT Group](https://www.vatvalve.com) | CH | Haag | Vacuum valves for chip equipment | high |  |
| VDL ETG | NL | Eindhoven | Precision modules for chip equipment | medium |  |

## L3 · Chip machines and design tools

| Company | Country | City | Role | Confidence | Note |
|---|---|---|---|---|---|
| Aixtron | DE | Herzogenrath | Compound-semiconductor deposition | medium |  |
| [Alphawave Semi](https://www.qualcomm.com/news/releases/2025/12/qualcomm-completes-acquisition-of-alphawave-semi) | UK | London | High-speed connectivity IP | high | Acquired by Qualcomm (US), completed Dec 2025 |
| [Annealsys](https://annealsys.com) | FR | Montpellier | RTP and CVD equipment | medium |  |
| Arm | UK | Cambridge | Processor IP | medium | Majority-owned by SoftBank |
| ASM International | NL | Almere | Deposition equipment | medium |  |
| ASML | NL | Veldhoven | EUV and DUV lithography | medium |  |
| [BE Semiconductor Industries (Besi)](https://www.besi.com) | NL | Duiven | Hybrid bonding and packaging equipment | high |  |
| [Beneq](https://beneq.com) | FI | Espoo | ALD equipment | medium |  |
| [CEA-Leti](https://www.leti-cea.com) | FR | Grenoble | Chip process R&D and pilot lines | medium | Public research institute |
| [centrotherm international](https://www.centrotherm.de) | DE | Blaubeuren | Thermal processing and furnaces | medium |  |
| [Codasip](https://codasip.com) | DE | Munich | RISC-V cores and design tools | medium | Sale process launched July 2025; outcome unconfirmed |
| [Cortus](https://www.cortus.com) | FR | Montpellier | RISC-V processor IP | low |  |
| [Defacto Technologies](https://www.defactotech.com) | FR | Grenoble | RTL signoff EDA software | medium |  |
| [Dolphin Design](https://www.dolphin-design.fr) | FR | Meylan | Low-power chip IP and design services | medium |  |
| [ERS electronic](https://www.ers-gmbh.com) | DE | Germering | Thermal wafer chucks and probers | medium |  |
| [Eulitha](https://www.eulitha.com) | CH | Villigen | Photonics lithography (PHABLE) | low |  |
| [EV Group](https://www.evgroup.com) | AT | St. Florian am Inn | Wafer bonding and lithography | high |  |
| [Evatec](https://www.evatecnet.com) | CH | Truebbach | Thin-film deposition tools | high |  |
| [ficonTEC](https://www.ficontec.com) | DE | Achim | Photonics assembly and test automation | low | Ownership unverified |
| [Heidelberg Instruments](https://heidelberg-instruments.com) | DE | Heidelberg | Maskless direct-write lithography | medium |  |
| [Imagination Technologies](https://www.imaginationtech.com) | UK | Kings Langley | GPU and AI processor IP | medium | Owned by Canyon Bridge (China-linked) |
| [imec](https://www.imec-int.com) | BE | Leuven | Chip process R&D and pilot lines | high |  |
| [INFICON](https://www.inficon.com) | CH | Bad Ragaz | Gas analysis and process control for fabs | high |  |
| [LayTec](https://www.laytec.de) | DE | Berlin | In-situ epitaxy metrology | low |  |
| [Menta](https://www.menta-efpga.com) | FR | Sophia Antipolis | Embedded FPGA IP | medium |  |
| [Mycronic](https://www.mycronic.com) | SE | Taby | Photomask writers, assembly equipment | high |  |
| [Nearfield Instruments](https://nearfieldinstruments.com) | NL | Rotterdam | Scanning-probe metrology for chips | high | TNO spin-off |
| [Obducat](https://www.obducat.com) | SE | Lund | Nanoimprint lithography | low |  |
| [Openchip & Software Technologies](https://openchip.com) | ES | Barcelona | RISC-V accelerator design | low |  |
| [Oxford Instruments](https://plasma.oxinst.com) | UK | Abingdon | Plasma etch and deposition tools | medium | Plasma business only; other units not chip tools |
| [Picosun](https://www.picosun.com) | FI | Espoo | ALD equipment | medium | Owned by Applied Materials (US) since 2023 |
| [Plassys-Bestek](https://www.plassys.com) | FR | Marolles-en-Hurepoix | MBE and e-beam evaporation | medium |  |
| [PVA TePla](https://www.pvatepla.com) | DE | Wettenberg | Crystal growing, plasma and vacuum systems | high |  |
| [Racyics](https://racyics.com) | DE | Dresden | Mixed-signal chip design house and IP | medium |  |
| [Raith](https://raith.com) | DE | Dortmund | Electron-beam lithography | medium |  |
| [RENA Technologies](https://www.rena.com) | DE | Guetenbach | Wet processing equipment | medium |  |
| [Riber](https://www.riber.com) | FR | Bezons | MBE epitaxy systems | high |  |
| [Rohde & Schwarz](https://www.rohde-schwarz.com) | DE | Munich | RF and chip test and measurement | high |  |
| [Semidynamics](https://semidynamics.com) | ES | Barcelona | RISC-V cores and tensor IP | medium |  |
| [Semilab](https://semilab.com) | HU | Budapest | Semiconductor metrology tools | medium |  |
| [Semsysco](https://www.semsysco.com) | AT | Salzburg | Wet process equipment for packaging | low |  |
| [Sensofar](https://www.sensofar.com) | ES | Terrassa | 3D optical surface metrology | medium |  |
| [SENTECH Instruments](https://www.sentech.com) | DE | Berlin | Plasma etch and ALD tools, ellipsometers | medium |  |
| [Sigasi](https://www.sigasi.com) | BE | Ghent | HDL design environment software | medium |  |
| [SPEA](https://www.spea.com) | IT | Volpiano | Automatic test equipment | medium |  |
| [SPTS Technologies](https://www.spts.com) | UK | Newport | Etch and deposition tools | medium | Owned by KLA (US); operations in Wales |
| [SUSS MicroTec](https://www.suss.com) | DE | Garching | Lithography, bonding and coating tools | high |  |
| [VON ARDENNE](https://www.vonardenne.biz) | DE | Dresden | Vacuum coating systems | medium |  |

## L4 · Chip design and manufacturing

| Company | Country | City | Role | Confidence | Note |
|---|---|---|---|---|---|
| [Ampleon](https://www.ampleon.com) | NL | Nijmegen | RF power transistors (LDMOS, GaN) | medium | Owned by Chinese investors (JAC Capital) |
| [ams OSRAM](https://ams-osram.com) | AT | Premstatten | Optical sensors, emitters and analog ICs | high | SIX Swiss Exchange listed; operational HQ Premstatten, Austria |
| Axelera AI | NL | Eindhoven | AI inference chips | medium |  |
| [Black Semiconductor](https://black-semiconductor.com) | DE | Aachen | Graphene photonics for chip interconnect | medium |  |
| [Cambridge GaN Devices](https://camgandevices.com) | UK | Cambridge | GaN power transistors, fabless | medium |  |
| [CSEM](https://www.csem.ch) | CH | Neuchatel | Ultra-low-power chip and systems R&D | medium |  |
| [Dynex Semiconductor](https://www.dynexsemi.com) | UK | Lincoln | High-power bipolar and IGBT devices, own fab | medium | Owned by CRRC Times Electric (China) |
| [Elmos Semiconductor](https://www.elmos.com) | DE | Dortmund | Automotive mixed-signal chips | high |  |
| [EnSilica](https://www.ensilica.com) | UK | Abingdon | ASIC design services and mixed-signal IP | medium | AIM listed |
| [ESMC (European Semiconductor Manufacturing Company)](https://focustaiwan.tw/business/202609150007) | DE | Dresden | 28/22 and 16/12nm foundry, under construction | high | ANNOUNCED/UNDER CONSTRUCTION: TSMC 70%, Bosch, Infineon, NXP 10% each; tool install H2 2027, production target 2027 |
| [Ferdinand-Braun-Institut](https://www.fbh-berlin.de) | DE | Berlin | III-V compound semiconductor R&D, GaN/GaAs | medium | Leibniz Association institute |
| [Ferroelectric Memory Company (FMC)](https://fmc.ag) | DE | Dresden | Ferroelectric memory (DRAM+/NVM) technology | medium |  |
| [Fractile](https://www.fractile.ai) | UK | London | In-memory compute AI inference chips | medium |  |
| [Fraunhofer-Gesellschaft (microelectronics institutes)](https://www.fraunhofer.de) | DE | Munich | Applied chip R&D, pilot lines (IMS, ISIT, IZM) | medium | Network of institutes; HQ Munich, relevant sites Duisburg, Itzehoe, Dresden, Berlin |
| [Graphcore](https://www.artificialintelligence-news.com/news/softbank-acquires-british-ai-chipmaker-graphcore/) | UK | Bristol | AI accelerator (IPU) designer | high | Wholly owned by SoftBank since 2024; HQ and ops remain Bristol |
| [IHP Leibniz Institute](https://www.ihp-microelectronics.com) | DE | Frankfurt (Oder) | SiGe BiCMOS pilot line, open foundry | medium | Leibniz Association institute |
| Infineon | DE | Neubiberg | Power chips, automotive and industrial | medium |  |
| [Innatera](https://innatera.com) | NL | Delft | Neuromorphic spiking edge AI processors | medium |  |
| [Lumai](https://www.lumai.co) | UK | Oxford | Optical AI compute accelerators | low |  |
| [Melexis](https://www.melexis.com) | BE | Ypres | Automotive sensor and driver ICs, fabless | high |  |
| [NANIUM](https://www.amkor.com) | PT | Vila do Conde | Wafer-level fan-out packaging OSAT | medium | Owned by Amkor Technology (US) |
| [Nexperia](https://en.wikipedia.org/wiki/Nexperia) | NL | Nijmegen | Discrete and power semiconductors, own fabs | high | Owned by China's Wingtech; Dutch state intervention Oct 2025, governance dispute and Chinese-subsidiary split ongoing Aug 2026 |
| [Nordic Semiconductor](https://www.nordicsemi.com) | NO | Trondheim | Low-power wireless and edge AI SoCs, fabless | high |  |
| NXP | NL | Eindhoven | Automotive and embedded chips | medium |  |
| [Pragmatic Semiconductor](https://www.pragmaticsemi.com) | UK | Durham | Flexible chips with own fabs | medium |  |
| [Prophesee](https://www.prophesee.ai) | FR | Paris | Neuromorphic event-based vision sensors | medium |  |
| [Q.ANT](https://qant.com) | DE | Stuttgart | Photonic AI processor | medium | Trumpf spin-out |
| [Salience Labs](https://www.salience.ai) | UK | Oxford | Photonic switching and compute chips | medium |  |
| [Schweizer Electronic](https://www.schweizer.ag) | DE | Schramberg | Chip embedding and power PCBs | low | Majority held by Katek/ Dr. Schweizer (verify) |
| [SEMIKRON Danfoss](https://www.semikron-danfoss.com) | DE | Nuremberg | Power semiconductor modules | medium | Merged with Danfoss Silicon Power 2022 |
| [SEMRON](https://www.semron.ai) | DE | Dresden | Analog in-memory edge AI chips | low |  |
| [Silicon Austria Labs](https://www.silicon-austria-labs.com) | AT | Villach | Electronic-based systems and chip research | medium | Public-private research centre |
| [Silicon Box (Novara plant)](https://www.teleborsa.it/News/2026/10/01/microchip-via-libera-invitalia-al-finanziamento-per-progetto-silicon-box-a-novara-119.html) | IT | Novara | Panel-level advanced packaging fab, planned | medium | ANNOUNCED: EUR 3.2bn Vulcan project; Silicon Box group HQ is Singapore, Italian entity only; Invitalia funding approved Oct 2026 |
| SiPearl | FR | Maisons-Laffitte | European HPC processor | medium |  |
| [Sivers Semiconductors](https://www.sivers-semiconductors.com) | SE | Kista | Photonics lasers and RF for optical interconnect | medium |  |
| [SMART Photonics](https://www.smartphotonics.nl) | NL | Eindhoven | Indium phosphide photonic chip foundry | medium |  |
| [SpiNNcloud Systems](https://spinncloud.com) | DE | Dresden | Neuromorphic HPC systems (SpiNNaker2) | medium | TU Dresden spin-out |
| STMicroelectronics | CH | Geneva | Broad chip portfolio, own fabs | medium | Legal HQ Geneva, French and Italian roots |
| [SynSense](https://www.synsense.ai) | CH | Zurich | Neuromorphic edge AI chips | medium | Operations also in Chengdu, China |
| [Tyndall National Institute](https://www.tyndall.ie/news/fames-becomes-first-eu-chips-act-pilot-line-to-reach-full-operation/) | IE | Cork | Photonics and chip R&D, FAMES pilot line partner | high | Part of University College Cork |
| [Ubitium](https://ubitium.com) | DE | Karlsruhe | Universal RISC-V processor architecture | low |  |
| [United Monolithic Semiconductors (UMS)](https://www.ums-rf.com) | DE | Ulm | GaN and GaAs RF foundry | low | HQ Ulm, fab in Ulm and Villebon-sur-Yvette FR; Airbus/Thales/Hensoldt shareholders (verify) |
| [VSORA](https://www.eetimes.eu/?p=44379) | FR | Paris | AI inference chip (Jotunn8) for data centres | medium | Taped out on TSMC 5nm; 2026 shipment status unverified |
| [VTT Technical Research Centre](https://www.vttresearch.com) | FI | Espoo | Micro/nanofabrication, photonics pilot line | medium | State-owned research company; Micronova cleanroom |
| [X-FAB Silicon Foundries](https://www.xfab.com) | BE | Tessenderlo | Analog/mixed-signal and SiC specialty foundry | high | Euronext Paris listed; fabs in DE, FR, MY, US |

## L5 · Systems and infrastructure

| Company | Country | City | Role | Confidence | Note |
|---|---|---|---|---|---|
| [ABB](https://www.abb.com) | CH | Zurich | Electrical equipment and power distribution | high |  |
| [ACS Group](https://www.grupoacs.com) | ES | Madrid | Construction, owns Turner | medium |  |
| [Alfa Laval](https://www.alfalaval.com) | SE | Lund | Heat exchangers for cooling | high |  |
| [AMS-IX](https://www.ams-ix.net) | NL | Amsterdam | Internet exchange | medium | Association |
| [Ansaldo Energia](https://www.ansaldoenergia.com) | IT | Genoa | Gas turbines | medium |  |
| [Arelion](https://www.arelion.com) | SE | Stockholm | Backbone network | medium | Owned by Polhem Infra |
| [Ark Data Centres](https://www.arkdc.com) | UK | Corsham | UK colocation operator | medium |  |
| [Aruba](https://www.aruba.it) | IT | Ponte San Pietro | Cloud and data centres | medium |  |
| [Arup](https://www.arup.com) | UK | London | Engineering design | medium | Trust-owned |
| [Asperitas](https://asperitas.com) | NL | Schiphol-Rijk | Immersion cooling | medium |  |
| [atNorth](https://www.atnorth.com) | IS | Reykjavik | Nordic HPC and AI colocation | medium | Owned by Partners Group |
| [Barcelona Supercomputing Center](https://www.bsc.es) | ES | Barcelona | Hosts MareNostrum 5 | high |  |
| [Bouygues](https://www.bouygues.com) | FR | Paris | Construction incl. data centres | medium |  |
| [Bull (Atos Advanced Computing)](https://atosgroup.com/en/press/atos-group-completes-sale-bull-its-advanced-computing-activities-french-state) | FR | Les Clayes-sous-Bois | BullSequana supercomputers and AI servers | high | Sold by Atos/Eviden to French state, closed 31 Mar 2026; corrects existing Eviden entry (Eviden now only cybersecurity/mission-critical) |
| [CINECA](https://www.cineca.it) | IT | Bologna | Hosts Leonardo supercomputer | high | University consortium |
| [Civo](https://www.civo.com) | UK | London | Developer cloud with GPU offering | low |  |
| [Cloud&Heat Technologies](https://www.cloudandheat.com) | DE | Dresden | Heat-reuse servers and sovereign cloud | medium |  |
| [Colt Data Centre Services](https://www.coltdatacentres.net) | UK | London | Hyperscale data centres | medium | Part of Colt Technology Services |
| [CSC - IT Center for Science](https://www.csc.fi) | FI | Espoo | Operates LUMI supercomputer | high | State-owned |
| [Danfoss](https://www.danfoss.com) | DK | Nordborg | Cooling components and heat reuse | medium |  |
| [Data4](https://www.data4group.com) | FR | Paris | Data centre campuses across Europe | high | Owned by Brookfield since 2023 |
| [DE-CIX](https://www.de-cix.net) | DE | Frankfurt | Internet exchange operator | medium |  |
| [Deutsche Telekom (T-Systems)](https://www.telekom.com) | DE | Bonn | Industrial AI Cloud, sovereign cloud, data centres | medium | With Nvidia AI factory in Munich |
| [E.ON](https://www.eon.com) | DE | Essen | Grids and energy | high |  |
| [E4 Computer Engineering](https://www.e4company.com) | IT | Scandiano | HPC and AI server systems | medium |  |
| [EcoDataCenter](https://ecodatacenter.se) | SE | Falun | Climate-positive data centres | medium |  |
| [EDF](https://www.edf.fr) | FR | Paris | Nuclear and utility | high | State-owned |
| [EFFECT Photonics](https://effectphotonics.com) | NL | Eindhoven | Coherent optical transceivers | medium |  |
| [Ekinops](https://www.ekinops.com) | FR | Lannion | Optical transport equipment | low |  |
| [Enel](https://www.enel.com) | IT | Rome | Utility and renewables | high |  |
| [ENGIE](https://www.engie.com) | FR | Courbevoie | Utility and renewables | high |  |
| [EuroHPC Joint Undertaking](https://eurohpc-ju.europa.eu) | LU | Luxembourg | Funds EU supercomputers and AI factories | high | EU public body |
| [Eurotech](https://www.eurotech.com) | IT | Amaro | Edge and HPC computers | medium |  |
| Eviden | FR | Bezons | Servers and supercomputers | low | Atos unit. Bull (HPC) was reportedly sold to the French state in March 2026 |
| [evroc](https://evroc.com) | SE | Stockholm | Sovereign hyperscale cloud and AI compute | high |  |
| [Exaion](https://exaion.com) | FR | Paris | HPC and AI cloud | low | EDF subsidiary |
| [Ferrovial](https://www.ferrovial.com) | ES | Madrid | Construction and infrastructure | low |  |
| [Forschungszentrum Julich (JSC)](https://www.fz-juelich.de) | DE | Julich | Hosts JUPITER exascale supercomputer | high |  |
| [Fortum](https://www.fortum.com) | FI | Espoo | Power and nuclear | medium |  |
| [Gcore](https://gcore.com) | LU | Luxembourg | AI cloud and edge | medium |  |
| [Genesis Cloud](https://www.genesiscloud.com) | DE | Munich | GPU cloud on Nordic data centres | medium |  |
| [Global Switch](https://www.globalswitch.com) | UK | London | Hyperscale colocation | medium | Owned by Chinese-led consortium |
| [Green Mountain](https://greenmountain.no) | NO | Stavanger | Norwegian green colocation | medium | Owned by Azrieli Group (Israel) |
| [Hetzner Online](https://www.hetzner.com) | DE | Gunzenhausen | Hosting, dedicated servers, GPU servers | high |  |
| [Hitachi Energy](https://www.hitachienergy.com) | CH | Zurich | Transformers and grid equipment | medium | Owned by Hitachi (Japan) |
| [HUBER+SUHNER](https://www.hubersuhner.com) | CH | Herisau | Fibre and RF connectivity | medium |  |
| [Hyperstack (NexGen Cloud)](https://www.hyperstack.cloud) | UK | London | GPU cloud | low |  |
| [Iberdrola](https://www.iberdrola.com) | ES | Bilbao | Utility, renewables, grids | high |  |
| [Iceotope](https://www.iceotope.com) | UK | Sheffield | Liquid cooling | high |  |
| [Infomaniak](https://www.infomaniak.com) | CH | Geneva | Swiss cloud and own data centres | medium |  |
| [IONOS](https://www.ionos.com) | DE | Montabaur | Cloud and hosting | high | United Internet majority owner |
| [Kao Data](https://www.kaodata.com) | UK | Harlow | AI-ready colocation campuses | medium |  |
| [Leaseweb](https://www.leaseweb.com) | NL | Haarlem | Hosting, cloud and GPU servers | medium |  |
| [Legrand](https://www.legrand.com) | FR | Limoges | Power distribution for data centres | high |  |
| [Mace](https://www.macegroup.com) | UK | London | Data centre construction management | medium |  |
| [MEGWARE](https://www.megware.com) | DE | Chemnitz | HPC cluster and liquid-cooled server builder | medium |  |
| [Mercury Engineering](https://www.mercury.ie) | IE | Dublin | Mechanical and electrical data centre contractor | low |  |
| [Merlin Properties](https://www.merlinproperties.com) | ES | Madrid | REIT developing data centres | medium |  |
| [Munters](https://www.munters.com) | SE | Kista | Data centre air and cooling | medium |  |
| [National Grid](https://www.nationalgrid.com) | UK | London | Transmission networks | high |  |
| Nebius | NL | Amsterdam | AI-focused cloud | medium |  |
| [Nebul](https://www.nebul.com) | NL | Leiden | Sovereign private AI cloud | medium | HQ reported as Leiden by NetApp, Amsterdam by some sources |
| [Nexans](https://www.nexans.com) | FR | Courbevoie | Power and data cables | high |  |
| [NKT](https://www.nkt.com) | DK | Brondby | High-voltage cables | medium |  |
| [Nokia](https://www.nokia.com) | FI | Espoo | Data centre networking and optical | high |  |
| [Nordex](https://www.nordex-online.com) | DE | Hamburg | Wind turbines | medium |  |
| [Northern Data](https://northerndata.de) | DE | Frankfurt | GPU cloud and HPC data centres | medium | 85.2% acquired by Rumble (US) 17 Jun 2026; operations/HQ remain Frankfurt |
| [Nscale](https://www.nscale.com) | UK | London | AI hyperscaler, GPU data centres incl. Narvik | high |  |
| [Oriole Networks](https://oriolenetworks.com) | UK | London | Optical switching for AI clusters | low |  |
| [Orsted](https://orsted.com) | DK | Fredericia | Offshore wind | high |  |
| [OUTSCALE](https://www.outscale.com) | FR | Saint-Cloud | SecNumCloud sovereign cloud | medium | Dassault Systemes subsidiary |
| OVHcloud | FR | Roubaix | European cloud and hosting | medium |  |
| [ParTec](https://par-tec.com) | DE | Munich | Modular supercomputer architecture, JUPITER system software | medium |  |
| [Piller Power Systems](https://www.piller.com) | DE | Osterode am Harz | Rotary UPS | medium | Owned by Langley Holdings (UK) |
| [Prysmian](https://www.prysmian.com) | IT | Milan | Power and fibre cables | high |  |
| [Riello UPS](https://www.riello-ups.com) | IT | Legnago | UPS systems | medium |  |
| [Rittal](https://www.rittal.com) | DE | Herborn | Enclosures and cooling | high | Friedhelm Loh Group |
| [Rolls-Royce (mtu power systems)](https://www.rolls-royce.com) | UK | London | Backup generators for data centres | medium |  |
| [Rolls-Royce SMR](https://www.rolls-royce-smr.com) | UK | Derby | Small modular reactors | medium |  |
| [Royal BAM Group](https://www.bam.com) | NL | Bunnik | Construction | low |  |
| [RWE](https://www.rwe.com) | DE | Essen | Power generation | high |  |
| [Scaleway](https://www.scaleway.com) | FR | Paris | European cloud with GPU clusters | high | Part of Iliad group |
| Schneider Electric | FR | Rueil-Malmaison | Data centre power and cooling | medium |  |
| [Seeweb](https://www.seeweb.it) | IT | Frosinone | Cloud with GPU services | low |  |
| [Sesterce](https://www.sesterce.com) | FR | Marseille | GPU cloud and AI data centres (Valence) | medium | HQ listed as Marseille on one directory only |
| [Siemens AG (Smart Infrastructure)](https://www.siemens.com) | DE | Munich | Switchgear and building systems | medium | Parent of Siemens Energy spin-off |
| Siemens Energy | DE | Munich | Power generation and grid equipment | medium |  |
| [Sisk](https://www.sisk.com) | IE | Dublin | Data centre construction | medium |  |
| [Skanska](https://group.skanska.com) | SE | Stockholm | Construction | medium |  |
| [Socomec](https://www.socomec.com) | FR | Benfeld | UPS and switching | medium |  |
| [SSE](https://www.sse.com) | UK | Perth | Renewables and networks | medium |  |
| [STACKIT](https://www.stackit.de) | DE | Neckarsulm | Sovereign cloud of Schwarz Group | high | Schwarz Digits |
| [START Campus](https://www.startcampus.com) | PT | Lisbon | Sines hyperscale data centre campus | medium |  |
| [Statkraft](https://www.statkraft.com) | NO | Oslo | Hydropower | high | Norwegian state-owned |
| [STULZ](https://www.stulz.com) | DE | Hamburg | Precision cooling | high |  |
| [Submer](https://submer.com) | ES | Barcelona | Immersion cooling and data centres | high |  |
| [Swisscom](https://www.swisscom.ch) | CH | Ittigen | Telco with AI cloud and data centres | medium | Majority Swiss state-owned |
| [Switch Datacenters](https://www.switchdatacenters.com) | NL | Amsterdam | Amsterdam colocation | low |  |
| [Telenor](https://www.telenor.com) | NO | Fornebu | Telco running Telenor AI Factory | medium | Norwegian state majority |
| [TenneT](https://www.tennet.eu) | NL | Arnhem | Transmission system operator | medium | Dutch state-owned |
| [Thomas-Krenn](https://www.thomas-krenn.com) | DE | Freyung | Server and storage manufacturer | low | Owned by Noris Network |
| [UpCloud](https://upcloud.com) | FI | Helsinki | Cloud infrastructure provider | medium |  |
| [Vattenfall](https://group.vattenfall.com) | SE | Stockholm | Nuclear, hydro, wind | high | Swedish state-owned |
| [Verda (formerly DataCrunch)](https://verda.com) | FI | Helsinki | Nordic GPU cloud | high | Rebranded Nov 2025 |
| [Verne](https://verne.com) | UK | London | Nordic hyperscale data centres | low | Owned by Ardian |
| [Vestas](https://www.vestas.com) | DK | Aarhus | Wind turbines | high |  |
| [Vinci](https://www.vinci.com) | FR | Rueil-Malmaison | Construction incl. data centres | medium |  |
| [Waertsilae](https://www.wartsila.com) | FI | Helsinki | Engine power plants | medium |  |

## L6 · Data and talent

| Company | Country | City | Role | Confidence | Note |
|---|---|---|---|---|---|
| [AI Sweden](https://www.ai.se) | SE | Gothenburg | National AI applied research centre | medium | Publicly funded, built GPT-SW3 |
| [Aindo](https://www.aindo.com) | IT | Trieste | Synthetic data platform | medium |  |
| [Alan Turing Institute](https://www.turing.ac.uk) | UK | London | UK national institute for data science and AI | high |  |
| [Anyverse](https://anyverse.ai) | ES | Valencia | Synthetic sensor data for perception AI | low | HQ city from memory |
| [Apheris](https://www.apheris.com) | DE | Berlin | Federated data collaboration for AI | medium |  |
| Clickworker | DE | Essen | Crowd work for data and labelling | medium |  |
| [Datarade](https://datarade.ai) | DE | Berlin | Data marketplace directory | low |  |
| [Dawex](https://www.dawex.com) | FR | Lyon | Data exchange and marketplace platform | medium |  |
| [DFKI](https://www.dfki.de) | DE | Kaiserslautern | German Research Center for AI | medium | Non-profit GmbH, several sites |
| [ELLIS Institute Tubingen](https://institute-tue.ellis.eu) | DE | Tubingen | European AI research institute and talent hub | medium | Part of the ELLIS network |
| [Encord](https://encord.com) | UK | London | Multimodal data annotation and curation platform | medium | Also large San Francisco presence; raised $60M Dec 2025 |
| [Entrepreneur First](https://www.joinef.com) | UK | London | Talent investor building AI founders | medium | Also operates in Paris, Berlin and elsewhere |
| [ETH AI Center](https://ai.ethz.ch) | CH | Zurich | ETH Zurich AI research and talent centre | medium | University unit |
| [Giskard](https://www.giskard.ai) | FR | Paris | AI testing and evaluation tooling | medium |  |
| [Hopsworks](https://www.hopsworks.ai) | SE | Stockholm | Feature store and ML data platform | medium |  |
| [Idiap Research Institute](https://www.idiap.ch) | CH | Martigny | Speech and machine-learning research institute | medium |  |
| [IDSIA USI-SUPSI](https://www.idsia.ch) | CH | Lugano | AI research institute | medium | Academic institute |
| [Innovatiana](https://www.innovatiana.com) | FR | Paris | Data labelling services | medium |  |
| [Inria](https://www.inria.fr) | FR | Paris | National research institute for digital science | medium | Public body; HQ at Le Chesnay near Paris |
| [isahit](https://www.isahit.com) | FR | Paris | Ethical data annotation workforce | medium |  |
| [Kili Technology](https://kili-technology.com) | FR | Paris | Data labelling platform and services | medium |  |
| Kyutai | FR | Paris | Open research lab (non-profit) | medium |  |
| LAION | DE | Hamburg | Open datasets (non-profit) | medium |  |
| [Lightly](https://www.lightly.ai) | CH | Zurich | Data curation for computer vision | medium |  |
| [Max Planck Institute for Intelligent Systems](https://is.mpg.de) | DE | Tubingen | Machine learning and robotics research | medium | Also site in Stuttgart |
| [Merantix](https://www.merantix.com) | DE | Berlin | AI venture studio and talent hub | medium |  |
| [Mostly AI](https://mostly.ai) | AT | Vienna | Synthetic tabular data platform | medium |  |
| [Pangeanic](https://pangeanic.com) | ES | Valencia | Language data and machine-translation data | medium |  |
| [Pleias](https://pleias.fr) | FR | Paris | Open training corpora (Common Corpus) and small models | medium | Also builds small open models |
| Prolific | UK | London | Human participant data for research and evals | medium |  |
| [Qdrant](https://qdrant.tech) | DE | Berlin | Open-source vector database | medium |  |
| [RWS Holdings](https://www.rws.com) | UK | Chalfont St Peter | Language and AI training data services (TrainAI) | medium |  |
| [Synthesized](https://www.synthesized.io) | UK | London | Synthetic and test data platform | medium |  |
| [Syntho](https://www.syntho.ai) | NL | Delft | Synthetic data generation for enterprises | medium |  |
| [Teleperformance](https://www.tp.com) | FR | Paris | Customer-service giant with AI data services (TP.ai) | medium | AI data is a small part of the business |
| Toloka | NL | Amsterdam | Human data labelling | medium |  |
| [V7](https://www.v7labs.com) | UK | London | Data annotation and labelling platform | medium |  |
| [Valohai](https://valohai.com) | FI | Turku | MLOps platform | medium |  |
| [Weaviate](https://weaviate.io) | NL | Amsterdam | Open-source vector database | medium |  |

## L7 · Frontier labs

| Company | Country | City | Role | Confidence | Note |
|---|---|---|---|---|---|
| Aleph Alpha | DE | Heidelberg | Enterprise and sovereign LLMs | medium |  |
| [Almawave](https://www.almawave.com) | IT | Rome | Velvet sovereign Italian LLMs | medium |  |
| [AMI Labs](https://trendingtopics.eu/yann-lecuns-ami-labs-raises-1-billion-for-world-models-in-bet-against-llms) | FR | Paris | World-model research lab (LeCun) | high | Raised about $1.03B seed in 2026; offices also in NY, Montreal, Singapore |
| [Basecamp Research](https://www.basecamp-research.com) | UK | London | Biological foundation models and data | medium |  |
| [Bioptimus](https://www.bioptimus.com) | FR | Paris | Biology foundation models | medium |  |
| Black Forest Labs | DE | Freiburg | Image generation models | medium |  |
| [Cradle](https://www.cradle.bio) | NL | Amsterdam | Protein engineering AI models | medium | Also Zurich office |
| [Domyn](https://www.domyn.com) | IT | Milan | Enterprise LLMs (formerly iGenius) | medium |  |
| [ElevenLabs](https://en.wikipedia.org/wiki/ElevenLabs) | UK | London | Speech and audio generation models | low | Founded by Poles; sources split HQ between London and New York, entity is ElevenLabs Inc. Borderline |
| Google DeepMind | UK | London | Frontier models (owned by Alphabet) | medium | Part of Alphabet |
| [GPT-NL](https://gpt-nl.nl) | NL | Leiden | Dutch sovereign LLM | low | Led by TNO (Leiden/The Hague area), SURF, NFI |
| [Gradium](https://sifted.eu/articles/gradium-70m-seed-voice-ai) | FR | Paris | Voice (TTS and STT) foundation models | high | Spun out of Kyutai 2025; raised $70M seed |
| [H Company](https://www.hcompany.ai) | FR | Paris | Agentic and computer-use models | medium |  |
| [Ineffable Intelligence](https://sifted.eu/articles/david-silver-1bn-ineffable-intelligence) | UK | London | Reinforcement-learning superintelligence lab (David Silver) | high | Raised about $1.1B seed; no product yet |
| [InstaDeep](https://www.instadeep.com) | UK | London | Bio and decision-making AI models | medium | Owned by BioNTech; offices in Paris and elsewhere |
| [Isomorphic Labs](https://www.isomorphiclabs.com) | UK | London | AI drug-discovery models | high | Alphabet subsidiary |
| [Jua](https://jua.ai) | CH | Zurich | Weather foundation model | low |  |
| [Latent Labs](https://www.latentlabs.com) | UK | London | Protein design foundation models | medium |  |
| [LightOn](https://www.lighton.ai) | FR | Paris | Enterprise LLMs and retrieval models | medium | Listed on Euronext Growth |
| Mistral AI | FR | Paris | Frontier and open-weight models | medium |  |
| [Neuphonic](https://www.neuphonic.com) | UK | London | Text-to-speech models | low |  |
| [Poolside](https://sifted.eu/articles/poolside-raises-126m-relocated-france-news) | FR | Paris | Coding foundation models | low | US-founded, Sifted reported move of HQ to Paris in 2023; current HQ disputed (SF vs Paris) |
| [Silo AI](https://www.silo.ai) | FI | Helsinki | Open Nordic LLMs (Poro, Viking) | high | Acquired by AMD in 2024 |
| [Speechmatics](https://www.speechmatics.com) | UK | Cambridge | Speech recognition foundation models | medium |  |
| Stability AI | UK | London | Open image and media models | medium |  |
| [Swiss National AI Institute (Apertus)](https://www.swiss-ai.org) | CH | Zurich | Open sovereign LLM Apertus | medium | EPFL and ETH Zurich joint initiative; HQ split Zurich/Lausanne |
| [Tilde](https://tilde.ai) | LV | Riga | TildeOpen open multilingual LLM | medium |  |
| [Wayve](https://wayve.ai) | UK | London | Embodied AI driving foundation models | high |  |

## L8 · Delivery and applications

| Company | Country | City | Role | Confidence | Note |
|---|---|---|---|---|---|
| [Ada Health](https://ada.com) | DE | Berlin | AI symptom assessment | medium |  |
| [Adaptive ML](https://www.adaptive-ml.com) | FR | Paris | Reinforcement-tuning of enterprise LLMs | medium |  |
| [Alpine Eagle](https://www.alpineeagle.com) | DE | Munich | AI counter-drone systems | medium |  |
| [ARX Robotics](https://arx-robotics.com) | DE | Munich | Autonomous military ground robots | medium |  |
| [Brainomix](https://www.brainomix.com) | UK | Oxford | AI stroke imaging | medium |  |
| [Capgemini](https://www.capgemini.com) | FR | Paris | IT services, large AI practice | medium |  |
| [Celonis](https://www.celonis.com) | DE | Munich | Process intelligence with AI | medium | Dual HQ Munich/New York |
| [Cognigy](https://www.cognigy.com) | DE | Dusseldorf | Conversational AI for contact centres | medium | Acquired by NICE (Israel) 2025 |
| [Cognite](https://www.cognite.com) | NO | Oslo | Industrial AI data platform | medium | Majority-owned by Aker |
| [Colossyan](https://www.colossyan.com) | UK | London | AI avatar video | low |  |
| [Corti](https://www.corti.ai) | DK | Copenhagen | AI for clinical conversations | medium |  |
| [Dassault Systemes](https://www.3ds.com) | FR | Paris | 3D software with AI (Velizy HQ) | medium | HQ at Velizy-Villacoublay |
| DeepL | DE | Cologne | AI translation and writing | medium |  |
| [deepset](https://www.deepset.ai) | DE | Berlin | Haystack framework and enterprise AI platform | medium |  |
| [Doctolib](https://www.doctolib.fr) | FR | Paris | Health platform with AI assistants | medium |  |
| [Dust](https://dust.tt) | FR | Paris | Enterprise AI agent platform | medium |  |
| [Faculty](https://faculty.ai) | UK | London | Applied AI for enterprise and defence | low | Possibly acquired by Accenture in 2026 (recollection, unverified) |
| [Flawless AI](https://www.flawlessai.com) | UK | London | AI dubbing and visual dubbing | medium |  |
| [Fyxer AI](https://www.fyxer.com) | UK | London | AI email assistant | low |  |
| [Gladia](https://www.gladia.io) | FR | Paris | Speech-to-text API | medium |  |
| [Harmattan AI](https://sifted.eu/articles/harmattan-ai-200m-series-b-unicorn) | FR | Paris | AI combat drones | high | $200M Series B Jan 2026, Dassault-led |
| Helsing | DE | Munich | Defence AI | medium |  |
| [JetBrains](https://www.jetbrains.com) | CZ | Prague | IDEs with AI assistant and Junie agent | high |  |
| [Klarna](https://www.klarna.com) | SE | Stockholm | Fintech with AI assistant | medium |  |
| [Legora](https://legora.com) | SE | Stockholm | AI legal assistant | high |  |
| [Leya](https://www.leya.law) | SE | Stockholm | Legal AI assistant | low |  |
| Lovable | SE | Stockholm | AI app builder | medium |  |
| [Luminance](https://www.luminance.com) | UK | Cambridge | AI contract review for legal | medium |  |
| [Multiverse Computing](https://multiverse.com) | ES | San Sebastian | Model compression (CompactifAI) | high |  |
| [n8n](https://n8n.io) | DE | Berlin | AI workflow automation | high |  |
| [Nabla](https://www.nabla.com) | FR | Paris | Ambient AI clinical scribe | high |  |
| [Neural Concept](https://www.neuralconcept.com) | CH | Lausanne | AI engineering simulation | medium |  |
| [Owkin](https://www.owkin.com) | FR | Paris | AI for drug discovery and diagnostics | medium | Also New York office |
| [Parloa](https://www.parloa.com) | DE | Berlin | AI customer-service agents | high |  |
| [Philips](https://www.philips.com) | NL | Amsterdam | Health tech with AI imaging | medium | Headquartered in Amsterdam |
| [Photoroom](https://www.photoroom.com) | FR | Paris | AI photo editing app | high |  |
| [Pitch](https://pitch.com) | DE | Berlin | AI presentation software | low |  |
| [PolyAI](https://poly.ai) | UK | London | Voice assistants for customer service | high |  |
| [Preligens](https://www.preligens.com) | FR | Paris | AI geospatial intelligence for defence | medium | Acquired by Safran 2024 |
| [Pruna AI](https://www.pruna.ai) | DE | Munich | Model optimisation for inference | low | HQ Munich/Paris, from memory |
| [Quantexa](https://www.quantexa.com) | UK | London | Decision intelligence and entity resolution | high |  |
| [Quantum Systems](https://quantum-systems.com) | DE | Munich | AI-enabled defence and survey drones | high |  |
| [Rasa](https://rasa.com) | DE | Berlin | Conversational AI framework | medium | Also US presence |
| [Respeecher](https://www.respeecher.com) | UA | Kyiv | Voice cloning | medium | Ukraine, Europe |
| [Sana](https://sana.ai) | SE | Stockholm | AI knowledge and learning platform | medium | Acquired by Workday 2025 |
| SAP | DE | Walldorf | Enterprise software with embedded AI | medium |  |
| [Siemens](https://www.siemens.com) | DE | Munich | Industrial AI and copilots | high |  |
| [SOPHiA GENETICS](https://www.sophiagenetics.com) | CH | Geneva | AI genomic analytics (HQ Rolle/Geneva area) | medium | Nasdaq-listed; HQ in Rolle, Vaud |
| [Spotify](https://www.spotify.com) | SE | Stockholm | Streaming with AI DJ and recommendations | medium | Luxembourg-incorporated |
| [Stark Defence](https://stark-defence.com) | DE | Berlin | Autonomous strike drones | medium |  |
| Synthesia | UK | London | AI video generation | medium |  |
| [Synthflow](https://synthflow.ai) | DE | Berlin | Voice AI agents | medium |  |
| [Tandem Health](https://www.tandemhealth.ai) | SE | Stockholm | AI medical scribe | medium |  |
| [Tekever](https://www.tekever.com) | PT | Lisbon | AI-enabled unmanned systems | medium |  |
| [Tessl](https://tessl.io) | UK | London | AI-native software development | medium |  |
| [Tractable](https://tractable.ai) | UK | London | AI vehicle damage assessment | medium |  |
| [Unbabel](https://unbabel.com) | PT | Lisbon | AI translation for customer support | medium |  |
| [Veed](https://www.veed.io) | UK | London | AI video editing | medium |  |
