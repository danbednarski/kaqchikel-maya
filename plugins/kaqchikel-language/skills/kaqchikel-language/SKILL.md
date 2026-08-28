---
name: kaqchikel-language
description: Speak, write, translate, gloss, and teach Kaqchikel Maya. Use whenever a request involves producing, correcting, analyzing or explaining Kaqchikel (Kaqchikel Maya, Cakchiquel, ISO cak) - translating to or from it, checking whether a form is real, glossing or parsing a word or text, reading colonial or modern Kaqchikel, writing lessons, drills or example sentences, or answering questions about its grammar, vocabulary, orthography, idioms or dialect variation.
---

# Kaqchikel Maya

Kaqchikel is a K'iche'an Mayan language of the Guatemalan highlands, roughly half a million
speakers around Tecpán, Comalapa, Sololá and Lake Atitlán. It is **ergative**, **predicate-initial**,
**morphologically head-marking**, and has **no copula**. Everything below is the working core;
the reference files hold the rest.

## How to work in this skill

1. **Attest before you invent.** Every Kaqchikel form you produce should be (a) a form you can
   point to in the corpus or in the reference files here, (b) built by a rule stated in this
   skill from morphemes that are themselves attested, or (c) explicitly flagged. To check a
   form here, search `references/examples.md` and `references/lexicon.md`, then
   `references/grammar.md` for the rule that would build it.
2. **Rule-derive openly.** `xtutz'ib'aj` "she will write it" = `xt-` potential + Ø 3sB + `u-` 3sA
   + `tz'ib'aj`. If every piece is attested and the assembly follows a rule below, the form is
   good; say which rule if it matters.
3. **Flag the rest.** A form you could not attest or derive gets `[?]` and a short parenthetical
   ("regular extrapolation, unattested"). Never present an invented form in confident type. This
   matters more than usual: a learner cannot tell your guess from the language.
4. **Say which dialect you are giving.** Kaqchikel varies sharply town to town. The default here
   is the central standard (Tecpán, Comalapa) in ALMG orthography. When a form is local, say so.
5. **Style, when writing for the project:** no em-dashes or en-dashes, straight apostrophe `'`
   for the glottal stop, bold **Kaqchikel** in prose and plain in tables, Kaqchikel line then
   English line.

## Orthography and sounds

`' a ä b' ch ch' e ë i ï j k k' l m n o ö p q q' r s t t' tz tz' u ü w x y`

| | Bilabial | Dental/alveolar | Alveopalatal | Velar | Post-velar | Glottal |
|---|---|---|---|---|---|---|
| Plain | p | t, tz | ch | k | q | ' |
| Glottalized | b' | t', tz' | ch' | k' | q' | |
| Fricative | | s | x (= sh) | | | j (= h) |
| Nasal | m | n | | | | |
| Other | w | l, r | y | | | |

Ten vowels: tense **a e i o u**, lax **ä ë ï ö ü**. The lax series is phonemic and non-negotiable,
`ch'ab'äl` "language" is not `ch'ab'el`.

- Lax vowels occur only in **final** syllables and **tense when a suffix follows**: `winäq` >
  `winaqi'`, `ch'akät` > `nuch'akat`, `tz'ib'ab'äl` > `nutz'ib'ab'al`.
- Word-initial glottal stop is real but unwritten; medial and final ones are written (`ye'el`, `ya'`).
- `w y l r` devoice word-finally. `b'` is implosive; `q q'` are uvular.
- **Stress falls on the final syllable** (tinaMIT, samaJEL). Exceptions: the vocatives `táta`, `nána`.
- Statements and wh-questions fall; yes/no questions rise.

## The two marker sets

Everything in the morphology runs on these. **Set A = ergative** (transitive subject, possessor).
**Set B = absolutive** (intransitive subject, transitive object, subject of a non-verbal predicate).

