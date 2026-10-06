# Chapter 15 notes. Pattern diagrams are drawn in code (inline SVG) from the book's definitions.
UP = "fill:var(--teal);stroke:var(--teal)"
DN = "fill:var(--brick);stroke:var(--brick)"
LINE = "stroke:var(--ink);stroke-width:1.5"
GUIDE = "stroke:var(--indigo);stroke-width:2;stroke-dasharray:6 4;fill:none"
PRICE = "stroke:var(--ink);stroke-width:2;fill:none"


def candles(data, mark=None, W=300, H=170):
    """data: list of (open, high, low, close). mark: (first, last) index of the pattern candles to highlight."""
    lo = min(d[2] for d in data); hi = max(d[1] for d in data)
    pad = 12
    y = lambda v: pad + (hi - v) / (hi - lo) * (H - 2 * pad)
    n = len(data); step = W / n; bw = step * 0.5
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-hidden="true" style="max-width:340px;display:block;margin:0 auto 8px">']
    if mark:
        x0 = mark[0] * step + step * 0.1; x1 = (mark[1] + 1) * step - step * 0.1
        out.append(f'<rect x="{x0:.1f}" y="2" width="{x1 - x0:.1f}" height="{H - 4}" rx="8" style="fill:var(--indigo-soft);stroke:var(--indigo);stroke-dasharray:4 3"/>')
    for i, (o, h, l, c) in enumerate(data):
        cx = i * step + step / 2
        st = UP if c >= o else DN
        out.append(f'<line x1="{cx:.1f}" y1="{y(h):.1f}" x2="{cx:.1f}" y2="{y(l):.1f}" style="{st};stroke-width:2"/>')
        top, bot = y(max(o, c)), y(min(o, c))
        out.append(f'<rect x="{cx - bw / 2:.1f}" y="{top:.1f}" width="{bw:.1f}" height="{max(bot - top, 2):.1f}" style="{st}"/>')
    out.append("</svg>")
    return "".join(out)


def sketch(lines, W=300, H=170):
    """lines: list of (style, points[(x,y)...]) on a 300 x 170 canvas."""
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-hidden="true" style="max-width:340px;display:block;margin:0 auto 8px">']
    for st, pts in lines:
        p = " ".join(f"{x},{y}" for x, y in pts)
        out.append(f'<polyline points="{p}" style="{st}"/>')
    out.append("</svg>")
    return "".join(out)


HANGING = candles([(30, 34, 29, 33), (33, 37, 32, 36), (36, 40, 35, 39), (39.5, 40, 33, 39), (38.5, 39, 34, 34.5)], mark=(3, 4))
HAMMER = candles([(50, 51, 46, 47), (47, 48, 43, 44), (44, 45, 40, 41), (39.5, 41, 34, 40.5), (41, 45, 40.5, 44.5)], mark=(3, 4))
BULL_ENG = candles([(50, 51, 46, 47), (47, 48, 44, 45), (45, 46, 42, 43), (43, 44, 40, 41), (41, 41.5, 39, 39.5), (39, 44, 38.5, 43.5)], mark=(4, 5))
BEAR_ENG = candles([(30, 34, 29, 33), (33, 36, 32, 35), (35, 38, 34, 37), (37, 38.5, 36.5, 38), (38.5, 39, 33, 33.5)], mark=(3, 4))
DARK = candles([(30, 33, 29, 32), (32, 35, 31, 34), (34, 40, 33.5, 39.5), (41, 41.5, 35.5, 36)], mark=(2, 3))
PIERCE = candles([(50, 51, 46, 47), (47, 48, 44, 45), (45, 45.5, 38.5, 39), (37, 43.5, 36.5, 43)], mark=(2, 3))
MORNING = candles([(50, 51, 46, 47), (47, 47.5, 40, 40.5), (39, 40, 37, 38.5), (39.5, 46.5, 39, 46)], mark=(1, 3))
EVENING = candles([(30, 33, 29, 32.5), (32.5, 40, 32, 39.5), (40.5, 42, 39.8, 41), (40, 40.5, 35.5, 36)], mark=(1, 3))

SYM_TRI = sketch([(GUIDE, [(20, 30), (210, 80)]), (GUIDE, [(20, 140), (210, 95)]),
                  (PRICE, [(20, 135), (50, 40), (85, 125), (120, 60), (150, 110), (180, 75), (205, 98), (240, 40), (280, 15)])])
ASC_TRI = sketch([(GUIDE, [(20, 50), (220, 50)]), (GUIDE, [(20, 150), (220, 60)]),
                  (PRICE, [(20, 145), (60, 50), (95, 125), (135, 50), (165, 100), (200, 50), (215, 70), (250, 30), (285, 10)])])
