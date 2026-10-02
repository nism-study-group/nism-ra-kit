// Layout engine for tldraw study boards.
// Runs inside a live tldraw editor (tldraw.com exposes window.editor), so every text
// block is measured by tldraw itself. Called from board_*.py through Playwright with a
// spec object; returns a .tldr document. Block types are documented in place().
async (spec) => {
	const editor = window.editor
	const S = spec.style
	const FW = spec.frameWidth
	const PAD = 56
	const CW = FW - 2 * PAD
	const GAP = 26
	const COL_GAP = 24
	const SAFE = 22 // extra height on measured boxes, in case a viewer's fonts render a little larger

	let n = 0
	const sid = () => `shape:${spec.slug}-${(n++).toString(36)}`

	// Mini markup to tldraw rich text: **bold**, ==highlight==, _italic_, "- " bullets, \n paragraphs.
	function inline(s) {
		const out = []
		const re = /(\*\*[^*]+\*\*|==[^=]+==|_[^_]+_)/g
		let last = 0
		let m
		while ((m = re.exec(s))) {
			if (m.index > last) out.push({ type: 'text', text: s.slice(last, m.index) })
			const tok = m[0]
			const mark = tok.startsWith('**') ? 'bold' : tok.startsWith('==') ? 'highlight' : 'italic'
			const cut = mark === 'italic' ? 1 : 2
			out.push({ type: 'text', text: tok.slice(cut, -cut), marks: [{ type: mark }] })
			last = re.lastIndex
		}
		if (last < s.length) out.push({ type: 'text', text: s.slice(last) })
		return out
	}
	function rt(src) {
		const content = []
		let list = null
		for (const line of String(src).split('\n')) {
			if (line.startsWith('- ')) {
				if (!list) content.push((list = { type: 'bulletList', content: [] }))
				list.content.push({ type: 'listItem', content: [{ type: 'paragraph', content: inline(line.slice(2)) }] })
			} else {
				list = null
				content.push(line ? { type: 'paragraph', content: inline(line) } : { type: 'paragraph' })
			}
		}
		return { type: 'doc', content }
	}

	const noOp = () => {}
	const gapFor = (labels, min) => Math.max(min, ...(labels || []).map((l) => 110 + 14 * String(l || '').length))
	const pageH = (id) => editor.getShapePageBounds(id).h

	// ---- primitives. x, y are in the parent frame's space. Each returns { h, stretch, ids }.
	function geo(ctx, x, y, w, text, o = {}) {
		const id = sid()
		editor.createShape({
			id, type: 'geo', parentId: ctx.parent, x, y,
			props: {
				geo: o.geo || 'rectangle', w, h: o.h || 44,
				color: o.color || 'blue', fill: o.fill || 'solid', dash: o.dash || S.dash,
				size: o.size || S.bodySize, font: o.font || S.bodyFont,
				align: o.align || 'start', verticalAlign: o.valign || 'start',
				labelColor: o.labelColor || 'black', richText: rt(text),
			},
		})
		const s = editor.getShape(id)
		const h = s.props.h + s.props.growY + (s.props.growY ? SAFE : 0)
		editor.updateShape({ id, type: 'geo', props: { h, growY: 0 } })
		return { h, ids: [id], stretch: (H) => editor.updateShape({ id, type: 'geo', props: { h: H, growY: 0 } }) }
	}
	function text(ctx, x, y, w, src, o = {}) {
		const id = sid()
		editor.createShape({
			id, type: 'text', parentId: ctx.parent, x, y,
			props: {
				w: w / (o.scale || 1), autoSize: false, scale: o.scale || 1,
				size: o.size || S.bodySize, font: o.font || S.bodyFont, color: o.color || 'black',
				textAlign: o.align || 'start', richText: rt(src),
			},
		})
		return { h: pageH(id), ids: [id], stretch: noOp }
	}
	function note(ctx, x, y, w, src, color) {
		const id = sid()
		editor.createShape({
			id, type: 'note', parentId: ctx.parent, x, y,
			props: {
				color, size: 's', font: S.noteFont, align: 'start', verticalAlign: 'start',
				scale: w / 200, richText: rt(src),
			},
		})
		return { h: pageH(id), ids: [id], stretch: noOp }
	}
	function arrow(ctx, fromId, toId, label, o = {}) {
		const id = sid()
		const a = editor.getShapePageBounds(fromId).center
		const b = editor.getShapePageBounds(toId).center
		editor.createShape({
			id, type: 'arrow', parentId: ctx.parent, x: a.x - ctx.ox, y: a.y - ctx.oy,
			props: {
				start: { x: 0, y: 0 }, end: { x: b.x - a.x, y: b.y - a.y },
				color: o.color || 'grey', size: o.size || 'm', dash: S.dash, bend: o.bend || 0,
				arrowheadStart: 'none', arrowheadEnd: 'arrow', font: S.headFont, labelColor: 'black',
				richText: rt(label || ''),
			},
		})
		const bind = (terminal, target, anchor) => ({
			type: 'arrow', fromId: id, toId: target,
			props: { terminal, normalizedAnchor: anchor || { x: 0.5, y: 0.5 }, isExact: false, isPrecise: !!anchor, snap: 'none' },
		})
		editor.createBindings([bind('start', fromId, o.a), bind('end', toId, o.b)])
		return id
	}
	// Unbound straight arrow or line between two points (frame space).
	function freeArrow(ctx, x1, y1, x2, y2, o = {}) {
		editor.createShape({
			id: sid(), type: 'arrow', parentId: ctx.parent, x: x1, y: y1,
			props: {
				start: { x: 0, y: 0 }, end: { x: x2 - x1, y: y2 - y1 }, color: o.color || 'grey',
				size: o.size || 's', dash: o.dash || 'solid', arrowheadEnd: o.head === false ? 'none' : 'arrow',
				arrowheadStart: 'none', font: S.bodyFont, richText: rt(o.label || ''),
			},
		})
	}
	function polyline(ctx, pts, o = {}) {
		const [x0, y0] = pts[0]
		const points = {}
		pts.forEach(([x, y], i) => {
			const k = 'a' + (i + 1)
			points[k] = { id: k, index: k, x: x - x0, y: y - y0 }
		})
		editor.createShape({
			id: sid(), type: 'line', parentId: ctx.parent, x: x0, y: y0,
			props: { color: o.color || 'black', dash: o.dash || 'solid', size: o.size || 'm', spline: 'line', points },
		})
	}

	const NOTE = {
		trap: ['orange', 'EXAM TRAP'],
		analogy: ['light-green', 'ANALOGY'],
		why: ['light-blue', null],
		remember: ['yellow', 'REMEMBER'],
		discuss: ['light-violet', null],
	}

	// ---- blocks
	function place(ctx, b, x, y, w) {
		switch (b.t) {
			case 'header': { // {no, title, sub}
				const badge = geo(ctx, x, y, 128, `**${b.no}**`, {
					geo: 'ellipse', h: 128, color: 'violet', fill: 'fill', labelColor: 'white',
					size: 'l', font: 'sans', align: 'middle', valign: 'middle', dash: 'solid',
				})
				const t = text(ctx, x + 160, y + 4, w - 160, b.title, { size: 'xl', font: S.headFont, scale: 1.2 })
				const s = text(ctx, x + 160, y + 12 + t.h, w - 160, b.sub, { size: 'm', color: 'grey' })
				return { h: Math.max(badge.h, t.h + s.h + 12) + 12, stretch: noOp }
			}
			case 'h': { // subheading, with a little extra space above
				const r = text(ctx, x, y + 14, w, b.text, { size: 'l', font: S.headFont, color: 'violet' })
				return { h: r.h + 14, stretch: noOp }
			}
			case 'p':
				return text(ctx, x, y, w, b.text, { size: b.size || S.bodySize, color: b.color })
			case 'card':
				return geo(ctx, x, y, w, b.text, b)
			case 'note': {
				const [color, head] = NOTE[b.kind]
				const nw = Math.min(w, b.w || S.noteWidth)
				return note(ctx, x, y, nw, head ? `**${head}**\n${b.text}` : b.text, color)
			}
			case 'stack': { // vertical stack of blocks
				let yy = y
				for (const it of b.items) yy += place(ctx, it, x, yy, w).h + (b.gap ?? GAP)
				return { h: yy - y - (b.gap ?? GAP), stretch: noOp }
			}
			case 'row': { // side by side. widths: px (>1) or fractions of what is left
				const gap = b.gap ?? COL_GAP
				const ws = b.widths || b.items.map(() => 1)
				const inner = w - gap * (b.items.length - 1)
				const fixed = ws.filter((v) => v > 1).reduce((s, v) => s + v, 0)
				const flex = ws.filter((v) => v <= 1).reduce((s, v) => s + v, 0)
				let xx = x
				const placed = b.items.map((it, i) => {
					const iw = ws[i] > 1 ? ws[i] : ((inner - fixed) * ws[i]) / flex
					const r = place(ctx, it, xx, y, iw)
					xx += iw + gap
					return r
				})
				const H = Math.max(...placed.map((r) => r.h))
				// cards match each other; a taller sticky note does not stretch them
				const Hs = Math.max(0, ...placed.filter((r) => r.stretch !== noOp).map((r) => r.h))
				if (b.equal !== false) placed.forEach((r) => r.stretch(Hs))
				return { h: H, stretch: noOp }
			}
			case 'grid': { // cards in equal columns, heights equalised per row
				const cols = b.cols
				const gap = b.gap ?? COL_GAP
				const cw = (w - gap * (cols - 1)) / cols
				let yy = y
				for (let i = 0; i < b.items.length; i += cols) {
					const rowItems = b.items.slice(i, i + cols)
					const placed = rowItems.map((it, j) => place(ctx, typeof it === 'string' ? { t: 'card', text: it, color: b.color } : { t: 'card', color: b.color, ...it }, x + j * (cw + gap), yy, cw))
					const H = Math.max(...placed.map((r) => r.h))
					if (b.equal !== false) placed.forEach((r) => r.stretch(H))
					yy += H + gap
				}
				return { h: yy - y - gap, stretch: noOp }
			}
			case 'notes': { // a wall of sticky notes
				const cols = b.cols
				const gap = b.gap ?? COL_GAP
				const nw = (w - gap * (cols - 1)) / cols
				let yy = y
				for (let i = 0; i < b.items.length; i += cols) {
					const hs = b.items.slice(i, i + cols).map((it, j) => {
						const [color, head] = NOTE[b.kind]
						const label = b.numbered ? `**${i + j + 1}.** ${it}` : head ? `**${head}**\n${it}` : it
						return note(ctx, x + j * (nw + gap), yy, nw, label, color).h
					})
					yy += Math.max(...hs) + gap
				}
				return { h: yy - y - gap, stretch: noOp }
			}
			case 'flow': { // boxes left to right joined by arrows
				const gap = b.gap ?? gapFor([...(b.labels || [])], 110)
				const k = b.items.length
				const bw = (w - gap * (k - 1)) / k
				const boxes = b.items.map((it, i) =>
					geo(ctx, x + i * (bw + gap), y, bw, it.text, { color: it.color || b.color || 'blue', ...it })
				)
				const H = Math.max(...boxes.map((r) => r.h))
				boxes.forEach((r) => r.stretch(H))
				for (let i = 0; i + 1 < k; i++) arrow(ctx, boxes[i].ids[0], boxes[i + 1].ids[0], b.labels?.[i] || '')
				let h = H
				if (b.back) { // curved return arrow under the row, from last box to first
					arrow(ctx, boxes[k - 1].ids[0], boxes[0].ids[0], b.back, { a: { x: 0.5, y: 1 }, b: { x: 0.5, y: 1 }, bend: -110, color: 'violet' })
					h += 150
				}
				return { h, stretch: noOp }
			}
			case 'table': { // tiles; first row is a header, first column is bold
				const gap = 8
				const fr = b.cols
				const tot = fr.reduce((s, v) => s + v, 0)
				const inner = w - gap * (fr.length - 1)
				const cws = fr.map((v) => (inner * v) / tot)
				let yy = y
				b.rows.forEach((cells, ri) => {
					let xx = x
					const placed = cells.map((c, ci) => {
						const head = ri === 0 || ci === 0
						const r = geo(ctx, xx, yy, cws[ci], head && c ? `**${c}**` : c, {
							dash: 'solid', fill: 'solid', color: ri === 0 ? 'violet' : ci === 0 ? 'blue' : 'grey', size: b.size || 's',
						})
						xx += cws[ci] + gap
						return r
					})
					const H = Math.max(...placed.map((r) => r.h))
					placed.forEach((r) => r.stretch(H))
					yy += H + gap
				})
				return { h: yy - y - gap, stretch: noOp }
			}
			case 'bars': { // proportional stacked bars, one per row, optional label column
				const lw = b.labelWidth ?? 280
				let yy = y
				for (const r of b.rows) {
					let hRow = b.barHeight || 64
					let bx = x
					let bwTotal = w
					if (r.label) {
						const t = text(ctx, x, yy + 6, lw - 20, r.label)
						hRow = Math.max(hRow, t.h)
						bx = x + lw
						bwTotal = w - lw
					}
					const segGap = 6
					const inner = bwTotal - segGap * (r.segs.length - 1)
					const tot = r.segs.reduce((s, g) => s + g.f, 0)
					const placed = r.segs.map((g) => {
						const sw = (inner * g.f) / tot
						const p = geo(ctx, bx, yy, sw, g.text, {
							h: b.barHeight || 64, color: g.color, fill: g.fill || 'solid', dash: 'solid',
							align: 'middle', valign: 'middle',
						})
						bx += sw + segGap
						return p
					})
					const H = Math.max(hRow, ...placed.map((p) => p.h))
					placed.forEach((p) => p.stretch(H))
					yy += H + 14
				}
				return { h: yy - y - 14, stretch: noOp }
			}
			case 'tree': { // nodes on a row/column grid, joined by labelled arrows
				const colGap = b.colGap ?? gapFor(b.edges.map((e) => e[2]), 120)
				const rowGap = b.rowGap ?? 110
				const inner = w - colGap * (b.cols.length - 1)
				const tot = b.cols.reduce((s, v) => s + v, 0)
				const cws = b.cols.map((v) => (inner * v) / tot)
				const cx = cws.map((_, i) => x + cws.slice(0, i).reduce((s, v) => s + v, 0) + colGap * i)
				const rows = Math.max(...b.nodes.map((nd) => nd.r)) + 1
				const made = {}
				let yy = y
				for (let r = 0; r < rows; r++) {
					const inRow = b.nodes.filter((nd) => nd.r === r)
					const placed = inRow.map((nd) => {
						const nw = nd.w || cws[nd.c]
						const g = geo(ctx, cx[nd.c] + (cws[nd.c] - nw) / 2, yy, nw, nd.text, {
							color: 'blue', ...nd, align: nd.geo ? 'middle' : 'start', valign: nd.geo ? 'middle' : 'start',
						})
						made[nd.id] = g
						return g
					})
					const H = Math.max(...placed.map((g) => g.h))
					// centre each node vertically in its row
					inRow.forEach((nd) => {
						const g = made[nd.id]
						editor.updateShape({ id: g.ids[0], type: 'geo', y: yy + (H - g.h) / 2 })
					})
					yy += H + rowGap
				}
				for (const [f, t, label] of b.edges) arrow(ctx, made[f].ids[0], made[t].ids[0], label, { color: 'violet' })
				return { h: yy - y - rowGap, stretch: noOp }
			}
			case 'payoff': { // call option profit and loss chart, strike K, premium P
				const { K, P, lo, hi } = b
				const top = 30, left = 110, bottom = 70, right = 30
				const H = b.height || 470
				const pw = w - left - right
				const ph = H - top - bottom
				const vmax = hi - K - P + 100
				const X = (s) => x + left + ((s - lo) / (hi - lo)) * pw
				const Y = (v) => y + top + ((vmax - v) / (2 * vmax)) * ph
				freeArrow(ctx, X(lo), Y(-vmax), X(lo), Y(vmax) - 10, { color: 'grey' })
				freeArrow(ctx, X(lo), Y(0), X(hi) + 20, Y(0), { color: 'grey' })
				polyline(ctx, [[X(K), Y(-vmax)], [X(K), Y(vmax)]], { color: 'grey', dash: 'dashed', size: 's' })
				polyline(ctx, [[X(lo), Y(-P)], [X(K), Y(-P)], [X(hi), Y(hi - K - P)]], { color: 'green', size: 'l' })
				polyline(ctx, [[X(lo), Y(P)], [X(K), Y(P)], [X(hi), Y(-(hi - K - P))]], { color: 'red', size: 'l' })
				const dot = geo(ctx, X(K + P) - 9, Y(0) - 9, 18, '', { geo: 'ellipse', h: 18, color: 'black', fill: 'fill', dash: 'solid' })
				const lab = (tx, ty, s, o = {}) => text(ctx, tx, ty, o.w || 200, s, o)
				const sm = { size: 's' }
				lab(X(K) + 10, y + top - 6, `**Strike ${K.toLocaleString('en-IN')}**`, { ...sm, color: 'grey' })
				lab(X(K + P) - 110, Y(0) + 44, `**Break-even ${(K + P).toLocaleString('en-IN')}**`, { ...sm, w: 220, align: 'middle' })
				lab(X(K + 60), Y(vmax * 0.72), '**Arvind (buyer)**\nLoss capped at the premium', { ...sm, color: 'green', w: 280 })
				lab(X(K + 60), Y(-vmax * 0.6), '**Salim (writer)**\nGain capped at the premium', { ...sm, color: 'red', w: 280 })
				lab(X(lo) + 12, Y(-P) + 8, `Arvind: minus ${P}`, { ...sm, color: 'green' })
				lab(X(lo) + 12, Y(P) - 30, `Salim: plus ${P}`, { ...sm, color: 'red' })
				for (const s of [lo, K, hi]) lab(X(s) - 50, Y(-vmax) + 10, s.toLocaleString('en-IN'), { ...sm, w: 100, align: 'middle', color: 'grey' })
				lab(X(lo) - 100, Y(0) - 12, 'Rs 0', { ...sm, w: 90, align: 'end', color: 'grey' })
				lab(x + left, y + H - 30, '_Nifty on expiry day_', { ...sm, w: pw, align: 'middle', color: 'grey' })
				void dot
				return { h: H, stretch: noOp }
			}
			default:
				throw new Error('unknown block ' + b.t)
		}
	}

	// ---- build
	await document.fonts.ready
	editor.deleteShapes([...editor.getCurrentPageShapeIds()])
	editor.renamePage(editor.getCurrentPageId(), spec.pageName)

	// warm up the fonts so measurement is right
	const warm = spec.style ? [S.bodyFont, S.headFont, S.noteFont] : []
	const warmIds = warm.map((f) => {
		const id = sid()
		editor.createShape({ id, type: 'text', x: 0, y: -500, props: { font: f, richText: rt('**Warm** up _fonts_ ==now==') } })
		return id
	})
	await new Promise((r) => setTimeout(r, 1500))
	await document.fonts.ready
	editor.deleteShapes(warmIds)

	const frames = spec.frames.map((f, i) => {
		const fid = sid()
		const ox = 0
		const oy = 20000 + i * 12000
		editor.createShape({ id: fid, type: 'frame', x: ox, y: oy, props: { w: FW, h: 200, name: f.name } })
		const ctx = { parent: fid, ox, oy }
		let y = PAD
		for (const b of f.blocks) y += place(ctx, b, PAD, y, CW).h + GAP
		const h = y - GAP + PAD
		editor.updateShape({ id: fid, type: 'frame', props: { h } })
		return { id: fid, h }
	})

	// banner across the top. Opening a file zooms to fit the whole board, so this is sized
	// to be readable at that zoom: it works as the title page.
	const FGAP = 140
	const cols = spec.columns
	const boardW = cols * (FW + FGAP) - FGAP
	const root = { parent: editor.getCurrentPageId(), ox: 0, oy: 0 }
	const bt = spec.banner
	const lw = 440
	const lgap = 40
	const legendW = bt.legend.length * (lw + lgap) - lgap
	const tw = boardW - legendW - 200
	const t1 = text(root, 0, 0, tw, bt.title, { size: 'xl', font: S.headFont, scale: 4.5 })
	const t2 = text(root, 0, t1.h + 30, tw, bt.sub, { size: 'l', color: 'grey', scale: 1.6 })
	const t3 = text(root, 0, t1.h + t2.h + 70, tw, bt.oneline, { size: 'l', font: S.headFont, color: 'violet', scale: 1.8 })
	const lx = boardW - legendW
	const lh = bt.legend.map(([kind, body], i) => {
		const [color, head] = NOTE[kind]
		return note(root, lx + i * (lw + lgap), 20, lw, `**${head || body.split('\n')[0]}**\n${head ? body : body.split('\n').slice(1).join('\n')}`, color).h
	})
	const hint = text(root, lx, 20 + Math.max(...lh) + 40, legendW, bt.hint, { size: 'l', color: 'grey', scale: 1.4 })
	const bannerH = Math.max(t1.h + t2.h + t3.h + 70, 60 + Math.max(...lh) + hint.h)

	// newspaper columns: fill a column top to bottom, then move right
	const total = frames.reduce((s, f) => s + f.h + FGAP, 0)
	const target = total / cols
	const top = bannerH + 220
	let col = 0
	let cy = top
	for (const f of frames) {
		if (cy > top && cy - top + f.h / 2 > target && col < cols - 1) {
			col++
			cy = top
		}
		editor.updateShape({ id: f.id, type: 'frame', x: col * (FW + FGAP), y: cy })
		cy += f.h + FGAP
	}

	const snap = editor.store.getStoreSnapshot('document')
	return {
		tldr: { tldrawFileFormatVersion: 1, schema: snap.schema, records: Object.values(snap.store) },
		frames: frames.map((f, i) => ({ id: f.id, name: spec.frames[i].name, h: Math.round(f.h) })),
		columns: col + 1,
	}
}
