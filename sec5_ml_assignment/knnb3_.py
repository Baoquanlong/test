from sklearn import neighbors
import  joblib as jb
model = neighbors.KNeighborsClassifier(n_neighbors=3)
jb.dump(model,'knnb3')
