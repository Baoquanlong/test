# ### 练习题：测试目前学到的 Classifier 的 performance。

#     对以下几种模型：
#         n_neighbor = 3, 5, 10 的 knn
#         logestic 回归
#         单层 100 个 neuron 的 neural_network
#         单层 200 个 neuron 的 neural_network
        
    
#     测试它们以下数据集的表现：
#         iris 
#         digits
        
#     请做到：
    
#         打印 model_selection.cross_val_score() 结果
        
#         把 validation 的结果作图，形象地演示（如，横坐表示不同的模型，纵坐标为 score，就像我ppt最后一页所示图）

from sklearn import model_selection,datasets,neighbors,neural_network,linear_model,metrics
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
fig,ax = plt.subplots(figsize = (16,8))
data = datasets.load_iris()
X,y =data.data,data.target

model_names = [
    neighbors.KNeighborsClassifier(n_neighbors=3),
    neighbors.KNeighborsClassifier(n_neighbors=5),
    neighbors.KNeighborsClassifier(n_neighbors=10),
    linear_model.LinearRegression(),
    neural_network.MLPClassifier(hidden_layer_sizes=(100,)),
    neural_network.MLPClassifier(hidden_layer_sizes=(200,))
]
x_modelsname = []
x_modelspresign = []
x_ticks = 1
model_model_name= ['knn_3','knn_5','knn_10','LR', 'mlp_100','mlp_200']
for model,model_name_ in zip(model_names,model_model_name):
    score = model_selection.cross_val_score(model,X,y,cv=5)
    ax.scatter(np.linspace(x_ticks,x_ticks+0.2,len(score)),score)
    x_modelspresign.append(x_ticks)
    x_modelsname.append(model_name_)
    x_ticks += 1
ax.set_xticks(x_modelspresign)
ax.set_xticklabels(x_modelsname,fontsize=14)
ax.set_title('model_name')
ax.set_ylabel('accuracy socre',fontsize= 16)
ax.grid()
plt.show()

fig.savefig('model_name--accuracy score')


