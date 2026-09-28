"""Build editable Food screen reconstructions using public cropped artwork.

Only writes design/polyulife SVG files. Assets were cropped from redacted public
evidence; raster assets are limited to map imagery and genuine logo artwork.
"""
from base64 import b64encode
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parents[1] / "polyulife"


def txt(x, y, value, size=22, weight=400, color="#141414", anchor=None):
    align = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="sans-serif" font-size="{size}" font-weight="{weight}"{align}>{escape(value)}</text>'


def bitmap(asset, x, y, w, h, gid):
    data = b64encode((OUT / "assets" / asset).read_bytes()).decode()
    return f'<g id="{gid}"><image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="none" xlink:href="data:image/png;base64,{data}"/></g>'


def header(title):
    return '<g id="Header"><rect x="0.5" y="0.5" width="575" height="99" fill="#FFFFFF" stroke="#E1E1E1"/><g id="Back"><path d="M34.5 57.5L27 65L34.5 72.5" stroke="#202020" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>' + txt(288, 75.5, title, 27, anchor="middle") + '</g>'


def svg(name, title, desc, body):
    content = f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="576" height="970" viewBox="0 0 576 970" fill="none"><title>{escape(title)}</title><desc>{escape(desc)}</desc><rect id="ScreenBackground" width="576" height="970" fill="#FFFFFF"/>' + body + '</svg>'
    (OUT / name).write_text(content)


def restaurant_icon(x, y, gid):
    return f'<g id="{gid}" transform="translate({x},{y})"><path d="M2 2L17 17M17 2L2 17M1 5L5 1M4 8L8 4M7 11L11 7" stroke="#818481" stroke-width="2.8" stroke-linecap="round"/><path d="M18 0L12 7L16 10L21 4" fill="#818481"/></g>'


def open_status(x, y, suffix, expand=False):
    result = f'<g id="OpeningHours{suffix}"><rect x="{x}" y="{y}" width="123" height="30" rx="15" fill="#E8F5DB"/><circle cx="{x+14}" cy="{y+15}" r="6" fill="#7EAD54"/>'
    result += txt(x + 27, y + 22, 'Open Now', 18) + txt(x + 128, y + 22, 'Close at 23:59', 17, color="#555555")
    result += f'<path d="M{x+247} {y+12}L{x+253} {y+19}L{x+259} {y+12}Z" fill="#878787"/>'
    if expand:
        result += f'<g id="OpeningHoursExpanded"><circle cx="{x+12}" cy="{y+54}" r="9" stroke="#8A8A8A" stroke-width="2.5"/><path d="M{x+12} {y+48}V{y+54}L{x+17} {y+57}" stroke="#8A8A8A" stroke-width="2"/>'
        result += txt(x + 32, y + 58, 'Mon - Sun, public holiday:   00:00 - 23:59', 14, color="#646464") + '</g>'
    return result + '</g>'


def tags(x, y, items, suffix, size=18, heights=26):
    result = f'<g id="Tags{suffix}">'
    for i, (label, width) in enumerate(items):
        result += f'<g id="Tag{suffix}{i}"><rect x="{x}" y="{y}" width="{width}" height="{heights}" rx="13" fill="#EFEFEF"/>'
        result += txt(x + 8, y + heights - 6, '#' + label, size, color="#555555") + '</g>'
        x += width + 4
    return result + '</g>'


def list_card(y, index, asset, show_tags=False, expanded=False, partial=False):
    result = f'<g id="VenueCard{index}">'
    result += f'<rect x="28" y="{y}" width="64" height="64" rx="8" fill="#FFFFFF" stroke="#E5E5E5"/>'
    result += bitmap(asset, 29, y + 1, 63, 45 if partial else 63, f'VenueLogo{index}')
    result += txt(119, y + 21, 'VA210 Vending Machine', 22, 700)
    result += restaurant_icon(122, y + 35, f'VenueTypeIcon{index}') + txt(151, y + 51, 'P/F, Block VA · Vending Machine', 20.5, color="#484848")
    if partial:
        return result + '</g>'
    result += open_status(119, y + 68, str(index), expanded)
    result += f'<g id="VenueMenu{index}"><circle cx="532" cy="{y+66 if not expanded else y+85}" r="2.7" fill="#9FB2BE"/><circle cx="540" cy="{y+66 if not expanded else y+85}" r="2.7" fill="#9FB2BE"/><circle cx="548" cy="{y+66 if not expanded else y+85}" r="2.7" fill="#9FB2BE"/></g>'
    if show_tags:
        result += '<g clip-path="url(#ListTagViewport)">' + tags(119, y + (155 if expanded else 115), [('Chinese Soup', 137), ('Snacks', 84), ('Bottled Herbal Tea', 187)] if index == 1 else [('Halal Certified Snacks', 203)], str(index)) + '</g>'
    return result + '</g>'


