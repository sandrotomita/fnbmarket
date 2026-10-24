"""All site text lives here. Edit, then run: python3 build_pages.py

Content is transcribed from:
  - Food_Ingredients_Market_2036.pptx (slides + speaker notes, evidence reviewed 24 Oct 2026)
  - 2036_fb.docx (consumer vision)
  - Sandro_Sato_Tomita.html (bio, kept in content/bio.html)
Plain text only: the build script escapes &, < and >.
"""

AUTHOR = "Sandro Sato Tomita"
SITE = "Food Ingredients 2036"
DOMAIN = "sandrotomita.com"
REVIEWED = "24 October 2026"

# ---------------------------------------------------------------- Sources (S01–S20 as numbered in the deck)
SOURCES = {
    "S01": ("Shell: What are Shell Scenarios?", "https://www.shell.com/news-and-insights/scenarios/what-are-shell-scenarios.html", "Scenario method, not a prediction"),
    "S02": ("Shell: 40 Years of Shell Scenarios", "https://www.shell.com/news-and-insights/scenarios/what-are-shell-scenarios/_jcr_content/root/main/section_509167378/promo/links/item0.stream/1652289755448/a0e75f042fee5322b72780ee36e5ba17c35a4fc6/shell-scenarios-40yearsbook080213.pdf", "Wack and Schwartz tradition"),
    "S03": ("UMass Amherst: David Julian McClements, research and publications", "https://www.umass.edu/food-science/about/directory/david-julian-mcclements", "Food structure, delivery systems and future foods"),
    "S04": ("Schreurs et al.: Predicting and improving complex beer flavor through machine learning", "https://www.nature.com/articles/s41467-024-46346-0", "Nature Communications, 2024. DOI: 10.1038/s41467-024-46346-0"),
    "S05": ("Kew et al.: Transforming sustainable plant proteins into high performance lubricating microgels", "https://www.nature.com/articles/s41467-023-40414-7", "Nature Communications, 2023. DOI: 10.1038/s41467-023-40414-7"),
    "S06": ("FDA: Substances Generally Recognized as Safe, proposed rule", "https://www.fda.gov/about-fda/economic-impact-analyses-fda-regulations/substances-generally-recognized-safe-proposed-rule", "August 2026. Proposed mandatory notification, not universal approval"),
    "S07": ("European Commission: Smoke flavouring renewals and phase-out measures", "https://food.ec.europa.eu/food-safety/food-improvement-agents/flavourings/smoke-flavouring-renewals-existing_en", "Category-specific transition dates in 2026 and 2029"),
    "S08": ("FDA: FD&C Red No. 3", "https://www.fda.gov/industry/color-additives/fdc-red-no-3", "Food reformulation deadline: 15 January 2027"),
    "S09": ("UK Government: Strengthening the Soft Drinks Industry Levy, summary of responses", "https://www.gov.uk/government/consultations/strengthening-the-soft-drinks-industry-levy/outcome/strengthening-the-soft-drinks-industry-levy-summary-of-responses", "Policy decision published 25 November 2025. Planned start: January 2028"),
    "S10": ("Singapore Food Agency: Overview of pre-market approval framework for novel food", "https://www.sfa.gov.sg/regulatory-standards-frameworks-guidelines/novel-food-framework/overview-of-pre-market-approval-framework-for-novel-food", "Safety assessment and pre-market approval requirements"),
    "S11": ("European Commission: Novel food legislation", "https://food.ec.europa.eu/food-safety/novel-food/legislation_en", "Regulation (EU) 2015/2283"),
    "S12": ("European Commission: EUDR postponement and implementation changes", "https://trade.ec.europa.eu/access-to-markets/en/news/delay-until-december-2026-and-other-developments-implementation-eudr-regulation", "Main application dates: December 2026 and June 2027"),
    "S13": ("European Commission: Regulation on deforestation-free products", "https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en", "Commodity and product scope. Additional products have later dates"),
    "S14": ("European Commission: Questions and answers on Directive (EU) 2024/825", "https://commission.europa.eu/document/download/3c257883-bb2a-4dd9-a6dc-501d587bb34f_en?filename=faq-empowerting-consumers-gtd.pdf", "Environmental claims. Application date: 27 September 2026"),
    "S15": ("EUR-Lex: Regulation (EC) 1334/2008, Article 16", "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02008R1334-20260216", "Natural flavouring and named-source requirements"),
    "S16": ("dsm-firmenich: EverSweet stevia sweetener", "https://www.dsm-firmenich.com/en/businesses/taste-texture-health/markets-products/dairy/fresh-dairy-fermented/eversweet.html", "Supplier example: fermentation-derived Reb M and Reb D"),
    "S17": ("GFI and Hawkwood Biotech: Driving down costs of fermentation-derived ingredients", "https://gfi.org/wp-content/uploads/2025/06/Driving-down-costs-of-fermentation-derived-ingredients.pdf", "June 2025. Techno-economic analysis, with advocacy-sector perspective"),
    "S18": ("IFF: NURICA enzyme solution", "https://www.iff.com/food-beverage/food-bioscience/cultures/dairy-cultures/nurica/", "Supplier example: in-situ conversion of lactose-derived sugars into GOS"),
    "S19": ("Tate & Lyle: NUTRAVA Citrus Fiber", "https://www.tateandlyle.com/ingredient/clean-label-nutrava-citrus-fiber", "Supplier example: functional fibre from juice-industry citrus peels"),
    "S20": ("University of Leeds: Professor Anwesha Sarkar", "https://environment.leeds.ac.uk/food-nutrition/staff/7151/professor-anwesha-sarkar", "Oral tribology, microgels and food colloids"),
    # Consumer-vision sources from 2036_fb.docx. The document gives no full URLs for C1 and C2.
    "C1": ("National Restaurant Association: 2025 experience research", None, "Cited in the consumer vision document (go.restaurant.org)"),
    "C2": ("Restaurants Canada: social-dining research", None, "Cited in the consumer vision document"),
}

