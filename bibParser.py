# parse bib file
# compare references and merges list

import bibtexparser
from references import *

def ImportBib(file):
    with open(file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
        references=[]
        for r in bib_database.entries :
            ref=Reference()
            ref.create_Ref(r)
            references.append(ref)
    return references