for expanded in (False, True):
    body = '<defs><clipPath id="ListTagViewport"><rect x="0" y="0" width="508" height="970"/></clipPath></defs>'
    body += bitmap('food-map-list.png', 0, 100, 576, 286, 'PublicMap')
    body += '<g id="VenueListPanel"><path d="M0 401Q0 356 43 356H533Q576 356 576 401V970H0Z" fill="#FFFFFF"/><g id="PanelHandle"><rect x="238.5" y="371" width="100" height="7.5" rx="2" fill="#31917D"/></g>'
    body += list_card(413, 1, 'food-thumb-soup.png', True, expanded)
    delta = 40 if expanded else 0
    body += list_card(600 + delta, 2, 'food-thumb-taobin.png')
    body += list_card(737 + delta, 3, 'food-thumb-freshup.png', True)
    body += list_card(924 + delta, 4, 'food-thumb-sakura-partial.png', partial=True)
    body += f'<path d="M0 {578+delta}H576M0 {715+delta}H576M0 {902+delta}H576" stroke="#DADADA" stroke-width="1.4"/></g>'
    body += header('Food')
    source = 'food-160657-opening-hours-expanded.png' if expanded else 'food-160642-map-list-loaded.png'
    svg('food-list-hours.svg' if expanded else 'food-list.svg', 'Food — List — Opening Hours Expanded' if expanded else 'Food — Map and List', f'Editable reconstruction from {source}. Public map imagery crop (0,100,576,386) from food-160642-map-list-loaded.png and genuine thumbnail-logo crops are raster; all app titles, venue data, tags, status controls, icons and list-panel geometry are native editable elements. The observed list map viewport did not show provider attribution; no visible attribution has been removed. Tag row clipping and partially visible fourth card follow the screenshot. No unseen restaurant records or actions invented. Cursor and hover omitted. Native icons and fonts are approximations.', body)


body = '<g id="PageContent"><rect x="0" y="100" width="576" height="870" fill="#F7F9F6"/><rect x="18.5" y="100" width="539" height="870" fill="#FFFFFF" stroke="#CACFD0"/>'
body += bitmap('food-hero-detail.png', 207, 100, 225, 244, 'VenueHero')
body += '<g id="ExpandImage"><path d="M497 287H490V294M505 287H512V294M490 304V311H497M505 311H512V304" stroke="#31917D" stroke-width="4"/></g>'
body += txt(35, 377, 'VA210 Vending Machine', 22, 700) + txt(35, 420, 'P/F, Block VA', 20.5, color="#3C3C3C")
body += '<g id="CallVenue"><rect x="175" y="384" width="113" height="48" rx="24" fill="#FFFFFF" stroke="#DEDEDE" stroke-width="1.5"/><path d="M202 400C200 403 203 411 210 416C216 421 220 419 221 416L216 412L212 414L207 408L208 404Z" stroke="#838383" stroke-width="2" stroke-linejoin="round"/>' + txt(231, 416, 'Call', 19.5, color="#4F4F4F") + '</g>'
body += '<g id="VenueOpeningHours"><rect x="35" y="452" width="138" height="34" rx="17" fill="#E8F5DB"/><circle cx="49" cy="469" r="6.5" fill="#7EAD54"/>' + txt(62, 477, 'Open Now', 20.5) + txt(179, 477, 'Close at 23:59', 20.5, color="#3F3F3F") + txt(35, 516, 'Mon - Sun, public holiday: 00:00 - 23:59', 20.5, color="#343434") + '</g>'
body += '<path d="M35 544.5H542M35 635H542" stroke="#DCDCDC" stroke-width="1.5"/>' + tags(35, 579, [('Chinese Soup', 158), ('Snacks', 95), ('Bottled Herbal Tea', 202)], 'Detail', 21)
body += bitmap('food-map-detail.png', 35, 671, 507, 299, 'PublicMap')
body += '<g id="MapCallout"><path d="M151 705H426V752H300L288 764L276 752H151Z" fill="#FFFFFF"/>' + txt(288, 736, 'VA210, P/F, Block VA', 27, anchor='middle') + '</g>'
body += '<g id="ExpandMap"><rect x="446.5" y="907.5" width="71" height="68" rx="12" fill="#FFFFFF" stroke="#ADB8C0" stroke-width="1.5"/><path d="M470 952L495 926M484 926H496V938M467 942V954H479" stroke="#272B29" stroke-width="3.7" stroke-linecap="round" stroke-linejoin="round"/></g></g>' + header('VA210 Vending Machine')
svg('food-detail.svg', 'Food — VA210 Vending Machine — Detail', 'Editable reconstruction from food-160738-vending-detail-map-loaded.png. Genuine public vendor artwork and public map crop (35,671,542,970) are raster. The map Google attribution is preserved. Map place labels remain part of map artwork, while app title, venue text, opening hours, tags, Call, image expansion, map expansion, Back and map callout are editable text/vectors. Public phone action was not invoked. Cursor/hover omitted. Native icon and font approximations.', body)


