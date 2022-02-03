from email import message_from_string
import os
import nltk



path = "C:\\FinalYearProject\\pdf to txt\\New folder\\dataset2"
os.chdir(path)

avg = 

for file in os.listdir():
    if file.endswith(".txt") :
        f1=open(file, encoding='utf8')

        file2 = "gold/" + file[:len(file)-4] + "_gold" + ".txt"

        f2 = open(file2, encoding='utf8')

        f1_str = f1.readlines()
        hypothesis = []
        for hypo in f1_str :
            hypothesis = hypothesis + hypo.split()
        

        f2_str = f2.readlines()
        reference = []
        for ref in f2_str :
            reference = reference + ref.split()
        references = [reference]
        BLEUScore = nltk.translate.bleu_score.sentence_bleu(references, hypothesis)

        print(BLEUScore)



        f2.close()
        f1.close()


