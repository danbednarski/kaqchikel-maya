[![skills.sh](https://skills.sh/b/danbednarski/kaqchikel-maya)](https://www.skills.sh/danbednarski/kaqchikel-maya)

# Kaqchikel Maya for Claude

A skill that makes Claude write Kaqchikel Maya correctly, in English or Spanish, and tell you when
it is not sure.

Kaqchikel is a Mayan language of the Guatemalan highlands with about half a million speakers.
Language models already "know" some of it, which is the problem: they write it fluently and get
the most common forms wrong. Unaided, a current model says *xinb'e* for "I went" (it is *xib'e*),
*nuchoch* for "my house" (*wochoch*), and *ka'k'al* for forty (*kak'al*, the other is K'iche'),
drops the lax vowels (*ütz*, *nimaläj*), and invents dialect facts about real towns, all in the
same confident voice as the parts it gets right.

Ask Claude Sonnet to conjugate "go" in the past tense:

| | Without the skill | With the skill |
|---|---|---|
| I went | **xinb'e** ✗ | **xib'e** |
| you went | **xatb'e** (regional) | **xab'e** |
| she went | xb'e | xb'e |
| we went | xojb'e | xojb'e |
| you all went | xixb'e | xixb'e |
| they went | xeb'e | xeb'e |

The two forms it gets wrong are the ones a learner says most.

## Install

Claude Code:

```
/plugin marketplace add danbednarski/kaqchikel-maya
/plugin install kaqchikel-language@kaqchikel-maya
```

Any skills-compatible agent:

```
npx skills add danbednarski/kaqchikel-maya
```

By hand: copy `skills/kaqchikel-language/` into `~/.claude/skills/`. In the Claude apps, zip that
folder and upload it under Settings > Capabilities > Skills.

## What it does

- **Fixes the specific mistakes models make.** We gave an unaided model 48 ordinary requests
  (translate, conjugate, gloss, explain a dialect) and graded every form against the sources. The
  skill's first section is that list of failures with the correct forms, so the model reads it
  before writing anything.
- **Checks instead of recalling.** The model is told to look forms up in the references and to
  sort everything it writes into attested, derived by a stated rule, or flagged `[?]`. Each
  lexicon entry says how many independent sources use the word.
- **Speaks Spanish.** Glosses come in English and Spanish, and the skill triggers on Spanish
  requests. Most people who ask about Kaqchikel ask in Spanish.
- **Knows the towns, and says when it doesn't.** Seven New Testament translations in seven regional
  varieties, aligned verse by verse, give a measured table of what actually differs between, say,
  Sololá and Santa María de Jesús. For a town the sources don't cover, it says so.

| File | Contents |
|---|---|
| `SKILL.md` | the failure list, how to check a form, and the core grammar: person markers, aspect, voice, possession, negation, no copula |
| `references/lexicon.md` | Kaqchikel / English / Spanish lexicon with possessed and plural forms and a source count per word |
| `references/paradigms.md` | full verb, pronoun, relational-noun, number and calendar tables, each cell attested or marked as derived |
| `references/grammar.md` | the grammar by topic, with cited examples and the places where sources disagree |
| `references/examples.md` | about 600 real sentences by construction, each with its source and an English or Spanish translation |
| `references/dialects.md` | variation across seven regional varieties, with parallel verses |
| `SOURCES.md` | every source, its licence, and what the skill takes from it |

Everything is plain Markdown that the model searches as needed. It needs no network access.

## Does it work?

`evals/` holds the test: 30 requests built from the baseline's real mistakes, each scored by
which forms the answer must and must not contain. Run it yourself:

```
python3 evals/run.py --model sonnet
```

Results on 30 cases (November 2026; the with-skill score varies by a case between runs):

| Model | Without the skill | With the skill |
|---|---|---|
| Claude Sonnet | 5 / 30 | 29-30 / 30 |
| Claude Haiku | 4 / 30 | 30 / 30 |

The cases come from the same failures the skill was written against, so read this as "the skill
fixes what it set out to fix", not as a general accuracy score. Add your own cases to
`evals/cases.json`.

## Sources and trust

Every example sentence in the skill is quoted from a source that permits it, with a citation:
the courses and grammar of Judith Maxwell, Walter Little and the Cuma Chávez family (used with the
authors' permission), the Wycliffe New Testaments, the MINEDUC/USAID readers on Bloom Library,
the Kaqchikel Wikipedia, Mozilla's Kaqchikel localization, and the colonial *Annals*. Word counts
also draw on grammars, dictionaries and newer writing that cannot be redistributed; those are
cited by title and page and never quoted. Spelling follows the ALMG standard (1987). Details are in
[`SOURCES.md`](skills/kaqchikel-language/SOURCES.md).

The skill reports what the sources attest. It is not a native speaker. Corrections from Kaqchikel
speakers are the most useful thing anyone can send: open an issue with the form, what is wrong
with it, and where you are from.

## License

This project's own writing is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Quoted
sentences keep their sources' terms, listed in `SOURCES.md`: the New Testament quotations are
CC BY-NC-ND, the Bloom and Wikipedia ones CC BY-NC-SA, the Mozilla ones MPL 2.0, and the Maxwell
and Little material is quoted by permission and is not relicensed.
