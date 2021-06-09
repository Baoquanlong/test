# 3. 自学神经网络的使用方法。写一个单层神经网络的模型学习 iris 数据。测试神经元个数对 performance 的影响。
# 已知多层感知机（Multiple Layers Perception, MLP）分类器的建模语句为
#     from sklearn import neural_network
#     model = neural_network.MLPClassifier( )
# 其中 model 的第一个选项
#     hidden_layer_sizes
# 代表需要多少层神经网络，每层几个神经元。例如
#     hidden_layer_sizes = (10, 15)
# 表示有两层神经元，个数分别为 10, 15

# 问题：
#     请用单层 layer 的 nerual network 拟合 iris 数据库；使用 validation_curve 画出 accuracy score 随 hidden_layer_sizes 的变化。看多少个 neuron 可以满足问题需求（达到高准确度的预测结果）
from sklearn import neural_network
from sklearn import datasets
from sklearn.model_selection import validation_curve
import matplotlib.pyplot as plt
model = neural_network.MLPClassifier(hidden_layer_sizes=...) 
fig = plt.figure(figsize=(16,12))
ax = fig.add_subplot(111)
data = datasets.load_iris()
X= data.data
y = data.target
train_score,test_score = validation_curve(model,X,y,param_name='hidden_layer_sizes', param_range=(range(1,100)), cv=5)
y1=[]
y2=[]
for score,index in zip(train_score,range(1,100)):
    y1.append(score.mean())
for score,index in zip(test_score,range(1,100)):
    y2.append(score.mean())

ax.plot(range(1,100),y1,label='train_score')

ax.plot(range(1,100),y2,label='test_score')
ax.legend(fontsize=16)
ax.grid()
plt.show()
ax.set_xlabel('the number of neurons')
ax.set_ylabel('accuracy score')
fig.savefig('neurons\' numbers and it\'s accuracy.png')


