"""Render the repository's Markdown into docs/ for GitHub Pages.

    python3 docs/build.py

Needs pandoc. Produces docs/index.html (progress log + links), docs/survey.html
and docs/dihedral.html, all sharing one stylesheet and MathJax for $...$ math.
"""

import subprocess, re, math, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")

PAGES = [
    # (source, output, eyebrow, title, dek)
    ("PROGRESS.md", "index.html", "Project · prove it or break it",
     "Lovász Conjecture Project",
     "Working toward a proof or a counterexample. Survey, notes on the dihedral case, tools, and the hand-off log."),
    ("lovasz-conjecture-survey.md", "survey.html", "Survey · Hamiltonian paths in vertex-transitive graphs",
     "The Lovász Conjecture",
     "What is known, by order, by group, and by density, about whether every finite connected vertex-transitive graph has a Hamiltonian path."),
    ("dihedral/NOTES.md", "dihedral.html", "Working notes · Cayley graphs on D₂ₙ, n odd",
     "The Odd Dihedral Case",
     "Reductions, two theorems with proofs, certificate code, and what the literature already knew."),
]

NAV = """<nav class="site"><a href="index.html">Progress</a><a href="survey.html">Survey</a><a href="dihedral.html">Dihedral notes</a><a href="https://github.com/geneweng/lovasz-conjecture">Repository</a></nav>"""

STYLE = """
:root {
  --paper:#F6F7F5; --ink:#1A2230; --muted:#5B6470; --rule:#D5D9D3; --soft:#ECEEEA;
  --accent:#1E6E73; --accent-ink:#155257; --open:#8A4B1A;
  --display:"Fraunces", Georgia, "Times New Roman", serif;
  --body:"Source Serif 4", Georgia, "Times New Roman", serif;
  --ui:"IBM Plex Sans", "Helvetica Neue", Arial, sans-serif;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper:#151A1F; --ink:#E6E8E4; --muted:#9AA3AD; --rule:#2C343C; --soft:#1D242B;
    --accent:#5FC1C5; --accent-ink:#8ED6D9; --open:#E0A06A; color-scheme: dark;
  }
}
* { box-sizing: border-box; }
body { margin:0; background:var(--paper); color:var(--ink); font-family:var(--body); font-size:17px; line-height:1.6; }
a { color:var(--accent-ink); text-decoration-thickness:1px; text-underline-offset:2px; }
a:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
.wrap { max-width:1120px; margin:0 auto; padding:0 24px 96px; }
nav.site { display:flex; gap:22px; padding:18px 0 0; font-family:var(--ui); font-size:13px; letter-spacing:.04em; text-transform:uppercase; }
nav.site a { color:var(--muted); text-decoration:none; }
nav.site a:hover { color:var(--accent-ink); }
header.mast { display:grid; grid-template-columns:1fr auto; gap:32px; align-items:end; padding:40px 0 32px; border-bottom:1px solid var(--rule); }
.eyebrow { font-family:var(--ui); font-size:12px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); margin:0 0 14px; }
header h1 { font-family:var(--display); font-weight:500; font-size:clamp(34px, 4.6vw, 54px); line-height:1.08; margin:0 0 18px; text-wrap:balance; max-width:22ch; letter-spacing:-.01em; }
.dek { font-size:19px; color:var(--muted); max-width:58ch; margin:0; text-wrap:pretty; }
.petersen { width:168px; height:168px; }
.petersen line { stroke:var(--accent); stroke-width:2.2; stroke-linecap:round; }
.petersen circle { fill:var(--paper); stroke:var(--ink); stroke-width:2.2; }
.grid { display:grid; grid-template-columns:220px minmax(0,1fr); gap:56px; padding-top:40px; }
nav.toc { position:sticky; top:24px; align-self:start; font-family:var(--ui); font-size:13.5px; line-height:1.45; }
nav.toc .eyebrow { margin-bottom:10px; }
nav.toc ol { list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:7px; }
nav.toc a { color:var(--muted); text-decoration:none; }
nav.toc a:hover { color:var(--accent-ink); text-decoration:underline; }
main { max-width:68ch; min-width:0; }
main h2 { font-family:var(--display); font-weight:600; font-size:27px; line-height:1.2; margin:56px 0 14px; text-wrap:balance; letter-spacing:-.005em; }
main h2:first-child { margin-top:0; }
main h3 { font-family:var(--ui); font-weight:600; font-size:14px; letter-spacing:.06em; text-transform:uppercase; color:var(--accent-ink); margin:34px 0 8px; }
main p { margin:0 0 16px; text-wrap:pretty; }
main ul, main ol { padding-left:1.3em; margin:0 0 18px; }
main li { margin:0 0 7px; }
main li::marker { color:var(--muted); font-family:var(--ui); font-size:.9em; }
main strong { font-weight:600; }
main code { font-family:"IBM Plex Mono", ui-monospace, Menlo, monospace; font-size:.88em; background:var(--soft); padding:1px 5px; border-radius:3px; }
main pre { background:var(--soft); padding:14px 16px; overflow-x:auto; border-radius:4px; font-size:14px; line-height:1.5; }
main pre code { background:none; padding:0; }
.tablewrap { overflow-x:auto; margin:8px 0 26px; border-top:2px solid var(--ink); border-bottom:1px solid var(--rule); }
table { border-collapse:collapse; width:100%; font-family:var(--ui); font-size:14px; line-height:1.4; font-variant-numeric:tabular-nums; }
th { text-align:left; font-weight:600; font-size:12px; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); padding:10px 14px 8px 0; border-bottom:1px solid var(--rule); }
td { vertical-align:top; padding:9px 14px 9px 0; border-bottom:1px solid var(--rule); }
tr:last-child td { border-bottom:0; }
#references ~ p { font-family:var(--ui); font-size:13px; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); margin:28px 0 8px; }
#references ~ ul { list-style:none; padding:0; font-size:15px; }
#references ~ ul li { padding:6px 0 6px 18px; text-indent:-18px; border-bottom:1px solid var(--soft); }
mjx-container { font-size:104% !important; }
mjx-container[display="true"] { overflow-x:auto; }
@media (max-width: 860px) {
  .grid { grid-template-columns:1fr; gap:32px; }
  nav.toc { position:static; border-bottom:1px solid var(--rule); padding-bottom:20px; }
  nav.toc ol { flex-direction:row; flex-wrap:wrap; gap:6px 18px; }
  header.mast { grid-template-columns:1fr; }
  .petersen { width:120px; height:120px; }
  body { font-size:16px; }
}
"""


