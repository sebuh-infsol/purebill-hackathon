# Demo describe result — locked scene, 2026-10-29 (new work)

## Provenance

- Photo: `6136224d-2355-455a-a72b-10dfc9644d28.jpg`
  (SHA-256 `cb75e804ff2203ee79836f344850ccdb5088127f1c20b9b0fad7e8ae173e6af6`)
- SAM 3.1 (hosted, one call per concept, ~1 s each). Validated boxes used:
  - fan grille: `x1=305 y1=205 x2=453 y2=344` (1280x960 space) — correct
  - screwdriver: `x1=831 y1=489 x2=917 y2=843` — correct
- SAM returned no true boxes for the 4 loose screws (its 4 "screws" boxes
  hit the tray's corner fasteners instead — rejected on overlay check) or
  the power cable. Overlay check saved as evidence of the rejection.
- Describe model: `muse-spark-1.3-contributor` (contributor variant, not
  standard), low effort, JPEG + boxes-in-prompt-text (proven format).

## Result (verbatim)

HB-1042 staging check in 1280x960 space:

- 1 intake-fan unit: FOUND. Upper-center black rectangular unit on table.
  SAM grille box only: x1=305 y1=205 x2=453 y2=344.
- 1 screwdriver: FOUND. Right side of table, vertical.
  SAM box: x1=831 y1=489 x2=917 y2=843.
- 4 loose M3 screws in the tray: Tray FOUND lower-left. Item as specified
  NOT FOUND. Dark tray interior shows small dark objects, but no SAM box exists.
- 1 fan power cable with 3-pin connector: NOT FOUND as specified. Small wire
  bundle with white connector visible at left edge of fan unit, but no SAM
  box exists.

Uncertainties - cannot determine from this photo:

- Screw count. Do not confirm 4.
- Screw size / thread. Do not confirm M3.
- Screw location in tray vs tray molding marks.
- Cable pin count. Do not confirm 3-pin.
- Connector type and wire count.
- Full extent of fan unit. SAM box covers grille only, not whole unit.

## Reading for the line-item step

2 of 7 items are box-confirmed (fan unit, screwdriver). 5 are
human-review items: the model refused to confirm counts/specs it cannot
see. A Quickerbooks line-item draft must propose lines only for confirmed
items and flag the rest — never invent the 4×/M3/3-pin values from the
inventory. If the Friday demo needs all-7 confirmed, the scene needs a
closer second photo, not a forced read.
