import os
import re
import xml.etree.ElementTree as ET

path = "C:\\FinalYearProject\\newfolder"
os.chdir(path)

for file in os.listdir():
    if file.endswith(".xml"):
        mytree = ET.parse(file)
        paper = mytree.getroot()
        file2 = "text_files/" + file[:len(file)-4] + ".txt"
        print(file2)
        fop = open(file2, 'w')
        for heading in paper:
            flag = False
            if heading.tag not in ["S", "ABSTRACT"]:
                flag = True
            head = " "
            if flag:
                head = heading.attrib['title']
            head = head.lower()
            reg1 = "(?:introduction|acknowledgement|conclusion|background|future|related|previous)"
            if flag and re.search(reg1, head) is not None:
                flag = False
            i = 0
            if flag:
                for sentence in heading:
                    line = sentence.text
                    line = line.strip()
                    line = line.encode("utf-8").decode('utf-8', 'ignore')
                    fop.write(line + "\n")
        fop.close()
