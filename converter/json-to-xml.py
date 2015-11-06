import sys
import json
import re
from lxml.etree import Element, SubElement, tostring

# Variables related to warnings
warnings = 0
errors = 0

# Format dependent constants
xmlid_regex = re.compile(r'^([a-zA-Z_][\w.-]*|)$')
meta_keys = ["contributor", "coverage", "creator", "date", "description", 
             "format", "identifier", "language", "publisher", "relation", 
             "rights", "source", "subject", "title", "type", "status", 
             "confidenceScore"]
language_regex = re.compile("^(((en-GB-oed|i-ami|i-bnn|i-default|i-enochian|i-hak|i-klingon|i-lux|i-mingo|i-navajo|i-pwn|i-tao|i-tay|i-tsu|sgn-BE-FR|sgn-BE-NL|sgn-CH-DE)|(art-lojban|cel-gaulish|no-bok|no-nyn|zh-guoyu|zh-hakka|zh-min|zh-min-nan|zh-xiang))|((([A-Za-z]{2,3}(-([A-Za-z]{3}(-[A-Za-z]{3}){0,2}))?)|[A-Za-z]{4}|[A-Za-z]{5,8})(-([A-Za-z]{4}))?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-([0-9A-WY-Za-wy-z](-[A-Za-z0-9]{2,8})+))*(-((-[A-Za-z0-9]{1,8})+))?)|(x(-[A-Za-z0-9]{1,8})+))$")
url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
declared_prefixes = {
    "wn": "http://wordnet-rdf.princeton.edu/ontology#",
    "lemon": "http://lemon-model.net/lemon#",
    "dc": "http://purl.org/dc/terms/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "wordnetlicense": "http://wordnet.princeton.edu/wordnet/license/",
    "cc": "http://creativecommons.org/ns#",
    "ili": "http://ili.globalwordnet.org/ili/"}
schema_uri = "http://globalwordnet.github.io/schemas/wn-json-context.json"
parts_of_speech = {"wn:noun": "n", "wn:verb": "v", "wn:adjective": "a", "wn:adverb": "r",
        "wn:adjective_satellite": "s", "wn:phrase": "p", "wn:unknown": "u"}
sense_relations = ["antonym", "also", "verb_group", "participle", "pertainym", 
    "derivation", "domain_category", "domain_member_category", "domain_region",
    "domain_member_region", "domain_usage", "domain_member_usage"]
synset_relations = ["hypernym", "hyponym", "instance_hypernym",
    "instance_hyponym", "part_holonym", "part_meronym", "member_holonym",
    "member_meronym", "substance_holonym", "substance_meronym", "entail", 
    "cause", "similar", "also", "attribute", "verb_group", "domain_category",
    "domain_member_category", "domain_region", "domain_member_region",
    "domain_usage", "domain_member_usage", "action", "theme", "product",
    "location", "agent", "instrument", "result", "patient", "beneficiary",
    "creator", "goal", "experiencer"]
ili_code = re.compile(r'^ili:i\d+$')

# Status
default_language = "unk"

def warn(reason):
    global warnings
    warnings += 1
    print("[WARNING] " + reason)

def fail(reason):
    global errors
    errors += 1
    print("[ERROR  ] " + reason)

def convert_language(language):
    if type(language) is str or type(language) is unicode:
        if not re.match(language_regex, language):
            fail("Bad language code")
    else:
        fail("Language code must be a string")

def convert_context_decl(elem):
    # From http://stackoverflow.com/questions/7035825/regular-expression-for-a-language-tag-as-defined-by-bcp47
    if type(elem) is dict:
        if "@language" not in elem:
            fail("No language in context declaration")
        for key in elem:
            if key == "@language":
                convert_language(elem[key])
                default_language = elem[key]
            elif type(elem[key]) is str or type(elem[key]) is unicode and ":" not in key:
                declared_prefixes[key] = elem[key]
            else:
                fail("Bad declaration: " + str(elem[key]))
    else:
        fail("Not a context declaration: " + str(elem))

def convert_context(context):
    if type(context) is list:
        if schema_uri not in context:
            fail("WN-JSON Schema URI is missing")
        for elem in context:
            if elem == schema_uri:
                pass
            else:
                convert_context_decl(elem)
    else:
        fail("@context should be a list")

def convert_id(identifier):
    if type(identifier) is str or type(identifier) is unicode:
        s = identifier.split(":")
        if re.match(url_regex, identifier):
            return identifier
        elif len(s) == 2 and s[0] in declared_prefixes and re.match(xmlid_regex, s[1]):
            return declared_prefixes[s[0]] + s[1]
        elif re.match(xmlid_regex, identifier):
            return identifier
        else:
            fail("Invalid id: %s" % identifier)
            return "##INVALID##"
    else:
        fail("Identifier is not string")
        return "##NOT A STRING##"

