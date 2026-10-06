LEARN = r"""
<style>
.calc{display:grid;gap:14px}
.calc label{display:block;font-weight:700;font-size:.92rem}
.calc input[type=number]{font:inherit;width:100%;padding:.45rem .6rem;border:1px solid var(--line);border-radius:8px;background:var(--paper);color:var(--ink)}
.calcin{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
@media (max-width:620px){.calcin{grid-template-columns:repeat(2,1fr)}}
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
<div class="kicker">Chapter 12 of 15</div>
<h1>Fundamentals of risk and return</h1>
<div class="meta"><span class="pill">Worth <b>7 marks</b> of 100</span><span class="pill">Book pages 228 to 246, and 334 to 341</span><span class="pill">About 75 minutes</span></div>
<p class="oneline">Measure the <span class="k">return</span> properly, name the <span class="k">risks</span> you took to earn it, and judge the return <span class="k">per unit of risk</span>. Then watch your own biases.</p>
</header>

<figure class="fig" id="fig-map"><figcaption>Chapter map<span>Twelve parts, plus the book's Annexure 3. 12.2 and 12.9 carry the numericals. Tap to jump.</span></figcaption>
<div class="map">
<a href="#s1"><b>12.1 and 12.2</b><span>Measuring return</span><small>ROI, simple, annualised, CAGR</small></a>
<a href="#s3"><b>12.3</b><span>Types of risk</span><small>Ten risks, systematic or not</small></a>
<a href="#s4"><b>12.4 and 12.5</b><span>Measuring risk</span><small>Standard deviation, beta, VaR</small></a>
<a href="#s6"><b>12.6 to 12.8</b><span>Judging an investment</span><small>Sensitivity, margin of safety, equity versus bonds</small></a>
<a href="#s9"><b>12.9</b><span>Risk-adjusted returns</span><small>Jensen, Sharpe, Treynor</small></a>
<a href="#s10"><b>12.10 to 12.12</b><span>Behaviour and liquidity</span><small>Biases, market wisdom, turnover ratios</small></a>
<a href="#ax3"><b>Annexure 3</b><span>Lessons from history</span><small>Barings, 2008, famous frauds</small></a>
</div></figure>

<div class="col">
<section class="sec" id="s1"><span class="secno">12.1</span><h2>Return on investment</h2>
<p>An investor expects two things: a <b>return</b>, and, more importantly, the <b>capital back</b>. Safety of capital matters as much as return. Judge a return by its <b>level</b>, its <b>volatility</b> and its <b>nature</b> (periodic income or capital gain).</p>
<p>A return in rupees means little on its own; compare it with the capital that earned it.</p>
<div class="formula">Return on investment (%) = (Net profit &divide; Investment) &times; 100</div>
<p>Higher is better, and it is simple to use. But be careful with investments whose returns are not known in advance, such as equity and mutual funds: their ROI is an estimate built on past returns and assumptions.</p>

<h3 id="s2">12.2 Simple, annualised and compounded returns</h3>
<p>A return measure should help investors judge whether the return is enough for their goals and risk, compare investments, and compare against a benchmark. <b>Total return</b> = periodic income (interest, dividend, rent) + change in value, whether realised or not. Gold and other commodities give no periodic income at all.</p>
</div>

<figure class="fig" id="fig-returns"><figcaption>One investment, three return figures<span>The book's example: 150 shares bought at Rs 25, sold at Rs 30, Rs 1 dividend per share, Rs 20 brokerage each way</span></figcaption>
<div class="flow">
<div class="step"><h4>Total cost</h4><p>150 &times; 25 + 20 = <b>Rs 3,770</b></p></div><div class="arrow"></div>
<div class="step"><h4>Total returns</h4><p>Sale 150 &times; 30 &minus; 20 = 4,480. Dividend 150. Total <b>Rs 4,630</b></p></div><div class="arrow"></div>
<div class="step hl"><h4>Simple (holding period) return</h4><p>4,630 &divide; 3,770 &minus; 1 = <b>23%</b></p></div>
</div>
<div class="grid g2" style="margin-top:12px">
<div class="box"><span class="tag">If held 15 months</span><h4>Simple annualised return</h4><p>(23% &divide; 15) &times; 12 = <b>18.4%</b></p><p>Divide by months (or days) held, multiply by 12 (or 365).</p></div>
<div class="box gd"><span class="tag">If held 5 years</span><h4>CAGR</h4><p>(4,630 &divide; 3,770)<sup>1/5</sup> &minus; 1 = <b>4.2%</b></p><p>Counts compounding.</p></div>
</div></figure>

<div class="col">
<div class="formula">CAGR = (End value &divide; Beginning value)<sup>1/n</sup> &minus; 1, where n = years held</div>
<ul>
<li>The simple return ignores <b>time</b>: 23% over one year is not the same as 23% over five.</li>
<li>Simple annualising ignores <b>compounding</b>. Most interest calculations assume compound interest.</li>
<li><span class="k">CAGR</span> assumes periodic returns are reinvested. It is the smoothed rate at which the investment grew. Actual yearly returns differ, and that difference reflects the risk.</li>
<li>CAGR is the accepted standard measure of return, <b>except for periods under one year</b>.</li>
<li>With several cash flows on different dates, use Excel's <b>XIRR</b>. The book's example: buy at Rs 150 on 31 July 2011; dividends of Rs 5, 6 and 4 each October; sell at Rs 165 on 15 January 2014. CAGR = <span class="num">8.06%</span>.</li>
</ul>
</div>

<figure class="fig" id="fig-retcalc"><figcaption>Try it: simple, annualised and CAGR<span>Defaults are the book's example held for 5 years (60 months)</span></figcaption>
<div class="calc">
<div class="calcin">
<div><label for="r-c">Total cost (Rs)</label><input type="number" id="r-c" value="3770"></div>
<div><label for="r-s">Sale proceeds (Rs)</label><input type="number" id="r-s" value="4480"></div>
<div><label for="r-i">Income received (Rs)</label><input type="number" id="r-i" value="150"></div>
<div><label for="r-m">Months held</label><input type="number" id="r-m" value="60" min="1"></div>
</div>
<div class="calcres">
<div><b id="r-hpr"></b><small>simple (holding period) return</small></div>
<div><b id="r-ann"></b><small>simple annualised</small></div>
<div><b id="r-cagr"></b><small>CAGR</small></div>
</div>
</div></figure>

<div class="col">
<section class="sec" id="s3"><span class="secno">12.3</span><h2>Risks in investments</h2>
<p><span class="k">Risk</span> is the volatility and uncertainty of returns and, at the extreme, loss of capital. An investment is also risky if actual returns differ from expected ones. A bank fixed deposit is low risk; equity is risky because dividends are uncertain and values swing. Higher return comes only with willingness to take higher risk. Investors should know which risks they face: a retired investor may accept low returns but not loss of capital.</p>
</div>

<figure class="fig" id="fig-risks"><figcaption>Ten risks, as described in the book</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Risk</th><th>What it is</th><th>Book's example or note</th></tr></thead>
<tbody>
<tr><th>Inflation (purchasing power)</th><td>Money received is worth less after inflation</td><td>Highest in fixed-return instruments: an 8% bond with 7% inflation earns 1% real. Lower for equity, as profits rise with prices. Venezuela 2018: inflation 65,370%; bonds became almost worthless; the Caracas index rose over 1,000 times</td></tr>
<tr><th>Interest rate</th><td>Bond prices fall when rates rise and rise when rates fall</td><td>Also hits equity: higher cost of capital lowers present value, borrowing and profits</td></tr>
<tr><th>Business</th><td>Risk in operations; measured as the standard deviation of EBIT or EBITDA</td><td>Includes commodity, operations, competition, supply chain and currency risk. Reduced by holding varied businesses</td></tr>
<tr><th>Market</th><td>Loss from adverse price moves in a traded asset</td><td>Affects equity, bonds, gold, real estate. Deposits and small savings have none, but also do not appreciate</td></tr>
<tr><th>Credit (default)</th><td>Issuer may not pay interest or principal</td><td>A sovereign has no default risk on local-currency debt (it can tax or print). Measured by credit ratings: AAA and A1 highest, D is default. Reduced by diversifying</td></tr>
<tr><th>Liquidity</th><td>Cannot sell when wanted, or only below value, or at high cost</td><td>Indian corporate bonds, property and art; lock-ins. Book: a Sovereign Gold Bond order book on 17 July 2020 had a bid-ask gap above Rs 80 (about 2%)</td></tr>
<tr><th>Call</th><td>A bond is called before maturity</td><td>Most common when rates are <b>falling</b>: issuers replace high-coupon bonds. Goes with reinvestment risk</td></tr>
<tr><th>Reinvestment</th><td>Coupons may have to be reinvested at a lower rate</td><td>Rates rise: risk falls. Rates fall: risk rises. A cumulative option avoids it (but a bond may then swing more in price)</td></tr>
<tr><th>Political</th><td>Unfavourable government action: nationalisation, tax or licensing changes</td><td>Almost all businesses are exposed</td></tr>
<tr><th>Country</th><td>Socio-economic-political-cultural risks of a country; it may not honour its commitments</td><td>A country default affects all securities issued there</td></tr>
</tbody></table></div></figure>

<div class="col">
<div class="analogy">Asha's fixed deposit pays her Rs 5,000 a month, enough for groceries. Prices rise 10%, and groceries now cost Rs 5,500. Her deposit is perfectly safe, yet she is poorer. That is inflation risk.</div>
<div class="trap">"Liquidity" has three meanings in the book: a <b>company's</b> ability to meet short-term obligations; an <b>asset's</b> ease of conversion into cash (shares and bonds easy, gold and real estate harder); and a <b>market's</b> depth of ready buyers and sellers. Check which one a question means.</div>
<h3>Systematic and unsystematic risk</h3>
</div>

<figure class="fig" id="fig-sysunsys"><figcaption>Can diversification remove it?<span>The book's classification</span></figcaption>
<div class="grid g2">
<div class="box bd"><span class="tag">Systematic (undiversifiable)</span><p>Felt across investments: government policy, external factors, wars, natural calamities.</p><p><b>Market, inflation, exchange rate, interest rate, reinvestment</b> risk.</p></div>
<div class="box gd"><span class="tag">Unsystematic (diversifiable)</span><p>Specific to one security or a small group. Reduced by adding other assets.</p><p><b>Credit, business, liquidity</b> risk.</p></div>
</div></figure>

<div class="col">
<ul>
<li><b>Ajay</b> buys shares of an infrastructure company. A change in the government's push for infrastructure hits all infra companies: unsystematic, reduced by investing in other sectors. Rising rates or a recession hit everyone: systematic, seen as market risk.</li>
<li><b>Ashima</b> buys bonds. She cuts credit risk by holding more highly rated bonds, but if rates rise, all her bonds fall: interest rate risk, common to all debt.</li>
</ul>
</section>

<section class="sec" id="s4"><span class="secno">12.4</span><h2>Measuring risk</h2>
<p>Risk is the variability of possible outcomes, both up and down, though we usually mean the downside. The book separates <b>risk</b> from <b>uncertainty</b>: when we know nothing about a cause (like a tsunami or COVID before they happened), it is uncertainty; once research explains the cause, it becomes a measurable risk. Risk is "known uncertainty".</p>
</div>

<figure class="fig" id="fig-measures"><figcaption>Three ways to measure risk</figcaption>
<div class="grid g3">
<div class="box"><span class="tag">1. Statistical</span><h4>Standard deviation</h4><p>Variability of returns around the mean. For a sample: s = &radic;[&Sigma;(X &minus; mean)&sup2; &divide; (n &minus; 1)].</p></div>
<div class="box"><span class="tag">2. Sensitivity</span><h4>Elasticity measures</h4><ul><li><b>Beta:</b> stock returns versus index returns; market (systematic) risk</li><li><b>Modified duration:</b> bond price versus interest rates; interest rate risk</li><li><b>Delta:</b> option price versus the underlying's price; market risk</li></ul></div>
<div class="box"><span class="tag">3. Loss</span><h4>Value at Risk (VaR)</h4><p>Maximum loss over a period at a given confidence level. VaR (1%) of 12%: 99% confident the loss will not exceed 12%; a 1% chance it will. Confidence level = 1 &minus; significance level.</p></div>
</div></figure>

<div class="col">
<h3 id="s5">12.5 Beta</h3>
<p><span class="k">Beta</span> measures <b>systematic risk</b> relative to the market index: the risk that cannot be diversified away. It is used in CAPM (Chapter 10).</p>
<div class="grid g3">
<div class="box"><h4>Beta = 1</h4><p>Moves with the market. Market +10%: stock +10%.</p></div>
<div class="box gd"><h4>Beta below 1</h4><p>Less volatile than the market.</p></div>
<div class="box bd"><h4>Beta above 1</h4><p>More volatile. Beta 1.2, market +15%: stock +18%.</p></div>
</div>
<div class="why"><b>Not everyone trusts beta</b>Value investor Seth Klarman, quoted in the book, calls it "preposterous" that one number from past price moves could describe a security's risk. Beta ignores business fundamentals and the price paid (IBM at $50 is less risky than at $100), and assumes upside and downside are equal. Past volatility does not reliably predict future performance.</div>
</section>

<section class="sec" id="s6"><span class="secno">12.6</span><h2>Sensitivity analysis</h2>
<p>A valuation model is only as good as its inputs. Identify the critical variables and see how the value changes when <b>one variable changes and all others stay constant</b>. That is <span class="k">sensitivity analysis</span>. Example: in a DCF, run the valuation at several discount rates and tabulate the results. <b>Scenario analysis</b> instead takes a best case, a worst case and the most likely case.</p>

<h3 id="s7">12.7 Margin of safety</h3>
<p>Popularised by <b>Benjamin Graham</b>, "the father of value investing", and followers such as Warren Buffett. <span class="k">Margin of safety</span> is the gap between value and price when a security is bought well <b>below its intrinsic value</b>. The bigger the gap, the bigger the margin.</p>
<ul>
<li>It allows investing with minimal downside risk, but does <b>not guarantee</b> success.</li>
<li>It gives a <b>cushion</b> against errors in the analyst's valuation, which is subjective anyway.</li>
<li>There is <b>no universal standard</b> for how wide it should be; each investor sets their own.</li>
</ul>
<div class="analogy">An engineer rates a bridge for 30 tonnes but lets only 10-tonne trucks cross. The gap covers the mistakes nobody knows they made.</div>

<h3 id="s8">12.8 Equity returns versus bond returns</h3>
</div>

<figure class="fig" id="fig-eqbond"><figcaption>How bond and equity returns differ</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th></th><th>Bonds</th><th>Equity</th></tr></thead>
<tbody>
<tr><th>Main source of return</th><td>Coupon income, plus some gain when rates fall</td><td>Appreciation in value; dividend is a small part</td></tr>
<tr><th>Assurance</th><td>Pre-defined coupon; may be secured</td><td>No assurance of dividend or appreciation</td></tr>
<tr><th>Risk and return</th><td>Lower risk, so lower return</td><td>Higher risk</td></tr>
<tr><th>Primary risk</th><td>Default risk: higher credit risk means higher interest</td><td>Company performance and the economy</td></tr>
</tbody></table></div></figure>

<div class="col">
<p>Buffett, as quoted in the book: compare the returns on bonds and stocks when deploying capital. If stocks offer more, buy stocks; if bonds offer more, buy bonds. In distress, rates fall sharply and equities may be "dirt cheap" even on dividend yield.</p>
</section>

<section class="sec" id="s9"><span class="secno">12.9</span><h2>Risk-adjusted returns</h2>
<p>A high-risk strategy usually earns more in the long run but swings more. So compare portfolios on return <b>per unit of risk</b>. For all three measures below, <b>higher is better</b>.</p>
</div>

<figure class="fig" id="fig-riskadj"><figcaption>Jensen's alpha, Sharpe, Treynor</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Measure</th><th>Formula</th><th>Risk used</th><th>Suits (as per the book)</th></tr></thead>
<tbody>
<tr><th>Jensen's alpha</th><td>Portfolio return &minus; [Rf + &beta; &times; market risk premium]</td><td>Beta (systematic). Excess over the CAPM return</td><td>&nbsp;</td></tr>
<tr><th>Sharpe ratio</th><td>(Portfolio return &minus; Rf) &divide; Standard deviation</td><td>Total risk (standard deviation)</td><td>Investors with much of their wealth in one investment, <b>not adequately diversified</b></td></tr>
<tr><th>Treynor ratio</th><td>(Portfolio return &minus; Rf) &divide; Beta</td><td>Beta (systematic)</td><td>Investors who have <b>adequately diversified</b> across asset classes</td></tr>
</tbody></table></div></figure>

<figure class="fig" id="fig-rcalc"><figcaption>Try it: risk-adjusted returns<span>All rates in % a year</span></figcaption>
<div class="calc">
<div class="calcin">
<div><label for="k-rp">Portfolio return</label><input type="number" id="k-rp" value="15" step="0.5"></div>
<div><label for="k-rf">Risk-free rate</label><input type="number" id="k-rf" value="6" step="0.25"></div>
<div><label for="k-sd">Standard deviation</label><input type="number" id="k-sd" value="12" step="0.5"></div>
<div><label for="k-b">Beta</label><input type="number" id="k-b" value="1.2" step="0.05"></div>
</div>
<div class="calcin" style="grid-template-columns:repeat(4,1fr)">
<div><label for="k-mrp">Market risk premium</label><input type="number" id="k-mrp" value="7" step="0.5"></div>
</div>
<div class="calcres">
<div><b id="k-sh"></b><small>Sharpe ratio</small></div>
<div><b id="k-tr"></b><small>Treynor ratio</small></div>
<div><b id="k-ja"></b><small>Jensen's alpha</small></div>
</div>
<p class="calcnote" id="k-note"></p>
</div></figure>

<div class="col">
<div class="trap">Sharpe divides by <b>standard deviation</b>; Treynor divides by <b>beta</b>. Jensen's alpha is a <b>difference</b> (return minus the CAPM return), not a ratio. The book says Jensen's alpha "factors the systematic risk using equity beta".</div>
</section>

<section class="sec" id="s10"><span class="secno">12.10</span><h2>Behavioural biases</h2>
<p>Classical finance assumes people are rational. In practice, emotion and psychology drive decisions. Benjamin Graham, in "The Intelligent Investor", said markets are more psychological and less logical. <b>Behavioural finance</b> combines psychology with economics to explain irrational financial decisions. Simon Savage of GLG Partners, quoted in the book: "We were all born to be bad fund managers because of inbuilt behavioural biases."</p>
</div>

<figure class="fig" id="fig-biases"><figcaption>Eight biases to watch</figcaption>
<div class="grid g2">
<div class="box"><span class="tag">Loss aversion</span><p>Strongly preferring to avoid losses over making gains. The pain of a loss is about <b>twice</b> as strong as the pleasure of an equal gain. Leads to inaction: holding losers, avoiding equity when volatility is in the news.</p></div>
<div class="box"><span class="tag">Confirmation (my-side) bias</span><p>Seeking or reading information so it confirms what you already believe. A trader whose reason for buying fails invents a new reason to hold.</p></div>
<div class="box"><span class="tag">Ownership bias (endowment effect)</span><p>Valuing what you own more than others would. You hold positions you would not buy at today's price.</p></div>
<div class="box"><span class="tag">Gambler's fallacy</span><p>Predicting random events from the past: believing something that happened often will now happen less, or the reverse, to "balance" things.</p></div>
<div class="box"><span class="tag">Winner's curse</span><p>Winning a competitive bid by overpaying. A behavioural win, a financial loss.</p></div>
<div class="box"><span class="tag">Herd mentality</span><p>Following others in the belief they know more. Leads to bubbles and crashes; small investors enter when markets are overheated. Keynes: "It is better for reputations to fail conventionally than to succeed unconventionally."</p></div>
<div class="box"><span class="tag">Anchoring</span><p>Relying too much on the first piece of information. Waiting for a "right price" to sell that is no longer realistic, and ignoring new information.</p></div>
<div class="box"><span class="tag">Projection bias</span><p>Projecting the recent past into the distant future, ignoring the more distant past.</p></div>
</div></figure>

<div class="col">
<h3 id="s11">12.11 Wisdom from investment gurus</h3>
<p>Markets move in <b>bull</b> and <b>bear</b> cycles. Great investors teach discipline through both.</p>
<ul>
<li><b>Bull market</b>: buyers pay higher and higher prices. Businesses are growing fast with strong demand, or there is just a change in perception or too much liquidity. It can overdo it: prices go past intrinsic value, firms borrow for expansion on rosy forecasts, and input, labour and interest costs rise near the peak. Unrealistic prices tend to correct with a crash.</li>
<li><b>Bear market</b>: prices fall. Businesses face lower demand, higher costs and less access to capital; some fail. Sellers quit in despair. When prices fall well below value, buyers return, central banks cut rates, and the next bull cycle slowly begins.</li>
</ul>
<div class="why"><b>Graham's Mr. Market</b>You own a business with a partner, Mr. Market, who offers every day to buy your share or sell you his, at prices swayed by his moods. Do not let his emotions drive yours. Use his mispricing as an opportunity.</div>
</div>

<figure class="fig" id="fig-quotes"><figcaption>Quotes the book collects</figcaption>
<div class="grid g2">
<div class="box"><span class="tag">Benjamin Graham</span><p>"In the short run, market is a voting machine but in the long run, it is a weighing machine."</p><p>"To achieve satisfactory investment results is easier than most people realize; to achieve superior results is harder than it looks."</p></div>
<div class="box"><span class="tag">Warren Buffett</span><p>"Rule No.1 is never lose money. Rule No.2 is never forget rule number one."</p></div>
<div class="box"><span class="tag">John Templeton</span><p>"Invest at the point of maximum pessimism."</p></div>
<div class="box"><span class="tag">Peter Lynch</span><p>"Go for a business that any idiot can run, because sooner or later, any idiot is probably going to run it."</p></div>
<div class="box"><span class="tag">David Dreman</span><p>"Psychology is probably the most important factor in the market, and one that is least understood."</p></div>
<div class="box"><span class="tag">Walter Schloss</span><p>"If you can't find good value investing positions, park your money in cash."</p></div>
<div class="box"><span class="tag">Charlie Munger</span><p>"Understanding how to be a good investor makes you a better business manager and vice versa."</p></div>
</div></figure>

<div class="col">
<h3 id="s12">12.12 Measuring liquidity of shares</h3>
<p>Stock exchanges exist to provide liquidity, but not every share is liquid: liquidity needs many buyers and sellers.</p>
<div class="grid g2">
<div class="box"><h4>Stock turnover ratio</h4><p>Shares traded in a period (usually a year) &divide; <b>free float</b> shares outstanding.</p><p class="ptr">Free float: shares held by non-promoter shareholders.</p></div>
<div class="box"><h4>Traded value turnover ratio</h4><p>Traded value of shares &divide; market capitalisation.</p></div>
</div>
</section>

<section class="sec" id="ax3"><span class="secno">A3</span><h2>Annexure 3: Lessons from history</h2>
<p>The book ends with real cases from market history. Its point: life is too short to learn only from your own mistakes, so learn from others'. It quotes Mark Twain: "We learn from the past that we don't learn from the past."</p>
<h3>Case 1: the Barings collapse</h3>
<p><b>Nick Leeson</b> headed derivatives trading at <b>Barings Futures Singapore</b>, a subsidiary of Barings Plc, London. He was a star trader and a favourite of top management. He ran both the <b>front office</b> (trading) and the <b>back office</b> (checking and reporting).</p>
</div>

<figure class="fig" id="fig-barings"><figcaption>How Barings fell<span>Annexure 3, Case 1</span></figcaption>
<div class="flow">
<div class="step"><h4>The bet</h4><p>Sold many <b>straddles</b> (a call and a put sold together) on Nikkei 225 index futures, on SGX-DT in Singapore and the Osaka Securities Exchange. A straddle loses if the market moves sharply either way. It was a bet that Japan's market would stay stable.</p></div><div class="arrow"></div>
<div class="step"><h4>The shock</h4><p>A violent earthquake hit <b>Kobe</b>. The Nikkei fell and the put side of his straddles lost money.</p></div><div class="arrow"></div>
<div class="step"><h4>Doubling down</h4><p>Instead of cutting the loss, he bought huge long Nikkei futures on both exchanges to hold the index up. He told London it was arbitrage between the two exchanges, and told each exchange he had opposite positions on the other.</p></div><div class="arrow"></div>
<div class="step"><h4>The collapse</h4><p>One trader could not turn the market. It kept falling, and Barings failed on both the futures and the straddles. The exchanges stayed safe because they had collected margins.</p></div>
</div></figure>

<div class="col">
<h3>Five lessons from Barings</h3>
<ol>
<li><b>One trader cannot move the market.</b> Work with the market and manage the position: here, cut the loss on the short puts.</li>
<li><b>Set clear position limits</b> for each trader, by product, market or total exposure, and tell every trader.</li>
<li><b>Monitor the limits closely.</b> Leeson broke his limits and sent false reports, which went unnoticed because he ran the back office himself. Keep front and back office under different people. Systems should block a trader at the limit.</li>
<li><b>Exchanges should share information</b> on large positions. The two exchanges competed for Nikkei business and never cross-checked. Sharing also deters manipulation across two exchanges.</li>
<li><b>Big institutions are as prone to risk as individuals.</b> Collect margins from everyone, on time. SEBI applies margins to all categories of participants, including institutions.</li>
</ol>
<p>Lessons 1 to 3 are for trading firms, 4 for exchanges, and 5 is the one SEBI has acted on in India.</p>
<div class="why"><b>The book's verdict</b>"Barings' failure was not the derivatives failure, it was management's failure." The Board of Banking Supervision blamed poor operational controls (<b>operational risk</b>), not derivatives. Afterwards, firms worldwide separated front and back office, exchanges began sharing information, and all positions came to be margined.</div>

<h3>Case 2: the credit event of 2008</h3>
</div>

<figure class="fig" id="fig-2008"><figcaption>How the 2008 crisis built up<span>Annexure 3, Case 2. The book's account, from 2003 to 2004 onwards</span></figcaption>
<div class="grid g2">
<div class="box"><span class="tag">Banks</span><p>Lent to less creditworthy borrowers and loosened <b>loan to value</b> (for example from 80:20 to 85:15) to earn higher margins (NIMs). They assumed ever-rising house prices would cover any default: a view on real estate, which is not a banker's job.</p></div>
<div class="box"><span class="tag">Selling the loans</span><p>To lend more, banks sold long-dated mortgages to investors at lower yields, booked the profit up front and earned bigger bonuses. They stopped caring about credit quality as long as someone bought: <b>moral hazard</b>. Lending became a fee business.</p></div>
<div class="box"><span class="tag">Home buyers</span><p>Got almost 100% financing, so they treated a house like a <b>call option</b>: if prices rose, sell and keep the profit; if prices fell, hand the keys to the bank.</p></div>
<div class="box"><span class="tag">Investors and raters</span><p>Funds bought <b>mortgage-backed securities</b> and passed them on, like passing the pillow. Rating agencies gave them top grades (AAA kind) based on history and the hard assets behind them. Many credit derivatives were written on them too.</p></div>
</div>
<p style="margin-top:12px">When prices began to fall, defaults rose and it came down like a pack of cards. The last holders were left with securities worth a couple of cents to the dollar.</p>
</figure>

<div class="col">
<h3>Lessons from 2008</h3>
<ul>
<li><b>Banks</b> are leveraged, so they must stay disciplined. Their business is lending, not betting on asset prices. Risk management is the heart of banking; never dilute it to win business.</li>
<li><b>Investors</b> should do their own due diligence, not just rely on rating agencies, and keep asking: "What could go wrong here?"</li>
<li>History matters, but decisions cannot rest <b>only</b> on historical data. Rating agencies leaned on past mortgage data. The book notes no rating agency ever stood up to take responsibility.</li>
<li>Respect the limits of what you understand. Nassim Taleb: "Black Swan events pose significant risk in this integrated world." Risk management should come first.</li>
</ul>
<h3>Frauds the book lists</h3>
<p>Warren Buffett: "People with pen do much bigger thefts than the people with guns."</p>
</div>

<figure class="fig" id="fig-frauds"><figcaption>Disgraced companies and fund managers<span>Facts as stated in the book</span></figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Who</th><th>What happened</th><th>Outcome in the book</th></tr></thead>
<tbody>
<tr><th>Enron</th><td>Power trading company. Massive accounting fraud wiped out <b>$78 billion</b> of market value</td><td>Bankrupt in <b>2001</b>. Former President Jeff Skilling: 24 years in prison</td></tr>
<tr><th>WorldCom</th><td>Telecom giant. Top management manipulated the financials; once had over <b>$100 billion</b> in assets</td><td>Fraud-induced bankruptcy in <b>2002</b>. Former CEO Bernard Ebbers: 25 years</td></tr>
<tr><th>Satyam Computers</th><td>Promoter <b>Ramalinga Raju</b> confessed in <b>2009</b> to inflating cash and bank balances by about <b>Rs 5,000 crore</b>, after a failed bid to buy Maytas, another promoter-owned company</td><td>Jailed on fraud charges. Satyam was later acquired by <b>Tech Mahindra</b></td></tr>
<tr><th>Bernard Madoff</th><td>New York money manager. <b>$65 billion Ponzi scheme</b>, the largest financial fraud in US history, exposed in December 2008</td><td>Sentenced in June 2009 to <b>150 years</b></td></tr>
<tr><th>Michael Milken</th><td>Drexel's "<b>Junk Bond King</b>" of the mid-1980s. Brought down by <b>insider trading</b></td><td>10 years in prison; $600 million fine</td></tr>
<tr><th>Raj Rajaratnam</th><td>Co-founded hedge fund <b>Galleon Group</b> in 1997. Arrested in October 2009 for <b>insider trading</b></td><td>Sentenced in October 2011 to 11 years and a $10 million fine</td></tr>
</tbody></table></div></figure>
</section>

<section class="sec" id="traps"><h2>All exam traps in this chapter</h2>
<ol class="traplist">
<li>ROI = net profit &divide; investment &times; 100. Safety of capital matters as much as return.</li>
<li>Simple (holding period) return ignores time; simple annualising ignores compounding.</li>
<li>Simple annualised = HPR &divide; months &times; 12.</li>
<li>CAGR = (end &divide; beginning)<sup>1/n</sup> &minus; 1. The standard measure, except for periods under one year.</li>
<li>Multiple cash flows on different dates: use XIRR.</li>
<li>Inflation risk is highest for fixed-return instruments and lower for equity.</li>
<li>Bond prices move opposite to interest rates.</li>
<li>Business risk is measured as the standard deviation of EBIT or EBITDA.</li>
<li>Deposits and small savings have no market risk.</li>
<li>A sovereign has no default risk on local-currency borrowing.</li>
<li>Credit ratings: AAA and A1 highest, D default. SEBI standardised the symbols.</li>
<li>Call risk is most prevalent when rates are falling.</li>
<li>Reinvestment risk rises when rates fall and falls when rates rise.</li>
<li>Systematic: market, inflation, exchange rate, interest rate, reinvestment. Unsystematic: credit, business, liquidity.</li>
<li>Beta measures market risk; modified duration, interest rate risk; delta, option sensitivity.</li>
<li>VaR (1%) of 12%: 99% confident the loss will not exceed 12%.</li>
<li>Beta above 1: more volatile than the market. Beta 1.2 and market +15% gives +18%.</li>
<li>Sensitivity analysis changes one variable at a time; scenario analysis uses best, worst and most likely cases.</li>
<li>Margin of safety: Benjamin Graham; no universal standard; no guarantee.</li>
<li>Jensen's alpha = Rp &minus; [Rf + &beta; &times; MRP]. Sharpe uses SD; Treynor uses beta.</li>
<li>Sharpe suits undiversified investors; Treynor suits well-diversified ones.</li>
<li>Loss aversion: losses hurt about twice as much as equal gains please.</li>
<li>Ownership bias is also called the endowment effect. Confirmation bias is also called my-side bias.</li>
<li>Graham: short run a voting machine, long run a weighing machine.</li>
<li>Stock turnover ratio uses free float shares; traded value turnover uses market cap.</li>
<li>Barings: "not the derivatives failure, it was management's failure". The root cause was operational risk: one person ran front and back office.</li>
<li>A short straddle loses if the market moves sharply either way. Leeson's was a bet on a stable Nikkei.</li>
<li>2008: banks diluted loan to value, sold loans on (moral hazard), and investors leaned on AAA ratings without their own due diligence.</li>
</ol>
</section>

<section class="sec" id="talk"><h2>For the group discussion</h2>
<ol class="talk">
<li>Your fixed deposit earns 7% and inflation is 6%. Your friend's equity fund fell 10% this year. Who took more risk?</li>
<li>Which bias do you recognise most in your own investing? Give a real example.</li>
<li>Klarman says beta is a poor measure of risk. Do you agree? What would you use instead?</li>
<li>Two funds both returned 18%. What else would you ask before choosing one?</li>
<li>How wide a margin of safety would you want before buying a share? Why that number?</li>
<li>Barings and 2008 were both called failures of management, not of the products. Do you agree?</li>
</ol>
</section>
</div>

<footer>Notes built from the NISM Series XV workbook (February 2026 version). Study aid only.</footer>
</div>
"""

