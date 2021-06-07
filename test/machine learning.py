import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import pandas as pd
filename= datasets.load_iris().filename
# print(filename)
pddata = pd.read_csv(filename)
pd.set_option('display.max_rows', 200)

pddata.columns= ['sepal length','sepal width','petal length','petal width','Species']
# print(pddata)
# print(pddata.describe())

# 下面的pairpot对数据给定的“列”两两组合画散点图，按照“Species”列进行分类

rlt = sns.pairplot(pddata,vars = ['sepal length', 'sepal width', 'petal length', 'petal width' ],hue='Species')
# plt.show()
fig,axs=plt.subplots(2,2,figsize=(8,8))
sns.boxplot(pddata['Species'],pddata['sepal length'],ax= axs[0,0])
sns.boxplot(pddata['Species'],pddata['sepal width'],ax= axs[0,1])
sns.boxplot(pddata['Species'],pddata['petal length'],ax= axs[1,0])
sns.boxplot(pddata['Species'],pddata['petal width'],ax= axs[1,1])
plt.show()