| | Set B prefix (before C / V) | Set B free word | Set A on nouns (C / V) | Set A on verbs (C / V) |
|---|---|---|---|---|
| 1s | i- / in- | in | nu- / w- | in- / inw- |
| 2s | a- / at- | at | a- / aw- | a- / aw- |
| 3s | Ø | Ø | ru- / r- | u- / r- |
| 1p | oj- | öj | qa- / q- | qa- / q- |
| 2p | ix- | ïx | i- / iw- | i- / iw- |
| 3p | e- / e'- | e | ki- / k- | ki- / k- |

Independent pronouns: `rin` (var. `yïn`), `rat`, `rija'`, `röj`, `rix`, `rije'`. They are optional
and used for emphasis or clarity, never required.

**Third-person Set A, `r` or no `r`:** after an aspect prefix before a consonant it is `u-`
(`nulöq'`, `xulöq'`, `xtulöq'`); after an aspect prefix before a vowel it is `r-` (`nrajo'`,
`xrajo'`, and `xt-` inserts i: `xtirajo'`); after a Set B vowel before a consonant it is `ru-`
(`yarutz'ët`); before a vowel, `r-` (`yarajo'`).

## Aspect and the verb template

    ASPECT + Set B + Set A + STEM (+ suffix)

Object marker precedes subject marker. The 3sB is zero, which is why the aspect prefixes alternate:

| | before zero 3sB | elsewhere |
|---|---|---|
| incompletive (present/habitual) | n- | y- |
| completive (past) | x- | x- |
| potential (future) | xt- | xk- |
| imperative / hortative | t- | k- |

### Intransitive verbs

