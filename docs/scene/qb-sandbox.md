# Sandbox QuickBooks writes — 2026-11-04 (new work)

Sandbox company: `Sandbox Company US b190`, realm `9341458631414879`.
Production untouched (production entry still read-only; no production calls).

## Connection

- Hermes gateway `mcp_servers.quickbooks-sandbox`: stdio MCP, sandbox token
  store (own OAuth handshake Oct/Nov), no disable flags — sandbox only.
- Sandbox token verified via `get_company_info` through the agent.

## Writes (sandbox only)

- Customer `Harbor Dental Studio` → ID **58** (demo Test Customer, HB-1042).
- Items created: fan unit **19**, M3 screw **20**, cable **21**, labor **22**.
- Invoice **145**, DocNumber **1038**, TotalAmt **41.00**, customer 58,
  lines: labor 22 ×1, fan 19 ×1, screws 20 ×4, cable 21 ×1.
  Posted (the QBO v3 API cannot create UI drafts), unsent, unpaid —
  created with explicit owner approval Nov 4. PrivateNote: HB-1042 demo.

## Proof

- Rendered invoice PDF (downloaded from the sandbox browser view):
  [`invoice-1038.pdf`](invoice-1038.pdf) — sandbox test data only.
- Browser screenshot of posted invoice 1038 (sandbox):
  [`invoice-1038-screenshot.png`](invoice-1038-screenshot.png) — 4 lines,
  quantities 1/1/4/1, all Nontaxable, matching the locked inventory.

## Demo line mapping

`docs/scene/line-items.md` lines 1–4 map to sandbox items 22/19/20/21.
Quantities 1/1/4/1 per the locked inventory; M3/3-pin/duration stay reviewer
flags on the invoice when it is created.
