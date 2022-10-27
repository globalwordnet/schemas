import gwadoc

elem = ""

for line in open("wn-lemon-1.2.ttl").readlines():
    if line.startswith(":"):
        elem = line.split(" ")[0][1:]
        print(line.rstrip())
    elif "rdfs:comment" in line:
        if elem in gwadoc.relations and "df" in gwadoc.relations[elem]:
            for lang, value in gwadoc.relations[elem].df.items():
                if ";" in line:
                    print("  rdfs:comment \"%s\"@%s ;" % (value.replace("\n","\\n"), lang))
                else:
                    print("  rdfs:comment \"%s\"@%s ." % (value.replace("\n","\\n"), lang))
        else:
            print(line.rstrip())
    else:
        print(line.rstrip())
