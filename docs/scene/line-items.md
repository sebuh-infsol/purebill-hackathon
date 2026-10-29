# Line-item proposal — HB-1042 demo draft, 2026-10-29 (new work)

Status: **proposal only, review-gated. No accounting write.**
Source: `describe-result.md` (2 of 7 items box-confirmed, 5 uncertain).

## Demo catalog (defined today, demo-only — not a real price list)

| Catalog ID | Description              | Unit |
|------------|--------------------------|------|
| DEMO-LABOR-FAN | Intake fan replacement labor | per job (duration set at review, never from photo) |
| DEMO-PART-FAN180 | 120 mm intake fan unit | each |
| DEMO-PART-SCRM3 | M3 mounting screw | each |
| DEMO-PART-CBL3P | 3-pin fan power cable | each |

No rates, tax, or authorization decisions are included — those are
reviewer inputs, not model outputs.

## Proposed lines (from confirmed observations only)

1. **DEMO-LABOR-FAN × 1** — job note "Replace intake fan", HB-1042.
   Duration: **TBD at review**. A photo is not proof of labor time.
2. **DEMO-PART-FAN180 × 1** — intake-fan unit FOUND (SAM grille box
   `305,205,453,344` quoted in describe).
3. **DEMO-PART-SCRM3 × 4** — screw COUNT box-confirmed by
   crop-then-segment (4 interior boxes, overlay-verified; corner magnets
   excluded). Size/thread: **verify M3 at review** — not readable
   dark-on-dark. If the reviewer rejects M3, this line comes off.

4. **DEMO-PART-CBL3P × 1** — cable lead FOUND via fan-unit crop
   (`wire` box `244,376,289,407` on the lead, `connector` box
   `231,397,256,418` on the white body, both overlay-verified). Pin count:
   **verify 3-pin at review** — connector too small to resolve pins. If
   the reviewer rejects 3-pin, this line comes off.

## Review holds

None. All 7 items are box-confirmed by count/location. Open review flags:
labor duration, M3 thread, 3-pin count.

## Rule applied

The draft shows the refusal where it belongs: 4 lines proposed, 0 held,
3 spec flags. The locked inventory counts enter lines only where boxes
confirm them; the M3/3-pin/duration specs never enter unconfirmed.
