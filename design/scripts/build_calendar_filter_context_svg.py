"""Copy public filter samples for the academic-only September28 context."""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
DESIGN = ROOT / "design/polyulife"
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
records = []
for selection, evidence in [
    ("acad", "E-CALENDAR-FILTER-PERSIST"),
    ("all", "E-CALENDAR-FILTER-ALL"),
    ("none", "E-CALENDAR-FILTER-NONE"),
]:
    source = DESIGN / f"calendar-filter-{selection}.svg"
    root = ET.parse(source).getroot()
    root.find(f"{{{NS}}}desc").text += (
        " Caller-preserving September28 academic-only context. Checked boxes "
        "are draft filter selection, not proof that filters have been applied. "
        "All/None are public panel samples composited over the academic-only "
        "background; only the academic persisted state has full native pixels. "
        "Figma navigation is configured separately. Apply All/None results, "
        "individual Class/Exam/Payment toggles and native X cancellation remain "
        "unverified. Prototype X is an explicitly inferred recovery."
    )
    output = DESIGN / f"calendar-filter-{selection}-context.svg"
    ET.ElementTree(root).write(output, encoding="unicode")
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    records.append({
        "selection": selection, "source_svg": source.name,
        "source_sha256": digest(source), "source_evidence_id": evidence,
        "output": output.name, "output_sha256": digest(output),
        "scope": "Persisted academic panel or composite public selection sample; approximate text/vector.",
        "full_native_background_verified": selection == "acad",
    })
(DESIGN / "calendar-filter-context-assets.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2) + "\n"
)
