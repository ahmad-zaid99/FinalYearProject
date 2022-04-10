import os
# import nltk
from rouge import Rouge


rouge = Rouge()

# path = "C:\\FinalYearProject\\pdf to txt\\New folder\\dataset2"
path = "C:\\FinalYearProject\\scisummnet\\pred"
os.chdir(path)

# avg = 0
# cnt = 0
# avg_rouge1 = 0
# avg_rouge2 = 0
# avg_rougel = 0

model_out_list = []
reference_list = []

count = 0

for file in os.listdir():
    if file.endswith(".txt"):

        count += 1

        model_out_R = ""
        reference_R = ""
        # f1=open(file, encoding='utf8')
        f1 = open(file)

        # file2 = "gold/" + file[:len(file)-4] + "_gold" + ".txt"
        file2 = "C:/FinalYearProject/scisummnet/gold/" + \
            file[:len(file)-4] + "_gold" + ".txt"

        # f2 = open(file2, encoding='utf8')
        f2 = open(file2)

        f1_str = f1.readlines()
        # hypothesis = []
        for hypo in f1_str:
            # hypothesis = hypothesis + hypo.split()
            model_out_R = model_out_R + hypo + "\n"

        model_out_list.append(model_out_R)

        f2_str = f2.readlines()
        # reference = []
        for ref in f2_str:
            # reference = reference + ref.split()
            reference_R = reference_R + ref + "\n"

        reference_list.append(reference_R)

        # references = [reference]
        # BLEUScore = nltk.translate.bleu_score.sentence_bleu(
        # references, hypothesis)

        # if BLEUScore>0.1 :
        # avg += BLEUScore
        # cnt += 1

        # print(BLEUScore)

        r_score = rouge.get_scores(model_out_R, reference_R,)
        # print(r_score)
        # print("R - ", r_score[0]['rouge-1']['r'])
        print(file, r_score)

        f2.close()
        f1.close()


avg_rouge_score = rouge.get_scores(model_out_list, reference_list, avg=True)

print("Average ROUGE SCORE ", avg_rouge_score)

# print(count)
# avg = avg/cnt
# print(cnt)
# print("Average BLEU Score = ", avg)
