Global WordNet Schemas 
======================

Read the documentation [here](https://globalwordnet.github.io/schemas)


Building the metadata
---------------------

`index.html` is constructed with PanDoc

    bash mkindex.sh

`wn.rdf` is generated from the Turtle with Rapper

    rapper -i turtle -o rdfxml-abbrev wn-lemon-$VERSION.ttl > wn.rdf
    rapper -i turtle -o rdfxml-abbrev wn-simple-$VERSION.ttl > wn-simple.rdf
    rapper -i turtle -o rdfxml-abbrev nomlex-$VERSION.ttl > nomlex.rdf

