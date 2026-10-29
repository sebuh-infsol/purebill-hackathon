# Spark contributor smoke test — 2026-10-29 (pass)

One single smoke test, run before any demo wiring.

## What was tested

Model: **`muse-spark-1.3-contributor`** (contributor variant — not standard `muse-spark-1.3`).
Mode: Contributor mode. Effort: low.

## Endpoint and format accepted

- Endpoint: `muse exec --model muse-spark-1.3-contributor --reasoning-effort low`
  (Meta provider default base URL; no override needed).
- Image: attached with `--image <jpeg-path>` (local JPEG bytes).
- SAM boxes: given **in the prompt text** as
  `box x1=660 y1=0 x2=1279 y2=494 in 1280x960 space`
  plus the SAM concept (`computer case`). No special schema or tool call required.
- Fixture used (probe only, not submission work): the Oct 23 stored photo
  `29b14339-….jpg` and its real SAM 3.1 box for concept `computer case`
  (`x1=660 y1=0 x2=1279 y2=494`, 1280x960 space).

## Result: PASS

The model quoted the box coordinates back verbatim, described only what is
visible inside that box (black tower, side panel, RGB glow/reflections,
cables, dark interior), and listed the rest as explicit uncertainties
(exact case/GPU model, front panel, cable routing, reflection-vs-strip).
Output demonstrably ties back to the supplied box.

## Consequence

The contributor-variant call is proven. Demo wiring may use this exact
endpoint + text-box format. No day burned on unproven calls; the local Qwen
fallback stays available but is not needed for this route.
