# FAQ

## Environment

- cannot import name 'DecisionBoundaryDisplay' from 'sklearn.inspection'
  - https://blog.csdn.net/m0_56448912/article/details/127803698
  - 手动安装scikit_learn-1.2.dev0以上版本，[下载链接](https://pypi.anaconda.org/scipy-wheels-nightly/simple/scikit-learn/)

## General

* 机器学习的分类系统：[机器学习的分类有哪些？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/577022227/answer/2844669853)

## Classification and Regression

* 分类和回归问题的汇总总结
  * 线性回归的问题有哪些？[线性回归模型有哪些？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/579151443/answer/2858496953)
  * 分类和回归问题的关系 [回归问题 广义上是不是也是 分类问题？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/576625500/answer/2828780085)
  * softmax和sigmoid对于分类问题的对比及效果可视化：[RetinaNet 为什么用sigmoid? - 知乎 (zhihu.com)](https://www.zhihu.com/question/576525745/answer/2837596942)
  * sigmoid为什么能代表概率：[通过逻辑回归的 sigmoid 函数把线性回归转化到 [0, 1] 之间，这个值为什么可以代表概率？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/41647192/answer/2854827224)

### 线性分类器

* SVM算法的基本思路和流程：[支持向量机（SVM）是什么意思？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/21094489/answer/2867702150)

## Cost Function（objective fuction，loss，error surface）

* 分类中为什么用交叉熵损失函数：[分类问题中为什么用交叉熵代替 MSE？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/562388855/answer/2731545250)
* 交叉熵和KL散度的关系：[为什么交叉熵和 KL 散度在作为损失函数时是近似相等的？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/559808909/answer/2717475457)
* 为什么逻辑回归不用LMS：[为什么逻辑回归不使用平方损失？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/559605858/answer/2716269977)
* 回归问题与最小二乘：[在进行线性回归时，为什么最小二乘法是最优方法？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/24095027/answer/2711358112)
* 分类问题与交叉熵损失函数：[分类问题为什么使用交叉熵损失函数？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/558686060/answer/2711219151)
* 模型参数正则化（规范化）：[如何理解机器学习中的正则化？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/555430093/answer/2691135856)
* 余弦距离与欧式距离：[计算机视觉为什么要使用余弦距离而不是欧式距离？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/554734182/answer/2690916458)
* 信息量、熵、KL散度、交叉熵的定义：[kl 散度和交叉熵的区别有哪些？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/579887503/answer/2862869448)

## Quality metric

* 分类模型的性能度量：[Python机器学习如何正确评估分类模型的准确性？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/573591611/answer/2825268164)
* 混淆矩阵的画法：[深度学习中如何画一个具有40个类的混淆矩阵？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/569173057/answer/2817684250)
* AP和mAP以及AUC，precision/recall的相关定义：[小样本分类任务为什么都使用accuracy作为评价指标？为何都不使用 P R F1？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/577905496/answer/2861493787)
* 目标检测指标：[如何解读目标检测指标？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/577375183/answer/2862818273)

## Neural Network

### General

- 反向传播算法：[Unsupervised Feature Learning and Deep Learning Tutorial (stanford.edu)](http://ufldl.stanford.edu/tutorial/supervised/MultiLayerNeuralNetworks/)
- 反向传播算法的复合函数的链式规则：[pytorch 如何根据底层梯度计算上层梯度? - 知乎 (zhihu.com)](https://www.zhihu.com/question/568604728/answer/2848515612)
- 神经网络的学习路线：[入门机器学习可以直接学神经网络吗？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/476567256/answer/2852713847)

* 神经网络拟合函数的几何直观示例：[为什么神经网络能拟合出任何函数？ - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/38229942)
* 神经网络为什么可以拟合任意函数：[神经网络为什么可以（理论上）拟合任何函数？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/268384579/answer/484612032)
* [为何深度学习采用神经网络这种层次网络结构？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/566839873/answer/2836531708)
* 神经网络的可解释性：
  * [函数拟合的视角](http://staff.ustc.edu.cn/~lgliu/Resources/DL/What_is_DeepLearning.html)
  * [(61条消息) 如何理解卷积神经网络（An Intuitive Explanation of Convolutional Neural Networks）_开曼Cayman的博客-CSDN博客](https://blog.csdn.net/qq_44490994/article/details/118724839)
  * [神经网络功能可视化](http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/)

### CNN

* CNN的特性：[如何解读 CNN 和传统神经网络的区别？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/575461202/answer/2825845986)
* 如何理解CNN中的通道：[如何理解 cnn 中的通道？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/575460913/answer/2824160988)
* 神经网络结构可视化：[神经网络的结构图的绘制有什么合适的软件推荐？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/574891317/answer/2817678890)
* 1*1卷积核的作用：[卷积神经网络中的 1x1 卷积核有什么作用？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/555176370/answer/2710720657)

### RNN

* LSTM网络的相关学习路线：[研一刚入学，从未接触过神经网络，python也是才开始学，现在导师要我做LSTM，我应该去学什么？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/492854858/answer/2776129718)
* LSTM的计算方式：[(1 条消息) LSTM可以提取时间序列特征，具体的实现过程的细节是怎么样的。? - 知乎 (zhihu.com)](https://www.zhihu.com/question/575080897/answer/2853931860)

### Transformer

* ViT

## Reinforcement Learning

* MDP中S，A的相关概念：[强化学习中的S×A什么意思啊？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/555097104/answer/2697797038)

## Feature Engineering(Data augumentation)

* 如何进行数据归一化：[python 如何实现归一化？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/575576083/answer/2823859483)
* 特征归一化的作用：[特征不归一化有什么危害？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/559345965/answer/2720599228)
* PCA的几何解释：[PCA降维后如何与原来的对应，哪几个特征对应降维后的特征？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/571894023/answer/2820040847)
* 非正态分布数据变换：
  * [非正态分布的数据怎么转换为正态分布？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/372019236/answer/2235639734)
  * 为什么要做正态分布的变换以及具体有哪些方法：[(1 条消息) 如何计算正态分布的众数？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/576588835/answer/2830362657)
* 为什么要对数据进行降维和压缩：[为什么要对数据做降维和压缩？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/557920195/answer/2703781485)
* 机器学习是如何做数据预处理的： [知乎问题](https://www.zhihu.com/question/574928730/answer/2833012100)
* Tencrop数据增强：[Pytorch中的transforms.TenCrop - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/433165698)\
* 核方法
  - 核方法的示例以及为什么高斯核映射到无穷维度：https://www.zhihu.com/question/40049373/answer/2872938370


## Clustering Algorithm

* KMeans算法： [如何解读机器学习的聚类分析 Kmeans 算法？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/574234701/answer/2817134561)
* Hierarchical Clustering方法的示例：[1、图1的聚类结果及含义？2、如果将聚类结果分为5类，结果是？3、最终聚类结果设置为多少类合适？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/576568363/answer/2828887729)
* 无监督学习怎么做超参选择： [无监督学习怎么做超参选择？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/573848676/answer/2812123529)
  * 可以再加一个DBSCAN算法的超参选择的说明
* 目前主要流行的聚类算法有哪些：[目前流行和先进的聚类算法有哪些? - 知乎 (zhihu.com)](https://www.zhihu.com/question/494753171/answer/2861340070)

## Trees

* Bootstrap采样方法：[统计学中，Bootstrap的意义是什么？从观测样本中重抽样比直接使用观测样本好在哪里？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/576318634/answer/2827057355)
* 决策树有哪些分类：[数据挖掘干货总结（九）-- 决策树分类 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/502595209)
* 随机森林的evaluation：[随机森林训练集能等于测试集吗? - 知乎 (zhihu.com)](https://www.zhihu.com/question/573482490/answer/2836356780)

## Optimization Algorithms

* 怎么解决梯度爆炸问题： [如何确定是否出现神经网络梯度爆炸？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/573856383/answer/2828372514)
* 正则化项（规范化项，regularization）：[L1范数和L2范数有什么区别？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/574589430/answer/2849557497)
* 学习率和损失函数的关系：[在损失函数前面乘以0.5，是不是相当于学习率减半？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/576927319/answer/2856105458)
