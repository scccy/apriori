import pandas as pd
import numpy as np
import re
from datetime import datetime


df = pd.read_excel("地震.xls")
df['newdate'] = df['日期'].map(lambda x: (int(x[5:7])+1)//2 + (int(x[:4])-2008)*6)
df["纬度"] = (df["纬度(°)"] + 0.5).apply(np.round).astype(str)
df["经度"] = (df["经度(°)"] + 0.5).apply(np.round).astype(str)
df["fhuzhu"] = "*"
df["location"] = df["经度"] + df["fhuzhu"] + df["纬度"]
df = df.set_index(df['newdate'])
df = df["参考地名"]
df = pd.DataFrame(df)
df = df.groupby(["newdate"])
l = []
for x in df:
    train_data = np.array(x[1])
    train_x_list = train_data.tolist()
    l.append(train_x_list)
print(l)


# for n in range(len(df["经度"])):
#     print(df["经度"][n] + add() + df["纬度"][n])


