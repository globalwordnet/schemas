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
* z: Multiword expression (inc. phrase, idiom)
* c: Conjunction
* p: Adposition (Preposition, postposition, etc.)
* x: Other (inc. particle, classifier, bound morphemes, determiners)
* u: Unknown

                <Lemma writtenForm="grandfather" partOfSpeech="n"/>
                <Sense id="example-10161911-n-1" synset="example-10161911-n"/>
            </LexicalEntry>
            <LexicalEntry id="w2">
                <Lemma writtenForm="paternal grandfather" partOfSpeech="n"/>
                <Sense id="example-1-n-1" synset="example-1-n">

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
* domain_usage: Indicates the usage of this word
* domain_member_usage: Indicates a word involved in the usage described by this word

                    <SenseRelation relType="derivation" target="example-10161911-n-1"/>
                </Sense>
            </LexicalEntry>
            <LexicalEntry id="w3">
                <Lemma writtenForm="pay" partOfSpeech="v"/>
                
Syntactic Behaviour is given as in Princeton WordNet

                <SyntacticBehaviour subcategorizationFrame="Sam cannot %s Sue "/>
                <SyntacticBehaviour subcategorizationFrame="Sam and Sue %s"/>
                <SyntacticBehaviour subcategorizationFrame="The banks %s the check"/>
            </LexicalEntry>

If a synset is already mapped to the ILI please give the ID here

            <Synset id="example-10161911-n" ili="i90287">
                <Definition>
                    the father of your father or mother
                </Definition>
The set of relations between synsets is limited to the following:

* hypernym: A concept with a broader meaning
* hyponym: A concept with a narrower meaning
* instance_hypernym: The class of objects to which this instance belongs
* instance_hyponym: An individual instance of this class
* part_holonym: A larger whole that this concept is part of
* part_meronym: A part of this concept
* member_holonym: A group that this concept is a member of
* member_meronym: A member of this concept
* substance_holonym: Something where a constituent material is this concept
* substance_meronym: A constituent material of this concept
* entail: A verb X entails Y if X cannot be done unless Y is, or has been, done.
* cause: A verb that causes another
* similar: Similar, though not necessarily interchangeable
* also: See also, a reference of weak meaning
* attribute: A noun for which adjectives express values. The noun weight is an attribute, for which the adjectives light and heavy express values.
* verb_group: Verb senses that similar in meaning and have been manually grouped together.
* domain_category: Indicates the category of this word
* domain_member_category: Indicates a word involved in this category described by this word
* domain_region: Indicates the region of this word
* domain_member_region: Indicates a word involved in the region described by this word
* domain_usage: Indicates the usage of this word
* domain_member_usage: Indicates a word involved in the usage described by this word

                <SynsetRelation relType="hypernym" target="example-10162692-n"/>
            </Synset>

If you wish to define a new concept call the concept "in" (ILI New). If there is
no mapping to the ILI leave this field empty (it is required).

            <Synset id="example-1-n" ili="in">
                <Definition>A father's father; a paternal grandfather</Definition>

You can include metadata (such as source) at many points
The ILI Definition must be at least 20 characters or five words

                <ILIDefinition dc:source="https://en.wiktionary.org/wiki/farfar">
                    A father's father; a paternal grandfather
                </ILIDefinition>
            </Synset>

