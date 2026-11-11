# Calendar redesign — HCI rationale and implementation record

Date: 2026-11-11  
Owner: B / LinHao — Calendar 课表与日历  
Scope: find a class/event on a specified date → filter → view details → return; Exam empty state must offer a recovery path.

## What was optimized

The redesign keeps the observed “month grid + events for the selected day” model but changes the parts that hid state or made recovery difficult. These are **theory-driven design decisions, not measured usability results**. No new participant data was collected for this iteration.

| Observed risk in the old flow | Redesign decision | HCI theory / citation |
| --- | --- | --- |
| Category filtering was hidden behind a small icon; the current filter was not obvious after returning. | A visible **Filter** button (96×44), an active filter chip, selected date, and result count remain on the results screen. **Clear** is available beside the applied filter. | Nielsen #1, **visibility of system status**; Norman’s **feedback**. [1][2] |
| Users had to remember category names and whether a draft had been applied. | Category names, selected state, and a short draft message are visible in the sheet; results explicitly say `1 event on this date` or `0 events on this date`. | Norman, **recognition rather than recall**. [2] |
| Small filter targets and an ambiguous apply path increased motor and decision cost. | Filter rows are 50 px high with full-width hit areas; the main Filter target is 44 px high; the entire class card is clickable. Apply is a single primary action, with **Reset** and **Close** also available. | **Fitts’ law**: larger/nearer targets reduce acquisition time; Nielsen #7, **flexibility and efficiency of use**. [3][1] |
| Draft/apply/cancel behavior was hard to infer, risking unintended changes. | The sheet says `Draft selection is kept until you apply or close`; **Apply / Reset / Close** are separate actions, and the applied filter can be cleared. | Nielsen #3, **user control and freedom**; #5, **error prevention**; Shneiderman, **easy reversal of actions**. [1][4] |
| The old Exam empty state used a generic instruction to enable all filters, without naming the actual empty condition or offering a direct recovery. | The new state says **No exams on this date**, names the selected date, and offers **Show all events** plus **Clear**; Filter remains available. | Nielsen #9, **help users recognize, diagnose, and recover from errors**; Norman’s actionable feedback. [1][2] |
| Repeated categories and generic system wording competed with the task. | Only the selected day and relevant events lead the hierarchy; wording uses `Class`, `Exam`, `No exams on this date`, and `Back to classes`. | Nielsen #4, **consistency and standards**; #8, **aesthetic and minimalist design**; #2, **match the system to the real world**. [1] |
| Calendar used a different size and navigation treatment from the other redesign modules. | All six frames are **390×844**, use the same green accent, card geometry, back behavior, and DEMO marking as the team redesign. | Nielsen #4, **consistency and standards**; Shneiderman, **strive for consistency**. [1][4] |

## Frames and prototype links

Main Figma file: `ulBuuteCRdzdBsHAaiqyUr`, page `02 · Team Redesign`, section `Calendar` (`1108:17`).

| Frame | Figma node | Main outgoing links |
| --- | --- | --- |
| C01 · Calendar — All | `1212-128` | FilterButton → C02; ClassCard → C04; HomeBack / NavHome → H00 |
| C02 · Calendar — Filter · Class | `1212-385` | ApplyFilter → C03; FilterOption_Exam → C05; CloseFilter / ResetFilter → C01 |
| C03 · Calendar — Class only | `1212-644` | ClassCard → C04; FilterButton → C02; ClearFilter → C01; HomeBack / NavHome → H00 |
| C04 · Calendar — Class detail | `1212-820` | HomeBack / BackToClasses → C03 |
| C05 · Calendar — Filter · Exam | `1212-998` | ApplyFilter → C06; FilterOption_Class → C02; CloseFilter / ResetFilter → C01 |
| C06 · Calendar — Exam empty | `1212-1254` | ShowAllEvents / ClearFilter → C01; FilterButton → C05; HomeBack / NavHome → H00 |

Shared entry: **H00 `NavCalendar` → C01**.  
Flow starting point: **C01**, flow title **Calendar · All**.

## Evidence and verification boundary

Verified in this run:

- Six SVG sources were generated locally and rendered in headless Chrome; the six-screen contact sheet was visually checked (`docs/evaluation/assets/calendar-redesign.png`).
- All six frames were imported into the main Figma file at 390×844, into the existing Calendar section.
- Imported date text is still a Figma **Text** layer, not an outlined bitmap/vector-only label.
- The links listed above were set and read back through Figma’s Prototype interaction editor.
- No user research, Maze responses, or usability-success claims are included.

Still required before final submission:

- A human should Present-walk `H00 → Calendar → Filter → Class → detail → back`, then `Filter → Exam → empty → Show all events`. Automated canvas clicking was not reliable in this environment, so this is **not claimed as completed**.
- Calendar should receive its own real-participant test. A suitable two-task Maze follow-up is: (1) find and inspect the Oct 2 class, then return; (2) filter to Exam and recover to all events. Five or more real participants should be recruited; no mock data may be submitted.

## Sources

- Editable generator: `design/scripts/build_calendar_redesign.py`
- Six editable SVGs: `design/polyulife/redesign-calendar/`
- Preview: `docs/evaluation/assets/calendar-redesign.png`

## HCI references

[1] Nielsen, J. (1994). *Usability Engineering*. Morgan Kaufmann.  
[2] Norman, D. A. (2013). *The Design of Everyday Things: Revised and Expanded*. Basic Books.  
[3] Fitts, P. M. (1954). The information capacity of the human motor system in controlling the amplitude of movement. *Journal of Experimental Psychology, 47*(6), 381–391.  
[4] Shneiderman, B. (2016). *Designing the User Interface: Strategies for Effective Human-Computer Interaction* (6th ed.). Pearson.
