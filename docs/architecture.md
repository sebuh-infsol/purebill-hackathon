# Hermes-agent × Muse Spark — how they interact (new work)

Two agents, one demo, split by capability. Nothing crosses the boundary
except reviewed files and explicit instructions.

## Roles

**Muse Spark — this session (Contributor mode, `muse-spark-1.3-contributor`)**
- Staged the scene, locked the pre-run inventory, verified photo hashes.
- Ran SAM 3.1 segmentation directly (Meta Responses API): whole-scene
  concepts, tray crop, unit crop; overlay-checked every box.
- Ran the contributor describe (`muse exec --model
  muse-spark-1.3-contributor --image …`, boxes in prompt text).
- Drafted the review-gated line items and wrote every file in this repo.
- Never touched QuickBooks, never held credentials, has no MCP tools.

**Hermes-agent — Debian office gateway (always-on service)**
- Hosts two QuickBooks MCP servers: `quickbooks` (production, all
  write/update/delete tools suppressed, read-only) and
  `quickbooks-sandbox` (sandbox company only, writes enabled).
- Runs the Quickerbooks bookkeeping agent (skill + `QBO-PLAYBOOK.md`):
  verified live reads, created sandbox customer 58, items 19–22, and
  posted invoice 145 — each step bounded, reported, and refused when the
  tool couldn't do it safely (no-draft invoice hold).
- Holds all credentials in owner-only local stores; none appear here.

## The handoff (the only coupling)

1. Muse Spark publishes machine-checked inputs: photo hash, SAM boxes,
   describe JSON with uncertainties, proposed lines with flags.
2. A human reviews (the Friday gate: quantities boxed, specs flagged).
3. Hermes-agent executes only approved sandbox writes and reads back IDs.
4. IDs and rendered artifacts (invoice 1038, PDF, screenshot) return to
   this repo as evidence.

## What never happens

- Muse Spark never calls QuickBooks and never sees a credential.
- Hermes-agent never invents counts, rates, or specs — unboxed values
  stay reviewer flags, and a missing tool (draft invoices) stops the run
  instead of being worked around.
- Production books are never written by either agent in this demo.
- The Oct 23 capture platform is prior art in a separate private tree —
  reused, not claimed.
