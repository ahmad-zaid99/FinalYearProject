import json
import re
import os

path = "C:\\Users\\91843\\Downloads\\SEND_Ahmed\\SEND_Ahmed"

os.chdir(path)

#f2 = open('output.json', 'w', encoding='utf8')
#lst = []
for file in os.listdir():
    if file.endswith(".txt") :
        f1=open(file, encoding='utf8')
        
        summary = ""
        document = ""
        flag = False
        while(True):
            l = f1.readline()
            if not l :
                break
            l = l.strip()
            if flag == True :
                x = re.search("@&#.*@&#",l)
                if x is not None :
                    flag = False
                else :
                    summary = summary + " " + l
            else :
                x = re.search("@&#ABSTRACT@&#", l)
                y = re.search("@&#.*@&#", l)
                if x is not None :
                    flag = True
                elif y is not None :
                    l = l.replace("@&#", " ")
                    document = document + " " + l
                else :
                    document = document + " " + l
        sz = len(file)

        objectResult={"id":file[:sz-4],"article":document.strip(),"highlights":summary.strip()}

        out_file = "dataset/" + file[:sz-4] + ".json"

        f2 = open(out_file, 'w', encoding='utf8')
        f2.write(json.dumps(objectResult))
        #lst.append(objectResult)

        f2.close()
        f1.close()