def petersen_svg():
    outer = [(90 * math.cos(-math.pi / 2 + 2 * math.pi * k / 5), 90 * math.sin(-math.pi / 2 + 2 * math.pi * k / 5)) for k in range(5)]
    inner = [(42 * math.cos(-math.pi / 2 + 2 * math.pi * k / 5), 42 * math.sin(-math.pi / 2 + 2 * math.pi * k / 5)) for k in range(5)]
    edges = []
    for k in range(5):
        edges += [(outer[k], outer[(k + 1) % 5]), (outer[k], inner[k]), (inner[k], inner[(k + 2) % 5])]
    s = ['<svg class="petersen" viewBox="-104 -104 208 208" role="img" aria-label="The Petersen graph">']
    s += [f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}"/>' for a, b in edges]
    s += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5"/>' for x, y in outer + inner]
    return "\n".join(s) + "\n</svg>"


def render(src, out, eyebrow, title, dek):
    body = subprocess.run(
        ["pandoc", os.path.join(ROOT, src), "-f", "gfm+tex_math_dollars", "-t", "html", "--mathjax", "--wrap=none"],
        capture_output=True, text=True, check=True).stdout
    body = re.sub(r"<h1[^>]*>.*?</h1>\s*", "", body, count=1, flags=re.S)
    body = re.sub(r"<p><em>Status as of [^<]*</em></p>\s*", "", body, count=1)
    # relative links to repo files -> GitHub
    body = re.sub(r'href="(?!https?://|#)([^"]+)"',
                  lambda m: f'href="https://github.com/geneweng/lovasz-conjecture/blob/main/{m.group(1)}"', body)
    toc = [(m.group(1), re.sub(r"<[^>]+>", "", m.group(2))) for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body)]
    toc_html = "\n".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    body = body.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono&display=swap">
<style>{STYLE}</style>
</head>
<body>
<div class="wrap">
{NAV}
<header class="mast">
  <div>
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title}</h1>
    <p class="dek">{dek}</p>
  </div>
  {petersen_svg()}
</header>
<div class="grid">
<nav class="toc" aria-label="Sections">
  <p class="eyebrow">Sections</p>
  <ol>
  {toc_html}
  </ol>
</nav>
<main>
{body}
</main>
</div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.js"></script>
</body>
</html>
"""
    with open(os.path.join(DOCS, out), "w") as f:
        f.write(page)
    print(out, len(page), "bytes,", len(toc), "sections")


if __name__ == "__main__":
    os.makedirs(DOCS, exist_ok=True)
    for args in PAGES:
        render(*args)
    open(os.path.join(DOCS, ".nojekyll"), "w").close()
