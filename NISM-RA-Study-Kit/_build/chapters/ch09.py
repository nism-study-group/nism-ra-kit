LEARN = r"""
<style>
.calc{display:grid;gap:14px}
.calc label{display:block;font-weight:700}
.calc select,.calc input[type=number]{font:inherit;width:100%;padding:.45rem .6rem;border:1px solid var(--line);border-radius:8px;background:var(--paper);color:var(--ink)}
.calcin{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
@media (max-width:620px){.calcin{grid-template-columns:repeat(2,1fr)}}
.calcres{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
@media (max-width:520px){.calcres{grid-template-columns:repeat(2,1fr)}}
.calcres div{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:.6rem;text-align:center}
.calcres b{display:block;font-family:var(--head);font-size:1.45rem}
.calcres small{color:var(--muted)}
.calcnote{font-weight:700;margin:.2rem 0 0}
</style>
<div class="wrap">
<header class="hero">
<div class="kicker">Chapter 9 of 15</div>
<h1>Corporate actions</h1>
<div class="meta"><span class="pill">Worth <b>5 marks</b> of 100</span><span class="pill">Book pages 187 to 197</span><span class="pill">About 35 minutes</span></div>
<p class="oneline">What a company does to its <span class="k">shares</span> and its <span class="k">shareholders</span>: pay them, give them more shares, buy shares back, merge, split up, or leave the stock exchange.</p>
</header>

<figure class="fig" id="fig-map"><figcaption>Chapter map<span>Thirteen short parts. Tap to jump.</span></figcaption>
<div class="map">
<a href="#s1"><b>9.1</b><span>The ground rules</span><small>Who regulates, record date</small></a>
<a href="#s2"><b>9.2 and 9.3</b><span>Dividend and rights issue</span><small>Paying out, raising more</small></a>
<a href="#s4"><b>9.4 to 9.6</b><span>Bonus, split, consolidation</span><small>More or fewer shares, same value</small></a>
<a href="#s7"><b>9.7 to 9.10</b><span>Restructuring</span><small>Mergers, demergers, schemes, loans</small></a>
<a href="#s11"><b>9.11</b><span>Buyback</span><small>Returning cash by buying shares</small></a>
<a href="#s12"><b>9.12 and 9.13</b><span>Delisting and share swap</span><small>Leaving the exchange, paying in shares</small></a>
</div></figure>

<div class="col">
<section class="sec" id="s1"><span class="secno">9.1</span><h2>The ground rules</h2>
<p><span class="k">Corporate actions</span> are actions a company takes, apart from its business, that directly affect its stakeholders: paying dividends, issuing more shares, buybacks, mergers and acquisitions, restructuring, delisting, raising debt and others. Once a company has made a public issue, the interests of <b>minority investors</b> must be protected.</p>
<p>Corporate actions are regulated by three sets of rules:</p>
<div class="grid g3">
<div class="box"><h4>Companies Act, 2013</h4></div>
<div class="box"><h4>SEBI regulations</h4></div>
<div class="box"><h4>The listing agreement</h4><p>Signed with the stock exchange</p></div>
</div>
<p>These include giving notice to regulators and stakeholders and following disclosure norms.</p>
<h3>Who gets the benefit?</h3>
<p>Investors whose names appear in the <b>register of members</b> (physical shares) or the <b>register of beneficial owners</b> kept by the depository (demat shares). To decide this, the company announces a <span class="k">record date</span> or a <b>book closure</b> period. Those on the records on that date are eligible.</p>
<div class="analogy">A record date is like a school's attendance register on prize day. Whoever is on the register that morning gets the prize, even if they leave the school the next week.</div>
</section>

<section class="sec" id="s2"><span class="secno">9.2</span><h2>Dividend</h2>
<p>Post-tax profit belongs to shareholders. A company can <b>retain</b> it for the business or <b>return</b> it. Returning money to all shareholders in equal proportion is <span class="k">declaring a dividend</span>. Most companies do some of each. How much they pay depends on opportunities to reinvest, the nature of management, shareholders' expectations and, finally, the cash available.</p>
<div class="grid g2">
<div class="box"><span class="tag">During the year</span><h4>Interim dividend</h4></div>
<div class="box"><span class="tag">At year end</span><h4>Final dividend</h4></div>
</div>
<p>A dividend must be paid within <span class="num">30 days</span> of declaration.</p>
<h3>Declared in rupees per share</h3>
<p>SEBI requires listed companies to declare dividends in <b>rupees per share</b>, not as a percentage of face value. The book's example: a 50% dividend means Re 1 on a Rs 2 share (company A) but Rs 5 on a Rs 10 share (company B). Same percentage, different money. So A now declares "Re 1 per share" and B declares "Rs 5 per share".</p>
<div class="trap">Chapter 3 taught that a dividend stated as a percentage is a percentage of <b>face value</b>. Chapter 9 adds that SEBI now wants listed companies to state it in <b>rupees per share</b>, to avoid that confusion.</div>
<ul>
<li>A company's dividend track record can be seen from its <b>payout ratio</b> = dividend per share &divide; earnings per share.</li>
<li>Dividends are now fully taxable in the hands of shareholders. As per the book, the company deducts <span class="num">10%</span> tax (under section 194 of the Income Tax Act) on dividend income of more than <span class="num">Rs 5,000</span> when paying it.</li>
<li>From assessment year <span class="num">2021-22</span>, a domestic company no longer pays dividend distribution tax.</li>
</ul>

<h3 id="s3">9.3 Rights issue</h3>
<p>A company that needs more equity can ask existing shareholders or bring in new investors. New investors <b>dilute</b> existing holders. The book's example: a company with 10 lakh shares of Rs 10 (capital Rs 1 crore) issues 10 lakh more to new investors. Capital doubles, so existing holders' share is <b>halved</b>.</p>
<p>To prevent this, the <b>Companies Act</b> requires a company raising more capital through shares to <b>first offer them to existing shareholders</b>. That offer is a <span class="k">rights issue</span>.</p>
</div>

<figure class="fig" id="fig-rights"><figcaption>A rights issue, step by step<span>The book's example: shareholder A holds 10 shares priced at Rs 100</span></figcaption>
<div class="flow">
<div class="step"><h4>Offer</h4><p>1-for-2 rights at Rs 70: one new share for every two held</p></div><div class="arrow"></div>
<div class="step hl"><h4>Entitlement</h4><p>A can buy 5 more shares at Rs 70</p></div><div class="arrow"></div>
<div class="step"><h4>Choices</h4><p>Subscribe, apply for extra shares, let it lapse, or <b>renounce</b> (transfer the right, for money or for free)</p></div><div class="arrow"></div>
<div class="step gd"><h4>Result</h4><p>More shares outstanding, more cash on the balance sheet</p></div>
</div></figure>

<div class="col">
<ul>
<li>Subscribing is a <b>choice</b>, not compulsory. Rights entitlements also trade on the stock exchange for a set period.</li>
<li>Rights shares are usually priced at a <b>discount</b> to market price. Logically, if the rights price were higher, investors would just buy in the market.</li>
<li>Shareholders may apply for <b>extra</b> shares beyond their entitlement, from rights that others do not take up.</li>
</ul>
<h3>The rules for a listed company (as per the book)</h3>
<div class="grid g2">
<div class="box"><ul><li>Fix a <b>record date</b> for eligibility</li><li>Issue a <b>letter of offer</b> stating the purpose of the funds</li><li>File the <b>draft</b> letter of offer with <b>SEBI</b></li></ul></div>
<div class="box"><ul><li>Send an <b>abridged</b> letter of offer at least <span class="num">3 days</span> before the issue opens</li><li>Investors may apply on <b>plain paper</b> if they do not get the form</li><li>Open for a minimum of <span class="num">15 days</span> and a maximum of <span class="num">30 days</span></li></ul></div>
</div>
<div class="trap">If every shareholder takes up their full rights, each one's <b>proportion of ownership stays the same</b>; only the number of shares goes up. Dilution hits only those who do not subscribe.</div>
</section>

<section class="sec" id="s4"><span class="secno">9.4</span><h2>Bonus issue</h2>
<p>A <span class="k">bonus issue</span>, also called an <b>equity dividend</b>, is an alternative to a cash dividend. Shareholders get new shares <b>free</b>. The company moves money from its reserves into paid-up capital. This is called <span class="k">capitalisation of reserves</span>.</p>
<ul>
<li>Ratio <b>1:3</b> means 1 bonus share for every 3 shares held.</li>
<li>Bonus is made only from <b>free reserves built from genuine profits</b>. Reserves from <b>revaluation of assets</b> cannot be used.</li>
<li>A company <b>cannot</b> issue bonus shares if it has defaulted on interest or principal of any debt security or fixed deposit.</li>
<li>No money changes hands, so the value of the holding is the same before and after. The book says bonus issues mainly influence investor <b>psychology</b>, with no economic impact.</li>
</ul>
<div class="analogy">Cutting a pizza into more slices. You have more slices, each one smaller, and exactly the same amount of pizza.</div>

<h3 id="s5">9.5 Stock split</h3>
<p>A <span class="k">stock split</span> reduces the <b>face value</b> of each share in a set ratio. Split <b>1:5</b> means one share becomes five, and face value falls to one fifth. The book's example: 100 shares of Rs 10 become 500 shares of Rs 2. Share capital does not change (more shares &times; lower face value).</p>
<p>Companies split when the share price is so high that it limits participation. A lower price per share brings <b>greater liquidity</b>. Like a bonus, it is a book entry with no economic benefit.</p>
<div class="why"><b>The book's SBI example</b>SBI split its shares from Rs 10 face value to Re 1. One share became ten. The share traded above Rs 2,700 at the announcement and around Rs 295 after the split, so one share's worth of holding went from about Rs 2,700 to Rs 2,950 (10 &times; 295). After a split, the price depends on demand and supply.</div>

<h3 id="s6">9.6 Share consolidation</h3>
<p>The <b>reverse</b> of a split. <span class="k">Consolidation</span> increases face value in a set ratio and reduces the number of shares, keeping paid-up capital the same. Consolidation <b>5:1</b> means five shares become one. The book's example: 500 shares of Rs 2 become 100 shares of Rs 10.</p>
<p>Companies consolidate when the share price is so low that it hurts how investors see the company. A higher price can improve that perception.</p>
</div>

<figure class="fig" id="fig-bonussplit"><figcaption>Bonus, split and consolidation side by side<span>All three are book entries. The value of your holding does not change.</span></figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th></th><th>Bonus issue</th><th>Stock split</th><th>Consolidation</th></tr></thead>
<tbody>
<tr><th>Number of shares</th><td>Goes up</td><td>Goes up</td><td>Goes down</td></tr>
<tr><th>Face value</th><td>Not discussed in the book. It says reserves move into paid-up capital</td><td>Goes down</td><td>Goes up</td></tr>
<tr><th>Share capital</th><td>Goes up (reserves capitalised)</td><td>No change</td><td>No change</td></tr>
<tr><th>Per-share data (EPS, book value, price)</th><td>Falls</td><td>Falls</td><td>Rises</td></tr>
<tr><th>Your share of ownership</th><td>Same</td><td>Same</td><td>Same</td></tr>
<tr><th>Book's price example</th><td>1:1 bonus: Rs 1,000 to about Rs 500. 100 &times; 1,000 = 200 &times; 500</td><td>SBI: above Rs 2,700 to about Rs 295 (1 share became 10)</td><td>5:1: Rs 5 to about Rs 25. 500 &times; 5 = 100 &times; 25</td></tr>
<tr><th>Why companies do it</th><td>Alternative to a cash dividend; investor psychology</td><td>Price too high; improve liquidity</td><td>Price too low; improve perception</td></tr>
</tbody></table></div></figure>

<figure class="fig" id="fig-cacalc"><figcaption>Try it: bonus, split or consolidation<span>The book's rule: the value of your holding stays the same. Real prices move a little with demand and supply.</span></figcaption>
<div class="calc">
<div class="calcin">
<div><label for="ca-act">Action</label><select id="ca-act"><option value="bonus">Bonus issue</option><option value="split">Stock split</option><option value="cons">Consolidation</option></select></div>
<div><label for="ca-r" id="ca-rl">Ratio</label><select id="ca-r"></select></div>
<div><label for="ca-n">Shares you hold</label><input type="number" id="ca-n" value="100" min="1"></div>
<div><label for="ca-p">Price before (Rs)</label><input type="number" id="ca-p" value="1000" min="1"></div>
</div>
<div class="calcres">
<div><b id="ca-sh"></b><small>shares after</small></div>
<div><b id="ca-pr"></b><small>price after, about</small></div>
<div><b id="ca-v1"></b><small>holding before</small></div>
<div><b id="ca-v2"></b><small>holding after</small></div>
</div>
<p class="calcnote" id="ca-note"></p>
</div></figure>

<div class="col">
<div class="trap">Watch the ratio wording. <b>Bonus 1:3</b> = 1 new share for every 3 held. <b>Split 1:5</b> = 1 share becomes 5. <b>Consolidation 5:1</b> = 5 shares become 1.</div>
</section>

<section class="sec" id="s7"><span class="secno">9.7</span><h2>Mergers and acquisitions</h2>
<p>These change the ownership structure of the companies involved.</p>
</div>

<figure class="fig" id="fig-ma"><figcaption>Merger, acquisition, consolidation<span>Who survives?</span></figcaption>
<div class="grid g3">
<div class="box"><span class="tag">Merger</span><h4>Target is absorbed</h4><p>The acquirer buys the target's shares. The target is absorbed into the acquirer and <b>ceases to exist</b>. Its assets and liabilities pass to the acquirer.</p></div>
<div class="box"><span class="tag">Acquisition (takeover)</span><h4>Both carry on</h4><p>The acquirer buys all or a substantial part of the target's stock. <b>Both entities</b> typically continue to exist.</p></div>
<div class="box"><span class="tag">Consolidation</span><h4>A new company is born</h4><p>Companies combine to form a <b>new company</b>, and the merged companies cease to exist.</p></div>
</div></figure>

<div class="col">
<h3>Why companies merge: four motives</h3>
<div class="grid g2">
<div class="box"><h4>Synergy</h4><p>Combined strengths give bigger benefits: economies of scale, forward and backward integration, a bigger market.</p></div>
<div class="box"><h4>Revenue and market share</h4><p>Two competitors combining gain revenue and share.</p></div>
<div class="box"><h4>Diversification</h4><p>Into a new geography or a complementary business.</p></div>
<div class="box"><h4>Taxation</h4><p>A profitable company buys a loss-making one to use its losses as a tax shield.</p></div>
</div>
<p>When an acquirer, and persons acting in concert with it, substantially acquire shares and voting rights in a listed company, SEBI's takeover regulations (named in the book as the SEBI (Substantial Acquisition of Shares and Takeover) Regulations, 1997) set the triggers and give public shareholders a chance to <b>exit</b> if they wish.</p>

<h3 id="s8">9.8 Demerger or spin-off</h3>
<p>A <span class="k">spin-off</span> carves one or more businesses out into a separate company. Shareholders on the record date get shares in the new company <b>in proportion</b> to their holding in the parent.</p>
<div class="why"><b>The book's Adani example</b>In <b>April 2018</b>, Adani Enterprises spun off its renewable energy business as <b>Adani Green Energy</b>, giving shareholders new shares in the ratio <span class="num">761:1000</span> (761 Adani Green shares for every 1,000 Adani Enterprises shares). Earlier, in <b>June 2015</b>, it spun off its ports and its power transmission businesses as <b>Adani Ports</b> and <b>Adani Transmission</b>.</div>

<h3 id="s9">9.9 Scheme of arrangement</h3>
<p>When a company cannot meet its obligations to creditors or to a class of shareholders (for example, failing to redeem preference shares), the company and its creditors or members can agree a <span class="k">scheme of arrangement</span>.</p>
<ul>
<li>A <b>court-monitored</b> settlement. Usually reorganises share capital: shareholders may give up part of their ownership to creditors, or classes of shares may be consolidated or divided.</li>
<li>Under <b>section 230 of the Companies Act, 2013</b>, it can be sought by the company, its creditors or its members.</li>
<li>The term covers <b>all types of corporate restructuring</b>, including mergers and acquisitions. Using it in bankruptcy is just one use.</li>
<li>The applicant approaches the <b>National Company Law Tribunal (NCLT)</b>, which orders meetings of the company, creditors and members to reach a compromise.</li>
</ul>

<h3 id="s10">9.10 Loan restructuring</h3>
<p>A company in financial distress, unable to pay its lenders, can change one or more terms of its loans: the amount, the interest rate, the mode of repayment (cash or equity), or the term. The aim is repayment within the borrower's capacity.</p>
<div class="grid g2">
<div class="box gd"><h4>The borrower gains</h4><p>A feasible way to repay, without being declared a defaulter. It can focus on rebuilding the business and the balance sheet.</p></div>
<div class="box gd"><h4>The lender gains</h4><p>Some repayment on a loan that would otherwise be written off as a bad debt.</p></div>
</div>
<p>The process: analyse the debt position, meet lenders, share current and future financials, and agree a workable plan backed by a <b>concrete business plan</b>.</p>
</section>

<section class="sec" id="s11"><span class="secno">9.11</span><h2>Buyback of shares</h2>
<p>A company with spare cash can grow the business, repay borrowings, or return money to shareholders. To return it, it can pay a <b>dividend</b> to everyone equally, or offer a <span class="k">buyback</span>: shareholders choose whether to sell shares back, and those who stay get a higher EPS and book value per share.</p>
</div>

<figure class="fig" id="fig-buyback"><figcaption>Six motives for a buyback<span>As listed in the book</span></figcaption>
<div class="grid g3">
<div class="box"><p>Give the stock a <b>value boost</b> if it looks undervalued</p></div>
<div class="box"><p><b>Excess cash</b> and too few profitable investments</p></div>
<div class="box"><p>A <b>confidence-building</b> measure</p></div>
<div class="box"><p>A <b>defence</b> against a possible takeover</p></div>
<div class="box"><p>Reduce equity and so <b>increase leverage</b></p></div>
<div class="box"><p>Offset <b>dilution</b> of promoters' holding, for example from ESOPs</p></div>
</div>
<p class="ptr" style="margin-top:8px">The book adds: every management talks up the benefits to minority shareholders, but its real intention is very hard to judge.</p>
</figure>

<div class="col">
<h3>The rules (as per the book)</h3>
<ul>
<li>Only out of <b>reserves and surplus</b>.</li>
<li>Bought-back shares are <b>extinguished</b> within a set time, so share capital falls.</li>
<li>Not allowed if the company has defaulted on interest or principal of debentures, fixed deposits or other borrowings, on redeeming preference shares, or on paying a declared dividend.</li>
<li>Methods: a <b>tender offer</b> to existing shareholders on a proportionate basis; the <b>open market</b> through book building or the stock exchange; or from <b>odd-lot holders</b>.</li>
<li>Needs a <b>special resolution</b> stating the time frame and the maximum price.</li>
</ul>
<div class="why"><b>Why EPS rises</b>Fewer shares share the same profit. Even with no change in the P&amp;L, EPS goes up for the shareholders who remain, and they may get a higher dividend per share. If the market values the company on earnings, the value per share also rises.</div>
</section>

<section class="sec" id="s12"><span class="secno">9.12</span><h2>Delisting and relisting</h2>
<p><span class="k">Delisting</span> is the permanent removal of a company's shares from a stock exchange.</p>
<div class="grid g2">
<div class="box bd"><span class="tag">Compulsory</span><p>Because the company did not comply with regulations or the listing agreement.</p></div>
<div class="box"><span class="tag">Voluntary</span><p>The company chooses to go private: to escape reporting complexity, after a merger or acquisition, or for freedom to change strategy. Must follow SEBI's regulations.</p></div>
</div>
</div>

<figure class="fig" id="fig-delist"><figcaption>Voluntary delisting: reverse book building<span>As per the book</span></figcaption>
<div class="flow">
<div class="step"><h4>Floor price</h4><p>Promoters invite bids and set a floor price</p></div><div class="arrow"></div>
<div class="step"><h4>Shareholders bid</h4><p>Each states the price at which they will sell</p></div><div class="arrow"></div>
<div class="step"><h4>Promoters decide</h4><p>Accept, reject (cancel the delisting) or make a counter-offer</p></div><div class="arrow"></div>
<div class="step gd"><h4>Delisting succeeds only if</h4><p>Promoter holding crosses <b>90%</b>, and at least <b>25%</b> of public shareholders took part</p></div>
</div></figure>

<div class="col">
<ul>
<li>SEBI requires promoters to give <b>all shareholders an exit</b> opportunity.</li>
<li>Public shareholders still holding shares after delisting can sell them to the promoters at the <b>exit price</b> within <span class="num">one year</span>.</li>
<li>No minority shareholder can be <b>forced</b> to exit.</li>
</ul>
<div class="trap">Relisting waiting periods, as per the SEBI (Delisting of Equity Shares) Regulations, 2009 cited in the book: <span class="num">5 years</span> after a <b>voluntary</b> delisting, <span class="num">10 years</span> after a <b>compulsory</b> one.</div>

<h3 id="s13">9.13 Share swap</h3>
<p>Swap means exchange. In a <span class="k">share swap</span>, usually in a merger or acquisition, the acquirer pays with <b>its own shares</b> instead of cash. Each shareholder of the acquired company gets a pre-set number of the acquirer's shares. Both companies must be valued accurately first, so the <b>swap ratio</b> is fair.</p>
</section>

<section class="sec" id="traps"><h2>All exam traps in this chapter</h2>
<ol class="traplist">
<li>Corporate actions are governed by the Companies Act 2013, SEBI regulations and the listing agreement.</li>
<li>Eligibility is decided by the record date or book closure.</li>
<li>Dividends must be paid within 30 days of declaration.</li>
<li>SEBI: listed companies declare dividends in rupees per share, not as a % of face value.</li>
<li>Payout ratio = DPS &divide; EPS.</li>
<li>Book: 10% tax deducted on dividend income above Rs 5,000. No dividend distribution tax from AY 2021-22.</li>
<li>A rights issue must be offered to existing shareholders first (Companies Act).</li>
<li>Rights: discount to market price; can be renounced; trade on the exchange.</li>
<li>Rights issue open 15 to 30 days; abridged letter of offer at least 3 days before opening; draft filed with SEBI.</li>
<li>Bonus = equity dividend = capitalisation of reserves. Not from revaluation reserves.</li>
<li>No bonus if the company has defaulted on interest or principal on debt securities or fixed deposits.</li>
<li>Bonus 1:3 = 1 new for every 3 held. Split 1:5 = 1 becomes 5. Consolidation 5:1 = 5 become 1.</li>
<li>Split and consolidation leave share capital unchanged; face value moves the other way to the number of shares.</li>
<li>Bonus and split: per-share data falls. Consolidation: per-share data rises. Ownership share never changes.</li>
<li>Merger: target ceases to exist. Acquisition: both continue. Consolidation: a new company, old ones cease.</li>
<li>M&amp;A motives: synergy, revenue and market share, diversification, taxation.</li>
<li>Spin-off: new shares in proportion to holdings. Adani Green: 761:1000 (April 2018).</li>
<li>Scheme of arrangement: section 230, Companies Act 2013; approach the NCLT; covers all restructuring including M&amp;A.</li>
<li>Buyback only out of reserves and surplus; shares extinguished; special resolution with time frame and maximum price.</li>
<li>Buyback raises EPS for remaining shareholders even with no change in profit.</li>
<li>Voluntary delisting: reverse book building; promoter holding must cross 90%; at least 25% of public shareholders must take part.</li>
<li>Remaining holders can sell at the exit price for one year after delisting.</li>
<li>Relisting: 5 years after voluntary delisting, 10 years after compulsory.</li>
<li>Share swap: acquirer pays in its own shares; a fair swap ratio needs both companies valued.</li>
</ol>
</section>

<section class="sec" id="talk"><h2>For the group discussion</h2>
<ol class="talk">
<li>If a bonus issue does not change the value of your holding, why do share prices often rise when a bonus is announced?</li>
<li>A cash-rich company announces a buyback instead of a dividend. Which would you prefer as a shareholder, and why?</li>
<li>You get a rights offer at a 30% discount but do not want to invest more. What are your choices?</li>
<li>Why might promoters want to delist a profitable company? How do the rules protect minority shareholders?</li>
<li>Pick a recent Indian demerger. Did the parts end up worth more than the whole?</li>
</ol>
</section>
</div>

<footer>Notes built from the NISM Series XV workbook (February 2026 version). Study aid only.</footer>
</div>
"""

