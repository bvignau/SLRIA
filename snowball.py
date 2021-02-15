import os
from references import *
from  pdfToBib import *
from bibParser import ImportBib

# This function extract the text from all pdf in the folder and subfolder given
# Then it extract the references part. This is done by identifying the IEEE Style "[X] ref". This may not work with other citation style
def SnowballExtract(folder_path:str):
    papers=os.listdir(folder_path)
    for p in papers :
        ld=os.listdir(folder_path+"/"+p)
        pdf=[]
        for f in ld :
            if ".pdf" in f :
                pdf.append(f)
        for doc in pdf : 
            ExtractTextFromPDF(doc, path=folder_path+"/"+p+"/")
            find_references_in_text(input_file=folder_path+"/"+p+"/text_"+doc+".txt",output_file=folder_path+"/"+p+"/ref_"+doc+".txt")

# This function transform the extracted section in bibfile that can be used to compare references and merge them
def SnowballDumpReferences(folder_path:str,round:int):
    papers=os.listdir(folder_path)
    for p in papers : 
        listfile= os.listdir(folder_path+"/"+p)
        refFiles=[]
        for f in listfile :
            if "ref_" and ".txt" in f : 
                refFiles.append(f)
        for rf in refFiles :
            ExtractReferencesFromTxt(filename=folder_path+"/"+p+"/"+rf,round=round)

# Create a list with one list of references for each bib file
def CreateRefLists(bib_folder:str):
    files=os.listdir(bib_folder)
    references_lists=[]
    for f in files :
        if ".bib" in f : 
            references_lists.append(ImportBib(bib_folder+"/"+f))
    return references_lists


def GetReferencesFromPreviousRound(ROUND:int):
    previous=[]
    files=os.listdir("bib_round_"+str(ROUND-1))
    for f in files :
        if ".bib" in f :
            previous.append(ImportBib("bib_round_"+str(ROUND-1)+"/"+f))
    return previous

def Round_Merge_All_List(references_lists:list,level:int):
    ref_len=len(references_lists)
    if ref_len == 2 :
        final=MergeList(references_lists[0],references_lists[1],level)
        return final
        # 2 lists => merge
    else if ref_len < 2 :
        return references_lists
    else :
        sp=int(ref_len/2)
        part_one=references_lists[:sp]
        part_two=references_lists[sp:]
        final = MergeList(Merge_All_List(part_one,lvl),Merge_All_List(part_two,lvl),lvl)
        return final
        # split and rec
