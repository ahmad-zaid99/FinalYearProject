
# importing modules

import re
import os
import nltk
from nltk import sent_tokenize


# function for finding keywords and extracting sentences

def fun(paragraph, result) :
    
    sentences = nltk.sent_tokenize(paragraph)

    # define reg expression
    reg = '(?:encoder|decoder|epoch|iteration|gpu|token|tokenizer|embedding|encoding|nltk|pgnet|cnn|rnn|neural|rouge|bert|bart|xlnet|roberta|electra|gpt|t5|text-to-text|elmo|ulmfit|framework|transformer|flair|stanfordnlp|classifier|lstm)'
    # model, dataset, width
    for i in range(len(sentences)) :
    
        sentence = sentences[i].lower()
        if re.search(reg, sentence) is not None :
            result.append(sentences[i])
        

# set path to folder containg txt files

path = "C:\\FinalYearProject\\pdf to txt\\New folder"

os.chdir(path)

#f2 = open("dataset2/abcdef.txt", 'w', encoding='utf8')


# loop through all txt files in the folder
for file in os.listdir():
    if file.endswith(".txt") :
        f1=open(file, encoding='utf8')

        result = []

        implementation = ""

        flag = True
        tag = "none"


        # separate contents by headings
        # check for keywords in contents other than abstract, introduction, conclusion 

        while(True):
            l = f1.readline()
            if not l :
                break
            l = l.strip()
            
            if len(l)>1 :
                if l=="@&#INTRODUCTION@&#" or l=="@&#ABSTRACT@&#" or l=="@&#CONCLUSION@&#" or l=="@&#CONCLUSIONS@&#" :
                    tag="none"
                elif l=="@&#DISCUSSION@&#" or l=="@&#DISCUSSIONS@&#" :
                    tag="none"
                    flag=False
                elif re.search("@&#.*@&#",l) is not None :
                    tag="implementation"
                    flag=False


                if tag == "implementation" :
                    if flag==True :
                        implementation = implementation + " " + l
                    flag = True
        
        fun(implementation, result)

        out_file_path = "dataset2/" + file
        out_file = open(out_file_path, 'w', encoding='utf8')

        if len(result)>0 :
            for sen in result :
                out_file.write(sen+"\n")

        # for sen in result :
        #     out_file.write(file+"\n")
        #     f2.write(sen+"\n")
        
        f1.close()
        out_file.close()



