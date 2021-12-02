import re
import os
import nltk
from nltk.corpus import stopwords
from nltk import sent_tokenize

#nltk.download('punkt')
#nltk.download('stopwords')

def first_400(words) :
    l = len(words)
    res = ""
    i = 0
    cnt = 0
    while(i<l and cnt<400) :
        w = words[i]
        w = w.strip()
        if re.search("([=/*\+])+", w) is None :
            res = res + " " + w
            cnt = cnt+1
        i = i + 1
    return res

def first_1000(words) :
    l = len(words)
    res = ""
    i = 0
    cnt = 0
    while(i<l and cnt<1000) :
        w = words[i]
        w = w.strip()
        if re.search("([=/*\+])+", w) is None :
            res = res + " " + w
            cnt = cnt+1
        i = i + 1
    return res

def remove_stop_words(paragraph):
    
    paragraph = re.sub("[\(\[].*?[\)\]]", "", paragraph)
    all_words = paragraph.split(' ')
    # sentences = nltk.sent_tokenize(paragraph)
    # for i in range(len(sentences)):
    #     words = nltk.word_tokenize(sentences[i])
    #     words = [word for word in words if word not in set(stopwords.words('english'))]
    #     words = [word for word in words if len(word)>1]
    #     sentences[i] = words
    #     all_words += words
    #print(all_words)
    return all_words


def write_400(text, out_file) :
    if text != "" :
        out_file.write(text + "\n\n")


def handle_highlights(highlights, out_file) :
    lst = highlights.split("\n")
    for sentence in lst :
        sent = sentence.strip()
        if sent != "" :
            out_file.write("@highlight "+sent+"\n")

def handle_abstract(wordlist_abstract, out_file) :
    abs = ""
    for word in wordlist_abstract :
        if re.search("([=/*\+])+", word) is None :
            abs = abs + " " + word
    out_file.write(abs + "\n\n")
    

# PATH = path of folder which contains text files

path = "C:\\Users\\91843\\Downloads\\SEND_Ahmed\\SEND_Ahmed"

os.chdir(path)

for file in os.listdir():
    if file.endswith(".txt") :
        f1=open(file, encoding='utf8')

        introduction = ""
        method = ""
        results = ""
        conclusions = ""
        abstract = ""
        highlights = ""

        flag = True
        tag = "none"
        l = f1.readline()
        l = l.strip()
        if l=="@&#HIGHLIGHTS@&#" :
            tag="highlights"
            flag=False
        elif l=="@&#INTRODUCTION@&#" :
            tag="introduction"
            flag=False
        elif l=="@&#METHOD@&#" :
            tag="method"
            flag=False
        elif l=="@&#RESULTS@&#" :
            tag="results"
            flag=False
        elif l=="@&#ABSTRACT@&#" :
            tag="abstract"
            flag=False
        elif l=="@&#CONCLUSIONS@&#" :
            tag="conclusions"
            flag=False
        else :
            tag="none"

            
        while(True):
            l = f1.readline()
            if not l :
                break
            l = l.strip()
            
            if len(l)>1 :
                if l=="@&#HIGHLIGHTS@&#" :
                    tag="highlights"
                    flag=False
                elif l=="@&#INTRODUCTION@&#" :
                    tag="introduction"
                    flag=False
                elif l=="@&#METHOD@&#" :
                    tag="method"
                    flag=False
                elif l=="@&#RESULTS@&#" :
                    tag="results"
                    flag=False
                elif l=="@&#ABSTRACT@&#" :
                    tag="abstract"
                    flag=False
                elif l=="@&#CONCLUSIONS@&#" :
                    tag="conclusions"
                    flag=False
                elif re.search("@&#.*@&#",l) is not None :
                    tag="none"

                if tag == "highlights" :
                    if flag==True :
                        highlights = highlights + "\n" + l
                    flag = True
                elif tag == "introduction" :
                    if flag==True :
                        introduction = introduction + " " + l
                    flag = True
                elif tag == "method" :
                    if flag==True :
                        method = method + " " + l
                    flag = True
                elif tag == "results" :
                    if flag==True :
                        results = results + " " + l
                    flag = True
                elif tag == "abstract" :
                    if flag==True :
                        abstract = abstract + " " + l
                    flag = True
                elif tag == "conclusions" :
                    if flag==True :
                        conclusions = conclusions + " " + l
                    flag = True


        wordlist_introduction = remove_stop_words(introduction)
        introduction = first_400(wordlist_introduction)
        wordlist_method = remove_stop_words(method)
        method = first_400(wordlist_method)
        wordlist_results = remove_stop_words(results)
        results = first_400(wordlist_results)
        wordlist_conclusions = remove_stop_words(conclusions)
        conclusions = first_400(wordlist_conclusions)
        wordlist_abstract = remove_stop_words(abstract)
        abstract = first_1000(wordlist_abstract)

        # OPEN OUTPUT FILE

        sz = len(file)
        out_file_path = "dataset1/" + file[:sz-4] + ".txt"
        out_file = open(out_file_path, 'w', encoding='utf8')

        # WRITE SECTIONS IN TEXT FILE

        #handle_abstract(wordlist_abstract, out_file)
        write_400(abstract, out_file)

        write_400(introduction, out_file)

        write_400(method, out_file)

        write_400(results, out_file)

        write_400(conclusions, out_file)


        handle_highlights(highlights, out_file)

        f1.close()
        out_file.close()

