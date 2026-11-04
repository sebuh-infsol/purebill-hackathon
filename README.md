# PureBill — field photo to invoice lines, with receipts

Solo hackathon submission. Everything in this repo was built **Oct 29 – Nov 4,
2026** (window: Oct 26 – Nov 4; deadline Wed Nov 4, 9pm ET). Nothing is
backdated; git history shows the work landing day by day.

## The demo in 60 seconds

A technician photographs a staged repair scene. The pipeline counts what's
in the photo against a pre-locked inventory, drafts invoice lines for human
review, and posts a sandbox invoice — with every step evidenced:

1. **Locked scene** — fake job Harbor Dental Studio / HB-1042, expected
   counts written *before* the run: 1 fan, 4 screws, 1 screwdriver, 1 cable.
2. **Capture receipt** — `6136224d-…`, 68,770 bytes, SHA-256 verified on
   readback (two earlier attempts preserved and marked superseded, not deleted).
3. **SAM 3.1 boxes** — whole-scene hits plus crop-then-segment passes that
   fixed two failures (corner magnets mistaken for screws; unboxed cable).
   Every box overlay-verified — see the infographic.
4. **Contributor describe** — `muse-spark-1.3-contributor` quotes the boxes
   back, confirms 7/7 by location, refuses specs it can't see (M3, 3-pin,
   labor time).
5. **Line items** — 4 proposed, 0 held, 3 spec flags; sandbox invoice 1038
   ($41.00) with rendered PDF and browser screenshot as proof. No accounting
   write outside the sandbox.

## Repo map

| Path | What it is |
|---|---|
| `docs/scene/INVENTORY.md` | Pre-run inventory, locked photo evidence, attempt history |
| `docs/scene/describe-result.md` | SAM boxes + verbatim describe output, incl. the two fixes |
| `docs/scene/line-items.md` | Review-gated proposal: 4 lines, 3 flags |
| `docs/scene/qb-sandbox.md` | Sandbox connection, writes log, proof links |
| `docs/scene/sam-boxes-infographic.jpg` | How SAM boxed the scene (real photo, real boxes) |
| `docs/scene/invoice-1038.pdf` | Rendered sandbox invoice |
| `docs/scene/invoice-1038-screenshot.png` | Browser view of posted invoice 1038 |
| `docs/spark-smoke-test.md` | Contributor-model endpoint/format proof |
| `docs/demo-draft.md` | Friday runbook: chain, Q&A, what to say when asked |
| `docs/architecture.md` | Hermes-agent × Muse Spark split and handoff |
| `docs/agent-handoff-infographic.jpg` | Handoff diagram + why-not-a-plugin |
| `scripts/describe_scene.py` | Reproduce the SAM + describe pass (needs your own keys) |

## Honesty notes (please hold us to these)

- The Oct 23 capture platform (ingest service, Android app, SAM/Qwen
  adapter) is **prior art in a separate private tree** — reused, never
  copied here, never claimed as new.
- The model is named as the **contributor variant**
  `muse-spark-1.3-contributor` throughout — never as standard `muse-spark-1.3`.
- The invoice is **posted, not a draft**: the QuickBooks API cannot create
  UI drafts. The repo says this explicitly; the demo does not pretend otherwise.
- All QuickBooks writes are **sandbox-only** (`Sandbox Company US b190`);
  production was never touched and its connection remains read-only.
- Failing paths are shown, not hidden: the magnet error, the null-fields
  capture, the typo'd customer, the refused invoice-draft substitution.

## Architecture — which Meta models, where each runs

- **SAM 3.1** (hosted Meta Responses API, `https://api.meta.ai/v1/responses`):
  runs at Meta; called from any machine with an API key. Takes the scene
  JPEG + a text concept, returns boxes + one-bit masks. Used whole-scene
  first, then on tray/unit crops for small objects.
- **`muse-spark-1.3-contributor`** (Meta, Contributor mode): invoked here via
  `muse exec --model muse-spark-1.3-contributor --image <jpeg>` with SAM
  boxes quoted in prompt text (no special schema). Runs wherever the Muse
  CLI runs with provider credentials; inference is hosted.
- **QuickBooks**: local MCP server (`intuit/quickbooks-online-mcp-server`,
  stdio) on the office box; production entry read-only, sandbox entry
  read/write. Held by the Hermes-agent, never by the model session.

## Run it yourself (judges)

Prereqs: Python 3 stdlib only, `muse` CLI, a Meta API key, your own photo.
No QuickBooks connection needed for this path.

```sh
cp .env.example .env   # put your key in .env (gitignored, never committed)
# 1. SAM boxes for any concept on your photo (prints boxes as JSON):
python3 scripts/describe_scene.py photo.jpg "loose screw"
# -> {"concept": "loose screw", "size": [1280, 960],
#     "boxes": [[308, 564, 332, 580], ...]}
# Overlay-verify every box before trusting it (see the magnet story in
# docs/scene/describe-result.md).

# 2. Contributor describe with those boxes (same format as the demo):
muse exec --model muse-spark-1.3-contributor --reasoning-effort low \
  --image photo.jpg \
  "SAM 3.1 returned boxes x1=308 y1=564 x2=332 y2=580 in 1280x960 space. \
  For each expected item state FOUND or NOT FOUND with its location, \
  quote the box coordinates where one exists, and list the rest as uncertainties."
```

QuickBooks is recorded evidence, not part of this path: `docs/scene/qb-sandbox.md`,
invoice 1038 PDF + browser screenshot, writes log. (Optional appendix: install
the MCP server above, complete Intuit's sandbox OAuth — localhost redirect
works for sandbox — and call `get_company_info`. Production stays read-only
by configuration and was never touched.)

## Verify it yourself

- `git log` — every commit Oct 29–Nov 4, no rewrites.
- Photo hashes: `sha256sum` any capture ID against its sidecar
  (`~/.purebill/capture-data/`, office disk) — receipts match.
- SAM boxes: coordinates in `describe-result.md` plot onto the locked photo;
  the overlays are reproducible from the logged calls.
- Invoice: sandbox company → Sales → Invoices → Doc 1038 (posted, unsent,
  unpaid), or read the PDF/screenshot in `docs/scene/`.

## Status

- [x] Repo created (Oct 29)
- [x] Staged scene locked pre-run, photo evidence hashed in
- [x] Spark contributor smoke test passed
- [x] SAM crop-then-segment: 7/7 boxed, overlays verified
- [x] Line items drafted review-gated; sandbox invoice posted
- [x] Friday demo draft + architecture docs written
- [ ] Submit before Wed Nov 4, 9pm ET
