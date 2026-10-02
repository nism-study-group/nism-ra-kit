LEARN = r"""
<style>
.calc{display:grid;gap:14px}
.calc label{display:block;font-weight:700;font-size:.92rem}
.calc input[type=number]{font:inherit;width:100%;padding:.45rem .6rem;border:1px solid var(--line);border-radius:8px;background:var(--paper);color:var(--ink)}
.calcin{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
@media (max-width:620px){.calcin{grid-template-columns:repeat(2,1fr)}}
.calcres{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
@media (max-width:520px){.calcres{grid-template-columns:repeat(2,1fr)}}
.calcres div{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:.6rem;text-align:center}
.calcres b{display:block;font-family:var(--head);font-size:1.45rem}
.calcres small{color:var(--muted)}
.calcnote{font-weight:700;margin:.2rem 0 0}
.calch{font-family:var(--head);font-weight:700;color:var(--indigo);margin:.2rem 0 -.3rem}
.formula{font-family:var(--head);font-weight:700;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.55rem .8rem;margin:.7rem 0;overflow-x:auto}
</style>
<div class="wrap">
<header class="hero">
<div class="kicker">Chapter 10 of 15</div>
<h1>Valuation principles</h1>
<div class="meta"><span class="pill">Worth <b>12 marks</b> of 100</span><span class="pill">Book pages 198 to 217</span><span class="pill">About 75 minutes</span></div>
<p class="oneline"><span class="k">Price</span> is what you pay; <span class="k">value</span> is what you get. Estimate value from <span class="k">cash flows</span>, or compare with <span class="k">similar companies</span>.</p>
</header>

<figure class="fig" id="fig-map"><figcaption>Chapter map<span>Thirteen parts. 10.5 (DCF) and 10.7 to 10.8 (multiples) carry the numericals. Tap to jump.</span></figcaption>
<div class="map">
<a href="#s1"><b>10.1 to 10.3</b><span>Price, value, sources</span><small>Why value, earnings and assets</small></a>
<a href="#s4"><b>10.4</b><span>Three approaches</span><small>Cost, intrinsic, relative</small></a>
<a href="#s5"><b>10.5</b><span>Discounted cash flow</span><small>DDM, FCFE, FCFF, CAPM, WACC</small></a>
<a href="#s7"><b>10.6 and 10.7</b><span>Earnings multiples</span><small>Dividend yield, P/E, PEG, EV/EBITDA, EV/Sales</small></a>
<a href="#s8"><b>10.8</b><span>Asset multiples</span><small>P/B, EV/capital employed, NAV, others</small></a>
<a href="#s9"><b>10.9 to 10.13</b><span>Putting it together</span><small>Trading versus transaction multiples, SOTP, new age, cautions</small></a>
</div></figure>

<div class="col">
<section class="sec" id="s1"><span class="secno">10.1</span><h2>Price is not value</h2>
<div class="why"><b>Two quotes from the book</b>Seth Klarman: "In capital markets, price is set by the most panicked seller; value, which is determined by cash flows and assets, is not." Warren Buffett: <b>"Price is what you pay and Value is what you get."</b></div>
<p><b>Price</b> comes from the stock market and is known to all. <b>Value</b> is the valuer's own estimate at a point in time. No formula gives a precise number, because the inputs are uncertain. At best, value is an <b>educated estimate</b>. That is why valuation is called both an <span class="k">art and a science</span>: it needs knowledge, experience and professional judgement.</p>

<h3 id="s2">10.2 Why value a business?</h3>
<div class="grid g3">
<div class="box"><p>Buying a business as an investment</p></div>
<div class="box"><p>Selling a business as an investment</p></div>
<div class="box"><p>Mergers and acquisitions</p></div>
<div class="box"><p>Owners' general sense of what it is worth</p></div>
<div class="box"><p>Fair treatment of stakeholders in an equity swap</p></div>
<div class="box"><p>Accounting, tax, regulatory and legal needs</p></div>
</div>
<p>Whatever the reason, the purpose is to <b>relate price to value</b>: is it fairly priced, over-priced or under-priced? Because of the uncertainty, valuers usually present <b>several scenarios</b> showing how value changes with the main inputs.</p>

<h3 id="s3">10.3 Where value comes from: earnings and assets</h3>
<p>Buffett, quoted in the book: <b>"There are only two sources of value in a business: Earnings and Assets."</b> Every asset produces periodic earnings plus a final inflow when it is sold.</p>
</div>

<figure class="fig" id="fig-sources"><figcaption>Two streams of cash from every asset</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Asset</th><th>Periodic earnings</th><th>One-time inflow</th></tr></thead>
<tbody>
<tr><th>Bond</th><td>Coupons</td><td>Redemption or sale</td></tr>
<tr><th>Equity share</th><td>Dividends</td><td>Sale of the share</td></tr>
<tr><th>Real estate</th><td>Rent</td><td>Appreciated value on sale</td></tr>
<tr><th>Business</th><td>Earnings (cash flows)</td><td>Sale of tangible and intangible assets, if earnings fall short</td></tr>
</tbody></table></div></figure>

<div class="col">
<div class="analogy">Lenders think the same way. A bank first checks whether the borrower's cash flows can repay the loan. The collateral is only a fallback if those estimates prove wrong. As the book warns, assets may be worth much less than their balance sheet value, but liabilities must be paid in full.</div>
</section>

<section class="sec" id="s4"><span class="secno">10.4</span><h2>Three approaches to valuation</h2>
</div>

<figure class="fig" id="fig-approaches"><figcaption>Cost, intrinsic, relative<span>The book focuses on the last two</span></figcaption>
<div class="grid g3">
<div class="box"><span class="tag">1</span><h4>Cost based</h4><p>Value = cost to create the asset. Suits only a buyer choosing between <b>buying and making</b>. Most stock market investors cannot build the company themselves, so it is generally <b>not suitable for financial investors</b>. Strategic, long-term investors may use it. Often needs technical assessment by engineers.</p></div>
<div class="box hl"><span class="tag">2</span><h4>Cash flow based (intrinsic)</h4><p>Value = what an investor would pay for the asset's cash flows, discounted at the return they expect.</p><ul><li><b>Risk neutral:</b> cash flows adjusted for probability, discounted at the <b>risk-free rate</b>. Used for <b>insurance companies</b> (embedded value and appraisal value).</li><li><b>Real world:</b> most likely cash flows, discounted at risk-free rate <b>plus a risk premium</b>.</li></ul></div>
<div class="box"><span class="tag">3</span><h4>Selling price based (relative)</h4><p>Value from the prices of <b>similar assets</b>, using ratios such as P/E, P/B, EV/EBITDA.</p></div>
</div></figure>

<div class="col">
<section class="sec" id="s5"><span class="secno">10.5</span><h2>Discounted cash flow (DCF)</h2>
<p>Start with a bond. It pays 9% a year and repays its face value of Rs 1,00,000 after 10 years. Investors also expect 9% for this maturity and credit quality. Its value today is the present value of all its cash flows at 9%, which comes to exactly the <b>face value</b>. If investors expect more than 9%, the value is below face value; if less, above.</p>
<p>Every asset is valued the same way. For equity, dividends replace coupons and the sale price replaces redemption. The difference: a bond's cash flows and timing are <b>known</b>; equity's are <b>uncertain</b>. So DCF valuations of businesses carry significant judgement error and can be very sensitive to some inputs.</p>
</div>

<figure class="fig" id="fig-dcfneeds"><figcaption>DCF works best when three things are known<span>Then the rest is simple present-value mathematics</span></figcaption>
<div class="flow">
<div class="step"><h4>1. Future cash flows</h4><p>The stream of free cash flows (inflows over outflows)</p></div><div class="arrow"></div>
<div class="step"><h4>2. Their timing</h4><p>When each cash flow arrives</p></div><div class="arrow"></div>
<div class="step"><h4>3. Discount rate</h4><p>The return investors expect</p></div><div class="arrow"></div>
<div class="step gd"><h4>Present value</h4><p>What an investor would pay today</p></div>
</div>
<p class="ptr" style="margin-top:8px">Analysts' DCF values differ mainly because they estimate the cash flows and the discount rate differently.</p>
</figure>

<figure class="fig" id="fig-dcfmodels"><figcaption>Three DCF models</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Model</th><th>What is discounted</th><th>Discount rate</th><th>Best for</th></tr></thead>
<tbody>
<tr><th>Dividend discount model (DDM)</th><td>Expected future dividends</td><td>Cost of equity</td><td>Companies paying regular, substantial dividends: <b>mature companies in defensive industries</b></td></tr>
<tr><th>Free cash flow to equity (FCFE)</th><td>Cash flow available to equity shareholders, instead of actual dividends</td><td>Cost of equity</td><td>Companies that pay little or no dividend, and companies in <b>high growth</b>. Book example: Alphabet (Google's parent) has never paid a dividend</td></tr>
<tr><th>Free cash flow to firm (FCFF)</th><td>Cash flow before any payments to any source of capital</td><td><b>WACC</b></td><td>When the company has no objective debt policy, so future borrowing cannot be estimated for FCFE</td></tr>
</tbody></table></div></figure>

<div class="col">
<h3>Gordon growth model</h3>
<p>Also called the <b>perpetual growth model</b>. It values a company whose dividend is expected to grow forever at a constant rate.</p>
<div class="formula">P = D1 &divide; (k &minus; g)</div>
<p><b>D1</b> = dividend expected at the <b>end of the year</b>. <b>k</b> = cost of equity. <b>g</b> = constant growth rate, which must be <b>lower than k</b>.</p>
<div class="trap">Use <b>next year's</b> dividend (D1), not the one just paid. If the last dividend was Rs 4 and growth is 5%, D1 = 4 &times; 1.05 = Rs 4.20.</div>

<h3>Free cash flow formulas (as given in the book)</h3>
</div>

<figure class="fig" id="fig-fcf"><figcaption>FCFE and FCFF<span>Figures come from the cash flow statement</span></figcaption>
<div class="grid g3">
<div class="box hl"><span class="tag">FCFE</span><p>Operating cash flow<br>&minus; Capital expenditure<br>&minus; Interest payments<br>&plusmn; Net borrowings (repayments)<br><b>= Free cash flow to equity</b></p></div>
<div class="box hl"><span class="tag">FCFF, direct</span><p>Operating cash flow<br>&minus; Capital expenditure<br>&minus; Tax benefit on interest payments<br><b>= Free cash flow to the firm</b></p></div>
<div class="box hl"><span class="tag">FCFF, indirect</span><p>EBIT &times; (1 &minus; tax rate)<br>+ Depreciation and non-cash charges<br>&minus; Increase (+ decrease) in non-cash working capital<br>&minus; Capital expenditure (+ sale of assets)</p></div>
</div>
<p class="ptr" style="margin-top:8px">Non-cash charges added back include amortisation and loss on sale of assets. A gain on sale of assets is deducted. (In the book the direct FCFF list ends with the label "Free cash flow to equity"; the section is about FCFF.)</p>
</figure>

<div class="col">
<h3>Two-stage valuation for high-growth companies</h3>
<p>A fast-growing company's growth may be unsustainable and even above its cost of capital, so a single constant growth rate does not fit. Value it in two stages:</p>
</div>

<figure class="fig" id="fig-twostage"><figcaption>Value = high-growth years + terminal value</figcaption>
<div class="flow">
<div class="step"><h4>Stage 1</h4><p>Estimate how long high growth lasts. Forecast each year's free cash flow and discount it</p></div><div class="arrow"></div>
<div class="step"><h4>Stage 2: terminal value</h4><p>Gordon model on the cash flow after high growth, <b>or</b> an exit value: EBITDA (or EBIT) at the end &times; EV/EBITDA (or EV/EBIT) of comparable firms</p></div><div class="arrow"></div>
<div class="step hl"><h4>Discount the terminal value</h4><p>It is a future amount, so bring it back to present value too</p></div><div class="arrow"></div>
<div class="step gd"><h4>Add them up</h4><p>Value of equity (FCFE) or of the firm (FCFF)</p></div>
</div></figure>

<div class="col">
<div class="why"><b>Capping the perpetual growth rate</b>The perpetual growth rate is often capped at the <b>long-term nominal GDP growth rate</b> of the company's markets, because no business can outgrow the economy forever. Analysts may use a lower rate. A rough forecast can extrapolate past growth; analysts refine it using the share of earnings ploughed back and the expected return on equity.</div>
<h3>From firm value to equity value (FCFF)</h3>
<div class="formula">Value of equity = Firm value &minus; minority interest &minus; preferred share capital &minus; interest-bearing debt</div>
<p>To get <b>enterprise value</b>, the book deducts surplus cash, cash equivalents and short-term investments not needed for current operations from the firm value.</p>

<h3>The discount rate</h3>
<p>It should reflect the risk in the cash flows. <b>FCFF</b> is discounted at <b>WACC</b> (debt and equity). <b>FCFE</b> is discounted at the <b>cost of equity</b>. <b>Cost of debt</b> is usually the prevailing interest rate for borrowers of comparable credit quality. <b>Cost of equity</b> is the return the company's shareholders require.</p>
</div>

<figure class="fig" id="fig-capm"><figcaption>CAPM and WACC<span>The book's formulas</span></figcaption>
<div class="grid g2">
<div class="box hl"><span class="tag">Cost of equity: CAPM</span><p class="formula" style="margin:.3rem 0">Ke = Rf + &beta; &times; (Rm &minus; Rf)</p><ul><li><b>Rf</b>: risk-free rate</li><li><b>Rm &minus; Rf</b>: market risk premium (MRP)</li><li><b>&beta;</b> (beta): sensitivity of the stock's return to the market's; a proxy for business and financial risk</li><li><b>&beta; &times; (Rm &minus; Rf)</b>: equity risk premium paid over the risk-free rate</li></ul></div>
<div class="box hl"><span class="tag">Weighted average cost of capital</span><p class="formula" style="margin:.3rem 0">WACC = Ke &times; We + Kd &times; (1 &minus; Tax) &times; Wd</p><ul><li><b>We</b> = Equity &divide; (Equity + Debt)</li><li><b>Wd</b> = Debt &divide; (Equity + Debt)</li><li><b>Kd</b>: cost of debt, taken <b>after tax</b> because interest saves tax</li></ul></div>
</div></figure>

<figure class="fig" id="fig-wacc"><figcaption>Try it: CAPM, WACC and Gordon<span>Change any number. All rates are % a year.</span></figcaption>
<div class="calc">
<p class="calch">Rates</p>
<div class="calcin">
<div><label for="w-rf">Risk-free rate</label><input type="number" id="w-rf" value="7" step="0.25"></div>
<div><label for="w-rm">Market return</label><input type="number" id="w-rm" value="12" step="0.25"></div>
<div><label for="w-b">Beta</label><input type="number" id="w-b" value="1.2" step="0.05"></div>
<div><label for="w-kd">Cost of debt</label><input type="number" id="w-kd" value="10" step="0.25"></div>
</div>
<p class="calch">Capital mix and dividend</p>
<div class="calcin">
<div><label for="w-wd">Debt weight %</label><input type="number" id="w-wd" value="40" step="5"></div>
<div><label for="w-t">Tax rate %</label><input type="number" id="w-t" value="25" step="1"></div>
<div><label for="w-d1">Next dividend D1 (Rs)</label><input type="number" id="w-d1" value="5" step="0.5"></div>
<div><label for="w-g">Dividend growth g</label><input type="number" id="w-g" value="8" step="0.25"></div>
</div>
<div class="calcres">
<div><b id="w-mrp"></b><small>market risk premium</small></div>
<div><b id="w-ke"></b><small>cost of equity (Ke)</small></div>
<div><b id="w-wacc"></b><small>WACC</small></div>
<div><b id="w-p"></b><small>Gordon value per share</small></div>
</div>
<p class="calcnote" id="w-note"></p>
</div></figure>

<div class="col">
<div class="trap">DCF gives wrong answers if the cash flows and the discount rate are not estimated with enough rigour. A small change in the discount rate or growth rate can move the value a lot.</div>
</section>

<section class="sec" id="s7"><span class="secno">10.6 and 10.7</span><h2>Relative valuation: earnings multiples</h2>
<p>DCF is complicated and rests on many assumptions. <span class="k">Relative valuation</span> compares <b>what we pay</b> (price) with <b>what we get</b> (earnings or assets). It does not give an absolute value, but shows whether something looks <b>cheap or expensive</b>, which supports a buy, sell or hold call.</p>

<h3>10.7.1 Dividend yield and price to dividend</h3>
<div class="formula">Dividend yield = Dividend per share &divide; Current price</div>
<p>The book's example: a company has paid Rs 5 or more in dividend every year for five years.</p>
</div>

<figure class="fig" id="fig-divyield"><figcaption>Same Rs 5 dividend, four prices<span>The book's table</span></figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Price (Rs)</th><th>50</th><th>100</th><th>150</th><th>200</th></tr></thead>
<tbody>
<tr><th>Dividend (Rs)</th><td>5</td><td>5</td><td>5</td><td>5</td></tr>
<tr><th>Dividend yield</th><td>10.00%</td><td>5.00%</td><td>3.33%</td><td>2.50%</td></tr>
<tr><th>Price / dividend</th><td>10</td><td>20</td><td>30</td><td>40</td></tr>
</tbody></table></div>
<p class="ptr" style="margin-top:8px">Price to dividend = what the market pays for one rupee of dividend.</p>
</figure>

<div class="col">
<ul>
<li>Compare dividend yield with <b>bond yields</b>. The book: a 10% bond taxed at 30% leaves about 7% after tax; at Rs 50 the share's 10% dividend yield looks better, with potential upside too. At Rs 200, the 2.5% yield is clearly inferior.</li>
<li>When equity yields are generally <b>above</b> bond yields, equity is cheap; this is typical when markets are down. In bull markets, equity yields are well <b>below</b> bond yields.</li>
<li>A high dividend yield is <b>not always</b> a value pick: a high payout may mean few avenues to grow, limiting capital gains. Check it against company fundamentals, which the book calls <span class="k">companion variables</span>.</li>
</ul>

<h3>10.7.2 Earnings yield and P/E</h3>
<div class="formula">Earnings yield = EPS &divide; Current price &nbsp;&nbsp;|&nbsp;&nbsp; P/E = Current price &divide; EPS (its reciprocal)</div>
<ul>
<li>Analysts move to earnings yield when dividend yields are very low.</li>
<li>P/E is the money needed to buy one unit of profit. It uses historical EPS, or forecast EPS for <b>forward P/E</b>.</li>
<li>All else equal, a P/E above peers and the market looks <b>expensive</b>; below looks <b>undervalued</b>.</li>
<li>But companies with <b>higher growth or lower risk</b> deserve a premium; lower growth or higher risk, a discount.</li>
<li>Earnings are for a period; price is at a point. Choose the EPS period with judgement: investors usually weigh <b>future</b> earnings more, and may use next year's if this year's is unusually high or low.</li>
</ul>

<h3>10.7.3 PEG ratio</h3>
<div class="formula">PEG = (Price &divide; EPS) &divide; Growth rate</div>
<p>Coined by <b>Peter Lynch</b>. A high P/E can be justified by high growth, but high growth may not last. Lynch: <b>PEG below 1</b> may be treated as <b>undervalued</b>. Use rules of thumb with care; comparing PEGs across competitors is more useful.</p>
</div>

<figure class="fig" id="fig-peg"><figcaption>P/E says A, PEG says B<span>The book's example: both have EPS of Rs 10</span></figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th></th><th>A Ltd</th><th>B Ltd</th></tr></thead>
<tbody>
<tr><th>Price</th><td>Rs 120</td><td>Rs 140</td></tr>
<tr><th>P/E</th><td>12x</td><td>14x</td></tr>
<tr><th>Expected growth</th><td>10% a year</td><td>15% a year</td></tr>
<tr><th>PEG</th><td>12 &divide; 10 = <b>1.2x</b></td><td>14 &divide; 15 = <b>0.93x</b></td></tr>
<tr><th>Verdict</th><td>Cheaper on P/E</td><td><b>Better value once growth is counted</b></td></tr>
</tbody></table></div></figure>

<div class="col">
<h3>10.7.4 EV to EBIT(DA)</h3>
<p>EPS, and so P/E and PEG, depend on the company's <b>capital structure</b> (equity has the residual claim). A retail investor cannot change that; a controlling shareholder can. So from an <b>acquirer's</b> view, or for a takeover target, use ratios <b>neutral to capital structure</b>: <span class="k">EV/EBIT</span> or <span class="k">EV/EBITDA</span> (see 3.1.7 for EV).</p>
<div class="grid g2">
<div class="box"><h4>EV/EBITDA</h4><p>Preferred for <b>capital-intensive</b> industries, where historical asset costs and depreciation choices distort EBIT.</p></div>
<div class="box"><h4>EV/EBIT</h4><p>Preferred for <b>other</b> industries.</p></div>
</div>
<p>Lower ratios look more attractive, all else equal; higher growth or lower risk earns a premium.</p>
<h3>10.7.5 EV to sales</h3>
<p>P/E, EV/EBITDA and EV/EBIT cannot be used when profit is <b>negative</b>, and are too high to mean much when a company has <b>only just broken even</b>. Sales are never negative, so <span class="k">EV/Sales</span> works. But only if the company is likely to turn and stay profitable. If no turnaround is likely, its "going concern" status is doubtful and it should be valued at <b>liquidation value</b>.</p>
</section>

<section class="sec" id="s8"><span class="secno">10.8</span><h2>Relative valuation: asset multiples</h2>
<p>Here assets replace earnings. Two ratios from earlier chapters: <b>ROE</b> = net profit &divide; net worth (return on the book value of equity); <b>ROCE</b> = EBIT &divide; capital employed (debt + net worth).</p>
<h3>10.8.1 Price to book value</h3>
<div class="formula">P/B = Market cap &divide; Book value of equity = Price per share &divide; Book value per share</div>
<p>How much an investor pays for ownership of one unit of the company's net assets.</p>
<div class="grid g3">
<div class="box gd"><h4>Financial companies</h4><p><b>Preferred here.</b> Their assets are mostly monetary, so book value is close to fair value.</p></div>
<div class="box bd"><h4>Capital-intensive firms</h4><p>Historical cost accounting means book values often do not reflect fair value.</p></div>
<div class="box bd"><h4>Services and technology</h4><p>Their key assets, people and self-generated intellectual property, are not on the balance sheet.</p></div>
</div>
<p>Because accounting is conservative, book value is often used for a <b>conservative</b> value of equity. Lower P/B looks more attractive, all else equal, but a <b>higher ROE deserves a premium</b>.</p>
</div>

<figure class="fig" id="fig-pb"><figcaption>The book's P/B example<span>Rs lakh, 50 lakh shares of Rs 10 each</span></figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th></th><th>AFB Finance</th><th>LKH Finance</th></tr></thead>
<tbody>
<tr><th>Share capital</th><td>500</td><td>500</td></tr>
<tr><th>Share premium</th><td>3,200</td><td>2,100</td></tr>
<tr><th>Reserves and surplus</th><td>6,200</td><td>5,400</td></tr>
<tr><th>Total equity</th><td>9,900</td><td>8,000</td></tr>
<tr><th>Book value per share</th><td>9,900 &divide; 50 = <b>Rs 198</b></td><td>8,000 &divide; 50 = <b>Rs 160</b></td></tr>
<tr><th>Market price</th><td>Rs 200</td><td>Rs 175</td></tr>
<tr><th>P/B</th><td><b>1.01</b></td><td><b>1.09</b></td></tr>
</tbody></table></div>
<p class="ptr" style="margin-top:8px">On P/B alone, AFB Finance is less expensive, even though its share price is higher.</p>
</figure>

<div class="col">
<div class="trap">Compare a company's multiple with the <b>industry</b>, not just one peer. In a fragmented industry, a few outliers can pull the <b>mean</b> up while most firms sit near the <b>median</b>. Check both before deciding.</div>

<h3>10.8.2 EV to capital employed</h3>
<div class="formula">EV / Capital employed = EV &divide; (Total equity + Total debt)</div>
<p>Used together with ROCE, it shows the return an investor actually earns on the price paid.</p>
</div>

<figure class="fig" id="fig-evce"><figcaption>The book's EV to capital employed example</figcaption>
<div class="flow">
<div class="step"><h4>Capital employed</h4><p>Net worth 1,00,000 + debt 1,00,000 = <b>2,00,000</b></p></div><div class="arrow"></div>
<div class="step"><h4>EV</h4><p>Market cap 5,00,000 + debt 1,00,000 &minus; cash 0 = <b>6,00,000</b></p></div><div class="arrow"></div>
<div class="step hl"><h4>EV / CE = 3</h4><p>ROCE of 45% on 2,00,000 is only <b>15%</b> on 6,00,000</p></div><div class="arrow"></div>
<div class="step gd"><h4>Want 20%?</h4><p>Pay at most 45 &divide; 20 = <b>2.25x</b> capital employed, that is EV of Rs 4,50,000</p></div>
</div></figure>

<div class="col">
<h3>10.8.3 Net asset value (NAV)</h3>
<p><span class="k">NAV</span> = <b>market value</b> of assets minus liabilities. Unlike book value, it uses market values. It can be stated in total or per share. Used for very asset-heavy businesses such as <b>real estate, shipping and aviation</b>.</p>
<h3>10.8.4 Other metrics</h3>
</div>

<figure class="fig" id="fig-othermetrics"><figcaption>Industry-specific multiples</figcaption>
<div class="grid g3">
<div class="box"><span class="tag">Life insurance</span><h4>Price / Embedded value</h4><p>Embedded value: present value of expected net future cash flows (probability-adjusted) from policies now in force.</p></div>
<div class="box"><span class="tag">NBFCs</span><h4>Price / Adjusted book value</h4><p>Adjusted book value: fair value of assets minus fair value of liabilities. Includes off-balance sheet items.</p></div>
<div class="box"><span class="tag">Start-ups, special situations</span><h4>EV / Capacity</h4><p>Operating metrics instead of financial ones: a closed steel plant by its production capacity; an e-commerce start-up by users, transactions or transaction value.</p></div>
</div></figure>

<div class="col">
<section class="sec" id="s9"><span class="secno">10.9</span><h2>Trading and transaction multiples</h2>
<div class="analogy">Buying a flat: you check what similar flats in the locality sold for, and that becomes your starting point for negotiation. That is relative valuation. Quick and intuitive, but it reflects the current market mood, which may be too optimistic or too pessimistic.</div>
<p>So use the <b>maximum, minimum and average</b> of the multiples, look at each company's own history over several years, and compare across peers and the industry.</p>
<div class="grid g2">
<div class="box"><span class="tag">Trading multiples</span><p>From prices in the <b>stock market</b>.</p></div>
<div class="box gd"><span class="tag">Transaction multiples</span><p>From similar <b>deals</b> completed recently. <b>More relevant</b> and more authentic: someone actually agreed to buy at that value.</p></div>
</div>

<h3 id="s10">10.10 Sum of the parts (SOTP)</h3>
<p>Conglomerates such as <b>ITC</b> and <b>L&amp;T</b> run many businesses under one umbrella. Value each business separately, as an independent business, using the methods above, then <b>add them up</b>. The book calls this sum-of-the-parts (SOTP or SOP) valuation.</p>

<h3 id="s11">10.11 New-age businesses</h3>
<p>Valuations of companies like WhatsApp, Zomato, LinkedIn and Facebook are hard to explain with numbers. Such deals use new measures: <b>eyeballs, page views, footfall, ARPU, number of users</b>. As Buffett would say, these must eventually become <b>profits for owners</b>. Without that, valuations last only as long as the story and the next buyer, and can fall like a pack of cards, as in the <b>dot-com boom of 2000 to 2001</b>.</p>

<h3 id="s12">10.12 Is valuation objective?</h3>
<p>It may look objective, but it is <b>very subjective</b>: the inputs have no generally accepted standards. It is also not timeless; it can change dramatically when the business changes. Complicated models do not make a value precise. They only give a <b>false impression of preciseness</b>.</p>

<h3 id="s13">10.13 Nine things to keep in mind</h3>
<ol>
<li>High earning power: book value matters less. Low earning power: book value matters a lot.</li>
<li>A share is part ownership, so to value a share, value the whole business.</li>
<li>For a private owner, the true value of the firm is <b>EV</b>, not market cap.</li>
<li>P/E of a leveraged firm can deceive: look at its debt.</li>
<li>Use <b>consolidated</b> numbers, not just standalone.</li>
<li>Focus on <b>ROE, not EPS</b>: EPS ignores retained earnings.</li>
<li>Leverage improves ROE, but excessive leverage is risky.</li>
<li><b>ROCE</b> reflects the true return on capital; ROE can be inflated by high leverage.</li>
<li>ROCE and ROE should be close. A wide gap should trigger investigation.</li>
</ol>
</section>

<section class="sec" id="traps"><h2>All exam traps in this chapter</h2>
<ol class="traplist">
<li>Price is known to all; value is an estimate. Valuation is an art and a science.</li>
<li>Buffett: only two sources of value, earnings and assets.</li>
<li>Lenders look at cash flows first; collateral is a fallback.</li>
<li>Cost-based valuation suits buy-versus-make decisions; generally not for financial investors.</li>
<li>Risk-neutral valuation discounts at the risk-free rate; used for insurers. Real-world adds a risk premium.</li>
<li>A bond whose coupon equals the required return is worth its face value.</li>
<li>DCF needs cash flows, timing and discount rate.</li>
<li>DDM suits mature dividend payers in defensive industries. FCFE suits low-dividend and high-growth firms. FCFF suits firms without an objective debt policy.</li>
<li>Gordon: P = D1 &divide; (k &minus; g). D1 is next year's dividend; g must be below k.</li>
<li>FCFF is discounted at WACC; FCFE and dividends at cost of equity.</li>
<li>Terminal value: perpetual growth capped at long-term nominal GDP growth, or an exit multiple. Discount it to present value.</li>
<li>Equity value = firm value &minus; minority interest &minus; preferred capital &minus; interest-bearing debt.</li>
<li>CAPM: Ke = Rf + &beta;(Rm &minus; Rf). Rm &minus; Rf is the market risk premium.</li>
<li>WACC uses after-tax cost of debt: Kd &times; (1 &minus; tax).</li>
<li>Dividend yield = DPS &divide; price. Price/dividend is its reciprocal.</li>
<li>Earnings yield = EPS &divide; price; P/E is its reciprocal.</li>
<li>PEG = P/E &divide; growth; coined by Peter Lynch; below 1 may mean undervalued.</li>
<li>EV/EBITDA and EV/EBIT are neutral to capital structure; suit acquirers. EV/EBITDA for capital-intensive industries.</li>
<li>EV/Sales for loss-making or just-profitable firms likely to turn profitable; otherwise liquidation value.</li>
<li>P/B is preferred for financial companies; poor for services and technology firms.</li>
<li>NAV uses market value of assets; used for real estate, shipping, aviation.</li>
<li>P/Embedded value: life insurers. P/Adjusted book value: NBFCs. EV/Capacity: start-ups and special situations.</li>
<li>Transaction multiples are more relevant than trading multiples.</li>
<li>SOTP: value each business separately and add up (ITC, L&amp;T).</li>
<li>Focus on ROE, not EPS. ROCE reflects true return on capital; a wide gap with ROE needs investigation.</li>
</ol>
</section>

<section class="sec" id="talk"><h2>For the group discussion</h2>
<ol class="talk">
<li>Pick a listed company. What would you need to know to value it by DCF? Which input are you least sure of?</li>
<li>Why might a bank trade on P/B and a software company on P/E? What could go wrong with each?</li>
<li>A start-up is valued on users, not profit. When is that reasonable, and when is it a story?</li>
<li>Two companies have the same P/E. One has no debt, the other is heavily borrowed. Which is cheaper?</li>
<li>Try the calculator: how much does the Gordon value change if growth moves from 8% to 9%? What does that tell you about DCF?</li>
</ol>
</section>
</div>

<footer>Notes built from the NISM Series XV workbook (February 2026 version). Study aid only.</footer>
</div>
"""

