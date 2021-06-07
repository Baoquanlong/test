# 1. 使用 knn 拟合 digits, 绘制 n_neighbors = 1-31 的 train_score 以及 test_score 的 cross_validation curve.
import joblib as jb
from sklearn.datasets import load_digits
from sklearn import metrics
model = jb.load('knnb3')
digits_data = load_digits()
X = digits_data.data
y = digits_data.target
model.fit(X,y)
y_pred = model.predict(X)
score = metrics.accuracy_score(y,y_pred)
print(score)

