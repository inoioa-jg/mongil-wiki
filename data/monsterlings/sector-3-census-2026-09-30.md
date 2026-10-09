---
region: sector-3
patch: "1.4"
checked: 2026-10-09
source_confidence: community
status: incomplete-localization
---

# Sector 3 Monsterling census

## Confirmed scope

- The 1.4/Sector 3 update announcement reports **29 new Monsterlings** and **15 new Link Chains**.
- Kaiden.gg exposes records apparently datamined from the update, but many names remain Korean and most new fixed abilities still display unresolved localization keys (`ABIL_LOCAL_*`).
- Therefore, the names below are a discovery census, not yet a complete kit database.

## Publicly attributable Sector 3 candidates

The following 26 entries form the conspicuous new block in Kaiden's 196-Monsterling index and/or have pages updated September 24, 2026:

| English/localized | Korean/unlocalized |
|---|---|
| Beepmo | 레드비 |
| Colossus | 보이드 이터니티 |
| Crusher | 블랙러스 |
| Destructor | 블랙서스 |
| EightB | 비스포모 |
| Fearless | 실비지 |
| Fidelis Raptor | 알투스 랩터 |
| Grippy | 캡큐 |
| Hak-yu | 클린 호더 |
| Macrodon | 헌터피 |
| Promo | 화이트론 |
| Ragnadon |  |
| Scrap Hoarder |  |
| Sludge |  |
| Titus |  |

`Unknown` also appears in the index, but is not counted above because its region and identity cannot yet be established. Three of the official 29 additions therefore remain unattributed in public English-facing data (or are represented by provisional/duplicate names).

The two columns above are independent lists for compactness; rows do not claim
that the English and Korean names are translations of each other.

## Newly resolved effects (October 8 community update)

The following are Rank 5 breed effects transcribed by a Korean community guide.
Names are translations/transliterations until confirmed in the English client.

| Monsterling | Element | Rank 5 breed effect | Unresolved details |
|---|---|---|---|
| Scrap Hoarder | unknown | On landing a Switch Skill, Basic Attack DMG +11% for 10s | Whether off-field Basic Attacks retain the bonus |
| Whiteron (`화이트론`) | Ice | On Ultimate Skill hit, target Ice RES -11.55% | Duration, cooldown, stacking |
| Clean Hoarder (`클린 호더`) | Wind | When attacking a boss, target Wind RES -11.55% | Duration, cooldown, stacking |
| Oblivion (`오블리비언`) | Wind | On dealing Wind DMG with a Special Skill, target Wind RES -11.55% | Duration, cooldown, stacking; not present in the initial Kaiden candidate block |

### Immediate account implications

- **Scrap Hoarder is a high-priority Ophelia test.** Her rotation begins from a
  switch and repeatedly uses Basic Attack chains, so the 10-second +11% Basic
  Attack DMG window may outperform Scar as a personal damage slot. This is a
  hypothesis until tested against the same encounter and build.
- **Whiteron is the first identified Sector 3 Ice RES shred.** It should be
  tested on Isabella or Narae so Ophelia receives the benefit without giving up
  a personal damage slot. Trigger ownership, uptime, and duplicate debuff
  stacking remain unknown.
- **Clean Hoarder and Oblivion answer the previous Wind-team gap:** Sector 3
  introduces at least two Wind RES reduction effects. The current account uses
  Clean Hoarder on Jiwon and Oblivion on Esther as staggered uptime sources.
  They are expected to overlap without stacking, maintaining approximately
  11.55% reduction rather than producing a 23.1% spike (`hypothesis`).

## Extracted records

All displayed stat values are Kaiden community data for the currently selected page state, not in-game verification.

| Monsterling | Grade | Trait slots | Page state | ATK | DEF | HP | Fixed ability key |
|---|---:|---:|---|---:|---:|---:|---|
| Beepmo | 5 | 4 | Lv.60 | 669 | 1.044 | 2.226 | `ABIL_LOCAL_4254511` |
| Colossus | 5 | 4 | Lv.60 | 743 | 1.159 | 2.473 | `ABIL_LOCAL_4259511` |
| Crusher | 5 | 4 | Lv.60 | 669 | 1.044 | 2.226 | `ABIL_LOCAL_4263511` |
| EightB | 5 | 4 | Lv.60 | 669 | 1.044 | 2.226 | `ABIL_LOCAL_4220511` |
| Grippy | 5 | 4 | Lv.60 | 669 | 1.044 | 2.226 | `ABIL_LOCAL_4222511` |
| Macrodon | 5 | 4 | Lv.60 | 743 | 1.159 | 2.473 | `ABIL_LOCAL_4265511` |
| Promo | 5 | 4 | Lv.60 | 669 | 1.044 | 2.226 | `ABIL_LOCAL_4252511` |
| Scrap Hoarder | 5 | 4 | Lv.60, Breakthrough 4 | 981 | 1.530 | 3.265 | `ABIL_LOCAL_4260511` |
| Titus | 5 | 4 | Lv.60 | 669 | 1.044 | 2.226 | `ABIL_LOCAL_4264511` |

No Link Skill marker is shown on these nine currently accessible pages. That does **not** establish that none participate in the 15 new Link Chains; link-chain relationships may be recorded elsewhere or absent from the incomplete extraction.

## Optimization relevance

Most public data remains insufficient for a complete ranking, but Scrap
Hoarder, Whiteron, Clean Hoarder, and Oblivion now warrant controlled tests
against established effects such as Scar, Fiend, Gulgak, Amon/Amon's Shadow,
and El Dorado Guardian. The remaining effects worth flagging when localization
resolves are:

1. team-wide damage, elemental damage, elemental weakness, or resistance reduction;
2. off-field/tag-triggered effects that fit short Conquest rotations;
3. boss-only DEF reduction or damage amplification;
4. effects with independent names that could stack with current allocations.

## Sources

- Game Donga, 1.4 update overview (29 new Monsterlings; 15 Link Chains): https://game.donga.com/124506/
- Kaiden.gg Monsterling index (196 records; mixed localized/unlocalized names): https://www.kaiden.gg/mongil/monsterlings/
- Kaiden.gg individual pages for Beepmo, Colossus, Crusher, EightB, Grippy, Macrodon, Promo, Scrap Hoarder, and Titus (checked 2026-09-30).
- Niini, community Monsterling build notes, updated 2026-10-08 (Rank 5 effects
  for Scrap Hoarder, Whiteron, Clean Hoarder, and Oblivion):
  https://note.com/niini_games/n/nbe14f28a322d?hl=ko

## Next verification pass

- Transcribe the Sector 3 capture screen or Monsterling inventory entries from the English client.
- Resolve each `ABIL_LOCAL_*` key to its English effect text and rank scaling.
- Identify the missing three entries and enumerate all 15 Link Chains.
- Mark element, acquisition source, mutation recipe, link relationships, and whether each effect is personal or team-wide.
