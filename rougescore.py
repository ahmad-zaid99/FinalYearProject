import os
from rouge import Rouge
rouge = Rouge()
path = "C:\\FinalYearProject\\text_files\\pred"
os.chdir(path)
model_out_list = []
reference_list = []
count = 0
for file in os.listdir():
    if file.endswith(".txt"):
        count += 1
        model_out_R = ""
        reference_R = ""
        f1 = open(file)
        file2 = "C:/FinalYearProject/text_files/gold/" + \
            file[:len(file)-4] + "_gold" + ".txt"
        f2 = open(file2)
        f1_str = f1.readlines()
        for hypo in f1_str:
            model_out_R = model_out_R + hypo + "\n"
        model_out_list.append(model_out_R)
        f2_str = f2.readlines()
        for ref in f2_str:
            reference_R = reference_R + ref + "\n"
        reference_list.append(reference_R)
        r_score = rouge.get_scores(model_out_R, reference_R,)
        print(file, r_score)
        f2.close()
        f1.close()
avg_rouge_score = rouge.get_scores(model_out_list, reference_list, avg=True)
print("Average ROUGE SCORE ", avg_rouge_score)
