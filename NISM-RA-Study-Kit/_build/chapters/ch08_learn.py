LEARN = r"""
<style>
.calc{display:grid;gap:14px}
.calc label{display:block;font-weight:700}
.calc input[type=number]{font:inherit;width:100%;padding:.45rem .6rem;border:1px solid var(--line);border-radius:8px;background:var(--paper);color:var(--ink)}
.calcin{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
@media (max-width:620px){.calcin{grid-template-columns:repeat(2,1fr)}}
.calcres{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
@media (max-width:520px){.calcres{grid-template-columns:repeat(2,1fr)}}
.calcres div{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:.6rem;text-align:center}
.calcres b{display:block;font-family:var(--head);font-size:1.45rem}
.calcres small{color:var(--muted)}
.calcnote{font-weight:700;margin:.2rem 0 0}
.formula{font-family:var(--head);font-weight:700;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.55rem .8rem;margin:.7rem 0;overflow-x:auto}
table.fs td:nth-child(2){font-family:var(--head);font-weight:700}
</style>
<div class="wrap">
<header class="hero">
<div class="kicker">Chapter 8 of 15</div>
<h1>Company analysis: financial analysis</h1>
<div class="meta"><span class="pill">Worth <b>12 marks</b> of 100</span><span class="pill">Book pages 145 to 186</span><span class="pill">About 90 minutes</span></div>
<p class="oneline">Read the <span class="k">balance sheet</span>, the <span class="k">profit and loss account</span> and the <span class="k">cash flow</span>, then turn them into <span class="k">ratios</span> that tell a story.</p>
</header>

<figure class="fig" id="fig-map"><figcaption>Chapter map<span>A long, numbers-heavy chapter. 8.11 (ratios) and 8.12 (DuPont) are the core for numericals. Tap to jump.</span></figcaption>
<div class="map">
<a href="#s1"><b>8.1 and 8.2</b><span>The statements</span><small>Five parts, standalone versus consolidated</small></a>
<a href="#s3"><b>8.3</b><span>Balance sheet</span><small>Line items, total debt, working capital</small></a>
<a href="#s4"><b>8.4 and 8.5</b><span>Profit and loss</span><small>Line items, EPS, EBITDA, EBIT</small></a>
<a href="#s6"><b>8.6</b><span>Cash flow</span><small>Operating, investing, financing</small></a>
<a href="#s7"><b>8.7 to 8.9</b><span>Notes and audit report</span><small>Policies, contingent liabilities, opinions</small></a>
<a href="#s10"><b>8.10 and 8.11</b><span>Ratios</span><small>Profitability, return, leverage, liquidity, efficiency</small></a>
<a href="#s12"><b>8.12 to 8.14</b><span>DuPont, forecasts, peers</span><small>Three parts of ROE</small></a>
<a href="#s15"><b>8.15</b><span>Other things to track</span><small>Dilution, dividends, insider trades</small></a>
</div></figure>

<div class="col">
<section class="sec" id="s0"><span class="secno">Intro</span><h2>Why financial analysis?</h2>
<p>Chapters 5 to 7 looked at the economy, the industry and the company's business. Financial analysis turns all that into the company's likely <b>profits, cash flows</b> and, finally, the <b>fair value</b> of its shares. Financial statements also supply the numbers for market sizing (6.4), industry KPIs (6.7) and strengths and weaknesses (7.5).</p>
<div class="why"><b>You do not need to be an accountant</b>The book says an analyst need not be a great accountant, but must be able to read and interpret financial statements. Accounting knowledge helps.</div>
</section>

<section class="sec" id="s1"><span class="secno">8.1</span><h2>The financial statements</h2>
<p>In India, the statements and their format are governed by <b>Schedule III of the Companies Act, 2013</b> and <b>Ind AS 1</b>. A complete set under Ind AS 1:</p>
</div>

<figure class="fig" id="fig-statements"><figcaption>A complete set of financial statements<span>Ind AS 1</span></figcaption>
<div class="grid g2">
<div class="box hl"><span class="tag">1</span><h4>Balance sheet</h4><p>Statement of financial position: assets, liabilities and equity <b>at the end</b> of the period. A snapshot.</p></div>
<div class="box hl"><span class="tag">2</span><h4>Statement of profit and loss</h4><p>Income, expenses and profit <b>for the period</b>. Must include <b>other comprehensive income (OCI)</b>.</p></div>
<div class="box"><span class="tag">3</span><h4>Statement of changes in equity</h4><p>How shareholders' funds changed: profit, dividends, new shares, buybacks, OCI.</p></div>
<div class="box"><span class="tag">4</span><h4>Cash flow statement</h4><p>Sources and uses of cash.</p></div>
<div class="box"><span class="tag">5</span><h4>Notes</h4><p>Accounting policies and break-ups of the figures.</p></div>
</div>
<p class="ptr" style="margin-top:8px">Each statement must show figures for at least <b>one prior period</b> for comparison. Companies may show more.</p>
</figure>

<div class="col">
<h3 id="s2">8.2 Standalone versus consolidated</h3>
<p>Every company is a separate legal entity and prepares its own <span class="k">standalone</span> statements. But for groups these can mislead: Toyota Motor Corporation's standalone accounts show only sales of that entity in Japan, not sales through subsidiaries in China, India or North America.</p>
<p><span class="k">Consolidated</span> statements treat all companies <b>controlled</b> by the parent as one group and combine their results.</p>
<dl class="terms">
<dt>Control</dt><dd>Owning more than 50% of voting rights, <b>or</b> the right to appoint a majority of the board. Even without 50%, a company that can direct a subsidiary's strategy and operations to change its returns is in de facto control, and must consolidate under <b>Ind AS 110</b>.</dd>
<dt>Holding (parent)</dt><dd>The company that controls.</dd>
<dt>Subsidiary</dt><dd>The company that is controlled. Book examples: Jio Platforms (controlled by Reliance Industries); Toyota Kirloskar Motor (majority owned by Toyota Motor Corporation, Japan).</dd>
</dl>
<div class="grid g2">
<div class="box gd"><h4>Usually prefer consolidated</h4><p>It gives a more holistic picture of the group.</p></div>
<div class="box"><h4>Also check standalone when...</h4><p>Subsidiaries cannot pass dividends to the parent: strict capital controls in their country, or a debt covenant banning dividends. Then ask: can the parent stand on its own in a crisis?</p></div>
</div>
<div class="trap">As per the book, SEBI requires listed companies to publish <b>consolidated statements annually</b> and <b>standalone results quarterly</b>. Quarterly consolidated results are voluntary, which leaves analysts with dated group numbers between annual reports.</div>
</section>

<section class="sec" id="s3"><span class="secno">8.3</span><h2>The balance sheet</h2>
<p>Format: Schedule III of the Companies Act, 2013. <b>Banks, insurers and utilities</b> follow formats set by their own regulators. The book uses Bharti Airtel's consolidated balance sheet for 31 March 2019 as its example.</p>
<p><span class="k">Assets</span> are items expected to give future benefits. A company can show only assets that can be measured in money and <b>have been paid for</b>. So a company generally cannot show its own <b>self-generated brand</b>.</p>
<dl class="terms">
<dt>Current asset</dt><dd>Gives benefit within one operating cycle, usually taken as one year. If the cycle is longer than a year, one year is the convention.</dd>
<dt>Non-current asset</dt><dd>Gives benefit over the long term, usually more than one year. Everything that is not current.</dd>
</dl>
</div>

<figure class="fig" id="fig-bsassets"><figcaption>Asset line items<span>What each one means, and how it is valued</span></figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Line item</th><th>What it is</th><th>How it is shown</th></tr></thead>
<tbody>
<tr><th>Property, plant and equipment (PPE)</th><td>Land, buildings, machines, furniture, computers</td><td>Historical cost less accumulated depreciation. Ind AS 16 allows a revaluation model, applied to a <b>whole class</b> of assets</td></tr>
<tr><th>Capital work in progress</th><td>PPE still under construction</td><td>Moved to PPE when ready to operate</td></tr>
<tr><th>Goodwill</th><td>Price paid for a business above the fair value of net assets taken over</td><td>Tested for impairment; any shortfall written off</td></tr>
<tr><th>Intangible assets</th><td>Legal rights: acquired copyrights, patents, brands. Internally developed software can be shown; other self-generated assets cannot</td><td>Cost less accumulated amortisation</td></tr>
<tr><th>Intangibles under development</th><td>Intangibles not yet ready</td><td>Moved to intangibles when ready</td></tr>
<tr><th>Investment in joint ventures and associates</th><td>Strategic stakes the company does not control</td><td><b>Equity method</b>: adjusted for its share of profit and OCI, reduced by dividends received</td></tr>
<tr><th>Non-current financial assets</th><td>Long-term investments, loans, advances</td><td>Debt held to collect interest and principal: amortised cost. Others: fair value</td></tr>
<tr><th>Inventory</th><td>Raw material, work in progress, unsold finished goods</td><td><b>Lower of cost or market value</b></td></tr>
<tr><th>Current financial assets</th><td>Cash and cash equivalents, bank balances, receivables, short-term investments</td><td>Receivables net of provision for doubtful debts. Investments at fair value</td></tr>
<tr><th>Other current assets</th><td>Prepaid expenses; benefits received in kind within a year</td><td>&nbsp;</td></tr>
</tbody></table></div></figure>

<div class="col">
<div class="why"><b>The book's goodwill example</b>In FY 2018, Bharti Airtel bought 100% of Tigo Rwanda for <b>Rs 3,200 crore</b>. Tigo's net assets were worth <b>Rs 2,838 crore</b>. The extra <b>Rs 362 crore</b> was recorded as goodwill. If a company pays <b>less</b> than fair value, the difference goes to <b>capital reserve</b> under equity.</div>

<h3>Equity: the owners' residual share</h3>
<p><span class="k">Equity</span> = assets minus liabilities. Its parts:</p>
<dl class="terms">
<dt>Share capital</dt><dd>Face value of paid-up shares.</dd>
<dt>Share premium</dt><dd>Amount received above face value when shares were issued (IPO or FPO).</dd>
<dt>Retained earnings</dt><dd>Profit and OCI not paid out as dividend or set aside.</dd>
<dt>General reserve</dt><dd>Retained earnings set aside for future use.</dd>
<dt>Capital and revaluation reserve</dt><dd>Surplus from showing assets above purchase price. Usually <b>not available for dividends</b>.</dd>
<dt>Non-controlling (minority) interest</dt><dd>Outside shareholders' share of a subsidiary's equity. Appears <b>only in consolidated</b> statements.</dd>
</dl>
<h3>Liabilities</h3>
</div>

<figure class="fig" id="fig-bsliab"><figcaption>Liability line items</figcaption>
<div class="grid g2">
<div class="box"><span class="tag">Non-current (beyond one year)</span><ul>
<li><b>Long-term debt</b>: loans, bonds, debentures due after a year. The part due within a year is shown as <b>current portion of long-term debt</b>.</li>
<li><b>Lease liability</b>: right to use an asset for more than a year. Analysts often treat it as <b>debt</b>.</li>
<li><b>Derivative instruments</b>: mark-to-market losses on contracts settled after a year.</li>
<li><b>Other long-term financial liabilities</b>.</li>
<li><b>Deferred revenue</b>: advance received for service still to be given.</li>
<li><b>Provisions</b>: for a <b>specific</b> obligation not yet fully quantified: retirement benefits, warranties, pending legal cases.</li></ul></div>
<div class="box"><span class="tag">Current (within one year)</span><ul>
<li><b>Payables</b>: owed to suppliers.</li>
<li><b>Short-term debt</b>: borrowed for under a year, but often rolled over.</li>
<li>Short-term provisions</li>
<li>Current portion of long-term liability</li>
<li>Deferred revenue (due within a year)</li>
<li>Advances from customers</li>
<li>Unpaid and accrued expenses</li></ul></div>
</div></figure>

<div class="col">
<div class="analogy">Deferred revenue, the book's example: a customer buys a 6-month prepaid pack for Rs 1,200. After one month, the company counts Rs 200 as revenue. The other <b>Rs 1,000</b> (1,200 &times; 5/6) is deferred revenue: a promise still owed.</div>
<div class="trap">A <b>provision</b> is for a specific obligation (like retirement benefits). A <b>reserve</b> is set aside without a specific obligation. Do not mix them up.</div>

<h3>8.3.2 Balance sheet metrics analysts add</h3>
<p>Balance sheets often miss fair value because of the historical cost and money measurement concepts. So analysts compute extra metrics.</p>
</div>

<figure class="fig" id="fig-bsmetrics"><figcaption>Total debt and working capital</figcaption>
<div class="grid g3">
<div class="box hl"><span class="tag">Total debt</span><p>Long-term debt + current portion of long-term debt + short-term debt + finance lease obligations + accrued interest.</p><p class="ptr">Debt is settled in cash and carries interest, unlike other liabilities.</p></div>
<div class="box"><span class="tag">Net working capital</span><p>Current assets &minus; current liabilities. The accountant's measure.</p><p class="ptr">Bharti Airtel FY 2019: 329.06 &minus; 930.55 = <b>minus Rs 601.49 billion</b>.</p></div>
<div class="box gd"><span class="tag">Core working capital</span><p>Inventory + trade receivables &minus; trade payables.</p><p class="ptr">Only items from core operations. Helps judge the need for bank working capital finance. The book suggests also including a reasonable cash balance.</p></div>
</div></figure>

<div class="col">
<div class="why"><b>Why working capital is needed</b>The book says the "day-to-day needs" idea is a misnomer. A company needs working capital because it <b>spends first</b> (raw materials, production) and <b>waits to be paid</b> by customers who buy on credit.</div>
</section>

<section class="sec" id="s4"><span class="secno">8.4</span><h2>The profit and loss account</h2>
<p>Shows performance <b>for a period</b>. Format: Schedule III; Ind AS 1 adds <b>OCI</b>, shown below net profit. Banks, insurers and utilities use their regulators' formats.</p>
</div>

<figure class="fig" id="fig-pl"><figcaption>P&amp;L line items</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Line item</th><th>Meaning</th></tr></thead>
<tbody>
<tr><th>Revenue</th><td>Sales of goods and services from core and incidental operations. Some show incidental income as "other operating income"</td></tr>
<tr><th>Other income</th><td>Non-operating income: investment income, profit on sale of assets</td></tr>
<tr><th>Cost of raw materials</th><td><b>Purchases + opening stock &minus; closing stock</b> of raw materials</td></tr>
<tr><th>Purchase of stock-in-trade</th><td>Goods bought and resold without processing. Most retail purchases</td></tr>
<tr><th>Change in inventory of WIP and finished goods</th><td>Opening minus closing balance of WIP and finished goods</td></tr>
<tr><th>Employee cost</th><td>Salaries, benefits, stock-based compensation, staff welfare, annual retirement provision</td></tr>
<tr><th>Depreciation</th><td>Allocates the cost of tangible assets over their useful life. Ind AS 16: method should reflect how the asset is used (a cab fleet by distance)</td></tr>
<tr><th>Amortisation</th><td>Gradual write-off of intangible assets</td></tr>
<tr><th>Finance cost</th><td>Interest, processing fees, amortised cost of issuing securities</td></tr>
<tr><th>Income from equity-accounted entities</th><td>Share of profit of joint ventures and associates</td></tr>
<tr><th>Exceptional items</th><td>Not from the normal course of business: natural calamity losses, one-time regulatory charges</td></tr>
<tr><th>Tax</th><td>Current tax, MAT, deferred tax. Deferred tax has <b>no cash impact</b></td></tr>
<tr><th>Non-controlling interest</th><td>Subsidiary profit belonging to outside shareholders</td></tr>
</tbody></table></div></figure>

<div class="col">
<h3>EPS: basic and diluted</h3>
<div class="formula">Basic EPS = net profit to equity shareholders &divide; weighted average shares outstanding</div>
<p><b>Diluted EPS</b> assumes all instruments that could become shares without full payment are converted: in-the-money warrants, ESOPs, convertibles. Profit is adjusted for the effect too. For a <b>loss-making</b> company, basic and diluted EPS are the <b>same</b>.</p>
<h3>Other comprehensive income (OCI)</h3>
<p>Income or expense that bypasses the P&amp;L, mostly changes in value from non-operating factors: revaluation surplus changes; remeasurement of defined benefit plans; translation of foreign operations; fair value changes of certain financial assets or liabilities; gains or losses on derivatives that hedge risk.</p>

<h3>8.4.2 Profit metrics</h3>
<p>Most companies present a <b>single-step</b> P&amp;L (all income minus all expenses = profit before tax). Some, like Bharti Airtel, present a <b>multi-step</b> P&amp;L showing EBITDA. Analysts often redraw single-step statements into multi-step ones.</p>
</div>

<figure class="fig" id="fig-waterfall"><figcaption>From revenue to profit<span>The profit "waterfall"</span></figcaption>
<div class="flow">
<div class="step"><h4>Revenue</h4><p>&nbsp;</p></div><div class="arrow"></div>
<div class="step"><h4>Gross profit</h4><p>Revenue &minus; cost of goods sold. Not computable for most Indian companies</p></div><div class="arrow"></div>
<div class="step hl"><h4>EBITDA</h4><p>Before interest, tax, depreciation, amortisation</p></div><div class="arrow"></div>
<div class="step hl"><h4>EBIT</h4><p>"Operating profit"</p></div><div class="arrow"></div>
<div class="step gd"><h4>PAT</h4><p>Net profit for shareholders</p></div>
</div></figure>

<div class="col">
<ul>
<li><b>Gross profit</b> suits manufacturers, but Indian companies disclose only raw material costs among direct costs, so it usually <b>cannot be calculated</b>.</li>
<li><span class="k">EBITDA</span> is not affected by <b>capital structure</b> (interest) or <b>infrastructure and accounting choices</b> (depreciation), so it is the right metric to <b>compare firms</b>, even across sectors. "Adjusted EBITDA" also strips out investment and other non-operating income. EBITDA is a proxy for cash profit, but use it that way only as a last resort.</li>
<li><span class="k">EBIT</span> is called <b>operating profit</b>. It shows the ability to meet interest, and feeds the interest coverage ratio and free cash flow to the firm.</li>
<li><b>PAT</b> (net profit, EAT) is what is left for shareholders after interest and tax.</li>
<li><b>Adjusted PAT</b> removes exceptional items, <b>with their tax impact</b>, so years can be compared. It may need judgement: Bharti Airtel's FY 2019 effective tax rate was "not meaningful" because it paid huge taxes despite reporting losses.</li>
</ul>

<h3 id="s5">8.5 Statement of changes in equity</h3>
<p>Required by Ind AS 1. Shows how each type of transaction changed each part of shareholders' equity.</p>
</section>

<section class="sec" id="s6"><span class="secno">8.6</span><h2>Cash flow</h2>
<p>Accounts use the <b>accrual</b> basis: income counts when earned, not when received; expenses when incurred, not when paid. So profit and cash can differ a lot.</p>
<div class="analogy">The book's example: buy goods for Rs 80,000 in cash, sell them for Rs 1,00,000. If the sale is in cash, you have a Rs 20,000 profit and the cash. If the sale is on credit, the P&amp;L still shows Rs 20,000 profit, but there is no money. If the customer never pays, even the Rs 80,000 is lost. Profit without cash is "paper profit".</div>
</div>

<figure class="fig" id="fig-cashflow"><figcaption>Three kinds of cash flow<span>Signs, as the book describes them</span></figcaption>
<div class="grid g3">
<div class="box hl"><span class="tag">Operating</span><h4>From the business (P&amp;L items)</h4><p>Net profit + non-cash expenses (depreciation, amortisation) &plusmn; changes in receivables and payables.</p></div>
<div class="box"><span class="tag">Investing</span><h4>From assets (B/S items)</h4><p>Buying assets: <b>negative</b>. Selling assets: <b>positive</b>.</p></div>
<div class="box"><span class="tag">Financing</span><h4>From liabilities and equity (B/S items)</h4><p>Borrowing or issuing equity: <b>positive</b>. Repaying debt or buying back equity: <b>negative</b>.</p></div>
</div></figure>

<div class="col">
<h3>A warning from Kingfisher Airlines</h3>
<p>A business with <b>negative operating cash flow</b> for years needs constant doses of borrowing or new equity. In the end it either turns cash-positive or dies when lenders and investors stop. The book's example (Rs crore, source moneycontrol.com):</p>
</div>

<figure class="fig" id="fig-kingfisher"><figcaption>Kingfisher Airlines, years ending March</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Rs crore</th><th>2013</th><th>2012</th><th>2011</th><th>2010</th><th>2009</th></tr></thead>
<tbody>
<tr><th>Net profit before tax</th><td>&minus;4,301.12</td><td>&minus;3,446.09</td><td>&minus;1,520.78</td><td>&minus;2,417.92</td><td>&minus;2,155.21</td></tr>
<tr><th>Net cash from operating activities</th><td>&minus;1,390.86</td><td>&minus;885.55</td><td>&minus;2.23</td><td>&minus;1,665.09</td><td>&minus;645.78</td></tr>
</tbody></table></div>
<p class="ptr" style="margin-top:8px">EBIT stayed far below interest for years, so it borrowed to pay interest, until lenders refused.</p>
</figure>

<div class="col">
<p>Expansion (negative investing cash flow) is funded by operating cash, past cash balances, or financing. Be cautious with firms that rely heavily on borrowing to expand: assets may realise less than book value, but liabilities must be paid in full.</p>
<div class="trap">Four rules from the book: <b>net cash flow can deceive</b>; analyse operating, investing and financing <b>separately</b>; focus on <b>sustainable, recurring</b> cash flows; adjust for <b>non-recurring</b> items.</div>
</section>

<section class="sec" id="s7"><span class="secno">8.7</span><h2>Notes to accounts</h2>
<h3>8.7.1 Significant accounting policies</h3>
<p>There are several ways to account for an item, for example <b>straight-line</b> or <b>written-down value</b> depreciation. The policies show which way the company chose. Companies must state any change from last year. <b>Frequent changes</b> in policy are a reason for suspicion of manipulation.</p>
<h3>8.7.2 Contingent liabilities</h3>
<p>Liabilities that arise only if an uncertain future event goes against the company. They are <b>not recorded in the accounts</b>, only in the notes. Examples: outstanding lawsuits, tax disputes, bank guarantees given, product warranty claims, pending investigations, changes in FX or government policy.</p>
<div class="trap">Management will usually say it does not expect to lose. Look at the <b>size</b> of contingent liabilities compared with the P&amp;L and balance sheet. If large, be cautious.</div>
<h3>Off-balance sheet items</h3>
<p>Any asset or liability that does not appear on the balance sheet. The book's examples: <b>operating leases</b>, <b>contingent liabilities</b>, and <b>derivative contracts</b> (shown only in notes). Derivatives have threatened many businesses worldwide, so analyse these in detail, especially negative surprises.</p>

<h3 id="s8">8.8 Points to keep in mind</h3>
<ul>
<li>Numbers can be dressed up by assumptions or creative accounting. Auditors' <b>qualifications</b> in the notes (the fine print) are very useful.</li>
<li>A <b>change in accounting period</b> can confuse comparisons with past years.</li>
<li>One-off items can raise or lower profit; miss them and the whole analysis changes.</li>
<li>The best company for investors shows <b>consistent</b> growth in sales, profit and net worth, lower debt, better margins and a rising <b>return on net worth (RoNW)</b>.</li>
</ul>

<h3 id="s9">8.9 The audit report</h3>
<p>Management prepares the accounts; auditors check that they give a <b>true and fair view</b>. Auditors work on the information given to them and cannot vouch for every transaction. So they check, in order: are adequate <b>control systems</b> in place; were they <b>properly implemented</b>; were <b>accounting standards</b> followed in measuring and disclosing items?</p>
</div>

<figure class="fig" id="fig-audit"><figcaption>Three kinds of audit report<span>As listed in the book</span></figcaption>
<div class="grid g3">
<div class="box gd"><span class="tag">Clean</span><h4>No issues</h4><p>Standard format, looks much the same across companies.</p></div>
<div class="box"><span class="tag">Disclaimer</span><h4>Could not verify</h4><p>Auditors could not verify part of the financials because information was not available.</p></div>
<div class="box bd"><span class="tag">Qualified</span><h4>Not true and fair</h4><p>Auditors believe all or part of the statements do not give a true and fair view: they disagree with a policy, or see serious discrepancies.</p></div>
</div>
<p class="ptr" style="margin-top:8px">For a disclaimer or a qualified report, auditors explain their reasons. Always read the audit report for reservations.</p>
</figure>

<div class="col">
<section class="sec" id="s10"><span class="secno">8.10</span><h2>Why ratios?</h2>
<p>A number alone means little. Bharti Airtel's FY 2019 EBIT of Rs 47.62 billion sounds large, until you compare it with revenue of Rs 807.8 billion (only 5.8%), or with interest expense of over Rs 110 billion (not enough to pay it). <span class="k">Ratio analysis</span> expresses one line item as a percentage or multiple of a related one. Only compare numbers that are related.</p>
</div>

<figure class="fig" id="fig-purposes"><figcaption>Three uses of ratio analysis<span>The book's Bharti Airtel FY 2019 example</span></figcaption>
<div class="grid g3">
<div class="box"><span class="tag">Descriptive</span><p>Adds a sense of proportion: operating profit was <b>5.8%</b> of revenue.</p></div>
<div class="box"><span class="tag">Diagnostic</span><p>Finds what went wrong: revenue fell <b>2.19%</b> but EBITDA fell <b>13.9%</b>. Network operating expense rose from <b>23.8%</b> to <b>27.6%</b> of revenue.</p></div>
<div class="box"><span class="tag">Predictive</span><p>Shows how costs behave: most costs stayed a steady % of sales (they move with sales); network costs rose as sales fell, so they are largely <b>fixed</b>. Two years of data is too little; more data gives more confidence.</p></div>
</div></figure>

<div class="col">
<h3 id="s11">8.11 Commonly used ratios</h3>
<p>Margins are thin in a competitive industry with pricing pressure. They are high when a business is unique with big entry barriers, or an early entrant in a sunrise industry. But very high profitability rarely lasts: new entrants and competition pull it back to moderate levels. Ratios that compare a period figure (sales, profit) with a balance sheet figure (equity, assets) should use the <b>average</b> balance, usually the average of opening and closing.</p>
</div>

<figure class="fig" id="fig-formulas"><figcaption>Ratio formula sheet<span>Formulas exactly as the book defines them, with the book's Bharti Airtel FY 2019 figures</span></figcaption>
<div class="scroll"><table class="cmp fs">
<thead><tr><th>Ratio</th><th>Formula</th><th>Reading it</th></tr></thead>
<tbody>
<tr><th colspan="3" style="color:var(--indigo)">Profitability</th></tr>
<tr><th>EBITDA margin</th><td>EBITDA &divide; Net sales</td><td>Operating efficiency; not affected by depreciation policy, funding or tax. Bharti: 32.2% (FY18: 36.6%)</td></tr>
<tr><th>PAT margin</th><td>PAT &divide; Net sales</td><td>Share of sales left for shareholders. Bharti: 2.1%</td></tr>
<tr><th>NOPAT</th><td>EBIT &times; (1 &minus; tax rate)</td><td>Used in valuation (later chapters)</td></tr>
<tr><th colspan="3" style="color:var(--indigo)">Return</th></tr>
<tr><th>ROE (RoNW)</th><td>PAT &divide; Net worth</td><td>"Single most important parameter" for equity investors. Net worth = share capital + reserves and surplus. Bharti: 2.1%</td></tr>
<tr><th>ROCE</th><td>EBIT &divide; Capital employed</td><td>Capital employed = total assets &minus; non-interest-bearing current liabilities, or equity + debt (book values). Pre-tax. Bharti: 2.38%</td></tr>
<tr><th colspan="3" style="color:var(--indigo)">Leverage</th></tr>
<tr><th>Debt / Equity</th><td>Total adjusted debt &divide; Net worth</td><td>Most conservative benchmark: <b>1 or less</b>. Bharti: 1.52x</td></tr>
<tr><th>Interest coverage</th><td>EBIT &divide; Interest expense</td><td>Below 1 or negative: earnings do not cover interest</td></tr>
<tr><th colspan="3" style="color:var(--indigo)">Liquidity</th></tr>
<tr><th>Current ratio</th><td>Current assets &divide; Current liabilities</td><td>Also called working capital ratio. Bharti: 0.35</td></tr>
<tr><th>Quick ratio</th><td>(Current assets &minus; Inventories) &divide; Current liabilities</td><td>Stricter: inventory cannot become cash immediately</td></tr>
<tr><th colspan="3" style="color:var(--indigo)">Efficiency</th></tr>
<tr><th>Receivable turnover</th><td>Revenue &divide; Average receivables</td><td>Higher is better: faster collection. Low may mean credit is too easy, or money is hard to recover</td></tr>
<tr><th>Payable turnover</th><td>Purchases &divide; Accounts payable</td><td>Low means long supplier credit: strength, or lack of cash</td></tr>
<tr><th>Asset turnover</th><td>Net sales &divide; Total assets</td><td>Higher is better: assets put to work. Used in DuPont</td></tr>
<tr><th>Inventory turnover</th><td>Sales &divide; Inventory</td><td>Higher is better. Slow stock locks up money, and perishables can spoil. High for FMCG, low for capital goods</td></tr>
</tbody></table></div></figure>

<div class="col">
<h3>Reading the liquidity ratios</h3>
<ul>
<li>High finished goods stock may mean slowing sales; high raw material stock may mean poor planning.</li>
<li>High receivables: selling on credit and struggling to collect. High payables: may show strength in getting good credit terms.</li>
<li>A current ratio <b>below 1</b> is <b>not always a red flag</b>. A company that collects cash on sales and pays suppliers on credit has its working capital funded by customers. Firms with strong bargaining power often <b>prefer</b> negative working capital: it is an interest-free obligation.</li>
<li>A very <b>high</b> current ratio may point to poor management of inventory, receivables and cash.</li>
</ul>
<div class="trap">ROE uses <b>PAT</b>; ROCE uses <b>EBIT</b>. ROE's denominator is net worth only; ROCE's is equity plus debt. Interest coverage uses <b>EBIT</b>, not PAT. Quick ratio removes <b>inventories</b>.</div>
<p class="ptr">The book notes several versions of ROCE and D/E are used in the industry (for example, net debt = total debt minus cash). For the exam, use the formulas in the sheet above.</p>
</section>

<section class="sec" id="s12"><span class="secno">8.12</span><h2>DuPont analysis</h2>
<p>Reading ratios together gives more insight. For example, sales rising while the collection period lengthens suggests lenient credit to push sales. <span class="k">DuPont analysis</span> breaks ROE into three parts:</p>
<div class="formula">ROE = (Net profit &divide; Sales) &times; (Sales &divide; Assets) &times; (Assets &divide; Equity)</div>
<div class="grid g3">
<div class="box gd"><span class="tag">1</span><h4>Net profit margin</h4><p>Profitability</p></div>
<div class="box gd"><span class="tag">2</span><h4>Asset turnover</h4><p>Efficiency</p></div>
<div class="box bd"><span class="tag">3</span><h4>Equity multiplier</h4><p>Leverage</p></div>
</div>
<div class="why"><b>Why split it?</b>ROE that rises from better margins or efficiency is good news. ROE that rises from more leverage need not be, because leverage also adds risk.</div>
</div>

<figure class="fig" id="fig-dupont"><figcaption>DuPont calculator<span>Starts with the book's HighLevCo. Press LowLevCo to compare.</span></figcaption>
<div class="calc">
<div class="btns" style="justify-content:flex-start;margin-top:0"><button class="btn sm" id="dp-high">HighLevCo (book)</button><button class="btn sm" id="dp-low">LowLevCo (book)</button></div>
<div class="calcin">
<div><label for="dp-s">Revenue</label><input type="number" id="dp-s" value="12000"></div>
<div><label for="dp-p">Net profit</label><input type="number" id="dp-p" value="2400"></div>
<div><label for="dp-a">Assets</label><input type="number" id="dp-a" value="5200"></div>
<div><label for="dp-e">Equity</label><input type="number" id="dp-e" value="2600"></div>
</div>
<div class="calcres">
<div><b id="dp-npm"></b><small>net profit margin</small></div>
<div><b id="dp-at"></b><small>asset turnover</small></div>
<div><b id="dp-em"></b><small>equity multiplier</small></div>
<div><b id="dp-roe"></b><small>ROE</small></div>
</div>
<p class="calcnote" id="dp-note"></p>
</div></figure>

<div class="col">
<p><b>The book's comparison.</b> HighLevCo: ROE <b>92.3%</b> = 20% margin &times; 2.3x turnover &times; 2.0x leverage. LowLevCo: ROE <b>52.4%</b> = 22% margin &times; 2.4x turnover &times; 1.0x leverage (no debt). LowLevCo is the better operator, with higher margin and slightly higher turnover. Its ROE is lower only because it uses no debt, which also means less risk.</p>

<h3 id="s13">8.13 Forecasting with ratios</h3>
<p>Analysts use how items behaved in the past to forecast. But that assumes the past represents the future, which need not hold. Apply judgement and adjust for changes.</p>
<div class="trap">The book's example: <b>Suzlon</b> was the only wind turbine maker, with great pricing power, until it faced tremendous domestic and offshore competition starting from the middle of 2000 (as the book puts it). Projecting its financials purely from history would have been a blunder.</div>
<p>Quotes from the book: Warren Buffett has "no use whatsoever for projections or forecasts" and looks deeply at <b>track records</b>. Charlie Munger says projections "do more harm than good". Graham and Dodd: a past trend is a fact, a future trend only an assumption, and the past is only a "rough index" to the future.</p>

<h3 id="s14">8.14 Peer comparison</h3>
<p>Comparing a company's ratios with those of peers in the same sector shows its competitive position. The book calls peer comparison <b>critical</b> for any research report. Databases give quick peer snapshots.</p>
</section>

<section class="sec" id="s15"><span class="secno">8.15</span><h2>Other things to track</h2>
<h3>History of equity expansion</h3>
<p>Raising money costs the business; if raised expensively, existing shareholders bear it. Debt costs are clear from the contract; the cost of issuing equity is harder to see. Ways to issue shares:</p>
<ul><li>Rights issue (to existing shareholders in proportion to holdings)</li><li>Public issue (IPO or FPO)</li><li>Private placement: preferential issue, qualified institutional placement (QIP)</li><li>Exercise of warrants</li><li>ESOPs or sweat equity</li></ul>
</div>

<figure class="fig" id="fig-dilution"><figcaption>Which issues dilute existing shareholders?<span>As the book explains</span></figcaption>
<div class="grid g2">
<div class="box gd"><span class="tag">Rights issue</span><p>No major dilution: offered to all in proportion. Dilutes <b>only those who do not take up</b> their rights.</p></div>
<div class="box"><span class="tag">Preferential allotment</span><p>Raises the chosen investor's stake, cuts everyone else's. Two views: dilution risk, <b>or</b> a sign that someone may bail the company out in a crisis. Check the situation and price: a <b>premium</b> price is value-accretive for minorities.</p></div>
<div class="box"><span class="tag">QIP</span><p>Dilutes, but likely shows <b>institutional confidence</b> in fundamentals.</p></div>
<div class="box gd"><span class="tag">Internal accruals</span><p>Growth funded from the company's own profits: very little dilution concern.</p></div>
</div></figure>

<div class="col">
<h3>Dividend and earnings history</h3>
<ul>
<li>Dividends plus capital gains make up an investor's total return.</li>
<li><b>Growth phase:</b> companies pay little or no dividend; shareholders do not mind if the company earns more on the money than they could.</li>
<li><b>Mature phase:</b> shareholders expect timely dividends. Predictability matters; high-yield stocks attract long-term income seekers.</li>
<li>Mature companies in <b>defensive</b> industries offer the most predictable dividends, often with interim dividends. Book examples: <b>Colgate Palmolive</b>, <b>Britannia</b>.</li>
<li>Some companies smooth dividends: build reserves in good years, use them in bad years.</li>
<li><b>Buybacks</b> (other than for stock-based compensation) are also a way to distribute profit; companies may prefer them for tax reasons, and they let investors choose to sell or raise their stake.</li>
</ul>
<div class="why"><b>Reading the signals</b>A strong company retaining more profit than usual may plan a big investment, or may expect hard times. A high-growth company raising its dividend may see fewer growth opportunities. When a dividend breaks sharply from the past, ask management why.</div>
<h3>History of corporate actions</h3>
<p>Dividends, bonuses, splits and rights affect the share price. Chapter 9 covers them.</p>
<h3>Insider buying and selling</h3>
<p>Owners know the business best, and trade within SEBI's guidelines. Their trades can give insight. Peter Lynch, quoted in the book: insiders sell for many reasons, which need not ring alarm bells, "but if insiders are buying, then there can be only one reason that the company is likely to make huge profits in future".</p>
<p class="ptr">The book's text gives Bharti Airtel's total debt as "Rs.12.87 billion" and core working capital as "negative Rs.2.36 billion", but its own tables (in Rs million) show 12,87,036 and minus 2,36,141. The quiz does not use these two figures.</p>
</section>

<section class="sec" id="traps"><h2>All exam traps in this chapter</h2>
<ol class="traplist">
<li>Statement format: Schedule III of the Companies Act, 2013 and Ind AS 1. Banks, insurers, utilities use their regulators' formats.</li>
<li>Ind AS 1 requires OCI in the P&amp;L statement, below net profit.</li>
<li>Control: more than 50% votes, or right to appoint the board majority, or de facto control (Ind AS 110).</li>
<li>SEBI (as per the book): consolidated annually, standalone quarterly.</li>
<li>Self-generated brands cannot be shown as assets; internally developed software can.</li>
<li>Goodwill = price paid minus fair value of net assets. Paying less goes to capital reserve.</li>
<li>Inventory: lower of cost or market value. Receivables: net of doubtful debt provision.</li>
<li>Investments in JVs and associates use the equity method.</li>
<li>Minority interest appears only in consolidated statements.</li>
<li>Provision: specific obligation. Reserve: no specific obligation.</li>
<li>Total debt includes current portion of long-term debt, finance leases and accrued interest.</li>
<li>Core working capital = inventory + receivables &minus; payables.</li>
<li>Raw material cost = purchases + opening stock &minus; closing stock.</li>
<li>Loss-making company: basic EPS = diluted EPS.</li>
<li>Gross profit usually cannot be computed for Indian companies.</li>
<li>EBITDA is best for comparing firms; EBIT is "operating profit".</li>
<li>Deferred tax has no cash impact.</li>
<li>Buying assets: negative investing cash flow. Borrowing: positive financing cash flow.</li>
<li>Contingent liabilities are not recorded in the accounts, only in notes.</li>
<li>Audit reports: clean, disclaimer, qualified.</li>
<li>ROE = PAT &divide; net worth. ROCE = EBIT &divide; capital employed. Use average balances.</li>
<li>D/E benchmark: 1 or less on the most conservative basis.</li>
<li>Current ratio below 1 is not always bad: customers may be funding working capital.</li>
<li>Inventory turnover is high for FMCG, low for capital goods.</li>
<li>DuPont: margin &times; asset turnover &times; equity multiplier. ROE from leverage adds risk.</li>
<li>Rights issues dilute only those who do not subscribe.</li>
<li>Insider buying is a stronger signal than insider selling (Peter Lynch).</li>
</ol>
</section>

<section class="sec" id="talk"><h2>For the group discussion</h2>
<ol class="talk">
<li>Pick a listed company. Do its standalone and consolidated revenues differ much? Why?</li>
<li>Why might a profitable company still run out of cash? Use the book's Rs 80,000 example.</li>
<li>Bharti Airtel's current ratio was 0.35. Is that a problem? Argue both sides.</li>
<li>Two companies have the same ROE. How would DuPont help you choose between them?</li>
<li>A company has made three preferential allotments in four years. What would you check?</li>
</ol>
</section>
</div>

<footer>Notes built from the NISM Series XV workbook (February 2026 version). Study aid only.</footer>
</div>
"""