# ---------------------------------------------------------------- Home
HOME = dict(
    eyebrow="Food ingredients in 2036 · Ten-year strategic horizon",
    title="Suppliers will increasingly sell a verified product outcome, alongside the ingredient.",
    lead="A market vision with flavours at its centre: five regulatory disruptions and five technology disruptions that will reshape food and beverage ingredients over the next decade.",
    brief="Keep our familiar taste. Lower sugar. Work with two protein sources. Show safety, legal status and origin for every market.",
    value_shift="Value moves towards integrated flavour, texture and nutrition systems, supported by application data and regulatory evidence. Commodity ingredients remain the volume backbone.",
    central="Central scenario: stricter evidence requirements, uneven market access and selective technology scale-up. This is a strategic hypothesis, not a market-size forecast.",
    scope="Scope: food and beverage ingredients, including flavours, sweeteners, proteins, fats, fibres, enzymes, colours and stabilisers. The lens is global, illustrated by the EU, US, UK and Singapore. China, India and Latin America need separate country-level validation. No aggregate market CAGR is asserted because ingredient-market definitions overlap and a consistent baseline has not been established. All 2036 outcomes are analyst scenarios.",
)

# ---------------------------------------------------------------- Findings (one page each)
FINDINGS = [
    dict(slug="ingredient-safety", kind="Regulation", n=1,
         title="More scrutiny of ingredient safety",
         meta="Highest strategic impact · 2026–2030 pressure, continuing through 2036 · High confidence in direction",
         summary="More suppliers may need maintained safety dossiers and rapid replacement options; historical use alone becomes a weaker commercial assurance.",
         evidence="The US proposed mandatory GRAS notices in August 2026. EU withdrawals already affect eight smoke flavourings. Red No. 3 has a US food reformulation deadline in January 2027.",
         change="By 2036, more suppliers may need maintained safety dossiers and rapid replacement options. Historical use alone becomes a weaker commercial assurance.",
         example="A barbecue seasoning supplier qualifies alternative flavour systems, checks contaminant profiles and validates taste with customers. Manufacturers absorb testing and relaunch costs. Suppliers with credible replacement libraries gain business.",
         status="EU withdrawals and Red No. 3 action are enacted. The US GRAS change remains a proposal, not blanket pre-market approval.",
         notes=["The EU transition for foods containing the eight affected smoke primary products ended on 1 July 2026 for most categories, with 1 July 2029 for specified cheese, meat and fish categories and relevant subcategories. Eligible existing stocks can remain until minimum durability/use-by dates. This is not a ban on every smoky taste or traditional smoking.",
                "FDA says GRAS notification is currently voluntary and the August 2026 proposed rule would require notices for certain uses if finalised. Red No. 3 food deadline: 15 January 2027.",
                "Forecast: broader dossier maintenance and reformulation demand; no prediction that all current additives will be prohibited."],
         sources=["S06", "S07", "S08"]),
    dict(slug="nutrition-policy", kind="Regulation", n=2,
         title="Nutrition policy reshapes recipes",
         meta="2026–2036 · High confidence for sugar reformulation, medium for wider policy expansion",
         summary="Taxes, nutrient-based rules and procurement standards could make sugar and sodium reduction an operating requirement in more markets.",
         evidence="The UK announced a lower soft-drink levy threshold of 4.5 g sugar/100 ml and expansion to certain milk and plant-based drinks from January 2028.",
         change="Further taxes, nutrient-based rules and procurement standards could make sugar and sodium reduction an operating requirement in more markets.",
         example="A beverage brand replaces part of its sugar with an approved sweetener, then adjusts aroma, acidity and body. Food producers face similar taste challenges when reducing sodium. Integrated systems gain over standalone sweeteners.",
         status="UK policy decision with legislative implementation steps. A universal ultra-processed-food tax is not assumed.",
         notes=["The UK final policy decision changed the proposed 4 g threshold to 4.5 g. Scope includes pre-packaged milk-based drinks with added sugar, with a lactose allowance, and plant-based drinks with added sugar. Exemptions and sugar-accounting rules matter. A technical legislative process was specified before January 2028 implementation.",
                "Forecast expansion to other jurisdictions is an inference, not enacted global policy. Sugar removal can affect preservation and physical performance as well as taste, so recipes require validation."],
         sources=["S09"]),
    dict(slug="novel-ingredients", kind="Regulation", n=3,
         title="Novel ingredients face regional access gates",
         meta="2026–2036 · High confidence that approvals remain material, medium on future divergence",
         summary="Biotechnology could progress faster than regulatory alignment: an ingredient may launch in one market while another requires more data or a different route.",
         evidence="The EU and Singapore have pre-market frameworks for novel foods. Ingredient identity, production method and intended use matter to the applicable pathway.",
         change="Biotechnology could progress faster than regulatory alignment. An ingredient may launch in one market while another requires more data or a different route.",
         example="A fermentation-derived protein dessert launches only where its ingredient and use are permitted. The brand retains a conventional-protein recipe elsewhere. Approval portfolios influence where production and R&D locate.",
         status="Existing frameworks. Future divergence is a scenario. Flavours, additives and enzymes may follow specific regimes rather than the general novel-food route.",
         notes=["Singapore requires evidence-based safety assessment before novel food supply and can cancel approvals under specified conditions, including relevant changes in production. EU Regulation 2015/2283 establishes a novel food framework.",
                "Do not equate a US GRAS no-questions letter with an EU authorisation or assume a platform-wide approval covers every organism, process and application. The recommended response is ingredient-by-ingredient legal pathway mapping, staged launch markets and recipe fallbacks."],
         sources=["S10", "S11", "S06"]),
    dict(slug="origin-evidence", kind="Regulation", n=4,
         title="Origin evidence becomes a condition of supply",
         meta="2026–2036 · High confidence for covered EU products, medium for broader expansion",
         summary="Supplier origin evidence could become a routine buying requirement well beyond the strictly regulated products.",
         evidence="EUDR covers specified commodities and listed derived products, including relevant cocoa, coffee, soy and palm-oil products. Main application dates are December 2026 and June 2027.",
         change="Supplier evidence could become a routine buying requirement well beyond the strictly regulated products. The ability to preserve traceability through blending gains value.",
         example="A chocolate manufacturer qualifies cocoa batches with the required origin evidence and builds backup supply. Ingredient distributors invest in chain-of-custody data. Small suppliers need shared systems to remain competitive.",
         status="Enacted, with phased dates and role-specific duties. There is no assumed universal ingredient passport or global carbon label.",
         notes=["Latest Commission material reflects the 2025 postponement and simplification. Dates and obligations depend on actor, size and product, and newly added products have later dates. Do not imply that all palm derivatives or every flavour ingredient fall within EUDR.",
                "The 2036 data package discussed here is a commercial scenario, not an existing legal digital passport requirement. Data verification and supplier inclusion are material costs."],
         sources=["S12", "S13"]),
    dict(slug="defensible-claims", kind="Regulation", n=5,
         title="Claims need more defensible evidence",
         meta="2026–2036 · High confidence in scrutiny, medium on additional future rules",
         summary="“Natural”, “upcycled” and environmental positioning may need more precise, product-specific support.",
         evidence="EU consumer rules against misleading environmental claims apply from September 2026. Existing flavour law also limits when a named source can accompany “natural”.",
         change="“Natural”, “upcycled” and environmental positioning may need more precise, product-specific support. Marketing teams work with ingredient and regulatory teams earlier.",
         example="A brand using fermentation-derived vanillin checks the legal flavour designation instead of assuming “natural vanilla”. A lower-impact ingredient claim needs evidence relevant to the actual product and supply chain.",
         status="Environmental-claims rules and named-source rules already exist. Their wider commercial influence is the forecast.",
         notes=["Directive 2024/825 is distinct from the separate Green Claims proposal; the latter is not enacted.",
                "EU Article 16 requires at least 95% by weight of the flavouring component to come from the named source for the specific natural named-source designation, with other conditions and alternative permitted descriptions. “Natural flavouring” and “natural vanilla flavouring” are not interchangeable.",
                "Biotechnology does not automatically determine natural status; process, source and jurisdiction matter. Claims substantiation is separate from ingredient market authorisation."],
         sources=["S14", "S15"]),
    dict(slug="ai-formulation", kind="Technology", n=1,
         title="AI links formulation to sensory outcomes",
         meta="Selective use today · Wider adoption by 2030–2036 · High confidence in assistance, medium in autonomy",
         summary="Models could recommend recipes within taste, cost, legal and supply constraints, with automated experiments closing the loop.",
         evidence="A 2024 study combined chemical and sensory data from 250 beers with machine learning, then experimentally improved appreciation of selected beers.",
         change="Models could recommend recipes within taste, cost, legal and supply constraints. Automated experiments close the loop between prediction and actual food performance.",
         example="A drinks team screens alternatives to a scarce citrus oil, then tests the best candidates for aroma, stability and consumer liking. Fewer low-value trials can reduce development cost and time.",
         status="Human panels and production trials remain essential. Proprietary data quality, rights and performance on unfamiliar recipes limit the advantage.",
         notes=["The Schreurs/Verstrepen study is a demonstrated domain-specific application, not proof of universal flavour prediction. The 2036 extension to constrained multi-objective recipe design and automated experimentation is this analysis’s inference.",
                "Useful metrics: successful launch rate, trials per qualified formula, time to validated prototype and performance on a held-out product family. A generic language model alone does not establish food safety or sensory quality."],
         sources=["S04"]),
    dict(slug="fermentation", kind="Technology", n=2,
         title="Fermentation as an ingredient factory",
         meta="Commercial in selected ingredients · 2028–2036 expansion · Medium confidence in broad scale-up",
         summary="High-value sweeteners, flavour molecules and selected functional proteins are plausible early winners; bulk replacement remains conditional on process economics.",
         evidence="EverSweet is a commercial example of fermentation-derived Reb M and Reb D sweeteners. Public techno-economic work identifies major cost and scale constraints.",
         change="High-value sweeteners, flavour molecules and selected functional proteins are plausible early winners. Bulk replacement remains conditional on process economics.",
         example="A supplier offers an approved fermentation-derived aroma molecule as an alternative sourcing route. A brand qualifies it for taste and legal designation, then contracts for dependable capacity.",
         status="Cost depends on yield, productivity, feedstock, purification and plant utilisation. Fermentation does not automatically mean lower emissions or “natural”.",
         notes=["Supplier material verifies EverSweet as an existing example, not a universal cost or sustainability advantage. The GFI/Hawkwood report is an original sector analysis with an alternative-protein advocacy perspective. Selective expansion is a scenario.",
                "Compare total delivered cost-in-use rather than price per kilogram alone, including dose, function, downstream recovery and quality. For dairy-identical proteins, an animal-free production route must not be treated as evidence of absence of milk allergens."],
         sources=["S16", "S17"]),
    dict(slug="enzymes", kind="Technology", n=3,
         title="Enzymes change ingredients inside the food",
         meta="Commercial foundations today · 2026–2032 expansion · High confidence in incremental adoption",
         summary="More manufacturers could tailor sweetness, texture and functionality during processing; suppliers sell a process recipe with the enzyme.",
         evidence="IFF’s NURICA demonstrates in-situ conversion of lactose-derived sugars into galactooligosaccharides, rather than only adding a separate fibre ingredient.",
         change="More manufacturers could tailor sweetness, texture and functionality during processing. Ingredient suppliers increasingly sell a process recipe with the enzyme.",
         example="A dairy plant develops a reduced-sugar yoghurt using controlled enzyme treatment, then adjusts culture and flavour. The opportunity is lower formulation complexity and a differentiated nutritional profile.",
         status="Time, temperature, side reactions and enzyme inactivation affect output. Fibre recognition and label claims need market-specific verification.",
         notes=["This differs from precision fermentation: the value arises by converting the food matrix during processing rather than manufacturing and purifying a target molecule in a separate microbial process. NURICA is a supplier-provided commercial example.",
                "Claimed sugar reduction and fibre content vary with substrate, recipe and process, so no universal percentage is assumed. Changes in sweetness and fermentation kinetics require sensory and production validation."],
         sources=["S18"]),
    dict(slug="food-structure", kind="Technology", n=4,
         title="Food structure controls texture and flavour",
         meta="Established platforms, emerging applications · 2028–2036 · Medium confidence in adoption breadth",
         summary="Microgels, emulsions and encapsulation could recover creaminess with less fat, control flavour release or protect sensitive aromas.",
         evidence="Research by Sarkar and colleagues shows plant-protein microgels can improve lubrication. McClements’ work connects colloidal structure with texture and delivery.",
         change="Microgels, emulsions and encapsulation could recover creaminess or control flavour release with less fat, or protect sensitive aromas in difficult recipes.",
         example="A sauce developer combines protein microgels with an aroma system to test a creamy, lower-fat product. A beverage team protects citrus aroma through processing and storage.",
         status="Bench-scale lubrication is not proof of consumer acceptance. Heat, acidity, shear, shelf life and regulatory classification determine viable applications.",
         notes=["Kew et al. demonstrated microgel lubrication in experimental systems. The commercial product applications here are hypothetical development briefs, not claims that identical products exist or that sensory equivalence is proven.",
                "Microencapsulation and emulsions already exist; the disruption is broader precision in joint texture and flavour design. Not every microstructure is an engineered nanomaterial, but relevant novel-food/nanomaterial rules must be evaluated when applicable."],
         sources=["S03", "S05", "S20"]),
    dict(slug="side-streams", kind="Technology", n=5,
         title="Useful ingredients from food side streams",
         meta="Commercial examples today · 2026–2036 · Medium-high confidence in selective expansion",
         summary="Improved separation and processing could recover more fibre, protein and flavour value from food-production side streams.",
         evidence="NUTRAVA Citrus Fiber uses peels from the juice industry and offers functional applications such as texturising and stabilisation.",
         change="Improved separation, fractionation and processing could recover more fibre, protein and flavour value from food-production side streams.",
         example="A regional juice processor sells qualified citrus fibre to beverage and sauce makers. Buyers assess stability and taste alongside cost. Local processing can reduce disposal and create a new revenue stream.",
         status="Drying and transport can erase savings. Variability, residues, allergens, microbial safety and reliable feedstock volumes require control.",
         notes=["Upcycling is not new. The prospective disruption is systematic recovery of useful functional fractions at repeatable specifications and competitive delivered cost. NUTRAVA demonstrates one existing route, while broader multiproduct biorefinery adoption is a scenario.",
                "Avoid assuming that “waste” is free or that every upcycled ingredient has a lower lifecycle impact. Compare with the current use of the side stream, such as animal feed, and account for displaced functions."],
         sources=["S19"]),
]

