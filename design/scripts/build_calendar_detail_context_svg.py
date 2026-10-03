"""Preserve the public holiday detail source for the Home/Week modal context."""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
DESIGN = ROOT / "design/polyulife"
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)

source = DESIGN / "calendar-holiday-detail.svg"
root = ET.parse(source).getroot()
root.find(f"{{{NS}}}desc").text += (
    " Caller-preserving context copy of the observed September26 public holiday. "
    "Figma swaps the existing month overlay to this detail and back; this is "
    "prototype implementation, not evidence of native overlay architecture. "
    "Transparent Back hit region is a prototype usability generalization. "
    "No other event or live calendar content is implemented."
)
back = root.find(f".//{{{NS}}}g[@id='Back']")
back.insert(0, ET.Element(f"{{{NS}}}rect", {
    "x": "8", "y": "32", "width": "52", "height": "56",
    "fill": "#FFFFFF", "fill-opacity": "0",
}))
output = DESIGN / "calendar-holiday-detail-context.svg"
ET.ElementTree(root).write(output, encoding="unicode")
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
metadata = {
    "source_svg": source.name,
    "source_sha256": digest(source),
    "source_evidence_id": "E-CALENDAR-EVENT",
    "output": output.name,
    "output_sha256": digest(output),
    "scope": "Public fixed holiday detail; editable approximate text and vectors.",
    "private_content": "none",
    "native_actions_added": False,
}
(DESIGN / "calendar-detail-context-assets.json").write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2) + "\n"
)
