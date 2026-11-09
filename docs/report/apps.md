# Apps and Service Discovery — Report-ready Subsection

Status: design and implementation draft, 2026-11-09. Real-participant results and the final Figma link remain to be inserted. The wording below deliberately does not claim an improvement that has not been evaluated.

## User task and observed problem

The Apps module supports students who need to locate a campus service without necessarily knowing its category. The core task selected for this redesign is to find the Visitor Registration System (VRS), understand its purpose, open the official service, and return to the service list. VRS allows a user to request a QR code for guests to access campus.

The original interface was observed in PolyULife 3.0.0 on 28 September 2026. In one recorded sequence, the user selected Job and then dragged the horizontal category bar to reveal earlier categories. The content still showed PolyU Job Board and the accessibility state still identified Job as selected, but the selected Job label was no longer visible. This establishes a mismatch between the current result state and the visible category controls. It does **not**, by itself, establish how often users become confused or fail the task. We therefore treated it as a evidence-based design hypothesis for subsequent testing rather than as a quantified usability defect.

![Before and after comparison of category visibility](../../prototypes/apps-studio/exports/figure-01-category-status.png)

*Figure X. In the observed interface, the active Job label can leave the visible category bar. The proposed interface keeps the selected chip, result heading, current-filter label, and result count visible together. Source: project evidence `apps-171722-category-bar-dragged.png`; redesign dated 9 November 2026.*

## Redesign and rationale

The redesigned service directory provides two complementary routes. Users can browse a wrapped set of category chips or search by a service name and related task words. A persistent result summary names the active category and the number of matches. This response follows **visibility of system status**: the interface communicates the current filter in more than one visible location rather than requiring users to infer it from the content. Search supports **recognition rather than recall** by letting users enter a partial name or task term and then recognise the appropriate service in a short result list. Search does not remove browsing, so users who do not know a service name retain an alternative.

The VRS detail page makes the external transition explicit before the user continues. It states the service purpose, the possible NetID requirement, and the official destination (`fmovrs.polyu.edu.hk/vrs`). A loading page identifies the service being opened and offers cancellation. The external sign-in preview uses disabled demonstration fields and collects no credentials. Back and close actions restore the previous list state, supporting **user control and freedom** and preventing an external detour from discarding the user’s context.

![Before and after comparison of the VRS detail and external handoff](../../prototypes/apps-studio/exports/figure-02-external-handoff.png)

*Figure X. The original VRS detail and the proposed detail page. The redesign explains the service, possible authentication requirement, and official destination before the external transition. The observed link worked; the redesign addresses handoff clarity rather than claiming to repair a broken link.*

## Prototype and evaluation plan

The interactive design contains eight principal states: common home, all services, Campus results, persistent Job state, VRS details, external loading, official sign-in handoff, and no-results recovery. The no-results state names the unsuccessful query and offers Clear search and category reset actions. Interactive targets are at least 44 px, selected states use text as well as colour, and the design uses the shared Fresh Campus typography and colour tokens.

The Maze task will ask at least five real target users to find the service for requesting a guest campus QR code, review what is required, open the official service page, and return to the service list. The wording does not reveal “Apps”, “search”, “Campus”, or “VRS” as a click path. We will record direct and indirect success, completion time, wrong turns, and participant comments. A short post-task question will ask participants to identify the active filter and what they expect to happen before external sign-in. The frozen test version and any subsequent changes will be dated and linked.

**Results and iteration — to be completed after real testing.** Insert the participant count, raw Maze export/dashboard reference, per-task outcomes, representative quotations, and the specific design changes made in response. Agent walkthroughs verify only that the implemented links and state restoration work; they are not usability findings and must not be reported as participant evidence.

## Candidate references for the related-work coordinator

- Nielsen, J. (1994). *Usability Engineering*. Morgan Kaufmann. Source for the visibility, recognition, and user-control heuristics used in this design analysis.
- Adar, E., Teevan, J., & Dumais, S. T. (2008). Large scale analysis of web revisitation patterns. *Proceedings of CHI 2008*, 1197–1206. https://doi.org/10.1145/1357054.1357241. Candidate context for revisitation and search-assisted recognition; the related-work author should check relevance and synthesis rather than adding it as an isolated summary.
