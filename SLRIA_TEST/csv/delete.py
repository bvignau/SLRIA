import os
import jellyfish

def Delete_Old(old_csv:str,new_csv:str):
    final=[]
    with open(old_csv,"r") as old_file:
        with open(new_csv,"r") as new_file:
            old_ref=old_file.readlines()[1:]
            new_ref=new_file.readlines()[1:]
            for nref in new_ref :
                add=True
                parts=nref.split(';')
                n_title = parts[0]
                for oref in old_ref :
                    o_title=oref.split(';')[0]
                    o_auth=o_title.split(' ')[-1]
                    o_title=o_title.split(' '+o_auth)[0]
                    o_title=o_title.rsplit(' ', 1)[0]
                    cmp=jellyfish.damerau_levenshtein_distance(o_title,n_title)
                    if cmp < 5 :
                        add=False
                if add :
                    final.append(nref)
    with open("/mnt/d/UQAC/UQAC/DOCTORAT/SLRIA/SLRIA_TEST/csv/final_0.csv",'w') as ffile :
        ffile.write("title;author;journal;year;round;appearance;\n")
        for ref in final : 
            ffile.write(ref)

Delete_Old('/mnt/d/UQAC/UQAC/DOCTORAT/SLRIA/SLRIA_TEST/csv/merge0.csv','/mnt/d/UQAC/UQAC/DOCTORAT/SLRIA/SLRIA_TEST/csv/filtered_new_papers_round_0.csv')