# ---------------------------------------------------------------- Scenarios page (slides 3, 4)
EXPERTS = [
    ("Pierre Wack / Peter Schwartz", "Separate durable forces from uncertainties", "Four contrasting futures and early signals"),
    ("David Julian McClements", "Connect food structure to sensory performance", "A functional view of future ingredients"),
    ("Kevin Verstrepen and colleagues", "Link chemistry and sensory data to consumer response", "AI opportunities and limits"),
    ("Anwesha Sarkar and colleagues", "Test mouthfeel as a physical property", "Texture and fat-replacement scenarios"),
]
EXPERTS_NOTE = "These are selected, relevant authorities rather than an objective ranking of the world’s “best” experts. Published methods and research inform the analysis. No expert was interviewed or asked to endorse it. Supplier material demonstrates availability or stated capability, not independently verified superiority."
MATRIX = dict(
    cols=("More aligned regulation", "More fragmented regulation"),
    rows=("Fast technology scale-up", "Selective / slow scale-up"),
    cells=[[("Open innovation", "Shared evidence standards support wider launches. Platforms scale across regions.", False),
            ("Regional innovation", "Strong technology, but distinct recipes and approval portfolios by market.", False)],
           [("Efficient reformulation", "Enzymes, conventional ingredients and shared dossiers deliver most gains.", False),
            ("Verified regional systems", "Central planning scenario: regional recipes, proven technology and resilient sourcing.", True)]],
    note="This matrix is an original scenario artefact inspired by Shell-style uncertainty framing. The central planning case is chosen for robustness, not assigned a probability. Regulatory alignment concerns acceptance of evidence and approvals, not whether rules are weak or strong. Across all four futures, taste, cost-in-use, reliable supply and credible evidence remain useful investment priorities.",
)

