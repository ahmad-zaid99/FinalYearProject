import os
import nltk
path = "C:\\FinalYearProject\\text_files\\pred"
os.chdir(path)
avg = 0
cnt = 0
for file in os.listdir():
    if file.endswith(".txt"):
        f1 = open(file)
        file2 = "C:/FinalYearProject/text_files/gold/" + \
            file[:len(file)-4] + "_gold" + ".txt"
        f2 = open(file2)
        f1_str = f1.readlines()
        hypothesis = []
        for hypo in f1_str:
            hypothesis = hypothesis + hypo.split()
        f2_str = f2.readlines()
        reference = []
        for ref in f2_str:
            reference = reference + ref.split()
        references = [reference]
        BLEUScore = nltk.translate.bleu_score.sentence_bleu(
            references, hypothesis)
        avg += BLEUScore
        cnt += 1
        print(file, BLEUScore)
        f2.close()
        f1.close()
avg = avg/cnt
print("Average BLEU Score = ", avg)
