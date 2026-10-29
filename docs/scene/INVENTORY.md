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

- Request ID: `6136224d-2355-455a-a72b-10dfc9644d28`
- Photo SHA-256: `cb75e804ff2203ee79836f344850ccdb5088127f1c20b9b0fad7e8ae173e6af6`
  (verified readback from office disk Oct 29; matches sidecar receipt)
- Byte count: `68770` (matches sidecar receipt)
- Sidecar: `6136224d-2355-455a-a72b-10dfc9644d28.json`, captured
  `2026-10-29T21:35:17Z`
- Sidecar job fields: customer `Harbor Dental Studio`, workOrder `HB-1042`,
  note `Replace intake fan` — all exact, no deviations
- Framing check Oct 29: same 7 scene items (tray with 4 screws, fan unit
  with cable connector, screwdriver), no edge clutter.

### Evidence history (all attempts preserved, none deleted)

- `3ecf896d-a263-4a4e-9fef-a9d66c07bc30` (73,022 bytes, job fields null):
  **superseded**. Kept on disk; not demo evidence.
- `7d172bdc-5414-47e9-b4af-c45006f27c43` (67,216 bytes, customer typo
  `Dentel`): **superseded**. Kept on disk; not demo evidence.
- `6136224d-2355-455a-a72b-10dfc9644d28`: **the locked demo photo.**

A passing demo describe must report counts matching the table above
(1 fan, 4 screws, 1 screwdriver, 1 cable) or list the mismatch as an
uncertainty — never invent matching counts.