# ---------------------------------------------------------------- Impact page (slides 15–18)
FLAVOURS = [
    ("Less sugar or sodium", "A complete taste system with masking, aroma and mouthfeel support", "Consumer liking at the target nutrient level"),
    ("Variable protein source", "A validated flavour system for more than one base recipe", "Performance after real processing and storage"),
    ("Scarce botanical supply", "Qualified source substitutions and alternative aroma routes", "Taste consistency, legal label and supply assurance"),
    ("Stricter evidence demands", "Documentation tied to each formula version and intended use", "Faster customer qualification and fewer relaunches"),
]
FLAVOURS_NOTE = "Commercial model inference: suppliers may earn development fees, licence proprietary systems or bundle services into ingredient pricing. Open ingredient catalogues remain relevant, but application data and trusted dossiers can increase switching costs. Risks include customer demands for data portability, commoditisation of basic AI tools and margin pressure from procurement. Premium origin-based extracts can coexist with biomanufactured molecules."
BRIEFS = [
    ("Citrus soft drink", "Target: 4 g sugar/100 ml", "Approved sweetener blend, acidity balance, citrus aroma and body adjustment", "Multi-market recipes. Validate preservation, liking and shelf life."),
    ("Creamy protein dessert", "Target: 15 g protein/serving", "Permitted plant or fermentation protein, texture system and bitterness control", "Regional protein choices. Validate allergens, heat stability and repeat purchase."),
    ("Smoky savoury snack", "Target: 20% less sodium than its reference", "Compliant flavour system, seasoning distribution and saltiness enhancement", "Requalify seasoning and label. Confirm taste and process consistency."),
]
BRIEFS_NOTE = "Fictional development briefs. Targets illustrate the scenario and are not validated recipes or health claims, nor recommendations for consumer diets. Soft-drink tax exposure depends on jurisdiction, recipe and future law, not the 4 g target alone. Protein permission, naming and allergen status are ingredient-specific. The sodium reference must be defined before making a comparative claim."
SEGMENTS = [
    ("Beverages", "Sweetness systems, aroma protection and stable colours", "More sensory work. Market-specific recipes."),
    ("Dairy and alternatives", "Proteins, cultures, enzymes and texture systems", "New process controls and allergen segregation."),
    ("Snacks, sauces and meals", "Sodium-reduction systems and replacement flavours", "Seasoning requalification and shelf-life checks."),
    ("Bakery and confectionery", "Functional fibres, fat systems and resilient cocoa sourcing", "Redesign texture and moisture control."),
    ("Ingredient manufacturers", "Application expertise, evidence services and qualified substitutes", "Higher data and compliance costs. More value in integrated systems."),
]
SEGMENTS_NOTE = "Directional market analysis, not a measured demand forecast. Likely relative winners include suppliers that combine sensory expertise with regulatory evidence, efficient bioprocess developers with contracted demand and functional-fraction producers close to feedstock. Pressure increases on undifferentiated intermediaries and products whose claims or composition cannot withstand scrutiny. Consumer affordability can still overwhelm technically superior propositions."
BUSINESS_CASE = [
    ("Sugar: 8 to 4 g/100 ml", "40 g/L less × 100m L = 4m kg. Assumed sugar price £0.60/kg", "£2.4m saving", False),
    ("Added sweetener, flavour and body system", "Assumed £0.04/L × 100m L", "£4.0m added cost", False),
    ("Tax avoided, if eligible", "Assumed £0.20/L × 100m L", "£20.0m saving", False),
    ("Recurring net benefit with assumed tax", "£2.4m − £4.0m + £20.0m", "£18.4m benefit", True),
    ("Recurring result without tax avoidance", "£2.4m − £4.0m", "£1.6m added cost", True),
]
BUSINESS_CASE_NOTE = "Illustrative annual model of 100 million litres. Every price and cost is an assumption, not a forecast. Assumes unchanged sales and full tax benefit; excludes one-off costs. The assumed £0.20/L is hypothetical: it is not the current UK rate or a prediction of the 2036 rate. The break-even avoided levy at unchanged sales is £0.016/L before one-off costs (£1.6m/100m L). This case shows why total cost-in-use and regulation can matter more than ingredient price per kg."

