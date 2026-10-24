"""Builds every page in public/ from content.py and content/bio.html.

Usage: python3 build_pages.py
"""
from html import escape as e
from pathlib import Path

import content as C

ROOT = Path(__file__).parent
OUT = ROOT / "public"
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500'
         '&family=Instrument+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">')
NAV = [("index.html", "Vision"), ("findings.html", "Findings"), ("consumer.html", "Consumer 2036"),
       ("scenarios.html", "Scenarios"), ("impact.html", "Impact"), ("strategy.html", "Strategy"), ("about.html", "About me")]


def page(path, title, description, body, current=None, extra=""):
    depth = path.count("/")
    p = "../" * depth
    links = "".join(f'<a href="{p}{href}"{" aria-current=page" if href == current else ""}>{label}</a>' for href, label in NAV)
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(description)}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}">
{FONTS}<link rel="stylesheet" href="{p}assets/styles.css"></head><body>
<nav class="site"><div class="wrap"><a class="mark" href="{p}index.html">{e(C.SITE)}<span>.</span></a><div class="links">{links}</div></div></nav>
<main>{body}</main>
<footer><div class="wrap"><span>© 2026 {e(C.AUTHOR)} · 2036 statements are scenarios, not predictions. Evidence reviewed {e(C.REVIEWED)}.</span><span><a href="{p}sources.html">Sources</a> · {e(C.DOMAIN)}</span></div></footer>
{extra}</body></html>"""
    out = OUT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


def src_list(ids, p=""):
    items = []
    for sid in ids:
        name, url, desc = C.SOURCES[sid]
        link = f'<a href="{e(url)}" rel="noopener">{e(name)}</a>' if url else e(name)
        items.append(f'<li><span class="id">{sid}</span><span>{link}<small>{e(desc)}</small></span></li>')
    return f'<ul class="srcs">{"".join(items)}</ul>'


def table(headers, rows, total_rows=()):
    th = "".join(f"<th scope=col>{e(h)}</th>" for h in headers)
    trs = "".join(
        f'<tr{" class=total" if i in total_rows else ""}>' + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>"
        for i, r in enumerate(rows))
    return f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def head(eyebrow, title, lead="", meta=""):
    return (f'<div class="wrap narrow page-head"><p class="eyebrow">{e(eyebrow)}</p><h1>{e(title)}</h1>'
            + (f'<p class="lead">{e(lead)}</p>' if lead else "")
            + (f'<p class="meta">{e(meta)}</p>' if meta else "") + "</div>")


def card(href, tag, title, text, go="Read more →"):
    return f'<a class="card" href="{href}"><span class="tag">{e(tag)}</span><h3>{e(title)}</h3><p>{e(text)}</p><span class="go">{go}</span></a>'


def finding_cards(kind, p=""):
    return "".join(card(f'{p}findings/{f["slug"]}.html', f'{kind} {f["n"]} of 5', f["title"], f["summary"])
                   for f in C.FINDINGS if f["kind"] == kind)


# ------------------------------------------------------------------ Home
H = C.HOME
home = f"""
<header class="hero"><div class="wrap">
 <div class="hero-text">
  <p class="eyebrow">{e(H["eyebrow"])}</p>
  <h1>{e(H["title"])}</h1>
  <p class="lead">{e(H["lead"])}</p>
  <div class="cta"><a class="btn" href="findings.html">Explore the 10 findings</a><a class="btn ghost" href="consumer.html">The 2036 consumer</a></div>
  <div class="byline"><img src="assets/portrait.jpg" alt="" width="44" height="44"><span>By <a href="about.html">{e(C.AUTHOR)}</a> · Global Head Coloration, dsm-firmenich</span></div>
 </div>
 <figure class="cover"><img src="assets/cover-2036.jpg" alt="Still life of citrus peel, vanilla, cocoa, protein powder and fermentation glassware" width="900" height="1200"><figcaption>Conceptual AI-generated image</figcaption></figure>
</div></header>

<section style="padding-top:24px"><div class="wrap">
 <div class="brief">
  <div class="panel accent"><p class="eyebrow">A typical buying brief in 2036</p><p class="quote">“{e(H["brief"])}”</p></div>
  <div class="panel"><p class="eyebrow">Where value is likely to move</p><p>{e(H["value_shift"])}</p><p class="note">{e(H["central"])}</p></div>
 </div>
</div></section>

