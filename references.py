from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import jellyfish


AUTHORS = 10
TITLE = 40
OTHERS = 1 
class Reference():
    def __init__(self):
        self.ID="unknow"
        self.ENTRYTYPE =""
        self.title = ""
        self.url = ""
        self.author = ""
        self.year = ""
        self.booktitle=""
        self.journal=""
        self.chapter=""
        self.editor=""
        self.howpublished=""
        self.institution=""
        self.month=""
        self.number=""
        self.organization=""
        self.pages=""
        self.publisher=""
        self.volume=""
        self.appearance=0 # nombre de fois que la référence est apparue dans notre recherche
        self.round=0
    

    def create_Ref(self,ref,slr_round):
        self.round=slr_round
        if 'ENTRYTYPE' in ref:
            self.ENTRYTYPE = str(ref['ENTRYTYPE'])
        else:
            self.ENTRYTYPE ="unknow ENTRYTYPE"
        if 'ID' in ref:
            self.ID = str(ref['ID'])
        else:
            self.ID ="unknow_ID"
        if 'title' in ref:
            self.title  = str(ref['title']).lower()
            if self.title[-1:] == '”':
                self.title=self.title[:-1]
        else:
            self.title  ="unknow title"
        if 'url' in ref:
            self.url  = str(ref['url'])
        else:
            self.url  ="unknow url"
        if 'author' in ref:
            self.author  = str(ref['author']).lower()
        else:
            self.author  ="unknow author"
        if 'year' in ref:
            self.year  = str(ref['year'])
        else:
            self.year  ="unknow year"
        if 'booktitle' in ref:
            self.booktitle = str(ref['booktitle']).lower()
        else:
            self.booktitle ="unknow booktitle"
        if 'journal' in ref:
            self.journal = str(ref['journal']).lower()
        else:
            self.journal ="unknow journal"
        if 'chapter' in ref:
            self.chapter = str(ref['chapter'])
        else:
            self.chapter ="unknow chapter"
        if 'editor' in ref:
            self.editor = str(ref['editor']).lower()
        else:
            self.editor ="unknow editor"
        if 'howpublished' in ref:
            self.howpublished = str(ref['howpublished'])
        else:
            self.howpublished ="unknow howpublished"
        if 'institution' in ref:
            self.institution = str(ref['institution']).lower()
        else:
            self.institution ="unknow institution"
        if 'month' in ref:
            self.month = str(ref['month'])
        else:
            self.month ="unknow month"
        if 'number' in ref:
            self.number = str(ref['number'])
        else:
            self.number ="unknow number"
        if 'organization' in ref:
            self.organization = str(ref['organization']).lower()
        else:
            self.organization ="unknow organization"
        if 'pages' in ref:
            self.pages = str(ref['pages'])
            if self.pages[-1:] == ',':
                self.pages=self.pages[:-1]
        else:
            self.pages ="unknow pages"
        if 'publisher' in ref:
            self.publisher = str(ref['publisher']).lower()
            
        else:
            self.publisher ="unknow publisher"
        if 'volume' in ref:
            self.volume = str(ref['volume']).lower()
        else:
            self.volume ="unknow volume"
        self.appearance=1
    
    def get_ID(self):
        return self.author.split()[0]+self.year+self.title.split()[0]

    def __str__(self):
        return self.title+" authored by "+self.author+" in "+self.journal
    
    def CSV_Line(self):
        return self.title+";"+self.author+";"+self.journal+";"+str(self.year)+";"+str(self.round)+";"+str(self.appearance)+";\n"

def authorsComp(R1,R2):
    score=0.0
    if "unknow" in R1.author or "unknow" in R2.author : # si l'un des deux est inconnu, pas de comparaisaon possible
        return 0
    else :
        auth1=R1.author.split("and")
        auth2=R2.author.split("and")
        for a1 in auth1 :
            if a1 in auth2 :
                score+=AUTHORS/len(auth1)
    return score
        