WIDGETS = r"""
window.__WIDGETS__=function(){
const act=document.getElementById('ca-act'),r=document.getElementById('ca-r'),n=document.getElementById('ca-n'),p=document.getElementById('ca-p');
if(!act)return;
const RAT={bonus:[['1:1','1 new for every 1 held',1,1],['1:2','1 new for every 2 held',1,2],['1:3','1 new for every 3 held',1,3],['2:1','2 new for every 1 held',2,1]],
 split:[['1:2','1 share becomes 2',2],['1:5','1 share becomes 5',5],['1:10','1 share becomes 10',10]],
 cons:[['2:1','2 shares become 1',2],['5:1','5 shares become 1',5],['10:1','10 shares become 1',10]]};
function fill(){r.innerHTML=RAT[act.value].map((x,i)=>'<option value="'+i+'">'+x[0]+' ('+x[1]+')</option>').join('');}
const inr=v=>'Rs '+Math.round(v).toLocaleString('en-IN');
function calc(){const N=Math.max(0,Math.floor(+n.value)),P=Math.max(0,+p.value),x=RAT[act.value][+r.value||0];
 let after,note;
 if(act.value==='bonus'){after=N+Math.floor(N*x[2]/x[3]);note='Bonus shares come from reserves moved into share capital. You pay nothing.'}
 else if(act.value==='split'){after=N*x[2];note='Face value falls to 1/'+x[2]+'. Share capital is unchanged.'}
 else{after=Math.floor(N/x[2]);note='Face value rises '+x[2]+' times. Share capital is unchanged.'+(N%x[2]?' ('+(N%x[2])+' leftover shares do not make a whole new share.)':'')}
 const v=N*P,pa=after?v/after:0;
 document.getElementById('ca-sh').textContent=after.toLocaleString('en-IN');
 document.getElementById('ca-pr').textContent='Rs '+(Math.round(pa*100)/100).toLocaleString('en-IN');
 document.getElementById('ca-v1').textContent=inr(v);
 document.getElementById('ca-v2').textContent=inr(after*pa);
 document.getElementById('ca-note').textContent=note;
}
act.addEventListener('change',()=>{fill();calc()});[r,n,p].forEach(e=>e.addEventListener('input',calc));r.addEventListener('change',calc);
fill();calc();
};
"""

