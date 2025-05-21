Global Wordnet Formats
======================

![](https://globalwordnet.github.io/schemas/img/GWA_logo.png)

The Global WordNet Association provides three formats for which WordNets can be
published and submitted to the ILI. These are as follows:

* [Lexical Markup Framework compatible XML](#xml)
    * [Example](http://github.com/globalwordnet/schemas/blob/master/example.xml)
    * [DTD](http://globalwordnet.github.io/schemas/WN-LMF-1.4.dtd)
* [JSON-LD using the lemon Vocabulary](#json)
    * [Example](http://github.com/globalwordnet/schemas/blob/master/example.json)
    * [JSON-LD Context](http://globalwordnet.github.io/schemas/wn-json-context-1.4.json)
    * [Schema](http://github.com/globalwordnet/schemas/blob/master/wn-json-schema.json)
* [OntoLex RDF](#rdf)
    * [Example](http://github.com/globalwordnet/schemas/blob/master/example.ttl)

All of these formats are considered equivalent and a converter between them can 
be used at.

A converter and validator is available at [http://server1.nlp.insight-centre.org/gwn-converter/](http://server1.nlp.insight-centre.org/gwn-converter/)

XML
---

The XML is specified by the following [DTD](WN-LMF-1.4.dtd). An example is 
given [here](https://github.com/globalwordnet/schemas/blob/master/example.xml):

The first three lines must always be as follows:

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE LexicalResource SYSTEM "http://globalwordnet.github.io/schemas/WN-LMF-1.4.dtd">
    <LexicalResource xmlns:dc="http://purl.org/dc/elements/1.1/">
    
A file may contain multiple WordNets in different languages:

The following information is required:

* id: A short name for the resource
* label: The full name for the resources
* language: Please follow BCP-47, i.e., use a two-letter code if 
             available else a three-letter code
* email: Please give a contact email address
* license: The license of your resource (please provide URL)
* version: A string identifying this version (preferably follow 
            major.minor format)
* url: A URL for your project homepage
* citation: The paper to cite for this resource
* logo: A link to a Logo (Image URL) for this project

Extra properties may be included from Dublin core and in addition

* status: The status of the resource, e.g., "valid", "checked", "unchecked"
* confidenceScore: A numeric value between 0 and 1 giving the 
                    confidence in the correctness of the element.

        <Lexicon id="example-en"
                 label="Example wordnet (English)"
                 language="en" 
                 email="john@mccr.ae"
                 license="https://creativecommons.org/publicdomain/zero/1.0/"
                 version="1.0"
                 citation="CILI: the Collaborative Interlingual Index. Francis Bond, Piek Vossen, John P. McCrae and Christiane Fellbaum, Proceedings of the Global WordNet Conference 2016, (2016)."
                 url="http://globalwordnet.github.io/schemas/"
                 dc:publisher="Global Wordnet Association">
                 
Each word (lexical entry) must have a unique id:

            <LexicalEntry id="w1">

The part of speech values are as follows:

* n: Noun
* v: Verb
* a: Adjective
* r: Adverb
* s: Adjective Satellite
* c: Conjunction
* p: Adposition (Preposition, postposition, etc.)
* x: Other (inc. particle, classifier, bound morphemes, determiners)
* u: Unknown

                <Lemma writtenForm="grandfather" partOfSpeech="n"/>
                <Sense id="example-en-10161911-n-1" synset="example-en-10161911-n"/>
            </LexicalEntry>
            <LexicalEntry id="w2">
                <Lemma writtenForm="paternal grandfather" partOfSpeech="n"/>
                <Sense id="example-en-1-n-1" synset="example-en-1-n">

The set of relations between senses is limited to the following

**Princeton WordNet Relations**

* antonym: An opposite and inherently incompatible word
* also: See also, a reference of weak meaning
* participle: An adjective that is a participle form a verb
* pertainym: A relational adjective. Adjectives that are pertainyms are usually defined by such phrases as "of or pertaining to" and do not have antonyms. A pertainym can point to a noun or another pertainym
* derivation: A word that is derived from some other word
* domain_topic: Indicates the category of this word
* domain_member_topic: Indicates a word involved in this category described by this word
* domain_region: Indicates the region of this word
* domain_member_region: Indicates a word involved in the region described by this word
* exemplifies: Indicates the usage of this word
* is_exemplified_by: Indicates a word involved in the usage described by this word
* similar: Similar, though not necessarily interchangeable

**Morphosemantic relations**

* agent: A word which is typically the one/that who/which does the action denoted by a given word (e.g. "to eat" - "eater")
* material: A word which is typically the material of a given word (e.g. "wood")
* event: An noun representing the event of a verb (e.g., "(a) meet" - "(to) meet")
* instrument: An instrument for doing a task (e.g., "photocopier" - "photocopy")
* location: A verb derived from the action performed at a place (e.g., "(a) forge" - "(to) forge")
* by_means_of: A word which is typically the means by which something is done (e.g.,g "deceive" - "deception")
* undergoer: A word which is typically the undergoer of a given word (e.g. "honor" - "honoree")
* property: Cause something to have a particular property (e.g., "magnetize" - "magnetization")
* result: A word which is typically the result of a given word (e.g. "nitrify" - "nitrate")
* state: A state caused by the verb (e.g., "sensitize" - "sensitization")
* uses: A verb that uses a noun (e.g., "(to) talc" - "talc")
* destination: The noun indicates the destination of a verb (e.g., "retire" - "retiree")
* body_part: A word which is typically a body part of a given word (e.g. "finger")
* vehicle: A verb indicating movement with a particular vehicle (e.g., "(to) ship" - "ship")

** Non-Princeton WordNet Relations**

* simple_aspect_ip: A word which is linked to another through a change from imperfective to perfective aspect
* secondary_aspect_ip: A word which is linked to another through a change in aspect (ip)
* simple_aspect_pi: A word which is linked to another through a change from perfective to imperfective aspect
* secondary_aspect_pi: A word which is linked to another through a change in aspect (pi)
* feminine: A feminine form of a word
* has_feminine: Indicates the base form of a word with a feminine derivation
* masculine: A masculine form of a word
* has_masculine: Indicates the base form of a word with a masculine derivation
* young: A form of a word with a derivation indicating the young of a species
* has_young: Indicates the base form of a word with a young derivation
* diminutive: A diminutive form of a word
* has_diminutive: Indicates the base form of a word with a diminutive derivation
* augmentative: An augmentative form of a word
* has_augmentative: Indicates the base form of a word with an augmentative derivation
* anto_gradable: A word pair whose meanings are opposite and which lie on a continuous spectrum
* anto_simple: A word pair whose meanings are opposite but whose meanings do not lie on a continuous spectrum
* anto_converse: A word pair that name or describe a single relationship from opposite perspectives
* metaphor: A relation between two senses, where the first sense is a metaphorical extension of the second sense
* has_metaphor: A relation between two senses, where the first sense can be metaphorically extended to the second sense
* metonym: A relation between two senses, where the first sense is a metonymic extension of the second sense
* has_metonym: A relation between two senses, where the first sense can be metonymically extended to the second sense

                    <SenseRelation relType="derivation" target="example-en-10161911-n-1"/>
                </Sense>
            </LexicalEntry>
            <LexicalEntry id="w3">
                <Lemma writtenForm="pay" partOfSpeech="v"/>
              
Syntactic behaviour is given as in Princeton WordNet

                <SyntacticBehaviour subcategorizationFrame="Somebody ----s" id="intransitive"/>
                <SyntacticBehaviour subcategorizationFrame="Somebody ----s somebody" id="transitive"/>
            </LexicalEntry>

Syntactic behaviour can also be given as part of the lexicon and referred to 
with the `subcat` property.

If a synset is already mapped to the ILI please give the ID here. __All synsets must
have an ID that starts with ID of the lexicon followed by a dash, e.g., `example-en` + `-` + `local_synset_id`__.

            <Synset id="example-en-10161911-n" ili="i90287" partOfSpeech="n"
                members="example-en-10161911-n-1 example-en-1-n-1">
                <Definition>
                    the father of your father or mother
                </Definition>


The `members` property gives the list of senses in order.

The set of relations between synsets is limited to the following:

**Princeton WordNet Properties**

* `hypernym`: a concept that is more general than a given concept
* `hyponym`: a concept that is more specific than a given concept
* `instance_hypernym`: the type of an instance
* `instance_hyponym`: an occurrence of something
* `mero_member`: concept A is a member of concept B
* `mero_part`: concept A is a component of concept B
* `mero_substance`: concept A is made of concept B.
* `holo_member`: concept B is a member of concept A
* `holo_part`: concept B is the whole where concept A is a part
* `holo_substance`: concept B is a substance of concept A
* `entails`: impose, involve, or imply as a necessary accompaniment or result
* `causes`: concept A is an entity that produces an effect or is responsible for events or results of concept B.
* `similar`: (of words) expressing closely related meanings
* `attribute`: an abstraction belonging to or characteristic of an entity
* `domain_region`: a concept which is a geographical / cultural domain pointer of a given concept.
* `domain_topic`: a concept which is the scientific category pointer of a given concept.
* `has_domain_region`: a concept which is the term in the geographical / cultural domain of a given concept.
* `has_domain_topic`: a concept which is a term in the scientific category of a given concept.
* `exemplifies`: a concept which is the example of a given concept.
* `is_exemplified_by`: a concept which is the type of a given concept.

**Non-Princeton WordNet Relations**

* `agent`: a concept which is typically the one/that who/which does the action denoted by a given concept.
* `also`: a word having a loose semantic relation to another word
* `anto_converse`: word pairs that name or describe a single relationship from opposite perspectives
* `anto_gradable`: word pairs whose meanings are opposite and which lie on a continuous spectrum
* `anto_simple`: word pairs whose meanings are opposite but whose meanings do not lie on a continuous spectrum
* `antonym`: an opposite and inherently incompatible word
* `attribute`: an abstraction belonging to or characteristic of an entity
* `augmentative`: a concept used to refer to generally larger members of a class
* `be_in_state`: a is qualified by B
* `classified_by`: concept B is modified by classifier A when it is counted.
* `classifies`: a concept A used when counting concept B
* `co_agent_instrument`: a concept which is the instrument used by a given concept in an action.
* `co_agent_patient`: a concept which is the patient undergoing an action carried out by a given concept.
* `co_agent_result`: a concept which is the result of an action taken by a given concept.
* `co_instrument_agent`: a concept which carries out an action by using a given concept as an instrument.
* `co_instrument_patient`: a concept which undergoes an action with the use of a given concept as an instrument.
* `co_instrument_result`: a concept which is the result of an action using an instrument of a given concept.
* `co_patient_agent`: a concept which carries out an action a given concept undergoing.
* `co_patient_instrument`: a concept which is used as an instrument in an action a given concept undergoes.
* `co_result_agent`: a concept which takes an action resulting in a given concept.
* `co_result_instrument`: a concept which is used as an instrument in an action resulting in a given concept.
* `co_role`: a concept undergoes an action in which a given concept is involved.
* `constitutive`: core semantic relations that define synsets
* `derivation`: a concept which is a derivationally related form of a given concept.
* `diminutive`: a concept used to refer to generally smaller members of a class
* `direction`: a concept which is the direction of the action or event expressed by a given concept.
* `domain`: a concept which is a Topic, Region or Usage pointer of a given concept.
* `domain_region`: a concept which is a geographical / cultural domain pointer of a given concept.
* `domain_topic`: a concept which is the scientific category pointer of a given concept.
* `eq_synonym`: A and B are equivalent concepts but their nature requires that they remain separate (e.g. Exemplifies)
* `exemplifies`: a concept which is the example of a given concept.
* `feminine`: a concept used to refer to female members of a class
* `has_augmentative`: a concept which has a special concept for generally larger members of its class
* `has_diminutive`: a concept which has a special concept for generally smaller members of its class
* `has_domain`: a concept which is a term of a given Topic, Region or Usage concept.
* `has_domain_region`: a concept which is the term in the geographical / cultural domain of a given concept.
* `has_domain_topic`: a concept which is a term in the scientific category of a given concept.
* `has_feminine`: a concept which has a special concept for female members of its class
* `has_masculine`: a concept which has a special concept for male members of its class
* `has_young`: a concept which has a special concept for young members of its class
* `holo_location`: B is a place located in A
* `holo_portion`: B is an amount/piece/portion of A
* `holonym`: A makes up a part of B
* `in_manner`: B qualifies the manner in which an action or event expressed by A takes place
* `instrument`: a concept which is the instrument necessary for the action or event expressed by a given concept.
* `involved`: a concept which is the action or event a given concept typically involved in.
* `involved_agent`: a concept which is the action done by an agent expressed by a given concept.
* `involved_direction`: a concept which is the action with the direction expressed by a given concept.
* `involved_instrument`: a concept which is typically the action with the instrument expressed by a given concept.
* `involved_location`: a concept which is the event happening in a place expressed by a given concept.
* `involved_patient`: a concept which is the action that the patient expressed by a given concept undergoing.
* `involved_result`: a concept which is the action or event with a result of a given concept comes into existence.
* `involved_source_direction`: a concept which is the action beginning from a place of a given concept.
* `involved_target_direction`: a concept which is the action or event leading to a place expressed by a given concept.
* `ir_synonym`: a concept that means the same except for the style or connotation
* `is_caused_by`: a comes about because of B
* `is_entailed_by`: opposite of entails
* `is_exemplified_by`: a concept which is the type of a given concept.
* `is_subevent_of`: a takes place during or as part of B, and whenever A takes place, B takes place
* `location`: a concept which is the place where the event expressed by a given concept happens.
* `manner_of`: a qualifies the manner in which an action or event expressed by B takes place
* `masculine`: a concept used to refer to male members of a class
* `mero_location`: A is a place located in B
* `mero_portion`: A is an amount/piece/portion of B
* `meronym`: B makes up a part of A
* `other`: any relation not otherwise specified
* `participle`: a concept which is a participial adjective derived from a verb expressed by a given concept.
* `patient`: a concept which is the one/that who/which undergoes a given concept.
* `pertainym`: a concept which is of or pertaining to a given concept.
* `restricted_by`: a relation between nominal (pronominal) B and an adjectival A (quantifier/determiner)
* `restricts`: a relation between an adjectival A (quantifier/determiner) and a nominal (pronominal) B
* `result`: a concept which comes into existence as a result of a given concept.
* `role`: a concept which is involved in the action or event expressed by a given concept.
* `secondary_aspect_ip`: a concept which is linked to another through a change in aspect (ip)
* `secondary_aspect_pi`: a concept which is linked to another through a change in aspect (pi)
* `simple_aspect_ip`: a concept which is linked to another through a change from imperfective to perfective aspect
* `simple_aspect_pi`: a concept which is linked to another through a change from perfective to imperfective aspect
* `source_direction`: a concept which is the place from where the event expressed by a given concept begins.
* `state_of`: B is qualified by A
* `subevent`: B takes place during or as part of A, and whenever B takes place, A takes place
* `target_direction`: a concept which is the place where the action or event expressed by a given concept leads to.
* `young`: a concept used to refer to young members of a class

                <SynsetRelation relType="hypernym" target="example-en-10162692-n"/>
            </Synset>

If you wish to define a new concept call the concept "in" (ILI New). If there is
no mapping to the ILI leave this field empty (it is required).

            <Synset id="example-en-1-n" ili="in" partOfSpeech="n">
                <Definition>A father's father; a paternal grandfather</Definition>

You can include metadata (such as source) at many points
The ILI Definition must be at least 20 characters or five words

                <ILIDefinition dc:source="https://en.wiktionary.org/wiki/farfar">
                    A father's father; a paternal grandfather
                </ILIDefinition>
            </Synset>

You must include all targets of relations

            <Synset id="example-en-10162692-n" ili="i90292" partOfSpeech="n"/>
        </Lexicon>
        <Lexicon id="example-sv"
                 label="Example wordnet (Swedish)"
                 language="sv" 
                 email="john@mccr.ae"
                 license="https://creativecommons.org/publicdomain/zero/1.0/"
                 version="1.0"
                 citation="CILI: the Collaborative Interlingual Index. Francis Bond, Piek Vossen, John P. McCrae and Christiane Fellbaum, Proceedings of the Global WordNet Conference 2016, (2016)."
                 url="http://globalwordnet.github.io/schemas/"
                 dc:publisher="Global Wordnet Association">

The list of lexical entries (words) in your wordnet

            <LexicalEntry id="w4">
                <Lemma writtenForm="farfar" partOfSpeech="n"/>

Synsets need not be language-specific but senses must be

                <Sense id="example-sv-2-n-1" synset="example-en-1-n">
                    <SenseExample dc:source="Europarl Corpus">
                        Jag vill berätta för er att min farfar var svensk beredskapssoldat vid norska gränsen under andra världskriget, ett krig som Sverige stod utanför
                    </SenseExample>
                </Sense>
            </LexicalEntry>
        </Lexicon>
    </LexicalResource>

***Pronunciation***

Since 2021, the schema has the ability to represent the pronunciation of lemmas.

This is in the `<Pronunciation>` element, which gives the IPA text.   It has the following attributes:
* `variety` uses the IETF language tags to indicate dialect, for example encoding British English in IPA as `en-GB-fonipa`
* `notation`:  can encode further information such as indicating a particular dialect (this was `notes` in the paper)
* `phonemic`: indicates whether the transcription is phonemic ('true') or phonetic (`false`), defaulting to 'false'
* `audio`:  gives the URL of an audio file of the pronuncation

An example of encoding is given below:

        <LexicalEntry id="ex-rabbit-n">
            <Lemma writtenForm="rabbit" partOfSpeech="n"/>
                <Pronunciation variety="en-GB-fonxsamp en-US-fonxsamp" 
		            audio ="https://path/rabbit.flac">'r\{bIt</Pronunciation>
	        <Pronunciation variety="en-AU-fonxsamp" notation="weak vowel merger" 
		            audio ="https://path/rabbit1.flac">'r\{b@t</Pronunciation>
             </Lemma>
         </LexicalEntry>


**Wordnet Extensions**

A file may contain a lexicon extension which serves to augment an existing lexicon with new lexical entries, synsets, senses, relations, etc.
They are defined much like regular lexicons, but the `<Extends>` element specifies the ID and version of the base lexicon:

        <LexiconExtension id="ewn-cs-example"
                          label="English WordNet Computer Science Terms (example)"
                          language="en"
                          email="goodmami@uw.edu"
                          license="https://creativecommons.org/publicdomain/zero/1.0/"
                          version="1.0">
            <Extends id="ewn" version="2020" />

The contents of the lexicon extension are the same as a regular lexicon with the addition of elements for external lexical entries, synsets, and senses.
There are two uses of external elements.
First, they allow one to add additional information to the corresponding element in the base lexicon, such as adding a new sense to an existing lexical entry:

            <ExternalLexicalEntry id="ewn-process-n">
                <Sense id="ewn-process-n-20000123" synset="ewn-20000123-n" />
            </ExternalLexicalEntry>

In the above example, the `ewn-process-n` ID is not used to create a new lexical entry, but rather it must already exist in the base lexicon.
The external lexical entry (as well as other external senses or synsets) may only add information; therefore it may not specify metadata or elements required on lexical entries, such as for the lemma.

Second, they introduce an ID which may be referenced by new structures, such as the target of synset relation:

            <ExternalSynset id="ewn-06581154-n" />
            <Synset id="ewn-20000123-n" ili="" partOfSpeech="n">
                <Definition>a running instance of a computer program</Definition>
                <SynsetRelation relType="hypernym" target="ewn-06581154-n" />
            </Synset>

Due to the way external IDs are used, a lexicon extension may not exist in the same file as the base lexicon.

**Wordnet Dependencies**

Some wordnets depend upon others, such as those in the [Open Multilingual Wordnet](https://lr.soh.ntu.edu.sg/omw/) which depend upon the Princeton WordNet for synset structure.
With the `<Requires>` element, it is possible to explicitly codify those dependencies:

        <Lexicon id="spawn"
                 label="Multilingual Central Repository"
                 language="es"
                 email="bond@ieee.org"
                 license="https://creativecommons.org/licenses/by/3.0/"
                 version="1.4+omw"
                 citation="Aitor Gonzalez-Agirre, Egoitz Laparra and German Rigau. 2012. `Multilingual Central Repository version 3.0: upgrading a very large lexical knowledge base &lt;http://adimen.si.ehu.es/web/sites/all/modules/pubdlcnt/pubdlcnt.php?file=http://adimen.si.ehu.es/~rigau/publications/gwc12-glr.pdf&amp;nid=18&gt;`_. In *Proceedings of the 6th Global WordNet Conference (GWC 2012)*. Matsue, Japan."
                 url="http://adimen.si.ehu.es/web/MCR/"
                 dc:publisher="Global Wordnet Association"
                 dc:format="OMW-LMF"
                 dc:description="Wordnet made from OMW 1.0 data"
                 confidenceScore="1.0">
	        <Requires id="pwn" version="3.0" />

This element signifies to an application processing the wordnet that the required wordnet should be loaded as well.
The `<Requires>` element may also be used on a `<LexiconExtension>` for cases where the lexicon extends one wordnet but requires another.

JSON
----

The JSON format follows that of the XML and is based on [JSON-LD](http://json-ld.org)
[An example](https://github.com/globalwordnet/schemas/blob/master/example.json)
of the JSON is as follows:

The top level of a JSON graph consists of an object with two properties `@context`
which must be the fixed string referring to the JSON-LD context and `@graph`
giving the lexicon format. This structure is required for submission to the 
Collaborative Interlingual Index, but web services may of course return shorter
fragments of the structure.

    { 
      "@context": "http://globalwordnet.github.io/schemas/wn-json-context-1.4.json",
      "@graph": [{

The following are required properties of every WordNet (note the language
must be given twice). `@id` gives the identifier of this wordnet (should be
unique in this document) and `@type` must be `lime:Lexicon`.

          "@context": { "@language": "en" },
          "@id": "example-en",
          "@type": "lime:Lexicon", 
          "label": "Example wordnet (English)",
          "language": "en",
          "email": "john@mccr.ae",
          "rights": "https://creativecommons.org/publicdomain/zero/1.0/",
          "version": "1.0",

In addition the properties `citation`, `url`, `logo`, `status`, `confidenceScore` and any 
property from [Dublin Core Elements 1.1](http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=elements)
May be used

          "citation": "CILI: the Collaborative Interlingual Index. Francis Bond, Piek Vossen, John P. McCrae and Christiane Fellbaum, Proceedings of the Global WordNet Conference 2016, (2016).",
          "url": "http://globalwordnet.github.io/schemas",
          "publisher": "Global Wordnet Association",

The entries are given as a list under the `entry` property it requires an `@id`
`partOfSpeech` and `lemma` and may have `sense`, `synBehavior`, `status`, 
`confidence` and Dublin Core properties. The lemma has only a single value 
`writtenForm` and the `partOfSpeech` must be one of the following:
[ `noun`, `verb`, `adjective`, `adverb`, `adjective_satellite`, `phrase`, `conjunction`, `adposition`, `other`, `unknown` ]. The `@id` must be unique in the
document, it is not the same as the `@id` of the wordnet or any other entry.

          "entry": [{
              "@id" : "w1",
              "lemma": { "writtenForm": "father" }, 
              "partOfSpeech": "noun",

The Sense requires only an `@id` and a `synsetRef` and may take `status`, 
`confidenceScore`, Dublin Core properties, an `example`.


              "sense": [{
                  "@id": "example-en-10161911-n-1",
                  "synsetRef": "example-en-10161911-n"
              }]
          }, {
              "@id" : "w2",
              "lemma": { "writtenForm": "paternal grandfather" }, 
              "partOfSpeech": "noun",
              "sense": [{
                  "@id": "example-en-1-n-1",
                  "synsetRef": "example-en-1-n",

A sense may also have any number of `relations` which have a `relType` from the
list below and a `target` and may have Dublin Core properties

* `antonym`: An opposite and inherently incompatible word
* `also`: See also, a reference of weak meaning
* `participle`: An adjective that is a participle form a verb
* `pertainym`: A relational adjective. Adjectives that are pertainyms are usually defined by such phrases as "of or pertaining to" and do not have antonyms. A pertainym can point to a noun or another pertainym
* `derivation`: A word that is derived from some other word
* `domain_topic`: Indicates the category of this word
* `domain_member_topic`: Indicates a word involved in this category described by this word
* `domain_region`: Indicates the region of this word
* `domain_member_region`: Indicates a word involved in the region described by this word
* `exemplifies`: Indicates the usage of this word
* `is_exemplified_by`: Indicates a word involved in the usage described by this word

                  "relations": [{
                      "relType": "derivation",
                      "target": "example-en-10161911-n-1",
                      "creator": "John McCrae"
                  }]
              }]
          }, {
              "@id": "w3",
              "lemma": { "writtenForm": "pay" },
              "partOfSpeech": "verb",

The syntactic behavior is given here as follows:

              "synBehavior": [
                 {"label": "Somebody ----s", "@id": "intransitive"}, 
                 {"label": "Somebody ----s somebody", "@id": "transitive"}
               ]
          }],
 
Synsets are listed under the `synset` property.
A synset requires only an `@id`. It may take an `ili` which is a code from the 
CILI (starting with `ili:i`), a `definition`, an `iliDefinition` (which must 
be given in English), `status`, `confidenceScore`, `relations` and Dublin Core properties.

In contrast to the XML form the `ili` is optional. If there is no match omit this
tag, if you wish to propose a new synset add only a `iliDefinition`.

          "synset": [{
              "@id": "example-en-10161911-n",
              "partOfSpeech": "noun",
              "ili": "ili:i90287",

Definitions must have a `gloss` and may be have a `language`, in addition, 
`status`, `confidenceScore` and Dublin Core properties may be added. An 
`iliDefinition` is the same but may not have a language.

              "definition": [{
                "gloss": "that which is perceived or known or inferred to have its own distinct existence (living or nonliving)"
               }],

Synset relations are given as for sense relations except the `target` must be the
`@id` of another synset not a sense. The following properties can be used:

* `hypernym`: A concept with a broader meaning
* `hyponym`: A concept with a narrower meaning
* `instance_hypernym`: The class of objects to which this instance belongs
* `instance_hyponym`: An individual instance of this class
* `part_holonym`: A larger whole that this concept is part of
* `part_meronym`: A part of this concept
* `member_holonym`: A group that this concept is a member of
* `member_meronym`: A member of this concept
* `substance_holonym`: Something where a constituent material is this concept
* `substance_meronym`: A constituent material of this concept
* `entail`: A verb X entails Y if X cannot be done unless Y is, or has been, done.
* `cause`: A verb that causes another
* `similar`: Similar, though not necessarily interchangeable
* `also`: See also, a reference of weak meaning
* `attribute`: A noun for which adjectives express values. The noun weight is an attribute, for which the adjectives light and heavy express values.
* `domain_topic`: Indicates the category of this word
* `domain_member_topic`: Indicates a word involved in this category described by this word
* `domain_region`: Indicates the region of this word
* `domain_member_region`: Indicates a word involved in the region described by this word
* `exemplifies`: Indicates the usage of this word
* `is_exemplified_by`: Indicates a word involved in the usage described by this word

              "relations": [{
                  "relType": "hypernym", "target": "example-en-10162692-n"
              }],

Indicate the members and the order they occur in:

              "members": ["example-en-10161911-n-1", "example-en-1-n-1"]
          }, {
              "@id": "example-en-1-n",
              "partOfSpeech": "noun",
              "definition": [{
                  "gloss": "the father of your father or mother"
              }],
              "iliDefinition": {
                  "gloss": "the father of your father or mother",
                  "source": "https://en.wiktionary.org/wiki/farfar"
              },
              "relations": [
                { "relType": "hypernym", "target": "example-en-10162692-n" }
              ]
          }]
        }, {
          "@context": { "@language": "sv" },
          "@id": "example-sv",
          "@type": "lime:Lexicon", 
          "label": "Example wordnet (Swedish)",
          "language": "sv",
          "email": "john@mccr.ae",
          "license": "https://creativecommons.org/publicdomain/zero/1.0/",
          "version": "1.0",
          "citation": "CILI: the Collaborative Interlingual Index. Francis Bond, Piek Vossen, John P. McCrae and Christiane Fellbaum, Proceedings of the Global WordNet Conference 2016, (2016).",
          "url": "http://globalwordnet.github.io/schemas",
          "publisher": "Global Wordnet Association",
          "entry": [{
              "@id" : "w4",
              "lemma": { "writtenForm": "farfar" }, 
              "form": [{ "writtenForm": "farfäder", "tag": [{ "category": "penn", "value": "NNS" }] }],
              "partOfSpeech": "noun",

Any examples should be given on the sense as follows:

              "sense": [{
                  "@id": "example-sv-2-n-1",
                  "synsetRef": "example-en-1-n",
                  "example": [{
                      "value": "Jag vill berätta för er att min farfar var svensk beredskapssoldat vid norska gränsen under andra världskriget, ett krig som Sverige stod utanför",
                      "source": "Europarl Corpus"
                  }]
              }]
          }]
      }]
    }


The JSON format can be validated by the [JSON Schema](http://json-schema.org)
provided at https://github.com/globalwordnet/schemas/blob/master/wn-json-schema.json

RDF
---

We acknowledge the existence of two vocabularies to wordnet
encoding. The wn-simple.ttl is based on the [W3C RDF/OWL
Representation of WordNet](https://www.w3.org/TR/wordnet-rdf/). This
vocabulary is a straightforward encoding in RDF of the original
Princeton data model where synsets, word senses, and words are the
main classes. In the current version, new relations are added and
additional axioms are provided to reinforce consistency.

The second RDF schema is significantly more flexible and builds
principally on the [W3C OntoLex
Model](https://www.w3.org/2016/05/ontolex/). The
details of the RDF serialization are principally built on those of the
JSON-LD model. We include a separate tutorial here for the benefit of
those who wish to create their resource natively in RDF.

The standard namespaces are

    @prefix dc: <http://purl.org/dc/terms/> .
    @prefix ili: <http://ili.globalwordnet.org/ili/> .
    @prefix lime: <http://www.w3.org/ns/lemon/lime#> .
    @prefix ontolex: <http://www.w3.org/ns/lemon/ontolex#> .
    @prefix owl: <http://www.w3.org/2002/07/owl#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix schema: <http://schema.org/> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
    @prefix synsem: <http://www.w3.org/ns/lemon/synsem#> .
    @prefix wn: <https://globalwordnet.github.io/schemas/wn#> .
    @prefix wordnetlicense: <http://wordnet.princeton.edu/wordnet/license/> .

Each wordnet is an instance of the class `lime:Lexicon` and must have the
following properties

* `rdfs:label`: A name for the wordnet.
* `dc:language`: The BCP 47 identifier for your language (usually a two letter code)
* `schema:email`: An email address for the owner of the wordnet
* `dc:rights`: A link to the license of the resource
* `owl:versionInfo`: The version number of this resource

The mapping to the Lemon-OntoLex model is as follows:

* Words are `ontolex:LexicalEntry`, they must have a `ontolex:canonicalForm` 
  and a `wn:partOfSpeech`. 
* Senses are `ontolex:LexicalSense`, they must have a `ontolex:reference`
* Synsets are `ontolex:LexicalConcept`.
* Definitions and examples are given by `skos:definition` and `skos:example` 
  optionally with a `rdf:value`.

A more extended example is given here:

    <#example-en> a lime:Lexicon ;
      rdfs:label "Example wordnet (English)"@en ;
      dc:language "en" ;
      schema:email "john@mccr.ae" ;
      cc:license <https://creativecommons.org/publicdomain/zero/1.0/> ;
      owl:versionInfo "1.0" ;
      schema:citation "CILI: the Collaborative Interlingual Index. Francis Bond, Piek Vossen, John P. McCrae and Christiane Fellbaum, Proceedings of the Global WordNet Conference 2016, (2016)." ;
      schema:url "http://globalwordnet.github.io/schemas/" ;
      dc:publisher "Global Wordnet Association" ;
      lime:entry <#w1>, <#w2>, <#w3> .
    
    <#w1> a ontolex:LexicalEntry ;
      ontolex:canonicalForm [
        ontolex:writtenRep "grandfather"@en 
      ] ;
      wn:partOfSpeech wn:noun ;
      ontolex:sense <#example-en-10161911-n-1> .
    
    <#example-en-10161911-n-1>  a ontolex:LexicalSense ;
      ontolex:reference <#example-en-10161911-n> .
    
    <#w2> a ontolex:LexicalEntry ;
      ontolex:canonicalForm [
        ontolex:writtenRep "paternal grandfather"@en 
      ] ;
      wn:partOfSpeech wn:noun ;
      ontolex:sense <#example-en-1-n-1> .
    
    <#example-en-1-n-1> a ontolex:LexicalSense ;
      ontolex:reference <#example-en-1-n> .
    
    [] a ontolex:SenseRelation ;
      vartrans:source <#example-en-1-n-1> ;
      vartrans:category wn:derivation ;
      vartrans:target <#example-en-10161911-n-1> ;
      dc:creator "John McCrae"@en .
              
    <#w3> a ontolex:LexicalEntry ;
      ontolex:canonicalForm [
        ontolex:writtenRep "pay"@en
      ] ;
      wn:partOfSpeech wn:verb ;
      synsem:synBehavior <#transitive>, <#intransitive> .

    <#intransitive> rdfs:label "Somebody ----s"@en .
    <#transitive> rdfs:label "Somebody ----s somebody"@en .
    
    <#example-en-10161911-n> a ontolex:LexicalConcept ;
      wn:partOfSpeech wn:noun ;
      skos:inScheme <#example-en> ;
      wn:ili ili:i90287 ;
      wn:definition [
        rdf:value "the father of your father or mother"@en
      ] ;
      wn:memberList ( <#example-en-1016911-n-1> <#example-en-1-n-1> ) .
    
    [] 
      vartrans:source <#example-en-10161911-n> ;
      vartrans:category wn:hypernym ; 
      vartrans:target <#example-en-10162692-n> .
              
    <#example-en-1-n> a ontolex:LexicalConcept ;
      wn:partOfSpeech wn:noun ;
      skos:inScheme <#example-en> ;
      wn:definition [
        rdf:value "the father of your father or mother"@en 
      ] ;
      wn:iliDefinition [
        rdf:value "the father of your father or mother"@en ;
        dc:source "https://en.wiktionary.org/wiki/farfar"
      ] .
    
    []
      vartrans:source <#example-en-1-n> ;
      vartrans:category wn:hypernym ;
      vartrans:target <#example-en-10162692-n> .
    
    <#example-sv> a lime:Lexicon ;
      rdfs:label "Example wordnet (Swedish)"@sv ;
      dc:language "sv" ;
      schema:email "john@mccr.ae" ;
      cc:license <https://creativecommons.org/publicdomain/zero/1.0/> ;
      owl:versionInfo "1.0" ;
      schema:citation "CILI: the Collaborative Interlingual Index. Francis Bond, Piek Vossen, John P. McCrae and Christiane Fellbaum, Proceedings of the Global WordNet Conference 2016, (2016)." ;
      schema:url "http://globalwordnet.github.io/schemas" ;
      dc:publisher "Global Wordnet Association" ;
      lime:entry <#w4> .
    
    <#w4> a ontolex:LexicalEntry ;
      ontolex:canonicalForm [
        ontolex:writtenRep "farfar"@sv 
      ] ;
      ontolex:otherForm [
        ontolex:writtenRep "farfäder"@sv ;
        wn:tag [
            wn:category "penn" ;
            rdf:value "NNS" 
        ]
      ] ;
      wn:partOfSpeech wn:noun ;
      wn:sense <#example-sv-2-n-1> .
    
    <#example-sv-2-n-1> a ontolex:LexicalSense ;
      ontolex:reference <#example-en-1-n> ;
      wn:example [
        rdf:value "Jag vill berätta för er att min farfar var svensk beredskapssoldat vid norska gränsen under andra världskriget, ett krig som Sverige stod utanför"@sv ;
        dc:source "Europarl Corpus"
      ] .
