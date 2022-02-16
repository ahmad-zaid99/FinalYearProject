import os
import re
import xml.etree.ElementTree as ET
from keywords import keywords


reg = "(?:"

for w in keywords:
    reg = reg + w + "|"

reg = reg[:len(reg)-1] + ")"


def check(sent):

    # print(sent)

    sent = re.sub("\([a-zA-Z, &. \d;]*[12]\d{3}\),? ?", "", sent)
    sent = re.sub("&[^ \t\r\v\f]*;", "", sent)

    sent = sent.lower()

    if len(re.findall("[\d\.]*\d+ ", sent)) > 1:
        return True

    if re.search(reg, sent) is not None:
        return True

    return False


path = "C:\\FinalYearProject\\scisummnet"
os.chdir(path)

for file in os.listdir():
    if file.endswith(".xml"):
        mytree = ET.parse(file)
        paper = mytree.getroot()

        file2 = "pred/" + file[:len(file)-4] + ".txt"

        fop = open(file2, 'w')

        for heading in paper:

            flag = False
            # if heading.tag in ["S", "ABSTRACT"] :
            #     continue

            # print(heading.tag, heading.attrib["title"])
            # head = ""
            if heading.tag not in ["S", "ABSTRACT"]:
                flag = True

            head = " "
            if flag:
                head = heading.attrib['title']
            head = head.lower()

            reg1 = "(?:introduction|acknowledgement|conclusion|background|future|related|previous)"

            if flag and re.search(reg1, head) is not None:
                flag = False

            # print(flag)
            #     head = heading.attrib['title']
            #     print(head)
            # head = head.lower()

            # reg = "(introduction|acknowledgement|conclusion|)"
            # if re.search(reg,head) is not None :
            #     continue
            # if heading.tag not in ["S", "ABSTRACT"] :
            #     abc = heading.attrib["title"]
            if flag:
                for sentence in heading:
                    if check(sentence.text) == True:
                        fop.write(sentence.text + "\n")

        fop.close()