CARDS = [
 {"f":"Corporate actions are regulated by...","b":"The <b>Companies Act, 2013</b>, <b>SEBI regulations</b>, and the <b>listing agreement</b> with the stock exchange."},
 {"f":"How is eligibility for a corporate action decided?","b":"By the <b>record date</b> or <b>book closure</b> period: names on the register of members or beneficial owners on that date."},
 {"f":"Interim versus final dividend","b":"Interim: declared during the year. Final: at the end of the year."},
 {"f":"Deadline for paying a declared dividend","b":"Within <b>30 days</b> of declaration."},
 {"f":"How must listed companies declare dividends now?","b":"In <b>rupees per share</b>, not as a % of face value (SEBI)."},
 {"f":"50% dividend on Rs 2 and Rs 10 face value shares","b":"<b>Re 1</b> and <b>Rs 5</b> per share. So SEBI wants rupees per share."},
 {"f":"Payout ratio","b":"Dividend per share &divide; earnings per share."},
 {"f":"Tax on dividends (book)","b":"Taxable for shareholders. Company deducts <b>10%</b> (section 194) on dividend income above <b>Rs 5,000</b>. No DDT from AY <b>2021-22</b>."},
 {"f":"Rights issue","b":"New shares offered <b>first to existing shareholders</b>, as the Companies Act requires, to prevent dilution."},
 {"f":"Renunciation of rights","b":"Transferring your rights entitlement to someone else, for money or for free."},
 {"f":"Why are rights shares priced at a discount?","b":"If the rights price were above market, investors would simply buy in the market."},
 {"f":"1-for-2 rights at Rs 70, holder of 10 shares","b":"Can buy <b>5</b> more shares at Rs 70."},
 {"f":"Rights issue period (book)","b":"Minimum <b>15 days</b>, maximum <b>30 days</b>."},
 {"f":"Abridged letter of offer (book)","b":"Sent at least <b>3 days</b> before the issue opens. The draft letter of offer is filed with SEBI."},
 {"f":"No application form received for a rights issue?","b":"Investors can apply on <b>plain paper</b>."},
 {"f":"Who is diluted in a rights issue?","b":"Only those who do <b>not</b> subscribe. Full takers keep their proportion."},
 {"f":"Bonus issue, other names","b":"<b>Equity dividend</b> (alternative to a cash dividend); issuing it is <b>capitalisation of reserves</b>."},
 {"f":"Which reserves can fund a bonus issue?","b":"<b>Free reserves from genuine profits.</b> Not revaluation reserves."},
 {"f":"When can a company not issue bonus shares?","b":"If it has defaulted on interest or principal of any debt security or fixed deposit."},
 {"f":"Bonus ratio 1:3","b":"<b>1</b> bonus share for every <b>3</b> held."},
 {"f":"1:1 bonus, price Rs 1,000 before","b":"About <b>Rs 500</b> after. 100 &times; 1,000 = 200 &times; 500."},
 {"f":"Stock split 1:5","b":"1 share becomes 5; face value falls to 1/5. 100 shares of Rs 10 become 500 of Rs 2."},
 {"f":"Why split shares?","b":"Price too high limits participation; a lower price gives <b>greater liquidity</b>."},
 {"f":"SBI split (book)","b":"Rs 10 to Re 1 face value. Price above Rs 2,700 before, about Rs 295 after."},
 {"f":"Share consolidation 5:1","b":"5 shares become 1; face value rises 5 times. 500 shares of Rs 2 become 100 of Rs 10."},
 {"f":"Why consolidate shares?","b":"Price too low hurts perception; a higher price improves it."},
 {"f":"Effect on share capital: split and consolidation","b":"<b>No change</b>. Number of shares and face value move in opposite directions."},
 {"f":"Per-share data after bonus or split, and after consolidation","b":"Bonus or split: <b>falls</b>. Consolidation: <b>rises</b>. Ownership share never changes."},
 {"f":"Merger versus acquisition versus consolidation","b":"Merger: target absorbed, ceases. Acquisition: both continue. Consolidation: new company formed, old ones cease."},
 {"f":"Four M&amp;A motives","b":"Synergy; revenue and market share; geographical or other diversification; taxation (using a loss-maker's tax shield)."},
 {"f":"Takeover regulations named in the book","b":"SEBI (Substantial Acquisition of Shares and Takeover) Regulations, 1997: triggers, and an exit for public shareholders."},
 {"f":"Spin-off (demerger)","b":"A business carved into a separate company; shareholders get new shares <b>in proportion</b> to their holding."},
 {"f":"Adani Green spin-off (book)","b":"<b>April 2018</b>, ratio <b>761:1000</b>. Earlier, June 2015: Adani Ports and Adani Transmission."},
 {"f":"Scheme of arrangement","b":"Court-monitored settlement with creditors or members, usually reorganising capital. Section <b>230</b>, Companies Act 2013. Apply to the <b>NCLT</b>."},
 {"f":"Does \"scheme of arrangement\" cover mergers?","b":"<b>Yes.</b> It covers all types of corporate restructuring, including M&amp;A."},
 {"f":"Loan restructuring: what can change?","b":"Loan amount, interest rate, mode of repayment (cash or equity), term."},
 {"f":"Who gains from loan restructuring?","b":"Both: the borrower avoids default; the lender recovers something instead of a bad debt."},
 {"f":"Six buyback motives","b":"Boost an undervalued stock; excess cash; confidence; takeover defence; raise leverage; offset ESOP dilution."},
 {"f":"Source of funds for a buyback","b":"Only <b>reserves and surplus</b>."},
 {"f":"What happens to bought-back shares?","b":"<b>Extinguished</b>, so share capital falls."},
 {"f":"Buyback methods","b":"Tender offer (proportionate); open market (book building or stock exchange); odd-lot holders."},
 {"f":"Approval needed for a buyback","b":"A <b>special resolution</b> stating the time frame and maximum price."},
 {"f":"Buyback and EPS","b":"EPS <b>rises</b> for remaining shareholders even if profit is unchanged."},
 {"f":"Compulsory versus voluntary delisting","b":"Compulsory: non-compliance. Voluntary: company chooses to go private."},
 {"f":"Voluntary delisting: pricing method","b":"<b>Reverse book building</b>: promoters set a floor price, shareholders bid the price they will sell at."},
 {"f":"Voluntary delisting: two conditions (book)","b":"Promoter holding must cross <b>90%</b>; at least <b>25%</b> of public shareholders must participate."},
 {"f":"After delisting, public shareholders can...","b":"Sell to promoters at the exit price within <b>one year</b>. No one can be forced to exit."},
 {"f":"Relisting waiting period (book)","b":"<b>5 years</b> after voluntary delisting; <b>10 years</b> after compulsory."},
 {"f":"Share swap","b":"Acquirer pays with its own shares. Both companies must be valued for a fair swap ratio."},
]

