# Locked staged scene — pre-run inventory

Locked: **2026-10-29** (before any photo or model run).
This exact scene is reused for the Friday demo draft. No substitutions.

## Fake job (distinct from the Oct 23 real capture)

- Customer: **Harbor Dental Studio** (fictional; not Infsol, Inc.)
- Work order: **HB-1042** (not `0001`)
- Technician note: **"Replace intake fan"** (not `Fix GPU`)
- Request ID for demo run: `demo-hb1042-intake-fan` (new; never reuse `29b14339-…`)

## Scene layout

White desk, parts laid out in a single row, left to right. Nothing else in frame.

## Expected counts (written before the run — the demo checks against these)

| # | Item | Expected count |
|---|------|----------------|
| 1 | 120 mm intake fan (front, label up) | 1 |
| 2 | M3 mounting screws in tray (loose, countable) | 4 |
| 3 | Phillips screwdriver (handle left, tip right) | 1 |
| 4 | Fan power cable with 3-pin connector (coiled beside fan) | 1 |

Total countable items: **7** (1 + 4 + 1 + 1).

## Photo

- [x] Photo taken of the scene above (original bytes preserved office-side)
- Request ID (actual, as captured): `3ecf896d-a263-4a4e-9fef-a9d66c07bc30`
  (planned `demo-hb1042-intake-fan` was not used at capture time; this UUID is
  the frozen record — no re-upload under a second ID)
- Photo SHA-256: `c4d186e7ca862afe2a2bfb89d9bc43fa2213181c2b09623ea2d7902c7d59e1f7`
  (verified readback from office disk Oct 29; matches sidecar receipt)
- Byte count: `73022` (matches sidecar receipt)
- Sidecar: `3ecf896d-a263-4a4e-9fef-a9d66c07bc30.json`, captured
  `2026-10-29T21:30:09Z`

### Deviations from plan (recorded honestly, scene counts unaffected)

- Job fields at capture are `null` (customer/workOrder/note not filled on the
  phone). The HB-1042 job binding lives in this repo (section above), not in
  the capture sidecar. Decide before the demo: keep repo-side binding, or
  re-capture with fields filled.
- Two unplanned items at frame edges: small plastic bag (top-right) and an
  unidentified object sliver (bottom-left). Countable scene items are still
  exactly the 7 above; a passing describe must not count edge clutter, and
  must list anything ambiguous as uncertainty.

A passing demo describe must report counts matching the table above
(1 fan, 4 screws, 1 screwdriver, 1 cable) or list the mismatch as an
uncertainty — never invent matching counts.
