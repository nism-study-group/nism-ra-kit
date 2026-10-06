LEARN = r"""
<style>
.calc{display:grid;gap:14px}
.calc label{display:block;font-weight:700}
.calc output{font-family:var(--head);font-weight:800}
.calc input[type=range]{width:100%}
.calcres{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
@media (max-width:520px){.calcres{grid-template-columns:repeat(2,1fr)}}
.calcres div{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:.6rem;text-align:center}
.calcres b{display:block;font-family:var(--head);font-size:1.45rem}
.calcres small{color:var(--muted)}
.calcnote{font-weight:700;margin:.2rem 0 0}
.formula{font-family:var(--head);font-weight:700;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.55rem .8rem;margin:.7rem 0;overflow-x:auto}
</style>
<div class="wrap">
<header class="hero">
<div class="kicker">Chapter 3 of 15</div>
<h1>Terms in the equity and debt markets</h1>
<div class="meta"><span class="pill">Worth <b>2 marks</b> of 100</span><span class="pill">Book pages 55 to 77</span><span class="pill">About 45 minutes</span></div>
<p class="oneline">The words analysts use to <span class="k">price a share</span>, <span class="k">price a bond</span> and <span class="k">price a commodity future</span>.</p>
</header>

<figure class="fig" id="fig-map"><figcaption>Chapter map<span>Five parts. 3.1 and 3.2 have the numericals. Tap to jump.</span></figcaption>
<div class="map">
<a href="#s0"><b>Intro</b><span>Equity or debt?</span><small>Owner versus lender</small></a>
<a href="#s1"><b>3.1</b><span>Equity words</span><small>Values, market cap, EV, EPS, P/E, P/S, P/BV, DVR</small></a>
<a href="#s2"><b>3.2</b><span>Debt words</span><small>Coupon, maturity, yields, duration</small></a>
<a href="#s3"><b>3.3</b><span>Types of bonds</span><small>Zero, floating, convertible, perpetual and more</small></a>
<a href="#s4"><b>3.4</b><span>Commodity words</span><small>Spot, basis, contango, cost of carry</small></a>
</div></figure>

<div class="col">
<section class="sec" id="s0"><span class="secno">Intro</span><h2>Equity or debt?</h2>
<p>A business that needs money can raise it in two ways. It can sell a part of itself (<span class="k">equity</span>) or borrow (<span class="k">debt</span>). Chapter 2 introduced both. Here is how they differ.</p>
</div>

<figure class="fig" id="fig-eqdebt"><figcaption>Owner versus lender</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th></th><th>Equity investor</th><th>Debt investor</th></tr></thead>
<tbody>
<tr><th>Role</th><td>Owner of the business</td><td>Lender to the business</td></tr>
<tr><th>Money stays</th><td>As long as the company needs it</td><td>Must be repaid after a fixed time</td></tr>
<tr><th>Return</th><td>No fixed return. Gets the <b>residual profit</b>, whatever is left</td><td>Fixed interest, plus principal back at maturity</td></tr>
<tr><th>Say in management</th><td>Yes</td><td>No</td></tr>
<tr><th>Risk</th><td>Higher. Long term, growth, volatile</td><td>Lower. Steady income, unless the company defaults</td></tr>
</tbody></table></div></figure>

<div class="col">
<div class="analogy">A company borrows at <span class="num">12%</span> and earns <span class="num">14%</span> on what it builds with the loan. The lender gets exactly 12%, as promised. The extra 2% goes to the owners. If the company earns only 10%, the lender still gets 12%, and the owners make up the gap from their share.</div>
<p>So the choice is a trade-off. Lower risk and a steady return: choose debt. A higher return: accept the extra risk of equity. Most investors split their money between the two.</p>
</section>

<section class="sec" id="s1"><span class="secno">3.1</span><h2>Equity words</h2>
<h3>Five kinds of "value"</h3>
</div>

<figure class="fig" id="fig-values"><figcaption>One share, five values<span>Each answers a different question</span></figcaption>
<div class="grid g3">
<div class="box"><span class="tag">Face value</span><h4>The printed price</h4><p>The nominal value of a share, such as Rs 10. Share capital = number of shares &times; face value.</p></div>
<div class="box"><span class="tag">Book value</span><h4>What the books say</h4><p>Net worth &divide; number of shares. What each share would get, in theory, if the company closed down.</p></div>
<div class="box"><span class="tag">Market value</span><h4>What buyers pay today</h4><p>The price on the stock exchange. Depends on expected performance, sentiment and liquidity.</p></div>
<div class="box"><span class="tag">Replacement value</span><h4>Cost to rebuild</h4><p>What a new company would pay today to set up the same plants and infrastructure.</p></div>
<div class="box hl"><span class="tag">Intrinsic value</span><h4>What it is really worth</h4><p>The present value of the cash the business will produce in future.</p></div>
</div></figure>

<div class="col">
<h3>Face value</h3>
<p>A share may be issued at face value, above it (at a <b>premium</b>) or below it (at a <b>discount</b>). Face value changes only when the company <b>splits</b> shares (face value goes down) or <b>consolidates</b> them (face value goes up).</p>
<p>Example: you hold 1 share of Rs 10. The company splits each share into 5. You now hold 5 shares of <span class="num">Rs 2</span> each.</p>
<div class="trap">A dividend stated as a percentage is a percentage of <b>face value</b>, not of market price. 30% dividend on a Rs 10 share = Rs 3. The same 30% on a Rs 2 share = <span class="num">Rs 0.60</span>.</div>

<h3>Book value</h3>
<p><span class="k">Book value per share</span> = net worth (equity capital plus reserves) &divide; number of shares outstanding. Assets sit in the books at cost less depreciation. Their real selling value may be different, and is never known for sure.</p>

<h3>Intrinsic value versus market price</h3>
<p><span class="k">Intrinsic value</span> is the present value of the expected free cash flows from an asset. Warren Buffett calls it "the discounted value of the cash that can be taken out of a business during its remaining life". The discount rate used is usually the investor's required return, adjusted for the risks of the business. Later chapters show how.</p>
<div class="grid g2">
<div class="box gd"><h4>Intrinsic value &gt; market price</h4><p>The share is <b>undervalued</b>. A buy candidate.</p></div>
<div class="box bd"><h4>Intrinsic value &lt; market price</h4><p>The share is <b>overvalued</b>. A sell candidate.</p></div>
</div>
<p>This is hard to get right every time, because what is being priced is an unknown future. The book calls equity investing both an art and a science, shaped by human behaviour in groups.</p>

<h3>Market capitalisation</h3>
<div class="formula">Market cap = market price per share &times; number of shares outstanding</div>
<p>Example: 1 lakh shares at Rs 20 = market cap of <span class="num">Rs 20 lakh</span>. It changes every time the price changes. "Outstanding" means issued, subscribed and fully paid up. Do not confuse it with authorised capital.</p>
</div>

<figure class="fig" id="fig-caps"><figcaption>Large, mid and small cap<span>The book's common rule of thumb, ranked by market cap</span></figcaption>
<div class="stack"><div style="flex:1;background:var(--indigo)">Large: top 50 to 100</div><div style="flex:2;background:var(--teal)">Mid: next 200 to 500</div><div style="flex:2.4;background:var(--muted)">Small: all the rest</div></div>
<p class="ptr" style="margin-top:8px">Large caps have high liquidity and include most <b>blue chips</b> (long history, stable profits, market share). Small caps have little liquidity.</p>
</figure>

<div class="col">
<div class="trap">The book says there is <b>no fixed size cut-off</b> for large, mid and small cap. The ranking floats with the market, the period and the regulatory definition.</div>
<p>The ratio of a country's total <b>market cap to its GDP</b> is used to judge the size and importance of its stock market.</p>

<h3>Enterprise value (EV)</h3>
<p><span class="k">EV</span> is the value of the whole business, counting only the capital actually at work in it. So it adds the lenders' and preference holders' money to the shareholders', then takes out cash and non-core investments.</p>
<div class="formula">EV (standalone) = market value of equity + preferred capital + debt &minus; cash and equivalents &minus; non-operating financial investments</div>
<p>On a <b>consolidated</b> basis you also add non-controlling interest and the subsidiary's preferred capital and debt, and subtract the subsidiary's cash and investments too. Use fair market values. If a value is not available (unlisted bonds, bank loans), use the balance sheet value instead.</p>
</div>

<figure class="fig" id="fig-ev"><figcaption>The book's EV example<span>Rs crore. 10 lakh shares trading at Rs 340.</span></figcaption>
<div class="flow">
<div class="step"><h4>Market cap</h4><p>340 &times; 10 lakh = <b>34.0</b></p></div><div class="arrow"></div>
<div class="step"><h4>+ Preferred</h4><p><b>8.5</b> (book value)</p></div><div class="arrow"></div>
<div class="step"><h4>+ Debt</h4><p><b>6.4</b> (book value)</p></div><div class="arrow"></div>
<div class="step bd"><h4>&minus; Cash, investments</h4><p><b>2.5 + 1.4</b></p></div><div class="arrow"></div>
<div class="step gd"><h4>EV</h4><p><b>Rs 45.0 crore</b></p></div>
</div>
<p class="ptr" style="margin-top:8px">The balance sheet shows equity at 12.5. That is ignored: for listed equity, use market value.</p></figure>

<div class="col">
<div class="trap">Cash is <b>subtracted</b> in EV, not added. The book's sample question: market cap 10 lakh, debt 3 lakh, cash 4 lakh. EV = 10 + 3 &minus; 4 = <span class="num">9 lakh</span>.</div>

<h3>Earnings: which profit, which period?</h3>
<dl class="terms">
<dt>Net profit</dt><dd>Profit left for the equity owners.</dd>
<dt>EBIT</dt><dd>Earnings before interest and taxes. To be shared among lenders, government and owners.</dd>
<dt>EBITDA</dt><dd>Earnings before interest, tax, depreciation and amortisation. First recovers the capital spent on assets, then is shared among lenders, government and owners.</dd>
<dt>Historical</dt><dd>Earnings of past years.</dd>
<dt>Trailing</dt><dd>The most recent period up to now, on a rolling basis. <b>TTM</b> = trailing twelve months. Also trailing 4 quarters. Useful when valuing a company in the middle of a year.</dd>
<dt>Forward</dt><dd>Earnings projected from future revenue and cost estimates.</dd>
</dl>
</div>

<figure class="fig" id="fig-ratios"><figcaption>Per-share numbers and price ratios<span>The book's worked examples</span></figcaption>
<div class="grid g2">
<div class="box"><span class="tag">EPS</span><h4>Earnings per share</h4><p>Net profit &divide; shares outstanding (strictly, the time-weighted average).</p><p>Rs 10 lakh &divide; 2 lakh shares = <b>Rs 5</b></p></div>
<div class="box"><span class="tag">DPS</span><h4>Dividend per share</h4><p>Dividend % &times; face value, or dividend paid &divide; shares.</p><p>40% on Rs 10 face value = <b>Rs 4</b></p></div>
<div class="box"><span class="tag">P/E</span><h4>Price to earnings</h4><p>Market price &divide; EPS. What the market pays for Rs 1 of earnings.</p><p>"12x" = twelve times earnings</p></div>
<div class="box"><span class="tag">P/S</span><h4>Price to sales</h4><p>Price &divide; sales per share, or market cap &divide; annual net sales.</p><p>Sales Rs 1 crore, 10 lakh shares, price Rs 40: 40 &divide; 10 = <b>4</b></p></div>
<div class="box"><span class="tag">P/BV</span><h4>Price to book value</h4><p>Market price &divide; book value per share.</p><p>(10 + 50 lakh) &divide; 6 lakh = BV Rs 10. Price Rs 20: <b>2x</b></p></div>
<div class="box"><span class="tag">Payout</span><h4>Dividend payout ratio</h4><p>DPS &divide; EPS. The share of profit paid out as dividend.</p></div>
</div></figure>

<div class="col">
<h3>Reading the P/E</h3>
<ul>
<li>A P/E on past earnings has limited use. Prices move ahead of earnings, in anticipation of future profits.</li>
<li>If earnings are expected to grow, the market pays a higher multiple. So analysts look at the <b>forward P/E</b>. Example: a share at 20 times this year's earnings but only 15 times next year's. The same price is divided by bigger future earnings.</li>
<li>The P/E of the whole index is used to judge if the market is expensive or cheap. It rises when prices run ahead of earnings and falls when markets correct. A value investor may buy when the P/E is low.</li>
<li>A large, stable company usually has a higher P/E than a small, risky one. But this is not "gospel truth": a small company with high expected growth can have a higher P/E.</li>
</ul>
<h3>When P/S and P/BV are useful</h3>
<div class="grid g2">
<div class="box"><h4>P/S</h4><p>Useful when a company is making <b>losses</b> for a while, so P/E means nothing. A lower P/S than peers may mean undervalued. A fall in revenue growth is a big risk for such shares.</p></div>
<div class="box"><h4>P/BV</h4><p>Useful when earnings are negative, and for <b>banks and financial institutions</b>, whose assets are mostly valued at market prices. Not relevant for <b>services</b> firms with few assets.</p></div>
</div>
<div class="trap">P/BV below 1 does <b>not</b> automatically mean a bargain. The company may have made poor investments that still have to be written down. Always ask why the market prices it below book value.</div>

<h3>Differential voting rights (DVR)</h3>
<p>A <span class="k">DVR share</span> is like a normal share but carries <b>less than one vote</b> per share. The company raises money without giving away control. Investors who only want dividends and price gains do not mind. DVRs trade separately, usually at a <b>discount</b> to the normal share.</p>
<p>Under the <b>Companies Act, 2013</b>, to issue DVRs a company needs a dividend record of at least <span class="num">10%</span> over the preceding <span class="num">3 years</span>, and DVRs cannot exceed <span class="num">25%</span> of total post-issue paid-up capital. Examples from the book: <b>Tata Motors</b> and <b>Pantaloons</b>.</p>
</section>

<section class="sec" id="s2"><span class="secno">3.2</span><h2>Debt words</h2>
<p>A company that needs Rs 100 crore can take a bank loan, or issue bonds to many investors. If it issues 1 crore bonds of Rs 100 each, an investor putting in Rs 1,000 gets 10 bonds. Each investor's risk is limited to what they put in.</p>
<p>A bond is a contract. Its features are the <b>principal</b>, the <b>coupon</b>, the <b>maturity</b>, how often coupons are paid, and any <b>collateral</b>. With <b>secured</b> debt, the lender can have assets sold if the company defaults. With <b>unsecured</b> debt, they cannot. Debt can be <b>privately placed</b> with a few select investors or sold to the public. Debt sold in a public issue must be listed on a stock exchange. Unlisted debt is held to maturity or traded over the counter.</p>
</div>

<figure class="fig" id="fig-bondwords"><figcaption>The three questions every loan answers</figcaption>
<div class="grid g3">
<div class="box hl"><span class="tag">How much?</span><h4>Face value (principal)</h4><p>The loan amount per bond, also called par value. Rs 100, Rs 1,000 or any amount. This is what is repaid at maturity, whatever price you paid in the market.</p></div>
<div class="box hl"><span class="tag">At what rate?</span><h4>Coupon rate</h4><p>The fixed yearly payment, as a % of face value. Coupon amount = face value &times; coupon rate.</p></div>
<div class="box hl"><span class="tag">For how long?</span><h4>Maturity (tenor)</h4><p>From 91 days (T-bills) to 30 years or more. Some bonds never mature. It shrinks every day until the bond is redeemed.</p></div>
</div></figure>

<div class="col">
<div class="why"><b>Coupon, not "interest rate"</b>The book advises calling it the coupon rate. "Interest rate" means the market-wide rate for borrowing and lending, which the central bank controls at its base.</div>
<p><b>Example.</b> 8.24GS2018 means an 8.24% government security maturing in 2018. With face value Rs 1,000 it pays Rs 82.40 a year. G-secs pay <b>twice a year</b>, so the investor gets <span class="num">Rs 41.20</span> every 6 months. The last coupon comes with the principal on the maturity date.</p>
<p><b>Maturity</b> is the single biggest factor behind changes in bond prices. Government T-bills are issued for <span class="num">91, 182 and 364 days</span>.</p>

<h3>Market price moves opposite to interest rates</h3>
<p>Once a bond trades, its price depends on market interest rates, inflation and default risk. A bond's value is its future cash flows, discounted at the market rate. So:</p>
<div class="grid g2">
<div class="box bd"><h4>Market rates go up</h4><p>Bond prices go <b>down</b></p></div>
<div class="box gd"><h4>Market rates go down</h4><p>Bond prices go <b>up</b></p></div>
</div>
<div class="analogy">Your bond pays 10%. New bonds now pay 12%. Nobody will pay full price for your 10% bond when 12% is on offer. To sell it, you must cut the price until the buyer's return matches 12%.</div>
<p><b>Redemption</b>: at maturity the issuer repays the principal and the final coupon. The bond then ceases to exist.</p>
</div>

<figure class="fig" id="fig-bondcalc"><figcaption>Bond calculator<span>Face value Rs 100, coupon paid once a year. Move the sliders.</span></figcaption>
<div class="calc">
<div><label for="bc-c">Coupon rate: <output id="bc-cv"></output></label><input type="range" id="bc-c" min="0" max="15" step="0.5" value="10"></div>
<div><label for="bc-y">Market yield (YTM): <output id="bc-yv"></output></label><input type="range" id="bc-y" min="1" max="15" step="0.5" value="12"></div>
<div><label for="bc-n">Years to maturity: <output id="bc-nv"></output></label><input type="range" id="bc-n" min="1" max="30" step="1" value="5"></div>
<div class="calcres">
<div><b id="bc-p"></b><small>price</small></div>
<div><b id="bc-cy"></b><small>current yield</small></div>
<div><b id="bc-md"></b><small>Macaulay duration (years)</small></div>
<div><b id="bc-mod"></b><small>modified duration</small></div>
</div>
<p class="calcnote" id="bc-note"></p>
</div></figure>

<div class="col">
<h3>Three ways to measure a bond's return</h3>
</div>

<figure class="fig" id="fig-yields"><figcaption>HPR, current yield, YTM, realised yield<span>From crude to complete</span></figcaption>
<div class="grid g2">
<div class="box"><span class="tag">Holding period return</span><h4>HPR</h4><p>(Coupons + interest on reinvested coupons + price gain) &divide; purchase price.</p><p>Book: buy at 104, coupon 8 reinvested at 7%, sell at 110 after a year. (8 + 0.56 + 6) &divide; 104 = <b>14.00%</b></p><p>Crude. Ignores compounding. Do not compare with annualised returns.</p></div>
<div class="box"><span class="tag">Current yield</span><h4>Coupon &divide; market price</h4><p>8.24GS2018 at Rs 104: 8.24 &divide; 104 = <b>7.92%</b></p><p>Simple, but ignores future cash flows, its biggest drawback. Like a share's dividend yield.</p></div>
<div class="box hl"><span class="tag">Yield to maturity</span><h4>YTM</h4><p>The rate that makes the present value of all future cash flows (coupons, their reinvestment, redemption) equal to today's price. It is the bond's <b>IRR</b>. Found by trial and error or Excel's <b>XIRR</b>.</p></div>
<div class="box"><span class="tag">Realised yield</span><h4>If you sell before maturity</h4><p>Annualised, with compounding. Book: buy at 1,000, 12% coupons reinvested at 14%, sell at 1,050 after 5 years = about <b>13%</b>.</p></div>
</div></figure>

<div class="col">
<div class="formula">Realised yield = [ (coupon &times; ((1 + reinvestment rate)<sup>years</sup> &minus; 1) &divide; reinvestment rate + sale price) &divide; purchase price ]<sup>1/years</sup> &minus; 1</div>
<div class="trap">YTM assumes two things: you <b>hold the bond to maturity</b>, and you <b>reinvest every coupon at the same YTM</b>. That means a flat yield curve that never changes, which is not realistic. It is still widely used because it is quick and simple.</div>

<h3>Duration</h3>
<p><span class="k">Macaulay duration</span> is the weighted average time in which you get your money back. The weights are the present values of each cash flow. It is usually less than the time to maturity.</p>
<div class="formula">Macaulay duration = &Sigma; [ t &times; CF<sub>t</sub> &divide; (1 + y)<sup>t</sup> ] &divide; current price</div>
<div class="formula">Modified duration = Macaulay duration &divide; (1 + y)</div>
<p><span class="k">Modified duration</span> measures how sensitive the price is to interest rates. The higher it is, the more the price rises when rates fall, and the more it drops when rates rise.</p>
</div>

<figure class="fig" id="fig-duration"><figcaption>What pushes duration (and rate risk) up<span>With everything else the same</span></figcaption>
<div class="grid g3">
<div class="box bd"><h4>Longer maturity</h4><p>Higher duration</p></div>
<div class="box bd"><h4>Lower coupon</h4><p>Higher duration</p></div>
<div class="box bd"><h4>Lower yield</h4><p>Higher duration</p></div>
</div>
<p class="ptr" style="margin-top:8px">Duration shrinks as a bond nears maturity, so the bond gets less risky with time.</p></figure>

<div class="col">
<div class="analogy">Duration is like a seesaw. A long plank (long maturity, small coupons) swings a lot when someone sits at the far end. A short plank barely moves. The "someone" is a change in interest rates.</div>
</section>

<section class="sec" id="s3"><span class="secno">3.3</span><h2>Types of bonds</h2>
<p>Every bond is built from three parts: principal, maturity and coupon. Change one of them and you get a new type of bond. Chapter 2 already covered convertible types (FCD, PCD, OCD, NCD) and the foreign, euro and masala naming rules. Here is what is new.</p>
</div>

<figure class="fig" id="fig-bondtypes"><figcaption>Eight types of bonds<span>Which part is changed, and who it helps</span></figcaption>
<div class="grid g2">
<div class="box"><span class="tag">Coupon removed</span><h4>Zero coupon bond</h4><p>No coupon. Issued at a <b>discount</b>, redeemed at <b>par</b>. The return is the gap. Higher duration, so more rate risk, than a coupon bond of the same maturity. The issuer keeps its cash until one "bullet" repayment.</p></div>
<div class="box"><span class="tag">Coupon floats</span><h4>Floating rate bond</h4><p>Coupon reset to a benchmark (inflation, inter-bank or call rates), typically every 6 months. Lower rate risk. Good when rates are rising. Limits: <b>cap</b> (maximum) and <b>floor</b> (minimum). Inverse floaters move opposite to the benchmark.</p></div>
<div class="box"><span class="tag">Principal becomes shares</span><h4>Convertible bond</h4><p>Debt that can turn into equity. Lower coupon than plain debt. Issuer need not repay. But existing owners are diluted and <b>EPS falls</b>.</p></div>
<div class="box"><span class="tag">Principal protected</span><h4>Principal protected note (PPN)</h4><p>Part goes into debt that grows back to the principal. The rest goes into equity, derivatives or commodities for upside. A synthetic product. Still carries the <b>issuer's credit risk</b>.</p></div>
<div class="box"><span class="tag">Linked to inflation</span><h4>Inflation protected securities</h4><p>Principal and coupon adjusted for inflation, so the real return is protected. Helps retired investors most.</p></div>
<div class="box"><span class="tag">Different currency</span><h4>Foreign currency bond</h4><p>Issued in a currency other than the issuer's home currency, such as USD. Lower rates, but the <b>issuer</b> carries currency risk.</p></div>
<div class="box"><span class="tag">Sold abroad</span><h4>External (Euro) bond</h4><p>Currency differs from the currency of the country where it is sold. INR bonds sold abroad are <b>masala bonds</b>; the <b>investor</b> carries currency risk.</p></div>
<div class="box"><span class="tag">No maturity</span><h4>Perpetual bond</h4><p>No maturity date. Issuer never has to redeem. May be "callable": the issuer can buy it back when it chooses.</p></div>
</div></figure>

<div class="col">
<h3>Zero coupon bonds in practice</h3>
<ul>
<li><b>Money market</b> instruments are short-term zeroes, under 1 year: <b>T-bills</b> (government), <b>commercial paper</b> (companies), <b>certificates of deposit</b> (banks and financial institutions).</li>
<li>Very long zeroes issued at a steep discount are <span class="k">deep discount bonds</span>. Examples: an old <b>IDBI</b> issue, and <b>Kisan Vikas Patra</b>.</li>
<li>The book's example: in October 2009, ETHL Communications Holdings (an Essar Group company) raised <span class="num">Rs 4,280 crore</span> in zero coupon bonds. Series 1 was issued at Rs 85.80 (implied rate 9.15%), Series 2 at Rs 82.55 (9.25%). Both repaid Rs 100 in 2011.</li>
</ul>
<div class="trap">For the same rupee return, a zero coupon bond has <b>more</b> interest rate risk than a coupon bond of the same maturity, because its duration is higher. A floating rate bond has <b>less</b>.</div>

<h3>Convertible bonds: the terms fixed at issue</h3>
<p>The conversion date (on or before which to convert), the conversion ratio (shares per bond), the conversion price (usually at a discount to market price), and the portion that converts. Conversion can be <b>compulsory</b> or <b>optional</b>, <b>full</b> or <b>partial</b>. After conversion, debt leaves the balance sheet and equity capital rises.</p>

<h3>Principal protected notes</h3>
<p>Several NBFCs have issued PPNs as <b>Equity Linked Bonds (ELBs)</b> and <b>Commodity Linked Bonds (CLBs)</b>. Some are listed.</p>
<div class="trap">"Principal protected" does not mean "no credit risk". If the issuer fails, the protection fails too.</div>

<h3>Inflation protection in India</h3>
<div class="grid g2">
<div class="box"><h4>Inflation Indexed Bonds (IIB)</h4><p>Government securities issued by the <b>RBI</b>. A fixed <b>real</b> coupon is applied to the inflation-adjusted principal. At maturity you get the higher of face value or adjusted principal. Index: <b>WPI</b>. Index ratio = reference index on settlement date &divide; reference index on issue date.</p></div>
<div class="box"><h4>Inflation Indexed National Saving Securities, Cumulative 2013</h4><p>For <b>retail</b> investors (individuals, minors, HUFs, charities). <b>10 years</b>. Interest = fixed <span class="num">1.5%</span> + inflation based on <b>CPI</b>. Compounded every 6 months and paid at maturity. The fixed rate is a floor, paid even in deflation. Taxable.</p></div>
</div>
<div class="trap">The two use different indices, as per the book: IIB uses <b>WPI</b>; the 2013 retail securities use <b>CPI</b>.</div>

<h3>Foreign currency and external bonds</h3>
<p>Foreign currency bond example: Delhi International Airport Limited (a GMR company) issued USD bonds in February 2020. Euro bond example: a USD bond sold in Kuwait. Hedging the currency risk can wipe out the interest saving. See Chapter 2 for the naming rules and the first masala bond.</p>

<h3>AT1 perpetual bonds</h3>
<p>Many Indian banks issued perpetual bonds as <span class="k">Additional Tier 1 (AT1)</span> capital under <b>Basel III</b>. They are riskier than normal bonds:</p>
<ol>
<li>No fixed maturity date.</li>
<li>Rank below deposits, loans from other banks and all other bonds.</li>
<li>Coupon can be paid only from distributable profits.</li>
<li>Coupon is <b>non-cumulative</b>: a missed coupon is not made up later.</li>
<li>Can be converted into equity by the issuer if a pre-set trigger event happens.</li>
</ol>
</section>

<section class="sec" id="s4"><span class="secno">3.4</span><h2>Commodity words</h2>
<dl class="terms">
<dt>Spot price</dt><dd>Price for immediate delivery, set by supply and demand. Exchanges publish it daily. It is the basis for futures and for the <b>Final Settlement Price (FSP)</b>, which matters for cash settlement or when a seller defaults on delivery.</dd>
<dt>Basis</dt><dd><b>Spot price &minus; futures price.</b></dd>
<dt>Contango</dt><dd>Futures price <b>above</b> spot. Traders may expect the spot price to rise.</dd>
<dt>Backwardation</dt><dd>Futures price <b>below</b> spot. Traders may expect the spot price to fall.</dd>
<dt>Cost of carry</dt><dd>Cost of holding the commodity from purchase until futures delivery: storage, insurance, transport, financing and other costs.</dd>
<dt>Delivery</dt><dd>Commodity futures are deliverable: on expiry the actual goods change hands between buyer and seller.</dd>
</dl>
<div class="trap">Basis is <b>spot minus futures</b>, not the other way round. So in contango (futures above spot) the basis is <b>negative</b>. In backwardation it is positive.</div>
</div>

<figure class="fig" id="fig-carry"><figcaption>Futures fair value calculator<span>Fair value = spot + spot &times; carry rate &times; months &divide; 12. Book example: gold at Rs 1,02,000, 8%, 3 months.</span></figcaption>
<div class="calc">
<div><label for="cc-s">Spot price (10 g gold): <output id="cc-sv"></output></label><input type="range" id="cc-s" min="80000" max="120000" step="1000" value="102000"></div>
<div><label for="cc-r">Cost of carry per year: <output id="cc-rv"></output></label><input type="range" id="cc-r" min="0" max="15" step="0.5" value="8"></div>
<div><label for="cc-m">Months to delivery: <output id="cc-mv"></output></label><input type="range" id="cc-m" min="1" max="12" step="1" value="3"></div>
<div class="calcres">
<div><b id="cc-c"></b><small>carry cost</small></div>
<div><b id="cc-f"></b><small>futures fair value</small></div>
<div><b id="cc-b"></b><small>basis (spot &minus; futures)</small></div>
<div><b id="cc-st"></b><small>market state</small></div>
</div>
</div></figure>

<div class="col">
<section class="sec" id="traps"><h2>All exam traps in this chapter</h2>
<ol class="traplist">
<li>Dividend % is on <b>face value</b>. 30% on Rs 2 face value = Rs 0.60.</li>
<li>Split lowers face value; consolidation raises it. 1 share of Rs 10 split into 5 = 5 shares of Rs 2.</li>
<li>Intrinsic value above market price = undervalued. Below = overvalued.</li>
<li>No fixed cut-off for large, mid and small cap. Book's rule of thumb: top 50 to 100 large, next 200 to 500 mid.</li>
<li>EV subtracts cash and non-operating investments. Use market value of listed equity, not its book value.</li>
<li>TTM = trailing twelve months. Forward earnings = projected.</li>
<li>Forward P/E is lower than current P/E when earnings are expected to grow.</li>
<li>P/S suits loss-making firms. P/BV suits banks and financial firms, not services firms.</li>
<li>P/BV below 1 is not automatically a bargain.</li>
<li>DVR: fewer than 1 vote per share; 10% dividend over 3 years; at most 25% of post-issue paid-up capital; trades at a discount.</li>
<li>Coupon amount = face value &times; coupon rate. G-secs pay half-yearly.</li>
<li>Rates up, bond prices down. A bond with a coupon below market yield trades below face value.</li>
<li>Current yield = coupon &divide; market price. Ignores future cash flows.</li>
<li>YTM = IRR of the bond. Assumes holding to maturity and reinvesting at the same rate.</li>
<li>HPR ignores compounding; realised yield is annualised.</li>
<li>Higher duration with longer maturity, lower coupon, lower yield. Modified duration = Macaulay &divide; (1 + y).</li>
<li>Zero coupon: issued at discount, higher rate risk. Floating: lower rate risk, cap and floor.</li>
<li>Convertibles have lower coupons and dilute EPS on conversion.</li>
<li>PPN still has credit risk.</li>
<li>IIB uses WPI. The 2013 retail inflation securities use CPI with a 1.5% fixed rate.</li>
<li>Foreign currency bond: issuer bears currency risk. Masala bond: investor bears it.</li>
<li>AT1 perpetual coupons are non-cumulative and paid only from distributable profits.</li>
<li>Basis = spot &minus; futures. Contango: futures above spot. Backwardation: futures below spot.</li>
</ol>
</section>

<section class="sec" id="talk"><h2>For the group discussion</h2>
<ol class="talk">
<li>Pick a listed company you know. Find its price, EPS and book value. Work out its P/E and P/BV. Is it cheap?</li>
<li>Why might a bank trade below book value? What would you check before calling it a bargain?</li>
<li>Would you buy a floating rate bond or a zero coupon bond if you expected rates to rise? Why?</li>
<li>Why would a promoter family issue DVRs instead of normal shares?</li>
<li>Gold futures trade below spot. What might traders be expecting?</li>
</ol>
</section>
</div>

<footer>Notes built from the NISM Series XV workbook (February 2026 version). Study aid only.</footer>
</div>
"""

