"""Copy observed public date samples into the Home/Week overlay context."""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
DESIGN = ROOT / "design/polyulife"
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
records = []
for date, evidence in [
    ("oct1", "E-CALENDAR-OCT1"),
    ("sep1", "E-CALENDAR-SEP1"),
    ("sep28", "E-CALENDAR-ACAD-EMPTY"),
]:
    source = DESIGN / f"calendar-{date}.svg"
    root = ET.parse(source).getroot()
    root.find(f"{{{NS}}}desc").text += (
        " Caller-preserving public date context copy. Only the historical "
        "academic-only state is reconstructed. Observed next-month selects "
        "October1, previous-month selects September1; it does not restore "
        "September26. Figma navigation configured separately; no arbitrary "
        "dates, live data, semester boundaries or unobserved details."
    )
    output = DESIGN / f"calendar-date-{date}-context.svg"
    ET.ElementTree(root).write(output, encoding="unicode")
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    records.append({
        "date": date, "source_svg": source.name,
        "source_sha256": digest(source), "source_evidence_id": evidence,
        "output": output.name, "output_sha256": digest(output),
        "scope": "Public fixed academic-only date; editable approximate text/vector.",
    })
(DESIGN / "calendar-date-context-assets.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2) + "\n"
)