WIDGETS = r"""
window.__WIDGETS__=function(){
const s=document.getElementById('dp-s'),p=document.getElementById('dp-p'),a=document.getElementById('dp-a'),e=document.getElementById('dp-e');
if(!s)return;
function set(v){s.value=v[0];p.value=v[1];a.value=v[2];e.value=v[3];calc()}
function calc(){const S=+s.value,P=+p.value,A=+a.value,E=+e.value;
 const ok=S>0&&A>0&&E>0;
 const npm=ok?P/S:0,at=ok?S/A:0,em=ok?A/E:0,roe=npm*at*em;
 document.getElementById('dp-npm').textContent=ok?(npm*100).toFixed(1)+'%':'-';
 document.getElementById('dp-at').textContent=ok?at.toFixed(2)+'x':'-';
 document.getElementById('dp-em').textContent=ok?em.toFixed(2)+'x':'-';
 document.getElementById('dp-roe').textContent=ok?(roe*100).toFixed(1)+'%':'-';
 document.getElementById('dp-note').textContent=!ok?'Enter positive revenue, assets and equity.':(em>1.5?'Much of this ROE comes from leverage (assets are '+em.toFixed(1)+' times equity). That adds risk.':'Little or no leverage: this ROE comes mainly from margin and asset turnover.');
}
[s,p,a,e].forEach(x=>x.addEventListener('input',calc));
document.getElementById('dp-high').addEventListener('click',()=>set([12000,2400,5200,2600]));
document.getElementById('dp-low').addEventListener('click',()=>set([11800,2620,5000,5000]));
calc();
};
"""
