LEARN = r"""
<style>
.calc{display:grid;gap:14px}
.calc label{display:block;font-weight:700;font-size:.92rem}
.calc input[type=number]{font:inherit;width:100%;padding:.45rem .6rem;border:1px solid var(--line);border-radius:8px;background:var(--paper);color:var(--ink)}
.calcin{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}
@media (max-width:700px){.calcin{grid-template-columns:repeat(2,1fr)}}
.calcres{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
@media (max-width:520px){.calcres{grid-template-columns:1fr}}
.calcres div{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:.6rem;text-align:center}
.calcres b{display:block;font-family:var(--head);font-size:1.45rem}
.calcres small{color:var(--muted)}
.calcnote{font-weight:700;margin:.2rem 0 0}
.formula{font-family:var(--head);font-weight:700;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.55rem .8rem;margin:.7rem 0;overflow-x:auto}
</style>
<div class="wrap">
<header class="hero">
<div class="kicker">Chapter 11 of 15</div>
<h1>Fundamental analysis of commodities</h1>
<div class="meta"><span class="pill">Worth <b>5 marks</b> of 100</span><span class="pill">Book pages 218 to 227</span><span class="pill">About 30 minutes</span></div>
<p class="oneline">A commodity has no balance sheet. Its price comes from <span class="k">supply and demand</span>, the <span class="k">US dollar</span>, the weather and politics. Users protect themselves by <span class="k">hedging</span>.</p>
</header>

<figure class="fig" id="fig-map"><figcaption>Chapter map<span>Nine short parts. 11.9 (hedging) has the only numerical. Tap to jump.</span></figcaption>
<div class="map">
<a href="#s1"><b>11.1 and 11.2</b><span>Supply and demand</span><small>Drivers, big producers and consumers</small></a>
<a href="#s3"><b>11.3 and 11.4</b><span>Dollar and world markets</span><small>Dollar index, global benchmarks</small></a>
<a href="#s5"><b>11.5 and 11.6</b><span>Reports and data</span><small>Crop, weather, inventory</small></a>
<a href="#s7"><b>11.7 and 11.8</b><span>Economy and politics</span><small>Macro indicators, policy, geopolitics</small></a>
<a href="#s9"><b>11.9</b><span>Hedging</span><small>Hedge ratio, pros and cons</small></a>
</div></figure>

<div class="col">
<section class="sec" id="s1"><span class="secno">11.1</span><h2>Supply and demand</h2>
<p>Equity analysis studies the company's financial statements, the industry and the economy. <span class="k">Fundamental analysis of commodities</span> depends mainly on the <b>supply and demand</b> of that particular commodity. Chapter 4 (4.7) gave a first look; this chapter goes further.</p>
</div>

<figure class="fig" id="fig-supdem"><figcaption>What drives supply and demand<span>11.1.1 and 11.1.2</span></figcaption>
<div class="grid g2">
<div class="box"><span class="tag">Supply side</span><ul>
<li><b>Production levels:</b> crop yields, mining output, oil drilling capacity</li>
<li><b>Weather and natural disasters:</b> droughts, floods, hurricanes</li>
<li><b>Geopolitical events:</b> wars, sanctions, trade restrictions, OPEC decisions</li>
<li><b>Technology and infrastructure:</b> better farming, mining and transport reduce supply risk</li>
<li><b>Government policies:</b> subsidies, tariffs, export bans, regulations</li>
<li><b>Cost of production:</b> labour, energy and other input costs</li></ul></div>
<div class="box"><span class="tag">Demand side</span><ul>
<li><b>Global economic growth:</b> expansions lift demand for energy, metals, food; recessions cut it</li>
<li><b>Industry and infrastructure:</b> construction and manufacturing lift steel and copper</li>
<li><b>Consumer preferences:</b> renewable energy raises demand for lithium and silver</li>
<li><b>Population and urbanisation:</b> more food, energy, housing</li>
<li><b>Substitutes:</b> electric vehicles reduce oil demand; plant-based food affects meat demand</li>
<li><b>Seasonality:</b> fuel in winter, crops after harvest, festive spikes</li></ul></div>
</div></figure>

<div class="col">
<h3>Country-specific factors (book examples)</h3>
<ul>
<li><b>Copper</b> is largely produced in <b>Chile</b>. Weather problems and labour strikes there affect world supply.</li>
<li><b>Crude oil</b> comes largely from North America, the Middle East and Russia. Middle East tension affects supply worldwide; the <b>Russia-Ukraine war</b> affected Russian crude supply.</li>
<li>On the demand side, a growing economy raises a country's consumption of <b>gold and silver</b>.</li>
</ul>

<h3 id="s2">11.2 Major producers and consumers</h3>
<p>Prices also depend on the health of the main producing and consuming countries: their economies, weather and political stability. Slowing growth or political instability in a key producing region can constrain supply and upset global balance. Trade sanctions, <b>currency volatility</b> and trade policies add to the swings.</p>
</div>

<figure class="fig" id="fig-players"><figcaption>The big players<span>Footnote in the book, citing the World Gold Council (June 2025) and the EIA</span></figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th></th><th>Largest producers</th><th>Largest consumers</th></tr></thead>
<tbody>
<tr><th>Gold</th><td>China, Australia, Russia, USA, Canada</td><td>China, <b>India</b>, USA, Germany, Saudi Arabia</td></tr>
<tr><th>Crude oil</th><td>USA, Russia, Saudi Arabia, Canada, China</td><td>USA, China, <b>India</b>, Germany, Japan</td></tr>
</tbody></table></div></figure>

<div class="col">
<section class="sec" id="s3"><span class="secno">11.3</span><h2>The dollar and the dollar index</h2>
<p>Countries trade commodities across borders: those with a surplus export to those short of it. Settling in many currencies creates <b>currency risk</b>, so the world settled on quoting and settling in a few easily convertible currencies. Since the post-war period, the <span class="k">US dollar</span> has been the preferred one, and central banks hold it as a reserve currency. Commodities trade mostly in US dollars, followed by the <b>euro</b>.</p>
<p>To see the overall movement of the dollar in one number, analysts use the <span class="k">dollar index</span>: the strength of the US dollar against <b>six</b> major currencies.</p>
</div>

<figure class="fig" id="fig-dxy"><figcaption>The six currencies in the dollar index</figcaption>
<div class="grid g3">
<div class="box"><h4>Euro</h4></div>
<div class="box"><h4>Japanese yen</h4></div>
<div class="box"><h4>Pound sterling</h4></div>
<div class="box"><h4>Canadian dollar</h4></div>
<div class="box"><h4>Swedish krona</h4></div>
<div class="box"><h4>Swiss franc</h4></div>
</div></figure>

<figure class="fig" id="fig-dollar"><figcaption>When the dollar moves, commodities move the other way</figcaption>
<div class="grid g2">
<div class="box bd"><span class="tag">Dollar strengthens</span><p>Commodities cost more for buyers paying in other currencies. Global demand falls, pushing commodity <b>prices down</b>.</p></div>
<div class="box gd"><span class="tag">Dollar weakens</span><p>Commodities look cheaper in other currencies. Demand rises, pushing <b>prices up</b>. A weaker dollar often supports gold and crude oil.</p></div>
</div></figure>

<div class="col">
<ul>
<li>Emerging markets with <b>weak currencies</b> pay more for dollar-priced imports, which feeds inflation and changes consumption.</li>
<li><b>Exporters</b> of commodities can gain when their own currency weakens: their dollar revenue converts into more home currency.</li>
</ul>
<div class="analogy">Think of the dollar as the price tag's language. When the dollar gets stronger, the same tag costs an Indian buyer more rupees, so they buy less, and sellers cut prices.</div>

<h3 id="s4">11.4 Global and domestic markets move together</h3>
<p>Organised commodity exchanges started in the mid-19th century and became global hubs that now set benchmark prices. Products on Indian exchanges are <b>replicas</b> of global ones, so their prices <b>strongly correlate</b> with international prices.</p>
</div>

<figure class="fig" id="fig-benchmarks"><figcaption>Global benchmark exchanges</figcaption>
<div class="grid g4">
<div class="box"><span class="tag">Agricultural</span><h4>CBOT</h4><p>Chicago Board of Trade</p></div>
<div class="box"><span class="tag">Bullion</span><h4>COMEX</h4></div>
<div class="box"><span class="tag">Energy</span><h4>NYMEX</h4><p>New York Mercantile Exchange</p></div>
<div class="box"><span class="tag">Base metals</span><h4>LME</h4><p>London Metal Exchange</p></div>
</div></figure>

<div class="col">
<ul>
<li>Crude oil on <b>NYMEX</b> directly affects fuel prices and inflation in importers like India. Indian base metal prices closely follow the <b>LME</b>.</li>
<li>A <b>weakening rupee</b> makes imports dearer and <b>amplifies</b> a global price rise.</li>
<li>Strong local demand, government action and seasonal supply can make domestic prices <b>diverge</b> from international ones for a while.</li>
</ul>
<div class="trap">Match the exchange to the commodity: CBOT, <b>agri</b>; COMEX, <b>bullion</b>; NYMEX, <b>energy</b>; LME, <b>base metals</b>.</div>
</section>

<section class="sec" id="s5"><span class="secno">11.5</span><h2>Crop and weather reports</h2>
<p><span class="k">Crop reports</span>, from government agencies or research bodies, give acreage, planting progress, yield estimates, production and stocks of crops such as wheat, corn, soybeans, cotton and pulses.</p>
<div class="grid g2">
<div class="box bd"><h4>Production higher than expected</h4><p>Prices generally <b>fall</b></p></div>
<div class="box gd"><h4>Production lower than expected</h4><p>Prices can <b>rise</b></p></div>
</div>
<p><span class="k">Weather reports</span> matter because crops are highly sensitive to rain, temperature, drought, floods and frost. Book examples: a <b>delayed monsoon</b> in India hits rice and sugarcane; bad weather in <b>Brazil</b> disrupts coffee and soybean. Traders watch short-term forecasts and long-term patterns such as <b>El Ni&ntilde;o and La Ni&ntilde;a</b>.</p>

<h3 id="s6">11.6 Inventory, production and consumption</h3>
</div>

<figure class="fig" id="fig-inventory"><figcaption>Three data sets that show the balance</figcaption>
<div class="grid g3">
<div class="box"><span class="tag">Inventory</span><p>Stock held in warehouses, exchanges or government reserves. <b>High</b> stock signals oversupply, so prices fall; <b>low</b> stock signals scarcity, so prices may rise.</p></div>
<div class="box"><span class="tag">Production</span><p>How much is supplied. Shaped by technology, policy, seasons, geopolitics. More OPEC output pushes crude <b>down</b>; less mining lifts base metals.</p></div>
<div class="box"><span class="tag">Consumption</span><p>Demand: industrial use of metals, energy use, changing diets in emerging economies. Demand rising faster than supply pushes prices <b>up</b>.</p></div>
</div></figure>

<div class="col">
<section class="sec" id="s7"><span class="secno">11.7</span><h2>Macroeconomic indicators</h2>
<p>Commodities are raw materials for industry and essentials for consumers, so their prices are tied to the wider economy.</p>
</div>

<figure class="fig" id="fig-macro"><figcaption>How the economy moves commodity prices</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Indicator</th><th>Effect on commodities (as per the book)</th></tr></thead>
<tbody>
<tr><th>GDP growth</th><td>Strong growth raises demand for energy, metals and farm goods. Slowdown or recession cuts demand, often lowering prices</td></tr>
<tr><th>Inflation</th><td>Rising inflation pushes investors to commodities, especially <b>gold</b> as a hedge. It also raises production and transport costs</td></tr>
<tr><th>Interest rates</th><td><b>Low</b> rates encourage borrowing and spending, lifting demand. <b>Higher</b> rates strengthen currencies and often <b>reduce</b> commodity prices</td></tr>
<tr><th>Trade balance and geopolitics</th><td>Import-dependent countries pay more when supply chains break; export curbs tighten world markets</td></tr>
<tr><th>Employment, sentiment, industrial production</th><td>Show the underlying trend in demand</td></tr>
</tbody></table></div></figure>

<div class="col">
<h3 id="s8">11.8 Government policies and geopolitics</h3>
<p>Uncontrolled cross-border trade can hurt local producers and the trade balance, so governments use <b>trade policy</b> to protect the domestic market.</p>
<div class="grid g2">
<div class="box"><span class="tag">Government policy</span><ul>
<li>Import-export rules, subsidies, tariffs and quotas decide how much enters or leaves</li>
<li>An <b>export ban</b> on wheat or rice tightens world supply, raising prices</li>
<li>Fuel subsidies cut production costs, encouraging farm output</li>
<li>Stricter mining or emission laws can cut output of metals and energy</li>
<li>Rates, taxes and infrastructure spending shift industrial demand</li></ul></div>
<div class="box"><span class="tag">Geopolitics</span><ul>
<li>Conflict in oil regions such as the Middle East disrupts supply and lifts crude sharply</li>
<li>Trade wars and sanctions restrict flows of energy, metals and farm goods</li>
<li>Strikes or unrest in producing nations cause sudden shortages</li>
<li>Producer alliances such as <b>OPEC</b> output agreements shape pricing power</li>
<li>Tension over shipping routes or pipelines adds a <b>risk premium</b></li></ul></div>
</div>
</section>

<section class="sec" id="s9"><span class="secno">11.9</span><h2>Hedging in commodities</h2>
<p><span class="k">Hedging</span> means taking an <b>opposite position</b> in futures or options to offset possible losses in the physical (cash) market. It is used by producers, consumers, traders, importers, exporters and investors.</p>
</div>

<figure class="fig" id="fig-hedge"><figcaption>Two hedges from the book</figcaption>
<div class="grid g2">
<div class="box gd"><span class="tag">Seller's hedge</span><h4>A wheat farmer</h4><p>Expects a harvest, so <b>sells wheat futures</b> in advance. If wheat prices fall by harvest, the gain on futures makes up the loss on the crop.</p></div>
<div class="box gd"><span class="tag">Buyer's hedge</span><h4>An airline</h4><p>Exposed to rising fuel prices, so <b>buys crude oil futures</b> to lock in its cost and protect profit.</p></div>
</div></figure>

<div class="col">
<div class="why"><b>The goal</b>The goal of hedging is <b>not to make a profit</b>. It is stable, predictable cash flows. But it needs careful planning: <b>over-hedging</b> or a wrong strategy can increase risk instead of reducing it. Transaction costs and margins also matter.</div>
<div class="analogy">Hedging is insurance. You pay a little and give up some upside, so that a bad day does not ruin you.</div>

<h3>11.9.1 Hedge ratio</h3>
<p>The <span class="k">hedge ratio</span> is the share of a position that is hedged with derivatives: how much of the price risk is covered.</p>
<div class="formula">Hedge ratio = correlation between spot and futures prices &times; (SD of change in spot price &divide; SD of change in futures price)</div>
<p>SD means standard deviation (Chapter 12).</p>
</div>

<figure class="fig" id="fig-copper"><figcaption>The book's copper example<span>ABC Company makes copper wire. MCX copper contract: 2.5 tonnes.</span></figcaption>
<div class="flow">
<div class="step"><h4>Inputs</h4><p>Correlation 0.9853. SD of spot changes 9.02. SD of futures changes 9.71</p></div><div class="arrow"></div>
<div class="step hl"><h4>Hedge ratio</h4><p>0.9853 &times; (9.02 &divide; 9.71) = <b>0.915</b></p></div><div class="arrow"></div>
<div class="step"><h4>Quantity</h4><p>For 100 tonnes of exposure: <b>91.5 tonnes</b></p></div><div class="arrow"></div>
<div class="step gd"><h4>Contracts</h4><p>91.5 &divide; 2.5 = 36.6, so <b>37 contracts</b></p></div>
</div>
<p class="ptr" style="margin-top:8px">The book says ABC needs 500 tonnes a month, but its worked answer (91.5 tonnes, 37 contracts) is for 100 tonnes. At 500 tonnes the same ratio would mean 457.5 tonnes. The quiz does not use this mismatch.</p>
</figure>

<figure class="fig" id="fig-hedgecalc"><figcaption>Try it: hedge ratio and contracts<span>Defaults are the book's numbers for 100 tonnes</span></figcaption>
<div class="calc">
<div class="calcin">
<div><label for="h-r">Correlation</label><input type="number" id="h-r" value="0.9853" step="0.01" min="-1" max="1"></div>
<div><label for="h-ss">SD of spot changes</label><input type="number" id="h-ss" value="9.02" step="0.1"></div>
<div><label for="h-sf">SD of futures changes</label><input type="number" id="h-sf" value="9.71" step="0.1"></div>
<div><label for="h-q">Exposure (tonnes)</label><input type="number" id="h-q" value="100" step="10"></div>
<div><label for="h-c">Contract size (tonnes)</label><input type="number" id="h-c" value="2.5" step="0.5"></div>
</div>
<div class="calcres">
<div><b id="h-hr"></b><small>hedge ratio</small></div>
<div><b id="h-hq"></b><small>quantity to hedge</small></div>
<div><b id="h-n"></b><small>contracts (rounded up)</small></div>
</div>
</div></figure>

<div class="col">
<h3>11.9.2 Advantages and disadvantages</h3>
<div class="grid g2">
<div class="box gd"><span class="tag">Advantages</span><ul><li><b>Risk reduction:</b> lock in prices against adverse moves</li><li><b>Stable earnings and cash flows:</b> easier budgeting and planning</li><li>Works like <b>insurance</b> for investors in volatile periods</li><li>Lets businesses focus on core operations</li><li>In thin-margin industries, can be the difference between profit and loss</li></ul></div>
<div class="box bd"><span class="tag">Disadvantages</span><ul><li><b>Cost:</b> margins on futures, premiums on options</li><li><b>Caps gains</b> if prices move favourably</li><li>Wrong strategy or wrong hedge ratio can <b>increase</b> risk</li><li>Needs specialist knowledge, monitoring and administration; may not suit small businesses</li></ul></div>
</div>
</section>

<section class="sec" id="traps"><h2>All exam traps in this chapter</h2>
<ol class="traplist">
<li>Commodity fundamental analysis rests mainly on supply and demand, not financial statements.</li>
<li>Technology and infrastructure reduce supply risk; cost of production is a supply factor.</li>
<li>Substitutes (EVs for oil) and seasonality are demand factors.</li>
<li>Copper: Chile. Crude: North America, Middle East, Russia.</li>
<li>Slowing growth, political instability, sanctions, currency volatility and trade policy disturb global balance.</li>
<li>Commodities trade mainly in US dollars, then euros.</li>
<li>Dollar index: USD against six currencies (euro, yen, pound, Canadian dollar, Swedish krona, Swiss franc).</li>
<li>Stronger dollar: commodity prices tend to fall. Weaker dollar: they tend to rise.</li>
<li>A weakening domestic currency makes imports dearer and amplifies global price rises.</li>
<li>CBOT: agri. COMEX: bullion. NYMEX: energy. LME: base metals.</li>
<li>Higher-than-expected crop production: prices fall.</li>
<li>High inventory: oversupply, prices fall. Low inventory: scarcity, prices rise.</li>
<li>Higher interest rates strengthen currencies and often reduce commodity prices.</li>
<li>An export ban on wheat or rice tightens global supply and raises prices.</li>
<li>Hedging takes the opposite position in futures or options; its goal is stability, not profit.</li>
<li>Farmer sells futures; airline buys crude futures.</li>
<li>Hedge ratio = correlation &times; (SD spot changes &divide; SD futures changes).</li>
<li>Over-hedging or a wrong hedge ratio can increase risk. Hedging costs margins or premiums and caps gains.</li>
</ol>
</section>

<section class="sec" id="talk"><h2>For the group discussion</h2>
<ol class="talk">
<li>India imports most of its crude oil. Walk through what a stronger dollar does to Indian petrol prices and inflation.</li>
<li>Why might Indian gold prices rise even when international gold prices are flat?</li>
<li>A delayed monsoon is forecast. Which commodities and which listed Indian companies would you watch?</li>
<li>A jeweller buys gold every month. Should it hedge all of its needs, part, or none? Why?</li>
<li>Can a company hedge too much? Give an example of how that could hurt it.</li>
</ol>
</section>
</div>

<footer>Notes built from the NISM Series XV workbook (February 2026 version). Study aid only.</footer>
</div>
"""

