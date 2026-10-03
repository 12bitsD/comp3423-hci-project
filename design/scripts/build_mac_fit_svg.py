"""Fit the existing desktop reference for nested prototype display, not native size."""
from pathlib import Path
r=Path(__file__).resolve().parents[1]/'polyulife'
x=(r/'mac-general.svg').read_text()
x=x.replace('width="1382" height="320" viewBox="0 0 1382 320"','width="576" height="133.372" viewBox="0 0 1382 320"',1)
x=x.replace('<title>Mac-only PolyULife General preferences — no setting change</title>','<title>Mac General — fitted prototype reference</title><desc>Existing native Mac reference reconstructed with editable vectors, uniformly fitted to576px width for nested prototype display. Native window size is1382x320, not576x133.372. No actual preference change. Original mac-general.svg retained.</desc>')
(r/'mac-general-overlay-fit.svg').write_text(x)