MCQS = [
 {"id":"9.1","q":"When companies give new shares to their existing shareholders without any consideration, it is known as ______.","o":["Stock dividend","Special dividend","Interim dividend","Cash dividend"],"a":0,"w":"Book sample question. The book calls a bonus issue an equity dividend: a dividend paid in shares, issued without consideration."},
 {"id":"9.2","q":"The Companies Act requires that a company wanting to raise further capital through an issue of shares must first offer them to existing shareholders. Such an offer is known as a ______.","o":["Rights issue","Bonus issue","Public issue","Preference issue"],"a":0,"w":"Book sample question."},
 {"id":"9.3","q":"Changing the structure of share capital by increasing the par value of shares in a defined ratio and correspondingly reducing the number of shares, to maintain paid-up capital, is known as ______.","o":["Share consolidation","Stock split","Spin-off","Share swap"],"a":0,"w":"Book sample question. Consolidation is the reverse of a split."},
 {"id":"9.4","q":"Corporate actions are regulated by which of the following?","o":["All of the above","The Companies Act, 2013","SEBI regulations","The listing agreement with the stock exchange"],"a":0,"w":"The book lists all three."},
 {"id":"9.5","q":"Shareholders eligible for a corporate action benefit are determined by the:","o":["Record date or book closure period","Date of the board meeting","Date of the AGM notice","Date the shares were first issued"],"a":0,"w":"Names on the register of members or beneficial owners on that date are eligible."},
 {"id":"9.6","q":"A company must pay a declared dividend within:","o":["30 days of declaration","7 days of declaration","90 days of declaration","The next financial year"],"a":0,"w":"As stated in the book."},
 {"id":"9.7","q":"SEBI has mandated that listed companies declare dividends:","o":["In rupees per share","As a percentage of face value","As a percentage of market price","As a percentage of net profit"],"a":0,"w":"This avoids confusion when shares have different face values."},
 {"id":"9.8","q":"Two companies each declare a 50% dividend. Company A's face value is Rs 2 and Company B's is Rs 10. The dividends per share are:","o":["Re 1 and Rs 5","Rs 5 and Re 1","Rs 50 for both","Re 1 for both"],"a":0,"w":"50% of face value: 0.5 &times; 2 = 1 and 0.5 &times; 10 = 5. The book's own example."},
 {"id":"9.9","q":"As per the book, a company deducts 10% tax on dividend income above Rs ______ while crediting the dividend.","o":["5,000","10,000","2,500","50,000"],"a":0,"w":"Under section 194 of the Income Tax Act, as per the book."},
 {"id":"9.10","q":"A company has 10 lakh shares and issues another 10 lakh shares to new investors. The proportion held by existing shareholders:","o":["Comes down by half","Doubles","Stays the same","Falls by 10%"],"a":0,"w":"The book's dilution example: capital doubles, so existing holders own half as much proportionately."},
 {"id":"9.11","q":"A shareholder holds 10 shares. The company announces a 1-for-2 rights issue at Rs 70. How many shares can the shareholder buy?","o":["5","20","2","10"],"a":0,"w":"One share for every two held: 10 &divide; 2 = 5."},
 {"id":"9.12","q":"Transferring your rights entitlement to another person, with or without consideration, is called:","o":["Renunciation of rights","Consolidation","Delisting","Share swap"],"a":0,"w":"Rights entitlements also trade on the stock exchange for a defined period."},
 {"id":"9.13","q":"Shares under a rights issue are generally offered:","o":["At a discount to the market price","At a premium to the market price","Only at face value","Free of cost"],"a":0,"w":"If the rights price were higher than market, investors would buy in the market instead."},
 {"id":"9.14","q":"As per the book, a rights issue is open for subscription for a minimum of ______ and a maximum of ______.","o":["15 days; 30 days","7 days; 15 days","30 days; 60 days","3 days; 10 days"],"a":0,"w":"3 days is the minimum gap between sending the abridged letter of offer and the issue opening."},
 {"id":"9.15","q":"If all shareholders subscribe to their full rights entitlement:","o":["Their proportionate ownership remains unchanged","Their ownership is diluted","The company's cash falls","The number of shares outstanding falls"],"a":0,"w":"Shares outstanding and cash both rise, but proportions stay the same."},
 {"id":"9.16","q":"Issuing bonus shares is termed:","o":["Capitalisation of reserves","Dilution of reserves","Revaluation of assets","Reduction of capital"],"a":0,"w":"Reserves are transferred to paid-up capital."},
 {"id":"9.17","q":"Which reserves can NOT be used for a bonus issue?","o":["Reserves built from revaluation of assets","Free reserves built from genuine profits","General reserve from profits","Retained earnings from profits"],"a":0,"w":"The book says only free reserves from genuine profits can be used."},
 {"id":"9.18","q":"A bonus issue in the ratio 1:3 entitles a shareholder to:","o":["1 bonus share for every 3 shares held","3 bonus shares for every 1 share held","1 share for every 3 shares after consolidation","A 33% cash dividend"],"a":0,"w":"The first number is the new shares, the second the shares held."},
 {"id":"9.19","q":"A shareholder holds 300 shares priced at Rs 800. After a 1:3 bonus, the theoretical price and holding value are:","o":["Rs 600 per share; Rs 2,40,000","Rs 800 per share; Rs 3,20,000","Rs 267 per share; Rs 2,40,000","Rs 600 per share; Rs 1,80,000"],"a":0,"w":"300 + 100 = 400 shares. Value stays 300 &times; 800 = 2,40,000. Price = 2,40,000 &divide; 400 = 600."},
 {"id":"9.20","q":"A company cannot make a bonus issue if it has:","o":["Defaulted on payment of interest or principal on any debt security or fixed deposit","Paid an interim dividend","Split its shares in the past","More than 1,000 shareholders"],"a":0,"w":"As stated in the book."},
 {"id":"9.21","q":"An investor holds 100 shares of face value Rs 10. After a 1:5 stock split, the investor holds:","o":["500 shares of face value Rs 2","20 shares of face value Rs 50","500 shares of face value Rs 10","100 shares of face value Rs 2"],"a":0,"w":"The book's own example. Share capital stays the same."},
 {"id":"9.22","q":"A company's share capital after a stock split:","o":["Remains unchanged","Increases","Decreases","Is converted to reserves"],"a":0,"w":"More shares at a lower face value: the product stays the same."},
 {"id":"9.23","q":"Companies usually split their shares when:","o":["The share price is very high and restricts participation","The share price is very low","They want to raise new capital","They want to delist"],"a":0,"w":"A lower price per share leads to greater liquidity."},
 {"id":"9.24","q":"After a share consolidation, per-share data such as EPS and book value per share:","o":["Improve immediately","Deteriorate immediately","Stay the same","Become zero"],"a":0,"w":"Fewer shares share the same profit and net worth. Ownership share does not change."},
 {"id":"9.25","q":"Shares trade at Rs 5 before a 5:1 consolidation. The fair price after is likely to be about:","o":["Rs 25","Rs 1","Rs 5","Rs 10"],"a":0,"w":"The book's example: 500 &times; 5 = 100 &times; 25."},
 {"id":"9.26","q":"In which corporate action does the target company cease to exist after being absorbed into the acquirer?","o":["Merger","Acquisition","Spin-off","Rights issue"],"a":0,"w":"In an acquisition both usually continue. In a consolidation, a new company is formed."},
 {"id":"9.27","q":"Companies combine to form a new company and the original companies cease to exist. This is a:","o":["Consolidation","Merger","Acquisition","Demerger"],"a":0,"w":"As defined in section 9.7."},
 {"id":"9.28","q":"A profitable company buys a loss-making company to gain a tax shield. This M&amp;A motive is:","o":["Taxation","Synergy","Market share","Geographical diversification"],"a":0,"w":"The four motives in the book: synergy, revenue and market share, diversification, taxation."},
 {"id":"9.29","q":"In a spin-off, shareholders of the parent company on the record date:","o":["Receive shares in the new company in proportion to their holding","Must pay for new shares at market price","Lose their parent company shares","Receive only cash"],"a":0,"w":"Book example: Adani Green Energy shares at 761 for every 1,000 Adani Enterprises shares."},
 {"id":"9.30","q":"A shareholder holds 2,000 shares of Adani Enterprises at the record date of the April 2018 spin-off (ratio 761:1000). How many Adani Green Energy shares does the shareholder get?","o":["1,522","761","2,628","1,000"],"a":0,"w":"2,000 &times; 761 &divide; 1,000 = 1,522."},
 {"id":"9.31","q":"Under the Companies Act, 2013, a scheme of arrangement is covered under section:","o":["230","194","49","110"],"a":0,"w":"The applicant approaches the NCLT."},
 {"id":"9.32","q":"A scheme of arrangement is sought by approaching the:","o":["National Company Law Tribunal (NCLT)","SEBI","Stock exchange","Reserve Bank of India"],"a":0,"w":"The NCLT orders meetings of the company, creditors and members."},
 {"id":"9.33","q":"Which statement about a scheme of arrangement is correct as per the book?","o":["It covers all types of corporate restructuring, including mergers and acquisitions","It can be used only in bankruptcy","Only creditors can seek it","It does not involve any court or tribunal"],"a":0,"w":"Bankruptcy is only one use. The company, creditors or members can seek it."},
 {"id":"9.34","q":"Which of the following is NOT a term that can be modified in loan restructuring, as per the book?","o":["The company's face value of shares","Rate of interest","Term of the loan","Mode of repayment"],"a":0,"w":"The book lists the loan amount, rate, mode of repayment and term."},
 {"id":"9.35","q":"Which of the following is NOT a motive for buyback listed in the book?","o":["To increase the number of shares outstanding","Excess cash and lack of profitable investment opportunities","A defensive strategy against a potential takeover","To offset dilution in promoters' holding from ESOPs"],"a":0,"w":"A buyback reduces the number of shares."},
 {"id":"9.36","q":"A buyback of shares can be done only out of:","o":["Reserves and surplus","Borrowed funds","Share premium on new issues","Revaluation reserve only"],"a":0,"w":"The shares bought back are then extinguished."},
 {"id":"9.37","q":"A company has net profit of Rs 100 crore and 10 crore shares. It buys back 2 crore shares and profit is unchanged. EPS moves from:","o":["Rs 10 to Rs 12.50","Rs 10 to Rs 8","Rs 12.50 to Rs 10","Rs 10 to Rs 10"],"a":0,"w":"100 &divide; 10 = 10 before; 100 &divide; 8 = 12.50 after."},
 {"id":"9.38","q":"For a buyback, the company must pass a:","o":["Special resolution specifying the time frame and maximum price","Board resolution only","Resolution of the stock exchange","Court order"],"a":0,"w":"As stated in the book."},
 {"id":"9.39","q":"Delisting because a company has not complied with regulations and the listing agreement is called:","o":["Compulsory delisting","Voluntary delisting","Relisting","Suspension of rights"],"a":0,"w":"Voluntary delisting is when the company chooses to go private."},
 {"id":"9.40","q":"In voluntary delisting, shares are acquired from public shareholders through:","o":["Reverse book building","A rights issue","A bonus issue","A stock split"],"a":0,"w":"Promoters set a floor price and shareholders bid the price they will sell at."},
 {"id":"9.41","q":"As per the book, voluntary delisting can go through only if the promoter holding crosses ______ and at least ______ of public shareholders participate in the reverse book building.","o":["90%; 25%","75%; 50%","51%; 10%","90%; 50%"],"a":0,"w":"Both conditions are stated in section 9.12."},
 {"id":"9.42","q":"After delisting, public shareholders still holding shares can sell them to the promoters at the exit price within:","o":["One year","One month","Five years","Ten years"],"a":0,"w":"No minority shareholder can be forced to exit."},
 {"id":"9.43","q":"As per the SEBI delisting regulations cited in the book, a company that delisted voluntarily can apply for relisting after:","o":["Five years","One year","Ten years","Three years"],"a":0,"w":"After a compulsory delisting, the wait is ten years."},
 {"id":"9.44","q":"In a share swap during an acquisition:","o":["The acquirer pays with its own shares, so both companies must be valued to set a fair swap ratio","The acquirer pays only in cash","Shareholders swap shares for bonds","The target buys back its own shares"],"a":0,"w":"Swap simply means exchange."},
]

