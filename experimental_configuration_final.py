import os
import re
import nltk
from nltk import sent_tokenize
# import xml.etree.ElementTree as ET
from keywords import keywords

reg = "(?:"
for w in keywords:
    reg = reg + w + "|"
reg = reg[:len(reg)-1] + ")"


def check(sent):
    sent = re.sub("\([a-zA-Z, &. \d;]*[12]\d{3}\),? ?", "", sent)
    sent = re.sub("&[^ \t\r\v\f]*;", "", sent)
    sent = sent.lower()
    if len(re.findall("[\d\.]*\d+ ", sent)) > 1:
        return True
    if re.search(reg, sent) is not None:
        return True
    return False


path = "C:\\FinalYearProject\\text_files2"
os.chdir(path)

for file in os.listdir():
    if file.endswith(".txt"):
        op = open(file)
        text = op.read()
        file2 = "pred/" + file[:len(file)-4] + ".txt"
        fop = open(file2, 'w')
        sentences = nltk.sent_tokenize(text)
        for sentence in sentences:
            if check(sentence) == True:
                fop.write(sentence + "\n")
        fop.close()
