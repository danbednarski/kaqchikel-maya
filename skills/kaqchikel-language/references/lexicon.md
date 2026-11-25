# Kaqchikel working lexicon

A trilingual working lexicon of about 1188 high-value words: the common core plus the words a
model tends to invent or get wrong (irregular possessed forms, kin terms that depend on the
speaker's sex, lax vowels, Spanish look-alikes). Grep it in any of the three languages.

Columns:

- **Kaqchikel**: ALMG spelling as the glossary gives it. A leading hyphen (`-ochoch`, `-achik'aj`)
  marks a bound stem: a possessed-only noun or a verb root that never appears bare.
- **POS**: n noun; n.poss noun that is always possessed; v.t transitive verb; v.i intransitive
  verb; v verb whose transitivity the sources do not settle here; pos positional root;
  adj adjective; adv adverb; num number; pron pronoun; part particle, preposition or
  conjunction; rel relational noun; phr phrase or idiom; name proper name.
- **English / Español**: the source's own glosses. An English gloss we supplied for a
  Spanish-only entry ends in `(our tr.)`.
- **Forms / notes**: possessed, plural or inflected forms and variants the sources give, plus
  our notes on traps (marked `NB`).
- **Attest.**: whole-word count across all 46 corpus sources (quotable and restricted,
  apostrophes normalized): `N src / M tok` = found in N sources, M tokens in all. A bound stem
  counts its prefixed forms (and so over-counts a short stem). Counts do not separate
  homographs: kan "snake" shares its count with the particle kan, rey "his tooth" with Spanish
  rey. Treat under 3 sources as rare or specialized. Pre-ALMG sources (New Testaments,
  colonial texts) do not register words they spell with c' or qu.
- **Src**: where the gloss comes from: `rukan` = Kik'aslemal ri Kaqchikela' glossary
  (Little, Maxwell, Cuma Chávez & Cuma Chávez, with permission); `ox p.N` = Oxlajuj Aj
  glossary page N (Maxwell & Little, with permission); `bloom` = Choltzij Kaqchikel ch'ab'äl
  (Magzul 2021, CC BY-NC-SA); `pontoon` = Firefox localization (MPL 2.0); `wiki` = Kaqchikel
  Wikipedia (CC BY-SA). Full credits in `../SOURCES.md`.

## Words models get wrong

Irregular possessed forms (a different stem, a dropped -aj, an inherent -Vl suffix), kin terms chosen by the speaker's sex, lax vowels that tense under a suffix, and Spanish look-alikes. These rows are not repeated in the main table.

| Kaqchikel | POS | English | Español | Forms / notes | Attest. | Src |
|---|---|---|---|---|---|---|
| jay | n | house (our tr.) | casa | NB 'my house' uses a different stem: wochoch my house, rochoch his/her house (-ochoch); nujay means 'my lineage', not 'my house' | 37 src / 4572 tok | ox p.102 |
| ixöq | n | woman (our tr.) | mujer | pl. ixoqi' (lax ö tenses before the suffix); NB "my wife" is wixjayil, not *wixöq | 21 src / 372 tok | ox p.102 |
| -ixjayil | n.poss | wife (our tr.) | esposa | wixjayil my wife, rixjayil his wife; ox also writes wixjayïl; abs. ixjayilonel | 20 src / 818 tok | ox p.102 |
| achin | n | man (our tr.) | hombre | pl. achi'a'; NB "my husband" is wachijil, not *wachin | 20 src / 2930 tok | ox p.92 |
| -achijil | n.poss | husband (our tr.) | esposo | wachijil my husband, rachijil her husband; abs. achijilonel | 14 src / 473 tok | ox p.92 |
| ak'wal | n | child (our tr.) | niño | pl. ak'wala'; NB "my child" is walk'wal, not *wak'wal | 25 src / 417 tok | ox p.93 |
| -alk'wal | n.poss | son or daughter (our tr.) | hijo/a | walk'wal my child (either parent); abs. alk'walaxel | 15 src / 89 tok | ox p.94 |
| -al | n.poss | a woman's child (our tr.) | hijo/a de una mujer | wal ala' my son, ral xtän her daughter; NB only a mother says wal | 18 src / 105 tok | ox p.93 |
| -k'ajol | n.poss | a man's son (our tr.) | hijo (de hombre) | nuk'ajol my son (father speaking); abs. k'ajolaxel | 22 src / 2698 tok | ox p.106 |
| -mi'al | n.poss | a man's daughter (our tr.) | hija (de hombre) | numi'al my daughter (father speaking); var. nume'al; abs. mi'alaxel | 19 src / 515 tok | ox p.110 |
| -chaq' | n.poss | younger sibling of the same sex as the speaker (our tr.) | hermano/a menor del mismo sexo del hablante | nuchaq'; abs. chaq'laxel; NB a man's younger brother, a woman's younger sister | 22 src / 272 tok | ox p.97 |
| -nimal | n.poss | older sibling of the same sex as the speaker (our tr.) | hermano/a mayor del mismo sexo del hablante | nunimal; abs. nimalaxel; plural nimalaxela' also = principal stewards (cofradía) [rukan] | 32 src / 536 tok | ox p.111 |
| -xib'al | n.poss | a woman's brother (our tr.) | hermano (de mujer) | nuxib'al; abs. xib'alon; NB any brother, older or younger, of a female speaker | 13 src / 50 tok | ox p.124 |
| -ana' | n.poss | a man's sister (our tr.) | hermana (de hombre) | wana'; archaic anab'axel; NB any sister, older or younger, of a male speaker | 15 src / 38 tok | ox p.94 |
| -ach'alal | n.poss | family, relatives (our tr.) | familia | awach'alal your family; standard written ach'alalri'il; also "brother" in church usage | 30 src / 4857 tok | ox p.92 |
| te'ej | n | mother (our tr.) | madre | nute', nte' my mother; ate' your mother | 28 src / 331 tok | ox p.119 |
| tata'aj | n | father (our tr.) | padre | nutata', nata' my father; atata' your father | 27 src / 554 tok | ox p.119 |
| mama'aj | n | grandfather (our tr.) | abuelo | numama' my grandfather; NB mama' alone also = old man, elder; mama' äk' = rooster | 13 src / 65 tok | ox p.109 |
| ati't | n | grandmother (our tr.) | abuela | wati't my grandmother | 14 src / 60 tok | ox p.94 |
| -mam | n.poss | grandchild of a grandfather (our tr.) | nieto/a de abuelo | numam ala' my grandson, rumam xtän his granddaughter; NB not "grandfather" (that is mama') | 9 src / 18 tok | ox p.109 |
| -jinan | n.poss | a man's father-in-law (our tr.) | suegro (de hombre) | nujinan; a woman says walinan | 10 src / 48 tok | ox p.103 |
| -alinan | n.poss | a woman's father-in-law (our tr.) | suegro (de mujer) | wal(i)nan | 5 src / 10 tok | ox p.93 |
| -jite' | n.poss | a man's mother-in-law (our tr.) | suegra (de hombre) | nujite'; a woman says walite' | 11 src / 58 tok | ox p.103 |
| -alite' | n.poss | a woman's mother-in-law (our tr.) | suegra (de mujer) | walte' | 11 src / 44 tok | ox p.93 |
| jolomaj | n | head (our tr.) | cabeza | nujolom my head: the absolute -aj drops when possessed; var. nujolon; wi'aj in some towns | 23 src / 117 tok | ox p.103 |
| q'ab'aj | n | arm, hand (our tr.) | brazo | nuq'a', ruq'a' (stem -q'a'); NB never *nuq'ab'aj | 20 src / 180 tok | ox p.115 |
| aqanaj | n | leg, foot (our tr.) | pierna/pie | raqän, awaqän: -aj drops and the stem shows a lax ä | 13 src / 78 tok | ox p.94 |
| chi'aj | n | mouth (our tr.) | boca | nuchi', ruchi'; ruchi' also = edge, shore, its opening | 12 src / 51 tok | ox p.97 |
| wi'aj | n | hair, head (our tr.) | pelo, cabeza | nuwi'; ruwi' also = its top, on top (pa ruwi') | 18 src / 91 tok | ox p.123 |
| pamaj | n | stomach, belly (our tr.) | estómago, panza, vientre | nupam, apan; rupam also = inside of (relational) | 15 src / 93 tok | ox p.113 |
| eyaj | n | tooth (our tr.) | diente | wey my tooth, rey its edge; NB counts for wey/rey are swamped by Spanish rey "king" | 18 src / 87 tok | ox p.101 |
| -xikinaj | n | ear; earrings (our tr.) | aretes, oreja | nuxikïn, ruxikin my/his ear; wichinaj my earrings | 10 src / 40 tok | ox p.124 |
| tz'umaj | n | woman's breast (our tr.) | pechos de mujer, chiche | rutz'um | 15 src / 53 tok | ox p.122 |
| b'aq | n | bone (our tr.) | hueso | NB nub'aqil my bone (in my body, inherent -il) vs nub'aq my bone (an animal's, one I own) | 19 src / 126 tok | ox p.95 |
| kik' | n | blood (our tr.) | sangre | nukik'el my blood (inherent -el) | 15 src / 231 tok | ox p.105 |
| ch'akulaj | n | body (our tr.) | cuerpo | ach'akul your body; also ch'akulal | 16 src / 191 tok | ox p.98 |
| ti'ij | n | meat (our tr.) | carne | NB ruti'ojil his flesh (own body, -il) vs ruti'ij his meat (food) | 24 src / 496 tok | ox p.119 |
| ulew | n | earth, land (our tr.) | tierra | rulewal its land, territory (inherent -al) | 28 src / 1276 tok | ox p.122 |
| wäy | n | tortilla (our tr.) | tortilla | nuway my tortilla, my food: lax ä tenses when possessed | 18 src / 213 tok | ox p.123 |
| tzyäq | n | clothes (our tr.) | ropa | nutzyaq my clothes (lax ä tenses); rukan: tela, ropa / fabric, cloth, clothes | 15 src / 144 tok | ox p.121 |
| winäq | n | person, people (our tr.) | gente, persona | pl. winaqi'; lax ä tenses before -i' | 22 src / 1401 tok | ox p.123 |
| mes | n | cat; trash (some towns) (our tr.) | gato; basura (en algunos pueblos) | NB not Spanish mes "month" (month = ik'); syan in some towns, xiwan = wildcat | 23 src / 141 tok | ox p.109 |
| ik' | n | moon, month (our tr.) | luna, mes | jun ik' one month | 30 src / 1054 tok | ox p.101 |
| kej | n | horse; deer (calendar Kej) (our tr.) | caballo; venado | taq kej horses; NB the same word for horse and deer | 21 src / 298 tok | ox p.105 |
| kaxlan | adj | foreign, from outside (our tr.) | extranjero | kaxlan wäy bread (lit. foreign tortilla), kaxlan ik'oy onion, kaxlan tzij Spanish | 23 src / 639 tok | ox p.105 |
| utz | adj | good (our tr.) | bueno | ALMG ütz; utzil favor, rutzil its goodness, matyöx/maltyox thanks | 25 src / 2770 tok | ox p.122 |
| roma | part | because (our tr.) | por eso, porqué | NB standard written roma; ruma is a common dialect/Bible spelling | 26 src / 35093 tok | ox p.116 |

## Cholq'ij day names

The twenty days of the 260-day ritual calendar, written capitalized as names. Each is also an ordinary noun (Kej = deer).

| Kaqchikel | POS | English | Español | Forms / notes | Attest. | Src |
|---|---|---|---|---|---|---|
| Imox | name | day name (our tr.) | nombre de día (our tr.) |  | 10 src / 56 tok |  |
| Iq' | name | wind; day name (our tr.) | viento, nombre caléndrico del cholq'ij |  | 8 src / 69 tok | ox p.101 |
| Aq'ab'al | name | night, dawn; day name (our tr.) | noche, nombre caléndrico del cholq'ij |  | 11 src / 27 tok | ox p.94 |
| K'at | name | net; day name (our tr.) | red, nombre caléndrico de cholq'ij | ox prints "rede" | 12 src / 90 tok | ox p.107 |
| Kan | name | snake; day name (our tr.) | serpiente, nombre caléndrico de cholq'ij | NB count includes the frequent particle kan "really, indeed" | 30 src / 39480 tok | ox p.104 |
| Kamey | name | death; day name (our tr.) | muerte, nombre caléndrico del cholq'ij | -kam die; not Kame, the K'iche' form | 11 src / 52 tok | ox p.104 |
| Kej | name | deer; day name (our tr.) | venado, nombre caléndrico del cholq'ij | ordinary kej = horse | 21 src / 298 tok | ox p.105 |
| Q'anil | name | rabbit, Venus; day name (our tr.) | conejo, venus, día del calendario sagrado |  | 8 src / 22 tok | ox p.115 |
| Toj | name | rain; day name (our tr.) | lluvia, nombre caléndrico |  | 18 src / 84 tok | ox p.120 |
| Tz'i' | name | dog; day name (our tr.) | perro, nombre caléndrico | ordinary tz'i' = dog | 29 src / 394 tok | ox p.121 |
| B'atz' | name | day in the sacred calendar, howler monkey | día en el calendario sagrado, zaraguate, mono aullador | b'atz' also = thread | 19 src / 232 tok | rukan |
| Ey | name | tooth; day name (our tr.) | diente, nombre calendario del cholq'ij | not E, the K'iche' form; ordinary eyaj = tooth | 14 src / 113 tok | ox p.101 |
| Aj | name | reed, cane; day name (our tr.) | caña, nombre caléndrico del cholq'ij | ordinary aj = cane, also skyrocket | 38 src / 10393 tok | ox p.92 |
| I'x | name | jaguar; day name (our tr.) | jaguar, nombre caléndrico del cholq'ij |  | 5 src / 8 tok | ox p.101 |
| Tz'ikin | name | bird; day name (our tr.) | pájaro, nombre caléndrico | pl. tz'ikina' birds, clan; also a man's name | 17 src / 97 tok | ox p.121 |
| Ajmaq | name | day name (our tr.) | nombre caléndrico del cholq'ij |  | 11 src / 64 tok | ox p.93 |
| No'j | name | incense; day name (our tr.) | incienso, nombre caléndrico |  | 15 src / 236 tok | ox p.111 |
| Tijax | name | flint; day name (our tr.) | pedernal, nombre caléndrico de cholq'ij |  | 14 src / 140 tok | ox p.119 |
| Kawoq | name | day name (our tr.) | nombre de día (our tr.) | also a man's name | 8 src / 52 tok |  |
| Ajpu' | name | day name (our tr.) | nombre de día (our tr.) | also a man's name | 12 src / 83 tok |  |
| ajq'ij | n | daykeeper, spiritual guide (our tr.) | guía espiritual, contador de los días (our tr.) | pl. ajq'ija'; rukan glosses ajpatan as "lay brother, daykeeper" | 12 src / 107 tok |  |
| cholq'ij | n | the 260-day sacred calendar (our tr.) | calendario sagrado (our tr.) | NB the sources write cholq'ij (ch'olq'ij: no hits); nawal = the day's spirit | 12 src / 157 tok |  |
| nawal | n | spirit, guardian spirit of a day (our tr.) | nahual, espíritu (our tr.) | kinawal their nawal | 13 src / 55 tok |  |

## Main lexicon (alphabetical)

| Kaqchikel | POS | English | Español | Forms / notes | Attest. | Src |
|---|---|---|---|---|---|---|
| A | part | young man (title for unmarried youths in some towns, married in others) (our tr.) | jóven |  | 38 src / 17990 tok | ox p.92 |
| a' | n | measure for counting years (our tr.) | med. para contar años | Juna' | 14 src / 258 tok | ox p.92 |
| -a' | n.poss | calf (of the leg) (our tr.) | pantorilla |  | 14 src / 258 tok | ox p.92 |
| ab'äj | n | stone (our tr.) | piedra | taq ab'äj | 20 src / 209 tok | ox p.92 |
| ach'alal ri'ïl | n | brotherhood, fraternity (our tr.) | hermandad, fraternidad |  | 7 src / 51 tok | ox p.92 |
| ach- | aff | prefix conveying company, collaboration (our tr.) | prefijo. que envuelve la idea de compañia, colaboración |  | 44 src / 42015 tok | ox p.92 |
| achi'a' | n | men (our tr.) | hombres |  | 31 src / 7275 tok | ox p.92 |
| achi'el | part | like, just as (our tr.) | como, así como |  | 24 src / 9358 tok | ox p.92 |
| achib'il | n.poss | companion, friend, sometimes husband (our tr.) | compañero, amigo, a veces se usa para esposo | iwachilb'il | 8 src / 84 tok | ox p.92 |
| achib'äl | n | photo, image (our tr.) | foto, imagen | re achib'äl re'; la achib'äl la' | 12 src / 104 tok | ox p.92 |
| achijilonel | n | husband (our tr.) | esposo | wachijil | 6 src / 18 tok | ox p.92 |
| -achik' | v.i | dream (our tr.) | soñar | tachik'; ke'achik' | 18 src / 261 tok | ox p.92 |
| -achik'aj | v.t | dream | soñar | xatinwachik'aj; k'a xkinawachik'aj | 12 src / 63 tok | rukan ox p.92 |
| achike | part | what, who (our tr.) | qué, quién |  | 26 src / 5443 tok | ox p.92 |
| achike na k'a | phr | depending on (our tr.) | a según |  | 6 src / 12 tok | ox p.92 |
| achike roma | part | why, what is its cause? (our tr.) | porqué, ¿Que es su causa? |  | 8 src / 764 tok | ox p.92 |
| achk'uljay | n | neighbor (our tr.) | vecino |  | 8 src / 15 tok | ox p.92 |
| achäq | n | butt, euphemism for shit (not a polite word) (our tr.) | culo, eufemismo para mierda (no es palabra muy decente) |  | 6 src / 16 tok | ox p.92 |
| aj juk'an ya' | n | foreigner, one who comes from across the sea (our tr.) | extranjero, que viene del otro lado del mar |  | 7 src / 8 tok | ox p.92 |
| aj pa q'ayis | n | guerrilla fighter ; leftist soldier (our tr.) | guerrillero; soldado de la izquierda guerrilla |  | 6 src / 21 tok | rukan |
| aj'ik' | n | maid, servant (our tr.) | criada, sirvienta |  | 7 src / 11 tok | ox p.93 |
| aj'itz | n | sorcerer, diviner (who does harm), witch, magician (our tr.) | brujo, agorero (el que hace mal), hechicero, mago |  | 7 src / 11 tok | ox p.93 |
| ajache'l | n | white sapote (matasano) (our tr.) | matasano |  | 12 src / 64 tok | ox p.92 |
| ajanel | n | carpenter, sculptor (our tr.) | carpintero, escultor |  | 9 src / 41 tok | ox p.92 |
| ajaw | n | lord, owner, boss (our tr.) | señor, dueño, jefe |  | 26 src / 1530 tok | ox p.92 |
| ajawarem | n | kingdom, dominion (our tr.) | reino, dominación |  | 8 src / 35 tok | ox p.92 |
| ajch'ame'y | n | indigenous authority | alguacil, alcalde, regidor, autoridad sheriff, mayor, alderman, indígena |  | 9 src / 17 tok | rukan ox p.92 |
| ajil | n | sadness, melancholy (our tr.) | tristeza, melancolía |  | 10 src / 48 tok | ox p.92 |
| ajilab'äl | n | number (our tr.) | número | jun; ka'i'; oxi'; kaji'; wo'o'; waqi'; wuqu'; waqxaqi' | 14 src / 165 tok | ox p.93 |
| -ajilaj | v.t | count | contar (Tawajlaj. Cuente.) ; contar |  | 20 src / 49 tok | rukan ox p.93 |
| -ajilan | v.i | count (our tr.) | contar | kinajilan; kojajilan | 16 src / 57 tok | ox p.93 |
| -ajin- | aff | is X-ing (our tr.) | está X-ando |  | 39 src / 6159 tok | ox p.92 |
| ajk'ot | n | sculptor, carver (our tr.) | escultor, tallador |  | 9 src / 12 tok | ox p.93 |
| ajkem | n | weaver (our tr.) | tejedora |  | 7 src / 36 tok | ox p.93 |
| ajmak | n | sinner, wrongdoer, criminal (our tr.) | pecador, vicioso, criminal |  | 6 src / 13 tok | ox p.93 |
| ajna'oj | n | knowledgeable, expert, wise, skilled (our tr.) | entendido, experto, sabio, perito |  | 8 src / 21 tok | ox p.93 |
| -ajo' | v.t | want (our tr.) | querer | ¿janpe nawajo'? | 36 src / 9091 tok | ox p.93 |
| ajowab'äl | n | love (our tr.) | amor |  | 12 src / 173 tok | ox p.93 |
| ajpatan | n | lay brother, daykeeper | cofrade, ajq'ij ; los recaudadores de las cofradías |  | 11 src / 22 tok | rukan ox p.93 |
| ajpop | n | chief, principal, leader (our tr.) | cacique mayor, principal, dirigente, líder |  | 13 src / 94 tok | ox p.93 |
| Ajpub' | name | hunter, blowgunner ; day name (our tr.) | cazador, cerbatanero/ nombre caléndrico del cholq'ij |  | 7 src / 83 tok | ox p.93 |
| ajsamaj | n | lay brother; anyone with a spiritual charge | cofrade; cualquier persona con un cargo espiritual |  | 8 src / 41 tok | rukan |
| ajtij | n | teacher (our tr.) | maestro | ajtija' | 8 src / 44 tok | ox p.93 |
| ajtun | n | trumpeter (our tr.) | trompetero |  | 6 src / 12 tok | ox p.93 |
| ajtz'aq | n | architect, mason (our tr.) | architecto, albañil |  | 8 src / 29 tok | ox p.93 |
| ajtz'ib' | n | secretary, writer | secretari@, escritor ; secretario, escritor |  | 17 src / 56 tok | rukan ox p.93 |
| ajyuq' | n | priest, shepherd (our tr.) | cura sacerdote, pastor |  | 9 src / 47 tok | ox p.93 |
| ak' | n | chia seed (our tr.) | semilla de chian |  | 12 src / 42 tok | ox p.93 |
| -ala' | aff | repeatedly, with multiple patients (our tr.) | repetidamente, con múltipes pacientes |  | 35 src / 2902 tok | ox p.94 |
| ala' | n | young man (our tr.) | joven |  | 26 src / 1222 tok | ox p.94 |
| ala's | n | doll, scarecrow (our tr.) | muñeco, espantajo |  | 9 src / 20 tok | ox p.94 |
| alab'o' | n | young people (our tr.) | jovenes | var. alab'om, alab'oni' (estandard escrita) | 6 src / 10 tok | ox p.94 |
| alaj | adj | young, small (our tr.) | joven, pequeño | alaji' | 27 src / 648 tok | ox p.94 |
| alaxib'äl | n | birth, source, spring | nacimiento, fuente ; nacimiento, Navidad |  | 9 src / 10 tok | rukan ox p.94 |
| alib'ätz | n | sister-in-law (of a woman), daughter-in-law (of a man) (our tr.) | cuñada (de mujer)/nuera (de hombre) | wali' - | 6 src / 13 tok | ox p.94 |
| -aläx | v.i | be born | nacer |  | 16 src / 160 tok | rukan |
| amaq' | n | town, nation (our tr.) | pueblo, nación |  | 16 src / 475 tok | ox p.94 |
| amaq'el | adv | constantly, steadily ; neighbor, settled resident (our tr.) | constantement, con fijeza; vecino, el que está fijo en algún pueblo |  | 9 src / 29 tok | ox p.94 |
| amolo' | n | fly (our tr.) | mosca |  | 10 src / 35 tok | ox p.94 |
| -anin | v.i | run (our tr.) | correr | katanin; kixanin | 34 src / 1855 tok | ox p.94 |
| aninäq | adv | lightly, quickly, soon (our tr.) | a la ligera, rápido, pronto |  | 14 src / 288 tok | ox p.94 |
| anom | n | scarecrow (our tr.) | espantapájaro |  | 6 src / 14 tok | ox p.94 |
| anx | n | garlic (our tr.) | ajo |  | 9 src / 15 tok | ox p.94 |
| ape' | part | how far? (our tr.) | ¿Hasta dónde? |  | 7 src / 490 tok | ox p.94 |
| apo | adv | toward there (our tr.) | para allá |  | 27 src / 5814 tok | ox p.94 |
| -apon | v.i | arrive there (our tr.) | llegar allí | kinapon; kojapon | 34 src / 7715 tok | ox p.94 |
| apon | adj | next (our tr.) | próximo |  | 19 src / 400 tok | ox p.94 |
| aq | n | pig (our tr.) | marrano | k'ixawuch'; k'ixa aq | 20 src / 114 tok | ox p.94 |
| aq' | n | tongue (our tr.) | lengua | awaq' | 9 src / 30 tok | ox p.94 |
| aq'a' | n | night (our tr.) | noche |  | 23 src / 612 tok | ox p.94 |
| aq'a'l | n | charcoal, ember, live coal (our tr.) | carbón, pavesa, brasa |  | 7 src / 11 tok | ox p.94 |
| aq'aj | n | tongue (our tr.) | lengua |  | 7 src / 13 tok | ox p.94 |
| aq'awinäq | n | racoon | mapache |  | 9 src / 21 tok | rukan ox p.94 |
| aq'om | n | medicine | medicina |  | 20 src / 336 tok | rukan ox p.94 |
| -aq'omaj | v.t | cure, treat with medicine, add spices to food, poison | curar, tratar con medicina, envenenar |  | 15 src / 115 tok | rukan ox p.94 |
| aq'omanel | n | doctor (our tr.) | médico, doctor | Ri nute' aq'omanel. | 19 src / 144 tok | ox p.94 |
| aqaj | n | black bee (our tr.) | abeja negra |  | 9 src / 17 tok | ox p.94 |
| armita | n | great room of the cofradia, lit. hermitage ; Guatemala City | sala grande de cofradía, ermita ; Ciudad de Guatemala ; Guatemala | neo. Chiche' | 17 src / 117 tok | rukan ox p.94 |
| -atin | v.i | bathe (our tr.) | bañarse | katatin; Rïx kixatin; xinatinisaj; yinatin; xkojatin | 27 src / 288 tok | ox p.94 |
| atux | part | what? (our tr.) | ¿qué? |  | 10 src / 267 tok | ox p.94 |
| atz'am | n | salt | sal | var. atz'an | 15 src / 77 tok | rukan ox p.94 |
| awex | n | small cornfield (our tr.) | milpa pequeña |  | 10 src / 34 tok | ox p.95 |
| aws | n | fava beans (our tr.) | habas | var. jaws | 7 src / 20 tok | ox p.95 |
| awäj | n | domestic animal (our tr.) | animal doméstico |  | 13 src / 61 tok | ox p.95 |
| awän | n | cornfield: corn with its inter- crops, e.g., beans and squash. | milpa | rawän | 17 src / 176 tok | rukan ox p.95 |
| ayin | n | lizard, caiman (our tr.) | largarto | var. ayim | 12 src / 34 tok | ox p.95 |
| -b'a'on | v.i | bark (our tr.) | ladrar |  | 8 src / 22 tok | ox p.95 |
| b'alam | n | tiger, jaguar (our tr.) | tigre, jagar | b'alami' | 20 src / 298 tok | ox p.95 |
| -b'anatäj | v.i | happen, occur (our tr.) | pasar, suceder |  | 16 src / 316 tok | ox p.95 |
| -b'anob'al | n.poss | culture | cultura |  | 16 src / 258 tok | rukan |
| b'anob'äl | n | place or tool for doing, culture (our tr.) | lugar o instrumento con que se hace, cultura |  | 19 src / 343 tok | ox p.95 |
| b'anoj | n | verb (our tr.) | verbo |  | 16 src / 254 tok | ox p.95 |
| -b'atz'in | v.i | spin thread, twist thread | hacer hilo, entorchar hilo ; gritar (animales) |  | 10 src / 28 tok | rukan ox p.95 |
| b'ay | n | mole | taltuza, topo |  | 15 src / 443 tok | rukan ox p.95 |
| -b'ayb'öt | v.i | tremble with cold, shiver | temblar de frío |  | 7 src / 16 tok | rukan |
| b'ey | n | time (occurrence) ; street, road, way of doing, method (our tr.) | vez ; calle, camino, modo de hacer algo, método | k'o b'ey; jampe b'ey; junjun b'ey; jantäq b'ey | 31 src / 1283 tok | ox p.95 |
| -b'eyal | n.poss | manner | manera |  | 26 src / 1859 tok | rukan |
| b'eyal | n | manner, composition (our tr.) | (ru) modo, composición |  | 13 src / 150 tok | ox p.96 |
| b'eyom | adj | rich, wealthy (our tr.) | rico, adinerado | b'eyoma' | 7 src / 32 tok | ox p.96 |
| b'eyomäl | n | wealth (our tr.) | riqueza |  | 6 src / 20 tok | ox p.96 |
| b'i'aj | n | name (our tr.) | nombre | rub'i' | 18 src / 801 tok | ox p.96 |
| -b'ij | v.t | say (our tr.) | decir | tab'ij | 29 src / 2939 tok | ox p.96 |
| -b'ini'an | v.i | be called, be named, be designated | denominar, ser nombrado, ser designado |  | 9 src / 131 tok | rukan |
| -b'inisaj- | v.t | make walk (our tr.) | hacer caminar | xinb'inisaj; man nab'inisaj ta | 7 src / 23 tok | ox p.96 |
| b'is | adj | sad (our tr.) | triste |  | 17 src / 79 tok | ox p.96 |
| -b'isoj | v.t | sadden (our tr.) | entristecer |  | 8 src / 17 tok | ox p.96 |
| -b'ison- | v.i | become sad (our tr.) | entristecerse | nib'ison | 17 src / 161 tok | ox p.96 |
| B'itol | name | Creator (mentioned in the Popol Wuj) (our tr.) | Creador (el Pop Wuj lo menciona) |  | 7 src / 23 tok | ox p.96 |
| b'ix | n | song (our tr.) | canción |  | 21 src / 94 tok | ox p.96 |
| -b'ixaj | v.t | sing (our tr.) | cantar |  | 13 src / 40 tok | ox p.96 |
| -b'ixan | v.i | sing (antipassive) (our tr.) | cantar (antipassivo) | yab'ixan; kab'ixan; kixb'ixan; yitikïr yib'ixan | 18 src / 167 tok | ox p.96 |
| b'ixanel | n | singer (our tr.) | cantante | var. ajb'ix | 12 src / 35 tok | ox p.96 |
| -b'iyaj | v.i | go, walk, stroll (our tr.) | irse, caminar, pasear | xb'eb'iyaj | 10 src / 54 tok | ox p.96 |
| -b'iyin- | v.i | walk (our tr.) | caminar | kixb'iyin; kab'iyin; xojb'iyin; xkojb'iyin | 24 src / 344 tok | ox p.96 |
| b'o'j | n | cotton | algodón |  | 8 src / 30 tok | rukan ox p.96 |
| b'ojo'y | n | pot | olla |  | 14 src / 182 tok | rukan ox p.96 |
| B'oko' | name | Chimaltenango (our tr.) | Chimaltenango | var. B'okob' lugar de escudos | 15 src / 77 tok | ox p.96 |
| b'ol- | pos | rolled up (our tr.) | enrollado | b'olon; b'olob'ïk; b'olob'äq | 16 src / 131 tok | ox p.96 |
| b'oloj | n | hill up a cornstalk with earth against the wind | calzado de maíz |  | 9 src / 17 tok | rukan |
| -b'oloj | v.t | make large mounds (our tr.) | hacer grandes montículos |  | 9 src / 17 tok | ox p.96 |
| -b'onij | v.t | paint, color (our tr.) | pintar, colorar | xab'onij awi' | 10 src / 78 tok | ox p.96 |
| -b'onil | n.poss | color (our tr.) | (ru) color |  | 17 src / 617 tok | ox p.96 |
| b'oq' | n | tamale (our tr.) | tamal |  | 6 src / 7 tok | ox p.96 |
| b'oraj | n | handful, armful (our tr.) | puñado, brazada, vea: aqa'n, ejqa'n handful, armful, see: aqa'n, ejqa'n |  | 9 src / 26 tok | rukan |
| b'uküt | n | shoe (our tr.) | zapato | nub'uküt; b'uküt | 9 src / 50 tok | ox p.96 |
| b'ulb'ux | n | spring (water source) (our tr.) | manantial |  | 6 src / 6 tok | ox p.96 |
| b'uy- | pos | soft (our tr.) | suave | b'uyül; b'uyub'ïk; b'uyub'äq | 15 src / 67 tok | ox p.96 |
| b'uyül | adj | soft ; lax (grammar) (our tr.) | suave ; relajada gr. |  | 11 src / 40 tok | ox p.96 |
| -b'yaj | v.i | walk (our tr.) | caminar | yib'yaj; var. b'iyaj | 11 src / 22 tok | ox p.97 |
| -b'äch- | v.t | mix (our tr.) | mezclar | tab'acha' | 8 src / 35 tok | ox p.95 |
| -b'än- | v.t | do, make (our tr.) | hacer | tab'ana'; ninb'än; xb'an; xinb'anala'; xb'eb'ana' | 24 src / 3275 tok | ox p.95 |
| -b'är- | v.t | bandage (our tr.) | vendar | tab'ara' | 8 src / 19 tok | ox p.95 |
| -b'ätz' | v.t | gird, tie (our tr.) | ceñir, amarrar |  | 13 src / 97 tok | ox p.95 |
| b'ätz' | n | thread | hilo |  | 13 src / 81 tok | rukan |
| -b'öl | v.t | twist, roll up (thread) | torcer, enrollar, entorchar (hilo) ; bordar | tab'olo' | 7 src / 28 tok | rukan ox p.96 |
| -b'öt | v.t | wrinkle, crumple (our tr.) | arrugar | Rïn ninb'öt ri wuj. | 7 src / 28 tok | ox p.96 |
| -b'öx | v.t | gather, light, kindle (our tr.) | juntar, prender, encender | Rïn ninb'öx ri q'aq'. | 8 src / 24 tok | ox p.96 |
| ch'a'k | n | wart, boil, pimple | grano, espinilla ; grano |  | 10 src / 48 tok | rukan ox p.99 |
| ch'a'oj | n | evil, problem, bad action | maldad, problema, mala acción |  | 17 src / 414 tok | rukan |
| ch'ab' | n | bow, arrow (our tr.) | arco, flecha |  | 9 src / 35 tok | ox p.98 |
| ch'ab'äl | n | language (our tr.) | idioma | qach'ab'äl | 20 src / 1092 tok | ox p.98 |
| ch'ajch'oj | adj | clean (our tr.) | limpio |  | 18 src / 1066 tok | ox p.98 |
| -ch'ajch'ojirisaj | v.t | clean, straighten, prepare (our tr.) | limpiar, enderecer, preparar | niqach'ajch'ojirisaj qi'; xqach'ajch'ojirisaj | 7 src / 147 tok | ox p.98 |
| ch'ajch'öj | adj | clean | limpio |  | 10 src / 41 tok | rukan |
| ch'akulal | n | body (our tr.) | cuerpo |  | 6 src / 220 tok | ox p.98 |
| ch'akät | n | chair (our tr.) | silla | taq ch'akät | 14 src / 99 tok | ox p.98 |
| ch'ame'y | n | staff of authority, staff | bastòn de autoridad, vara ; bastón |  | 11 src / 68 tok | rukan ox p.98 |
| -ch'anab'a' | v.t | undress (our tr.) | desnudarse |  | 6 src / 9 tok | ox p.98 |
| ch'anin | adv | rapid, fast, var. chanin | rápido, var. chanin |  | 10 src / 213 tok | rukan |
| ch'at | n | bed (our tr.) | cama | kich'at; nuch'at | 21 src / 110 tok | ox p.99 |
| ch'atal | n | table (our tr.) | mesa | re ch'atal re'; la ch'atal la'; taq ch'atal; ach'atal | 15 src / 128 tok | ox p.99 |
| -ch'ayon | v.i | hit, strike (our tr.) | pegar, golpear | kach'ayon; kixch'ayon | 14 src / 112 tok | ox p.99 |
| ch'ekaj | n | knee (our tr.) | rodilla | nuch'ek; ruch'ek | 9 src / 23 tok | ox p.99 |
| -ch'eq- | pos | wet (our tr.) | mojado | ch'eqël; nich'eqe'; niruch'eqeb'a' | 14 src / 62 tok | ox p.99 |
| ch'i'p | n | youngest, last, smallest offspring (our tr.) | el/la menor, última/o, más pequeño cría | nuch'i'p; var. ch'ïp | 6 src / 15 tok | ox p.99 |
| ch'ima' | n | chayote (our tr.) | hüisquil |  | 6 src / 19 tok | ox p.99 |
| -ch'o | v.i | talk | hablar |  | 29 src / 2455 tok | rukan |
| -ch'o'n | v.i | speak, chat ; talk, say (our tr.) | hablar, platicar ; charlar, decir | yach'o'n; yich'o'n; nich'o'n | 10 src / 604 tok | ox p.100 |
| ch'ob' | n | order, brotherhood ; group ; ethnic group (our tr.) | orden, hermandad; agrupación; etnia |  | 10 src / 47 tok | ox p.99 |
| -ch'ob'on | v.i | think (our tr.) | pensar |  | 9 src / 45 tok | ox p.99 |
| ch'ob'onïk | v.i | ask, examine, correct, analyze (our tr.) | preguntar, examinar, corregir, analizar, 99 |  | 8 src / 23 tok | ox p.99 |
| -ch'ojij | v.t | claim, demand | reclamar |  | 17 src / 127 tok | rukan |
| -ch'ojin | v.i | demand (rights) | exigir (derechos), reclamar |  | 13 src / 72 tok | rukan |
| -ch'ok- | pos | mounted (our tr.) | montado (p) | xach'okob'a | 22 src / 301 tok | ox p.100 |
| -ch'olij | v.t | scold | regañar |  | 13 src / 139 tok | rukan |
| ch'op | n | pineapple (our tr.) | piña | ch'än ch'op | 11 src / 32 tok | ox p.100 |
| ch'u'j | adj | crazy, forgetful (our tr.) | loco. olvidadizo |  | 12 src / 72 tok | ox p.100 |
| ch'uch' | adj | frozen, cold (our tr.) | helado |  | 7 src / 22 tok | ox p.100 |
| ch'umil | n | star (our tr.) | estrella | ch'umila' | 29 src / 342 tok | ox p.100 |
| ch'uti ramaj | n | minute (our tr.) | minuto |  | 7 src / 22 tok | ox p.100 |
| ch'uti'q | adj | very small (pl.) (our tr.) | pequeñitos |  | 8 src / 38 tok | ox p.100 |
| ch'utin | adj | tiny, humble (our tr.) | pequeñito, humilde | var. ch'uti'n, ch'utïn | 16 src / 98 tok | ox p.100 |
| ch'utite'ej | n | aunt (our tr.) | tía | var. ch'itite'ej | 6 src / 10 tok | ox p.100 |
| -ch'äj | v.t | wash (our tr.) | lavar | tach'aja'; ninch'äj wey; niqach'äj qey; xich'ajon; xch'aj | 12 src / 80 tok | ox p.99 |
| ch'äm | adj | sour, var. ch'än | ácido, var. ch'än |  | 11 src / 29 tok | rukan |
| -ch'äm- | v.i | go off (food) (our tr.) | pasarse (comida) |  | 11 src / 33 tok | ox p.99 |
| -ch'är | v.t | split firewood, separate | rajar leña, separar ; rajar (leña), dividir | tach'ara' | 9 src / 19 tok | rukan ox p.99 |
| -ch'äy | v.t | hit (our tr.) | pegar | xch'ay; xinch'äy wi'; xonch'aya'; xiruch'äy; xqach'äy qi' | 7 src / 75 tok | ox p.99 |
| -ch'öb' | v.t | think, consult (our tr.) | pensar, consular | tach'ob'o' | 10 src / 28 tok | ox p.100 |
| -ch'öl | v.t | peel (our tr.) | pelar | tach'olo' | 8 src / 18 tok | ox p.100 |
| -ch'üp | v.t | pick fruit (our tr.) | cortar fruta |  | 6 src / 7 tok | ox p.100 |
| -cha' | v.t | select, choose | escoger, elegir ; decir |  | 32 src / 13299 tok | rukan |
| cha'oj | n | problem, harm, hurt | problema, daño, pleito |  | 11 src / 155 tok | rukan |
| cha'on | n | selection, vote, chosen | selección, votación, escogido |  | 14 src / 455 tok | rukan |
| chaj | n | ash | ceniza ; gris; ceniza | chajchöj | 29 src / 168 tok | rukan ox p.97 |
| chajinel | n | guardian (our tr.) | guardián |  | 22 src / 246 tok | ox p.97 |
| -chak- | pos | on all fours, crawling position (our tr.) | posición para gatear | chakäl; in chakäl; yichake'; ninchakab'a | 33 src / 3381 tok | ox p.97 |
| chakäch | n | basket (our tr.) | canasta | qachakach | 13 src / 141 tok | ox p.97 |
| -chame' | v.i | be quiet | callarse |  | 6 src / 7 tok | rukan |
| champomal | n | government | gobierno |  | 14 src / 164 tok | rukan ox p.97 |
| chanin | adv | fast (our tr.) | rápido | var. ch'anin | 18 src / 536 tok | ox p.97 |
| -chapon | v.i | scold (our tr.) | regañar | kichapon; kojchapon | 22 src / 640 tok | ox p.97 |
| chaq'laxel | n | younger sibling of the speaker's sex (our tr.) | hermano/a menor del mismo sexo del hablante | nuchaq' | 9 src / 51 tok | ox p.97 |
| chaqi'j | adj | dry | seco |  | 18 src / 179 tok | rukan |
| -chaqirisaj | v.t | dry | secar ; secar, madurarse | ninchaqirisaj wi'; xachaqarisaj | 9 src / 35 tok | rukan ox p.97 |
| chawon | adj | large, var. chowen | grande, var. chowen |  | 7 src / 16 tok | rukan |
| chay | n | flint knife (our tr.) | cuchillo de pedernal |  | 19 src / 139 tok | ox p.97 |
| che' | n | jail, tree | cárcel, árbol ; árbol, palo, madera | taq che' | 38 src / 2318 tok | rukan ox p.97 |
| chi re' | adv | here (our tr.) | aquí |  | 17 src / 147 tok | ox p.97 |
| chi rij | rel | behind him (our tr.) | atrás de él | var. chrij | 21 src / 1129 tok | ox p.97 |
| chij | n | thread, especially wool | hilo, especialmente lana ; algodón en bruto, lana, oveja, vela pequeña |  | 22 src / 925 tok | rukan ox p.97 |
| chiköp | n | animal, bird (our tr.) | animal, pájaro | chikopi' | 17 src / 109 tok | ox p.97 |
| chila | adv | over there (our tr.) | allá |  | 8 src / 90 tok | ox p.97 |
| chinamital | n | lineage, tribe, nation (our tr.) | linaje, tribu, nación |  | 6 src / 19 tok | ox p.97 |
| chojmil | n | rectitude, slenderness (our tr.) | rectitud, la esbeltez |  | 7 src / 17 tok | ox p.97 |
| chojmilal | n | truth, rectitude, slenderness (our tr.) | verdad, rectitud, la esbeltez |  | 10 src / 57 tok | ox p.97 |
| chojmin | n | shortcut, straying (our tr.) | atajo, extavio |  | 8 src / 16 tok | ox p.97 |
| -chojmirisaj | v.t | compose, put in order, arrange, tidy | componer, poner en orden |  | 14 src / 395 tok | rukan |
| cholaj | n | order, arrangement (our tr.) | orden, disposición |  | 16 src / 210 tok | ox p.98 |
| choloj | n | prayer, ritual speech | oración, invocación, habla ritual ; discurso ceremonial |  | 12 src / 34 tok | rukan ox p.98 |
| cholonel | n | master of ceremonies (our tr.) | maestro de ceremonias |  | 7 src / 19 tok | ox p.98 |
| choltzij | n | phrase (our tr.) | frase |  | 13 src / 184 tok | ox p.98 |
| choy | n | lake, lagoon (our tr.) | lago, laguna |  | 24 src / 387 tok | ox p.98 |
| -choyon | v.i | cut sticks (our tr.) | cortar palos | kachoyon; kixchoyon | 7 src / 22 tok | ox p.98 |
| chrij | rel | behind, around (our tr.) | atrás de, alrededor de | chwij; chawij; chqij; var. chi rij | 10 src / 770 tok | ox p.98 |
| chuchi | rel | edge, shore (our tr.) | orilla |  | 16 src / 153 tok | ox p.98 |
| -chuluj | v.i | wet oneself (our tr.) | orinarse |  | 8 src / 13 tok | ox p.98 |
| chum | n | mineral lime | cal |  | 7 src / 18 tok | rukan |
| -chunaj | v.t | whitewash, var. -chumaj | encalar, var. -chumaj |  | 6 src / 12 tok | rukan |
| -chup | v.i | go out (fire, light) (our tr.) | apagarse |  | 26 src / 458 tok | ox p.98 |
| chupül | adj | extinguished, off (our tr.) | apagado |  | 9 src / 105 tok | ox p.98 |
| chuqa' | adv | also (our tr.) | también |  | 25 src / 15016 tok | ox p.98 |
| chuw | adj | stinky, smelly | apestoso, nauseabundo |  | 11 src / 27 tok | rukan |
| -chuw | v.i | stink (our tr.) | heder |  | 11 src / 27 tok | ox p.98 |
| chuwi' | num | measure for counting eight thousand (our tr.) | medida para contar ocho millares | juchuwi'; var. chuy | 7 src / 176 tok | ox p.98 |
| chuy | num | eight hundred, 800 | ochocientos, 800 Ch' ; pavo, medida para maíz |  | 9 src / 19 tok | rukan ox p.98 |
| chwa'q | adv | tomorrow (our tr.) | mañana |  | 18 src / 201 tok | ox p.98 |
| chwäch | rel | in front of (our tr.) | enfrente de | chi nuwäch; chuwäch; chi qawäch | 13 src / 134 tok | ox p.98 |
| chäj | n | pine, pine needles, pine kindling | pino, ocote | qachaj | 11 src / 57 tok | rukan ox p.97 |
| -chäp | v.t | scold (our tr.) | regañar | tachapa'; xchap; yatb'enchapa'; nonchapa' | 15 src / 308 tok | ox p.97 |
| chäq' | adj | ripe (plant) (our tr.) | maduro (planta) |  | 10 src / 20 tok | ox p.97 |
| chöj | adj | correct, straight | correcto, recto, directo |  | 9 src / 31 tok | rukan |
| -chöp | v.t | grab (our tr.) | agarrar | tachapa'; rïn ninchöp; xinchöp; xachöp awi'; xinchapala' | 8 src / 53 tok | ox p.98 |
| -chöy | v.t | fell, cut with a blade, cut wood with machete or axe (our tr.) | talar, cortar con filo, cortar la madera de un árbol con machete o hacha | tachoyo' ri si'; tachoyo' ri che'; tachoyo'; man nachoy ta | 11 src / 73 tok | ox p.98 |
| -chüp | v.t | put out (fire) (our tr.) | apagar | tachupu' ri q'aq'; xinchüp ri q'aq' | 12 src / 136 tok | ox p.98 |
| -echan | n.poss | brother-in-law (of a woman) (our tr.) | cuñado (de muer) | wechan | 7 src / 20 tok | ox p.100 |
| ejqa'n | n | load | cargo ; carga | rejqa'n; var. eqa'n | 13 src / 93 tok | rukan ox p.100 |
| -ejqaj | v.t | carry on the back, go into debt | cargar en la espalda, endeudarse ; cargar en la espalda |  | 10 src / 30 tok | rukan ox p.100 |
| ejqalem | n | respect, consideration | importancia, valor, cargo, dignidad, Importance, valor, office, dignity, respeto, consider |  | 9 src / 58 tok | rukan ox p.100 |
| -el | v.i | leave, go out (our tr.) | salir | yinel el; nel; var. ntel; ndel | 34 src / 19416 tok | ox p.100 |
| -eleq'aj | v.t | rob, steal | robar | xreleq'aj kaxlan wäy | 14 src / 109 tok | rukan ox p.100 |
| -eleq'an | v.i | rob, steal | robar |  | 8 src / 50 tok | rukan |
| eleq'on | n | thief, robber, var. eleq'om | ladrón, asaltante, var. eleq'om ; ladrón |  | 8 src / 13 tok | rukan ox p.100 |
| -elesaj | v.t | take out, put out, squeeze, throw out (our tr.) | sacar, hacer salir, esprimir, echar | xqelesaj | 26 src / 1978 tok | ox p.100 |
| eqal | adv | slowly (our tr.) | despacio | var. eqal ök | 22 src / 303 tok | ox p.100 |
| etab'äl | n | measuring ruler (our tr.) | regla para medir |  | 12 src / 104 tok | ox p.100 |
| -etaj | v.t | weigh, measure | medir |  | 22 src / 184 tok | rukan |
| etal | n | signal, sign, seal, mark (our tr.) | señal, signo, sello, marca |  | 13 src / 172 tok | ox p.100 |
| -etam | v.t | know (our tr.) | saber/conocer |  | 7 src / 59 tok | ox p.100 |
| etamab'äl | n | learning, apprenticeship, knowledge | aprendizaje, conocimiento ; sust. enseñanza, sabiduría, ciencia |  | 15 src / 531 tok | rukan ox p.100 |
| etamanïk | v.i | know, understand (our tr.) | conocer, entender, saber |  | 9 src / 15 tok | ox p.100 |
| -etz'an | v.i | play (our tr.) | jugar (etz'anïk) | ke'etz'an | 27 src / 173 tok | ox p.100 |
| etz'anib'äl | n | playing field | campo deportivo ; campo de recreo |  | 10 src / 22 tok | rukan ox p.100 |
| -etzelaj | v.t | damage, hurt (our tr.) | dañar, lastimar |  | 12 src / 443 tok | ox p.100 |
| etzelal | n | harm, hurt | daño ; daño lastima |  | 14 src / 930 tok | rukan ox p.101 |
| -ewaj | v.t | hide | esconder |  | 18 src / 371 tok | rukan |
| eya' | n | pericon (medicinal plant) (our tr.) | perícon (planta medicinal) |  | 7 src / 18 tok | ox p.101 |
| -i' | pron | reflexive, reciprocal (our tr.) | reflexivo, recíproco | ri' | 12 src / 614 tok | ox p.101 |
| ichaj | n | greens | hojas comestibles ; hierbas, legumbres | qichaj; jolon ichaj; nima kulix; jolon kulix; k'ix ichaj | 24 src / 270 tok | rukan ox p.101 |
| -ichin | rel | belonging to X, of, to belong (our tr.) | posesión de X, de, pertenecer | wichin; awichin; richin; iwichin | 38 src / 48314 tok | ox p.101 |
| ichinaj | n | necklaces, jewelry (our tr.) | collares, joyería |  | 9 src / 27 tok | ox p.101 |
| -ij | rel | behind (our tr.) | détras de | chi iwïj; chi wïj | 22 src / 2152 tok | ox p.101 |
| ija'tz | n | seed, seed corn | semilla |  | 19 src / 403 tok | rukan ox p.101 |
| ijaj | n | back (our tr.) | espalda | wij; rij | 8 src / 21 tok | ox p.101 |
| ik | n | chili (our tr.) | chile | räx ik; chaqi'j ik; sik' ik; rik ch'oy, raxik ch'oy; tukr ik | 20 src / 347 tok | ox p.101 |
| -ik'in | rel | with X (our tr.) | con X | wik'in; awik'in; rik'in; iwik'in; var. uk'in | 28 src / 21712 tok | ox p.101 |
| -ik'o | v.i | surpass (our tr.) | sobrepasar | yatik'o pa ruwi' | 18 src / 628 tok | ox p.101 |
| ik'oy | n | huicoy squash (our tr.) | huicoy (güicoy) |  | 12 src / 37 tok | ox p.101 |
| ikäj | n | ax | hacha | n.b. Ö ikej rix; var. ikej, ikëj | 8 src / 39 tok | rukan ox p.101 |
| -ilij | v.t | maintain, sustain, nurture | mantener, alimentar |  | 19 src / 227 tok | rukan |
| -ilitäj | v.i | be found | Ser encontrado |  | 13 src / 540 tok | rukan |
| -ilon | v.i | find, locate | encontrar |  | 31 src / 718 tok | rukan |
| is | n | potato or sweet potato (our tr.) | papa o camotes |  | 20 src / 3386 tok | ox p.101 |
| itz | n | witchcraft, sorcery, spell (our tr.) | hechicería, brujería, ecantamiento |  | 18 src / 239 tok | ox p.101 |
| itzel | adj | ugly, bad (our tr.) | feo, malo |  | 28 src / 6973 tok | ox p.101 |
| ixim | n | maize (corn granules, seeds) | maíz | wixim; var. ixin | 28 src / 366 tok | rukan ox p.102 |
| Iximche' | name | Tecpán (our tr.) | Tecpán |  | 16 src / 261 tok | ox p.101 |
| -iy | n.poss | grandchild (of a grandmother) (our tr.) | nieto/a de abuela | wiy ala'; riy xtän | 14 src / 98 tok | ox p.102 |
| iyom | n | midwife (our tr.) | comadrona |  | 8 src / 28 tok | ox p.102 |
| ja la' | pron | that (our tr.) | eso |  | 13 src / 22 tok | ox p.102 |
| ja re | pron | this | esto |  | 17 src / 918 tok | rukan |
| ja re' | pron | this (our tr.) | esto |  | 20 src / 298 tok | ox p.102 |
| ja' | part | yes (our tr.) | sí |  | 31 src / 1386 tok | ox p.102 |
| jachonïk | v.i | share out, distribute, divide (our tr.) | repartir, distribuir, dividir |  | 6 src / 9 tok | ox p.102 |
| jaj | n | armful (our tr.) | brazada |  | 9 src / 242 tok | ox p.102 |
| -jalon | v.i | change oneself (our tr.) | cambiarse | tijalon; kejalon | 19 src / 93 tok | ox p.102 |
| jalonïk | v.i | change clothes ; fake, pretend, adulterate (our tr.) | mudarse de ropa; falsear, fingir, adulterar |  | 6 src / 9 tok | ox p.102 |
| -jam- | pos | empty (our tr.) | vacío (p) (jamonïk - desocupar) | n(i)jame'; jamäl; xinjamab'a' | 32 src / 1008 tok | ox p.102 |
| jampe | part | how many (our tr.) | cuántos | var. janpe, janipe' | 9 src / 91 tok | ox p.102 |
| jani | adv | still, yet (our tr.) | aún, todavía | man jani ta | 15 src / 1138 tok | ox p.102 |
| jantape' | adv | always (our tr.) | siempre |  | 21 src / 1344 tok | ox p.102 |
| jantäq | adv | times, sometimes (our tr.) | veces, algunas veces |  | 15 src / 44 tok | ox p.102 |
| janíla | adv | good, very, much (our tr.) | bueno, muy, mucho |  | 6 src / 1298 tok | ox p.102 |
| -jaq'- | pos | reclining face up (our tr.) | reclinado bocarriba (p) | in jaq'äl; yijaq'e'; ninjaq'ab'a' | 17 src / 63 tok | ox p.102 |
| jaqäl | adj | open (our tr.) | abierto |  | 12 src / 242 tok | ox p.102 |
| jarupe | part | how many (our tr.) | cuántos |  | 6 src / 14 tok | ox p.102 |
| jas | n | secret (our tr.) | secreto |  | 7 src / 21 tok | ox p.102 |
| jeb'ël | adv | good, very (our tr.) | bueno, muy | jeb'ël ütz; jeb'ël ruk'u'x | 24 src / 962 tok | ox p.103 |
| -jel | v.i | approach, come near, come alongside | acercarse, arrimarse |  | 39 src / 25573 tok | rukan |
| jey | n | tail (our tr.) | cola |  | 9 src / 19 tok | ox p.103 |
| jilan | adj | slippery (our tr.) | resbaladizo |  | 9 src / 11 tok | ox p.103 |
| -jilijo' | v.i | slip | resbalar |  | 10 src / 31 tok | rukan |
| -jilon | v.i | slip (our tr.) | resbalarse |  | 7 src / 37 tok | ox p.103 |
| jis- | pos | long (our tr.) | largo | jisïl; jisijïk | 12 src / 106 tok | ox p.103 |
| -jitz' | v.t | hang (someone) (our tr.) | ahorcar |  | 13 src / 31 tok | ox p.103 |
| jo'q | n | dry corn husk | doblador, tusa ; tusa, doblador |  | 9 src / 16 tok | rukan ox p.103 |
| jok'on | n | sauce (usually of tomatoes) | salsa |  | 9 src / 22 tok | rukan |
| jos | n | sickle | hoz |  | 8 src / 23 tok | rukan |
| josoj | n | weeding of the crop (our tr.) | limpia de la siembra |  | 6 src / 8 tok | ox p.103 |
| -jot- | pos | up, above (our tr.) | arriba (p) | in jotöl; xjote'; xujotob'a' | 37 src / 1639 tok | ox p.103 |
| jotay | n | sprout, descendants, lineage | retoño, herederos, descendientes, linaje ; retoño, descendencia |  | 10 src / 18 tok | rukan ox p.103 |
| -jotob'a' | v.t | raise | levantar, subir, elevar |  | 13 src / 73 tok | rukan |
| jotöl | adj | high, above, north (our tr.) | alto, arriba, norte |  | 18 src / 194 tok | ox p.103 |
| jub'a' | adv | a little (our tr.) | un poco |  | 26 src / 1089 tok | ox p.103 |
| jub'anoj | n | intransitive verb (grammar) (our tr.) | verbo intransitivo gr. |  | 9 src / 43 tok | ox p.103 |
| jub'ül | adj | fragrant, aromatic | aromático ; fragante aromático |  | 12 src / 46 tok | rukan ox p.103 |
| jujun | pron | some, each one | unos, uno cada uno ; algunos, unas |  | 33 src / 1472 tok | rukan ox p.103 |
| juk'al | num | twenty (our tr.) | veinte, otros se usan -winäq solo para contar |  | 15 src / 229 tok | ox p.103 |
| juk'an | n | unit, on land or water (our tr.) | unidad, terreste o acuática |  | 16 src / 320 tok | ox p.103 |
| juku' | n | canoe (our tr.) | canoa |  | 12 src / 40 tok | ox p.103 |
| jukumaj | adv | early (our tr.) | temprano |  | 20 src / 133 tok | ox p.103 |
| julajuj | num | eleven (our tr.) | once |  | 26 src / 180 tok | ox p.103 |
| jun | num | someone, some, a, one (our tr.) | alguien, alguno, un, una, uno | jun etab'äl xkoya' | 45 src / 63141 tok | ox p.103 |
| juna' | n | year (our tr.) | año |  | 30 src / 2032 tok | ox p.103 |
| junan | adj | similar (our tr.) | parecido | var. junam | 19 src / 3600 tok | ox p.103 |
| -junumaj | v.i | agree | ponerse de acuerdo |  | 13 src / 76 tok | rukan |
| -jup- | pos | lying face down (people) (our tr.) | acostado bocabajo (gente) | in jupül; yijupe'; ninjupub'a'; jupujïk; jupujäq | 23 src / 175 tok | ox p.103 |
| -jupe' | pos | lie face down (our tr.) | ponerse bocabajo | kajupe'; kixjupe' | 12 src / 25 tok | ox p.104 |
| jupül | pos | face down (our tr.) | boca abajo |  | 7 src / 16 tok | ox p.104 |
| jut | n | earthworm, worm, mucus (our tr.) | lombriz, gusano, moco | rujutil | 17 src / 83 tok | ox p.104 |
| juwinäq | num | twenty (our tr.) | veinte |  | 11 src / 41 tok | ox p.104 |
| -jäch | v.t | separate (our tr.) | separar |  | 15 src / 87 tok | ox p.102 |
| -jäch' | v.t | harvest (corn ears) | cosechar, tapiscar ; tapiscar | tajach'a' | 9 src / 30 tok | rukan ox p.102 |
| jäch' | n | corn harvest (our tr.) | tapisca |  | 8 src / 23 tok | ox p.102 |
| -jäl | v.t | change (our tr.) | cambiar | niqajäl qatziyaq; tajala' | 21 src / 442 tok | ox p.102 |
| jäl | n | hardened ear of corn | mazorca | ajal | 11 src / 168 tok | rukan ox p.102 |
| -jäm | v.t | put through the colander ; make room or time for | pasar en colador ; desocupar, hacer espacio o tiempo |  | 6 src / 14 tok | rukan |
| -jäq- | v.t | open (our tr.) | abrir | tajaqa' ruchi' jay; ninjäq; nujäq | 16 src / 183 tok | ox p.102 |
| jät | v.i | go! (imperative of go) (our tr.) | Imp. ¡andáte!, ¡vete! (de ir) |  | 6 src / 37 tok | ox p.103 |
| jöb' | n | rain (our tr.) | lluvia | var. jäb' | 7 src / 120 tok | ox p.103 |
| -jüx | v.t | sign, give one's signature | firmar |  | 7 src / 31 tok | rukan |
| -jüx- | v.t | scratch, draw lines (our tr.) | rayar |  | 8 src / 32 tok | ox p.104 |
| k'a | part | well, then ; until (our tr.) | pues ; hasta | ütz k'a.; Matyöx k'a ri. | 31 src / 34875 tok | ox p.106 |
| k'a ri' | part | then, afterwards (our tr.) | entonces, luego |  | 22 src / 816 tok | ox p.106 |
| k'a'äl | adj | delicate, irritable (our tr.) | delicado, enojadizo |  | 6 src / 12 tok | ox p.106 |
| K'ab'owil | n | celestial glyph band, sky (our tr.) | banda celestial glifica, cielo |  | 6 src / 10 tok | ox p.106 |
| -k'achoj | v.i | recover, get well, end a process/illness | curarse, componerse, terminar |  | 19 src / 252 tok | rukan |
| k'aj | n | flour, something finely ground (our tr.) | harina, algo molido finamente |  | 7 src / 17 tok | ox p.106 |
| k'ajola' | n | older boys, young men | jóvenes, varones |  | 12 src / 47 tok | rukan |
| k'ajolaxel | n | son (of a man) (our tr.) | hijo (de hombre) |  | 8 src / 53 tok | ox p.106 |
| k'ak'a' | adj | new (our tr.) | nuevo |  | 21 src / 1368 tok | ox p.106 |
| k'ala' | n | the weaving in groups of twenty | pita para ordenar el hilo en grupos decane and/or thread that separates veinte |  | 7 src / 12 tok | rukan ox p.106 |
| k'alk'a'x | n | rib (our tr.) | costilla |  | 6 src / 7 tok | ox p.106 |
| k'amöl b'ey | n | guide, leader, director (our tr.) | guía, líder, dirigente |  | 17 src / 118 tok | ox p.106 |
| k'an | n | maguey fiber ; measurement of land, var. k'am | pita de maguey ; cuerda de tierra, var. k'am | ruk'an | 19 src / 124 tok | rukan ox p.106 |
| -k'apij | v.t | bite (our tr.) | morderlo | niqak'apij; yojrukapij | 9 src / 31 tok | ox p.106 |
| k'aqo'j | adj | brown (our tr.) | café, pardo |  | 10 src / 55 tok | ox p.106 |
| k'as | n | debt, occupation (our tr.) | deuda, ocupación |  | 12 src / 76 tok | ox p.106 |
| -k'asb'a' | v.t | give life to | dar vida a |  | 8 src / 12 tok | rukan |
| k'aslemal | n | culture, way of life (our tr.) | cultura, sistema de vida |  | 20 src / 261 tok | ox p.106 |
| k'aslen | n | life, lived (our tr.) | vida, vivido | var. k'aslem | 9 src / 507 tok | ox p.106 |
| -k'astan | v.i | have fun (our tr.) | divertirse (k'astanïk) |  | 9 src / 27 tok | ox p.106 |
| -k'astäj | v.i | wake up (our tr.) | despertarse | kak'astäj; kixk'astäj | 10 src / 67 tok | ox p.106 |
| k'ate' | adv | a little while ago, at last, in short, suddenly (our tr.) | hace poco, al fin, en suma, de repente |  | 9 src / 122 tok | ox p.107 |
| k'atinäq | adj | burnt | quemado |  | 9 src / 16 tok | rukan |
| -k'atzin | v.i | be useful, need, serve (our tr.) | ser útil, necesitar, servir |  | 24 src / 1333 tok | ox p.107 |
| k'atän | n | fever, heat ; xpe k'atän chwij I have a fever | fiebre, calentura ; calor, caliente | xpe k'atän chwij | 15 src / 99 tok | rukan ox p.107 |
| -k'aw- | pos | lying face up (our tr.) | acostado bocarriba (p) | k'awäl; in k'awäl; yik'awe'; nink'awab'a' | 26 src / 283 tok | ox p.107 |
| -k'ay | v.t | sell (our tr.) | vender |  | 17 src / 162 tok | ox p.107 |
| k'ayb'äl | n | market | mercado ; tienda, mercado | k'ayb'äl wuj; var. k'ayib'äl | 16 src / 203 tok | rukan ox p.107 |
| -k'ayew | v.i | be difficult, hard | ser difícil |  | 23 src / 634 tok | rukan |
| k'ayew | adj | difficult | difícil |  | 22 src / 625 tok | rukan ox p.107 |
| k'ayewal | n | problem, difficulty, worry (our tr.) | problema, dificultad, preocupación problem, difficulty, worry | ri k'ayewal ri' | 20 src / 1009 tok | rukan ox p.107 |
| k'ayij | n | sale, store (our tr.) | venta, tienda |  | 17 src / 121 tok | ox p.107 |
| k'ayinel | n | seller (our tr.) | vendedor | k'ayinela' | 14 src / 69 tok | ox p.107 |
| k'ek' | adj | stingy, miserly, mean (our tr.) | tacaño, ávaro, ruín |  | 6 src / 10 tok | ox p.107 |
| k'el | n | green parakeet that doesn't speak | perico verde que no habla ; perico | estawi' | 14 src / 21 tok | rukan ox p.107 |
| -k'em- | v.t | bring (our tr.) | traer | var. k'äm-, -k'än- | 8 src / 19 tok | ox p.107 |
| -k'et- | v.t | sting (insect) (our tr.) | picar (un insecto) | xuk'ët raqän | 20 src / 275 tok | ox p.107 |
| k'ex | n | change, barter, purchase (our tr.) | cambio, trueque, compra |  | 7 src / 14 tok | ox p.107 |
| K'iche' | name | K'iche' (our tr.) | Quiche' | var. K'ichee' | 15 src / 153 tok | ox p.107 |
| -k'ilin | v.i | toast (our tr.) | tostar |  | 8 src / 27 tok | ox p.107 |
| k'im | n | straw | paja | var. k'in | 14 src / 77 tok | rukan ox p.107 |
| -k'is | v.i | run out, end (our tr.) | acabarse, terminarse | Xk'is ri samaj. | 23 src / 1706 tok | ox p.107 |
| k'isis | n | cypress | ciprés |  | 6 src / 27 tok | rukan |
| k'ix | n | thorn ; chayote, perulero (our tr.) | espina ; güisquil (huisquil), perulero | rutza'n k'ix; rutza'n ch'ima'; var. k'ïx | 19 src / 158 tok | ox p.107 |
| -k'ix- | v.i | prick, be thorny (our tr.) | espinar | yalan nik'ixan | 33 src / 863 tok | ox p.107 |
| -k'iyïr | v.i | grow, be plentiful | crecer, abundar |  | 6 src / 26 tok | rukan |
| k'o | v.i | there is (our tr.) | hay |  | 31 src / 16902 tok | ox p.108 |
| k'o re | adv | at times, sometimes | a veces |  | 11 src / 70 tok | rukan |
| k'oj | n | mask (our tr.) | máscara |  | 19 src / 379 tok | ox p.108 |
| k'ojlib'äl | n | place | lugar ; utensilios |  | 14 src / 354 tok | rukan ox p.108 |
| -k'owisaj | v.t | cross, pass, translate (our tr.) | atravesar, pasar, traducir | xink'owisaj; xink'owisaj nuq'ij. | 10 src / 207 tok | ox p.108 |
| -k'ox | v.i | drink liquor (our tr.) | tomar trago (vugar) | k'oxinïk; yik'oxin | 12 src / 25 tok | ox p.108 |
| k'oy | n | monkey (our tr.) | mico | taq k'oy'i' | 13 src / 42 tok | ox p.108 |
| k'u'x | n | heart of the weaving, heart | corazón de la urdimbre, corazón ; corazón |  | 21 src / 726 tok | rukan ox p.108 |
| k'ujay | n | corncrib, maize granary (our tr.) | troje, granero de maíz, var. k'ujay corncrib, var. k'ujay | var. k'ojoy (Chiq'a'l) | 11 src / 38 tok | rukan ox p.108 |
| -k'ul | v.i | marry (our tr.) | casarse | xk'ulue junab'ïr. | 25 src / 1122 tok | ox p.108 |
| k'ulan | adj | married (our tr.) | casado/a |  | 15 src / 112 tok | ox p.108 |
| -k'ule' | v.i | marry | casarse |  | 16 src / 260 tok | rukan |
| -k'ulub'a' | v.t | answer, respond, marry (our tr.) | contestar, responder, casar | nink'ulub'a'; xe'ink'ulub'a. | 6 src / 13 tok | ox p.108 |
| k'um | n | squash (ayote) (our tr.) | ayote |  | 10 src / 35 tok | ox p.108 |
| -k'utuj | v.t | ask (our tr.) | preguntar |  | 25 src / 1924 tok | ox p.108 |
| k'utuj | n | marriage proposal negotiation | pedida (de casamiento) |  | 13 src / 70 tok | rukan |
| k'utunïk | n | question (our tr.) | pregunta |  | 14 src / 325 tok | ox p.108 |
| -k'uxlaj | v.t | concern oneself with, remember a person, worry | preocuparse por, recordar con cariño y tenerlo presente |  | 8 src / 33 tok | rukan |
| -k'waj | v.t | carry (our tr.) | llevar | tak'waj ka'i'... | 18 src / 341 tok | ox p.108 |
| -k'wäx | v.i | be taken | ser llevado |  | 7 src / 56 tok | rukan |
| -k'äm | v.t | bring, carry | traer ; llevar, traer | tak'ama'; var. k'em, -k'än | 15 src / 288 tok | rukan ox p.107 |
| -k'äq | v.t | choose, point at (our tr.) | elegir, apuntar | nikik'äq ruwäch | 18 src / 109 tok | ox p.107 |
| k'äq | n | flea (our tr.) | pulga | var. k'eq | 10 src / 20 tok | ox p.107 |
| k'äs | pos | alive (our tr.) | posicional vivo |  | 17 src / 117 tok | ox p.107 |
| k'äy | adj | sour, bitter (our tr.) | ácido, amargo | k'ayiläj | 9 src / 35 tok | ox p.107 |
| -k'ïs | v.t | finish (our tr.) | terminar | Xink'ïs ri nusamaj. | 14 src / 125 tok | ox p.107 |
| -k'ïx | v.i | be ashamed (our tr.) | avergonzarse | kak'ïx; kixk'ïx | 7 src / 151 tok | ox p.107 |
| -k'ïy | v.i | grow, engrandize, make big, enlarge | crecer, engrandecer, hacerse grande |  | 22 src / 1317 tok | rukan |
| k'ïy | adj | much, many (our tr.) | mucho(s) | k'ïy xna'j | 22 src / 1270 tok | ox p.107 |
| -k'öl | v.t | keep, store (our tr.) | guardar |  | 14 src / 53 tok | ox p.108 |
| -k'öt | v.t | dig, scratch, carve (our tr.) | cavar, escarbar, tallar | nink'öt; tak'oto' | 10 src / 43 tok | ox p.108 |
| k'üch | n | vulture (our tr.) | zopilote |  | 8 src / 22 tok | ox p.108 |
| -k'ül | v.t | find, receive, collect | encontrar, recibir, recoger ; encontrar, recibir |  | 19 src / 423 tok | rukan ox p.108 |
| -k'üq | v.t | start up, tear, pull | arrancar | tak'uqu' | 7 src / 10 tok | rukan ox p.108 |
| -k'üt | v.t | teach ; point out, show (our tr.) | enseñar ; señalar, enseñar | nuk'ut; tak'utu'; ruk'utik | 22 src / 411 tok | ox p.108 |
| ka' | n | grinding stone and metate (our tr.) | mano y metate |  | 18 src / 93 tok | ox p.104 |
| ka'i' | num | two (our tr.) | dos | ka'i' manq'u'q' rajïl; ka'i' xajab'; kaka' | 29 src / 2070 tok | ox p.104 |
| kab' | n | sugar, sweet (our tr.) | azúcar, dulce |  | 21 src / 108 tok | ox p.104 |
| kab'anoj | n | transitive verb (grammar) (our tr.) | verbo transitivio gr. |  | 9 src / 58 tok | ox p.104 |
| kab'ijir | adv | the day before yesterday (our tr.) | antiyer, anteayer |  | 9 src / 35 tok | ox p.104 |
| kab'lajuj | num | twelve (our tr.) | doce |  | 24 src / 184 tok | ox p.104 |
| kab'raqän | n | earthquake (our tr.) | terremoto |  | 9 src / 33 tok | ox p.104 |
| kach' | n | chewing gum (our tr.) | chicle | kach' tulül; kach' | 6 src / 21 tok | ox p.104 |
| -kaj | n | span, measure of the outstretched hand (our tr.) | cuarta, medida de la mano extendida |  | 37 src / 2538 tok | ox p.104 |
| kaj | n | sky (our tr.) | cielo |  | 27 src / 497 tok | ox p.104 |
| kaji' | num | four (our tr.) | cuatro | kaji' jay; kajkäj | 22 src / 622 tok | ox p.104 |
| kajlajuj | num | fourteen (our tr.) | catorce |  | 19 src / 95 tok | ox p.104 |
| kajtz'uk | adj | square (our tr.) | cuadrado |  | 11 src / 35 tok | ox p.104 |
| kajulew | n | universe (our tr.) | universo |  | 15 src / 54 tok | ox p.104 |
| kamel | adj | mortal, humble (our tr.) | mortal, humilde |  | 11 src / 61 tok | ox p.104 |
| Kamey | name | death, day name (our tr.) | muerte, nombre caléndrico del cholq'ij |  | 11 src / 52 tok | ox p.104 |
| kaminäq | adj | deceased | muerto | rukaminaq; rukaminaqil; var. kamnäq | 17 src / 51 tok | rukan ox p.104 |
| -kamisaj | v.t | kill (our tr.) | matarlo | xkamisäx | 18 src / 917 tok | ox p.104 |
| -kamisan | v.i | kill (our tr.) | matar | kikamisan; kojkamisan | 11 src / 170 tok | ox p.104 |
| kamixa' | n | shirt (our tr.) | camisa | ikamixa'; var. kamxa, kamixa | 9 src / 44 tok | ox p.104 |
| -kamuluj | v.t | repeat (our tr.) | repetir | takamuluj | 14 src / 66 tok | ox p.104 |
| -kanoj | v.t | look for (our tr.) | buscar |  | 25 src / 793 tok | ox p.104 |
| kanonel | n | searcher, hunter (our tr.) | buscador, cazador | var. kanunel | 8 src / 29 tok | ox p.104 |
| -kanäj | v.i | stay, remain (our tr.) | quedar | yekanäj kan | 14 src / 68 tok | ox p.104 |
| kape | n | coffee (our tr.) | café |  | 9 src / 73 tok | ox p.104 |
| kaplin | n | cherry (our tr.) | cereza | var. koxkob'al | 7 src / 11 tok | ox p.104 |
| kaq'ïq | n | wind (our tr.) | viento |  | 6 src / 8 tok | ox p.104 |
| kaqix | n | macaw (our tr.) | guacamaya |  | 9 src / 23 tok | ox p.104 |
| kaqköj | adj | reddish (our tr.) | rojizo |  | 9 src / 17 tok | ox p.104 |
| karne'l | n | ram, sheep (our tr.) | carnero (sheep) | kite' karne'l | 12 src / 506 tok | ox p.104 |
| katel | phr | go out! (our tr.) | ¡salga! |  | 9 src / 45 tok | ox p.104 |
| kaxlan wäy | n | bread (our tr.) | pan |  | 7 src / 42 tok | ox p.105 |
| ke la' | adv | over there | allá |  | 20 src / 144 tok | rukan |
| ke re' | adv | like this (our tr.) | así |  | 19 src / 380 tok | ox p.105 |
| -ke'ej | v.t | grind (our tr.) | moler |  | 7 src / 16 tok | ox p.105 |
| ke'en | n | corn dough | masa |  | 10 src / 52 tok | rukan ox p.105 |
| kem | n | weaving, backstrap loom | tejido, telar de palitos | var. ken | 17 src / 220 tok | rukan ox p.105 |
| -kemon | v.i | weave | tejer |  | 14 src / 114 tok | rukan |
| ki' | adj | sweet, delicious | dulce, delicioso ; dulce |  | 32 src / 3180 tok | rukan ox p.105 |
| -kikot | v.i | be glad, be happy (our tr.) | alegrarse, ser feliz | kakikot; kixkikot | 24 src / 771 tok | ox p.105 |
| kinäq' | n | bean (our tr.) | frijol | ikinaq; q'eqakinäq'; saqakinäq'; kaxlan kinäq' | 17 src / 101 tok | ox p.105 |
| -kiraj | v.t | scatter, strew, var. -kraj | dispersar, esparcir, var. -kraj |  | 8 src / 23 tok | rukan |
| kiran | adj | scattered (our tr.) | regado |  | 6 src / 37 tok | ox p.105 |
| ko'öl | adj | small (our tr.) | pequeño |  | 15 src / 284 tok | ox p.105 |
| -koj | v.i | be in a place (our tr.) | estar en un lugar | xakoje' | 26 src / 831 tok | ox p.105 |
| kok | n | turtle (our tr.) | tortuga |  | 8 src / 19 tok | ox p.105 |
| koköj | adj | small (pl.) (our tr.) | pequeños |  | 9 src / 44 tok | ox p.105 |
| -kolaj | v.t | have a snack, finish eating (our tr.) | refaccionar, terminar de comer | xikolaj yan, matyox. | 15 src / 61 tok | ox p.105 |
| kolo' | n | lasso (our tr.) | laso |  | 10 src / 87 tok | ox p.105 |
| kolob'äl | n | snack | refacción ; merienda, refacción |  | 8 src / 11 tok | rukan ox p.105 |
| koqolajay | n | thunder (our tr.) | trueno |  | 9 src / 77 tok | ox p.105 |
| -kos | v.i | tire (our tr.) | cansar | xkos | 15 src / 86 tok | ox p.105 |
| kosnäq | adj | tired (our tr.) | cansado | var. kosinäq | 7 src / 18 tok | ox p.105 |
| kot | n | eagle (our tr.) | águila | koti' | 19 src / 212 tok | ox p.106 |
| koton | n | jacket | chumpa ; chaqueta, suéter | akoton; nukoton | 8 src / 27 tok | rukan ox p.105 |
| -kotz'- | pos | lying down (our tr.) | acostado (p) | kotz'öl; in kotz'öl; yikotz'e'; ninkotz'ob'a' | 31 src / 792 tok | ox p.105 |
| -kotz'e' | pos | lie down (our tr.) | acostarse |  | 11 src / 40 tok | ox p.105 |
| kotz'i'j | n | ceremony, flower | ceremonia, flor ; flor, candela | ikotz'i'j; pa kotz'i'j | 25 src / 258 tok | rukan ox p.105 |
| kow | adj | hard (our tr.) | duro | kowiläj | 18 src / 282 tok | ox p.105 |
| -kowil | n.poss | Strength, hardness, valor | fuerza, dureza, fortaleza, valor |  | 15 src / 76 tok | rukan |
| -kowirisaj | v.t | harden (our tr.) | hacer duro | xinkowirisaj | 9 src / 92 tok | ox p.105 |
| koyopa' | n | lightning (our tr.) | relámpago | koyopa'i' | 9 src / 75 tok | ox p.106 |
| kuk | n | squirrel (our tr.) | ardilla | saqab'ojo'y | 13 src / 42 tok | ox p.106 |
| kuku' | n | water jug (with 2 handles), var. q'e'l | tinaja, var. q'e'l |  | 10 src / 31 tok | rukan |
| kumätz | n | snake, serpent, arthritis (our tr.) | serpiente, culebra, artritis | kumatzi' | 14 src / 102 tok | ox p.106 |
| kup | n | stem of corncobs and fruits (our tr.) | tallo de mazorca, y frutas |  | 6 src / 9 tok | ox p.106 |
| -kusaj | v.t | use, wear | usar, ponerse |  | 15 src / 986 tok | rukan |
| kux | n | weasel (our tr.) | comadreja (weasle) |  | 8 src / 43 tok | ox p.106 |
| -käm | v.i | to die | morir | kakän; kixkän; var. kän morir | 16 src / 148 tok | rukan ox p.105 |
| käq | adj | red (our tr.) | rojo | var. këq | 18 src / 141 tok | ox p.105 |
| kär | n | fish (our tr.) | pescado, pez |  | 13 src / 84 tok | ox p.105 |
| -këm | v.t | weave | tejer | xukëm she wove it; passive xkem; antipassive xkemon | 7 src / 55 tok | rukan ox p.105 |
| -köch' | v.t | endure, bear | aguantar, soportar ; aguantar |  | 7 src / 51 tok | rukan ox p.106 |
| -köl | v.t | store | guardar |  | 14 src / 100 tok | rukan |
| -küy | v.t | forgive | perdonar | yatinküy; rïn yanküy | 11 src / 39 tok | rukan ox p.106 |
| la | part | interrogative ; adverb of doubt, I don't know, maybe (our tr.) | interrogativo/ adv. de duda no sé...., puede ser |  | 37 src / 11315 tok | ox p.108 |
| la' | part | that, of that (our tr.) | ese, esa, de ese |  | 34 src / 948 tok | ox p.108 |
| lab'al | n | war, armed conflict | guerra, conflicto armado ; guerra |  | 13 src / 154 tok | rukan ox p.108 |
| lajuj | num | ten (our tr.) | diez |  | 33 src / 1068 tok | ox p.108 |
| lantar | n | woman's apron (our tr.) | delantal de mujer |  | 7 src / 12 tok | ox p.108 |
| leme't | n | bottle (our tr.) | botella |  | 11 src / 15 tok | ox p.108 |
| lemow | n | glass, mirror (our tr.) | vidrio, espejo |  | 8 src / 26 tok | ox p.108 |
| lemowäch | n | eyeglasses (our tr.) | lentes |  | 8 src / 14 tok | ox p.108 |
| liq' | adj | slimy, sticky | ligoso, pegajoso |  | 10 src / 39 tok | rukan |
| lo'x | adj | tender, soft, pliable | tierno, suave |  | 11 src / 24 tok | rukan |
| lol | n | grasshopper, hope | saltamontes, esperanza |  | 7 src / 16 tok | rukan |
| loman | adj | medium, average, so-so | medio ; mediano |  | 15 src / 117 tok | rukan ox p.108 |
| loq' | adj | kind, pleasant (our tr.) | amable, agradable |  | 9 src / 54 tok | ox p.108 |
| loq'ob'äl | n | thanks ; blessing (our tr.) | gracias, bendición |  | 7 src / 11 tok | rukan |
| läq | n | dish, deep bowl, pot (our tr.) | traste, plato hondo, olla | nulaq; semet läq | 16 src / 97 tok | ox p.108 |
| -löq' | v.t | purchase | comprar |  | 16 src / 282 tok | rukan |
| -löq'- | v.t | buy (our tr.) | comprar |  | 16 src / 284 tok | ox p.109 |
| Ma | part | Don (title for men in some towns) (our tr.) | Don |  | 32 src / 5427 tok | ox p.109 |
| majani | adv | not yet (our tr.) | de tiempo, aún no, todavía no. |  | 13 src / 67 tok | ox p.109 |
| majun | pron | nothing, nobody, never (our tr.) | nada, nadie, nunca | majun rutzyäq; var. manjun | 19 src / 2686 tok | ox p.109 |
| mak | n | guilt, offense, malice, sin | culpa, delito, maldad, ofensa, pecado |  | 16 src / 836 tok | rukan |
| -makun | v.i | sin (our tr.) | pecar |  | 6 src / 399 tok | ox p.109 |
| -malij | v.i | be sad, abandoned, deserted (our tr.) | estar triste, abandonado, desierto |  | 15 src / 414 tok | ox p.109 |
| malka'n | n | widow, widower (our tr.) | viuda, viudo | rumalka'n | 6 src / 57 tok | ox p.109 |
| man kan ta | phr | not just, not only, not just yet | no solo, no todavía |  | 17 src / 191 tok | rukan |
| man nunimaj ta | phr | is stubborn, does not obey (our tr.) | es necio, no obedece |  | 9 src / 29 tok | ox p.109 |
| man wetaman ta | phr | I don't know (our tr.) | no sé |  | 12 src / 84 tok | ox p.109 |
| manäq | part | no (our tr.) | no |  | 19 src / 764 tok | ox p.109 |
| masat | n | deer (our tr.) | venado | taq masat | 14 src / 102 tok | ox p.109 |
| matyöx | part | thank you (our tr.) | gracias | matyöx che nuway; matyoxb'äl; matyöx k'a ri'; ninmatyoxij | 6 src / 192 tok | ox p.109 |
| may | n | tobacco, cigar, cigarette | tabaco, puro, cigarro ; tobaco |  | 18 src / 413 tok | rukan ox p.109 |
| Maya' b'anob'äl | n | Maya Culture | Cultura Maya |  | 6 src / 26 tok | rukan |
| Maya' na'oj | n | Maya thought; Maya cosmovision | Penasamiento Maya, cosmovisión Maya |  | 7 src / 34 tok | rukan |
| meb'a' | n | orphan, poor (our tr.) | huérfano, pobre |  | 12 src / 38 tok | ox p.109 |
| men | adj | mute (our tr.) | mudo | var. mem | 10 src / 180 tok | ox p.109 |
| meq'en | adj | hot (our tr.) | caliente |  | 13 src / 52 tok | ox p.109 |
| -mestaj | v.t | forget (our tr.) | olvidar | ximestaj | 23 src / 474 tok | ox p.110 |
| metz' | n | girlfriend (metz' xtän), boyfriend (metz' ala') ; eyebrow, eyelash (our tr.) | novia/o ; ceja, pestaña |  | 8 src / 26 tok | rukan ox p.110 |
| meway | n | fast, fasting (our tr.) | ayuno |  | 7 src / 20 tok | ox p.110 |
| mo's | n | foreigner, Ladino, white person | extranjero, ladino, blanco |  | 8 src / 43 tok | rukan |
| molaj | n | measure, pile of leaves or papers, kinds (our tr.) | medida, montón de hojas o papeles, especies | Jumolaj; Kamolaj | 22 src / 709 tok | ox p.110 |
| molonel | n | gatherer, collector (our tr.) | el que reúne, coleccionista |  | 7 src / 29 tok | ox p.110 |
| moq' | n | fistful, especially of grain and beans | medida, un puño, especialmente de granos y frijol | jumoq' | 9 src / 25 tok | rukan ox p.110 |
| moy | adj | blind (our tr.) | ciego |  | 14 src / 310 tok | ox p.110 |
| moyew | n | fog, mist (our tr.) | neblina |  | 10 src / 22 tok | ox p.110 |
| much' | n | Longbeak Rattlebox, scientific: Crotalaria longirostrata | chipilín ; chipilín, chipilines | rumuch' | 9 src / 29 tok | rukan ox p.110 |
| mujal | n | shade, shadow (our tr.) | sombra | numuj | 8 src / 12 tok | ox p.110 |
| mul | n | time (occurrence) (our tr.) | vez | jampe mul? | 23 src / 696 tok | ox p.110 |
| munil | n | snack, sweet snack, candy (our tr.) | refacción, merienda dulce, golosinas sweet snack, candy |  | 10 src / 32 tok | rukan |
| muquj | n | hill up a cornstalk with earth against the wind | calzado de milpa |  | 6 src / 11 tok | rukan |
| muqül | adj | cloudy, covered ; underlying, deep (our tr.) | nublado, tapado ; subyacente, "profundo | muqül choltzij | 12 src / 37 tok | ox p.110 |
| -mux | v.i | swim (our tr.) | nadar | yemuxan | 10 src / 91 tok | ox p.110 |
| -muxan | v.i | swim (our tr.) | nadar | kamuxan; Rïx kixmuxan; yatikïr yamuxan | 16 src / 104 tok | ox p.110 |
| -mäl | v.t | rub lightly, massage (our tr.) | frotar ligeramente, sobar |  | 18 src / 137 tok | ox p.109 |
| -mës- | v.t | sweep (our tr.) | barrer | yimeson; tamesa' | 6 src / 19 tok | ox p.110 |
| -möl | v.t | gather, join ; collect (our tr.) | reunir, juntar (molonïk) ; recoger | xojmolon; tamolo' | 21 src / 470 tok | ox p.110 |
| -müq | v.t | bury | enterrar ; enterrar tapar | nikimüq | 13 src / 34 tok | rukan ox p.110 |
| -na' | v.t | feel, remember, taste, test | sentir, recordar, saborear, probar ; sentir, saber (sabores) (na'onïk) | Utz nana'?; Tew nina'.; Xinna' nutel'. | 15 src / 52 tok | rukan ox p.111 |
| na'oj | n | character, sense, reason, idea, experience, art (our tr.) | carácter, sentido, razón, idea, experiencias, arte |  | 30 src / 1894 tok | ox p.111 |
| na'ojib'äl | n | ideology, belief | ideología, creencia |  | 6 src / 13 tok | rukan |
| na'onel | adj | prudent, wise, knowledgeable (our tr.) | prudente, sabio, conocedor |  | 6 src / 58 tok | ox p.111 |
| nak- | adj | foolish, useless, worthless (our tr.) | tonto, inútil, inservible | nakäl; nakanïk; nakanäq | 36 src / 4472 tok | ox p.110 |
| Nan | part | Ma'am (vocative) (our tr.) | Señora (vocativa) | var. nana | 21 src / 205 tok | ox p.110 |
| naqaj | adv | near, close | cerca |  | 23 src / 223 tok | rukan ox p.111 |
| -naqon | v.i | bother, annoy, mortify, challenge (our tr.) | molestar, importunar, mortificar, desafiar | Niqa chwäch ninaqon | 9 src / 20 tok | ox p.111 |
| natab'äl | n | knowledge, sense, memorial, memory (our tr.) | conocimiento, sentido, memorial, recuerdo |  | 6 src / 144 tok | ox p.111 |
| -nataj | v.t | remember, recall | recordarse ; recordar |  | 23 src / 1916 tok | rukan ox p.111 |
| ne'y | n | baby | bebé ; nene, bebé |  | 16 src / 122 tok | rukan ox p.111 |
| nik'aj | n | half, middle (our tr.) | media, medio, mitad | nik'aj achin; nik'aj ixöq | 27 src / 529 tok | ox p.111 |
| nik'aj q'ij | n | midday, noon (our tr.) | mediodía |  | 12 src / 21 tok | ox p.111 |
| -nik'ajal | rel | between, in the middle of, center (our tr.) | entre de, en medio de, centro | nik'aj q'ij | 17 src / 164 tok | ox p.111 |
| nik'ajal | n | reproductive organs (our tr.) | órganos de reproducción |  | 9 src / 21 tok | ox p.111 |
| nima'q | adj | big (plural) (our tr.) | grandes |  | 21 src / 834 tok | ox p.111 |
| nimab'ey | n | avenue, causeway (our tr.) | avenida, calzada |  | 7 src / 20 tok | ox p.111 |
| nimab'äl | n | solemnity, honor (our tr.) | solemnidad, honra |  | 12 src / 80 tok | ox p.111 |
| nimab'äl k'u'x | n | religion (our tr.) | religión |  | 11 src / 72 tok | ox p.111 |
| Nimach'umil | name | Venus (our tr.) | Venus |  | 7 src / 11 tok | ox p.111 |
| -nimaj | v.t | create, obey | creer, obedecer ; dejarse convencer, obedecer | man ninnimaj ta | 24 src / 3770 tok | rukan ox p.111 |
| nimajay | n | living room (our tr.) | sala |  | 18 src / 88 tok | ox p.111 |
| nimalaxel | n.poss | older sibling of the same sex as the speaker (our tr.) | hermano/a mayor del mismo sexo del hablante | nunimal | 19 src / 136 tok | ox p.111 |
| nimalaxela' | n | principal stewards, lit. older same sex siblings | mayordomos principales, lit. hermanos mayores |  | 6 src / 13 tok | rukan |
| nimaläj | adj | very big (our tr.) | grandísima/o |  | 22 src / 614 tok | ox p.111 |
| nimanel | adj | obedient (our tr.) | obediente |  | 6 src / 23 tok | ox p.111 |
| nimaq'a' | n | tomorrow (our tr.) | mañana |  | 20 src / 305 tok | ox p.111 |
| nimaq'ij | n | celebration (our tr.) | celebración |  | 22 src / 426 tok | ox p.111 |
| nimasaq'ul | n | plantain | plátano |  | 8 src / 21 tok | rukan ox p.111 |
| -noj | v.i | fill up (our tr.) | llenarse | xnoj; xinnoj(i)saj; nojnäq; var. nojinäq | 35 src / 1742 tok | ox p.111 |
| nojib'äl | n | knowledge (our tr.) | conocimiento |  | 9 src / 26 tok | ox p.111 |
| -nojij | v.t | think (our tr.) | pensar | xinnojij | 19 src / 1337 tok | ox p.111 |
| nojinäq | adj | full, full of food (our tr.) | lleno, repleta de comida |  | 6 src / 38 tok | ox p.111 |
| nojnäq | adj | full (our tr.) | lleno |  | 9 src / 22 tok | ox p.111 |
| nuk'ajol | n.poss | my son (of a man) (our tr.) | mi hijo (de hombre) |  | 13 src / 265 tok | ox p.111 |
| nuk'un | adj | placed in order arranged properly | puesto en orden, ordenado |  | 12 src / 135 tok | rukan |
| nuk'unïk | v | ordered, rehearse, arrange, ask for advice (our tr.) | ordenado, ensayar, arreglar, pedir consejo |  | 6 src / 12 tok | ox p.111 |
| nunimal | n.poss | my older sister (our tr.) | mi hermana grande | NB a woman says this of her older sister, a man of his older brother | 23 src / 104 tok | ox p.112 |
| näj | adj | far | lejos ; lejos, lejano, profundo, largo |  | 23 src / 204 tok | rukan ox p.111 |
| -näq | v.t | bother, tease (our tr.) | molestar, bromear | yarunäq | 27 src / 3980 tok | ox p.111 |
| -nïm | v.t | herd, drive (animals) (our tr.) | arrear | tanima' | 15 src / 791 tok | ox p.111 |
| nïm | adj | big, grown, thick, immense (our tr.) | grande, crecido, grueso, inmenso | nima'q; nimawinäq | 15 src / 767 tok | ox p.111 |
| -nük' | v.t | order, put in order | ordenar, poner en orden ; aperchar | tanuk'u' | 14 src / 212 tok | rukan ox p.112 |
| -nüm | v.i | be hungry (our tr.) | tener hambre | ninüm chïk | 10 src / 40 tok | ox p.112 |
| -o- | v.i | come (auxiliary verb) (our tr.) | venir verbo auxiliar |  | 34 src / 8775 tok | ox p.112 |
| och' | n | young ear of corn | jilote, elote tierno, elote naciente ; elote tierno, elote naciente | var. o'ch' | 9 src / 31 tok | rukan ox p.112 |
| oj | n | avocado (our tr.) | aguacate |  | 27 src / 1481 tok | ox p.112 |
| ojer | adv | before, in former times (our tr.) | antes, en otros tiempos | ojer kan | 36 src / 2147 tok | ox p.112 |
| ojöb' | n | cough ; have a cough or a cold (xpe ojöb' chwe) | tos, esputo, expectoración ; tos, esputo, expectoración | xpe ojöb' chwe | 8 src / 41 tok | rukan ox p.112 |
| -ok | v.i | enter (our tr.) | entrar | nok; katok; yinok pe; kixok; ok aq'a'; ok chi ajawarem | 28 src / 1117 tok | ox p.112 |
| okel | adj | necessary | necesario ; justo, conveniente, oportuno | var. okik | 15 src / 461 tok | rukan ox p.112 |
| oköx | n | mushroom (our tr.) | hongo |  | 10 src / 23 tok | ox p.112 |
| -oma | rel | cause (our tr.) | causa | roma; woma; awoma; iwoma; var. uma (propuesta para estandar) | 36 src / 38554 tok | ox p.112 |
| -onojel | pron | all (our tr.) | todo | konojel; ronojel | 37 src / 22282 tok | ox p.112 |
| -oq' | v.i | cry (our tr.) | llorar (oq'enïk) | noq'; yinoq'; katoq'; kixoq'; xinoq'; var. ntoq' llora | 11 src / 37 tok | ox p.112 |
| otzoy | n | small sea shrimp (our tr.) | camaroncitos de mar |  | 6 src / 9 tok | ox p.112 |
| oxi' | num | three (our tr.) | tres | oxi' che' | 30 src / 2142 tok | ox p.112 |
| oxijir | adv | three days ago (our tr.) | hace tres días |  | 9 src / 19 tok | ox p.112 |
| oxlajuj | num | thirteen (our tr.) | trece |  | 23 src / 273 tok | ox p.112 |
| -oyob'ej | v.t | wait | esperar ; esperar (oyob'enïk) | yiroyob'ej; katinwoyob'ej; ke'iwoyob'ej; kixqoyob'ej | 17 src / 153 tok | rukan ox p.112 |
| -oyob'en | v.i | expecting (a baby) | está esperando (bebé) |  | 13 src / 245 tok | rukan |
| -oyoj | v.t | call, invite (our tr.) | llamar, invitar | nikoyoj; ninwoyoj; yatinwoyoj; yekoyoj; yeroyoj; yi'iwoyoj | 23 src / 1001 tok | ox p.112 |
| -oyowal | n.poss | anger, wrath | enojo, furia ; enojo, problema, en unos pueblos se usa | royowal; woyowal | 22 src / 1789 tok | rukan ox p.112 |
| oyowal | n | problem ; | problema |  | 17 src / 908 tok | rukan |
| pa | part | in, of, toward, to, around, near (our tr.) | en, de, hacia, a, alrededor, cerca |  | 45 src / 70621 tok | ox p.113 |
| pa che' | n | jail (our tr.) | cárcel | yab'e pa che' | 14 src / 62 tok | ox p.113 |
| pa jotöl | adv | to the north, upward (our tr.) | al norte, hacia arriba |  | 14 src / 77 tok | ox p.113 |
| pa q'ij | adv | by day, midday (our tr.) | de día, medio día |  | 13 src / 46 tok | ox p.113 |
| pa ruwi' | rel | on top of (our tr.) | encima de | pa nuwi' | 28 src / 4466 tok | ox p.113 |
| pa xulan | phr | to the south (our tr.) | al sur |  | 21 src / 147 tok | ox p.113 |
| -pa'- | pos | standing (our tr.) | de pie, parado (p) | in pa'äl; yipa'e' | 10 src / 49 tok | ox p.113 |
| -pa'e' | v.i | stand up (our tr.) | pararse, ponerse de pie | kapa'e'; kixpa'e' | 23 src / 545 tok | ox p.113 |
| pa'äl | pos | standing (our tr.) | parado |  | 15 src / 113 tok | ox p.113 |
| -pab'a' | v.t | arrest, detain | detener, arrestar |  | 13 src / 107 tok | rukan |
| -pach'uj | v.t | braid, plait | trenzar |  | 16 src / 55 tok | rukan |
| pach'un | n | brocade, braided | brocado, trenzado |  | 21 src / 82 tok | rukan |
| pach'un tzij | n | poetry, poem (our tr.) | poesía, poema |  | 14 src / 33 tok | ox p.113 |
| paj | n | word, syllable, verse (our tr.) | palabra, sílaba, verso | jupaj; kapaj | 13 src / 141 tok | ox p.113 |
| palamax | n | kite, butterfly (our tr.) | papalote, mariposa |  | 9 src / 24 tok | ox p.113 |
| palow | n | sea (our tr.) | mar |  | 17 src / 83 tok | ox p.113 |
| Pan Q'än | name | Antigua (our tr.) | Antigua |  | 11 src / 48 tok | ox p.113 |
| par | n | skunk, squirrel (our tr.) | zorrillo, ardilla |  | 20 src / 470 tok | ox p.113 |
| pas | n | sash (our tr.) | faja |  | 14 src / 168 tok | ox p.113 |
| patan | n | tribute ; civic duty (our tr.) | tributo ; carga cívica |  | 15 src / 71 tok | ox p.113 |
| patz'än | n | cornstalk, cf. aj | caña de milpa, vea aj ; caña de milpa |  | 7 src / 23 tok | rukan ox p.113 |
| patän | n | tumpline, oak (our tr.) | mecapal, roble |  | 11 src / 30 tok | ox p.113 |
| pawi'aj | n | hat (our tr.) | sombrero | nupawi'; var. pay'aj | 9 src / 19 tok | ox p.113 |
| -pax | v.i | burst (our tr.) | estallar | xpax; nipax atzük | 21 src / 120 tok | ox p.113 |
| -paxij | v.t | break (our tr.) | quebrarse |  | 15 src / 99 tok | ox p.113 |
| pay | adj | mocking (our tr.) | burlón |  | 8 src / 65 tok | ox p.113 |
| peraj | n | panel of fabric, shawl | lienzo, perraje, rebozo ; perraje, rebozo |  | 18 src / 518 tok | rukan ox p.113 |
| -peyoj | v.t | invite | invitar |  | 9 src / 55 tok | rukan |
| peyon | adj | hired (our tr.) | contratado | apeyon | 6 src / 9 tok | ox p.113 |
| pi'q | n | corncob, var. pe'q | xilote, var. pe'q ; olote, corncob |  | 9 src / 11 tok | rukan ox p.113 |
| -pik'- | pos | on tiptoe (our tr.) | de puntillas | pik'ïl; in pik'ïl; yipik'e'; ninpik'ab'a' | 10 src / 55 tok | ox p.113 |
| pir | n | little piece | trocito, pedazo |  | 11 src / 28 tok | rukan |
| pisb'äl | n | blanket, panel of fabric, cloth to wrap things | manta, lienzo, tela para envolver cosas |  | 7 src / 15 tok | rukan |
| -piskolin | v.i | turn over (our tr.) | voltear |  | 6 src / 14 tok | ox p.114 |
| pixa' | n | advice (our tr.) | consejo |  | 18 src / 958 tok | ox p.114 |
| pixab'aj | v.t | advise (our tr.) | -aconsejar | Nata' xirup'ixab'aj. | 6 src / 9 tok | ox p.114 |
| -pixab'an | v.i | give advice, advise | dar consejos, aconsejar |  | 9 src / 29 tok | rukan |
| -plin | v.i | slip, fall (things, thoughts) (our tr.) | resbalarse, caerse (cosas, pensamientos) | xplin el chi nuq'a' | 7 src / 18 tok | ox p.114 |
| po't | n | huipil (our tr.) | huipil |  | 12 src / 218 tok | ox p.114 |
| pok'öl | pos | lying as fallen on the ground | tirado en el suelo ; tirado(s) |  | 7 src / 16 tok | rukan ox p.114 |
| pom | n | incense | incienso ; copal |  | 14 src / 264 tok | rukan ox p.114 |
| pop | n | woven mat | petate |  | 18 src / 158 tok | rukan ox p.114 |
| poqolaj | n | dust | polvo ; polvo, polvoroso |  | 13 src / 102 tok | rukan ox p.114 |
| poqon | adj | spicy (our tr.) | picante |  | 13 src / 285 tok | ox p.114 |
| poqonal | n | suffering | sufrimiento |  | 16 src / 437 tok | rukan ox p.114 |
| -poroj | v.t | burn | quemar |  | 17 src / 263 tok | rukan |
| potz' | n | police | policía ; policia |  | 9 src / 61 tok | rukan ox p.114 |
| poy | n | scarecrow | espantapájaros |  | 9 src / 26 tok | rukan ox p.114 |
| pun- | adj | thick (things) (our tr.) | grueso (cosas) | punül | 24 src / 249 tok | ox p.114 |
| -purij | v.t | bite ; disobey (our tr.) | morder ; desobedecor | Xirupurij ri tz'i'.; xirupurij | 7 src / 21 tok | ox p.114 |
| -päj | v.t | measure by weight | medir por peso ; sacar (líquido) | xinpäj el | 9 src / 21 tok | rukan ox p.113 |
| päk | n | custard apple (our tr.) | anona | var. kawex | 8 src / 13 tok | ox p.113 |
| q'a'n | n | ladder, bridge (our tr.) | escalera, puente | aq'a'n | 9 src / 16 tok | ox p.115 |
| q'ab'arel | n | drunk, drunkard (our tr.) | borracho, bolo |  | 8 src / 21 tok | ox p.115 |
| -q'ajan | v.i | sing (animals) (our tr.) | cantar (animales) |  | 16 src / 143 tok | ox p.115 |
| -q'alajin | v.i | be clear; be visible | ser claro, ser visible |  | 17 src / 518 tok | rukan |
| -q'alajisaj | v.t | explain (our tr.) | explicar | var. q'alajirisaj | 7 src / 44 tok | ox p.115 |
| q'anq'öj | adj | light yellow (our tr.) | amarillo claro |  | 10 src / 16 tok | ox p.115 |
| q'aq' | n | fire (our tr.) | fuego | qaq'aq' | 27 src / 945 tok | ox p.115 |
| -q'at- | pos | stuck, jammed (our tr.) | trabado (p) | xq'ate'; q'atäl | 24 src / 3100 tok | ox p.115 |
| q'atöy tzij | n | court officer, municipal officer, lawyer | juez, funcionario municipal, abogado ; abogado |  | 13 src / 55 tok | rukan ox p.115 |
| -q'ax | v.i | remain, leave, pass, cross ; understand (our tr.) | quedarle, dejar, pasar cruzar ; entender | xq'ax pa awi'; niq'ax pa awi'; xq'ax | 23 src / 1213 tok | ox p.115 |
| -q'axaj | v.t | cross, pass to the other side | cruzar, pasar de otro lado |  | 11 src / 307 tok | rukan |
| q'axomal | n | pain, worrying, suffering | dolor, pena, sufrimiento |  | 13 src / 91 tok | rukan |
| q'axomäl | n | pain (our tr.) | dolor |  | 6 src / 8 tok | ox p.115 |
| -q'axon | v.i | hurt, be in pain | dolerse ; doler ; -k'u'x apenarse, afligirse |  | 10 src / 133 tok | rukan ox p.115 |
| q'aynäq | adj | rotten (our tr.) | podrido | ruq'aynaqil; q'aynäq chïk | 7 src / 17 tok | ox p.115 |
| q'ayïs | n | weeds, plants, trash | plantas, maleza, monte, basura ; plantas, maleza monte, basura |  | 14 src / 260 tok | rukan ox p.115 |
| q'e'l | n | water jug (in other towns k'uk'u') (our tr.) | cántaro (en otros pueblos se dice k'uk'u') |  | 7 src / 9 tok | ox p.115 |
| q'e'ël | pos | lying crosswise (our tr.) | atravesado |  | 6 src / 6 tok | ox p.115 |
| -q'ejel- | v.t | visit, greet (our tr.) | visitar, saludar | xixqaq'ejela'; xpe q'ejelonel | 19 src / 191 tok | ox p.115 |
| q'enum | n | jocote (hog plum) (our tr.) | jocote | q'än q'enüm; käq q'enüm; var. q'enüm | 7 src / 17 tok | ox p.115 |
| q'eqq'öj | adj | light black (our tr.) | negro claro |  | 6 src / 9 tok | ox p.115 |
| q'equ'm | adj | dark (our tr.) | obscuro |  | 13 src / 254 tok | ox p.115 |
| q'etaj | n | armful | brazada |  | 7 src / 23 tok | rukan |
| -q'etej | v.t | hug (our tr.) | abrazar | xiruq'etaj; rat naq'etej; man naq'etej ta; yatb'enq'etej | 13 src / 154 tok | ox p.115 |
| q'ij | n | sun, day (our tr.) | sol, día | q'ija'; xqaq'ij, k'a | 34 src / 7606 tok | ox p.115 |
| q'ijob'äl | n | clock (our tr.) | reloj | kiq'ijob'äl | 8 src / 30 tok | ox p.115 |
| q'in | n | warp thread | urdimbre |  | 6 src / 18 tok | rukan |
| q'ojom | n | music (our tr.) | música |  | 17 src / 225 tok | ox p.116 |
| -q'ojomaj | v.t | play (music) (our tr.) | tocar (música) |  | 9 src / 45 tok | ox p.116 |
| q'ojomanel | n | marimba player, musician (our tr.) | marimbista, música/o |  | 6 src / 20 tok | ox p.116 |
| q'ol | n | glue (our tr.) | pegamento |  | 9 src / 18 tok | ox p.116 |
| q'opoj | n | maiden, young woman, virgin | señorita, joven |  | 11 src / 92 tok | rukan |
| q'oq' | n | chilacayote squash (our tr.) | chilacayote |  | 9 src / 23 tok | ox p.116 |
| q'or | n | atole ; lazy (our tr.) | atole ; perezoso | äj q'or; aws q'or | 15 src / 188 tok | ox p.116 |
| q'os | n | onion, fodder | cebolla, zacate |  | 7 src / 72 tok | rukan |
| q'utu'n | n | food (our tr.) | comida | kiq'utu'n | 12 src / 148 tok | ox p.116 |
| -q'äj | v.t | break | quebrar ; vertir en un líquido |  | 9 src / 28 tok | rukan ox p.115 |
| q'än | adj | yellow (our tr.) | amarillo | q'anq'öj | 20 src / 171 tok | ox p.115 |
| q'ëq | adj | black (our tr.) | negro |  | 15 src / 79 tok | ox p.115 |
| -q'öl | v.t | deceive ; joke (our tr.) | engañar(se) ; bromear, chistar | yeq'olon | 10 src / 34 tok | rukan ox p.116 |
| q'ös | n | grass, fodder (our tr.) | zacate |  | 7 src / 18 tok | ox p.116 |
| qab'anob'al | n | our culture, our roots | nuestra cultura, nuestras raíces |  | 10 src / 62 tok | rukan |
| -qasaj | v.t | lower (our tr.) | rebajar | xuqasaj b'a | 21 src / 709 tok | ox p.114 |
| qitzij | n | truth (our tr.) | verdad | var. arcaica qi | 19 src / 2041 tok | ox p.114 |
| qo'l | n | turkey (our tr.) | pavo, chompipe | iqo'l | 9 src / 34 tok | ox p.114 |
| qulaj | n | neck, necklace, throat (our tr.) | cuello, collar, garganta | nuqul; ruqul | 11 src / 30 tok | ox p.114 |
| -qumun | v.i | drink (our tr.) | tomar, berber | kaqumun; kixqumun | 6 src / 58 tok | ox p.115 |
| -qup- | v.t | cut (our tr.) | cortar | xinqupila'; xinqupixtaj; xinqupij | 20 src / 359 tok | ox p.115 |
| qupib'äl | n | scissors, knife | tijeras, knife ; cuchillo |  | 10 src / 46 tok | rukan ox p.115 |
| -qupij | v.t | cut Q' | cortar |  | 12 src / 90 tok | rukan |
| -qupin | v.i | cut (general) (our tr.) | cortar (general) | kaqupin; kixqupin | 9 src / 49 tok | ox p.115 |
| -qäj | v.t | rent, lend, borrow | rentar, prestar, alquilar ; prestar | ninqäj apwaq; taqaja' rupwaq xta Irma | 11 src / 50 tok | rukan ox p.114 |
| -qöl | v.t | hurt | lastimar |  | 13 src / 18 tok | rukan |
| -qüm | v.t | drink (our tr.) | tomar (líquido) | taqumu'; xinqüm; ninqüm nukape; var. qün | 13 src / 96 tok | ox p.115 |
| rab'- | pos | flexible (our tr.) | flexible | rab'äl; rab'aräq | 14 src / 90 tok | ox p.116 |
| rachäq | n | leftover pulp or unground pieces | bagazo ; base de la mazorca, base del tallo de arbol |  | 10 src / 30 tok | rukan ox p.116 |
| rajawal | n | spirit; rajawal juyu' owner, guardian spirit of the mountain | encanto; rajawal juyu' dueño, espíritu guardián de la montaña |  | 12 src / 97 tok | rukan |
| rajowaxik | n | need, lack | necesidad, hace falta |  | 7 src / 112 tok | rukan |
| ramaj | n | hour (our tr.) | hora |  | 25 src / 684 tok | ox p.116 |
| -raq' | pos | leaning (our tr.) | inclinado (p) | in raq'äl; yiraq'e'; ninraq'ab'a'; raq'äl; raq'arïk | 15 src / 33 tok | ox p.116 |
| raqän jay | n | corridor, hallway (our tr.) | corredor pasillo |  | 6 src / 13 tok | ox p.116 |
| raqän ya' | n | river (our tr.) | río |  | 15 src / 69 tok | ox p.116 |
| rat | pron | you (our tr.) | Usted, tu, vos |  | 29 src / 6799 tok | ox p.116 |
| raxkej | n | cramp | calambre |  | 11 src / 20 tok | rukan ox p.116 |
| raxröj | adj | light green (our tr.) | verde claro |  | 11 src / 19 tok | ox p.116 |
| raxtew | n | chills, malaria, paladness | escalofrío, malaria, paludismo |  | 8 src / 15 tok | rukan ox p.116 |
| raxwach | n | (ear of) blue corn | mazorca negra, maíz negro |  | 8 src / 15 tok | rukan |
| raxya' | n | ice-cold water (our tr.) | agua helada |  | 9 src / 19 tok | ox p.116 |
| rayib'äl | n | desire, interest, aspiration, craving | deseo, interés, aspiración, antojo |  | 9 src / 62 tok | rukan |
| -rayij | v.t | desire, crave (our tr.) | desear, antojarse |  | 27 src / 1285 tok | ox p.116 |
| rejqa'n | n | weight, town office or obligation | peso, carga (oficio) del pueblo |  | 9 src / 14 tok | rukan |
| rejqalem | n | esteem, importance, obligation (our tr.) | estimación, importancia, obligación importance, weight, obligation |  | 14 src / 520 tok | rukan |
| releb'al q'ij | n | east, lit. sunrise (our tr.) | el este, oriente, lit. salido del sol |  | 11 src / 32 tok | ox p.116 |
| relik | adj | enough (our tr.) | suficiente |  | 9 src / 184 tok | ox p.116 |
| ri' | part | that, the (our tr.) | eso, el, la |  | 38 src / 28906 tok | ox p.116 |
| ri'j | adj | old (our tr.) | viejo | rijta'q; rijitäq | 22 src / 174 tok | ox p.116 |
| rija' | pron | he, she (our tr.) | él, ella |  | 29 src / 12087 tok | ox p.116 |
| rik'in jub'a' | adv | perhaps, possibly, if anything, maybe | acaso, quizás, si acaso, tal vez |  | 9 src / 402 tok | rukan |
| ro' | num | fifth (our tr.) | quinto |  | 19 src / 158 tok | ox p.116 |
| Rochoch Ajaw | n | Catholic Church, also said of some Protestant churches | Iglesia Católica, también de unas iglesias evangélicas |  | 9 src / 47 tok | rukan |
| -ropin | v.i | jump, leap (our tr.) | brincar, saltar | yiropin; Rat karopin; kixropin; xiropin | 15 src / 81 tok | ox p.116 |
| -ropop | v.i | flap wings (our tr.) | alentear | tiropop nib'e | 9 src / 20 tok | ox p.117 |
| -roqowisaj | v.t | boil | hervir |  | 7 src / 22 tok | rukan ox p.117 |
| rox | num | third (our tr.) | tercero | rox samaj | 31 src / 714 tok | ox p.117 |
| rox winäq | n | third person (our tr.) | tercera persona |  | 6 src / 84 tok | ox p.117 |
| rub'i' | n.poss | his/her name (our tr.) | su nombre |  | 22 src / 1689 tok | ox p.117 |
| ruchi' | rel | its mouth, edge (our tr.) | su boca, orilla |  | 31 src / 1597 tok | ox p.117 |
| ruchi' jay | n | door | puerta ; puerta dentro de la casa |  | 19 src / 66 tok | rukan ox p.117 |
| ruchojmilal | n | directional (our tr.) | direccional |  | 11 src / 695 tok | ox p.117 |
| ruchuq'a' | n.poss | strong (our tr.) | fuerte |  | 19 src / 737 tok | ox p.117 |
| ruk'an | n | girlfriend or boyfriend | novia o novio |  | 10 src / 22 tok | rukan |
| ruk'exel | n | replacement, namesake | sustituto, tocayo |  | 12 src / 584 tok | rukan |
| ruk'isib'äl | adj | last (our tr.) | último |  | 10 src / 424 tok | ox p.117 |
| ruk'u'x ichaj | n | cabbage (our tr.) | repollo |  | 7 src / 11 tok | ox p.117 |
| ruk'u'x tinamït | n | town center, central plaza, center of town | centro de la ciudad, parque central |  | 7 src / 39 tok | rukan |
| ruka' | n | his molar, his grinding stone (our tr.) | su muela, su piedra de moler |  | 7 src / 9 tok | ox p.117 |
| ruka'n | num | second, his/her boyfriend/girlfriend (our tr.) | segundo, su novia/o |  | 20 src / 566 tok | ox p.117 |
| ruka'n samaj | n | second work (of the cornfield) (our tr.) | segundo trabajo (de milpa) |  | 6 src / 6 tok | ox p.117 |
| rukaj | num | fourth (our tr.) | cuarta |  | 21 src / 185 tok | ox p.117 |
| rukojol | rel | in the middle of, between | en medio de, entre |  | 13 src / 105 tok | rukan |
| ruloman | part | while | mientras |  | 6 src / 33 tok | rukan |
| ruloq'ik | n | purchase of…, their or your purchase | su compra, compra de… |  | 6 src / 18 tok | rukan |
| runaq' wachaj | n | eye (our tr.) | ojo | runaq' ruwa | 8 src / 11 tok | ox p.117 |
| runuk'ik | n | the ordering the threads one by one on the loom bars | el ordenar los hilos del tejido uno por uno sobre los sostenedores |  | 11 src / 102 tok | rukan |
| runuk'uxik | n | ordered, put in order, its ordering | su ordenamiento |  | 6 src / 14 tok | rukan |
| rupaläj | n.poss | face (our tr.) | cara |  | 10 src / 28 tok | ox p.117 |
| ruq'a' che' | n | branch (our tr.) | rama |  | 11 src / 13 tok | ox p.117 |
| ruq'a' ka' | n | metate hand stone (our tr.) | mano de metate |  | 6 src / 7 tok | ox p.117 |
| ruq'ijul | n | time ; future time (our tr.) | tiempo ; apo tiempo futuro |  | 15 src / 508 tok | ox p.117 |
| ruqajb'al q'ij | n | west (our tr.) | oeste, occidente |  | 6 src / 9 tok | ox p.117 |
| ruqul | n.poss | its throat, its neck (our tr.) | su garganta, su cuello |  | 11 src / 76 tok | ox p.117 |
| rusamajixik | n | its use | su uso |  | 11 src / 186 tok | rukan |
| rusolik | n | resolution, untangling (our tr.) | resolución, desenredo |  | 12 src / 75 tok | rukan |
| rute' q'aq' | n | kitchen (our tr.) | cocina |  | 9 src / 33 tok | ox p.117 |
| rutz'i' | n | otter (our tr.) | nutria, perro de agua |  | 7 src / 21 tok | ox p.117 |
| rutz'ik | n | elbow (our tr.) | codo |  | 8 src / 18 tok | ox p.117 |
| rutz'umal | n | skin (of people) (our tr.) | pellejo, piel (personas) |  | 12 src / 38 tok | ox p.117 |
| rutza'n | n | the point or ends of something | punta de cualquiera cosa |  | 17 src / 280 tok | rukan |
| rutzijol | n | newspaper (our tr.) | periódico |  | 28 src / 3562 tok | ox p.117 |
| ruwa jay | n | patio (our tr.) | patio |  | 7 src / 19 tok | ox p.117 |
| ruwaq | num | sixth (our tr.) | sexto |  | 19 src / 104 tok | ox p.117 |
| ruwaqxaq | num | eighth (our tr.) | octavo |  | 10 src / 44 tok | ox p.117 |
| ruwi' | rel | its tip, head (our tr.) | su punta, cabeza |  | 31 src / 6166 tok | ox p.117 |
| ruwi' jay | n | roof (our tr.) | techo |  | 12 src / 26 tok | ox p.117 |
| ruwi' q'ab'aj | n | fingers (our tr.) | dedos de la mano | ruwi' nuq'a' | 8 src / 48 tok | ox p.117 |
| ruwuq | num | seventh (our tr.) | séptima |  | 17 src / 121 tok | ox p.117 |
| ruwäch che' | n | fruit (our tr.) | fruta |  | 14 src / 93 tok | ox p.117 |
| ruwäch ulew | n | the land, terrain (our tr.) | el terreno |  | 11 src / 40 tok | ox p.117 |
| ruxaq awän | n | cornstock leaf, corn husk | hoja de milpa |  | 7 src / 11 tok | rukan ox p.117 |
| ruxaq che' | n | leaf (our tr.) | hoja |  | 8 src / 18 tok | ox p.117 |
| ruxe' | n | root | raíz ; xinga (de maíz) |  | 31 src / 366 tok | rukan ox p.117 |
| ruxe'el | n | root (our tr.) | raíz |  | 17 src / 369 tok | ox p.117 |
| ruxikin jay | n | bathroom, toilet (our tr.) | baño, sanitario | var. ruxkin jay | 10 src / 16 tok | ox p.118 |
| räx | adj | green, unripe (our tr.) | verde, no maduro (plant) | raxröj | 20 src / 177 tok | ox p.116 |
| -sa' | v.t | roast, sun-dry, dry (our tr.) | asar, asolear, secar |  | 6 src / 12 tok | ox p.118 |
| sakil | n | ground squash seed (pepitoria) (our tr.) | pepitoria |  | 14 src / 606 tok | ox p.118 |
| -samaj | n.poss | work (our tr.) | trabajo | nusamaj | 37 src / 9080 tok | ox p.118 |
| samajel | n | worker (our tr.) | trabajador | samajela' | 24 src / 844 tok | ox p.118 |
| samajib'äl | n | tool, instrument | herramienta, instrumento |  | 18 src / 419 tok | rukan |
| -samajij | v.t | work | trabajar |  | 21 src / 798 tok | rukan |
| -samäj | v.i | work (our tr.) | trabajar | yisamäj; tisamäj; kesamäj | 21 src / 1119 tok | ox p.118 |
| sanayi' | n | sand | arena ; grama |  | 20 src / 116 tok | rukan ox p.118 |
| saq'ij | n | summer (our tr.) | verano |  | 18 src / 72 tok | ox p.118 |
| saq'ul | n | banana (our tr.) | guineo, banano | nimasaq'ul | 15 src / 51 tok | ox p.118 |
| saqb'äch | n | hail (our tr.) | granizo | rusaqb'ach; saqb'äch jöb'; var. saqb'öch; saqb'öch jöb' | 6 src / 22 tok | ox p.118 |
| saqil | n | clarity | claridad |  | 18 src / 316 tok | rukan |
| saqmolo' | n | eggs (our tr.) | huevos |  | 11 src / 84 tok | ox p.118 |
| saqsöj | adj | off-white (our tr.) | medio-blanco |  | 7 src / 20 tok | ox p.118 |
| saqwäch | n | potatoes (our tr.) | papas (Patzitzía) |  | 12 src / 32 tok | ox p.118 |
| sase' | n | liver (our tr.) | hídago |  | 11 src / 26 tok | ox p.118 |
| -set- | pos | round, spherical (our tr.) | esférico | setël; setesïk; setesäq | 35 src / 971 tok | ox p.118 |
| setaj | n | land | parcela, pedazos de tierra circulares parcel or plot, circular patches of |  | 7 src / 12 tok | rukan |
| setesïk | adj | round (our tr.) | redondo |  | 11 src / 68 tok | ox p.118 |
| si' | n | firewood (our tr.) | leña |  | 19 src / 146 tok | ox p.118 |
| -sib' | v.t | inject, puncture something soft | inyectar, pullar |  | 14 src / 51 tok | rukan |
| sik' | n | cigar, cigarette (our tr.) | cigarro, cigarrillo | isik' | 7 src / 22 tok | ox p.118 |
| -sik'ij- | v.t | read, shout (our tr.) | leer, gritar | ninsik'ij | 23 src / 334 tok | ox p.118 |
| -sik'in- | v.i | shout, sing (animals) (our tr.) | gritar, cantar (para animales) | kasik'in; nisik'in; kojsik'in | 19 src / 555 tok | ox p.118 |
| -siloj | v.t | move, stretch (our tr.) | mover, estirar |  | 21 src / 144 tok | ox p.118 |
| silonel | n | earthquake (our tr.) | temblor |  | 14 src / 142 tok | ox p.118 |
| silonïk | n | movement, exercise (our tr.) | movimiento, ejercicio |  | 6 src / 46 tok | ox p.118 |
| simïl | adj | delicious, tasty, exquisite | delicioso, sabroso, exquisito |  | 6 src / 38 tok | rukan |
| sina'j | n | scorpion (our tr.) | alacrán | nusina'j | 6 src / 13 tok | ox p.118 |
| -sipaj | v.t | give as a gift (our tr.) | regalar | ninsipaj; nisipäx chwe | 25 src / 289 tok | ox p.118 |
| -sipoj | v.i | swell, distend | hincharse |  | 16 src / 36 tok | rukan |
| sokaj | n | nest (our tr.) | nido |  | 7 src / 16 tok | ox p.118 |
| sotz' | n | bat (our tr.) | murciélago |  | 14 src / 30 tok | ox p.119 |
| spa'ch | n | lizard (our tr.) | largartija |  | 6 src / 16 tok | ox p.119 |
| stape | part | even though, even if, although | aunque |  | 10 src / 45 tok | rukan |
| su't | n | sute (headcloth) (our tr.) | sute (headcloth) |  | 18 src / 62 tok | ox p.119 |
| sub'an | n | tamalito | tamalito ; tamal, tamalito |  | 10 src / 52 tok | rukan ox p.119 |
| -surin- | v.i | turn around (our tr.) | dar vuelta | kasurin; kixsurin | 12 src / 45 tok | ox p.119 |
| sutz' | n | cloud, waterfall (our tr.) | nube, catarata |  | 23 src / 391 tok | ox p.119 |
| -säch- | v.t | lose (our tr.) | perder | tasacha'; sachnäq nuwuj; iwir xinsäch nuwuj | 11 src / 105 tok | ox p.118 |
| säq | adj | white (our tr.) | blanco | saqsöj | 23 src / 241 tok | ox p.118 |
| -sël | v.t | slice (our tr.) | rodajar |  | 6 src / 23 tok | ox p.118 |
| -sëq- | v.t | smell, sniff (our tr.) | oler, olfatear | taseqa'; ütz nasëq | 6 src / 22 tok | ox p.118 |
| -sïk'- | v.t | catch, grab (our tr.) | coger | tasik'a' | 8 src / 15 tok | ox p.118 |
| -sök | v.t | cut oneself (our tr.) | cortarse | tasoko' | 7 src / 36 tok | ox p.119 |
| -söl | v.t | resolve, uncoil, untie | resolver, desenrollar |  | 17 src / 121 tok | rukan |
| -söl- | v.t | untangle, unwrap (our tr.) | desenredar, desenvolver | tasolo' | 17 src / 122 tok | ox p.119 |
| -süj- | v.t | offer, sacrifice (our tr.) | ofrecer, sacrificar | ninsüj; tasuju' | 9 src / 84 tok | ox p.119 |
| t'iso'n | n | sewing, thing for sewing or sown thing | costura, cosa para coser o cosa cosida, costurada |  | 11 src / 21 tok | rukan |
| -t'ison | v.i | sew (our tr.) | coser |  | 11 src / 35 tok | ox p.120 |
| t'ison | adj | sewn, sewed up | cosido |  | 9 src / 15 tok | rukan |
| t'oj | adj | deaf (our tr.) | sordo |  | 8 src / 11 tok | ox p.120 |
| takamäl | n | tamal, large and small | tamal, chuchito |  | 6 src / 49 tok | rukan |
| -taluj | v.t | stir up, undo, scatter, distribute, spread (our tr.) | alborotar, deshacer, regar, repartir, diseminar |  | 20 src / 356 tok | ox p.119 |
| -tane | v.i | stop (doing) (our tr.) | dejar de |  | 10 src / 129 tok | ox p.119 |
| tapa'l | n | nance (fruit) (our tr.) | nance |  | 7 src / 12 tok | ox p.119 |
| taq | part | when, if (our tr.) | cuando, si | taq ma jani....ta; var. töq (propuesta para estandar) | 33 src / 20673 tok | ox p.119 |
| taqikil | n | errand (our tr.) | mandado, errand |  | 6 src / 31 tok | ox p.119 |
| taqonem | n | command, imperative (our tr.) | mandato, imperativo |  | 11 src / 338 tok | ox p.119 |
| Tat | part | Sir (vocative) (our tr.) | Señor (vocativa) |  | 19 src / 193 tok | ox p.119 |
| -telej | v.t | carry on the head (our tr.) | cargar en la cabeza |  | 10 src / 18 tok | ox p.119 |
| telemaj | n | shoulder (our tr.) | hombro | rutele'n; nutele'n | 7 src / 19 tok | ox p.119 |
| tem | n | column (our tr.) | columna | rutemal jay | 11 src / 134 tok | ox p.119 |
| tew | adj | cold (our tr.) | frío |  | 20 src / 223 tok | ox p.119 |
| -ti' | v.t | sting, bite (our tr.) | picar, morder |  | 7 src / 18 tok | ox p.119 |
| ti'oj | adj | fat, solid, strong (our tr.) | gordo, macizo, fuerte |  | 15 src / 78 tok | ox p.119 |
| -tijoj | v.t | learn, teach, study (our tr.) | aprender, enseñar, estudiar |  | 27 src / 1639 tok | ox p.119 |
| tijonel | n | teacher (our tr.) | maestro/a | tijonela' | 27 src / 394 tok | ox p.119 |
| tijoxel | n | student (our tr.) | alumno/a | tijoxela' | 20 src / 132 tok | ox p.119 |
| tik'asäs | adj | happy (our tr.) | alegre |  | 7 src / 43 tok | ox p.120 |
| tikirel | adj | powerful, possible (our tr.) | poderoso, es posible |  | 20 src / 1218 tok | ox p.119 |
| tiko'n | n | field, planted field | agricultura, siembra ; siembra |  | 16 src / 389 tok | rukan ox p.119 |
| tikonel | n | farmer | agricultor | tikonela' | 14 src / 68 tok | rukan ox p.119 |
| -tikïr | v.i | begin, be able (our tr.) | comenzar, poder | nitikïr | 15 src / 1646 tok | ox p.120 |
| tinamital | n | population | población |  | 9 src / 114 tok | rukan |
| tinamït | n | town, city (our tr.) | ciudad |  | 20 src / 1108 tok | ox p.120 |
| tiqaq'ij | adv | afternoon, in the afternoon (our tr.) | tarde, en la tarde |  | 17 src / 112 tok | ox p.120 |
| titij | n | flavor (our tr.) | sabor |  | 8 src / 19 tok | ox p.120 |
| -to' | v.t | help, encourage (our tr.) | ayudar, animar | yiruto'; yinuto'; kinato'; xkatinto' | 12 src / 69 tok | ox p.120 |
| to'on | n | bean tamale, tortilla with beans (our tr.) | tamalito de frijol, tortilla con frijol |  | 13 src / 31 tok | ox p.120 |
| tob'äl | n | help (our tr.) | ayuda |  | 11 src / 166 tok | ox p.120 |
| -tok' | pos | lying with legs spread (our tr.) | acostado piernabierto (p) | in tok'öl; yitok'e'; nintok'ob'a' | 16 src / 87 tok | ox p.120 |
| top | n | crab (our tr.) | congrejo | var. töp | 12 src / 76 tok | ox p.120 |
| toq'a' | adv | at night (our tr.) | de noche |  | 7 src / 86 tok | ox p.120 |
| -torij | v.t | throw away, throwout | tirar, echar ; tirar | Xa xutorij qa. | 14 src / 126 tok | rukan ox p.120 |
| tra's | n | peach (our tr.) | durazno | var. t(u)ras | 7 src / 35 tok | ox p.120 |
| tuj | n | sauna | temascal, sauna ; temascal |  | 12 src / 115 tok | rukan ox p.120 |
| tul | n | reeds for making woven mats | tule grueso |  | 6 src / 30 tok | rukan |
| tulül | n | sapote, Pouteria sapota | zapote ; zapote, caimito |  | 10 src / 34 tok | rukan ox p.120 |
| tunay | n | elderberry | sauco, saúco |  | 8 src / 18 tok | rukan |
| tuq' | adj | purple (our tr.) | morado |  | 9 src / 19 tok | ox p.120 |
| tz'aläm | n | shelf, board ; blackboard (our tr.) | estante, tabla ; pizarrón |  | 10 src / 29 tok | ox p.121 |
| tz'aläm tz'ib'ab'äl | n | blackboard (our tr.) | pizarra, pizarrón |  | 7 src / 15 tok | ox p.121 |
| -tz'apij | v.t | close (our tr.) | cerrar | tatz'apej ruchi' jay; tz'apb'äl rutza'n | 24 src / 284 tok | ox p.121 |
| tz'apäl | adj | closed (our tr.) | cerrado |  | 10 src / 38 tok | ox p.121 |
| -tz'aqatirisaj | v.t | complete, perfect, fulfill (our tr.) | completar, perfeccionar, cumplir | xutz'aqatirisaj rujuna' | 7 src / 19 tok | ox p.121 |
| tz'aqät | adv | on the dot, exact (our tr.) | en punto, exacto |  | 14 src / 182 tok | ox p.121 |
| tz'etb'äl | n | example | ejemplo |  | 12 src / 36 tok | rukan |
| -tz'etetäj | v.i | be observed | ser observado |  | 12 src / 37 tok | rukan |
| tz'ib' | n | letter, writing (our tr.) | letra, escritura |  | 16 src / 296 tok | ox p.121 |
| tz'ib'ab'äl | n | pen, pencil (our tr.) | pluma, lápiz | atz'ib'ab'al; rutz'ib'ab'al | 16 src / 100 tok | ox p.121 |
| -tz'ib'aj | v.t | write (our tr.) | escribir |  | 26 src / 929 tok | ox p.121 |
| -tz'ib'an | v.i | write (our tr.) | escribir | katz'ib'an; kixtz'ib'an; xojtz'ib'an | 23 src / 804 tok | ox p.121 |
| tz'ib'anel | n | secretary, author (our tr.) | secretaria, autor |  | 11 src / 27 tok | ox p.121 |
| tz'ik | adj | stingy, cheap | codo, tacaño |  | 9 src / 23 tok | rukan |
| tz'il | adj | dirty (our tr.) | sucio |  | 24 src / 217 tok | ox p.121 |
| tz'in | n | cassava (our tr.) | yuca | tzakon tz'in; käq tz'in | 9 src / 21 tok | ox p.121 |
| tz'iran | n | silence (our tr.) | silencio |  | 15 src / 574 tok | ox p.121 |
| tz'ite' | n | palo pito seed (Erythrina berteroana), red, used in ceremony | palo pito, frijol de palo pito |  | 8 src / 19 tok | rukan ox p.121 |
| tz'o' | n | nixtamal (our tr.) | nixtamal |  | 11 src / 37 tok | ox p.122 |
| -tz'ub'aj | v.t | kiss, suck (our tr.) | besar, chupar | xkatintz'ub'aj; Xutz'ub'aj ruchi' ri ruk'an. | 9 src / 40 tok | ox p.122 |
| tz'uj | n | drop, droplet | gota |  | 19 src / 72 tok | rukan |
| -tz'ukuj | v.t | sprout, arise, devise (our tr.) | brotar, surgir, idear |  | 8 src / 77 tok | ox p.122 |
| -tz'ukutäj | v.i | begin, commence, start | empezar, comenzar, iniciar |  | 8 src / 42 tok | rukan |
| tz'um | n | leather | cuero |  | 18 src / 204 tok | rukan |
| -tz'uman | v.i | suckle (our tr.) | mamar |  | 13 src / 72 tok | ox p.122 |
| tz'un | n | hide (animal skin) (our tr.) | cuero (pellejo de animal) | var. tz'um | 8 src / 78 tok | ox p.122 |
| tz'unün | n | hummingbird (our tr.) | colibrí | taq tz'unün | 14 src / 29 tok | ox p.122 |
| -tz'uy- | pos | seated (our tr.) | sentado (p) | tz'uyül; yitz'uye'; nintz'uyub'a' | 33 src / 1968 tok | ox p.122 |
| -tz'uye'- | v.i | sit down (our tr.) | sentarse | katz'uye'; Rïx kixtz'uye'; tz'uyutz'äq; tz'uyutz'ïk | 25 src / 580 tok | ox p.122 |
| -tz'ët- | v.t | see (our tr.) | ver | tatz'eta'; xintz'etela' | 22 src / 1033 tok | ox p.121 |
| -tz'ük | v.t | begin, start, invent (our tr.) | iniciar, empezar, comenzar, inventar begin, commence, start, invent |  | 10 src / 126 tok | rukan |
| -tzal- | pos | side, beside, tilted (our tr.) | lado, lado de, inclinado | in tzalan; yitzale'; nintzalab'a'; tzalatzïk | 36 src / 778 tok | ox p.120 |
| -tzalan | pos | tilted, leaning to one side (our tr.) | ladeado |  | 12 src / 31 tok | ox p.120 |
| tzam | n | liquor | licor |  | 10 src / 42 tok | rukan |
| tzamaj | n | nose (our tr.) | nariz | rutza'm | 8 src / 24 tok | ox p.120 |
| tzatz | n | cap (our tr.) | gorra |  | 9 src / 31 tok | ox p.120 |
| tzay | adv | extremely, very (our tr.) | externadamente, mucho | tzay tew; var. tzan | 10 src / 29 tok | ox p.121 |
| tze'en | v.i | laugh (our tr.) | reírse | xtze'en | 11 src / 37 tok | ox p.121 |
| -tzeqej | v.t | lift, raise (our tr.) | levantar, alzar | titzeqej iq'a' | 6 src / 54 tok | ox p.121 |
| tzetz | n | cucumber (our tr.) | pepino |  | 8 src / 21 tok | ox p.121 |
| tzij | n | word (our tr.) | palabra |  | 38 src / 10788 tok | ox p.121 |
| -tzijon | v.i | talk (our tr.) | hablar | xitzijon; xb'etzijon | 27 src / 1353 tok | ox p.121 |
| tzijïl | adj | lit, turned on (our tr.) | encendido |  | 6 src / 109 tok | ox p.121 |
| tzimay | n | dipper | guacal, recipiente ; jícara, taza, tazón |  | 11 src / 27 tok | rukan ox p.121 |
| -tzolin | v.i | return, go back (our tr.) | regresar, volver |  | 26 src / 1621 tok | ox p.121 |
| -tzu' | v.t | see, look at (our tr.) | ver, mirar | katintzu'; kinatzu'; kixqatzu'; tatzu'; rïn nintzu' | 25 src / 1716 tok | ox p.121 |
| tzuy | n | gourd (tecomate) (our tr.) | tecomate | nutzuy; rutzuy | 13 src / 41 tok | ox p.121 |
| -tzäk | v.t | cook | cocer |  | 8 src / 28 tok | rukan |
| -tzäq | v.t | lose (our tr.) | perder | tatzaqa' | 9 src / 25 tok | ox p.121 |
| tzäy | adj | salty (our tr.) | salado | tzayläj | 10 src / 23 tok | ox p.121 |
| -tzïj | v.t | light | encender | tatzija'; xutzij roma ri chäj | 7 src / 94 tok | rukan ox p.121 |
| -tzüq | v.t | feed, give food | dar de comer, alimentar |  | 7 src / 23 tok | rukan |
| -täq | v.t | send ; command, order (our tr.) | enviar ; mandar, ordenar | niqatäq | 24 src / 530 tok | ox p.119 |
| -tïj | v.t | eat (our tr.) | comer | titija' | 15 src / 254 tok | ox p.120 |
| -tïk | v.t | plant, breed, (Xtik - engendered) | sembrar, engendrar (Xtik - engendrado) |  | 14 src / 143 tok | rukan |
| -tïk- | v.t | sow (our tr.) | sembrar | tatika' | 14 src / 145 tok | ox p.119 |
| -töj | v.t | pay (our tr.) | pagar | tatojo'; var. toj | 11 src / 79 tok | ox p.120 |
| töq | part | when (our tr.) | cuando | var. taq | 12 src / 617 tok | ox p.120 |
| -tük | v.t | shake, stir (our tr.) | menear, revolver | tatuku' | 7 src / 385 tok | ox p.120 |
| -tün | v.t | join, unite | juntar, unir ; juntar | tatunu'; var. tun | 13 src / 142 tok | rukan ox p.120 |
| uchuq'a' | n | force, power, energy | fuerza, poder, energía |  | 13 src / 520 tok | rukan |
| uk' | n | louse (our tr.) | piojo | ruk' | 10 src / 51 tok | ox p.122 |
| uk'ya' | n | beverage, flavored soft drink of a variety of flavors | bebida, refresco |  | 10 src / 31 tok | rukan |
| ula' | n | visitor, invited guest, tourist | visitante, invitado, turista, huésped | pl. ula'i' | 12 src / 25 tok | rukan ox p.122 |
| umül | n | rabbit (our tr.) | conejo | umuli'; var. umul | 15 src / 67 tok | ox p.122 |
| uq | n | wrap skirt (corte) (our tr.) | corte |  | 12 src / 102 tok | ox p.122 |
| utiw | n | coyote ; middleman in crop exports (our tr.) | coyote ; intermediario en exportación de siembras o en | utiwa' | 15 src / 99 tok | ox p.122 |
| utzil | n | favor (our tr.) | favor |  | 24 src / 2108 tok | ox p.122 |
| uxla' | n | steam, breath, smell ; smell (our tr.) | vapor, respiración, olor ; olor | majun ruxla' ta | 13 src / 54 tok | ox p.122 |
| uxlan | v.i | rest (our tr.) | descansar | yatuxlan; yinuxlan; yojuxlan | 12 src / 22 tok | ox p.122 |
| uxlanib'äl k'u'x | n | Mayan spirituality | espiritualidad Maya |  | 6 src / 54 tok | rukan |
| -wa' | v.i | eat (our tr.) | comer | kiwa'; kojwa'; yojwa'; yib'ewa'; xab'ewa' | 11 src / 82 tok | ox p.122 |
| wachb'äl | n | photo (our tr.) | foto | var. achib'äl | 6 src / 18 tok | ox p.122 |
| wachinäq | n | thing (our tr.) | cosa |  | 16 src / 309 tok | ox p.122 |
| -wak- | pos | leaning on the hands (our tr.) | echado sobre las manos como para hacer | in wak'äl; ninwak'aba' | 35 src / 4577 tok | ox p.122 |
| wakamin | adv | now (our tr.) | ahora |  | 9 src / 136 tok | ox p.122 |
| wakx | n | cow, cattle (our tr.) | vaca, ganado | taq wakx | 17 src / 125 tok | ox p.122 |
| wal | n.poss | my son/daughter (of a woman) (our tr.) | mi hijo/a (de mujer) |  | 18 src / 105 tok | ox p.122 |
| waqi' | num | six (our tr.) | seis |  | 19 src / 359 tok | ox p.122 |
| waqlajuj | num | sixteen (our tr.) | dieciséis |  | 17 src / 78 tok | ox p.122 |
| waqxaqi' | num | eight (our tr.) | ocho |  | 21 src / 179 tok | ox p.122 |
| waqxaqlajuj | num | eighteen (our tr.) | dieciocho |  | 15 src / 84 tok | ox p.122 |
| waqxaqtäq | num | eight by eight (our tr.) | de ocho en ocho |  | 6 src / 8 tok | ox p.122 |
| warab'äl | n | bedroom (our tr.) | alcoba, dormitorio | var. warab'äl jay | 12 src / 55 tok | ox p.122 |
| warab'äl jay | n | hotel | hotel |  | 8 src / 23 tok | rukan |
| -waraj | v.t | keep vigil | velar |  | 10 src / 18 tok | rukan ox p.123 |
| waran | n | sleepiness, tiredness (our tr.) | sueño, cansancio | yin k'o nuwaran | 9 src / 60 tok | ox p.123 |
| -warisaj | v.t | put to sleep, numb (our tr.) | adormecer | nikiwarisaj; ninwarisaj; yekiwarisaj; yatinwarisaj | 6 src / 26 tok | ox p.123 |
| wawe' | adv | here (our tr.) | aquí |  | 28 src / 1588 tok | ox p.123 |
| wayb'äl | n | dining room (our tr.) | comedor |  | 11 src / 63 tok | ox p.123 |
| wayb'äl jay | n | diner | comedor |  | 7 src / 44 tok | rukan |
| wayjal | n | hunger | hambre |  | 16 src / 226 tok | rukan ox p.123 |
| -weqon | v.i | adorn oneself, get dressed (our tr.) | adornar, vestirse, ponerse la ropa. | tiweqon | 6 src / 11 tok | ox p.123 |
| wexaj | n | trousers (our tr.) | pantalón | var. wex | 11 src / 60 tok | ox p.123 |
| winaqil | n | people, populace, culture | pueblo, cultura |  | 13 src / 85 tok | rukan |
| wo'o' | num | five (our tr.) | cinco | wo'o' tumin | 23 src / 493 tok | ox p.123 |
| wolajuj | num | fifteen (our tr.) | quince |  | 18 src / 127 tok | ox p.123 |
| -won- | pos | squatting ; crouched, squatting (our tr.) | en cuclillas ; acurrucado, encuclillas (p) | yiwone'; in wonöl; ninwonob'a' | 26 src / 584 tok | ox p.123 |
| wotz'otz' | n | toasted, toasted tortilla | tostado, tortilla tostada ; chicharrones, tostaditos |  | 7 src / 21 tok | rukan ox p.123 |
| wotäq | num | five by five (our tr.) | 5_5 |  | 8 src / 14 tok | ox p.123 |
| wuch' | n | opossum (our tr.) | tacuasín, tacuazín | taq wuch' | 8 src / 31 tok | ox p.123 |
| -wuch'- | pos | rolled up (our tr.) | enrollado (p) | in wuch'ül; yiwuch'e' | 12 src / 55 tok | ox p.123 |
| wuj | n | book (our tr.) | libro | re wuj re'; la wuj la' | 31 src / 1545 tok | ox p.123 |
| -wujil | n.poss | identification document, ID card (our tr.) | documento de identificación, carnet identity papers, passport, etc. |  | 17 src / 549 tok | rukan |
| -wuq- | pos | crouched forward (our tr.) | acurrucado hacia adelante (p) | in wuqül; yiwuqe'; ninwuqub'a' | 33 src / 1846 tok | ox p.123 |
| wuqlajuj | num | seventeen (our tr.) | diecisiete |  | 13 src / 64 tok | ox p.123 |
| wuqu' | num | seven (our tr.) | siete |  | 23 src / 594 tok | ox p.123 |
| wuxuj | n | harvest (fruits, coffee and vegetables) | corte, cosecha (de frutas, café y vegetales) |  | 7 src / 10 tok | rukan |
| -wäch | rel | in front of (our tr.) | enfrente de | chi iwäch; chi kiwäch; chi nuwäch; chi ruwäch; var. chiwäch | 30 src / 6523 tok | ox p.123 |
| -wär | v.i | sleep (our tr.) | dormir | yiwär, yawär; tiwär; kewär; yib'ewär | 20 src / 301 tok | ox p.123 |
| -wëq | v.t | decorate | adornar | taweqa' | 8 src / 30 tok | rukan ox p.123 |
| -wüx | v.t | harvest fruit or vegetables | cosechar frutas y vegetales |  | 7 src / 16 tok | rukan |
| xa ja ri' | part | however, but, nevertheless | sin embargo, pero, no obstante |  | 7 src / 47 tok | rukan |
| -xa'oj | v.i | throw oneself (our tr.) | arrojarse |  | 12 src / 30 tok | ox p.124 |
| xa'oj | n | vomit | vómito |  | 10 src / 21 tok | rukan ox p.123 |
| xa'r | n | small jug (our tr.) | jarilla |  | 6 src / 11 tok | ox p.123 |
| xab'on | n | soap (our tr.) | jabón |  | 12 src / 29 tok | ox p.123 |
| xajab' | n | sandal (caite) (our tr.) | caite |  | 14 src / 83 tok | ox p.123 |
| xajan | n | sin | pecado |  | 17 src / 163 tok | rukan |
| xajoj | n | dance | baile, danza ; baile |  | 19 src / 46 tok | rukan ox p.123 |
| -xajon | v.i | dance (our tr.) | bailar | yixajon; kaxajon; kixxajon; xixajon; yib'exajon; xab'exajon | 10 src / 62 tok | ox p.123 |
| -xak- | pos | standing with legs apart (our tr.) | parado con las piernas abiertas (p) | in xakäl; yixakake'; ninxakab'a' | 31 src / 922 tok | ox p.123 |
| xan | n | adobe, cement block, brick | adobe, bloc, ladrillo ; pared |  | 19 src / 139 tok | rukan ox p.123 |
| xar | adj | blue (our tr.) | azul |  | 16 src / 77 tok | ox p.124 |
| xara | n | clay cup (our tr.) | taza de barro |  | 9 src / 26 tok | ox p.124 |
| xarxöj | adj | light blue (our tr.) | azul claro |  | 9 src / 14 tok | ox p.124 |
| xax | adj | thin (our tr.) | delgado |  | 20 src / 153 tok | ox p.124 |
| -xe' | n.poss | root (our tr.) | raíz | chi nuxe' | 18 src / 197 tok | ox p.124 |
| xex | n | odor of fish, eggs, or blood | olor de pescado, huevos, y sangre |  | 6 src / 28 tok | rukan |
| -xib'ij | v.t | be afraid | asustar ; asustar, temer | Xinxib'ij wi' | 18 src / 188 tok | rukan ox p.124 |
| xik | n | hawk (our tr.) | gavilán | kixik | 11 src / 26 tok | ox p.124 |
| xik' | n | wings (our tr.) | alas |  | 9 src / 172 tok | ox p.124 |
| xik'a'y | adj | thin (like a twig) (our tr.) | delgado (como ramita de un arbol) | una persona: | 7 src / 29 tok | ox p.124 |
| -xik'an | v.i | fly (our tr.) | volar |  | 15 src / 94 tok | ox p.124 |
| xil | n | piece (our tr.) | pedazo |  | 11 src / 35 tok | ox p.124 |
| ximb'äl | n | belt (our tr.) | cincho |  | 9 src / 27 tok | ox p.124 |
| ximoj | n | knot | nudo |  | 9 src / 79 tok | rukan |
| xkoya' | n | tomato | tomate | ixin xkoya'; xkoya' pa rij | 12 src / 75 tok | rukan ox p.124 |
| xnakät | n | onion | cebolla |  | 10 src / 36 tok | rukan ox p.124 |
| xokon | adj | left | izquierda/o |  | 8 src / 234 tok | rukan |
| xoqa' | phr | good night (our tr.) | buenas noches |  | 6 src / 12 tok | ox p.124 |
| xot | n | roof tile (our tr.) | teja |  | 19 src / 140 tok | ox p.124 |
| xqaq'ij | phr | good afternoon (our tr.) | buenas tardes |  | 7 src / 40 tok | ox p.124 |
| Xta | part | miss, young lady (our tr.) | señorita, señora joven |  | 22 src / 417 tok | ox p.124 |
| -xtan | aff | quickly, suddenly (our tr.) | rapidamente, de repente | xib'inixtan | 18 src / 200 tok | ox p.124 |
| xti | adj | small, short (our tr.) | pequeña, bajita |  | 14 src / 78 tok | ox p.124 |
| xtän | n | young lady (our tr.) | señorita | xtani' | 19 src / 259 tok | ox p.124 |
| -xub'an | v.i | whistle (our tr.) | silbar | yixub'an; yojxub'an | 11 src / 63 tok | ox p.124 |
| -xuk- | pos | kneeling (our tr.) | arrodillado (p) | in xukül; yixuke'; ninxukub'a'; xukül | 40 src / 3275 tok | ox p.124 |
| -xuke' | v.i | kneel | arrodillarse |  | 14 src / 144 tok | rukan |
| xukulem | n | ceremony | ceremonia |  | 9 src / 71 tok | rukan |
| xul | n | penny whistle | silbato ; pito, flauta, chirimiya |  | 23 src / 232 tok | rukan ox p.124 |
| xulan q'ij | n | 12 p.m. to 6 p.m. (our tr.) | 12 p.m. - 6 p.m. |  | 6 src / 7 tok | ox p.124 |
| -xupuj | v.t | blow (our tr.) | soplar | Rija' nuxupuj ruq'aq'. | 14 src / 128 tok | ox p.124 |
| -xïm | v.t | tie | amarrar |  | 11 src / 192 tok | rukan |
| -xöl | v.t | stir, mix (our tr.) | revolver, mesclar |  | 6 src / 19 tok | ox p.124 |
| ya' | n | water | agua ; aqua |  | 40 src / 4673 tok | rukan ox p.125 |
| -ya' | v.t | give, pour, put | dar, verter, poner |  | 40 src / 4673 tok | rukan |
| -ya'aj | v.t | water | regar |  | 7 src / 25 tok | rukan |
| ya'l | n | net or woven bag | red o matate ; red, morral, matate, red, ataraya |  | 19 src / 182 tok | rukan ox p.125 |
| ya'öl na'oj | n | advisor (our tr.) | consejero |  | 8 src / 9 tok | ox p.125 |
| -ya- | v.t | give (our tr.) | dar | Xkatinya' jun achi' | 34 src / 2682 tok | ox p.124 |
| -yakatäj | v.i | get up, wake up (our tr.) | levantarse, despertarse | kayakatäj; kixyakatäj; var. yakatej | 15 src / 71 tok | ox p.125 |
| yakb'äl wuj | n | library, bookcase (our tr.) | biblioteca, librera |  | 7 src / 23 tok | ox p.125 |
| yalan | adv | good, very (our tr.) | bueno, muy |  | 27 src / 2728 tok | ox p.125 |
| yan | adv | already, now, immediately, finally | ya, ahora, enseguida, por fin ; ya | xk'achoj yan | 35 src / 5519 tok | rukan ox p.125 |
| yawa' | adj | sick, ill | enfermo | yawa'i' | 20 src / 289 tok | rukan ox p.125 |
| -yawäj | v.i | get sick | enfermarse |  | 15 src / 56 tok | rukan ox p.125 |
| -yojtäj | v.i | break down (our tr.) | descomponer | xyojtäj nuq'ijob'al | 7 src / 9 tok | ox p.125 |
| -yoke' | v.i | block, stay, not advance. | tardarse, no apurarse |  | 6 src / 36 tok | rukan |
| -yon | n.poss | alone, by oneself (our tr.) | solito, a solas | ayon; ruyon; nuyon; kiyon | 31 src / 3951 tok | ox p.125 |
| yonil | adj | alone, only ; solitude (our tr.) | solo, único, soledad |  | 9 src / 65 tok | ox p.125 |
| yuq'unel | n | shepherd (our tr.) | pastor |  | 6 src / 83 tok | ox p.125 |
| -yuqej | v.t | pull, carry (our tr.) | jalar, llevar |  | 6 src / 61 tok | ox p.125 |
| -yäk | v.t | store, put away, put in place, var. -yïk | guardar, var. -yïk |  | 11 src / 370 tok | rukan |
| -yïk | v.t | raise up, lift | levantar |  | 10 src / 72 tok | rukan |
| -yïk- | v.t | store, keep (our tr.) | guardar | tayika' | 10 src / 73 tok | ox p.125 |
| -yüq | v.t | stretch out | estirar |  | 8 src / 13 tok | rukan |
| -yüq- | v.t | stretch (our tr.) | estirar | tayuqu' | 8 src / 17 tok | ox p.125 |
| äj | n | ear of corn, corn on the cob | elote | qäj | 11 src / 90 tok | rukan ox p.95 |
| äk' | n | chicken, hen | gallina B' ; gallina | taq äk' | 17 src / 195 tok | rukan ox p.95 |
| än | n | spider (our tr.) | araña | var. om, öm, äm | 7 src / 11 tok | ox p.95 |
| ïs | n | body hair (our tr.) | vello |  | 7 src / 38 tok | ox p.102 |
| ök | part | particle of entreaty, pleading (our tr.) | que envuelve la idea de súplica, de ruego. | Ja ök; kere' ök | 8 src / 71 tok | ox p.112 |
| üs | n | mosquito (our tr.) | mosquito |  | 8 src / 12 tok | ox p.122 |
| ütz k'a | phr | well then (our tr.) | Bien, pues. |  | 11 src / 95 tok | ox p.122 |
| ütz nina' | phr | I like the taste, it feels good to me (our tr.) | me gusta el sabor, lo siento bien |  | 6 src / 7 tok | ox p.122 |

