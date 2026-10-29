# Friday Demo Draft — HB-1042 runbook (new work, 2026-10-29)

One staged job, end to end: photo → evidence → SAM boxes → contributor
describe → review-gated line items. Every claim below links to a hash,
a box, or a named uncertainty. Nothing is asserted without one.

## 0. What the demo is (30-second version)

A field tech photographs a staged repair scene; the office pipeline
counts what's in the photo against a pre-locked inventory and drafts
invoice lines for human review — confirming 7 of 7 items by location,
refusing the 3 specs it cannot see, and never writing to accounting.

## 1. The locked scene

- Fake job: **Harbor Dental Studio / HB-1042 / "Replace intake fan"**
  (`docs/scene/INVENTORY.md`, locked pre-run Oct 29).
- Expected counts: 1 fan unit, 4 loose screws, 1 screwdriver, 1 cable (7).
- Layout: fan unit top, tray with 4 screws lower-left, screwdriver right,
  short cable lead at the fan's bottom-left (inventory corrected Oct 29 —
  no coiled cable exists).

## 2. Capture receipt (show this)

- Request `6136224d-2355-455a-a72b-10dfc9644d28`, 68,770 bytes,
  SHA-256 `cb75e804ff2203ee79836f344850ccdb5088127f1c20b9b0fad7e8ae173e6af6`
  — read back from office disk, matches sidecar.
- Two earlier attempts preserved on disk and marked superseded (null
  fields; `Dentel` typo). Each capture is one evidence record; retries
  never overwrite.
- Job fields in the sidecar are exact: no silent fixes anywhere.

## 3. SAM boxes (show the overlays)

| Item | Concept that hit | Box (1280x960) | Check |
|---|---|---|---|
| Fan grille | `fan` | 305,205,453,344 | correct |
| Screwdriver | `screwdriver` | 831,489,917,843 | correct |
| Tray | `plastic tray` (`tray`: 0) | 179,464,630,826 | correct |
| 4 screws | `screw` on tray crop | 4 interior boxes | correct, magnets excluded |
| Cable lead | `wire` on unit crop | 244,376,289,407 | correct, on the lead |
| Connector | `connector` | 231,397,256,418 | correct, on white body |

Tell the magnet story: whole-scene `screws` hit the 4 lid-closure magnets
instead of the screws — caught by overlay, fixed by crop-then-segment
(tray box → crop → `screw` → 4 interior boxes, 4/4 expected). Failed
wordings on record: `tray`, `loose screw`, `metal screw` (corners only),
`cable`, `container`, `lid`.

## 4. Contributor describe (show the quote-back)

- Model: `muse-spark-1.3-contributor` (contributor variant, not standard),
  JPEG + boxes in prompt text, low effort — the smoke-tested format.
- Output quoted the SAM boxes back, confirmed 7 of 7 by location, and
  refused screw count/size and pin count until the crop pass supplied
  boxes. Full text in `docs/scene/describe-result.md`.

## 5. Line items (show the gate)

- Catalog: demo-only (`DEMO-` IDs, no rates), in `docs/scene/line-items.md`.
- 4 lines proposed: labor (duration TBD at review), fan ×1, screws ×4
  (count boxed, M3 flagged), cable ×1 (lead boxed, 3-pin flagged).
- 0 held, 3 spec flags: duration, M3, 3-pin. The draft's honesty feature
  is the flags, not the lines.
- **No accounting write in the demo.** Write tests go to a sandbox
  company first; production needs separate approval.

## 6. What to say when asked

- "Why not just trust the photo?" — A photo is supporting evidence, not
  proof of duration, price, or repair. The pipeline counts locations, a
  human sets specs and rates.
- "What if SAM is wrong?" — The magnet error is in the deck. Overlays are
  mandatory; unvalidated boxes never enter lines.
- "Is this the standard model?" — No. `muse-spark-1.3-contributor`,
  Contributor mode, named as such throughout.
- "Where's the Oct 23 platform?" — Prior art, separate private tree, not
  in this repo. This repo is Oct 29+ work only.
