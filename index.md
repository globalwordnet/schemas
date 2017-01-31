Global Wordnet Formats
======================

The Global WordNet Association provides three formats for which WordNets can be
published and submitted to the ILI. These are as follows:

* [Lexical Markup Framework compatible XML](#xml)
    * [Example](http://github.com/globalwordnet/schemas/blob/master/example.xml)
    * [DTD](http://globalwordnet.github.io/schemas/WN-LMF-1.0.dtd)
* [JSON-LD using the lemon Vocabulary](#json)
    * [Example](http://github.com/globalwordnet/schemas/blob/master/example.json)
    * [JSON-LD Context](http://globalwordnet.github.io/schemas/wn-json-context-1.0.json)
    * [Schema](http://github.com/globalwordnet/schemas/blob/master/wn-json-schema.json)
* [lemon-based RDF](#rdf)
    * [Example](http://github.com/globalwordnet/schemas/blob/master/example.ttl)

All of these formats are considered equivalent and a converter between them can 
be used at.

XML
---

The XML is specified by the following [DTD](WN-LMF-1.0.dtd). An example is 
given [here](https://github.com/globalwordnet/schemas/blob/master/example.xml):

The first three lines must always be as follows:

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE LexicalResource SYSTEM "http://globalwordnet.github.io/schemas/WN-LMF-1.0.dtd">
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

* antonym: An opposite and inherently incompatible word
* also: See also, a reference of weak meaning
* verb_group: Verb senses that similar in meaning and have been manually grouped together.
* participle: An adjective that is a participle form a verb
* pertainym: A relational adjective. Adjectives that are pertainyms are usually defined by such phrases as "of or pertaining to" and do not have antonyms. A pertainym can point to a noun or another pertainym
* derivation: A word that is derived from some other word
* domain_category: Indicates the category of this word
* domain_member_category: Indicates a word involved in this category described by this word
* domain_region: Indicates the region of this word
* domain_member_region: Indicates a word involved in the region described by this word
* exemplifies: Indicates the usage of this word
* is_exemplified_by: Indicates a word involved in the usage described by this word

                    <SenseRelation relType="derivation" target="example-en-10161911-n-1"/>
                </Sense>
            </LexicalEntry>
            <LexicalEntry id="w3">
                <Lemma writtenForm="pay" partOfSpeech="v"/>
                
Syntactic Behaviour is given as in Princeton WordNet

                <SyntacticBehaviour subcategorizationFrame="Sam cannot %s Sue "/>
                <SyntacticBehaviour subcategorizationFrame="Sam and Sue %s"/>
                <SyntacticBehaviour subcategorizationFrame="The banks %s the check"/>
            </LexicalEntry>

If a synset is already mapped to the ILI please give the ID here. __All synsets must
have an ID that starts with ID of the lexicon followed by a dash, e.g., `example-en` + `-` + `local_synset_id`__.

            <Synset id="example-en-10161911-n" ili="i90287" partOfSpeech="n">
                <Definition>
                    the father of your father or mother
                </Definition>
The set of relations between synsets is limited to the following:


* agent
* also: See also, a reference of weak meaning
* antonym
* attribute: A noun for which adjectives express values. The noun weight is an attribute, for which the adjectives light and heavy express values.
* be_in_state
* causes: A verb that causes another
* classified_by
* classifies
* co_agent_instrument
* co_agent_patient
* co_agent_result
* co_instrument_agent
* co_instrument_patient
* co_instrument_result
* co_patient_agent
* co_patient_instrument
* co_result_agent
* co_result_instrument
* co_role
* direction
* domain_category: Indicates the category of this word
* domain_member_category: Indicates a word involved in this category described by this word
* domain_member_region: Indicates a word involved in the region described by this word
* domain_region: Indicates the region of this word
* domain_topic
* entails: A verb X entails Y if X cannot be done unless Y is, or has been, done.
* eq_synonym
* exemplifies: Indicates the usage of this word
* has_domain_region
* has_domain_topic
* holo_location
* holo_member: A group that this concept is a member of
* holo_part: A larger whole that this concept is part of
* holo_portion
* holo_substance: Something where a constituent material is this concept
* holonym
* hypernym: A concept with a broader meaning
* hyponym: A concept with a narrower meaning
* in_manner
* instance_hypernym: The class of objects to which this instance belongs
* instance_hyponym: An individual instance of this class
* instrument
* involved
* involved_agent
* involved_direction
* involved_instrument
* involved_location
* involved_patient
* involved_result
* involved_source_direction
* involved_target_direction
* is_caused_by
* is_entailed_by
* is_exemplified_by: Indicates a word involved in the usage described by this word
* is_subevent_of
* location
* manner_of
* mero_location
* mero_member: A member of this concept
* mero_part: A part of this concept
* mero_portion
* mero_substance: A constituent material of this concept
* meronym
* other
* patient
* restricted_by
* restricts
* result
* role
* similar
* similar: Similar, though not necessarily interchangeable
* source_direction
* state_of
* subevent
* target_direction
* verb_group: Verb senses that similar in meaning and have been manually grouped together.

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
      "@context": "http://globalwordnet.github.io/schemas/wn-json-context-1.0.json",
      "@graph": [{

The following are required properties of every WordNet (note the language
must be given twice). `@id` gives the identifier of this wordnet (should be
unique in this document) and `@type` must be `ontolex:Lexicon`.

          "@context": { "@language": "en" },
          "@id": "example-en",
          "@type": "ontolex:Lexicon", 
          "label": "Example wordnet (English)",
          "language": "en",
          "email": "john@mccr.ae",
          "rights": "https://creativecommons.org/publicdomain/zero/1.0/",
          "version": "1.0",

In addition the properties `citation`, `url`, `status`, `confidenceScore` and any 
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

The Sense requires only an `@id` and a `synset` and may take `status`, 
`confidenceScore`, Dublin Core properties, an `example`.


              "sense": [{
                  "@id": "example-en-10161911-n-1",
                  "synset": "example-en-10161911-n"
              }]
          }, {
              "@id" : "w2",
              "lemma": { "writtenForm": "paternal grandfather" }, 
              "partOfSpeech": "noun",
              "sense": [{
                  "@id": "example-en-1-n-1",
                  "synset": "example-en-1-n",

A sense may also have any number of `relations` which have a `relType` from the
list below and a `target` and may have Dublin Core properties

* `antonym`: An opposite and inherently incompatible word
* `also`: See also, a reference of weak meaning
* `verb_group`: Verb senses that similar in meaning and have been manually grouped together.
* `participle`: An adjective that is a participle form a verb
* `pertainym`: A relational adjective. Adjectives that are pertainyms are usually defined by such phrases as "of or pertaining to" and do not have antonyms. A pertainym can point to a noun or another pertainym
* `derivation`: A word that is derived from some other word
* `domain_category`: Indicates the category of this word
* `domain_member_category`: Indicates a word involved in this category described by this word
* `domain_region`: Indicates the region of this word
* `domain_member_region`: Indicates a word involved in the region described by this word
* `exemplifies`: Indicates the usage of this word
* `domain_member_usage`: Indicates a word involved in the usage described by this word

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
                 {"label": "Sam cannot %s Sue"}, 
                 {"label": "Sam and Sue %s"},
                 {"label": "The banks %s the check"}
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
* `verb_group`: Verb senses that similar in meaning and have been manually grouped together.
* `domain_category`: Indicates the category of this word
* `domain_member_category`: Indicates a word involved in this category described by this word
* `domain_region`: Indicates the region of this word
* `domain_member_region`: Indicates a word involved in the region described by this word
* `exemplifies`: Indicates the usage of this word
* `domain_member_usage`: Indicates a word involved in the usage described by this word

              "relations": [{
                  "relType": "hypernym", "target": "example-en-10162692-n"
              }]
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
          "@type": "ontolex:Lexicon", 
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
                  "synset": "example-en-1-n",
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

The RDF schema is significantly more flexible and builds principally on the 
[W3C OntoLex Model](http://cimiano.github.io/ontolex/specification.html). The 
details of the RDF serialization are principally built on those of the JSON-LD
model. We include a separate tutorial here for the benefit of those who wish
to create their resource natively in RDF.

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
    @prefix wn: <http://wordnet-rdf.princeton.edu/ontology#> .
    @prefix wordnetlicense: <http://wordnet.princeton.edu/wordnet/license/> .

Each wordnet is an instance of the class `ontolex:Lexicon` and must have the
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
* Synsets are `ontolex:LexicalConept`.
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
    
    [] a ontolex:Sense ;
      vartrans:source <#example-en-1-n-1> ;
      vartrans:category wn:derivation ;
      vartrans:target <#example-en-10161911-n-1> ;
      dc:creator "John McCrae"@en .
              
    <#w3> a ontolex:LexicalEntry ;
      ontolex:canonicalForm [
        ontolex:writtenRep "pay"@en
      ] ;
      wn:partOfSpeech wn:verb ;
      synsem:synBehavior [
        rdfs:label "Sam cannot %s Sue" @en
      ], [
        rdfs:label "Sam and Sue %s"@en
      ], [
        rdfs:label "The banks %s the check"@en
      ] .
    
    <#example-en-10161911-n> a ontolex:LexicalConcept ;
      wn:partOfSpeech wn:noun ;
      skos:inScheme <#example-en> ;
      wn:ili ili:i90287 ;
      wn:definition [
        rdf:value "the father of your father or mother"@en
      ] .
    
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
