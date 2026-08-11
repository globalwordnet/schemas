#!/bin/sh

pandoc index.md -s --metadata title="Global WordNet Formats" --highlight-style=pygments -c https://cdn.jsdelivr.net/npm/water.css@2/out/light.css -o index.html --syntax-definition=sparql.xml 
