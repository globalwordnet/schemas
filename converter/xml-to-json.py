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
    CONTEXT = [ "http://globalwordnet.github.io/schemas/wn-json-context.json" ]


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


    def doMeta(self, name, attrs, target):
        for meta_prop in attrs.keys():
            target[meta_prop] = attrs[meta_prop]



    def startElement(self, name, attrs):
        if name == "LexicalResource":
            assert(len(self.parent) == 0)
            self.lexicon = { "@context": self.CONTEXT }
            self.root.append(self.lexicon)
        elif name == "Lexicon":
            assert(self.parent[-1] == "LexicalResource" or len(self.parent) == 0)
            self.lexicon["language"] = attrs["language"]
            if "label" in attrs:
                self.lexicon["label"] = attrs["label"]
            if "id" in attrs:
                self.lexicon["@id"] = attrs["id"]
            self.lexicon["@type"] = "lemon:Lexicon"
            self.lexicon["entry"] = []
        elif name == "LexicalEntry":
            assert(self.parent[-1] == "Lexicon")
            self.entry = {}
            if "id" in attrs:
                self.entry["@id"] = attrs["id"]
            self.lexicon["entry"].append(self.entry)
            self.entry["sense"] = []
        elif name == "Lemma":
            assert(self.parent[-1] == "LexicalEntry")
            self.entry["lemma"] = { "writtenForm": attrs["writtenForm"] }
            self.entry["partOfSpeech"] = self.map_pos(attrs["partOfSpeech"])
        elif name == "Sense":
            assert(self.parent[-1] == "LexicalEntry")
            self.sense = {}
            self.sense["@id"] = attrs["id"]
            if attrs["synset"] not in self.senses_by_synset:
                self.senses_by_synset[attrs["synset"]] = []
            self.entry["sense"].append(self.sense)
            self.senses_by_synset[attrs["synset"]].append(self.sense)
        elif name == "Synset":
            assert(self.parent[-1] == "Lexicon")
            self.synset = {}
            self.synset["@id"] = attrs["id"]
            self.synset["iliRef"] = "ili:" + attrs["ili"]
            head = True
            for sense in self.senses_by_synset[attrs["id"]]:
                if head:
                    sense["synset"] = self.synset
                    head = False
                else:
                    sense["synset"] = {"@id": attrs["id"]}
        elif name == "Definition":
            assert(self.parent[-1] == "Synset")
            self.synset["definition"] = {
                    "gloss": attrs["gloss"],
                    "iliDef": attrs["iliDef"]
                    }
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
                self.doMeta(name, attrs, self.lexicon)
            elif self.parent[-1]  == "LexicalEntry":
                self.doMeta(name, attrs, self.entry)
            elif self.parent[-1] == "Sense":
                self.doMeta(name, attrs, self.sense)
            elif self.parent[-1] == "Synset":
                self.doMeta(name, attrs, self.synset)
            elif self.parent[-1] == "Definition":
                self.doMeta(name, attrs, self.synset)
            else:
                assert(False)
        else:
            print(name)
            assert(False)

        self.parent.append(name)

    def endElement(self, name):
        self.parent.pop()

if __name__ == "__main__":
    parser = xml.sax.make_parser()
    handler = WNLMFHandler()
    parser.setContentHandler(handler)
    if len(sys.argv) >= 2:
        parser.parse(open(sys.argv[1],"r"))
    else:
        parser.parse(sys.stdin)
    if len(handler.root) > 1:
        print(json.dumps(handler.root, indent=4))
    else:
        print(json.dumps(handler.root[0], indent=4))
