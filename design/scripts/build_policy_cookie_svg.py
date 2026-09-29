"""Rebuild observed policy cookie-close viewports; no unobserved body text."""
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parents[1] / 'polyulife'


def group_span(svg, group_id):
    start = svg.index(f'<g id="{group_id}"')
    depth = 0
    for match in re.finditer(r'<g\b[^>]*>|</g>', svg[start:]):
        depth += -1 if match.group() == '</g>' else 1
        if depth == 0:
            return start, start + match.end()
    raise ValueError(f'Unclosed group: {group_id}')


specs = {
    'privacy': ('privacy-policy', 903, [
        (0, 22, '2.', '#A3273D', 400),
        (38, 22, 'We protect the privacy of users of our', '#292929', 400),
        (38, 55, 'website. Any personal data collected from', '#292929', 400),
    ]),
    'terms': ('terms-of-use', 902.5, [
        (0, 22, '2.', '#A3273D', 400),
        (38, 22, 'Links to and from this Website', '#292929', 700),
        (38, 70, 'The links on this Website may take you to', '#292929', 400),
    ]),
}
for slug, (base, top, lines) in specs.items():
    texts = ''.join(f'<text x="{x}" y="{y}" font-family="Roboto" font-size="21.7" font-weight="{weight}" fill="{color}">{escape(text)}</text>' for x, y, text, color, weight in lines)
    fragment = f'<g id="RevealedParagraphFragment">{texts}</g>'
    (ROOT / f'{slug}-revealed-paragraph.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="500" height="80" viewBox="0 0 500 80">{fragment}</svg>\n')
    path = ROOT / f'{base}.svg'
    svg = path.read_text()
    if '<g id="RevealedParagraphFragment"' in svg:
        start, end = group_span(svg, 'RevealedParagraphFragment')
        svg = svg[:start] + svg[end:]
    fragment = fragment.replace('<g id="RevealedParagraphFragment">', f'<g id="RevealedParagraphFragment" transform="translate(65 {top})">')
    insert, _ = group_span(svg, 'CookieNotice')
    svg = svg[:insert] + fragment + svg[insert:]
    path.write_text(svg)
    start, end = group_span(svg, 'CookieNotice')
    (ROOT / f'{base}-no-cookie.svg').write_text(svg[:start] + svg[end:])
