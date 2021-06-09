from sklearn import datasets,neighbors,metrics
# import numpy as np
import numpy as np
import matplotlib.pyplot as plt

data = datasets.load_iris()
# print(data.DESCR)
# print(data.keys())
# print(data.values())
X,y = data.data, data.target
# print(X.shape,y.shape)
# print(y)
model = neighbors.KNeighborsClassifier()
model.fit(X,y)
y_pred = model.predict(X)

## accuracy_score 代表准确率

acc = metrics.accuracy_score(y,y_pred)
# print(acc)
wrong_index = np.where(y!=y_pred)[0]
print(wrong_index)


# 混淆矩阵， 第 i 行 ，第j列表示y中属于第i种，y_pre中属于第j种

cm = metrics.confusion_matrix(y,y_pred)
print(cm)



