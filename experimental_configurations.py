import re
import os
import nltk
from nltk import sent_tokenize


def fun(paragraph, result) :
    
    #paragraph = re.sub("[\(\[].*?[\)\]]", "", paragraph)
    sentences = nltk.sent_tokenize(paragraph)

    reg = '(?:encoder|decoder|epoch|iteration|gpu|token|tokenizer|embedding|encoding|nltk|pgnet|cnn|rnn|neural network|rouge|bert|bart|xlnet|roberta|electra|gpt|t5|text-to-text|elmo|ulmfit|transformer|flair|stanfordnlp)'

    for i in range(len(sentences)) :
    
        sentence = sentences[i].lower()
        if re.search(reg, sentence) is not None :
            result.append(sentences[i])
        


    
    


path = "C:\\Users\\91843\\Downloads\\SEND_Ahmed\\SEND_Ahmed"

os.chdir(path)

f2 = open("dataset2/abcdef.txt", 'w', encoding='utf8')


for file in os.listdir():
    if file.endswith(".txt") :
        f1=open(file, encoding='utf8')

        result = []

        method = ""
        results = ""
        implementation = ""

        flag = True
        tag = "none"
            
        while(True):
            l = f1.readline()
            if not l :
                break
            l = l.strip()
            
            if len(l)>1 :
                
                if l=="@&#METHOD@&#" or l=="@&#METHODS@&#" :
                    tag="method"
                    flag=False
                elif l=="@&#RESULTS@&#" or l=="@&#RESULT@&#" :
                    tag="results"
                    flag=False
                elif l=="@&#IMPLEMENTATION@&#" or l=="@&#IMPLEMENTATIONS@&#" :
                    tag="implementation"
                    flag=False
                elif l=="@&#EXPERIMENT@&#" or l=="@&#EXPERIMENT@&#" or l=="@&#EXPERIMENTATION@&#" or l=="@&#EXPERIMENTATIONS@&#":
                    tag="implementation"
                    flag=False
                elif l=="@&#MODEL@&#" or l=="@&#MODELS@&#" :
                    tag="implementation"
                    flag=False
                elif re.search("@&#.*@&#",l) is not None :
                    tag="none"


                if tag == "method" :
                    if flag==True :
                        method = method + " " + l
                    flag = True
                elif tag == "results" :
                    if flag==True :
                        results = results + " " + l
                    flag = True
                elif tag == "implementation" :
                    if flag==True :
                        implementation = implementation + " " + l
                    flag = True
        
        fun(method, result)
        fun(results, result)
        fun(implementation, result)

        out_file_path = "dataset2/" + file
        out_file = open(out_file_path, 'w', encoding='utf8')

        if len(result)>0 :
            for sen in result :
                # out_file.write(file+"\n")
                f2.write(sen+"\n")
                out_file.write(sen+"\n")

        # for sen in result :
        #     out_file.write(file+"\n")
        #     f2.write(sen+"\n")
        if len(result)>0 :
            f2.write("\n")
        f1.close()
        out_file.close()
f2.close()