| | -wär "sleep" (C stem) | -oq' "cry" (V stem) | completive (-b'e) | potential (-b'e) |
|---|---|---|---|---|
| 1s | yiwär | yinoq' | xib'e | xkib'e |
| 2s | yawär | yatoq' | xab'e | xkab'e |
| 3s | niwär | noq' | xb'e | xtib'e |
| 1p | yojwär | yojoq' | xojb'e | xkojb'e |
| 2p | yixwär | yixoq' | xixb'e | xkixb'e |
| 3p | yewär | ye'oq' | xeb'e | xkeb'e |

Rule of thumb: `y-` everywhere except the zero third singular, where it is `n-`. Before a vowel
stem, 1s/2s add `-n`/`-t` and 3p adds a glottal stop.

### Transitive verbs, "it" as object

| | -löq' "buy" | -k'utuj "ask" | -ajo' "want" (V) | completive | potential |
|---|---|---|---|---|---|
| 1s | ninlöq' | nink'utuj | ninwajo' | xinlöq' | xtinlöq' |
| 2s | nalöq' | nak'utuj | nawajo' | xalöq' | xtalöq' |
| 3s | nulöq' | nuk'utuj | nrajo' | xulöq' | xtulöq' |
| 1p | nqalöq' | nqak'utuj | nqajo' | xqalöq' | xtiqalöq' |
| 2p | nilöq' | nik'utuj | niwajo' | xilöq' | xtilöq' |
| 3p | nkilöq' | nkik'utuj | nkajo' | xkilöq' | xtikilöq' |

Non-third-singular objects (with `-to'` "help"): `yatinto'` "I help you", `yinato'` "you help me",
`yiruto'` "he helps me", `yojruto'` "he helps us", `yeqato'` "we help them", `yixkito'` "they help
you all". Completive `xatinto'`, potential `xkatinto'`. Full matrix: `references/paradigms.md`.

**Root vs derived transitives.** Root transitives are CVC with a lax vowel (`-b'än`, `-löq'`,
`-tz'ët`, `-tij`); derived transitives end in `-Vj` (`-k'utuj`, `-tz'ib'aj`, `-elesaj`). The
distinction governs the imperative suffix, the passive, and the antipassive.

### Imperative and hortative

| | intransitive (C / V) | transitive, root (-b'än) | transitive, derived (-k'utuj) |
|---|---|---|---|
| let me | ki- / kin- | tinb'ana' | tink'utuj |
| you | ka- / kat- | tab'ana' | tak'utuj |
| let him/her | ti- / t- | tub'ana' | tuk'utuj |
| let's | koj- | tiqab'ana' | tiqak'utuj |
| you all | kix- | tib'ana' | tik'utuj |
| let them | ke- / ke'- | tikib'ana' | tikik'utuj |

Root transitives take a final vowel matching the root, and the root vowel tenses: `ä > -a'`
(`tab'ana'`), `ö > -o'` (`taloq'o'`), `ü > -u'` (`tak'utu'`), `i, ë > -a'` (`tatija'`, `tasela'`).
Glottal-final roots add nothing (`taya'`, `kinato'`). Exceptions `tab'ij`, `tak'waj`.

Negative command: `man` + imperative + `ta`. Softer, to children: `mani` + incompletive
(`mani nachäp` "don't touch it"). Routinized without `ta`: `man tab'ij ke ri'` "don't mention it".

## No copula: non-verbal predicates

Nouns, adjectives, positionals and `k'o` are predicates by themselves, and take the **free Set B**
words `in at Ø öj ïx e` in front.

| Frame | Example | English |
|---|---|---|
| Set B + noun | Rin in tijonel. | I am a teacher. |
| Set B + adjective | At kosnäq. | You are tired. |
| predicate + `ri` NP | Ajkem ri te Ixk'at. | Ixk'at is a weaver. |
| name | Tojil rub'i'. | His name is Tojil. |
| `aj` + place | In aj Iximche'. | I am from Tecpán. |
| negation | Man in tijonel ta. | I am not a teacher. |

`k'o` "exists, is (located), has": `in k'o, at k'o, k'o, öj k'o, ïx k'o, e k'o`.

| Frame | Example | English |
|---|---|---|
| existence | K'o jun tijob'äl pa Chiq'a'l. | There is a school in Comalapa. |
| location | K'o pa jay ri nute'. | My mother is at the house. |
| possession | K'o jun nutz'i'. | I have a dog. |
| none | Majun nupwaq. | I have no money. |
| where | ¿Akuchi' k'o wi ri wuj? | Where is the book? |

## Possession

Set A on the noun. `nuwuj` "my book", `awuj` "your book", `ruwuj`, `qawuj`, `iwuj`, `kiwuj`.
Six behaviors when a noun is possessed:

| Class | Example | Members |
|---|---|---|
| no change | wuj > nuwuj | most nouns, all loans and new words |
| lax vowel tenses | ch'akät > nuch'akat | `-b'äl` instruments/places, `-ik` action nouns |
| drops a suffix | jolomaj > nujolom; te'ej > nute' | body parts, kin |
| adds -Vl | b'aq > nub'aqil | inner body parts, abstracts, inherent possession |
| always possessed | wichin, roma, rik'in | relational nouns |
| suppletive | jay > wochoch | house, blanket, midwife |

Order: possessed noun first, possessor after: `rochoch ri tijonel` "the teacher's house",
`rochoch rutata' ri a Tojil` "Tojil's father's house". `richin ri a Tojil` "it is Tojil's".

## Determiners and demonstratives

| Frame | Meaning | With noun | Fused |
|---|---|---|---|
| re ... re' | this, these (near speaker) | re wuj re' | rere' |
| la ... la' | that, those (far) | la wuj la' | lala' |
| ri ... ri' | that (already known) | ri wuj ri' | riri'; rija' for people |
| ri | the (neutral definite) | ri wuj | |
| jun | a, one | jun wuj | |

Plurality is not in the frame: use `taq` (`taq wuj`), a suffixed plural (`ixoqi'`), or a number.
`ja ri X` "it is X that ..."; `ke ri'` "thus"; `k'a ri'` "then"; `roma ri'` "therefore";
`chi ri'` "there"; `wawe'` "here" (`waral` in the lake towns); `chila'` "over there".

## Negation, questions, word order

Negation is a **frame**: `man` ... `ta` around the negated element. Scope follows the frame.

| Kaqchikel | English |
|---|---|
| Man xb'e ta. | He didn't go. |
| Man in tijonel ta. | I'm not a teacher. |
| Man rin ta ri tijonel. | It isn't ME who is the teacher. |
| Majun nupwäq. | I have no money. |
| Manäq. | No. (the answer word, it does not negate a clause) |
| Man ... ta chik | no longer |
| Majani | not yet |
| Majun b'ey | never |
| Rik'in jub'a' | maybe |

Questions: `la` + statement for yes/no (`¿La yab'e?`), answered `Ja', yib'e.` / `Manäq, man yib'e ta.`
Question words: `achike` who/what/which, `akuchi'` where (+ trace `wi` after the verb: `¿Akuchi'
xab'e wi?`), `jampe` when/how much, `jaru` how much, `achike roma` why, `achike rub'eyal` how,
`achoj ichin` whose, `achoj ik'in` with whom (+ `wi`). Embedded: verb + question word, or verb +
`chi` for "that", or negated verb + `wi` for "whether".

**Word order is VOS**, with V-S for intransitives. Fronting a phrase makes it topic or focus.
When the **agent** is questioned, relativized or focused with `ja`, the verb must go
**antipassive** (`¿Achike xkemon?` "Who wove it?"), never plain transitive.

## Voice, perfect, positionals

| Voice | Shape | Subject | Example |
|---|---|---|---|
| active transitive | ASP-B-A-stem | Set A agent, Set B patient | xukem ri po't "she wove the blouse" |
| passive | ASP-B-stem (tense vowel, or -Vx) | Set B = patient | xkem ri po't "the blouse was woven" |
| antipassive | ASP-B-stem-on / -Vn | Set B = agent | xkemon "she wove / did weaving" |
| middle | stem + -täj / -itäj | Set B | xyojtäj "it got ruined" |

Perfects are non-verbal predicates, not tensed verbs:
intransitive `stem + -inäq/-näq` with free Set B (`in kosinäq` "I'm tired", `b'enäq` "he is gone");
transitive `Set A + stem + -on/-Vn` (`nutz'eton` "I have seen it", `wetaman` "I know").
Contrast the perfect (Set A) with the antipassive (Set B): `nutz'eton` "I have seen it" vs
`yitz'eton` "I see things".

Positional roots (CVC) run through a family of shapes: stative `-Vl` with a lax copy vowel
(`tz'uyül` "seated", free Set B: `in tz'uyül`), intransitive `-e'` (`yitz'uye'` "I sit down"),
transitive `-Vb'a'` (`nintz'uyub'a'` "I seat him"), passive `-Vb'äx`, adjective `-VCik` / plural
`-VCäq` (`setesik` "round").

## Frequently needed frames

| Meaning | Pattern | Example |
|---|---|---|
| want (thing / to do) | Set A + `-ajo'` | ninwajo' jun kape; ninwajo' yib'e |
| would like | `-ajo'` + `ta` | ninwajo' ta jun kape |
| like | `nqa chi` + Set A `-wäch` | nqa chi nuwäch |
| need | `nik'atzin` + `chwe` | nik'atzin chwe jun wuj |
| have to | `k'o chi` + verb | k'o chi yib'e |
| can, be able | Set B + `-tikir` + verb | yitikir yib'e |
| know how | Set A + `-etaman` + verb | wetaman yikemon |
| should | hortative + `ta` | tiqalöq' ta |
| if ... then | `wi` A, B | Wi yape, yiwa'. |
| counterfactual | `manta` A, B `ta` | Manta k'o nupwäq, xtinlöq' ta. |
| because / therefore | B `roma` A / `Roma ri'` B | |
| when / while / even though | `töq` / `loman` / `stape` | |

## Relational nouns

These carry what English does with prepositions. They are obligatorily possessed.

| | of | because of | with | to | self |
|---|---|---|---|---|---|
| 1s | wichin | woma | wik'in | chwe | wi' |
| 2s | awichin | awoma | awik'in | chawe | awi' |
| 3s | richin | roma | rik'in | chre | ri' |
| 1p | qichin | qoma | qik'in | chqe | qi' |
| 2p | iwichin | iwoma | iwik'in | chiwe | iwi' |
| 3p | kichin | koma | kik'in | chike | ki' |

Locatives, shown in the third singular: `pa ruwi'` on top of, `chi ruxe'` under, `chupam` inside,
`chrij` behind/about, `chuwäch` in front of / more than, `chi ruxikin` beside, `chi kikojol`
among them, `pa ruchi'` at the edge of, `chi raqän` at the foot of. `pa` alone is the general
"in, at, on, to". These inflect for any person: `chwij` behind me, `chawäch` in front of you,
`chi kiwäch` in front of them.

## Directionals

Placed after the verb: `pe` hither, `el` away, `apo` thither, `kan` remaining/left behind,
`qa` down, `aqanäj` up. Slot order: VERB + `wi`/`ta` + DIRECTIONAL + object.
`xtzolin pe` "came back", `xuya' kan` "left it", `xwär qa` "fell asleep".

Motion: `-b'e` go, `-pe` come, `-apon` arrive there, `-oqa` arrive here, `-tzolin` return.
Destination takes `pa` for common nouns (`yib'e pa k'ayb'äl`), `chi` for possessed places
(`xkib'e chi wochoch`), and **nothing** for town names (`nb'e Iximche'`).
Go-and-do: ASPECT + Set B + `b'e` + (Set A) + stem: `xb'entz'eta'` "I went to see it".

## Numbers

1 `jun`, 2 `ka'i'`, 3 `oxi'`, 4 `kaji'`, 5 `wo'o'`, 6 `waqi'`, 7 `wuqu'`, 8 `waqxaqi'`,
9 `b'eleje'`, 10 `lajuj`, 11 `julajuj`, 12 `kab'lajuj`, 13 `oxlajuj`, 14 `kajlajuj`, 15 `wolajuj`,
16 `waqlajuj`, 17 `wuqlajuj`, 18 `waqxaqlajuj`, 19 `b'elejlajuj`, 20 `juk'al` / `juwinäq`.
Vigesimal above that: 40 `kak'al`, 60 `oxk'al`, 80 `jumuch'`, 100 `wok'al`, 400 `juq'o'`.
In between, either additive (`juk'al jun` 21) or forward-looking (`jun rukak'al` 21).
Ordinals: `nab'ey, ruka'n, rox, rukaj, ro'` ...

## Survival phrases

| Kaqchikel | English |
|---|---|
| Xseqër k'a. / Xqa q'ij k'a. / Xoq'a' k'a. | Good morning / afternoon / evening. |
| ¿La ütz awäch? - Ütz, matyöx. | How are you? - Fine, thanks. |
| ¿Achike ab'i'? - X nub'i'. | What's your name? - My name is X. |
| ¿Aj akuchi' rat? - In aj X. | Where are you from? - I'm from X. |
| Matyöx (chawe). | Thank you. |
| Man tab'ij ke ri'. / Majun achike ta. | You're welcome. |
| Tab'ana' utzil. | Please. |
| Kinakuyu'. / Takuyu' numak. | Excuse me. / Forgive me. |
| Katok. | Come in. |
| Man wetaman ta. | I don't know. |
| Tab'ij jun b'ey chik. | Say it again. |
| Nq'ax chi nuwäch. / Man nq'ax ta chi nuwäch. | I understand. / I don't understand. |
| Jub'a' yich'o'n pa Kaqchikel. | I speak a little Kaqchikel. |
| ¿Jampe rajil? | How much is it? |
| Chwa'q chik. / Ke ri' k'a. | See you tomorrow. / That's it then. |
| Taya' rutzil ruwäch X. | Give my regards to X. |

## Pitfalls

1. Do not supply a copula. "I am tired" is `In kosnäq`, never with a verb "to be".
2. Do not drop the closing `ta` of a negation, or the closing `re'`/`la'` of a demonstrative.
3. Do not use `manäq` to negate a clause; it is only the answer "no".
4. Do not forget the trace `wi` after the verb in a "where" question or a focused place.
5. Do not use a plain transitive when the **agent** is questioned or focused; use the antipassive.
6. Do not read 2p Set A `i-/iw-` as first person: 1s is `in-/inw-`.
7. Do not flatten the lax vowels. `ä ë ï ö ü` are different phonemes, not accents.
8. Do not stack adjectives before a noun; split into two statements, or let one follow.
9. Do not mark plural twice where the language does not: `taq` and `-a'/-i'` are alternatives,
   and agreement with `e` does the rest.
10. Do not assume a Spanish preposition maps to a Kaqchikel one; use the relational noun.
11. Watch sibling terms, they depend on the sex of the speaker: a man's sister is `wana'`,
    a woman's brother is `nuxib'al`.
12. Title particles before names are lowercase: `a Tojil`, `xta Ixchel`, `ma Kawoq`, `te Ixk'at`.

## Canonical spellings

Where sources differ, these are the citation forms; mention the variant rather than pretending
there is only one. `k'ayb'äl` (var. k'ayib'äl), `matyöx` (var. matyox), `jöb'` (var. jäb'),
`wakami` (var. wakamin, wakamïn), `chuwäch` (contracted chwäch), `rochoch` (never rachoch),
`achib'il` (var. achb'il), `chike` (var. chke), `roma` (not ruma), `mes` "cat", `manq'uq'`
quetzal, `Iximulew` Guatemala.

## Glossing convention

Our labels: **Set A = ergative** (1sA ... 3pA), **Set B = absolutive** (1sB ... 3pB), aspects
COMPL / INCOMPL / POT / IMP. `x-Ø-u-löq'` COMPL-3sB-3sA-buy "she bought it".

**Trap:** most published Kaqchikel grammars use the mirrored letters, where A = absolutive and
E = ergative, and the Chronicles interlinear tags do the same (3Ap = 3pl absolutive, 3Ep = 3pl
ergative, PS = completive). Translate the labels before comparing anything; never string-match
across the two systems, or every person marker inverts.

## Reference files

Load only what the question needs.

| File | Load it when |
|---|---|
| `references/grammar.md` | you need the full pattern tables for a topic: every chapter's grammar compressed into tables |
| `references/paradigms.md` | you need a complete paradigm (all persons, all aspects, both voices, positionals, relational nouns, numbers, time words) or a definition of a grammatical term |
| `references/lexicon.md` | you need vocabulary: 15 domain lists, set phrases and idioms, an English-Kaqchikel finder, and the 400 most frequent corpus words |
| `references/examples.md` | you need attested models: 1,300 verified Kaqchikel/English pairs, arranged by topic |
| `references/usage-and-dialect.md` | the question is about register, town-to-town variation, a competing form, or a known learner error |

These five files are self-contained. Nothing here needs network access, a corpus download,
or any tool beyond reading the files.

## Sources

The grammar and vocabulary here were compiled from published descriptions of Kaqchikel and from
a corpus of attested text: the standard first-year course (Brown, Maxwell and Little,
*¿La ütz awäch?*, 2006), ALMG and Cholsamaj grammars, readers and dictionaries, the dialect
survey *Rujunamaxik ri Kaqchikel Chi'*, Salazar Tetzagüic's literary anthology, Maxwell and
Hill's *Kaqchikel Chronicles*, present-day written Kaqchikel, and unpublished materials used with
their authors' permission. Facts of the language are the common property of its speakers; the
wording, tables and example sentences assembled here are this project's own. Do not name or cite
the unpublished materials.