<section style="padding-top:0"><div class="wrap">
 <div class="sec-head"><p class="eyebrow">Five regulatory disruptions</p><h2>Rules that will reshape recipes</h2><p>Safety, nutrition, approvals, origin and claims: each one raises the value of evidence.</p></div>
 <div class="cards">{finding_cards("Regulation")}</div>
</div></section>

<section class="band"><div class="wrap">
 <div class="sec-head"><p class="eyebrow">Five technology disruptions</p><h2>Capabilities that will change how ingredients are made</h2><p>From AI-assisted formulation to side-stream recovery, selectively scaled where the economics work.</p></div>
 <div class="cards">{finding_cards("Technology")}</div>
</div></section>

<section><div class="wrap">
 <div class="sec-head"><p class="eyebrow">What it means</p><h2>From disruption to decision</h2></div>
 <div class="cards pair">
  {card("consumer.html", "Consumer 2036", "What people could pay for", "Food that feels made for them, delivers an exceptional experience and lets them take part in occasions they value.")}
  {card("scenarios.html", "Scenarios", "Four plausible markets in 2036", "Two uncertainties, technology scale-up and regulatory alignment, define four futures and one central planning case.")}
  {card("impact.html", "Impact", "Flavours capture more reformulation value", "Product briefs, impact by industry segment and a worked reformulation business case.")}
  {card("strategy.html", "Strategy", "A staged response through 2036", "Management gates, signals that would change the plan, and the strategic choice.")}
 </div>
</div></section>

<section style="padding-top:0"><div class="wrap">
 <div class="panel accent" style="padding:40px">
  <p class="eyebrow">The strategic choice</p>
  <h2>{e(C.CHOICE["headline"])}</h2>
  <div class="two" style="margin-top:12px">
   <div><h3>Commit now</h3><p class="muted">{e(C.CHOICE["commit"])}</p></div>
   <div><h3>Scale only with evidence</h3><p class="muted">{e(C.CHOICE["scale"])}</p></div>
  </div>
  <p><strong>{e(C.CHOICE["advantage"])}</strong></p>
 </div>
 <p class="note" style="margin-top:28px">{e(H["scope"])}</p>
</div></section>
"""
page("index.html", f"{C.SITE} | {C.AUTHOR}", H["lead"], home, "index.html")

# ------------------------------------------------------------------ Findings overview
overview = head("Ten findings", "Five regulatory and five technology disruptions",
                "Each finding separates today’s evidence from the plausible change by 2036, with an industry example, its limits and primary sources.")
overview += f"""<section style="padding-top:8px"><div class="wrap">
 <div class="sec-head"><p class="eyebrow">Regulation</p><h2>Regulatory disruptions</h2></div><div class="cards">{finding_cards("Regulation")}</div>
 <div class="sec-head" style="margin-top:56px"><p class="eyebrow">Technology</p><h2>Technology disruptions</h2></div><div class="cards">{finding_cards("Technology")}</div>
</div></section>"""
page("findings.html", f"Findings | {C.SITE}", "Five regulatory and five technology disruptions for food ingredients by 2036.", overview, "findings.html")

# ------------------------------------------------------------------ Finding detail pages
for i, f in enumerate(C.FINDINGS):
    prev_f = C.FINDINGS[i - 1] if i > 0 else None
    next_f = C.FINDINGS[i + 1] if i < len(C.FINDINGS) - 1 else None
    pager = '<div class="pager">'
    pager += (f'<a href="{prev_f["slug"]}.html">← Previous<b>{e(prev_f["title"])}</b></a>' if prev_f else '<a href="../findings.html">← All findings</a>')
    pager += (f'<a href="{next_f["slug"]}.html" style="text-align:right">Next →<b>{e(next_f["title"])}</b></a>' if next_f else '<a href="../strategy.html" style="text-align:right">Next →<b>A staged response through 2036</b></a>')
    pager += "</div>"
    notes = "".join(f"<p>{e(n)}</p>" for n in f["notes"])
    body = head(f'{f["kind"]} {f["n"]} of 5', f["title"], f["summary"], f["meta"])
    body += f"""<div class="wrap narrow">
 <div class="two block"><div class="panel"><p class="eyebrow">Evidence today</p><p>{e(f["evidence"])}</p></div>
 <div class="panel accent"><p class="eyebrow">Plausible change by 2036</p><p>{e(f["change"])}</p></div></div>
 <div class="block"><h2>Example and industry impact</h2><p>{e(f["example"])}</p></div>
 <div class="block"><h2>Status and limits</h2><p class="note">{e(f["status"])}</p></div>
 <div class="block notes"><h2>Analyst notes</h2>{notes}</div>
 <div class="block"><h2>Sources</h2>{src_list(f["sources"])}<p class="muted" style="font-size:.9rem">2036 statements are scenarios. Sources accessed {e(C.REVIEWED)}.</p></div>
 {pager}
