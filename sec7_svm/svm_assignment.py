# https://zhuanlan.zhihu.com/p/77750026   svm理论
from sklearn import  datasets,metrics,model_selection,linear_model,svm,neural_network,neighbors
import matplotlib.pyplot as plt
import numpy as np

class performance:

    fig,ax = plt.subplots(figsize=(16,8))

    def __init__(self,model_name,name_of_modelname,data):
        self.data = data
        self.model_name = model_name
        self.name_of_modelname=name_of_modelname
        self.X,self.y = data.data,data.target

    def figsave(self):
        self.fig.savefig(r'/media/baoquanlong/repository/OneDrive/Vscode_mypy/sec7_svm/accuracy-models_digitsdata')

    def plot(self):
        x_ticks=1
        x_ticks_name_pre=[]
        x_ticks_name = []
        for model,modelname in zip(self.model_name,self.name_of_modelname):
            score = model_selection.cross_val_score(model,self.X,self.y,cv=5)
            self.ax.scatter(np.linspace(x_ticks,x_ticks+0.2,len(score)),score)
            x_ticks_name_pre.append(x_ticks)
            x_ticks += 1.5
            x_ticks_name.append(modelname)
        self.ax.grid()
        self.ax.set_title('accuracy-models',fontsize=16)
        self.ax.set_ylabel('accuracy score')
        self.ax.set_xticks(x_ticks_name_pre)
        self.ax.set_xticklabels(x_ticks_name,fontsize=10)
        plt.xticks(rotation=-20)
        plt.show()
        # self.figsave()


model_name = [
    neighbors.KNeighborsClassifier(n_neighbors=3),
    neighbors.KNeighborsClassifier(n_neighbors=5),
    neighbors.KNeighborsClassifier(n_neighbors=10),
    linear_model.LinearRegression(),
    neural_network.MLPClassifier(hidden_layer_sizes=(100,)),
    neural_network.MLPClassifier(hidden_layer_sizes=(200,)),
    svm.SVC(kernel='rbf'),
    svm.SVC(kernel='linear')
]


name_of_modelname = [str(name) for name in model_name]




data  = datasets.load_digits()
figure = performance(model_name,name_of_modelname,data)


figure.plot()