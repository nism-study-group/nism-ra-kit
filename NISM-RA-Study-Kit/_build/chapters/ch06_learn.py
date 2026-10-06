LEARN = r"""
<style>
.porter{display:grid;grid-template-columns:1fr 1.2fr 1fr;grid-template-rows:auto auto auto;gap:10px;align-items:stretch}
.porter .box{display:flex;flex-direction:column;justify-content:center;text-align:center}
.porter .c{grid-column:2;grid-row:2;border:2px solid var(--brick);background:var(--brick-soft)}
.porter .t{grid-column:2;grid-row:1}.porter .b{grid-column:2;grid-row:3}
.porter .l{grid-column:1;grid-row:2}.porter .r{grid-column:3;grid-row:2}
.porter .v{border-color:var(--indigo);background:var(--indigo-soft)}
.porter .h{border-color:var(--teal);background:var(--teal-soft)}
@media (max-width:560px){.porter{grid-template-columns:1fr}.porter .box{grid-column:1!important;grid-row:auto!important}}
.bcg{display:grid;grid-template-columns:2rem 1fr 1fr;grid-template-rows:1fr 1fr 2rem;gap:10px}
.bcg .ax{font-family:var(--head);font-weight:700;color:var(--muted);font-size:.85rem;display:flex;align-items:center;justify-content:center}
.bcg .ay{writing-mode:vertical-rl;transform:rotate(180deg);grid-row:1/3}
.bcg .axx{grid-column:2/4}
.bcg .box h4{font-size:1.1rem}
</style>
<div class="wrap">
<header class="hero">
<div class="kicker">Chapter 6 of 15</div>
<h1>Industry analysis</h1>
<div class="meta"><span class="pill">Worth <b>8 marks</b> of 100</span><span class="pill">Book pages 105 to 129</span><span class="pill">About 60 minutes</span></div>
<p class="oneline">A great captain cannot save a leaking boat. Study the <span class="k">industry</span> before the company: its <span class="k">cycles</span>, its <span class="k">competition</span> and its <span class="k">rules</span>.</p>
</header>

<figure class="fig" id="fig-map"><figcaption>Chapter map<span>Ten parts. 6.6 (four frameworks) and 6.7 (KPIs) carry the most detail. Tap to jump.</span></figcaption>
<div class="map">
<a href="#s1"><b>6.1 and 6.2</b><span>What is "the industry"?</span><small>Role, definitions, GICS</small></a>
<a href="#s3"><b>6.3</b><span>How cyclical?</span><small>Defensive, semi, deep</small></a>
<a href="#s4"><b>6.4</b><span>How big?</span><small>Top-down and bottom-up sizing</small></a>
<a href="#s5"><b>6.5</b><span>Long-term shifts</span><small>Secular trends, value migration, life cycle</small></a>
<a href="#s6"><b>6.6</b><span>Four frameworks</span><small>Porter, PESTLE, BCG, SCP</small></a>
<a href="#s7"><b>6.7</b><span>What to measure</span><small>Unit of pricing, constraints, KPIs</small></a>
<a href="#s8"><b>6.8 and 6.9</b><span>Rules and taxes</span><small>Regulation, direct and indirect tax</small></a>
<a href="#s10"><b>6.10</b><span>Where to find data</span><small>Four sources</small></a>
</div></figure>

<div class="col">
<section class="sec" id="s1"><span class="secno">6.1</span><h2>Why study the industry?</h2>
<p>Economic analysis (Chapter 5) asks whether the economy will grow. <span class="k">Industry analysis</span> asks how each industry will be affected by that economy, and how the players in it will react.</p>
<dl class="terms">
<dt>Industry</dt><dd>Firms offering the same or similar products for the same customer need. Examples: auto, insurance, steel, telecom.</dd>
<dt>Business sector</dt><dd>A broader group of related industries. Financial services = insurance, banking, credit rating, investment banking. Industrial metals = steel, copper, aluminium.</dd>
<dt>Economic sector</dt><dd>Parts of the economy that add to national income: agriculture, manufacturing, public utilities, services.</dd>
</dl>
<p>Seven questions every industry analysis must answer:</p>
<ol>
<li>Which industry is the company in?</li>
<li>How much do economic cycles affect it?</li>
<li>How big can it get?</li>
<li>How has it done in the past, and why?</li>
<li>How strong is competition, and how does that affect pricing power?</li>
<li>Which secular trends affect it, and are they causing value migration?</li>
<li>Are there regulatory headwinds or tailwinds?</li>
</ol>

<h3 id="s2">6.2 Defining the industry</h3>
<p>This is the first step, and it is not always easy. Standard systems exist: <b>NIC</b> (National Industry Classification) in India, <b>GICS</b> (Global Industry Classification Standard), and <b>NAICS</b> (North American Industry Classification System) in the US. But they may miss the real substance.</p>
</div>

<figure class="fig" id="fig-define"><figcaption>Three examples of the definition problem</figcaption>
<div class="grid g3">
<div class="box"><span class="tag">Too broad</span><h4>Cars</h4><p>NIC puts every passenger car maker in one class. But entry-level cars and luxury cars behave very differently. Analysts may treat them as separate industries.</p></div>
<div class="box"><span class="tag">Too narrow?</span><h4>PVR cinemas</h4><p>Competes with OTT platforms and TV, and also with live theatre and sport. Call it only a "cinema exhibitor" and you miss rivals. Call it "media and entertainment" and the peers are not comparable.</p></div>
<div class="box"><span class="tag">Moving target</span><h4>Cameras</h4><p>Phone cameras took sales from entry-level, then mid-tier cameras. Treat cameras as a standalone industry and you ignore the biggest competitor.</p></div>
</div></figure>

<div class="col">
<div class="why"><b>The book's rule</b>Group a company with others that share the <b>same driving factors</b>. If PVR's business depends on people's wish to spend time out of home, put it in out-of-home entertainment. If it depends on people's wish to watch movie content, put it in entertainment media. This choice matters later, when you pick peers and compare valuations.</div>
<p><b>GICS</b> is widely used by global investors. It has four tiers: sectors, industry groups, industries and sub-industries. As of March 2023 (source MSCI): <span class="num">11</span> sectors, <span class="num">25</span> industry groups, <span class="num">74</span> industries, <span class="num">163</span> sub-industries.</p>
</section>

<section class="sec" id="s3"><span class="secno">6.3</span><h2>How cyclical is the industry?</h2>
<p>Economic cycles affect every business, but some far more than others.</p>
</div>

<figure class="fig" id="fig-cyclical"><figcaption>Three kinds of industry by cyclicality</figcaption>
<div class="grid g3">
<div class="box gd"><span class="tag">Defensive</span><h4>Barely moves</h4><p>Low <b>income elasticity</b>: demand hardly changes when income rises or falls. Affected mainly by secular trends.</p><p><b>Examples:</b> food, agricultural inputs, healthcare.</p></div>
<div class="box"><span class="tag">Semi-cyclical</span><h4>Moves, with a floor</h4><p>Grows in expansion, falls in recession, but keeps a base level of demand.</p><p><b>Example:</b> consumer durables.</p></div>
<div class="box bd"><span class="tag">Deep cyclical</span><h4>Swings hard</h4><p>Driven by economic and commodity cycles. Sales collapse in recession as firms freeze expansion, then surge at the first sign of recovery from pent-up orders.</p><p><b>Examples:</b> capital goods, steel.</p></div>
</div></figure>

<div class="col">
<div class="analogy">Income elasticity is how much you cut back when money is tight. You still buy rice and medicine (defensive). You delay a new fridge (semi-cyclical). A factory delays a new machine altogether (deep cyclical).</div>
</section>

<section class="sec" id="s4"><span class="secno">6.4</span><h2>How big is the market?</h2>
<p>An <b>under-penetrated</b> industry has room to grow. As it matures, growth slows. So analysts estimate both the <b>current</b> and the <b>potential</b> market size. Both are hard: unorganised and private players do not publish data, and potential size rests on assumptions that may be wrong. Past trends help fill the gaps and reveal secular trends.</p>
</div>

<figure class="fig" id="fig-sizing"><figcaption>Two ways to size a market<span>The book's example: a medical therapy</span></figcaption>
<div class="grid g2">
<div class="box hl"><span class="tag">Top-down</span><h4>Start from the big picture</h4><p>Start from macro factors and work down to the industry.</p><p>Number of patients who had the therapy &times; average spend per patient = industry revenue.</p></div>
<div class="box hl"><span class="tag">Bottom-up</span><h4>Start from the companies</h4><p>Add up data from individual companies.</p><p>For each hospital offering the therapy, take the revenue from it. Add them all.</p></div>
</div></figure>

<div class="col">
<div class="why"><b>Book sample question, worked</b>Three organised tyre makers earn Rs 6,000, 8,000 and 10,000 crore = <b>Rs 24,000 crore</b>. Unorganised players make about 20% of sales, so organised = 80%. Market size = 24,000 &divide; 0.8 = <span class="num">Rs 30,000 crore</span>.</div>
</section>

<section class="sec" id="s5"><span class="secno">6.5</span><h2>Long-term shifts</h2>
<p><span class="k">Secular trends</span> are long-term changes in what is made or consumed (Chapter 5). The book names five drivers:</p>
</div>

<figure class="fig" id="fig-secular"><figcaption>Five drivers of secular trends, with the book's examples</figcaption>
<div class="grid g2">
<div class="box"><span class="tag">Technology</span><ul><li>Horizontal drilling opened up shale gas, lowering long-term oil and gas prices</li><li>Digital cameras killed film rolls; phone cameras hit entry-level digital cameras</li><li>Better batteries are driving electric vehicles</li></ul></div>
<div class="box"><span class="tag">Income</span><p>As incomes rise, people shift to premium products.</p></div>
<div class="box"><span class="tag">Demography</span><p>Japan's ageing population cut per capita beer consumption.</p></div>
<div class="box"><span class="tag">Culture and tastes</span><p>Western influence raised demand for western clothing in Asia. Change can be sudden, as after a pandemic.</p></div>
<div class="box"><span class="tag">Regulation</span><p>GST made logistics more efficient, which reduced demand for new commercial vehicles.</p></div>
</div></figure>

<div class="col">
<h3>6.5.1 Value migration</h3>
<p>When a secular trend gives one party a lasting advantage at another's cost, <span class="k">shareholder value migrates</span> from loser to winner. Spotting it early helps analysts get in ahead of time and get out of losing businesses.</p>
</div>

<figure class="fig" id="fig-migration"><figcaption>Four kinds of value migration</figcaption>
<div class="grid g2">
<div class="box"><span class="tag">Across geographies</span><p>Shale gas moved value to <b>US</b> oil exploration. Globalisation helped low-cost <b>China</b> grow.</p></div>
<div class="box"><span class="tag">Across industries</span><p>Digital cameras crushed the film roll industry; <b>Kodak</b> had to shut down.</p></div>
<div class="box"><span class="tag">Across the value chain</span><p>Fierce competition cut Indian <b>telecom</b> prices and telecom shareholder value, but cheap data boosted <b>digital content</b> providers.</p></div>
<div class="box"><span class="tag">Across companies</span><p><b>Blackberry</b> led corporate mobile email. With 2G, rivals like <b>Apple</b> offered the same and took the value. (The least common of the four.)</p></div>
</div></figure>

<div class="col">
<h3>6.5.2 Business life cycle</h3>
</div>

<figure class="fig" id="fig-lifecycle"><figcaption>Five stages of an industry's life</figcaption>
<div class="flow">
<div class="step"><h4>Pioneering</h4><p>Just taking shape. Concept being proven.</p></div><div class="arrow"></div>
<div class="step gd"><h4>Growth</h4><p>Concept works. Customers adopt. Steep growth.</p></div><div class="arrow"></div>
<div class="step"><h4>Mature</h4><p>Most possible users already use it. Few new customers.</p></div><div class="arrow"></div>
<div class="step bd"><h4>Declining</h4><p>New technology or tastes replace it.</p></div><div class="arrow"></div>
<div class="step hl"><h4>Reinvention</h4><p>Rare: finds a new use and starts again.</p></div>
</div></figure>

<div class="col">
<p><b>The book's Indian example: call taxis.</b> They took shape around the turn of the century, grew fast for a decade on the back of more phones and rising income, then shrank sharply when app-based aggregators arrived.</p>
<p>Each shift displaces workers, who must reskill, and capacity, which must find a new use. Not every disruptor causes displacement, though: shale gas lowered crude prices for the long term without changing what people consumed.</p>
<div class="trap">Secular trends tell you the <b>long-term</b> path. For the medium and short term, study <b>cyclical</b> trends.</div>
</section>

<section class="sec" id="s6"><span class="secno">6.6</span><h2>Four frameworks for the industry landscape</h2>
<p><b>Industry landscaping</b> means studying all the players and how they interact: competitors, customers, suppliers, regulators and new technology. Low competition lets firms pass cost increases to customers and keep margins. High competition squeezes prices and profits. Four established frameworks help:</p>
</div>

<figure class="fig" id="fig-porter"><figcaption>6.6.1 Porter's five forces<span>Michael Porter, 1979. Laid out the way the book classifies them.</span></figcaption>
<div class="porter">
<div class="box v t"><span class="tag">Vertical</span><h4>Bargaining power of suppliers</h4></div>
<div class="box h l"><span class="tag">Horizontal</span><h4>Threat of new entrants</h4></div>
<div class="box c"><h4>Industry rivalry</h4><p class="ptr">Threat of established rivals (horizontal)</p></div>
<div class="box h r"><span class="tag">Horizontal</span><h4>Threat of substitutes</h4></div>
<div class="box v b"><span class="tag">Vertical</span><h4>Bargaining power of buyers</h4></div>
</div>
<p class="ptr" style="margin-top:8px">The book: 3 horizontal forces (substitutes, new entrants, established rivals) and 2 vertical forces (suppliers, customers).</p>
</figure>

<div class="col">
<div class="grid g2">
<div class="box bd"><h4>Unattractive for owners (book)</h4><p>Aviation, telecom, retail, textile, sugar, power. The forces keep profits low.</p></div>
<div class="box gd"><h4>Attractive for owners (book)</h4><p>Education, FMCG, healthcare, IT. Weak forces, high margins for long periods.</p></div>
</div>
<div class="analogy">Warren Buffett, quoted in the book: "Should you find yourself in a chronically leaking boat, energy devoted to changing vessels is likely to be more productive than energy devoted to patching leaks." And: when brilliant management takes on a business with bad economics, "it is the reputation of the business that remains intact."</div>
</div>

<figure class="fig" id="fig-forces"><figcaption>When is each force strong?<span>The book's checklist</span></figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Force</th><th>High when...</th><th>Book examples</th></tr></thead>
<tbody>
<tr><th>Industry rivalry</th><td>Many companies; little differentiation; everyone competes on price or credit; low switching cost</td><td>Aviation, Indian telecom. Munger: "If only basis of competition in an industry is pricing, it is a self-defeating business." Micromax won 10% share in 3 years with special features at low prices.</td></tr>
<tr><th>Threat of substitutes</th><td>Substitute is as good or better (quality, price, ease); low switching cost</td><td>Telegram to SMS; cement pipes to steel and plastic; typewriters to computers; Kodak. No substitute threat: power, healthcare, education. Solar and LED are slow because of upfront cost.</td></tr>
<tr><th>Buyer power</th><td>Strong competition among sellers; standard products; close substitutes with low switching cost</td><td>Large buyers such as the government have more power</td></tr>
<tr><th>Supplier power</th><td>Few suppliers, many buyers; critical inputs; low competition with differentiation; no substitutes; high switching cost</td><td>Sugarcane price set by government with farmers; OPEC and crude oil; hospitals and schools (you rarely bargain) versus the vegetable seller (you always do)</td></tr>
<tr><th>Threat of new entrants</th><td>Low barriers. Barriers are high with licensing, patents, huge specialised investment, strong brands, distribution and loyalty</td><td>Skills (IT), capital (oil and gas), distribution (banking), brand loyalty (toothpaste, coffee). Buffett: "economic castles protected by unbreachable moats"</td></tr>
</tbody></table></div></figure>

<div class="col">
<div class="why"><b>How to win in a crowded industry</b>Innovate. Internally: efficient operations, less working capital, faster turnaround, lower cost of capital. Externally: differentiated products, strong brands, unique positioning.</div>
<h3>The attractive industry, in five features</h3>
<p>Low competition, high barriers to entry, weak supplier power, weak buyer power, few substitutes. Such an industry has strong <b>pricing power</b> and high margins.</p>
<p><b>The book's example: education in India.</b> Demand is large and growing; students have little bargaining power; it is largely recession-proof; opening an institute needs many permissions (high barriers); quality institutes are few (low competition); teachers' salaries are set by management (weak suppliers); alternative courses lack credibility (few substitutes).</p>

<h3>6.6.2 PESTLE analysis</h3>
<p><b>P</b>olitical, <b>E</b>conomic, <b>S</b>ocio-cultural, <b>T</b>echnological, <b>L</b>egal and <b>E</b>nvironmental. Adding <b>E</b>thics and <b>D</b>emographics gives <span class="k">STEEPLED</span>. It looks at the <b>external</b> environment, mostly from the view of a business choosing which country to set up a unit in.</p>
</div>

<figure class="fig" id="fig-pestle"><figcaption>PESTLE: what investors look at in a country</figcaption>
<div class="grid g3">
<div class="box"><span class="tag">Political</span><p>Stable laws and policy, little corruption and red tape, press freedom, ease of doing business, healthy public finances.</p></div>
<div class="box"><span class="tag">Economic</span><p>GDP growth, inflation, rates, trade mix, BoP, currency stability, forex reserves, monetary policy, dependence on imported resources like oil.</p></div>
<div class="box"><span class="tag">Socio-cultural</span><p>Age, education, health, values, lifestyle. Young India versus ageing Japan. Nuclear families raise demand for day care and packaged food.</p></div>
<div class="box"><span class="tag">Technological</span><p>R&amp;D push, tech-savvy people and institutions, scientific temper.</p></div>
<div class="box"><span class="tag">Legal</span><p>Consistent, transparent, enforced laws. Book examples of discomfort: Vodafone retrospective tax, cancelled telecom and mining licences.</p></div>
<div class="box"><span class="tag">Environmental</span><p>Clear policy on pollution, waste, mining, forests, rehabilitation. Unclear rules deter manufacturers.</p></div>
</div>
<p class="ptr" style="margin-top:8px">Not every factor matters equally to every company. Judge each factor's weight for the business.</p>
</figure>

<div class="col">
<h3>6.6.3 BCG matrix</h3>
<p>Developed by the Boston Consulting Group. Unlike Porter and PESTLE, which look at industries and countries, BCG looks at the <b>segments within one business</b>, as a portfolio, through market growth and cash generation.</p>
</div>

<figure class="fig" id="fig-bcg"><figcaption>BCG matrix<span>With the book's Indian examples</span></figcaption>
<div class="bcg">
<div class="ax ay">Market growth: high (top) to low (bottom)</div>
<div class="box gd"><span class="tag">High growth, high share</span><h4>Star</h4><p>Rising cash generation over time.</p><p><b>Cera Sanitaryware</b></p></div>
<div class="box"><span class="tag">High growth, low share</span><h4>Question mark</h4><p>Could grow with the right strategy, but may eat cash and fail.</p><p><b>Tata Nano</b> (failed), <b>Bajaj Pulsar</b> (succeeded)</p></div>
<div class="box hl"><span class="tag">Low growth, high share</span><h4>Cash cow</h4><p>Little investment needed, steady cash.</p><p><b>Navneet Publications</b>, <b>Colgate</b></p></div>
<div class="box bd"><span class="tag">Low growth, low share</span><h4>Dog</h4><p>Slow growth, tough competition, little cash.</p></div>
<div></div><div class="ax axx">Market share: high (left) to low (right)</div>
</div></figure>

<div class="col">
<h3>6.6.4 Structure, Conduct, Performance (SCP)</h3>
<p>Can be seen as an extension of Porter's model that also looks at the financial results.</p>
</div>

<figure class="fig" id="fig-scp"><figcaption>SCP in three steps</figcaption>
<div class="flow">
<div class="step"><h4>Structure</h4><p>Number of players (monopoly, oligopoly), concentration, organised versus unorganised, substitutes, supplier and buyer equations, market size, growth, integration. Overlaps Porter and SWOT.</p></div><div class="arrow"></div>
<div class="step"><h4>Conduct</h4><p>Behaviour that follows: commoditised or branded, seasonal (umbrellas) or year-round (FMCG, pharma), cyclical, skill needs, dependence on policy.</p></div><div class="arrow"></div>
<div class="step gd"><h4>Performance</h4><p>Financial result: RoE, RoIC, WACC. High return on capital creates wealth.</p></div>
</div></figure>

<div class="col">
<p class="ptr">Conduct example from the book: high interest rates may deter buyers of real estate and four-wheelers, but hit two-wheelers less.</p>
</section>

<section class="sec" id="s7"><span class="secno">6.7</span><h2>What to measure: industry KPIs</h2>
<p>Key performance indicators (KPIs) differ by industry. Revenue per employee suits a BPO, which bills by headcount, but tells little about a capital-heavy manufacturer. Company annual reports and management discussion show which KPIs an industry uses. Two more guides:</p>
<div class="grid g2">
<div class="box"><span class="tag">6.7.1</span><h4>Unit of pricing</h4><p>What the company treats as one unit when it sets a price. Easy for manufacturers (goods sold). Hard for services: a cafe like Starbucks prices on what it expects to earn per <b>patron</b>, not per cup.</p></div>
<div class="box"><span class="tag">6.7.2</span><h4>Key constraining factors</h4><p><b>Demand</b>, <b>supply</b> or <b>regulatory</b>. Limited market: track <b>penetration rate</b>. Limited capacity: track <b>capacity utilisation</b>. Regulated: track what the regulator tracks.</p></div>
</div>
</div>

<figure class="fig" id="fig-kpis"><figcaption>6.7.3 KPIs for select industries</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Industry</th><th>Unit of pricing and constraint</th><th>Key metrics</th></tr></thead>
<tbody>
<tr><th>Airlines, transport, logistics</th><td>Passengers or cargo &times; distance. Constraint: capacity</td><td>Passenger or cargo km; price per passenger or cargo km; capacity and occupancy rate</td></tr>
<tr><th>Autos, capital goods</th><td>Goods sold. Constraint: capacity</td><td>Volume and growth; average realisation and growth; capacity utilisation</td></tr>
<tr><th>Banks, NBFCs</th><td>Loan value, priced as interest. Constraints: deposits, regulatory capital, liquid assets, market liquidity</td><td>Net interest margin; capital adequacy; NPA ratio; deposit and loan growth; CRR and SLR; CASA ratio; central bank policy rates</td></tr>
<tr><th>Consumer goods</th><td>Goods sold. Durables: capacity in high growth</td><td>Volume and growth; average price and growth; capacity utilisation (durables)</td></tr>
<tr><th>IT services, BPO, KPO</th><td>Full-time equivalent (FTE) per month. Constraints: workforce, currency, few big clients</td><td>FTEs billed; revenue per FTE; bench strength and attrition; constant currency growth; customer concentration and "million dollar" clients</td></tr>
<tr><th>Media</th><td>Print: ad space. TV and radio: airtime. Online: views or clicks. Mostly ad revenue</td><td>Readership, viewership, TRPs, site visitors; ad realisation per unit; content acquisition cost</td></tr>
<tr><th>Retail</th><td>Unit of pricing less relevant (trading business). Constraint: store network</td><td>Number of stores; same-store sales growth</td></tr>
<tr><th>Telecom, internet</th><td>A subscriber. Constraint: market size limited by population</td><td>ARPU (average revenue per user); churn; subscriber acquisition cost; market share</td></tr>
</tbody></table></div></figure>

<div class="col">
<div class="trap">Match the KPI to the industry. CASA and NPA are bank metrics. ARPU and churn are telecom. Same-store sales growth is retail. Revenue per FTE and bench strength are IT services. Passenger km is airlines.</div>
</section>

<section class="sec" id="s8"><span class="secno">6.8</span><h2>The rules of the game</h2>
<p>Small changes in regulation can have big effects. The book's examples: the long debate on FDI in multi-brand retail (back-end investment, local sourcing), mine closures after environmental policy changes, cancelled telecom licences, and amendments to the Companies Act. Analysts must pay close attention to regulation.</p>

<h3 id="s9">6.9 Taxation</h3>
<p>Taxes raise money for the government, and also encourage or discourage businesses. Kerala's <b>fat tax</b> (2017) added <span class="num">14.5%</span> tax on junk food. GST charges essentials little or nothing and luxuries more.</p>
</div>

<figure class="fig" id="fig-tax"><figcaption>Direct versus indirect taxes</figcaption>
<div class="grid g2">
<div class="box hl"><span class="tag">6.9.1 Direct</span><h4>The payer bears it</h4><p>The person who bears the tax also pays it to the government. Main example: <b>income tax</b>.</p></div>
<div class="box"><span class="tag">6.9.2 Indirect</span><h4>Someone else collects it</h4><p>The seller collects it and pays the government; the <b>end consumer</b> bears it. Main example: <b>GST</b>.</p></div>
</div></figure>

<div class="col">
<h3>Direct tax: how it shapes behaviour</h3>
<ul>
<li>To promote research, companies can claim <span class="num">1.5 times</span> the actual spend on certain scientific research as an expense.</li>
<li>Interest owed to scheduled commercial banks is deductible only when <b>actually paid</b>, to discourage delays.</li>
<li>Such rules make tax profit differ from reported profit. This shows as a <b>deferred tax asset</b> (paying more tax now, less later) or a <b>deferred tax liability</b> (paying less now, more later).</li>
</ul>
<h3>Corporate income tax in India: four parts (as per the book)</h3>
</div>

<figure class="fig" id="fig-corptax"><figcaption>Income tax, MAT, surcharge, cess<span>Book figures, for assessment year 2025-26 where stated</span></figcaption>
<div class="grid g2">
<div class="box"><span class="tag">Income tax</span><p><b>30%</b> of taxable profit; <b>25%</b> if turnover was below Rs 400 crore. Optional schemes: <b>15% to 25%</b> if the company gives up certain deductions.</p></div>
<div class="box"><span class="tag">MAT</span><p>Minimum Alternate Tax. If normal tax is below <b>15% of book profits</b>, pay 15% of book profits + 4% cess + surcharge. The excess becomes <b>MAT credit</b> for future years.</p></div>
<div class="box"><span class="tag">Surcharge</span><p>A tax on tax. All goes to the <b>central</b> government, not shared with states. <b>12%</b> if income is above Rs 10 crore; <b>7%</b> from Rs 1 to 10 crore; nil below Rs 1 crore.</p></div>
<div class="box"><span class="tag">Cess</span><p>Levied on tax plus surcharge, and used only for its stated purpose. <b>4%</b> for health and education.</p></div>
</div>
<p class="ptr" style="margin-top:8px">Worked example: taxable profit Rs 100 crore at 30% = 30. Surcharge 12% of 30 = 3.6. Cess 4% of 33.6 = 1.344. Total about Rs 34.94 crore.</p>
</figure>

<div class="col">
<h3>Indirect taxes</h3>
<dl class="terms">
<dt>GST</dt><dd>Charged on the sale of goods and services as a % of invoice value. Sellers deduct GST paid to their suppliers (tax credit), so there is no double taxation. As per the book: most items at <b>18%</b>, range 0% to 28%.</dd>
<dt>Excise duty</dt><dd>Tax on production. Now only on <b>liquor, petrol and diesel</b>, which are outside GST.</dd>
<dt>VAT</dt><dd>Charged by <b>state</b> governments on sale. Also now only on liquor, petrol and diesel.</dd>
<dt>Customs duty</dt><dd>Tax on imports. Rate depends on the product.</dd>
</dl>
<h3>6.9.3 Other taxes and who they hit</h3>
<div class="grid g3">
<div class="box"><h4>Road tax</h4><p>Lifetime tax paid upfront on new vehicles. Hits auto sales, auto ancillaries, motor insurers.</p></div>
<div class="box"><h4>Stamp duty</h4><p>Paid when documents are registered, mostly on buying or selling assets. Hits real estate, brokers and AMCs.</p></div>
<div class="box"><h4>STT</h4><p>Securities Transaction Tax, paid on sale of securities. Discourages short-term trading. Hits traders and brokers.</p></div>
</div>
</section>

<section class="sec" id="s10"><span class="secno">6.10</span><h2>Where to find data</h2>
<div class="grid g2">
<div class="box"><h4>Industry reports</h4><p>Industry journals and media reports</p></div>
<div class="box"><h4>Annual reports</h4><p>The <b>Management Discussion and Analysis</b> section</p></div>
<div class="box"><h4>Associations and trade bodies</h4><p>Their publications</p></div>
<div class="box"><h4>Relevant ministry</h4><p>Websites and publications</p></div>
</div>
</section>

<section class="sec" id="traps"><h2>All exam traps in this chapter</h2>
<ol class="traplist">
<li>Industry: same need. Business sector: related industries. Economic sector: agriculture, manufacturing, utilities, services.</li>
<li>NIC is India's classification. NAICS is North America's. GICS: 11 sectors, 25 industry groups, 74 industries, 163 sub-industries.</li>
<li>Classify by common driving factors, not by product label.</li>
<li>Defensive: low income elasticity (food, agri inputs, healthcare). Semi-cyclical: consumer durables. Deep cyclical: capital goods, steel.</li>
<li>Top-down sizing starts from macro factors; bottom-up adds up companies.</li>
<li>Tyre sample: 24,000 is 80% of the market, so the market is 30,000.</li>
<li>Five secular drivers: technology, income, demography, culture, regulation.</li>
<li>Value migration: geography, industry, value chain, companies (least common).</li>
<li>Life cycle: pioneering, growth, mature, declining, reinvention. Call taxis went through it.</li>
<li>Porter (1979): 3 horizontal (substitutes, new entrants, rivals), 2 vertical (suppliers, buyers).</li>
<li>High rivalry means lower pricing power and lower incomes.</li>
<li>No substitute threat (book): power, healthcare, education.</li>
<li>Attractive industry: low competition, high barriers, weak suppliers, weak buyers, few substitutes.</li>
<li>PESTLE plus Ethics and Demographics = STEEPLED. Mostly used when choosing a country.</li>
<li>BCG looks at segments within a business. Star: Cera. Cash cow: Navneet, Colgate. Question mark: Nano (failed), Pulsar (succeeded).</li>
<li>SCP: structure, conduct, performance (RoE, RoIC, WACC). An extension of Porter.</li>
<li>Limited market: penetration rate. Limited capacity: utilisation rate.</li>
<li>Bank KPIs include NIM, CASA, NPA; telecom: ARPU, churn; retail: same-store sales; IT: revenue per FTE.</li>
<li>Direct tax: payer bears it. Indirect: consumer bears it, seller collects.</li>
<li>R&amp;D deduction: 1.5 times. MAT: 15% of book profits. Surcharge: 12% above Rs 10 crore, 7% from 1 to 10 crore. Cess: 4%.</li>
<li>Surcharge goes wholly to the centre. Cess is for a specific purpose.</li>
<li>Excise and VAT now only on liquor, petrol, diesel. STT discourages short-term trading.</li>
</ol>
</section>

<section class="sec" id="talk"><h2>For the group discussion</h2>
<ol class="talk">
<li>How would you define the industry for a food delivery app? Who are its real competitors?</li>
<li>Run Porter's five forces on Indian airlines. Why does the book call aviation unattractive?</li>
<li>Pick a company you know with several businesses. Place each in the BCG matrix.</li>
<li>Which KPI would you check first for a bank, a telecom company and a retailer? Why?</li>
<li>Name a value migration you have seen in India in the last ten years. Who won, who lost?</li>
</ol>
</section>
</div>

<footer>Notes built from the NISM Series XV workbook (February 2026 version). Study aid only.</footer>
</div>
"""