</div><div style="height:56px"></div>"""
    page(f'findings/{f["slug"]}.html', f'{f["title"]} | {C.SITE}', f["summary"], body, "findings.html")

# ------------------------------------------------------------------ Consumer
K = C.CONSUMER
body = head("Consumer 2036", "What people could pay for in 2036", K["intro"][0])
body += f"""<div class="wrap narrow"><p class="note" style="margin-bottom:44px">{e(K["intro"][1])}</p></div>
<div class="wrap"><div class="block">{table(("What people could pay for", "A concrete experience", "Immediate, visible or social benefit", "Role of ingredients and technology"), K["table"])}</div></div>
<div class="wrap narrow">
 <div class="block"><h2>Imagine a personalised café breakfast</h2><p>The most interesting 2036 product could combine several of these benefits.</p>
  <ul>{"".join(f"<li>{e(x)}</li>" for x in K["breakfast"])}</ul><p>{e(K["breakfast_close"])}</p></div>
 <div class="block"><h2>What might become “fancy”, and what could become ordinary?</h2><p>My scenario is that personalisation splits into two markets:</p>
  {table(("Everyday personalisation", "Premium personalisation"), K["split"])}<p>{e(K["split_close"])}</p></div>
 <div class="block"><h2>Where I would be sceptical</h2><p>I would be more sceptical of products sold mainly as:</p><ul>{"".join(f"<li>{e(x)}</li>" for x in K["sceptical"])}</ul></div>
 <div class="block panel accent"><p class="eyebrow">The strongest 2036 proposition for the ingredients industry</p><p class="quote">“{e(K["proposition"])}”</p><p>{e(K["proposition_close"])}</p></div>
 <div class="block"><h2>Evidence and sources</h2><p class="note">{e(K["evidence_note"])}</p>{src_list(K["sources"])}</div>
</div><div style="height:40px"></div>"""
page("consumer.html", f"Consumer 2036 | {C.SITE}", K["intro"][0], body, "consumer.html")

# ------------------------------------------------------------------ Scenarios
M = C.MATRIX
cells = '<div class="ax corner"></div>' + "".join(f'<div class="ax top">{e(c)}</div>' for c in M["cols"])
for r, row in enumerate(M["cells"]):
    cells += f'<div class="ax">{e(M["rows"][r])}</div>'
    for col, (name, text, central) in enumerate(row):
        cells += (f'<div class="cell{" central" if central else ""}"><span class="eyebrow">{e(M["rows"][r])} · {e(M["cols"][col])}</span>'
                  f'<h3>{e(name)}{" (central case)" if central else ""}</h3><p>{e(text)}</p></div>')
body = head("Scenarios", "Four plausible food-ingredient markets in 2036", "Two uncertainties shape the decade: the pace of technology scale-up and the degree of regulatory alignment.")
body += f"""<div class="wrap">
 <div class="block"><div class="matrix">{cells}</div></div>
</div><div class="wrap narrow">
 <div class="block"><p class="note">{e(M["note"])}</p>{src_list(["S01"])}</div>
 <div class="block"><h2>Expert foundations</h2><p>Published methods and research inform the analysis.</p>
  {table(("Expert foundation", "Lens used", "Artefact produced"), C.EXPERTS)}<p class="note">{e(C.EXPERTS_NOTE)}</p>
  {src_list(["S01", "S02", "S03", "S04", "S05", "S20"])}</div>
 <div class="block"><h2>Signals that would change the plan</h2><p>A credible vision includes reasons it might be wrong.</p>
  {table(("Signal to monitor", "What it would mean", "Strategic response"), C.SIGNALS)}<p class="note">{e(C.SIGNALS_NOTE)}</p></div>
