import fitz  # this is pymupdf
import os
import subprocess
import re

def find_references_in_text(input_filename:str, output_filename:str):
    with open(input_filename, "r") as input_file:
        text=input_file.read()
        refNumber="references( )*(\n)*\[([0-9])*]"
        ref = re.split(refNumber,text, flags=re.IGNORECASE)[-1]
        ref="[1]"+ref
        with open(output_filename, "w",encoding='utf-8') as output_file:
            for r in ref.split('['):
                r=r.replace('\n',' ')
                r=r.split(']')
                if len(r) > 1:
                    r=r[1]
                    r=r[1:]+"\n"
                    output_file.write(r)
    


def ExtractTextFromPDF(filename,path):
    with fitz.open(path+filename) as doc:
        text = ""
        for page in doc:
            text += page.getText()
    with open(path+"/temp.txt", 'w', encoding='utf-8') as of:
        of.write(text)
        
def CorrectEncodeSave(text,filename):
    with open(filename,'w', encoding='utf-8') as of:
        references=text.split("REFERENCES")[1]
        for r in references.split('['):
            r=r.replace('\n',' ')
            r=r.split(']')
            if len(r) > 1:
                r=r[1]
                r=r[1:]+"\n"
                of.write(r)
    

def ExtractReferencesFromPDF(filename:str,round:int):
    if ".pdf" not in filename:
        print("error not a pdf file, exit")
        exit
    else :
        fname=filename.strip().split(".")[0]+"-temp.txt"
        find_references_in_text("temp.txt",fname)
        val=os.system("anystyle -f bib parse "+fname+ " bib_round_"+str(round))
        if val != 0:
            print("ERROR WHILE PARSING REFERENCES")
            print(val)
            exit(1)
        os.remove(fname)
        os.remove("temp.txt")