WIDGETS = r"""
window.__WIDGETS__=function(){
const g=id=>document.getElementById(id);
if(!g('h-r'))return;
function calc(){const r=+g('h-r').value,ss=+g('h-ss').value,sf=+g('h-sf').value,q=+g('h-q').value,c=+g('h-c').value;
 if(!(sf>0)||!(c>0)){g('h-hr').textContent='-';g('h-hq').textContent='-';g('h-n').textContent='-';return}
 const hr=r*ss/sf,hq=hr*q,n=Math.ceil(hq/c-1e-9);
 g('h-hr').textContent=hr.toFixed(3);g('h-hq').textContent=(Math.round(hq*10)/10)+' t';g('h-n').textContent=n;}
['h-r','h-ss','h-sf','h-q','h-c'].forEach(i=>g(i).addEventListener('input',calc));calc();
};
"""

CARDS = [
 {"f":"What does commodity fundamental analysis mainly depend on?","b":"The <b>supply and demand</b> of that commodity (not financial statements, as with equity)."},
 {"f":"Six supply-side factors","b":"Production levels; weather and disasters; geopolitics (wars, sanctions, OPEC); technology and infrastructure; government policy; cost of production."},
 {"f":"Six demand-side factors","b":"Global growth; industry and infrastructure; consumer preferences; population and urbanisation; substitutes; seasonality."},
 {"f":"Demand example: renewable energy","b":"Raises demand for <b>lithium and silver</b>."},
 {"f":"Substitute examples (book)","b":"Electric vehicles reduce oil demand; plant-based food affects meat demand."},
 {"f":"Where is copper largely produced?","b":"<b>Chile</b>. Weather and labour strikes there affect world supply."},
 {"f":"Where is crude oil largely produced?","b":"North America, the Middle East and Russia."},
 {"f":"Gold: largest producers and consumers (book footnote)","b":"Producers: China, Australia, Russia, USA, Canada. Consumers: China, India, USA, Germany, Saudi Arabia."},
 {"f":"Crude oil: largest producers and consumers (book footnote)","b":"Producers: USA, Russia, Saudi Arabia, Canada, China. Consumers: USA, China, India, Germany, Japan."},
 {"f":"What disturbs global commodity equilibrium (11.2)?","b":"Slowing growth or political instability in producing regions; trade sanctions; currency volatility; trade policies."},
 {"f":"Main currencies for commodity trade","b":"<b>US dollar</b>, followed by the <b>euro</b>."},
 {"f":"Dollar index","b":"Strength of the US dollar against <b>six</b> currencies: euro, yen, pound sterling, Canadian dollar, Swedish krona, Swiss franc."},
 {"f":"Dollar strengthens: commodity prices?","b":"Tend to <b>fall</b>: dearer for non-dollar buyers, so demand drops."},
 {"f":"Dollar weakens: commodity prices?","b":"Tend to <b>rise</b>. A weaker dollar often supports gold and crude."},
 {"f":"Who gains when a commodity exporter's own currency weakens?","b":"The exporter: dollar revenue converts into more home currency."},
 {"f":"CBOT, COMEX, NYMEX, LME","b":"CBOT: <b>agri</b>. COMEX: <b>bullion</b>. NYMEX: <b>energy</b>. LME: <b>base metals</b>."},
 {"f":"Why do Indian commodity prices track global ones?","b":"Indian products are replicas of global contracts, so prices strongly correlate."},
 {"f":"Weakening rupee and a global price rise","b":"Imports get dearer; the rupee fall <b>amplifies</b> the global rise."},
 {"f":"Why can domestic prices diverge from global?","b":"Strong local demand, government intervention, seasonal supply."},
 {"f":"What do crop reports contain?","b":"Acreage, planting progress, yield estimates, production, inventory."},
 {"f":"Higher-than-expected crop production","b":"Prices generally <b>fall</b>. Lower output can push prices up."},
 {"f":"Weather examples (book)","b":"Delayed Indian monsoon hits rice and sugarcane; bad weather in Brazil hits coffee and soybean. Watch El Ni&ntilde;o and La Ni&ntilde;a."},
 {"f":"High versus low inventory","b":"High: oversupply, prices fall. Low: scarcity, prices may rise."},
 {"f":"OPEC raises output: crude price?","b":"Downward pressure."},
 {"f":"Inflation and commodities","b":"Investors move to commodities, especially <b>gold</b> as a hedge; costs of production and transport rise."},
 {"f":"Interest rates and commodities","b":"Low rates lift demand. Higher rates strengthen currencies and often <b>reduce</b> commodity prices."},
 {"f":"Export ban on wheat or rice","b":"Tightens global supply, so prices <b>rise</b>."},
 {"f":"Why do governments use trade policy on commodities?","b":"To protect the domestic market and the trade balance from uncontrolled cross-border trade."},
 {"f":"Geopolitical risk premium","b":"Extra price from tension over shipping routes or energy pipelines."},
 {"f":"Hedging","b":"Taking an <b>opposite position</b> in futures or options to offset losses in the physical market."},
 {"f":"Goal of hedging","b":"<b>Stability</b> and predictable cash flows, not profit."},
 {"f":"Farmer's hedge versus airline's hedge","b":"Farmer <b>sells</b> wheat futures. Airline <b>buys</b> crude oil futures."},
 {"f":"Hedge ratio","b":"Proportion of a position hedged. = correlation (spot, futures) &times; SD of spot changes &divide; SD of futures changes."},
 {"f":"Book's copper hedge","b":"0.9853 &times; 9.02 &divide; 9.71 = <b>0.915</b>. For 100 tonnes: 91.5 tonnes = <b>37</b> MCX contracts of 2.5 tonnes."},
 {"f":"Advantages of hedging","b":"Risk reduction; stable earnings and cash flows; insurance for portfolios; focus on core business; can decide profit or loss in thin-margin industries."},
 {"f":"Disadvantages of hedging","b":"Cost (margins, premiums); caps gains; wrong ratio can raise risk; needs expertise and monitoring."},
]

