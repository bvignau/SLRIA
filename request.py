import os
import jellyfish

def pmkdir(path:str):
    try :
        os.mkdir(path)
    except :
        print("[!] Error in creating "+path+"directory")

def GenDirs(requests:list,papers_by_request:int,databases:list,BASE_DIR):
    for d in databases :
        database_path=BASE_DIR+"/"+d
        pmkdir(database_path)
        for r in requests :
            pmkdir(database_path+"/"+r)
            for i in range(papers_by_request):
                with open(database_path+"/"+r+"/"+str(i)+"_meta.txt", "w") as meta_file:
                    p=["title=REPLACE_ME\n","year=REPLACE_ME\n","author=REPLACE_ME\n"]
                    meta_file.writelines(p)


def compareRequest(r1,r2):
    dist =jellyfish.damerau_levenshtein_distance(r1,r2)
    if dist > 5 :
        return False
    else :
        return True


def MergeRequests(requests:list,papers_by_request:int,databases:list,BASE_DIR):
    merged_papers={} # dict {paper:appeareance}
    for d in databases :
        for r in requests :
            for i in range(papers_by_request):
                base_path=BASE_DIR+"/"+d+"/"+r+"/"
                try : 
                    with open(base_path+str(i)+"_meta.txt") as meta_file :
                        meta_data=meta_file.readlines()
                        title=meta_data[0].split("=")[1].split("\n")[0].strip(".")
                        year=meta_data[1].split("=")[1].split("\n")[0]
                        author=meta_data[2].split("=")[1].split("\n")[0]
                        ref=title.replace(" ","_").lower()+"_"+year+"_"+author.replace(" ","_").lower()
                        find=False
                        for rmerged in merged_papers.keys():
                            if compareRequest(rmerged,ref) :
                                merged_papers[rmerged]+=1
                                find=True
                        if find == False:
                            merged_papers[ref]=1
                except IOError :
                    print("dossier "+base_path+str(i)+"_meta.txt manquant")
    sorted_papers= sorted(merged_papers,key=merged_papers.get, reverse=True)
    return sorted_papers,merged_papers

def StatsForRequests(sorted_papers:list,merged_papers:dict,papers_by_request:int,request:list,databases:list,BASE_DIR:str):
    total_papers_searched=papers_by_request*len(databases)*len(request)
    total_merged_papers=len(sorted_papers)
    duplicate=total_papers_searched-total_merged_papers
    csv_path=BASE_DIR+"/csv/merge0.csv"
    with open(csv_path,"w") as csv_file :
        csv_file.write("paper ref;appearance\n")
        for p in sorted_papers :
            csv_line=p+";"+str(merged_papers[p])+"\n"
            csv_file.write(csv_line)
        csv_file.write("\ntotal_papers;total duplicate;final papers\n")
        csv_file.write(str(total_papers_searched)+";"+str(duplicate)+";"+str(total_merged_papers)+"\n")

def GenDirectoriesForPapers(merged_papers:dict, sorted_papers:list, BASE_DIR:str, round:int):
    i=0
    basepath=BASE_DIR+"/papers_round_"+str(round)+"/"
    pmkdir(basepath)
    for p in sorted_papers : 
        path=basepath+str(i)+"_"+p+"_"+str(merged_papers[p])
        pmkdir(path)
        i+=1

