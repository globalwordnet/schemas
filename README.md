Global WordNet Schemas 
======================

Read the documentation [here](https://globalwordnet.github.io/schemas)


Building the metadata
---------------------

`index.html` is constructed with PanDoc

    pandoc -t html -H template/header -A template/afterbody -B template/beforebody --metadata title="GlobalWordNet Schemas" index.md > index.html

`wn.rdf` is generated from the Turtle with Rapper

    rapper -i turtle -o rdfxml-abbrev wn.ttl > wn.rdf