def convert_label(label):
    if type(label) is str or type(label) is unicode:
        pass
    else:
        fail("Label must be a string")

def convert_meta(key, meta, xml):
    if key == "rights":
        xml.attrib["rights"] = convert_id(meta)
    elif type(meta) is str or type(meta) is unicode:
        xml.attrib[key] = meta
    else:
        fail("Meta valua should be a string")

def convert_lemma(lemma, xml):
    if type(lemma) is dict:
        if "writtenForm" not in lemma:
            fail("Lemma must have a written form")
        for key in lemma:
            if key == "writtenForm":
                if type(lemma[key]) is str or type(lemma[key]) is unicode:
                    xml.attrib["writtenForm"] = lemma[key]
                else:
                    fail("writtenForm is not a string: %s" % str(lemma[key]))
            else:
                warn("Non-standard key ignored: %s" % key)
    else:
        fail("Lemma is not an object")

def convert_partOfSpeech(partOfSpeech):
    if type(partOfSpeech) is str or type(partOfSpeech) is unicode:
        if str(partOfSpeech) not in parts_of_speech:
            fail("Invalid POS: %s" % partOfSpeech)
            return "u"
        else:
            return parts_of_speech[partOfSpeech]
    else:
        fail("Part of speech is not a string")
        return "u"

def convert_synset_relation(relation, target, xml):
    if type(target) is list:
        for t in target:
            sr_xml = Element("SynsetRelation")
            xml.append(sr_xml)
            sr_xml.attrib["target"] = convert_id(t)
            sr_xml.attrib["relType"] = relation
            convert_id(t)
    else:
        sr_xml = Element("SynsetRelation")
        xml.append(sr_xml)
        sr_xml.attrib["target"] = convert_id(target)
        sr_xml.attrib["relType"] = relation
        convert_id(t)

def convert_sense_relation(relation, target, xml):
    if type(target) is list:
        for t in target:
            sr_xml = Element("SenseRelation")
            xml.append(sr_xml)
            sr_xml.attrib["target"] = convert_id(t)
            sr_xml.attrib["relType"] = relation
            convert_id(t)
    else:
        sr_xml = Element("SenseRelation")
        xml.append(sr_xml)
        sr_xml.attrib["target"] = convert_id(target)
        sr_xml.attrib["relType"] = relation
        convert_id(target)

def convert_ili_ref(ref):
    if type(ref) is str or type(ref) is unicode:
        if not re.match(ili_code, ref):
            fail("ILI References not of correct form")
            return "##ERROR##"
        else:
            return ref[4:]
    else:
        fail("ILI Reference must be a string")

def convert_ili_def(defn):
    if type(defn) is str or type(defn) is unicode:
        pass
    else:
        fail("ILI Definition must be a string")

def convert_gloss(defn):
    if type(defn) is str or type(defn) is unicode:
        pass
    else:
        fail("Gloss must be string (in WordNet language)")

def convert_example(example, xml):
    if type(example) is str or type(example) is unicode:
        xml.attrib["example"] = example
    else:
        fail("Example must literal or list of literals")

def convert_examples(examples, xml):
    if type(examples) is list:
        for example in examples:
            example_xml = Element("Statement")
            xml.append(example_xml)
            convert_example(example, example_xml)
    else:
        example_xml = Element("Statement")
        xml.append(example_xml)
        convert_example(examples, example_xml)

def convert_definition(definition, xml):
    defn_xml = Element("Definition")
    xml.append(defn_xml)
    if type(definition) is dict:
        if "iliDef" not in definition:
            fail("Definition requires an ILI Def")
        elif "gloss" not in definition:
            fail("Definition requiers a gloss")
        for key in definition:
            if key == "@id":
                warn("Definition ID is unnecessary")
                convert_id(definition[key])
            elif key == "iliDef":
                convert_ili_def(definition[key])
                defn_xml.attrib["iliDef"] = definition[key]
            elif key == "gloss":
                convert_gloss(definition[key])
                defn_xml.attrib["gloss"] = definition[key]
            elif key == "examples":
                convert_examples(definition[key], defn_xml)
            else:
                warn("Non-standard key ignored: %s" % key)
    else:
        fail("Definition should be an object")

def convert_synset(synset, xml):
    synset_xml = Element("Synset")
    xml.append(synset_xml)
    meta = None
    if type(synset) is dict:
        if "@id" not in synset:
            fail("Synset identifier is requied")
        if "iliRef" not in synset:
            fail("Synset does not have reference to ILI")
        for key in synset:
            if key == "@id":
                synset_xml.attrib["id"] = synset[key]
                convert_id(synset[key])
            elif key == "iliRef":
                synset_xml.attrib["ili"] = convert_ili_ref(synset[key])
            elif key == "definition":
                convert_definition(synset[key], synset_xml)
            elif key in synset_relations:
                convert_synset_relation(key, synset[key], synset_xml)
            elif key in meta_keys:
                if meta is None:
                    meta = Element("Meta")
                    synset_xml.append(meta)
                convert_meta(key, synset[key], meta)
            else:
                warn("Non-standard key ignored: %s" % key)
    else:
        fail("Synset must be single object")

