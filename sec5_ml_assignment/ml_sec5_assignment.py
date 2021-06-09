# 1. 使用 knn 拟合 digits, 绘制 n_neighbors = 1-31 的 train_score 以及 test_score 的 cross_validation curve.

from sklearn import datasets,metrics,model_selection,neighbors
import numpy as np
import matplotlib.pyplot as plt
digits_data = datasets.load_digits()
X = digits_data.data
y = digits_data.target
model = neighbors.KNeighborsClassifier()
train_score,test_score = model_selection.validation_curve(model,X,y,param_name='n_neighbors',cv=10,param_range=range(1,31))
X = range(1,31)
y1 = [score.mean() for score in train_score ]
y2 = [score.mean() for score in test_score]
fig = plt.figure(figsize=(16,12))
ax = fig.add_subplot()
ax.plot(X,y1,label='train_score',ls = '--')
ax.plot(X,y2,label='test_score',ls = ':')
ax.legend()
plt.show()