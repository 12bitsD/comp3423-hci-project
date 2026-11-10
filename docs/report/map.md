# 4.5 Map — from “a pin on a map” to “which floor, then which door”

Responsible member: XueBoChen (Accessibility & Evaluation Lead)

This file mirrors the Map subsection of the group report. Screenshots are in the
report itself (Fig. 1a–1c, Fig. 2a–2h); the Figma file is the source of truth for
the prototype.

## 4.5.1 What we observed

In the shipping PolyULife Map, a student who wants the nearest toilet has to
answer three questions the interface never asks: which building, which floor,
which room.

| No. | Observation |
| --- | --- |
| O1 | Category encoding is lost. Every facility type uses the same pink droplet; with three filters active the map rendered roughly forty identical pins. |
| O2 | The list adds no information. Each row repeats the building name twice: “Toilet (Core H)”, then “Core H”, then “Core H” again. |
| O3 | The floor is never shown. The detail screen offers a building-level 3-D view in which only rooftops are visible. |
| O4 | Filtering is invisible in the list. Selecting a category updates the map but not the list, so the two views disagree about the current result set. |

## 4.5.2 Principles violated

| Observation | Violated principle |
| --- | --- |
| O1, O4 | Visibility of system status (Nielsen #1) |
| O1, O2 | Recognition rather than recall (#6) |
| O3 | Match between the system and the real world (#2) |

## 4.5.3 The redesign

The redesign has eight screens (Fig. 2a–2g) and two start-point overlays
(Fig. 2h). The flow rests on one assumption: someone looking for a toilet already
knows which building they are standing in, so the screens go building, then
floor, then room.

Information is revealed in the same order (progressive disclosure, Nielsen 2006).
The bottom sheet opens only when the list is actually needed.

- **F0, campus map.** Buildings are cards sorted by distance, and every category
  chip shows how many results it has (“Toilets 12”, nearest 10 m). We did not try
  to replace outdoor routing: Google Maps already does that, and the shipping app
  already opens it from “View on Google Maps”. Our scope was the part after the
  entrance.
- **F1, arrival floor.** Entering on P/F shows “No toilets on this level. The
  nearest ones are on 3/F”. The 3F button carries a count badge, and the only
  primary action is “Show me 3/F”.
- **F2, floor plan with results.** Each category keeps an icon next to its colour,
  so the map does not depend on colour alone (W3C, 2023). The sheet lists the two
  nearest results and ends with “3 more on this floor”.
- **F2b, two categories on.** Both filters apply to the map and to the list at the
  same time, so the two halves of the screen cannot disagree.
- **F3, expanded sheet.** The map stays visible and the rows are sorted by
  distance.
- **F4, detail.** Floor, room, walking time, step-free access, and the first three
  steps of the route.
- **F5, turn by turn.** The same plan, with the walk cut into three named steps and
  only the current step highlighted.
- **F1-Start and F2-Start, start-point overlays.** They list the entrance or the
  nearby rooms and close by tapping the scrim, dragging the 24 px handle, or
  picking a row.

## 4.5.4 Design decisions

| Decision | Why |
| --- | --- |
| Map and list are complementary | The map answers “where”; the list answers “which one, how far”. |
| The empty state names the next step | On P/F the screen answers what happened, where the results are, and what to do next. |
| The start point is visible and adjustable | GPS cannot resolve a floor and the campus publishes no indoor positioning, so the blue dot is a start point the user confirms, not a claim of live position. |
| State is encoded more than once | Floors differ by fill, weight, text colour and a count badge; categories keep an icon as well as a colour. |
| Disclosure is staged | Overview, then detail, then route. |

## 4.5.5 The key decision: the floor is already inside the room code

“W305” already means Industrial Centre, 3/F, room 05. The floor is therefore in
the string the app already prints, and the redesign only has to read it
(W305 → 3/F). No new dataset, no 3-D model, no asking students to photograph
corridors.

| Option | Cost | Answers “which floor?” | Verdict |
| --- | --- | --- | --- |
| 3-D model of the campus | 3–5 days | No — still a top-down view | Rejected |
| Photograph every entrance | Half a day | Partially | Rejected |
| Floor plan + floor switcher | 2–3 hours | Yes | Chosen |
| AR indoor navigation | Not achievable | Yes | Future work |

The blue dot follows the same logic. It is a start point the user can change
(“Start: Lift 2, 3/F”), not a claim about where they are: the campus publishes no
indoor positioning, and GPS cannot tell you the floor, so a “you are here” label
would be a promise we cannot keep.

## 4.5.6 Scope and limitation

The prototype is a design demonstration, not a working application. The
start-point sheet does not recompute the route, the search field is shown as
“coming soon”, and “Use current location” is not wired to any positioning
service. The turn-by-turn screen is a static walkthrough rather than live
navigation, and its first step assumes the user arrives by lift.

The worked example is the Industrial Centre (IC), because it is the only PolyU
building for which official per-floor plans are publicly available. Core
buildings share the same information structure but publish no floor plans, so the
design is demonstrated on IC.

## References (Map subsection)

- Nielsen, J. (1994). Heuristic evaluation. In *Usability Inspection Methods*. Wiley.
- Nielsen, J. (2006). Progressive disclosure. Nielsen Norman Group.
- W3C (2023). Web Content Accessibility Guidelines (WCAG) 2.2.