WIDGETS = r"""
window.__WIDGETS__=function(){
const g=id=>document.getElementById(id);
if(!g('w-rf'))return;
const ids=['w-rf','w-rm','w-b','w-kd','w-wd','w-t','w-d1','w-g'];
const pct=v=>(Math.round(v*100)/100).toFixed(2)+'%';
function calc(){const rf=+g('w-rf').value,rm=+g('w-rm').value,b=+g('w-b').value,kd=+g('w-kd').value,wd=Math.min(100,Math.max(0,+g('w-wd').value))/100,t=+g('w-t').value/100,d1=+g('w-d1').value,gr=+g('w-g').value;
 const mrp=rm-rf,ke=rf+b*mrp,wacc=ke*(1-wd)+kd*(1-t)*wd;
 g('w-mrp').textContent=pct(mrp);g('w-ke').textContent=pct(ke);g('w-wacc').textContent=pct(wacc);
 let note='Ke = '+rf+' + '+b+' x ('+rm+' - '+rf+'). WACC = Ke x '+(1-wd).toFixed(2)+' + '+kd+' x (1 - '+t.toFixed(2)+') x '+wd.toFixed(2)+'.';
 if(gr>=ke){g('w-p').textContent='n/a';note+=' Gordon needs growth below the cost of equity.'}
 else{g('w-p').textContent='Rs '+(Math.round(d1/((ke-gr)/100)*100)/100).toLocaleString('en-IN');note+=' Gordon value = D1 / (Ke - g).'}
 g('w-note').textContent=note;}
ids.forEach(i=>g(i).addEventListener('input',calc));calc();
};
"""
