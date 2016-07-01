#!/bin/bash

die() { echo "$@" 1>&2 ; exit 1; }

xmllint --dtdvalid WN-LMF.dtd example.xml >/dev/null || die "XML not working"
python wn-json-validate.py example.json || die "JSON not working"
rapper -i turtle example.ttl >/dev/null || die "RDF not working"
rapper -i turtle wn.ttl > wn.rdf || die "Ontology not valid"

