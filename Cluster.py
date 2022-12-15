import pandas as pd
import numpy as np

data = pd.read_csv("C:\\Users\\21995\\Desktop\\Math\\Stat332\\Final project\\STAT332\\Result.csv", index_col=0)

result = {}
for a in data.columns:
    data.sort_values(by=[a], inplace=True)

    result[a] = data[a][1:11]

for a in result:
    print(a, result[a].index.tolist())