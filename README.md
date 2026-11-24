# The One-Line AI Excuse for Breaking Production

[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/exc-ana/one-line-ai-excuse-01/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/exc-ana/one-line-ai-excuse-01/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

Bounty: https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66
Prize: $2 total, 8 places (1st $1.00, 2nd $0.50, 3rd $0.25, 4th $0.13, 5th $0.06, 6th $0.03, 7th $0.02, 8th $0.01)
Rounds (WIB): R1 Wed Nov 25 06:25, R2 Wed Nov 25 22:25, Final Thu Nov 26 14:25
Dev phase (per kit competition.yaml): 2026-11-24T07:25:38Z – 2026-11-26T07:25:00Z

## Entry line

> In my defence, the deploy succeeded flawlessly; the database has simply decided to become a paperweight.

- Characters: **104** (limit 180)
- Bytes: 104 (ASCII only)
- Lines: 1, no trailing newline
- SHA-256 of `/output/entry.txt`: `4b3ffb07f4714c1dee4f207203ef55b1f17b1cc7c5743bc357bece1c8e2ad8d3`
- Determinism: run twice, outputs byte-identical (`cmp` clean, same SHA-256)

## How it works

`main.py` (repo root entrypoint, Python) writes the fixed line to
`/output/entry.txt`. No randomness, no clock, no network, no environment
input — fully deterministic.

## Status

- Built from scratch from the official kit rules alone. No earlier entry
  code was read or copied (this is the first entry for this bounty).
- Kit verified (see WORKING-NOTES.md). Determinism verified.
- REVISED Tue Nov 24 2026 ~14:59 WIB in a new session: new line (104
  chars, SHA-256 `4b3ffb07…`), see "Revision session" in WORKING-NOTES.md.
  The revision was made so the entry's final content comes from 2+
  write/edit messages (thinking_revised fix). Determinism re-verified
  after the revision.
- NOT YET DONE (out of scope for this build task): GitHub repo, transcript
  bundle, kit check, submission. No wallet was touched.