WIDGETS = r"""
window.__WIDGETS__=function(){
const g=id=>document.getElementById(id);
const pct=v=>isFinite(v)?(Math.round(v*1000)/10).toFixed(1)+'%':'-';
if(g('r-c')){
 const rc=()=>{const c=+g('r-c').value,s=+g('r-s').value,i=+g('r-i').value,m=+g('r-m').value;
  if(!(c>0)||!(m>0)){['r-hpr','r-ann','r-cagr'].forEach(x=>g(x).textContent='-');return}
  const h=(s+i)/c-1;g('r-hpr').textContent=pct(h);g('r-ann').textContent=pct(h/m*12);
  g('r-cagr').textContent=m<12?'under 1 year':pct(Math.pow((s+i)/c,12/m)-1);};
 ['r-c','r-s','r-i','r-m'].forEach(x=>g(x).addEventListener('input',rc));rc();}
if(g('k-rp')){
 const kc=()=>{const rp=+g('k-rp').value,rf=+g('k-rf').value,sd=+g('k-sd').value,b=+g('k-b').value,mrp=+g('k-mrp').value;
  g('k-sh').textContent=sd>0?((rp-rf)/sd).toFixed(2):'-';
  g('k-tr').textContent=b!==0?((rp-rf)/b).toFixed(2):'-';
  const ja=rp-(rf+b*mrp);g('k-ja').textContent=(Math.round(ja*100)/100)+'%';
  g('k-note').textContent='Expected return by CAPM = '+rf+' + '+b+' x '+mrp+' = '+(Math.round((rf+b*mrp)*100)/100)+'%. Higher is better for all three.';};
 ['k-rp','k-rf','k-sd','k-b','k-mrp'].forEach(x=>g(x).addEventListener('input',kc));kc();}
};
"""
