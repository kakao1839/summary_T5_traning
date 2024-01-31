import os
import pandas as pd

df = pd.DataFrame(columns=["text","summary"])

with open ("output.tsv", encoding="utf-8") as f:
    for line in f.readlines():
        strs = line.split("\t")
        summary = strs[0]+"。"+strs[1]+"。"+strs[2]
        print(strs)
        df = df.append({"text":strs[3], "summary":summary},ignore_index=True)

df = df.sample(frac=1)

num = len(df)
df[:int(num*0.8)].to_csv("work/train.csv",sep="," ,index=False)
df[int(num*0.8):].to_csv("work/dev.csv",sep=",",index=False)