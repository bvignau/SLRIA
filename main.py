from pdfToBib import ExtractReferencesFromPDF
from references import *
from bibParser import *
from request import *
import configparser
import argparse
import os
import shutil
import sys

BASE_DIR=(sys.argv[2])
print(BASE_DIR)
pathname = os.path.dirname(sys.argv[0])
SOURCE_DIR= os.path.abspath(pathname)+"/"

def ConfigParse(base_folder, add_round:bool):
    config = configparser.ConfigParser()
    config.read(base_folder+'/SLR.conf')
    requests=[]
    for i in range(len(config['Request'])):
        r="r"+str(i)
        requests.append(config['Request'][r].replace(' ','_'))

    #CSV=config['RQ']['CSV'].split(',')
    #TEXTE=config['RQ']['Text'].split(',')

    COMPARISON=int(config['Filter']['comparison'])
    #APPEARANCE=int(config['Filter']['appearance'])

    NKWORDS=int(config['Filter']['NKwords'])
    KWORDS=config['Filter']['Kwords'].split(',')

    ROUND=int(config['SLRIA']['round'])
    PAPERS_BY_REQUEST=int(config['SLRIA']['papers_by_request'])
    DATABASES=config['SLRIA']['databases'].split(',')
    #return requests,CSV,TEXTE, COMPARISON, APPEARANCE, KWORDS, NKWORDS, ROUND, PAPERS_BY_REQUEST, DATABASES
    if add_round :
        config['SLRIA']['round']=str(ROUND+1)
        with open(base_folder+'/SLR.conf', 'w') as config_file :
            config.write(config_file)
    return requests, COMPARISON, KWORDS, NKWORDS, ROUND, PAPERS_BY_REQUEST, DATABASES



def init(): 
    if os.path.isdir(BASE_DIR) == False:
        pmkdir(BASE_DIR)
        print("[+] The Project Folder will contain later the folders for the pdf to analyse")
        #srcConf=SOURCE_DIR+"empty.conf"
        srcConf="empty.conf"
        if os.path.isfile("SLR.conf"):
            print("[!] Error SLR.conf already created")
            print("[!] Please complete it")
        else :
            shutil.copyfile(srcConf,BASE_DIR+"/SLR.conf")
        pmkdir(BASE_DIR+"/final_bib")
        pmkdir(BASE_DIR+"/csv")
        print("[+] SLRHelper create a folder 'bib' to put your bibfile in")
        print("[+] NOW COMPLETE THE SLR.conf FILE FOR FURTHER USE !")
    else :
        print("Error Results folder already exist")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument('base_folder')
    arg = parser.parse_args()
    if arg.command not in ["init","start","extract","merge", "request"]:
        print("Error, unknow command")
        print("Use : 'slrh init' to create a directory and a empty config file")
        # TODO make the help menu
    else : 
        if arg.command == "init":
            init()
        if arg.command == "request":
            requests, COMPARISON, KWORDS, NKWORDS, ROUND, PAPERS_BY_REQUEST, DATABASES = ConfigParse(BASE_DIR, False)
            GenDirs(requests,PAPERS_BY_REQUEST,DATABASES,BASE_DIR)
        if arg.command == "start":
            # merge 1st round
            requests, COMPARISON, KWORDS, NKWORDS, ROUND, PAPERS_BY_REQUEST, DATABASES = ConfigParse(BASE_DIR, False)
            sorted_papers,merged_papers=MergeRequests(requests,PAPERS_BY_REQUEST,DATABASES,BASE_DIR)
            StatsForRequests(sorted_papers,merged_papers,PAPERS_BY_REQUEST,requests,DATABASES,BASE_DIR)
            GenDirectoriesForPapers(merged_papers,sorted_papers,BASE_DIR,0)
        if arg.command == "extract" :
            print("TODO")
            requests, COMPARISON, KWORDS, NKWORDS, ROUND, PAPERS_BY_REQUEST, DATABASES = ConfigParse(BASE_DIR, False)
            folder_path="/papers_round_"+str(ROUND)
            os.chdir(BASE_DIR)
            

            # Check round folder
            # for each folder, extract References
            # ASK to check txt file
        if arg.command == "merge" :
            print("TOFO")
            # Find good folder / round
            # dump bib
            # merge references
            # generate new bib
            # generate csv with all new papers
            # generate folders for all new papers
            # update round

if __name__ == "__main__":
    main()