# Repository instructions

This repository is the canonical source of truth for this Mongil: Star Dive account.

## Evidence rules

- Never replace verified data with speculation.
- Prefer official or in-game text over third-party summaries.
- Prefer repeatable empirical testing over community assumptions.
- Cite or record the source of factual kit changes.
- Mark uncertainty explicitly with one of: `official`, `in_game`, `tested`, `community`, `hypothesis`, `unknown`.
- When sources conflict, preserve both claims and document the conflict.
- Preserve historical test results; supersede them with links rather than rewriting history.
- Never fabricate missing kits, numbers, durations, cooldowns, or proc behavior.

## Architecture

- Keep objective game data in `data/`, account state in `account/`, empirical results in `testing/`, and conclusions in `strategy/`.
- Update roster investment independently from static character documentation.
- Avoid duplicating facts when a canonical record can be linked.
- Use stable YAML front matter where useful.
- Keep generated indexes reproducible through scripts.

## Optimization behavior

- Avoid generic tier-list recommendations.
- Optimize for the actual roster, awakenings, Fate/signature levels, and opportunity cost.
- Account for field time, rotation timing, buff/debuff persistence, uptime, and monsterling allocation.
- Do not assume same-element teams are automatically optimal.
- Conquest teams contain exactly three characters.

