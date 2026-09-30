"""Prepare observed Assistant transient states; does not import or wire Figma.

Requires Pillow. Uses only already reviewed public native screenshots/assets.
"""
from pathlib import Path
import base64
import copy
import hashlib
import json
import xml.etree.ElementTree as ET
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
DESIGN = ROOT / "design/polyulife"
NATIVE = ROOT / "evidence/2026-09-28-full-audit"
SVG = "http://www.w3.org/2000/svg"
XLINK = "http://www.w3.org/1999/xlink"
ET.register_namespace("", SVG)
ET.register_namespace("xlink", XLINK)
ns = {"s": SVG}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def group(root, name):
    return root.find(f'.//s:g[@id="{name}"]', ns)


def metadata(root, title, description):
    root.find("s:title", ns).text = title
    root.find("s:desc", ns).text = description


records = []


def write(root, filename, state, evidence, screenshot, base, details):
    output = DESIGN / filename
    ET.ElementTree(root).write(output, encoding="unicode")
    records.append({
        "state_id": state,
        "source_evidence_ids": [evidence],
        "native_screenshot": "../../evidence/2026-09-28-full-audit/" + screenshot,
        "native_screenshot_sha256": digest(NATIVE / screenshot),
        "base_svg": base,
        "base_svg_sha256": digest(DESIGN / base),
        "output": filename,
        "output_sha256": digest(output),
        "frame_size": [576, 970],
        "status": "prepared_not_imported_not_replayed",
        "details": details,
    })


detail_name = "virtual-assistant-detail.svg"
before = ET.parse(DESIGN / detail_name).getroot()
page = group(before, "PageContent")
page.remove(group(before, "HeroArtwork"))
page.remove(group(before, "ExpandImage"))
# Native before-image title baselines approx.152/188 versus loaded355/391.
# This is an observed layout shift, not a measured loading duration.
group(before, "VirtualAssistantBody").set("transform", "translate(0 -203)")
metadata(before, "Virtual Assistant — before hero appears",
         "Editable approximation of E-ASSISTANT-BEFORE-HERO, public native screenshot "
         "virtual-assistant-154604-before-hero.png. Hero/expand group absent; article "
         "moved upward203px against loaded source baselines. Native layout shift "
         "observed, duration unknown. Fonts/icons remain approximate; captured "
         "cursor/halo omitted. Prepared source only, not imported/wired/replayed.")
write(before, "virtual-assistant-before-hero.svg", "S-ASSISTANT-BEFORE-HERO",
      "E-ASSISTANT-BEFORE-HERO", "virtual-assistant-154604-before-hero.png", detail_name,
      "Article position before hero appears; no invented reserved image space or spinner.")

welcome_name = "virtual-assistant-welcome.svg"
template = ET.parse(DESIGN / welcome_name).getroot()
logo_source = NATIVE / "virtual-assistant-154628-web-loading.png"
logo_crop = (261, 533, 317, 591)
logo_path = DESIGN / "assets/virtual-assistant-loading-mark.png"
Image.open(logo_source).convert("RGB").crop(logo_crop).save(logo_path)
for state, evidence, screenshot, filename, loading in [
    ("S-ASSISTANT-WEB-LOADING", "E-ASSISTANT-WEB-LOADING",
     "virtual-assistant-154628-web-loading.png", "virtual-assistant-web-loading.svg", True),
    ("S-ASSISTANT-WEB-BLANK", "E-ASSISTANT-WEB-BLANK",
     "virtual-assistant-154746-web-blank.png", "virtual-assistant-web-blank.svg", False),
]:
    root = copy.deepcopy(template)
    embedded = group(root, "EmbeddedBrowser")
    old = group(root, "ThirdPartyWebContent")
    index = list(embedded).index(old)
    embedded.remove(old)
    content = ET.Element(f"{{{SVG}}}g", {"id": "ThirdPartyWebContent"})
    ET.SubElement(content, f"{{{SVG}}}rect", {
        "x": "9", "y": "152", "width": "560", "height": "726", "fill": "#FFFFFF"})
    if loading:
        # Native loading chrome has no title. The captured loading mark is static.
        header = group(root, "WebHeader")
        for child in list(header):
            if child.tag == f"{{{SVG}}}text":
                header.remove(child)
        ET.SubElement(content, f"{{{SVG}}}image", {
            "x": "261", "y": "533", "width": "56", "height": "58",
            f"{{{XLINK}}}href": "data:image/png;base64," + base64.b64encode(logo_path.read_bytes()).decode(),
        })
    embedded.insert(index, content)
    metadata(root, "Virtual Assistant — " + ("web loading" if loading else "unresolved blank web"),
             f"Editable browser chrome approximation of {evidence}, source {screenshot}. "
             + ("Static public loading mark crop261,533,317,591; title blank as captured. "
                if loading else "Blank content after AX focus attempt; root cause unknown. "
                "Do not implement an input click causing blank as established product behavior. ")
             + "No input field/messages added. Fonts/icons approximate; cursor/halo omitted. "
             "Prepared source only, not imported/wired/replayed. No measured latency.")
    write(root, filename, state, evidence, screenshot, welcome_name,
          "Intermediate loading source, no duration established." if loading else
          "Unresolved blank reference; close source confirmed via native AX only; causal trigger not modeled.")

manifest = {
    "kind": "assistant_transient_source_preparation",
    "status": "prepared_not_imported_not_replayed",
    "records": records,
    "loading_mark": {
        "file": "assets/virtual-assistant-loading-mark.png",
        "sha256": digest(logo_path),
        "dimensions": [56, 58],
        "source_evidence_id": "E-ASSISTANT-WEB-LOADING",
        "source_sha256": digest(logo_source),
        "crop_xyxy": list(logo_crop),
        "scope": "Static native public loading artwork only; no spinner timing inferred.",
    },
}
(DESIGN / "virtual-assistant-transient-assets.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
