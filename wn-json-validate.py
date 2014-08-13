import sys
import json
import jsonschema
from jsonschema.exceptions import ValidationError

if __name__ == "__main__":
    if len(sys.argv) < 2:
        source = sys.stdin
    else:
        source = open(sys.argv[1])
    try:
        jsonschema.validate(json.load(source),json.load(open("wn-json-schema.json")))
        print("Valid")
    except ValidationError as e:
        print(e.message)
        for error in e.context:
            print(error)
            print()
        sys.exit(-1)

    