</div><div style="height:40px"></div>"""
page("scenarios.html", f"Scenarios | {C.SITE}", "Four plausible food-ingredient markets in 2036.", body, "scenarios.html")

# ------------------------------------------------------------------ Impact
briefs = [(f"{n}. {t}", s, b) for n, t, s, b in C.BRIEFS]
body = head("Impact", "Flavours capture more reformulation value", "2036 hypothesis: more business comes from preserving a sensory promise under changing constraints.")
body += f"""<div class="wrap narrow">
 <div class="block">{table(("Customer problem", "What the flavour supplier sells", "What determines value"), C.FLAVOURS)}<p class="note">{e(C.FLAVOURS_NOTE)}</p>{src_list(["S04", "S07", "S15", "S16"])}</div>
 <div class="block"><h2>Three products that make 2036 concrete</h2>{table(("2036 product brief", "Ingredient system", "Business effect"), briefs)}<p class="note">{e(C.BRIEFS_NOTE)}</p></div>
 <div class="block"><h2>The impact across food and beverages</h2><p>Strategic inferences for the central 2036 scenario.</p>{table(("Industry segment", "Likely change in demand", "Operating consequence"), C.SEGMENTS)}<p class="note">{e(C.SEGMENTS_NOTE)}</p></div>
 <div class="block"><h2>A concrete reformulation business case</h2><p>Illustrative annual model: 100 million litres. Every price and cost below is an assumption, not a forecast.</p>
  {table(("Change", "Calculation", "Annual effect"), [r[:3] for r in C.BUSINESS_CASE], total_rows={i for i, r in enumerate(C.BUSINESS_CASE) if r[3]})}
  <p class="note">{e(C.BUSINESS_CASE_NOTE)}</p></div>
</div><div style="height:40px"></div>"""
page("impact.html", f"Impact | {C.SITE}", "How the 2036 disruptions change value across food and beverage segments.", body, "impact.html")

# ------------------------------------------------------------------ Strategy
steps = "".join(f'<div class="step"><span class="when">{e(w)}</span><h3>{e(a)}</h3><p>Evidence before expansion: {e(ev)}</p></div>' for w, a, ev in C.ROADMAP)
body = head("Strategy", "A staged response through 2036", "Backcasting from the central scenario. Proposed management gates, not industry benchmarks.")
body += f"""<div class="wrap narrow">
 <div class="block"><div class="timeline">{steps}</div><p class="note" style="margin-top:28px">{e(C.ROADMAP_NOTE)}</p></div>
 <div class="block panel accent"><p class="eyebrow">The strategic choice</p><h2>{e(C.CHOICE["headline"])}</h2>
  <div class="two"><div><h3>Commit now</h3><p class="muted">{e(C.CHOICE["commit"])}</p></div><div><h3>Scale only with evidence</h3><p class="muted">{e(C.CHOICE["scale"])}</p></div></div>
  <p><strong>{e(C.CHOICE["advantage"])}</strong></p></div>
 <div class="block"><p class="note">{e(C.CHOICE["note"])}</p><p><a href="scenarios.html">See the signals that would change this plan →</a></p></div>
</div><div style="height:40px"></div>"""
page("strategy.html", f"Strategy | {C.SITE}", "A staged response for food-ingredient companies through 2036.", body, "strategy.html")

# ------------------------------------------------------------------ About (bio)
bio = (ROOT / "content" / "bio.html").read_text()
script = (ROOT / "content" / "bio-script.html").read_text()
page("about.html", f"{C.AUTHOR} | About", "Senior commercial leader with 21+ years in the global B2B ingredients industry.", bio, "about.html", extra=script)

# ------------------------------------------------------------------ Sources
body = head("Sources", "Primary rules, original research and identified commercial examples",
            "Primary legal and research sources are preferred. Supplier examples are identified as supplier evidence. 2036 scenarios, rankings and financial assumptions are original analysis.")
body += f'<div class="wrap narrow"><div class="block">{src_list(list(C.SOURCES))}<p class="muted" style="font-size:.9rem">Accessed {e(C.REVIEWED)}.</p></div></div><div style="height:40px"></div>'
page("sources.html", f"Sources | {C.SITE}", "Sources behind the Food Ingredients 2036 vision.", body)

# ------------------------------------------------------------------ 404
page("404.html", f"Page not found | {C.SITE}", "Page not found", head("404", "Page not found", "") + '<div class="wrap narrow"><p><a href="/index.html">Go to the home page →</a></p></div><div style="height:80px"></div>')

print("Built", len(list(OUT.rglob("*.html"))), "pages")
