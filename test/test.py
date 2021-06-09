# from sklearn import datasets,model_selection,linear_model,neural_network,neighbors,metrics
# import numpy as np 
# import matplotlib.pyplot as plt
# data = datasets.load_iris()
# X,y = data.data,data.target

# model = linear_model.LogisticRegression()

# model.fit(X,y)
# y_pred = model.predict(X)
# score  = metrics.accuracy_score(y,y_pred)
# print(score)
# print(metrics.confusion_matrix(y,y_pred))


# score  = model_selection.cross_val_score(model,X,y,cv=5)
# print(score)
from sklearn import  datasets,metrics,model_selection,linear_model,svm,neural_network,neighbors
import matplotlib.pyplot as plt
import numpy as np



x = datasets.load_digits()

X,y = x.data,x.target
np.set_printoptions(threshold=np.inf)
print(X,y,sep='\n')