DESC_TRI = sketch([(GUIDE, [(20, 20), (220, 115)]), (GUIDE, [(20, 125), (220, 125)]),
                   (PRICE, [(20, 25), (60, 125), (95, 45), (135, 125), (165, 80), (200, 125), (215, 110), (250, 145), (285, 162)])])
FLAG = sketch([(PRICE, [(20, 160), (40, 150), (90, 40)]), (GUIDE, [(90, 35), (180, 60)]), (GUIDE, [(95, 75), (180, 100)]),
               (PRICE, [(90, 40), (110, 70), (125, 50), (145, 85), (160, 60), (175, 95), (200, 45), (240, 15)])])
PENNANT = sketch([(PRICE, [(20, 160), (40, 150), (90, 40)]), (GUIDE, [(90, 35), (180, 65)]), (GUIDE, [(95, 100), (180, 75)]),
                  (PRICE, [(90, 40), (110, 95), (130, 50), (150, 85), (165, 62), (178, 78), (210, 35), (250, 10)])])
SUPRES = sketch([(GUIDE, [(10, 40), (300, 40)]), (GUIDE, [(10, 130), (190, 130)]),
                 (PRICE, [(10, 120), (40, 45), (70, 128), (100, 45), (130, 128), (160, 45), (190, 125), (220, 30), (250, 20), (270, 38), (300, 12)])])
CHANNEL = sketch([(GUIDE, [(10, 110), (290, 20)]), (GUIDE, [(10, 160), (290, 70)]),
                  (PRICE, [(10, 155), (50, 97), (90, 133), (130, 72), (170, 108), (210, 46), (250, 82), (290, 22)])])

