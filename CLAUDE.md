# Working rules for this repo

This repo hosts rendered media. The rules that govern what may be *said* in that media live in the
private `social-media` repo at `docs/FACT_CHECK_STANDARD.md`. Routines that only check out this
repo cannot read that file, so the essentials are repeated here. They are not optional.

## Nothing is rendered until the fact passes two gates

His standing instruction, 2026-08-13: *"Authentic information and no fake and avoid ai tells and em
dashes. Validate with scientific published work before publishing. Pipeline and memory should
include this information to use even if i do not provide it next time."*

1. **The event is real.** Any current-events claim traces to a primary source: the agency page, the
   company release, the government statement, the dataset itself. Never a search summary or an
   aggregator. Then confirm with a second independent outlet.
2. **The science is published.** The one surprising fact at the heart of a short needs peer-reviewed
   support, or an agency technical basis document built on one. Record author, year, journal and
   DOI, and verify the DOI at `api.crossref.org`. **No paper, no short:** pick a different concept
   rather than hedging the number into vagueness.

Match the claim to the study's scope. A result from one region or one crop is not a global fact.
Never invent a number, a place name, a date or a map feature.

## This matters more here than anywhere else

Text burned into a video frame **cannot be corrected after upload**. On 2026-08-13 the short
`DroughtEarly` had to be pulled from a live post because its on-screen text carried both a lead
time no publication supports and a banned em dash. Neither was fixable without a re-render.

## Voice, and it applies to every `Text()` object

- **No em dashes and no en dashes.** Not in the hook, the fact line, the punch line, the end card,
  the cover, the caption or the commit message. Grep the scene file before rendering.
- **No AI tells.** No "delve", "dive in", "unlock", "game changer", "in today's world". No
  rule-of-three padding, no sentence opening with "Moreover" or "Furthermore".
- Plain words. Explain the mechanism, do not name the library.

## Frame zero must be fully drawn

Measured 2026-08-13: older shorts in this library open at mean luma 243, standard deviation 0.00,
**0.00% ink coverage**. A perfectly blank frame. TikTok's auto-cover grabbed a frame about 2% drawn
and published a thumbnail that looked empty; that post got 282 views at a 2.5% like rate.

So open every scene with the complete hook already on screen (`self.add(hook)` then `self.wait(1)`,
never `self.play(Write(hook))` as the opening beat), and check the first frame after rendering.

Cover content beats cover brightness. The two best performers (886 and 953 views, 8.3 to 8.8% like
rates) used a real photographic background plus one bold, complete, high-contrast claim. Flat
diagrams, half-drawn charts and contentless titles landed between 117 and 345 views.

## Manifest entries carry their sources

Every `captions_manifest.json` entry includes `cover`, `source_doi` and `source_url`, so downstream
scheduling routines can cite the claim without re-researching it.
