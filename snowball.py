import os
import bibParser
import references
from  pdfToBib import *

def SnowballExtract(folder_path):
    papers=os.listdir(folder_path)
    for p in papers :
        ld=os.listdir(folder_path+"/"+p)
        pdf=[]
        for f in ld :
            if ".pdf" in f :
                pdf.append(f)
        for doc in pdf : 
            ExtractTextFromPDF(doc, path=folder_path+"/"+p+"/")