You must include all targets of relations

            <Synset id="example-10162692-n" ili="i90292"/>
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

                <Sense id="example-2-n-1" synset="example-1-n">
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
[ `wn:noun`, `wn:verb`, `wn:adjective`, `wn:adverb`, `wn:adjective_satellite`, `wn:phrase`, `wn:conjunction`, `wn:adposition`, `wn:other`, `wn:unknown` ]. The `@id` must be unique in the
document, it is not the same as the `@id` of the wordnet or any other entry.

          "entry": [{
              "@id" : "w1",
              "lemma": { "writtenForm": "father" }, 
              "partOfSpeech": "wn:noun",

The Sense requires only an `@id` and a `synset` and may take `status`, 
`confidenceScore`, Dublin Core properties, an `example` and any number of 
sense relations as follows:

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
* `domain_usage`: Indicates the usage of this word
* `domain_member_usage`: Indicates a word involved in the usage described by this word

              "sense": [{
                  "@id": "example-10161911-n-1",

A synset requires only an `@id`. It may take an `ili` which is a code from the 
CILI (starting with `ili:i`), a `definition`, an `iliDefinition` (which must 
be given in English), `status`, `confidenceScore`, Dublin Core properties and
any relations from the following list:

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
* `domain_usage`: Indicates the usage of this word
* `domain_member_usage`: Indicates a word involved in the usage described by this word

In contrast to the XML form the `ili` is optional. If there is no match omit this
tag, if you wish to propose a new synset add only a `iliDefinition`.

                   "synset": {
                      "@id": "example-10161911-n",
                      "ili": "ili:i90287",

Definitions must have a `gloss` and may be have a `language`, in addition, 
`status`, `confidenceScore` and Dublin Core properties may be added. An 
`iliDefinition` is the same but may not have a language.

                      "definition": {
                          "gloss": "that which is perceived or known or inferred to have its own distinct existence (living or nonliving)"
                      },

Relations (on senses or synsets) are given as an array of references to `@id` 
values (these must correspond to elements at the same level with that `@id`).

                      "hyponym": ["example-10162692-n"]
                  }
              }]
          }, {
              "@id" : "w2",
              "lemma": { "writtenForm": "paternal grandfather" }, 
              "partOfSpeech": "wn:noun",
              "sense": [{
                  "@id": "example-1-n-1",
                  "synset": {
                      "@id": "example-1-n",
                      "definition": {
                          "gloss": "the father of your father or mother"
                      },
                      "iliDefinition": {
                          "gloss": "the father of your father or mother",
                          "source": "https://en.wiktionary.org/wiki/farfar"
                      },
                      "hypernym": ["example-10162692-n"]
                  },

Relations may also be stated in full form, in which case the `status`, 
`confidenceScore` and Dublin Core properties may be stated.

                  "relations": [
                    {
                      "category": "wn:derivation",
                      "target": "example-10161911-n",
                      "creator": "John McCrae"
                    }
                  ]
              }]
          }, {
              "@id": "w3",
              "lemma": { "writtenForm": "pay" },
              "partOfSpeech": "wn:verb",

The syntactic behavior is given here as follows:

              "synBehavior": [{
                 {"label": "Sam cannot %s Sue"}, 
                 {"label": "Sam and Sue %s"},
                 {"label": "The banks %s the check"}
              }]
          }]
      }, {
          "@context": { "@language": "sv" },
          "@id": "example-sv",
          "@type": "ontolex:Lexicon", 
          "label": "Example wordnet (Swedish)",
          "language": "sv",
          "email": "john@mccr.ae",
          "rights": "https://creativecommons.org/publicdomain/zero/1.0/",
          "version": "1.0",
          "citation": "CILI: the Collaborative Interlingual Index. Francis Bond, Piek Vossen, John P. McCrae and Christiane Fellbaum, Proceedings of the Global WordNet Conference 2016, (2016).",
          "url": "http://globalwordnet.github.io/schemas",
          "publisher": "Global Wordnet Association",
          "entry": [{
              "@id" : "w4",
              "lemma": { "writtenForm": "farfar" }, 
              "partOfSpeech": "wn:noun",
              "sense": [{
                  "@id": "example-2-n-1",
                  "synset": "example-1-n",

Any examples should be given on the sense as follows:

                  "example": {
                      "value": "Jag vill berätta för er att min farfar var svensk beredskapssoldat vid norska gränsen under andra världskriget, ett krig som Sverige stod utanför",
                      "source": "Europarl Corpus"
                  }
              }]
          }]
      }]
    }