CASES = [
 {"id":"C17","title":"Meghna's corporate action year","text":"Meghna holds 600 shares of Sunita Steel, face value Rs 10, trading at Rs 900. During the year the company: (1) announces a 1:2 bonus issue; (2) later announces a stock split of 1:2; (3) finally offers rights in the ratio 1-for-6 at a discount to market price.",
  "qs":[
   {"q":"How many shares does Meghna hold after the bonus issue?","o":["900","1,200","800","300"],"a":0,"w":"1 bonus share for every 2 held: 600 &divide; 2 = 300 new. Total 900."},
   {"q":"Ignoring market movements, what is the theoretical price after the bonus?","o":["Rs 600","Rs 450","Rs 900","Rs 300"],"a":0,"w":"Value stays 600 &times; 900 = 5,40,000. Spread over 900 shares: Rs 600."},
   {"q":"After the 1:2 split, what are Meghna's shares and face value?","o":["1,800 shares of Rs 5","900 shares of Rs 20","1,800 shares of Rs 10","450 shares of Rs 5"],"a":0,"w":"Each share becomes 2 and face value halves: 900 &times; 2 = 1,800 shares of Rs 5."},
   {"q":"Meghna does not want to invest more in the rights issue. Which statement is correct?","o":["She can renounce her rights to someone else; if she does nothing, her ownership share is diluted","She must subscribe, as rights are compulsory","Her ownership share is unaffected whatever she does","She will receive the rights shares free"],"a":0,"w":"Subscribing is a choice. Dilution hits only those who do not take up their rights."},
  ]},
 {"id":"C18","title":"Orion Pharma wants to leave the exchange","text":"Orion Pharma's promoters hold 78% of its shares. They plan to delist voluntarily. Orion has spare cash and also considers a buyback first. Orion had once been delisted compulsorily years ago and later relisted.",
  "qs":[
   {"q":"Which method must the promoters use to acquire public shares for voluntary delisting?","o":["Reverse book building with a floor price","A bonus issue","A rights issue at a discount","Open market purchase only"],"a":0,"w":"Shareholders bid the price at which they will sell, above the promoters' floor price."},
   {"q":"Under the book's conditions, when can the delisting succeed?","o":["Only if promoter holding crosses 90% and at least 25% of public shareholders participate","As soon as promoter holding crosses 75%","Whenever SEBI approves, whatever the holding","Only if all public shareholders sell"],"a":0,"w":"Both conditions apply. No minority shareholder can be forced to exit."},
   {"q":"If Orion does a buyback first, which statement is correct?","o":["It can use only reserves and surplus, and the shares bought back are extinguished","It can borrow to fund it and keep the shares as treasury stock","It needs only a board resolution","It increases the number of shares outstanding"],"a":0,"w":"A special resolution with the time frame and maximum price is also needed."},
   {"q":"After Orion's earlier compulsory delisting, how long did it have to wait to apply for relisting, as per the book?","o":["10 years","5 years","1 year","3 years"],"a":0,"w":"5 years after voluntary delisting, 10 years after compulsory delisting."},
  ]},
]

DATA = {"id":"ch09","short":"Ch9","title":"Chapter 9: Corporate actions","cards":CARDS,"mcqs":MCQS,"cases":CASES}
