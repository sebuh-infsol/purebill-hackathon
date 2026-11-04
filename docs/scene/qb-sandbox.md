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
- Invoice: **held, not created.** The sandbox MCP create path posts (no
  draft-status option), and per repo rules an unsent invoice is not assumed
  non-posting — so no invoice was written without explicit approval.

## Demo line mapping

`docs/scene/line-items.md` lines 1–4 map to sandbox items 22/19/20/21.
Quantities 1/1/4/1 per the locked inventory; M3/3-pin/duration stay reviewer
flags on the invoice when it is created.