def convert_sense(sense, xml, lexicon_xml):
    if type(sense) is dict:
        if "@id" not in sense:
            fail("Sense id is required")
        if "synset" not in sense:
            fail("Synset is required for sense")
        for key in sense:
            if key == "@id":
                xml.attrib["id"] = sense[key]
                convert_id(sense[key])
            elif key == "synset":
                xml.attrib["synset"] = sense[key]["@id"]
                convert_synset(sense[key], lexicon_xml)
            elif key in meta_keys:
                convert_meta(key, sense[key], None)
            elif key in sense_relations:
                convert_sense_relation(key, sense[key], xml)
            else:
                warn("Non-standard key ignored: %s" % key)
    else:
        fail("Sense is not an object")

def convert_senses(senses, entry_xml, lexicon_xml):
    if type(senses) is list:
        for sense in senses:
            sense_xml = Element("Sense")
            entry_xml.append(sense_xml)
            convert_sense(sense, sense_xml, lexicon_xml)
    else:
        convert_sense(senses, sense_xml, lexicon_xml)

def convert_subcat(frame, xml):
    if type(frame) is dict:
        if "label" in frame:
            sb_xml = Element("SyntacticBehaviour")
            xml.append(sb_xml)
            sb_xml.attrib["subcategorizationFrame"] = str(frame)
        else:
            fail("Subcategorization Frame does not have label")
        for key in frame:
            if key == "@id":
                warn("Subcategorization frames do not need an ID")
            elif key == "label":
                pass
            else:
                warn("Non-standard key ignored: %s" % key)
    else:
        fail("Subcategorization Frame must be a structure")

def convert_syntacticBehavior(frames, xml):
    if type(frames) is list:
        for frame in frames:
            convert_subcat(frame, xml)
    else:
        convert_subcat(frames, xml)
        
def convert_entry(entry, xml, lexicon_xml):
    lemma_xml = Element("Lemma")
    xml.append(lemma_xml)
    meta = None
    if type(entry) is dict:
        if "lemma" not in entry:
            fail("Entry must have a lemma")
        if "@id" not in entry:
            fail("Entry must have an @id")
        for key in entry:
            if key == "@id":
                xml.attrib["id"] = entry[key]
                convert_id(entry[key])
            elif key == "lemma":
                convert_lemma(entry[key], lemma_xml)
            elif key == "partOfSpeech":
                lemma_xml.attrib["partOfSpeech"] = convert_partOfSpeech(entry[key])
            elif key == "sense":
                convert_senses(entry[key], xml, lexicon_xml)
            elif key == "syntacticBehavior":
                convert_syntacticBehavior(entry[key], xml)
            elif key in meta_keys:
                if meta is None:
                    meta = Element("Meta")
                    xml.append(meta)
                convert_meta(key, entry[key], meta)
            else:
                fail("Unexpected key: %s" % key)
    else:
        fail("Entry is not an object")

def convert_entries(entries, xml):
    if type(entries) is list:
        for entry in entries:
            entry_xml = Element("LexicalEntry")
            xml.append(entry_xml)
            convert_entry(entry, entry_xml, xml)
    else:
        entry_xml = Element("LexicalEntry")
        xml.append(entry_xml)
        convert_entry(entries, entry_xml, xml)

def convert_root(root, xml):
    if type(root) is dict:
        lexicon = Element("Lexicon")
        xml.append(lexicon)
        meta = None
        if "language" not in root:
            fail("Language is required")
        if "@type" not in root:
            fail("Type is requied")
        if "@context" not in root:
            fail("Context is required")
        else:
            convert_context(root["@context"])
        for key in root:
            if key == "@context":
                pass
            elif key == "@id":
                convert_id(root[key])
                lexicon.attrib["id"] = root[key]
            elif key == "@type":
                if root[key] != "lemon:Lexicon":
                    fail("Root must be a single lexicon")
            elif key == "label":
                convert_label(root[key])
                lexicon.attrib["label"] = root[key]
            elif key in meta_keys:
                if meta is None:
                    meta = Element("Meta")
                    lexicon.append(meta)
                convert_meta(key, root[key], meta)
            elif key == "entry":
                convert_entries(root[key], lexicon)
            else:
                fail("%s is not an expected key" % key)
    elif type(root) is list:
        for lexicon in root:
            convert_root(lexicon, xml)
    else:
        fail("Root must be a single JSON Object or List")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        source = sys.stdin
    else:
        source = open(sys.argv[1])
    root = Element("LexicalResource")
    convert_root(json.load(source), root)
    print("%d Errors and %d Warnings" % (errors, warnings))
    print(tostring(root, pretty_print=True))
