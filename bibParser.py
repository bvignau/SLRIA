# parse bib file
# compare references and merges list

import bibtexparser
from references import *

def ImportBib(file,slr_round):
    with open(file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
        references=[]
        for r in bib_database.entries :
            ref=Reference()
            ref.create_Ref(r,slr_round)
            references.append(ref)
    return references