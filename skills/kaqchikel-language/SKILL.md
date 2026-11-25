---
name: kaqchikel-language
description: Load this before writing, checking or explaining ANY Kaqchikel Maya, even a single word or one verb form - unaided, models get about a third of Kaqchikel forms wrong (verb prefixes, lax vowels, possessed nouns, numbers, day names) while sounding sure. Covers Kaqchikel (Cakchiquel, ISO cak) in English or Spanish - translating to or from it, conjugating, glossing, "how do you say", vocabulary, spelling, the cholq'ij calendar, greetings, lessons and town-to-town dialect differences. También en español - cómo se dice en kaqchikel, traducir, conjugar, idioma maya kaqchikel, cakchiquel.
---

# Kaqchikel Maya

Kaqchikel is a K'iche'an Mayan language of the central Guatemalan highlands, with roughly half a
million speakers from Chimaltenango and Sacatepéquez to Sololá and Lake Atitlán. It is ergative,
verb-initial and head-marking, and it has no verb "to be".

You already know a fair amount of Kaqchikel, and that is the danger: you produce it fluently, and
about a third of what you produce unaided is wrong in ways a learner cannot see. Measured on 48
typical requests, an unaided model got the transitive verb tables, imperatives, negation and
greetings right, and went wrong on the things listed in the next section, always in confident type.
Read that section before writing any Kaqchikel.

Answer in the language the user writes in. Spanish glosses are in `references/lexicon.md` and
`references/examples.md` next to the English ones.

## The mistakes you will make without checking

1. **`in-`/`at-` before a consonant.** The 1s and 2s absolutive prefixes have two shapes. Before a
   consonant they are `i-` and `a-`; `in-` and `at-` appear only before a vowel.
   `xib'e` "I went", `xab'e` "you went", `xkib'e` "I will go", `xiwa'` "I ate", `yiwär` "I sleep";
   but `xinel` "I left", `xatel` "you left". The courses teach `i-`/`a-` here, and running text
   overwhelmingly agrees (`xib'e` 47 times, `xinb'e` never). The OKMA grammar and some school
   books do show `in-`/`at-` before a consonant (`xkinb'e`, `xatb'e`, `xinwa'`); treat those as a
   minority form and label them if you use them.
2. **Dropping the lax vowels.** `ä ë ï ö ü` are separate vowels, not accents, and they are written
   every time: `ütz`, `nimaläj`, `tz'uyül`, `xtiqalöq'`, `waqän`, `räx`, `wäy`, `ch'ab'äl`,
   `kosnäq`, `winäq`. Most older Bibles and pre-1987 texts never write them, so a form you remember
   without its dots is suspect. When a suffix follows, a final-syllable lax vowel usually turns
   tense: `winäq` > `winaqi'`.
3. **Forgetting the person marker on a non-verbal predicate.** The pronoun is optional, the marker is
   not: `In kosnäq` or `Rin in kosnäq` "I am tired", never `Rin kosnäq`. Same for nouns:
   `In ak'wal na` "I am still a child". See "No copula" below.
4. **Losing agreement inside a sentence.** A paradigm you can recite comes out wrong in context.
   Each verb in a chain carries its own subject: `Ninwajo' yib'e` "I want to go",
   `Wetaman yikemon` "I know how to weave" (not `nikemon`, which is "she weaves"). Speaking,
   walking and weaving are intransitive: `yach'o'n` "you speak", not `nach'o'`.
5. **K'iche' leaking in.** Numbers and day names especially: 40 is `kak'al` and 100 `wok'al` (not
   `ka'k'al`, `o'k'al`); the days are `Ey` and `Kamey` in the Kaqchikel courses (not `E`, `Kame`). Good afternoon is
   `Xqa q'ij`.
6. **Inventing a word, or grabbing a neighbour.** If you cannot find a word in
   `references/lexicon.md`, say so. Real slips from the test: `wanab'` (no such word) for `wana'`
   "a man's sister", `wa'` for `wäy` "tortilla" (`-wa'` is the verb "eat"), `tayaka'` "pick it up"
   for `taya'` "give it", `wachalal` for `wach'alal` "my relative".
7. **"My house".** The possessed stem is `-ochoch`, vowel-initial: `wochoch`, `awochoch`,
   `rochoch`. `nuchoch` does not exist. Other vowel-initial nouns behave the same (`w-`, `aw-`, `r-`).
