from pdfToBib import ExtractReferencesFromPDF
from references import *
from bibParser import *
def main():
    file_test='bib/pal2012-temp.bib'
    ExtractReferencesFromPDF("pal2012.pdf")
    t1=ImportBib(file_test)
    t2=ImportBib(file_test)
    tf=MergeList(t1,t2,50)
    printList(tf)
    genBib(tf,"final.bib")
    

if __name__ == "__main__":
    main()