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

## Addendum — crop-then-segment screw count, 2026-10-29 (pass)

Whole-scene "screws" had hit the tray's corner magnets (lid-closure magnets,
not screws). Fix: SAM `plastic tray` box `[179,464,630,826]` (concept `tray`
returned nothing; `plastic tray` hit), cropped with 10 px padding, re-ran
screw concepts on the crop:

- `screw`: 8 boxes — 4 corner magnets (rejected, same as before) + 4
  interior boxes, all overlay-verified on the loose screws:
  `[308,564,332,580]`, `[342,563,358,587]`, `[388,589,414,602]`,
  `[430,600,455,614]` (1280x960 space).
- `metal screw`: only the 4 corners. `loose screw`: 0.

Screw count is now box-confirmed: **4 of 4 expected**. Size/thread (M3)
remains unconfirmed — dark-on-dark, no spec readable.

## Addendum 2 — cable lead via fan-unit crop, 2026-10-29 (pass)

Inventory corrected same day: no beside-fan coil exists; the cable is a
short (~0.5 in) lead exiting the bottom-left of the fan unit. SAM on the
fan-unit crop (`black box` box `[221,179,825,477]` + 10 px padding):

- `wire`: `[244,376,289,407]` — overlay-verified on the red/black lead.
- `connector` and `white connector`: `[231,397,256,418]` — overlay-verified
  on the white connector body. `cable`: 0.

Cable lead is box-confirmed (1 lead, connector visible). Pin count (3-pin)
remains unconfirmed — connector too small to resolve pins.

## Reading for the line-item step

All 7 items are box-confirmed by count/location (fan unit, screwdriver,
4 screws, 1 cable lead). Remaining unconfirmed specs: screw size/thread
(M3), cable pin count (3-pin). A Quickerbooks line-item draft must propose
lines only for confirmed items and flag specs — never invent the M3/3-pin
specs from the inventory. If the Friday demo needs spec-level certainty,
that takes a closer second photo, not a forced read.
