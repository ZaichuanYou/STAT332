import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import os
from sklearn.preprocessing import StandardScaler


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
        stdsc = StandardScaler() 
        X_std = stdsc.fit_transform(data)
        cov_mat =np.cov(X_std.T)
        plt.figure(figsize=(10,10))
        sns.set(font_scale=1.5)
        hm = sns.heatmap(cov_mat,
                        cbar=True,
                        annot=True,
                        square=True,
                        fmt='.2f',
                        annot_kws={'size': 12},
                        cmap='coolwarm',                 
                        yticklabels=data.columns,
                        xticklabels=data.columns)
        plt.title('Covariance matrix showing correlation coefficients', size = 18)
        plt.tight_layout()
        plt.savefig(fname=f"{file[:-4]}_Covariance.png")
        #dataset[file[-3:]] = data.describe()