LEARN = r"""
<div class="wrap">
<header class="hero">
<div class="kicker">Chapter 15 of 15</div>
<h1>Technical analysis</h1>
<div class="meta"><span class="pill">Worth <b>15 marks</b> of 100</span><span class="pill">Book pages 295 to 327</span><span class="pill">About 90 minutes</span></div>
<p class="oneline">Read the market from its own record of <span class="k">price and volume</span>: the trend, the <span class="k">patterns</span> that signal a turn, and the <span class="k">indicators</span> that confirm it.</p>
</header>

<figure class="fig" id="fig-map"><figcaption>Chapter map<span>Nine parts. The highest-weighted chapter: learn the patterns and indicator rules exactly. Tap to jump.</span></figcaption>
<div class="map">
<a href="#s1"><b>15.1</b><span>What technical analysis is</span><small>Five assumptions; versus fundamental</small></a>
<a href="#s2"><b>15.2</b><span>Chart types</span><small>Line, bar, candlestick, P&amp;F, Renko, Heikin-Ashi</small></a>
<a href="#s3"><b>15.3 and 15.4</b><span>Dow Theory and trends</span><small>Six tenets; primary, secondary, tertiary</small></a>
<a href="#s5"><b>15.5</b><span>Reversal patterns</span><small>Eight candlestick patterns</small></a>
<a href="#s6"><b>15.6</b><span>Consolidation patterns</span><small>Triangles, flags, pennants</small></a>
<a href="#s7"><b>15.7 and 15.8</b><span>Support, resistance, trendlines</span><small>Floors, ceilings, channels</small></a>
<a href="#s9"><b>15.9</b><span>Indicators</span><small>MA, MACD, RSI, ADX, RSC, OBV</small></a>
</div></figure>

<div class="col">
<section class="sec" id="s1"><span class="secno">15.1</span><h2>What technical analysis is</h2>
<p><span class="k">Technical analysis</span> evaluates securities from statistics of trading activity, mainly <b>price and volume</b>. Unlike fundamental analysis, it assumes all relevant information is <b>already in the price</b>. It is used across equities, currencies, commodities and crypto, especially for <b>short to medium term</b> trading. Chapter 4 (4.3) gave a first look.</p>
</div>

<figure class="fig" id="fig-assume"><figcaption>Five core assumptions</figcaption>
<div class="grid g3">
<div class="box hl"><span class="tag">1</span><h4>Price discounts everything</h4><p>Economic, political and psychological information is already in the price. Analysts look only at price and volume.</p></div>
<div class="box hl"><span class="tag">2</span><h4>Price moves in trends</h4><p>Up, down or sideways. An established trend is more likely to continue than reverse.</p></div>
<div class="box hl"><span class="tag">3</span><h4>History repeats itself</h4><p>Behaviour is cyclical and driven by psychology; patterns recur.</p></div>
<div class="box hl"><span class="tag">4</span><h4>Predictable, to a degree</h4><p>Patterns give probabilities, not certainty. It is about managing risk, not guaranteeing outcomes.</p></div>
<div class="box hl"><span class="tag">5</span><h4>Volume confirms price</h4><p>High volume on breakouts or reversals adds credibility.</p></div>
</div></figure>

<figure class="fig" id="fig-tavsfa"><figcaption>Technical versus fundamental analysis</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th></th><th>Technical</th><th>Fundamental</th></tr></thead>
<tbody>
<tr><th>Focus</th><td>Price action and market behaviour</td><td>Intrinsic value of the asset</td></tr>
<tr><th>Data</th><td>Historical price and volume</td><td>Financial statements, economic reports, industry publications</td></tr>
<tr><th>Horizon</th><td>Short and medium term trading</td><td>Long-term investment</td></tr>
<tr><th>Tools</th><td>Chart patterns; RSI, moving averages, MACD, OBV</td><td>Cash flow statements, DCF, SWOT, ratio analysis</td></tr>
<tr><th>Assumption</th><td>Price captures all information; trends continue</td><td>Prices can deviate from intrinsic value</td></tr>
<tr><th>Objective</th><td>Forecast price moves and trading opportunities</td><td>Find undervalued or overvalued assets</td></tr>
<tr><th>Used by</th><td>Traders, chartists, speculators, short-term investors</td><td>Fund and portfolio managers, value and long-term investors</td></tr>
</tbody></table></div></figure>

<div class="col">
<section class="sec" id="s2"><span class="secno">15.2</span><h2>Chart types</h2>
</div>

<figure class="fig" id="fig-charts"><figcaption>Six chart types</figcaption>
<div class="grid g3">
<div class="box"><span class="tag">Line</span><p>Closing prices joined as a line. Quick trend view, long-term perspective. Ignores open, high and low.</p></div>
<div class="box"><span class="tag">Bar (OHLC)</span><p>Open, high, low, close for each period. Detailed price action and volatility; shows range and direction.</p></div>
<div class="box"><span class="tag">Candlestick</span><p>Like a bar chart but clearer, with coloured "candles". Best for patterns such as doji, hammer, engulfing.</p></div>
<div class="box"><span class="tag">Point and figure</span><p>Price moves only; <b>ignores time and volume</b>. Breakouts and support and resistance; filters noise; long-term trends.</p></div>
<div class="box"><span class="tag">Renko</span><p>Fixed price moves ("bricks"), not time intervals. Trend clarity, momentum; smooths minor moves; suits trailing stops.</p></div>
<div class="box"><span class="tag">Heikin-Ashi</span><p>Adjusted candles that <b>average</b> price data to cut noise. Trend following; keeps traders in longer by filtering whipsaws.</p></div>
</div></figure>

<div class="col">
<section class="sec" id="s3"><span class="secno">15.3</span><h2>Dow Theory</h2>
<p>Developed by <b>Charles Dow</b> through editorials between <span class="num">1900 and 1902</span>, and organised into a formal theory after his death by <b>William Hamilton</b> and <b>Robert Rhea</b>. Still a foundation of technical analysis.</p>
</div>

<figure class="fig" id="fig-dow"><figcaption>The six tenets of Dow Theory</figcaption>
<div class="grid g3">
<div class="box"><span class="tag">1</span><h4>The market discounts everything</h4><p>Aligns with the Efficient Market Hypothesis.</p></div>
<div class="box"><span class="tag">2</span><h4>The market has three trends</h4><p>Primary (long term), secondary (weeks to months), tertiary (days to weeks).</p></div>
<div class="box"><span class="tag">3</span><h4>Primary trends have three phases</h4><p>Accumulation (smart money enters quietly), public participation, distribution (smart money exits). Mirrors Wyckoff's cycle.</p></div>
<div class="box"><span class="tag">4</span><h4>Indices must confirm each other</h4><p>Major indices should move the same way, for example Nifty and Sensex.</p></div>
<div class="box"><span class="tag">5</span><h4>Volume confirms the trend</h4><p>Volume should rise in the direction of the primary trend.</p></div>
<div class="box"><span class="tag">6</span><h4>Trends persist until a clear reversal</h4><p>The basis of trend following, trailing stops and moving average crossovers.</p></div>
</div></figure>

<div class="col">
<div class="trap">Dow Theory has <b>three</b> trends, not four, and <b>six</b> tenets. The book's sample question offers "the market has four trends" as the false tenet.</div>

<h3 id="s4">15.4 Understanding market trends</h3>
</div>

<figure class="fig" id="fig-trends"><figcaption>Primary, secondary, tertiary</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th></th><th>Primary</th><th>Secondary</th><th>Tertiary</th></tr></thead>
<tbody>
<tr><th>What</th><td>Dominant, long-term direction</td><td>Correction or rally against the primary trend. Lets the market digest gains or losses, shake out weak hands and reset overbought or oversold levels</td><td>Short-term moves within the larger trend</td></tr>
<tr><th>Length</th><td>Typically one year or more</td><td>About 3 weeks to 3 months (can vary)</td><td>Usually under 3 weeks (some say up to 6)</td></tr>
<tr><th>Types or traits</th><td>Bull (confidence, expansion), bear (fear, contraction), sideways (indecision)</td><td>Bull market <b>correction</b> (often 10% to 20%, a "pullback"); bear market <b>rally</b> ("relief rally"). Retraces <b>1/3 to 2/3</b> of the prior move (Dow Theory). Volume usually lower</td><td>Volatile, news-driven, reverses often; unreliable for long-term forecasts</td></tr>
<tr><th>Drivers</th><td>Economic cycles, monetary and fiscal policy, geopolitics, investor psychology</td><td>Data releases, central bank shifts, geopolitics, earnings surprises, technical exhaustion</td><td>Sentiment, news, technical triggers</td></tr>
<tr><th>Tools</th><td>50 or 100-day moving averages, trendlines, MACD, higher highs and lows</td><td>Fibonacci retracement (38.2%, 50%, 61.8%), trendlines, 50 DMA, volume, RSI or stochastic</td><td>5, 10 or 20-day EMAs, RSI, stochastic, candlestick patterns, pivots</td></tr>
<tr><th>Use</th><td>Asset allocation, avoiding counter-trend trades, riding the trend</td><td>Buying dips in uptrends, selling rallies in downtrends, swing trading</td><td>Fine-tuning entries, exits and tight stops. Building blocks of flags, pennants and wedges</td></tr>
</tbody></table></div></figure>

<div class="col">
<div class="why"><b>The book's example</b>Nifty 50, 2020 to 2021: a bullish primary trend after the COVID crash; a secondary correction of about 7% in September to October 2020 on global risk-off sentiment; then new highs by early 2021.</div>
<div class="analogy">The primary trend is the tide, the secondary trend is the waves, and the tertiary trend is the ripples. A ripple against the tide does not turn it.</div>
<p>Tertiary trends carry risks: noise in choppy markets, <b>whipsaws</b> (false breakouts), and <b>overtrading</b>, which raises costs and risk.</p>
</section>

<section class="sec" id="s5"><span class="secno">15.5</span><h2>Reversal patterns (candlesticks)</h2>
<p>Each candle shows open, high, low and close. The <b>real body</b> is the gap between open and close; the thin lines above and below are the <b>shadows</b> (wicks). Below, green candles closed higher and red candles closed lower. The highlighted candles form the pattern.</p>
</div>

<figure class="fig" id="fig-candles1"><figcaption>Single-candle reversals: hanging man and hammer<span>Same shape, opposite meaning: it depends on what came before</span></figcaption>
<div class="grid g2">
<div class="box bd">""" + HANGING + r"""<span class="tag">Bearish, after an up move</span><h4>Hanging man</h4><ul><li>Small real body; long lower shadow at least <b>twice</b> the body; little or no upper shadow</li><li>Close can be above or below the open, but near it</li><li>The long lower shadow shows sellers took control for part of the session</li><li>Only a warning: the <b>next candle must close lower</b> to confirm. Traders act during or after confirmation</li></ul></div>
<div class="box gd">""" + HAMMER + r"""<span class="tag">Bullish, after a decline</span><h4>Hammer</h4><ul><li>Same shape as a hanging man, but after a price fall</li><li>Sellers could not push lower; buyers drove the price back near the open</li><li>Tail at least <b>twice</b> the body</li><li>Confirmation: price must start moving up. Trades are taken after confirmation</li></ul></div>
</div></figure>

<figure class="fig" id="fig-candles2"><figcaption>Engulfing patterns</figcaption>
<div class="grid g2">
<div class="box gd">""" + BULL_ENG + r"""<span class="tag">Bullish</span><h4>Bullish engulfing</h4><ul><li>A small red candle followed by a large green candle whose body <b>completely engulfs</b> the red body</li><li>More likely a reversal when preceded by <b>four or more</b> red candles</li><li>Look at the preceding candles too</li></ul></div>
<div class="box bd">""" + BEAR_ENG + r"""<span class="tag">Bearish</span><h4>Bearish engulfing</h4><ul><li>A red candle's body completely engulfs the previous green body</li><li>More significant after a price advance</li><li>Both candles should be relatively long; two tiny candles matter far less</li><li>Only the <b>real bodies</b> count. Ignore it in choppy markets</li></ul></div>
</div></figure>

<figure class="fig" id="fig-candles3"><figcaption>Dark cloud cover and piercing pattern<span>Two-candle patterns at the edges of a congestion area</span></figcaption>
<div class="grid g2">
<div class="box bd">""" + DARK + r"""<span class="tag">Bearish, near the top</span><h4>Dark cloud cover</h4><ul><li>Occurs near the <b>top</b> of a congestion area, in an uptrend</li><li>A green candle, then a <b>gap up</b> that turns into a red candle</li><li>The red candle closes <b>below the midpoint</b> of the green candle</li></ul></div>
<div class="box gd">""" + PIERCE + r"""<span class="tag">Bullish, near the bottom</span><h4>Piercing pattern</h4><ul><li>A <b>two-candlestick</b> pattern near the <b>bottom</b> of a congestion area</li><li>A red candle, then a green candle that opens with a significant <b>gap down</b></li><li>The green body covers <b>at least half</b> of the red candle</li></ul></div>
</div>
<p class="ptr" style="margin-top:8px">A congestion area is a price range where the market trades repeatedly, often for several weeks, before breaking out up or down.</p>
</figure>

<figure class="fig" id="fig-candles4"><figcaption>Star patterns<span>Three-candle reversals</span></figcaption>
<div class="grid g2">
<div class="box gd">""" + MORNING + r"""<span class="tag">Bullish</span><h4>Morning star</h4><ul><li>A tall red candle; a small red or green candle with a short body and long wicks; a tall green candle</li><li>The middle candle is indecision: bears give way to bulls</li><li>The third candle confirms the reversal and can mark a new uptrend</li></ul></div>
<div class="box bd">""" + EVENING + r"""<span class="tag">Bearish</span><h4>Evening star</h4><ul><li>A large green candle in an uptrend; a small-bodied candle (red or green) that closes above the first; a large red candle</li><li>The red candle opens below the middle candle and closes near the <b>centre of the first candle's body</b></li></ul></div>
</div></figure>

<div class="col">
<div class="trap">Count the candles. <b>One</b>: hanging man, hammer. <b>Two</b>: bullish and bearish engulfing, dark cloud cover, piercing. <b>Three</b>: morning star, evening star. Top or bottom: dark cloud cover forms near the <b>top</b> of a congestion area; piercing near the <b>bottom</b>.</div>
</section>

<section class="sec" id="s6"><span class="secno">15.6</span><h2>Consolidation patterns</h2>
<p>Pauses within a trend, usually followed by a breakout. Dashed lines are the trendlines drawn along the highs and lows.</p>
</div>

<figure class="fig" id="fig-triangles"><figcaption>Three triangles</figcaption>
<div class="grid g3">
<div class="box">""" + SYM_TRI + r"""<span class="tag">Either way</span><h4>Symmetrical triangle</h4><ul><li>Consolidation before a forced breakout or breakdown</li><li>Break above the upper line: new bullish trend. Below the lower line: new bearish trend</li><li>The book says it is also known as a wedge pattern</li></ul></div>
<div class="box gd">""" + ASC_TRI + r"""<span class="tag">Bullish continuation</span><h4>Ascending triangle</h4><ul><li><b>Higher lows</b> against the <b>same resistance</b> level; usually in an uptrend</li><li>Trendlines need at least two swing highs and lows</li><li>Long if price breaks above the top; short if it breaks below the lower line</li><li><b>Target:</b> height of the triangle at its thickest point, added to (or subtracted from) the breakout point</li></ul></div>
<div class="box bd">""" + DESC_TRI + r"""<span class="tag">Bearish continuation</span><h4>Descending triangle</h4><ul><li><b>Lower highs</b> and lows at the <b>same level</b>; usually in a downtrend</li><li>Bears gain control, pushing to the support line</li><li>A signal to go short to accelerate a breakdown</li></ul></div>
</div></figure>

<figure class="fig" id="fig-flags"><figcaption>Flags and pennants<span>Continuation patterns, traded the same way</span></figcaption>
<div class="grid g2">
<div class="box">""" + FLAG + r"""<span class="tag">Rectangle</span><h4>Flag</h4><p>After a sharp rally (the <b>flagpole</b>), price moves sideways or slightly lower in a small rectangle.</p></div>
<div class="box">""" + PENNANT + r"""<span class="tag">Small triangle</span><h4>Pennant</h4><p>Same idea, but the pause forms a small triangle. Traders buy when price breaks above the upper trendline.</p></div>
</div></figure>

<div class="col">
<section class="sec" id="s7"><span class="secno">15.7</span><h2>Support and resistance</h2>
</div>

<figure class="fig" id="fig-supres"><figcaption>Floor and ceiling<span>The lower line is support; the upper line is resistance. A break above resistance on volume is a breakout.</span></figcaption>
<div class="grid g2">
<div class="box">""" + SUPRES + r"""<h4>Definitions</h4><p><b>Support:</b> a level where a downtrend is expected to pause because of concentrated <b>demand</b>: a "floor".</p><p><b>Resistance:</b> a level where an uptrend is expected to pause because of concentrated <b>supply</b>: a "ceiling".</p></div>
<div class="box"><h4>Why they matter</h4><ul><li>Psychological anchors: traders remember past turning points</li><li>Buy and sell orders cluster near them</li><li>Help set stop-loss and take-profit levels</li><li>Breakouts or bounces confirm trend direction</li></ul><h4>Role reversal</h4><p>Broken support often becomes resistance, and vice versa: trapped traders exit at breakeven, sentiment shifts, institutions reposition.</p></div>
</div></figure>

<figure class="fig" id="fig-srtypes"><figcaption>Types of support and resistance</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Type</th><th>Description</th><th>Book's example</th></tr></thead>
<tbody>
<tr><th>Horizontal</th><td>Flat levels where price repeatedly reverses</td><td>A stock resisting around Rs 1,950</td></tr>
<tr><th>Trendline</th><td>Diagonal lines through higher lows (support) or lower highs (resistance)</td><td>Upward sloping support in a bull trend</td></tr>
<tr><th>Moving averages</th><td>Dynamic levels, for example the 50-day MA</td><td>Price bouncing off the 50 DMA</td></tr>
<tr><th>Fibonacci levels</th><td>From retracement ratios 23.6%, 38.2%, 61.8%</td><td>Stock retracing 23.6% from a swing high</td></tr>
<tr><th>Pivot points</th><td>From the previous period's high, low and close</td><td>Mostly used intraday</td></tr>
<tr><th>Psychological</th><td>Round numbers act as barriers</td><td>Nifty 25,000</td></tr>
</tbody></table></div></figure>

<div class="col">
<ul>
<li><b>Breakout:</b> price moves decisively beyond the level <b>with volume</b>. <b>False breakout:</b> a brief breach that quickly reverses, trapping traders. Volume and candlestick confirmation help tell them apart.</li>
<li><b>Strength of a level:</b> more touches, higher volume at the level, more time spent near it, and more recent levels all make it stronger.</li>
<li><b>Uses:</b> bounce trades (buy near support, sell near resistance), breakout trades, pullback entries on a retest, and stop-losses just below support or above resistance.</li>
<li><b>Limits:</b> levels are zones, not exact prices; drawing them is subjective; in strong trends they are respected less; news can override them.</li>
<li><b>Advanced ideas:</b> order blocks, liquidity pools (where stop orders cluster), VWAP and anchored VWAP.</li>
</ul>
<p class="ptr">Book's case notes: Nifty found strong support around 24,350 from May to September 2025; Reliance faced resistance around 1,300 from October 2021 to July 2023 before breaking out in January 2024.</p>

<h3 id="s8">15.8 Trendlines and channels</h3>
</div>

<figure class="fig" id="fig-channel"><figcaption>Trendlines and an ascending channel</figcaption>
<div class="grid g2">
<div class="box">""" + CHANNEL + r"""<h4>Channel</h4><p>Two <b>parallel</b> trendlines, one through highs and one through lows. Ascending (higher highs and lows) is bullish; descending is bearish; horizontal is range-bound. Its width reflects volatility. Trade within it (buy at support, sell at resistance); a break of either line is a breakout or breakdown, with a target projected from the channel width.</p></div>
<div class="box"><h4>Trendline rules</h4><ul><li>A straight line through two or more price points, extended forward as support or resistance</li><li>Upward through higher lows: bullish. Downward through lower highs: bearish. Sideways: range-bound</li><li>Needs at least <b>two</b> points; <b>three or more</b> make it more reliable</li><li>Use wicks or closes depending on the strategy; adjust as new data comes</li><li>Used for trend strength, entry and exit timing, and stop-losses</li></ul></div>
</div></figure>

<div class="col">
<div class="grid g2">
<div class="box gd"><h4>Validation</h4><p>Rising volume on breakouts; candlesticks (engulfing, hammer, shooting star) at the lines; RSI divergence or MACD crossovers near boundaries; lines visible on higher timeframes carry more weight.</p></div>
<div class="box bd"><h4>Common pitfalls</h4><p>Forcing lines to fit a bias; ignoring breakouts and not redrawing after invalidation; relying on lines without other confirmation.</p></div>
</div>
</section>

<section class="sec" id="s9"><span class="secno">15.9</span><h2>Technical indicators</h2>
<h3>15.9.1 Moving averages</h3>
<p>A smoothed line of average closing prices (daily, weekly or monthly). Rising MA: uptrend; falling: downtrend. MAs are <b>lagging</b> indicators but good for major trends. When monthly, weekly and daily MAs point the same way, the trend is likely to continue. Trading at or near a rising MA can be a good time to buy.</p>
</div>

<figure class="fig" id="fig-ema"><figcaption>The book's 13, 21 and 34 EMA combination<span>Periods from the Fibonacci series</span></figcaption>
<div class="grid g2">
<div class="box gd"><span class="tag">Uptrend</span><h4>Price &gt; 13 EMA &gt; 21 EMA &gt; 34 EMA</h4><p>In a bull market price usually finds support around the <b>34 EMA</b>. All three rising and spreading apart: a strong bull market.</p></div>
<div class="box bd"><span class="tag">Downtrend</span><h4>Price &lt; 13 EMA &lt; 21 EMA &lt; 34 EMA</h4><p>Price tends to meet resistance around the <b>34 EMA</b>. All three falling and spreading apart: strong selling pressure.</p></div>
</div></figure>

<div class="col">
<h3>15.9.2 MACD</h3>
<div class="formula" style="font-family:var(--head);font-weight:700;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.55rem .8rem;margin:.7rem 0">Default MACD line = difference between the 26 EMA and the 12 EMA. Slow line = 9 EMA of the default line.</div>
<ul>
<li>Shows shifts in <b>momentum</b> and can warn early of a trend change. At times it <b>leads</b> price.</li>
<li><b>Buy</b> when both lines are rising and the fast line crosses above the slow line; also when the fast line, already above, turns up again after nearly touching the slow line.</li>
<li><b>Divergence:</b> price makes a higher high but MACD a lower high: losing upward momentum. Price makes a new low but MACD a higher low: losing downward momentum, likely to bottom out.</li>
<li>The <b>zero line</b> separates confirmed bull and bear markets, but a crossover of zero <b>should not be used for trading</b>.</li>
<li>Steep MACD: a powerful move; shallow: lack of power. A bulge of the fast line far above the slow line: a buying climax, possibly followed by a sideways market or mild correction.</li>
<li>MACD can go flat or turn without a trend reversal; it shows momentum, not price, so use it with other indicators and price action.</li>
<li>A double top or bottom in MACD suggests a likely reversal. Avoid stocks whose weekly or monthly MACD is clearly trending down.</li>
</ul>
</div>

<figure class="fig" id="fig-rsi"><figcaption>RSI: a scale from 0 to 100<span>Relative Strength Index</span></figcaption>
<div class="stack"><div style="flex:30;background:var(--teal)">0 to 30: oversold</div><div style="flex:40;background:var(--muted)">30 to 70</div><div style="flex:30;background:var(--brick)">70 to 100: overbought</div></div>
<div class="grid g2" style="margin-top:12px">
<div class="box"><h4>Reading RSI</h4><ul><li>Measures speed and size of recent price changes; can be a <b>lead</b> indicator</li><li>Works well in a <b>trading range</b></li><li>Bull market: rarely falls below <b>44 to 45</b>. Bear market: rarely rises above <b>50 to 55</b></li><li>Can stay overbought (or oversold) for long in a strong trend</li></ul></div>
<div class="box"><h4>Divergence</h4><ul><li><b>Bullish divergence:</b> in an oversold market the stock makes a new low but RSI does not. An early buy signal</li><li><b>Bearish divergence:</b> in an overbought market the stock makes a new high but RSI does not. An early sell signal</li></ul></div>
</div></figure>

<div class="col">
<h3>15.9.4 ADX (Average Directional Index)</h3>
<ul>
<li>Measures the <b>strength</b> of a trend, <b>not its direction</b>. Values from 0 to 100; default setting <b>14</b> bars.</li>
<li>Below <b>25</b>: weak or no trend. A rising ADX, especially above 25: a strong trend.</li>
<li>Plotted with <b>+DMI</b> and <b>&minus;DMI</b>. Buy when +DMI crosses above &minus;DMI and ADX is rising; sell when +DMI crosses below &minus;DMI and ADX is rising. Ignore crossovers when ADX is weak.</li>
</ul>
<h3>15.9.5 RSC (Relative Strength Comparative)</h3>
<ul>
<li>Also called the Relative Strength Indicator or Price Relative Indicator. A <b>ratio chart</b> comparing one security with another, such as a stock against the Nifty 50 or its sector.</li>
<li>Use about a <b>5 to 6 year</b> period. Normalised to <b>100</b>: above 100 means outperforming the benchmark; below 100, underperforming.</li>
<li>A good buy: RSC below 100 for a long time, then turning up and crossing 100.</li>
</ul>
<h3>15.9.6 OBV (On Balance Volume)</h3>
<ul>
<li>Add the day's volume to a running total if the close is higher than yesterday's; subtract it if lower.</li>
<li>OBV should rise with prices and fall with them. In a divergence, volume often <b>leads</b> price, warning of a reversal.</li>
<li>Read OBV 1 (the line) with OBV 20 (its 20-period average). Buy when OBV 1 crosses above a rising OBV 20; sell when it crosses below a falling OBV 20.</li>
<li>A pronounced weakening of OBV on long-term charts can mean <b>smart money is quietly exiting</b>. A higher high in price without a higher OBV: buying pressure is fading.</li>
<li>The book's example: Maharashtra Scooters' weekly OBV turned up from May 2023, and the stock delivered about 4 times from there.</li>
</ul>
</div>

<figure class="fig" id="fig-indicators"><figcaption>Six indicators at a glance</figcaption>
<div class="scroll"><table class="cmp">
<thead><tr><th>Indicator</th><th>Measures</th><th>Key numbers and signals (book)</th></tr></thead>
<tbody>
<tr><th>Moving averages</th><td>Trend (lagging)</td><td>13, 21, 34 EMA; price above all three in an uptrend</td></tr>
<tr><th>MACD</th><td>Momentum</td><td>26 EMA minus 12 EMA; slow line 9 EMA; do not trade zero-line crossovers</td></tr>
<tr><th>RSI</th><td>Speed and size of price changes</td><td>0 to 100; above 70 overbought, below 30 oversold; best in a trading range</td></tr>
<tr><th>ADX</th><td>Trend strength, not direction</td><td>14 bars; below 25 weak; use with +DMI and &minus;DMI</td></tr>
<tr><th>RSC</th><td>Performance versus a benchmark</td><td>Normalised to 100; above 100 outperforming; 5 to 6 years of data</td></tr>
<tr><th>OBV</th><td>Volume flow</td><td>Read with its 20-period average; divergence warns of reversal</td></tr>
</tbody></table></div></figure>

<div class="col">
<div class="why"><b>The book's closing view</b>Technical analysis is a guide, not a guarantee. It works best with discipline, risk management, an understanding of market context, and combined with macroeconomic and sentiment analysis. Critics call it self-fulfilling, yet its wide use keeps it relevant.</div>
</section>

<section class="sec" id="traps"><h2>All exam traps in this chapter</h2>
<ol class="traplist">
<li>Technical analysis uses price and volume and assumes price discounts everything.</li>
<li>Point and figure ignores time and volume. Renko uses fixed price bricks. Heikin-Ashi averages prices.</li>
<li>Line charts use closing prices only; bar charts show OHLC.</li>
<li>Dow Theory: Charles Dow, editorials 1900 to 1902; formalised by Hamilton and Rhea; six tenets; three trends.</li>
<li>Primary trend phases: accumulation, public participation, distribution.</li>
<li>Indices must confirm each other; volume should rise in the primary trend's direction.</li>
<li>Secondary trends last about 3 weeks to 3 months and retrace 1/3 to 2/3 of the primary move.</li>
<li>Tertiary trends: usually under 3 weeks.</li>
<li>Hanging man: bearish, after an up move, needs a lower close next. Hammer: bullish, after a decline. Shadow at least twice the body.</li>
<li>Bullish engulfing: stronger after four or more red candles. Only real bodies count.</li>
<li>Dark cloud cover: top of congestion; red closes below the green's midpoint. Piercing: bottom; green covers at least half the red.</li>
<li>Morning star bullish, evening star bearish: three candles each.</li>
<li>Ascending triangle: flat top, higher lows, bullish continuation. Descending: flat bottom, lower highs, bearish continuation.</li>
<li>Triangle target: height at its thickest point, from the breakout point.</li>
<li>Flag: small rectangle after a flagpole; pennant: small triangle.</li>
<li>Support is demand (a floor); resistance is supply (a ceiling). Broken support becomes resistance.</li>
<li>A trendline needs at least two points; three or more make it more reliable.</li>
<li>Moving averages are lagging. 13, 21, 34 EMA; price supported near the 34 EMA in a bull market.</li>
<li>MACD line = 26 EMA minus 12 EMA; slow line = 9 EMA of it. Do not trade zero-line crossovers.</li>
<li>RSI above 70 overbought, below 30 oversold. Stock new low, RSI not: bullish divergence.</li>
<li>RSI rarely below 44 to 45 in a bull market, rarely above 50 to 55 in a bear market.</li>
<li>ADX measures strength, not direction; below 25 weak; default 14.</li>
<li>RSC above 100: outperforming the benchmark.</li>
<li>OBV adds volume on up days and subtracts on down days; read with its 20-period average.</li>
</ol>
</section>

<section class="sec" id="talk"><h2>For the group discussion</h2>
<ol class="talk">
<li>Open a candlestick chart of a stock you know. Can you find a hammer or an engulfing pattern? Did the next candle confirm it?</li>
<li>Is technical analysis self-fulfilling? Does that make it more or less useful?</li>
<li>Where would you place a stop-loss for a breakout from an ascending triangle? Why?</li>
<li>RSI says overbought but ADX says a strong trend. Which do you trust, and why?</li>
<li>How would you combine one fundamental test from Chapter 8 with one technical signal from this chapter?</li>
</ol>
</section>
</div>

<footer>Notes built from the NISM Series XV workbook (February 2026 version). Study aid only.</footer>
</div>
"""
