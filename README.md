# PureBill — Hackathon Submission (solo)

New work window: **October 26 – November 4, 2026**. Deadline: **Wed Nov 4, 9pm ET**.
Everything in this repo was built on or after October 29, 2026, for this
submission. Nothing here is backdated.

## What is pre-existing (NOT in this repo, NOT claimed as new)

The October 23 capture platform lives separately in the private
`Pure-Bill` tree and is **not** part of this submission:

- Office photo-ingest capture service (14/14 suite green Oct 23).
- Android field app + Mentra Live capture flow (Oct 23 real capture:
  customer `Infsol, Inc.`, work order `0001`, note `Fix GPU`,
  request `29b14339-…`, 113,903 bytes, SHA-256 `e6c93f…078fa`).
- Hosted SAM 3.1 segmentation + local Qwen describe adapter (offline
  24/24 green, unaccepted/un-deployed as of Oct 23).

This repo reuses that platform as a **prior-art dependency only**. Judges
should treat all of the above as pre-existing. No files from that tree are
copied here.

## What IS new hackathon work (this repo)

1. **Staged demo scene** (`docs/scene/`): one fake job, inventory with
   expected counts written BEFORE the run, and the scene photo. The scene is
   deliberately distinct from the Oct 23 real capture and is locked for
   reuse in the Friday demo draft.
2. **Contributor-model describe check** (`docs/spark-smoke-test.md`): a
   single smoke test proving the exact endpoint and box format accepted by
   `muse-spark-1.3-contributor`, with output tied back to the SAM boxes.
   - The demo names the **contributor variant** `muse-spark-1.3-contributor`.
     It is **not** presented as standard `muse-spark-1.3`.
   - Working in **Contributor mode** for this submission; there is no
     Standard-mode requirement.

## Status

- [x] Repo created (Oct 29)
- [x] Staged scene inventory locked pre-run (photo pending — see `docs/scene/`)
- [x] Spark contributor smoke test passed (Oct 29)
- [ ] Friday demo draft (reuses the locked scene, no substitutions)