# TODO
# title = 40 pts
# authors = 10/ nb authors 
# all other 1 pts
def RefCompare(R1:Reference, R2:Reference, lvl:int):
    score=0
    if R2.title != "unknow title" and R1.title != "unknow title":
        if jellyfish.damerau_levenshtein_distance(R2.title,R1.title) < 5 :
            score+=TITLE
    score+=authorsComp(R1,R2)
    attrR1=R1.__dict__
    attrR2=R2.__dict__
    for a in attrR1.keys() : 
        if a != "author" and a != "title":
            if attrR1[a] == attrR2[a]:
                score += OTHERS
    if score >= lvl :
        return True
    else:
        return False

def MergeRef(R1:Reference,R2:Reference, lvl:int):
    if RefCompare(R1,R2,lvl) :
        if R1.round < R2.round :
            R1.appearance+=R2.appearance
            return [R1]
        else :
            R2.appearance+=R1.appearance
            return [R2]
    else :
        return [R1,R2]

def Merge_List_Ref(R1:Reference,L2:list,lvl:int):
    add = True
    for r in L2 :
        if RefCompare(R1,r,lvl):
            r.appearance+=R1.appearance
            add = False
            break
    if add :
        L2.append(R1)
    return L2

def Filtre_title(Ref,Kwords,lvl):
    filtre=[]
    for r in Ref :
        total=0
        for w in r.title.split(' '):
            if w in Kwords :
                total+=1
        for w in r.misc.split(' '):
            if w in Kwords :
                total+=1
        if total >= lvl :
            filtre.append(r)
    return filtre


def MergeList(L1:list,L2:list,lvl:int):
    final=[]
    if isinstance(L2,list):
        #L2 = List
        if isinstance(L1,list):
            #L1 & L2 = List
            for r2 in L2:
                add = True
                for r1 in L1 :
                    if RefCompare(r1,r2,lvl) == True:
                        r1.appearance+=r2.appearance 
                        add = False
                        break
                if add == True :
                    final.append(r2)
            final.extend(L1)
        else :
            #R1 & L2
            final=Merge_List_Ref(L1,L2,lvl)
    else:
        # R2
        if isinstance(L1,list):
            #L1 & R2 = List
            final=Merge_List_Ref(L2,L1,lvl)
        else :
            #R1 & R2
            final=MergeRef(L1,L2,lvl)
    return final




def Merge_All_List(L,lvl):
    if len(L) > 2:
        # Divide by 2 and recursive
        L1=[]
        L2=[]
        for i in range(int(len(L)/2)):
            L1.append(L[i])
        for j in range(i+1,len(L)):
            L2.append(L[j])
        return MergeList(Merge_All_List(L1,lvl),Merge_All_List(L2,lvl),lvl)
    else :
        if len(L) == 1 :
            return L
        else :
            #print("L0 = "+str(L[0]))
            #print("L1 = "+str(L[1]))
            return MergeRef(L[0],L[1],lvl)

def filtre(L,app):
    final=[]
    for r in L :
        if r.appearance >= app :
            final.append(r)
    return final

def genBib(refList, file):
    entries=[]
    attr=refList[0].__dict__.keys()
    for ref in refList:
        entry={}
        for a in attr :
            if  a != 'appearance' and a != 'round':
                att=getattr(ref, a, "unknow")
                if "unknow" not in str(att) or a == 'ID': 
                    entry[a]=att
        entries.append(entry)
    db=BibDatabase()
    db.entries=entries
    writer = BibTexWriter()
    with open("./final_bib/"+file, "w") as bibfile:
        bibfile.write(writer.write(db))


def genCSV(L:list,file):
    with open("./csv/"+file,"w") as csvFile :
        csvFile.write("title;author;journal;year;round;appearance;\n")
        for ref in L :
            csvFile.write(ref.CSV_Line())

def printList(L:list):
    for r in L :
        print(str(r))