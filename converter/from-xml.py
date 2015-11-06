import sys
import xml.sax
import json

class WNLMFHandler(xml.sax.handler.ContentHandler):
    parent = []

    root = []
    lexicon = {}
    entry = {}
    entries = {}
    sense = {}
    synset = {}
    senses_by_synset = {}


    def map_pos(self, pos):
        if pos == "n":
            return "wn:noun"
        if pos == "v":
            return "wn:verb"
        if pos == "a":
            return "wn:adjective"
        if pos == "r":
            return "wn:adverb"
        if pos == "s":
            return "wn:adjective_satellite"
        if pos == "p":
            return "wn:phrase"
        if pos == "u":
            return "wn:unknown"


    def startElement(self, name, attrs):
        if name == "LexicalResource":
            assert(len(self.parent) == 0)
            self.lexicon = {}
            self.root.append(self.lexicon)
        elif name == "Lexicon":
            assert(self.parent[-1] == "LexicalResource" or len(self.parent) == 0)
            self.lexicon["language"] = attrs["language"]
            if "label" in attrs:
                self.lexicon["label"] = attrs["label"]
            if "id" in attrs:
                self.lexicon["@id"] = attrs["id"]
            self.lexicon["synsets"] = []
        elif name == "LexicalEntry":
            assert(self.parent[-1] == "Lexicon")
            self.entry = {}
            if "id" in attrs:
                self.entry["@id"] = attrs["id"]
        elif name == "Lemma":
            assert(self.parent[-1] == "LexicalEntry")
            self.entry["lemma"] = attrs["writtenForm"]
            self.entry["partOfSpeech"] = self.map_pos(attrs["partOfSpeech"])
        elif name == "Sense":
            assert(self.parent[-1] == "LexicalEntry")
            self.sense = {}
            self.sense["@id"] = attrs["id"]
            self.sense["entry"] = self.entry
            if attrs["synset"] not in self.senses_by_synset:
                self.senses_by_synset[attrs["synset"]] = []
            self.senses_by_synset[attrs["synset"]].append(self.sense)
        elif name == "Synset":
            assert(self.parent[-1] == "Lexicon")
            self.synset = {}
            self.synset["@id"] = attrs["id"]
            self.synset["iliRef"] = "ili:" + attrs["ili"]
            self.synset["senses"] = []
            for sense in self.senses_by_synset[attrs["id"]]:
                self.synset["senses"].append(sense)
            self.lexicon["synsets"].append(self.synset)
        elif name == "Definition":
            assert(self.parent[-1] == "Synset")
            self.synset["definition"] = attrs["gloss"]
            self.synset["iliDef"] = attrs["iliDef"]
        elif name == "Statement":
            assert(self.parent[-1] == "Definition")
            if "examples" not in self.synset:
                self.synset["examples"] = []
            self.synset["examples"].append(attrs["example"])
        elif name == "SynsetRelation":
            assert(self.parent[-1] == "Synset")
            if attrs["relType"] not in self.synset:
                self.synset[attrs["relType"]] = []
            self.synset[attrs["relType"]].append(attrs["target"])
        elif name == "SenseRelation":
            assert(self.parent[-1] == "Sense")
            if attrs["relType"] not in self.sense:
                self.sense[attrs["relType"]] = []
            self.sense[attrs["relType"]].append(attrs["target"])
        elif name == "SyntacticBehaviour":
            assert(self.parent[-1] == "LexicalEntry")
            if "syntacticBehaviour" not in self.entry:
                self.entry["syntacticBehaviour"] = []
            self.entry["syntacticBehaviour"].append(attrs["subcategorizationFrame"])
        elif name == "Meta":
            if self.parent[-1] == "Lexicon":
                doMeta(name, attrs, self.lexicon)
            elif self.parent[-1]  == "LexicalEntry":
                doMeta(name, attrs, self.entry)
            elif self.parent[-1] == "Sense":
                doMeta(name, attrs, self.sense)
            elif self.parent[-1] == "Synset":
                doMeta(name, attrs, self.synset)
            else:
                assert(False)
        else:
            assert(False)

        self.parent.append(name)

    def endElement(self, name):
        self.parent.pop()

if __name__ == "__main__":
    parser = xml.sax.make_parser()
    handler = WNLMFHandler()
    parser.setContentHandler(handler)
    parser.parse(open(sys.argv[1],"r"))
    print(json.dumps(handler.root))
