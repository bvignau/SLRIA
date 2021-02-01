import os
with open("f.txt", "r") as f:   
    fields=f.readlines()
    with open("code.py","w") as cf:
        for l in fields:
            l=l.split("\n")[0]
            cline="if '"+l+"' in ref:\n\tself."+l+" = str(ref['"+l+"']).split(\"'\")[1].lower()\nelse:\n\tself."+l+" =\"unknow "+l+"\"\n"
            print(cline)
            cf.write(cline)