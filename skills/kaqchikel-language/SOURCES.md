# Sources

This skill rests on a corpus of Kaqchikel texts. Every source it quotes or counts is listed here
with its credit, its licence or permission status, and what the skill uses it for.

Two kinds of use:

- **Quoted.** Short selections (single sentences, glossary entries, interface strings) appear in
  the reference files, each tagged with its source, e.g. `[rukan p.214]`, `[oxlajuj p.97]`,
  `[nt_central MAT 6:9]`, `[bloom: <book> p.3]`, `[pontoon]`. Only sources whose holders allow it
  are quoted, and only in selections, never as a corpus.
- **Counted.** The attestation counts in `references/lexicon.md` (`N src / M tok`) are whole-word
  counts across all sources below, quoted or not. A count is a fact about a word, not a
  reproduction of anyone's text. Restricted sources are counted and cited, never reproduced.

## Licence of this skill

The repository's CC BY 4.0 licence covers only this project's own text: the explanations, tables,
glosses marked `(our tr.)`, and the selection and arrangement. It does not relicense anything
quoted. Quoted selections stay under their holders' terms:

| Source | Holder's terms |
|---|---|
| Kik'aslemal ri Kaqchikela' (text, glossary, interlinear examples) | Copyright the authors; quoted with their permission |
| Kaqchikel Tijonïk: Oxlajuj Aj (course and glossary) | Copyright the authors; quoted with their permission |
| Runuk'ulem ri Kaqchikel Q'atb'äl Tzij (Kaqchi' Wuj) | Copyright the authors; quoted with permission |
| Rub'eyal kichinan Qach'ab'äl nima'q taq winaqi' (Nelson) | Copyright the author; quoted with permission |
| Wycliffe Kaqchikel New Testaments | CC BY-NC-ND; quoted verbatim only, never respelled |
| Bloom Library readers and picture dictionary | CC BY, CC BY-SA or CC BY-NC-SA 4.0, per book |
| Wikipedia in Kaqchikel (Incubator) | CC BY-SA 4.0 |
| Firefox / Mozilla localization | MPL 2.0 |
| Annals of the Cakchiquels (Brinton) | Public domain |

If you reuse a quoted selection, carry its credit and its holder's terms with it.

## Quoted sources (selections, with credit)

### Kik'aslemal ri Kaqchikela' / Kaqchikel Maya Life
- *Kik'aslemal ri Kaqchikela' / Kaqchikel Maya Life: Advanced Kaqchikel Maya Language*, by
  Waqi' Kan (Walter E. Little), Ixq'anil (Judith M. Maxwell), Kawoq (Baldomero Cuma Chávez) and
  Ixnal (Ambrosia Cuma Chávez); illustrations by Yaxche' Chanquin Cuma. Unpublished draft,
  384 pp.