MCQS = [
 {"id":"11.1","q":"The ______ of commodities is largely dependent on the supply and demand dynamics of the particular commodity.","o":["Fundamental analysis","Technical analysis","SWOT analysis","Ratio analysis"],"a":0,"w":"Book sample question."},
 {"id":"11.2","q":"Which of the following factors cause global disruptions, thereby affecting the global commodity market equilibrium?","o":["Currency fluctuations and trade policies","Increase in economic growth","Stable political conditions in producing countries","All of the above"],"a":0,"w":"Book sample question. The book names slowing growth, political instability, sanctions, currency volatility and trade policies. Rising growth and stability are the opposite."},
 {"id":"11.3","q":"A ______ domestic currency against the US dollar can make imports more expensive, in a scenario of rising global prices.","o":["Weakening","Strengthening","Stable"],"a":0,"w":"Book sample question. A weaker rupee amplifies the impact of global price rises."},
 {"id":"11.4","q":"Which of the following is a supply-side factor for commodities?","o":["Cost of production","Population growth and urbanisation","Consumer preferences","Seasonality of consumption"],"a":0,"w":"The other three are demand-side factors."},
 {"id":"11.5","q":"According to the book, a shift towards renewable energy increases demand for:","o":["Lithium and silver","Coal and crude oil","Wheat and rice","Copper only"],"a":0,"w":"An example of consumer preferences and lifestyle as a demand factor."},
 {"id":"11.6","q":"Electric vehicles reducing oil demand is an example of which demand factor?","o":["Substitutes and alternatives","Seasonality","Population growth","Production levels"],"a":0,"w":"The book also cites plant-based food affecting meat demand."},
 {"id":"11.7","q":"According to the book, copper is largely produced in:","o":["Chile","Saudi Arabia","Japan","Germany"],"a":0,"w":"Weather problems and labour strikes in Chile affect world copper supply."},
 {"id":"11.8","q":"Which country appears in the book's list of largest consumers of both gold and crude oil?","o":["India","Canada","Australia","Russia"],"a":0,"w":"China and the USA are also in both lists, but are not among these options."},
 {"id":"11.9","q":"After the US dollar, which currency is the most preferred for quoting and trading commodities, as per the book?","o":["Euro","Japanese yen","Chinese yuan","Indian rupee"],"a":0,"w":"The dollar became the preferred currency after the post-war period, followed by the euro."},
 {"id":"11.10","q":"The dollar index measures the strength of the US dollar against how many major currencies?","o":["Six","Four","Ten","Two"],"a":0,"w":"Euro, Japanese yen, pound sterling, Canadian dollar, Swedish krona and Swiss franc."},
 {"id":"11.11","q":"Which of the following currencies is NOT part of the dollar index as listed in the book?","o":["Indian rupee","Swedish krona","Swiss franc","Canadian dollar"],"a":0,"w":"The six are the euro, yen, pound, Canadian dollar, Swedish krona and Swiss franc."},
 {"id":"11.12","q":"When the US dollar strengthens against other currencies, commodity prices typically:","o":["Come under downward pressure","Rise sharply","Stay unchanged","Become fixed by exchanges"],"a":0,"w":"Commodities become dearer for non-dollar buyers, reducing demand."},
 {"id":"11.13","q":"An exporter of commodities may benefit when:","o":["Its local currency weakens","Its local currency strengthens","The dollar index rises sharply","Global demand falls"],"a":0,"w":"Dollar revenue converts into more home currency."},
 {"id":"11.14","q":"Which global exchange is the benchmark for base metals?","o":["London Metal Exchange (LME)","Chicago Board of Trade (CBOT)","COMEX","NYMEX"],"a":0,"w":"CBOT: agri. COMEX: bullion. NYMEX: energy."},
 {"id":"11.15","q":"COMEX is the global benchmark exchange for:","o":["Bullion","Agricultural commodities","Base metals","Energy products"],"a":0,"w":"Gold and silver."},
 {"id":"11.16","q":"Why do prices of derivatives on Indian commodity exchanges strongly correlate with international prices?","o":["They are replicas of their global counterparts","They are set by the RBI","They are fixed by the government","They trade only in dollars"],"a":0,"w":"Global benchmarks set the tone for domestic markets."},
 {"id":"11.17","q":"Which of the following can make domestic commodity prices diverge from international benchmarks?","o":["Government intervention","Strong correlation with global markets","Use of the dollar for pricing","Replication of global contracts"],"a":0,"w":"Strong local demand and seasonal supply can also cause divergence."},
 {"id":"11.18","q":"A crop report shows production much higher than expected. Prices are generally likely to:","o":["Decline","Rise","Stay unchanged","Become more volatile only abroad"],"a":0,"w":"Lower output projections can drive prices up."},
 {"id":"11.19","q":"According to the book, a delayed monsoon in India affects the production of:","o":["Rice and sugarcane","Coffee and soybean","Crude oil","Copper"],"a":0,"w":"Adverse weather in Brazil disrupts coffee and soybean."},
 {"id":"11.20","q":"High inventory levels of a commodity generally signal:","o":["Oversupply and downward pressure on prices","Scarcity and rising prices","Higher demand","Lower production costs"],"a":0,"w":"Low inventory suggests scarcity."},
 {"id":"11.21","q":"An increase in oil output by OPEC members typically:","o":["Exerts downward pressure on crude prices","Pushes crude prices up","Has no effect","Raises base metal prices"],"a":0,"w":"More supply, lower price."},
 {"id":"11.22","q":"According to the book, higher interest rates:","o":["Strengthen currencies and often reduce commodity prices","Weaken currencies and raise commodity prices","Encourage borrowing and lift commodity demand","Have no link with commodities"],"a":0,"w":"Low rates encourage borrowing and lift demand."},
 {"id":"11.23","q":"Rising inflation typically pushes investors towards which commodity as a hedge?","o":["Gold","Crude oil","Wheat","Copper"],"a":0,"w":"Precious metals like gold act as an inflation hedge."},
 {"id":"11.24","q":"An export ban on wheat by a major producer is likely to:","o":["Tighten global supply and drive prices higher","Increase global supply","Lower world wheat prices","Have no effect on world markets"],"a":0,"w":"Government policy directly shapes availability."},
 {"id":"11.25","q":"Hedging in commodities involves:","o":["Taking an opposite position in futures or options to offset losses in the physical market","Buying more of the physical commodity","Speculating on price direction for profit","Avoiding all derivatives"],"a":0,"w":"The goal is stability of cash flows, not profit."},
 {"id":"11.26","q":"A wheat farmer expecting a harvest wants to protect against falling prices. The farmer should:","o":["Sell wheat futures","Buy wheat futures","Buy crude oil futures","Do nothing"],"a":0,"w":"If prices fall, the gain on short futures offsets the lower crop price."},
 {"id":"11.27","q":"An airline worried about rising fuel prices should:","o":["Buy crude oil futures","Sell crude oil futures","Sell wheat futures","Buy gold"],"a":0,"w":"Long futures lock in the fuel cost."},
 {"id":"11.28","q":"According to the book, the goal of hedging is:","o":["Stability and predictability of cash flows","Maximum profit","Avoiding all transaction costs","Raising leverage"],"a":0,"w":"Over-hedging or wrong strategies can increase risk."},
 {"id":"11.29","q":"The hedge ratio in commodities is calculated as:","o":["Correlation between spot and futures &times; (SD of change in spot &divide; SD of change in futures)","SD of spot &times; SD of futures","Spot price &divide; futures price","Futures price &minus; spot price"],"a":0,"w":"The book's formula."},
 {"id":"11.30","q":"Correlation between spot and futures is 0.9, SD of change in spot price is 8 and SD of change in futures price is 10. The hedge ratio is:","o":["0.72","1.125","0.80","0.90"],"a":0,"w":"0.9 &times; 8 &divide; 10 = 0.72."},
 {"id":"11.31","q":"A company has 500 tonnes of exposure and a hedge ratio of 0.72. Each futures contract is 2.5 tonnes. How many contracts should it use?","o":["144","200","360","72"],"a":0,"w":"500 &times; 0.72 = 360 tonnes. 360 &divide; 2.5 = 144 contracts."},
 {"id":"11.32","q":"Which of the following is a disadvantage of hedging?","o":["It caps potential gains if prices move favourably","It reduces price risk","It stabilises cash flows","It lets businesses focus on core operations"],"a":0,"w":"Hedging also costs margins or premiums and needs expertise."},
 {"id":"11.33","q":"Which statement about hedging is correct as per the book?","o":["Poorly designed hedges or incorrect hedge ratios can increase risk","Hedging always removes all risk","Hedging is free of cost","Only producers can hedge"],"a":0,"w":"Traders, importers, exporters and investors also hedge."},
]

