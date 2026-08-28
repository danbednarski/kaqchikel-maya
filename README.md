# Kaqchikel Maya, as a Claude skill

Kaqchikel is a K'iche'an Mayan language of the Guatemalan highlands, spoken by roughly half a
million people around Tecpán, Comalapa, Sololá and Lake Atitlán. It is ergative,
predicate-initial, head-marking, and has no copula. Off-the-shelf, language models write it
badly: they invent verb forms, flatten the lax vowels, and reach for a copula that does not
exist.

This is a skill that fixes that. It packs the whole working grammar into the always-loaded
`SKILL.md`, and puts the long tail behind five reference files that load only when a question
needs them.

## Install

```
/plugin marketplace add danbednarski/kaqchikel-maya
/plugin install kaqchikel-language@kaqchikel-maya
```

Or drop it in by hand, no plugin machinery required:

```
git clone https://github.com/danbednarski/kaqchikel-maya
cp -r kaqchikel-maya/plugins/kaqchikel-language/skills/kaqchikel-language ~/.claude/skills/
```

It works anywhere skills work: Claude Code, the Claude apps, and the API.

## What it knows

`SKILL.md` alone carries the alphabet and phonology, both person-marker sets, the verb template
and all four aspects with complete paradigms, non-verbal predicates, the six possession classes,
determiners, the negation and question frames, voice, positionals, relational nouns,
directionals, numbers, survival phrases, and the mistakes English speakers reliably make.

| Reference | What is in it |
|---|---|
| `grammar.md` | the compressed pattern tables of all 32 chapters of the source textbook |
| `paradigms.md` | complete paradigms: every person, aspect, voice, positional derivation, relational noun, number and time word, plus a glossary of grammatical terms |
| `lexicon.md` | 15 domain vocabulary lists, set phrases and idioms, an English-Kaqchikel finder, and the 400 most frequent words in the corpus |
| `examples.md` | 1,300 Kaqchikel/English sentence pairs, arranged by topic, every one checked against the corpus |
| `usage-and-dialect.md` | register, town-to-town variation, competing forms, and known learner errors |

## What it is careful about

The skill is built to refuse to bluff. It tells the model to attest a form, or derive it from a
stated rule and say which rule, or mark it `[?]` and say it is unattested. That last part matters:
a learner cannot tell a model's guess from the language.

It also carries two traps worth knowing about. Kaqchikel's lax vowels (ä ë ï ö ü) are
separate phonemes, not accents, and most published grammars label the person markers with the
mirror image of the convention used here (their A is absolutive, this skill's Set A is ergative),
so glosses cannot be compared across the two systems without translating the labels first.

## Where it comes from

The content is distilled from *Kaqchikel from the Ground Up*, an original English-language
textbook of Kaqchikel, and checked against a corpus of attested text. The grammar was compiled
from published descriptions of the language: the standard first-year course (Brown, Maxwell and
Little, *¿La ütz awäch? Introduction to Kaqchikel Maya Language*, University of Texas Press,
2006), ALMG and Cholsamaj grammars, readers and dictionaries, the dialect survey *Rujunamaxik
ri Kaqchikel Chi'*, Salazar Tetzagüic's literary anthology, Maxwell and Hill's *Kaqchikel
Chronicles*, and present-day written Kaqchikel.

The facts of Kaqchikel grammar and vocabulary are the common property of the language's
speakers. The wording, tables and example sentences assembled here are this project's own; no
dialogue, reading or exercise from any of those works is reproduced. Orthography is ALMG (1987).

Corrections from Kaqchikel speakers are more welcome than anything else that could land in the
issue tracker.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Use it, ship it, build on it, credit it.
