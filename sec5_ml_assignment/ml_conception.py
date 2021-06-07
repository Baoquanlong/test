from sklearn import  metrics,model_selection,datasets,neighbors
iris_data = datasets.load_iris()
X,y = iris_data.data,iris_data.target
# X_train,X_test,y_train,y_test = model_selection.train_test_split(X,y,test_size = 0.3)
# print(X_train,X_test,y_train,y_test)

#K折交叉检验（K-fold cross-validation)
#一般取k为5或10
# model = neighbors.KNeighborsClassifier(n_neighbors=5)
# score = model_selection.cross_val_score(model,X,y,cv=10,scoring='accuracy')
# print(score)
#超参数（Hyperparameters)
#人工设置的模型参数

#超参数决定模型的大框架
#超参数-验证结果的，即验证曲线（validatino curve)
## sklearn 绘制验证曲线（validation curve)

#  例如：对KNN分类的n_neighbors 参数绘制5折cross-validation验证曲线（本质就是对param_range的一个循环）
model = neighbors.KNeighborsClassifier()
train_scores,test_scores = model_selection.validation_curve(model,X,y,param_name = 'n_neighbors',param_range=range(1,10),cv = 3)
print(train_scores, test_scores,sep = '\n\n\n')