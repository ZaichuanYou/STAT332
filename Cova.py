import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import os


path = "C:/Users/21995/Desktop/量化投资/CTA/CTA/data"
os.chdir(path)
  

dataset = pd.DataFrame()
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if not file.endswith("adj.csv"):
        file_path = f"{path}/{file}"
  
        data = pd.read_csv(file_path)
        data = data.drop(columns=["time", "code", "price_adjust_factor", "bid1", "ask1", "bidvol1", "askvol1", "open", "high", "low"])
        sns.pairplot(data, size=2.0)
        plt.savefig(fname=f"{file[:-4]}_scattered.png")
        #dataset[file[-3:]] = data.describe()

