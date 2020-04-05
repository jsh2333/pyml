import matplotlib.pyplot as plt
import pandas as pd
import json

import glob, os.path, re, json
# print('cwd: '+ os.getcwd())
os.chdir('./day3')

# 알파벳 출현 빈도 데이터 읽어 들이기 --- (※1)
with open("./lang/freq.json", "r", encoding="utf-8") as fp:
    freq = json.load(fp)

# fq=freq[0]["labels"]
# print(fq)
# print(len(fq))
# exit()
# fq = freq[0]["freqs"]
# print(fq)
# print(len(fq))
# exit()
#------------------------------
# 언어마다 계산하기 --- (※2)  출현빈도계산
lang_dic = {}
for i, lbl in enumerate(freq[0]["labels"]):
    fq = freq[0]["freqs"][i]
    if not (lbl in lang_dic):
        lang_dic[lbl] = fq
        # print(lang_dic[lbl])
        # print(lbl)
        # print(len(lang_dic[lbl]))
        continue
    for idx, v in enumerate(fq):
        # print(v)
        # print(idx)
        # print(lbl)
        # print(len(fq))
        # print(lang_dic[lbl][idx])
        lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v) / 2
        # print(lang_dic[lbl][idx])
# print(len(lang_dic))
# exit()
#------------------------------

# Pandas의 DataFrame에 데이터 넣기 --- (※3)
asclist = [[chr(n) for n in range(97,97+26)]]
df = pd.DataFrame(lang_dic, index=asclist)
# print(asclist)
# print(df)
# exit()
#------------------------------

# 그래프 그리기 --- (※4)
plt.style.use('ggplot')
df.plot(kind="bar", subplots=True, ylim=(0,0.15))
plt.savefig("lang-plot-bar.png")

# 그래프 그리기 --- (※5)
plt.style.use('ggplot')
df.plot(kind="line", subplots=True, ylim=(0,0.15))
plt.savefig("lang-plot-line.png")


df.plot(kind="line")  
plt.show()