WIDGETS = r"""
window.__WIDGETS__=function(){
const inr=v=>'Rs '+Math.round(v).toLocaleString('en-IN');
/* bond calculator */
const c=document.getElementById('bc-c'),y=document.getElementById('bc-y'),n=document.getElementById('bc-n');
function bond(){const C=+c.value,Y=+y.value/100,N=+n.value;let p=0,w=0;
 for(let t=1;t<=N;t++){const cf=C+(t===N?100:0),pv=cf/Math.pow(1+Y,t);p+=pv;w+=t*pv}
 const mac=w/p;
 document.getElementById('bc-cv').textContent=C+'%';document.getElementById('bc-yv').textContent=(+y.value)+'%';document.getElementById('bc-nv').textContent=N;
 document.getElementById('bc-p').textContent='Rs '+p.toFixed(2);
 document.getElementById('bc-cy').textContent=C===0?'0%':(C/p*100).toFixed(2)+'%';
 document.getElementById('bc-md').textContent=mac.toFixed(2);
 document.getElementById('bc-mod').textContent=(mac/(1+Y)).toFixed(2);
 const d=Math.abs(C-(+y.value))<1e-9;
 document.getElementById('bc-note').textContent=d?'Coupon equals market yield, so the bond trades at face value.':(C<+y.value?'Coupon is below the market yield, so the bond trades below face value (at a discount).':'Coupon is above the market yield, so the bond trades above face value (at a premium).')+(C===0?' A zero coupon bond: duration equals maturity.':'');
}
[c,y,n].forEach(e=>e.addEventListener('input',bond));bond();
/* futures fair value */
const s=document.getElementById('cc-s'),r=document.getElementById('cc-r'),m=document.getElementById('cc-m');
function carry(){const S=+s.value,R=+r.value,M=+m.value,cost=S*R/100*M/12,F=S+cost,b=S-F;
 document.getElementById('cc-sv').textContent=inr(S);document.getElementById('cc-rv').textContent=R+'%';document.getElementById('cc-mv').textContent=M;
 document.getElementById('cc-c').textContent=inr(cost);document.getElementById('cc-f').textContent=inr(F);
 document.getElementById('cc-b').textContent=(b<0?'minus ':'')+inr(Math.abs(b));
 document.getElementById('cc-st').textContent=F>S?'Contango':'Flat';
}
[s,r,m].forEach(e=>e.addEventListener('input',carry));carry();
};
"""