base = (OUT / 'search-empty.svg').read_text()
base = base.replace('<title>Search — Empty</title>', '<title>Food — Tag Search — Chinese Soup</title>')
a = base.index('<desc>'); b = base.index('</desc>', a) + len('</desc>')
base = base[:a] + '<desc>Editable reconstruction from food-160820-chinese-soup-tag-result.png. Observed Chinese Soup tag opens Search with one visible VA210 Vending Machine result. Back, input and result are native editable controls. No clear button was visible in this tag-search state, so none is invented. Pointer/hover omitted.</desc>' + base[b:]
base = base.replace('fill="#8D9AA4" font-family="sans-serif" font-size="23" font-weight="400" >Search</text>', 'fill="#141414" font-family="sans-serif" font-size="23" font-weight="400">Chinese Soup</text>')
base = base.replace('</svg>', '<g id="SearchResult">' + txt(31, 248, 'VA210 Vending Machine', 22, color='#4F4F4F') + '<path d="M485 232L491 239L485 246" stroke="#818181" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></g></svg>')
(OUT / 'food-tag-search.svg').write_text(base)


body = bitmap('food-hero-expanded.png', 203, 360, 237, 283, 'ExpandedVenueArtwork')
body += '<g id="CloseImage"><path d="M514 134L535 155M535 134L514 155" stroke="#141414" stroke-width="4.5" stroke-linecap="square"/></g>'
svg('food-image.svg', 'Food — Expanded Venue Image', 'Editable reconstruction from food-160932-hero-expanded.png. Only the genuine vendor artwork crop (203,360,440,643), converted to sRGB, is raster. Page background and Close control are native editable vectors. Cursor and hover omitted.', body)

for panned in (False, True):
    asset = 'food-map-full-panned.png' if panned else 'food-map-full-campus.png'
    source = 'food-165258-full-map-panned-pointer-on-header.png' if panned else 'food-165325-full-map-campus-pointer-on-header.png'
    body = '<g id="MapViewport">' + bitmap(asset, 0, 100, 576, 870, 'PublicMap')
    if not panned:
        body += '<g id="MapCallout"><path d="M151 442H426V488H300L288 500L276 488H151Z" fill="#FFFFFF"/>' + txt(288, 473, 'VA210, P/F, Block VA', 27, anchor='middle') + '</g>'
        body += '<g id="VenueMapMarker"><path d="M288 561C282 548 269 537 269 526C269 515 277 507 288 507C299 507 307 515 307 526C307 537 295 552 288 561Z" fill="#D55376" stroke="#AD415B" stroke-width="1.5"/><circle cx="288" cy="526" r="8" fill="#A32944"/></g>'
    body += '<g id="Locate"><circle cx="518" cy="968" r="43.5" fill="#FFFFFF" stroke="#E2E7E7" stroke-width="1.5"/><circle cx="518" cy="969" r="12" stroke="#656A6B" stroke-width="3.2"/><circle cx="518" cy="969" r="6" fill="#656A6B"/><path d="M518 951V956M500 969H505M531 969H536" stroke="#656A6B" stroke-width="3.2"/></g></g>'
    body += header('VA210 Vending Machine')
    state = 'Observed Panned View' if panned else 'Observed Campus View'
    svg('food-map-panned.svg' if panned else 'food-map.svg', 'Food — Full Map — ' + state, f'Editable reconstruction from {source}. Only the actual public map viewport crop (0,100,576,970), converted to sRGB, is raster. This source contains the pointer on the header, so the header is fully rebuilt with native text and Back; pointer and hover are omitted. Map callout, venue marker and partly visible Locate control are native editable elements where present. All remaining map place labels are part of public map artwork. The actual full-screen map viewport did not display a Google attribution; no visible attribution is removed and no attribution is fabricated. This is a static observed map state, not a claim of working geolocation or free-form map pan in the prototype. No map content cropped to hide the pointer and no synthetic replacement map.', body)

print('Built seven Food SVGs: list, hours, detail, tag search, image, map and panned map')
