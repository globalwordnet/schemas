Global WordNet Schemas 
======================

Read the documentation [here](https://globalwordnet.github.io/schemas)


Building the metadata
---------------------

`index.html` is constructed with PanDoc

    pandoc -t html -H template/header -A template/afterbody -B template/beforebody --shift-heading-level-by=-1 index.md > index.html

`wn.rdf` is generated from the Turtle with Rapper

    rapper -i turtle -o rdfxml-abbrev wn-lemon-$VERSION.ttl > wn.rdf
    rapper -i turtle -o rdfxml-abbrev wn-simple-$VERSION.ttl > wn-simple.rdf
    rapper -i turtle -o rdfxml-abbrev nomlex-$VERSION.ttl > nomlex.rdf

