import os
from references import *
from  pdfToBib import *
from bibParser import ImportBib
import re

# This function extract the text from all pdf in the folder and subfolder given
# Then it extract the references part. This is done by identifying the IEEE Style "[X] ref". This may not work with other citation style
def SnowballExtract(folder_path:str):
    papers=os.listdir(folder_path)
    for p in papers :
        ld=os.listdir(folder_path+"/"+p)
        pdf=[]
        for f in ld :
            if f.endswith(".pdf"):
                pdf.append(f)
        for doc in pdf : 
            ExtractTextFromPDF(doc, path=folder_path+"/"+p+"/")
            find_references_in_text(input_filename=folder_path+"/"+p+"/text_"+doc+".txt",output_filename=folder_path+"/"+p+"/ref_"+doc+".txt")

# This function transform the extracted section in bibfile that can be used to compare references and merge them
def SnowballDumpReferences(folder_path:str,round:int):
    papers=os.listdir(folder_path)
    for p in papers : 
        listfile= os.listdir(folder_path+"/"+p)
        refFiles=[]
        for f in listfile :
            if "ref_" in f and ".txt" in f and "text_" not in f: 
                refFiles.append(f)
        for rf in refFiles :
            ExtractReferencesFromTxt(filename=folder_path+"/"+p+"/"+rf,round=round)

# Create a list with one list of references for each bib file
def CreateRefLists(bib_folder:str,slr_round:int):
    files=os.listdir(bib_folder)
    references_lists=[]
    for f in files :
        if ".bib" in f : 
            references_lists.append(ImportBib(bib_folder+"/"+f,slr_round))
    return references_lists


def GetReferencesFromPreviousRound(ROUND:int):
    previous=[]
    files=os.listdir("bib_round_"+str(ROUND-1))
    for f in files :
        if ".bib" in f :
            previous.append(ImportBib("bib_round_"+str(ROUND-1)+"/"+f,slr_round=ROUND))
    return previous

def Round_Merge_All_List(references_lists:list,level:int):
    # references_list is a list of all the references list. Each sub list contains all the references from one paper
    ref_len=len(references_lists)
    if ref_len == 2 :
        final=MergeList(references_lists[0],references_lists[1],level)
        return final
        # 2 lists => merge
    if ref_len < 2 :
            return references_lists[0]
    else :
        sp=int(ref_len/2)
        part_one=references_lists[:sp]
        part_two=references_lists[sp:]
        final = MergeList(Round_Merge_All_List(part_one,level),Round_Merge_All_List(part_two,level),level)
        return final
        # split and rec

def Gen_filtered_CSVs(L:list,slr_round:int,file_name,filter_words:list,NKwords:int):
    new_papers=[]
    filtered=[]
    for ref in L : 
        if ref.round == slr_round :
            new_papers.append(ref)
    new_papers.sort(key=lambda x: x.appearance, reverse=True)
    for ref in new_papers :
        nkwords=0
        title_word=ref.title.split(" ")
        for w in title_word:
            if w in filter_words :
                nkwords+=1
        if nkwords < NKwords :
            filtered.append(ref)
            new_papers.remove(ref)
    with open("./csv/"+file_name,"w") as filtered_csv : 
        filtered_csv.write("title;author;journal;year;round;appearance;\n")
        for ref in new_papers : 
            filtered_csv.write(ref.CSV_Line())
        filtered_csv.write("###;###;###;###;###;\n")
        for ref in filtered :
            filtered_csv.write(ref.CSV_Line())
    