# ---------------------------------------------------------------- Strategy page (slides 19–21)
ROADMAP = [
    ("2026–2028", "Map exposure and claims. Qualify priority replacements.", "Legal pathway, owner and fallback for each ingredient."),
    ("2028–2031", "Pilot AI, enzymes and texture systems in customer products.", "Consumer liking, shelf life and positive cost-in-use case."),
    ("2031–2033", "Scale qualified biomanufacturing and side-stream partnerships.", "Repeatable commercial batches. Contracted demand supports cost."),
    ("2033–2036", "Expand successful systems. Maintain alternative recipes.", "Margin, resilient supply and consumer preference."),
]
ROADMAP_NOTE = "Backcasting from the central scenario: proposed management gates, not industry benchmarks. R&D, regulatory affairs, procurement and marketing need a shared recipe-and-evidence record with controlled access. Do not buy a large fermentation plant solely because a molecule works in the lab. Set capital gates around customer-qualified batches, downstream recovery, audited full costs and demand commitments. Review the scenario at least annually and after major rule changes."
SIGNALS = [
    ("Approval timelines converge across regions", "The open-innovation scenario becomes more plausible", "Accelerate cross-market platforms and joint dossiers."),
    ("Commercial fermentation cost misses customer targets", "Biotechnology remains selective", "Keep capacity flexible. Focus on high-value ingredients."),
    ("Repeat purchase falls despite good laboratory results", "Consumer trust or experience is the bottleneck", "Rework taste, price or positioning before expanding."),
    ("Processing-based food rules tighten sharply", "Some advanced ingredients face new access or perception risk", "Maintain simpler recipes and finished-food evidence."),
    ("Climate or trade shocks disrupt a key crop", "Supply resilience outweighs lowest spot price", "Activate qualified substitutions and diversify origins."),
]
SIGNALS_NOTE = "Wildcards are not base-case predictions. Individualised microbiome foods, broad cultivated-meat displacement and autonomous AI food approval are excluded from the central case because evidence, economics or regulation remain too uncertain. A universal ultra-processed-food tax is not assumed."
CHOICE = dict(
    headline="Build the capability to reformulate without losing the consumer.",
    commit="Sensory data, sound ingredient dossiers, qualified replacement recipes and application teams that work with manufacturing.",
    scale="Fermentation capacity, specialised delivery systems and side-stream processing that meet a real customer’s cost and performance requirements.",
    advantage="The likely 2036 advantage: better taste under tighter constraints, delivered reliably and supported by evidence.",
    note="Final synthesis is analyst judgment. Rankings reflect expected breadth of exposure, magnitude of recipe or cost disruption and persistence through 2036. They are ordinal strategic priorities, not quantified probabilities. No expert or supplier named on this site endorses these forecasts.",
)