- Status: **used with the authors' permission.**
- Ids: `rukan_wuj` (the readings and Maxwell's grammar appendix), `rukan_glossary` (Appendix A,
  the trilingual Kaqchikel / Spanish / English glossary), `rukan_interlinear` (the numbered
  Appendix B examples, Maxwell's parses of modern sentences).
- Used for: the main trilingual glosses in the lexicon, example sentences, and modern
  grammatical analysis. Its analysis tier labels A = absolutive, E = ergative; this skill
  writes Set A = ergative, Set B = absolutive and translates the labels before quoting.

### Kaqchikel Tijonïk: Oxlajuj Aj
- Ixq'anil (Judith M. Maxwell) and Waqi' Kan (Walter E. Little). Course packet of the Oxlajuj Aj
  summer program of Kaqchikel language and culture, with a Kaqchikel-Spanish glossary.
- Status: **used with the authors' permission.**
- Ids: `oxlajuj_aj` (lessons, dialogues, student readings), `oxlajuj_glossary` (1,959 headwords
  with Spanish, variants, inflected forms and notes).
- Used for: Spanish glosses, possessed and plural forms, dialogue examples. English glosses
  that this skill adds to its Spanish-only entries are marked `(our tr.)`.

### Runuk'ulem ri Kaqchikel Q'atb'äl Tzij
- Kot Umül and Timothy J. Smith, *Kaqchi' Wuj* 15:9, 2001. A one-page essay in Kaqchikel on the
  indigenous mayoralty of Sololá.
- Status: **used with permission.** Id: `kaqchi_wuj`.
- Used for: short quotations of civic prose. Not strict ALMG spelling.

### Rub'eyal kichinan Qach'ab'äl nima'q taq winaqi' / Adult acquisition of Kaqchikel
- Jun Ajpu' (Brett C. Nelson), Guatemala Scholars Network New Scholars Forum, 2019. Trilingual
  slides.
- Status: **used with permission.** Id: `nelson_2019`.
- Used for: academic neologisms and a long-form date.

### The New Testament in seven Kaqchikel varieties
- Wycliffe Bible Translators, 1993-2012, via eBible.org. **CC BY-NC-ND.**
- Ids: `nt_central`, `nt_chimaltenango`, `nt_eastern`, `nt_solola`, `nt_sacatepequez`, `nt_smj`
  (Santa María de Jesús, written with the saltillo ꞌ for the glottal stop), `nt_yepocapa`
  (Southwestern Yepocapa and Acatenango).
- Used for: verse-tagged examples and dialect comparison of the same verse. They predate the
  ALMG alphabet (c', qu, v), so they say nothing about vowel quality. Quoted verbatim only; any
  respelling into ALMG would be a derivative work, so none is published.

### Bloom Library readers
- Ministerio de Educación de Guatemala and USAID (2012-2021), SIL LEAD and others, via
  bloomlibrary.org. **CC BY, CC BY-SA or CC BY-NC-SA,** as stated on each book's title row.
- Id: `bloom_readers`. Graded primary readers, health leaflets, a home-learning guide, with the
  Spanish printed beside each line.
- Used for: simple modern sentences with their Spanish. Spelling is fast (ütz beside utz), so
  these never settle a vowel.

### Choltzij Kaqchikel ch'ab'äl (picture dictionary)
- Justo Magzul; Ministerio de Educación de Guatemala and USAID, 2021, via Bloom Library.
  **CC BY-NC-SA 4.0.** Id: `bloom_choltzij`.
- Used for: headword confirmation and definitions written in Kaqchikel. Not the ALMG
  terminology dictionary of the same name (below).

### Wikipedia in Kaqchikel (Incubator)
- Volunteer editors of Wp/cak on the Wikimedia Incubator. **CC BY-SA 4.0.** Id: `wiki_incubator`.
- Used for: modern and technical vocabulary in running prose. Uneven quality; only paragraphs
  that read as Kaqchikel were kept.

### Firefox and Mozilla in Kaqchikel
- Mozilla and its Kaqchikel localizers, via Pontoon (Hugging Face `ayymen/Pontoon-Translations`,
  en-cak). **MPL 2.0.** Id: `pontoon_firefox`.
- Used for: coined computer and internet vocabulary (k'amaya'l, kematz'ib', taqoya'l) with the
  English string each one translates.

### The Annals of the Cakchiquels / Memorial de Sololá
- Daniel G. Brinton, 1885. Project Gutenberg #20775. **Public domain.**
- Ids: `annals` (aligned colonial text, ALMG normalization, English), `annals_raw` (the etext).
- Used for: colonial attestations. Pre-ALMG and colonial, so evidence for word shape and
  history, never for modern usage or vowel quality.

## Restricted sources: counted and cited, not reproduced

These are under copyright without reproduction permission. The skill may count words in them
and cite them by title and page or line. Their sentences are never reproduced.

| Id | Work | Credit |
|---|---|---|
| utz_awach | ¿La ütz awäch? Introduction to Kaqchikel Maya Language | Brown, Maxwell & Little, University of Texas Press, 2006 |
| gramatica | Rukemik ri Kaqchikel Chi' / Gramática Kaqchikel | García Matzar & Rodríguez Guaján, Cholsamaj, 1997 |
| dialect | Rujunamaxik ri Kaqchikel Chi' / Variación Dialectal en Kaqchikel | Patal Majzul et al. (OKMA), Cholsamaj, 2000 |
| chronicles | Kaqchikel Chronicles: The Definitive Edition | Maxwell & Hill, 2006 |
| lectoescritura2 | Ruka'n Kaqchikel Sik'itz'ib'anem (Lectoescritura Kaqchikel No. 2) | Cholsamaj |
| nabey | Ri nab'ey taq nusik'inem, Kaqchikel | Ministerio de Educación, Guatemala |
| kaq3 | Kaqchikel 3, Tercero primaria | Ministerio de Educación, Guatemala |
| kojtzijon | Kojtzijon pa Kaqchikel Ch'ab'äl / Conversemos en idioma Kaqchikel | ALMG, 2003 |
| neologismos | Criterios para la Creación de Neologismos en Kaqchikel | UNICEF / Kaqchikel Cholchi' |
| literatura | Rupach'uxik kina'oj qati't qamama' / Características de la literatura maya kaqchikel | Salazar Tetzagüic, Cholsamaj, 1995 |
| choltzij | Kaqchikel Choltzij (terminology dictionary of old and new words) | ALMG |
| vocab_es_kaq | Vocabulario Español - Kaqchikel | ALMG |
| mormon_dict | Diccionario Español-Cakchiquel-Inglés | Blair, Robertson, Richman et al., BYU/Garland, 1981 |
| kqc_bible | Ri Loq'oläj Wuj (the Kaqchikel Bible, KQC) | Sociedad Bíblica de Guatemala, 2003 |
| bom | Selections from the Book of Mormon in Kaqchikel | Intellectual Reserve |
| fb | Contemporary Kaqchikel from public Facebook posts | Comunidad Lingüística Kaqchikel-ALMG, Sara Curruchich, Editorial Cholsamaj and other public pages |
| social | Kaqchikel on X and Facebook (2026 harvest) | Comunidad Lingüística Kaqchikel-ALMG, Prensa Comunitaria, Gelder Vasquez and other public accounts |
| curruchich | Song lyrics | Sara Curruchich (some tracks with Rebeca Lane, Lila Downs, Amparo Sánchez, Edu Falaschi) |
| broadwell | Word Order and Markedness in Kaqchikel | George Aaron Broadwell, Proceedings of LFG00, CSLI, 2000 |
| koechert | Maintenance of Kaqchikel Ritual Speech in the Confraternities of San Juan Sacatepéquez | Andreas Koechert & Barbara Pfeiler, IJSL 220, 2013 |
| tummons_medical | So that We Don't Lose Words: Reconstructing a Kaqchikel Medical Lexicon | Emily Tummons, Robert Henderson & Peter Rohloff, Indiana University, 2011 |
| tummons_positionals | Positional Roots in Kaqchikel Maya | Emily J. Tummons, MA thesis, University of Kansas, 2010 |
| web_news | Kaqchikel news and civil-society writing from the web | La Hora, La Luciérnaga (Agencia Ocote), Cultural Survival, AMARC Guatemala, Global Voices, Sotz'il, Wuqu' Kawoq, Kaqchi' Wuj and others, via FineWeb-2 and FinePDFs |
| web_public_docs | Government and institutional documents in Kaqchikel | ALMG, Government of Guatemala (SCEP, MIDES, SAT, FODIGUA, municipality of Patzún and others), OHCHR, OSHA, ICEFI, LAPOP and others, via FineWeb-2 and FinePDFs |

Each of these is **counted and cited, not reproduced.**

Two further sources have no licence established yet and are treated as restricted, so they too
are **counted and cited, not reproduced**:

| Id | Work | Credit |
|---|---|---|
| swarthmore | Kaqchikel Talking Dictionary | Living Tongues Institute / Swarthmore College |
| tajo_awi | Tajo' awi' (Love Yourself), video subtitles | INEB Santo Domingo Xenacoj |

## How counts are made

Counts are whole-word, case-insensitive matches
over the Kaqchikel text of every source above (a bilingual table contributes only its Kaqchikel
column), after folding ’ ‘ ʼ ꞌ to the straight apostrophe. A stem written with a leading hyphen
(`-ochoch`) also counts its prefixed forms (`wochoch`, `rochoch`). Sources in pre-ALMG spelling
(the New Testaments, the colonial texts) are counted as written, so a word they spell with c' or
qu does not register there.