8. **Inventing dialect facts.** Do not describe a town's speech from intuition. The courses teach
   `rin` (also written `rïn`) for "I"; `yïn` belongs to other towns, and old Bibles spell it `yin`. Look the town up in
   `references/dialects.md`, and if it is not there, say you do not have data for it.
9. **Calques.** "I am from X" is `In aj X` (not `richin`). The name comes before `nub'i'`:
   `Ixchel nub'i'`. "And you?" repeats the question: `¿La ütz awäch rat?`. For a price, ask
   with `janipe'` "how much" and `rajil` "its price". Money is `pwäq` (possessed `nupwaq`).
10. **Root-transitive passives.** A CVC root makes its passive by turning its lax vowel tense, with
    no suffix: `xukëm` "she wove it" > `xkem` "it was woven", not `xkemäx`; `xtz'et` "it was
    seen". Derived `-j` verbs use `-äx`.
11. **Trusting your own hedges.** Your doubt tends to land on rare words while the systematic errors
    above come out confident. Check the common verb forms too.

## How to work

1. **Look it up, don't recall it.** The reference files are large; search them, don't read them
   whole. `grep -i "wochoch" references/*.md` finds a form; `grep -i "| house"` or
   `grep -i "casa"` finds a gloss. Normalize apostrophes to the straight `'` first.
2. **Every form you produce is one of three things**, and you should know which:
   - *attested*: found in the references (the lexicon's last column gives how many sources use it;
     `1 src` is thin, `10+ src` is solid);
   - *derived*: built by a rule below from attested pieces. Say so when it matters:
     `xtutz'ib'aj` = `xt-` potential + Ø 3sB + `u-` 3sA + `tz'ib'aj` "write";
   - *uncertain*: mark it `[?]` with a short reason ("regular form, not found in the sources").
     Never present a guess in the same type as a fact; a learner cannot tell them apart.
3. **Name the variety.** The default here is the central standard in ALMG spelling (1987). If the
   user asks about a town, or uses a local form, use `references/dialects.md`.
4. **Copy from real sentences.** For a construction you are unsure of, find a model in
   `references/examples.md` and adapt it, rather than building from English.

## Spelling and sounds

Alphabet (ALMG): `' a ä b' ch ch' e ë i ï j k k' l m n o ö p q q' r s t t' tz tz' u ü w x y`.
`x` = English sh, `j` = h, `q` = a k pronounced further back, `b'` is implosive, and the
apostrophe after a consonant is part of the letter (`k'`, `tz'`). A glottal stop between or after
vowels is written (`ya'` "water", `ja'` "yes"); at the start of a word it is not. Stress is on the
last syllable. Ten vowels: tense `a e i o u` and lax `ä ë ï ö ü`, all written.

## Person markers

**Set A** (ergative): who does a transitive action, and who owns a noun.
**Set B** (absolutive): who undergoes a transitive action, who does an intransitive one, and who a
noun or adjective describes (`in tijonel`, "I [am] a teacher").

| | Set B on verbs (before C / V) | Set B free word | Set A on nouns (C / V) | Set A on verbs (C / V) |
|---|---|---|---|---|
| 1s | i- / in- | in | nu- / w- | in- / inw- |
| 2s | a- / at- | at | a- / aw- | a- / aw- |
| 3s | Ø | Ø | ru- / r- | u- / r- |
| 1p | oj- | öj | qa- / q- | qa- / q- |
| 2p | ix- | ïx | i- / iw- | i- / iw- |
| 3p | e- / e'- | e | ki- / k- | ki- / k- |

Pronouns `rin` (or `rïn`), `rat`, `rija'`, `röj`, `rix`, `rije'` are for emphasis only. 3s Set A on a verb is `u-` after
an aspect prefix (`xuya'` "he gave it"), `r-` before a vowel (`xrajo'`, `nrajo'`), and `ru-` after a
Set B prefix (`yaruto'` "he helps you").

## Verbs

Template: `ASPECT + Set B + Set A + stem`. The object (Set B) comes before the subject (Set A).

| Aspect | before 3s (Ø) | elsewhere | meaning |
|---|---|---|---|
| incompletive | n- | y- | present, habitual |
| completive | x- | x- | past |
| potential | xt- | xk- | future, intention |
| imperative | t- | k- | commands, let's |

So `nb'e` "she goes" but `yib'e` "I go"; `xtib'e` "she will go" but `xkib'e` "I will go".
Before a vowel-initial transitive stem `xt-` usually takes an `i` (`xtirajo'`, `xtirïl`), though
`xtrïl` also occurs.