In addition, the JSON format can be validated by the [JSON Schema](http://json-schema.org)
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

    <#example-en> a lemon:Lexicon ;
      rdfs:label "Example wordnet"@en ;
      dc:language "en"@en ;
      schema:email "john@mccr.ae" ;
      dc:rights <https://creativecommons.org/publicdomain/zero/1.0/> ;
      owl:versionInfo "1.0" ;
      schema:citation "CILI: the Collaborative Interlingual Index. Francis Bond, Piek Vossen, John P. McCrae and Christiane Fellbaum, Proceedings of the Global WordNet Conference 2016, (2016)."@en ;
      schema:url <http://globalwordnet.github.io/schemas/> ;
      dc:publisher "Global Wordnet Association"@en ;
      lime:entry <#w1>, <#w2>, <#w3> .
            
    <#w1> a ontolex:LexicalEntry ;
      ontolex:canonicalForm [ ontolex:writtenRep "grandfather"@en ] ;
      wn:partOfSpeech wn:noun ;
      ontolex:sense <#example-10161911-n-1> .
    
    <#example-10161911-n-1> a ontolex:LexicalSense ;
      ontolex:reference <example-10161911-n> .
    
    <#w2> a ontolex:LexicalEntry ;
      ontolex:canonicalForm [ ontolex:writtenRep "paternal grandfather"@en ] ;
      wn:partOfSpeech wn:noun ;
      ontolex:sense <#example-1-n-1> .
    
    <#example-1-n-1> a ontolex:LexicalSense ;
      ontolex:reference <#example-1-n> ;
      wn:derivation <example-10161911-n-1> .
    
    <#w3> a ontolex:LexicalEntry ;
      ontolex:canonicalForm [ ontolex:writtenRep "pay"@en ] ;
    // Be careful with spelling here:
      synsem:synBehavior 
        [ rdfs:label "Sam cannot %s Sue" ] ,
        [ rdfs:label "Sam and Sue %s" ] ,
        [ rdfs:label "The banks %s the check" ] .
    
    <#example-10161911-n> a ontolex:LexicalConcept ;
      owl:sameAs ili:i90287 ;
      // Definitions can also be given directly
      skos:definition "the father of your father or mother"@en ;
      wn:hypernym <#example-10162692-n> .
    
    <#example-1-n> a ontolex:LexicalConcept ;
      skos:definition [
        rdf:value "A father's father; a paternal grandfather"@en ;
      ] ,
      wn:iliDefinition [
        dc:source <https://en.wiktionary.org/wiki/farfar> ;
        rdf:value "A father's father; a paternal grandfather"@ en
      ] .
            
    <#example-10162692-n> owl:sameAs ili:i90292" .
        
    <#example-sv> a ontolex:Lexicon ;
      rdfs:label "Example wordnet (Swedish)"@en ;
      dc:languager "sv" ;
      schema:email "john@mccr.ae" ;
      dc:rights <https://creativecommons.org/publicdomain/zero/1.0/> ;
      owl:versionInfo <1.0> ;
      schema:citation "CILI: the Collaborative Interlingual Index. Francis Bond, Piek Vossen, John P. McCrae and Christiane Fellbaum, Proceedings of the Global WordNet Conference 2016, (2016)."@en ;
      schema:url <http://globalwordnet.github.io/schemas/> ;
      dc:publisher <Global Wordnet Association> ;
      lime:entry <#w4> .
    
    <#w4> a ontolex:LexicalEntry ;
      ontolex:canonicalForm [ ontolex:writtenRep "farfar"@en ] ;
      wn:partOfSpeech wn:noun ;
      ontolex:sense <#example-2-n-1> .
    
    <#example-2-n-1> a ontolex:LexicalSense ;
      ontolex:reference <#example-1-n> ;
      skos:example [
        dc:source "Europarl Corpus"@en ;
        rdf:value "Jag vill berätta för er att min farfar var svensk beredskapssoldat vid norska gränsen under andra världskriget, ett krig som Sverige stod utanför"@sv
      ] .