CASES = [
 {"id":"C21","title":"Kaveri Jewellers and the dollar","text":"Kaveri Jewellers imports gold every month. This quarter, the US dollar index has risen sharply, the rupee has weakened against the dollar, and international gold prices are rising. India also reports a strong festive season.",
  "qs":[
   {"q":"What does a rising dollar index usually do to international commodity prices, as per the book?","o":["Puts downward pressure on them","Pushes them sharply up","Has no effect","Fixes them at last year's level"],"a":0,"w":"A stronger dollar makes commodities dearer for non-dollar buyers, reducing demand."},
   {"q":"With international gold prices rising and the rupee weakening, Kaveri's rupee cost of gold will:","o":["Rise by more than the international price rise","Rise by less than the international price rise","Fall","Stay the same"],"a":0,"w":"A weakening domestic currency amplifies the impact of global price rises."},
   {"q":"Strong festive demand in India is an example of:","o":["Seasonality, a demand-side factor","A supply-side factor","A currency factor","A geopolitical factor"],"a":0,"w":"The book lists festive consumption spikes under seasonality."},
   {"q":"To protect against a further rise in gold prices, Kaveri should:","o":["Buy gold futures","Sell gold futures","Sell its gold stock","Buy crude oil futures"],"a":0,"w":"Like the airline buying crude futures, a buyer of the commodity takes a long futures position."},
  ]},
 {"id":"C22","title":"Rao Cables hedges copper","text":"Rao Cables needs 250 tonnes of copper every month. Its analyst finds a correlation of 0.95 between changes in spot and futures prices, a standard deviation of 9.0 for spot price changes and 10.0 for futures price changes. The MCX copper contract is 2.5 tonnes. LME prices have been rising.",
  "qs":[
   {"q":"What is the hedge ratio?","o":["0.855","1.056","0.950","0.900"],"a":0,"w":"0.95 &times; 9.0 &divide; 10.0 = 0.855."},
   {"q":"How many tonnes should Rao hedge?","o":["213.75 tonnes","250 tonnes","237.5 tonnes","225 tonnes"],"a":0,"w":"250 &times; 0.855 = 213.75 tonnes."},
   {"q":"How many MCX contracts is that, rounded up?","o":["86","100","85","214"],"a":0,"w":"213.75 &divide; 2.5 = 85.5, so 86 contracts (the book rounds 36.6 up to 37 the same way)."},
   {"q":"Why do Indian copper prices tend to follow LME?","o":["Domestic base metal prices closely follow LME trends","LME is an Indian exchange","SEBI fixes Indian prices to LME","Copper is not traded in India"],"a":0,"w":"LME is the global benchmark for base metals."},
  ]},
]

DATA = {"id":"ch11","short":"Ch11","title":"Chapter 11: Fundamental analysis of commodities","cards":CARDS,"mcqs":MCQS,"cases":CASES}