# ---------------------------------------------------------------- Consumer page (2036_fb.docx)
CONSUMER = dict(
    intro=["In 2036, people are likely to pay for food that feels made for them, delivers an exceptional experience, and helps them participate in occasions they value. Health can strengthen that proposition, but the immediate reward will usually remain taste, convenience, confidence or social connection.",
           "The change from today could be how precisely and conveniently those benefits are delivered. These are plausible scenarios, not predictions of guaranteed demand."],
    table=[
        ("“My perfect taste”", "A café remembers your preferred sweetness, aroma, temperature and texture, then makes a lower-sugar drink you genuinely enjoy", "Immediate: it tastes right. Social: a recognisable personal order and ritual", "AI translates preferences into recipes; flavours, sweeteners and texture systems make them work"),
        ("Indulgence with fewer compromises", "A rich, creamy dessert delivers a useful amount of protein or fibre without an obvious sensory penalty", "Immediate: pleasure. Visible: appetising presentation. Social: everyone enjoys the same dessert", "Better proteins, emulsions, fibres and flavour systems; nutritional claims remain evidence-dependent"),
        ("One occasion that includes everyone", "A family orders one shared dinner, with coordinated versions accommodating different dietary requirements and preferences", "Immediate: less planning. Social: everyone participates without receiving a visibly inferior substitute", "Modular formulations, verified ingredient information and dependable kitchen controls"),
        ("A meal that removes the work", "A household service learns its budget and preferences, provides suitable meals and adapts quantities to reduce leftovers", "Immediate: time and decisions saved. Visible: an attractive meal ready when needed", "AI planning, convenient preparation, stable ingredients and reliable reheating performance"),
        ("Experiences worth sharing", "A dessert is finished at the table with contrasting textures, changing aromas or a personalised visual design", "Immediate: surprise and enjoyment. Social: entertainment, conversation and memories", "Controlled flavour release, texture engineering and on-demand preparation"),
        ("Membership in a food community", "A local café or creator releases seasonal flavours that customers help choose, with tastings and member events", "Immediate: discovery. Social: belonging, recognition and participation", "Faster small-batch development, flavour libraries and production flexibility"),
        ("A gift that visibly expresses care", "A personalised chocolate or celebration cake reflects the recipient’s tastes, cultural preferences and relevant dietary requirements", "Visible: the thought behind the gift. Social: generosity and connection", "Custom flavour combinations, flexible production and verified suitability"),
        ("Credible craftsmanship and origin", "A premium food combines excellent taste with a convincing, verifiable story about its producer, place or production method", "Immediate: quality. Social: discernment and a story to share", "Ingredient quality and traceability; digital information supports the experience rather than replacing it"),
    ],
    breakfast=["It is ready when you arrive.", "The drink has your preferred flavour and sweetness.", "The food provides a clearly specified nutritional contribution.",
               "It looks and tastes like something you would choose for pleasure.", "You can enjoy it with colleagues without explaining a complicated diet.",
               "The total price remains acceptable compared with your usual breakfast."],
    breakfast_close="The customer pays for a breakfast that fits their life. The ingredient supplier enables that experience through taste, texture, nutrition and consistency. A wearable could contribute information where useful, but owning one need not be a condition of purchase.",
    split=[("Choosing among a few well-designed recipes", "A highly customised recipe or preparation"),
           ("Preferences remembered automatically", "Special consultations or testing where justified"),
           ("Familiar food at a competitive price", "Exclusive flavours, craftsmanship and theatrical service"),
           ("Convenience is the main reward", "Experience, recognition and exclusivity justify the premium")],
    split_close="An AI recommendation may become commonplace. The scarce value could be the ability to deliver the recommended food deliciously, consistently and conveniently.",
    sceptical=["“AI-created” without a noticeable improvement.", "“Personalised” when the recommendation is generic.", "“Longevity food” with an expensive but uncertain promise.",
               "A subscription requiring constant tracking and effort.", "An attractive health score that does not establish a meaningful benefit."],
    proposition="We make desirable experiences possible while improving the nutritional formulation.",
    proposition_close="Consumers may pay the brand or restaurant for the experience; manufacturers then pay ingredient suppliers for the capabilities that deliver it.",
    evidence_note="The evidence anchors are today’s findings on experience, social dining and experimentally demonstrated AI-assisted flavour development. They support the mechanisms above, not the specific 2036 outcomes.",
    sources=["C1", "C2", "S04"],
)
