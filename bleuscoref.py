import os
import nltk
# from rouge import Rouge


# rouge = Rouge()

# path = "C:\\FinalYearProject\\pdf to txt\\New folder\\dataset2"
path = "C:\\FinalYearProject\\text_files2\\pred"
os.chdir(path)

avg = 0
cnt = 0


for file in os.listdir():
    if file.endswith(".txt"):

        # f1=open(file, encoding='utf8')
        f1 = open(file)

        # file2 = "gold/" + file[:len(file)-4] + "_gold" + ".txt"
        file2 = "C:/FinalYearProject/text_files2/gold/" + \
            file[:len(file)-4] + "_gold" + ".txt"

        # f2 = open(file2, encoding='utf8')
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

        # if BLEUScore>0.1 :
        avg += BLEUScore
        cnt += 1

        print(file, BLEUScore)

        # r_score = rouge.get_scores(model_out_R, reference_R,)
        # print(r_score)
        # print("R - ", r_score[0]['rouge-1']['r'])

        f2.close()
        f1.close()

avg = avg/cnt
# print(cnt)
print("Average BLEU Score = ", avg)