## Coined modern terms

Neologisms for technology and institutions. Most come from the Firefox localization and the Kaqchikel Wikipedia; restricted sources are cited by title only. A coinage with one source is a translator's choice, not settled usage; in conversation the Spanish word is often what people say, so do not force a coinage into casual dialogue.

| Kaqchikel | POS | English | Español | Forms / notes | Attest. | Src |
|---|---|---|---|---|---|---|
| kematz'ib' | n | computer (our tr.) | computadora | kem weaving [rukan] + tz'ib' writing; also in neologismos and the ALMG Vocabulario | 11 src / 185 tok | pontoon, wiki, ALMG Vocabulario |
| k'amaya'l | n | internet, network (our tr.) | internet, red (our tr.) | ajk'amaya'l of the internet; okik'amaya'l browser | 9 src / 1448 tok | pontoon, wiki |
| ruxaq k'amaya'l | phr | web page (our tr.) | página web (our tr.) | ruxaq "its leaf, page"; Firefox also writes ajk'amaya'l ruxaq "website" | 3 src / 531 tok | pontoon |
| okik'amaya'l | n | browser | navegador (our tr.) |  | 3 src / 685 tok | pontoon |
| oyonib'äl | n | mobile, telephone | teléfono | lit. instrument for calling (-oyoj call); ALMG Vocabulario and Choltzij also list it | 13 src / 206 tok | pontoon, wiki, ALMG Vocabulario |
| taqoya'l | n | e-mail | correo electrónico (our tr.) | rochochib'al taqoya'l email address [pontoon] | 5 src / 870 tok | pontoon |
| ewan tzij | phr | password (our tr.) | contraseña (our tr.) | lit. hidden word; pl. ewan taq tzij "passwords" [pontoon] | 1 src / 429 tok | pontoon |
| yakb'äl | n | file; storage place (our tr.) | archivo; lugar para guardar (our tr.) | from -yak store; yakb'äl tzyäq wardrobe, yakb'äl wuj bookcase [bloom] | 14 src / 752 tok | pontoon, bloom |
| yakwuj | n | folder | carpeta (our tr.) | lit. paper store | 2 src / 236 tok | pontoon |
| kanob'äl | n | search engine | buscador (our tr.) | from -kanoj search | 2 src / 120 tok | pontoon |
| pitz'ib'äl | n | keyboard | teclado (our tr.) | rare outside Firefox | 1 src / 9 tok | pontoon |
| ch'oy | n | mouse; rat | ratón; rata | the ordinary word for rat (ox p.100), reused for the computer mouse | 18 src / 149 tok | pontoon, ox p.100 |
| elesäy wachib'äl | phr | camera | cámara (our tr.) | lit. image-taker | 2 src / 55 tok | pontoon |
| wachib'äl | n | image, picture, photo (our tr.) | imagen, foto (our tr.) | achib'äl "foto, imagen" in ox p.92 | 13 src / 563 tok | pontoon, wiki |
| silowäch | n | video | video (our tr.) | lit. moving face | 1 src / 125 tok | pontoon |
| chokoy | n | app, application | aplicación (our tr.) |  | 3 src / 396 tok | pontoon, wiki |
| kema' | n | software | software (our tr.) | cf. kem weaving, backstrap loom [rukan] | 6 src / 112 tok | pontoon |
| okisanel | n | user | usuario (our tr.) | from -okisaj use | 2 src / 152 tok | pontoon |
| molojri'ïl | n | session, account, group (our tr.) | sesión, cuenta, grupo (our tr.) | titikirisäx molojri'ïl "sign in" [pontoon]; ordinary sense = association, organization | 8 src / 697 tok | pontoon |
| taluwäch | n | television (our tr.) | televisión | listed in the ALMG Vocabulario | 11 src / 44 tok | wiki, ALMG Vocabulario |
| talutzij | n | radio (our tr.) | radio | listed in the ALMG Vocabulario | 12 src / 47 tok | wiki, ALMG Vocabulario |
| talutz'ib' | n | newspaper (our tr.) | periódico | listed in the ALMG Vocabulario; ox glosses rutzijol as periódico | 5 src / 8 tok | wiki, ALMG Vocabulario |
| xik'anel ch'ich' | phr | airplane (our tr.) | avioneta, avión | lit. flying machine; ch'ich' alone = metal, car | 2 src / 2 tok | ALMG Vocabulario |
| ch'ich' | n | metal, machine, car (our tr.) | máquina, metal, carro | ruch'ich' his machine [ox]; xik'anel ch'ich' airplane | 30 src / 576 tok | ox p.98 |
| aq'omab'äl jay | phr | hospital, clinic (our tr.) | hospital, clínica | lit. house of medicine; aq'omanel doctor | 11 src / 55 tok | wiki, ALMG Vocabulario |
| tijob'äl | n | school (our tr.) | escuela | tijonel teacher, tijoxel student | 20 src / 274 tok | ox p.119, bloom |
| pwäq | n | money (our tr.) | dinero (our tr.) | pwaqb'äl bank [ALMG Vocabulario] | 13 src / 334 tok | wiki |
| q'atb'äl tzij | phr | authority, government (our tr.) | autoridad, gobierno (our tr.) | lit. where the word is decided; champomal = government in legal prose | 15 src / 138 tok | wiki |
| k'amöy b'ey | phr | president, leader (our tr.) | presidente | lit. one who leads the way | 2 src / 2 tok | pontoon, ALMG Vocabulario |
| cholb'äl q'ij | phr | calendar | calendario (our tr.) | lit. day-orderer | 3 src / 35 tok | pontoon |
| ch'utiramaj | n | minute (our tr.) | minuto (our tr.) | lit. small hour (ramaj hour) | 4 src / 76 tok | pontoon |
| q'ijul | n | date (our tr.) | fecha (our tr.) |  | 11 src / 256 tok | pontoon, wiki |
| ch'ich'al na'ojil | phr | artificial intelligence | inteligencia artificial (our tr.) | one Firefox string; not established | 1 src / 1 tok | pontoon |
| uchuq'ab'äl | n | battery | batería (our tr.) | from uchuq'a' strength | 4 src / 9 tok | pontoon |
| tz'ajb'äl | n | printer | impresora (our tr.) |  | 2 src / 10 tok | pontoon |