Transitive "it" as object: `ninlöq'` "I buy it", `nalöq'`, `nulöq'`, `nqalöq'`, `nilöq'`, `nkilöq'`;
completive `xinlöq'` ... `xkilöq'`; potential, with `-b'än` "do": `xtinb'än`, `xtab'än`, `xtub'än`,
`xtiqab'än`, `xtib'än`, `xtikib'än`. With other objects both markers show: `xojkito'` "they helped us",
`xatintz'ët` "I saw you". Full tables: `references/paradigms.md`.

Root transitives (CVC, lax vowel: `-b'än` "do", `-löq'` "buy", `-tz'ët` "see") and derived
transitives (ending `-Vj`: `-tz'ib'aj` "write", `-k'utuj` "ask") differ in the imperative, the
passive and the antipassive:

| | root `-këm` "weave" | derived `-tz'ib'aj` "write" |
|---|---|---|
| active | xukëm "she wove it" | xutz'ib'aj "she wrote it" |
| passive | xkem "it was woven" | xtz'ib'äx "it was written" |
| antipassive / agent focus | xkemon "she wove (things)" | xtz'ib'an |
| imperative "you" | takema' | tatz'ib'aj |

When the agent is questioned, focused or relativized, the verb goes antipassive:
`¿Achike xkemon?` "Who wove it?".

## No copula

Nouns, adjectives, positionals and `k'o` are predicates on their own, with the free Set B word in
front: `In tijonel` "I am a teacher", `At kosnäq` "you are tired", `E k'o pa jay` "they are at the
house". `k'o` means "there is / is located / has": `K'o jun nutz'i'` "I have a dog",
`Majun nupwaq` "I have no money". Negation wraps the predicate: `Man in tijonel ta`.

## Possession

Set A on the noun, possessor after it: `rochoch ri ak'wal` "the child's house". Possession can
change the noun: lax vowel tenses (`ch'akät` > `nuch'akat`), body parts and kin drop a suffix
(`jolomaj` > `nujolom`), inherent parts add `-Vl` (`b'aq` > `nub'aqil`), and a few are suppletive
(`jay` "house" > `wochoch`). Look up any noun you possess in `references/lexicon.md`.

## Small words that frame clauses

- Negation is a frame: `man` ... `ta`. `Man xb'e ta` "he didn't go". `Manäq` is only the answer "no".
- Yes/no questions start with `la`: `¿La xab'e?`. "Where" needs `wi` after the verb:
  `¿Akuchi' xab'e wi?`
- Demonstratives are frames too: `re wuj re'` "this book", `la wuj la'` "that book", and `ri` "the".
- Relational nouns do the work of prepositions and take Set A: `wik'in` "with me", `chwe` "to me",
  `wichin` "mine", `chuwäch` "in front of", `pa` "in, at".
- Directionals follow the verb: `pe` hither, `el` away, `apo` thither, `kan` left behind, `qa` down,
  `aqanäj` or `aqanïj` up: `xtzolin pe` "came back".

## Kin terms depend on the speaker

A man calls his sister `wana'`; a woman calls her brother `nuxib'al`. Same-sex siblings are
`nunimal` (older) and `nuchaq'` (younger). A woman's child is `wal`, a man's son `nuk'ajol` and
daughter `numi'al`.

## Glossing labels

This skill writes Set A = ergative, Set B = absolutive, and COMPL / INCOMPL / POT / IMP for aspect:
`x-Ø-u-löq'` COMPL-3sB-3sA-buy "she bought it". Many published grammars, including the Maxwell and
Little sequel and the *Kaqchikel Chronicles*, use the mirror image (A = absolutive, E = ergative). Convert labels before comparing.

## Reference files

| File | Use it for |
|---|---|
| `references/lexicon.md` | any word: Kaqchikel, English or Spanish gloss, possessed and plural forms, attestation count |
| `references/paradigms.md` | complete verb, pronoun, relational-noun, number and calendar tables |
| `references/grammar.md` | the rule behind a pattern, with cited examples and where sources disagree |
| `references/examples.md` | real sentences by construction, with English and Spanish, to imitate |
| `references/dialects.md` | town and regional variation, with parallel texts across seven varieties |
| `SOURCES.md` | where every quotation and count comes from |

Example sentences are quoted from published or permitted sources with a citation tag. Counts come
from a larger private corpus of Kaqchikel texts and are cited, not reproduced.
