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

## Photo (locked demo capture)

- Request ID: `7d172bdc-5414-47e9-b4af-c45006f27c43`
- Photo SHA-256: `80fb319640915e7ca326483e79a53070fa5c1f36ef3168041ec5ca5d0b5a73b4`
  (verified readback from office disk Oct 29; matches sidecar receipt)
- Byte count: `67216` (matches sidecar receipt)
- Sidecar: `7d172bdc-5414-47e9-b4af-c45006f27c43.json`, captured
  `2026-10-29T21:33:36Z`
- Sidecar job fields: customer `Harbor Dentel Studio`, workOrder `HB-1042`,
  note `Replace intake fan`
- Framing check Oct 29: same 7 scene items, no edge clutter this time
  (tray with 4 screws, fan unit with cable connector, screwdriver).

### Evidence history (all attempts preserved, none deleted)

- `3ecf896d-a263-4a4e-9fef-a9d66c07bc30` (73,022 bytes, job fields null):
  **superseded** by re-capture below. Kept on disk; not demo evidence.
- `7d172bdc-5414-47e9-b4af-c45006f27c43`: **the locked demo photo.**

### Deviations from plan (recorded honestly, scene counts unaffected)

- Operator typo frozen in the sidecar: customer reads `Harbor Dentel
  Studio`, not `Harbor Dental Studio`. The record is what it is — the demo
  quotes the actual value and notes the intended spelling; no silent fix.

A passing demo describe must report counts matching the table above
(1 fan, 4 screws, 1 screwdriver, 1 cable) or list the mismatch as an
uncertainty — never invent matching counts.
