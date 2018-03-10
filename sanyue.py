import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel("/Users/shici/Desktop/qk/三月第一周.xls")
df["all_time"] = df["访问次数"] * df["平均访问时长"]
timedf = df[["类别", "all_time"]]
timedf = timedf.groupby(["类别"], as_index=False).sum()
x = timedf["类别"]
y = timedf["all_time"]
plt.pie(x=y)
plt.show()
print(timedf)