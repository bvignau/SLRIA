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
    if os.path.exists(path+filename) :
        with fitz.open(path+filename) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        with open(path+"/text_"+filename+".txt", 'w', encoding='utf-8') as of:
            of.write(text)
    else :
        print("error no file "+path+filename)

        
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
    

def ExtractReferencesFromTxt(filename:str,round:int):
    if ".txt" not in filename:
        print("error not a txt file, exit")
        exit
    else :
        val=os.system("anystyle -f bib parse '"+filename+ "' bib_round_"+str(round))
        if val != 0:
            print("[!] ERROR "+str(val)+" WHILE PARSING REFERENCES OF "+filename)


