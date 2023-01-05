# FAQ

## Environment

- cannot import name 'DecisionBoundaryDisplay' from 'sklearn.inspection'
  - https://blog.csdn.net/m0_56448912/article/details/127803698
  - 手动安装scikit_learn-1.2.dev0以上版本，[下载链接](https://pypi.anaconda.org/scipy-wheels-nightly/simple/scikit-learn/)

## Classification and Regression

* 分类和回归问题的汇总总结
  * 问题1，分类和回归问题的关系 [回归问题 广义上是不是也是 分类问题？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/576625500/answer/2828780085)
  * 

## Cost Function（objective fuction，loss）

* 分类中为什么用交叉熵损失函数：[分类问题中为什么用交叉熵代替 MSE？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/562388855/answer/2731545250)
* 交叉熵和KL散度的关系：[为什么交叉熵和 KL 散度在作为损失函数时是近似相等的？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/559808909/answer/2717475457)
* 为什么逻辑回归不用LMS：[为什么逻辑回归不使用平方损失？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/559605858/answer/2716269977)
* 回归问题与最小二乘：[在进行线性回归时，为什么最小二乘法是最优方法？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/24095027/answer/2711358112)
* 分类问题与交叉熵损失函数：[分类问题为什么使用交叉熵损失函数？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/558686060/answer/2711219151)
* 模型参数正则化（规范化）：[如何理解机器学习中的正则化？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/555430093/answer/2691135856)
* 余弦距离与欧式距离：[计算机视觉为什么要使用余弦距离而不是欧式距离？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/554734182/answer/2690916458)

## Quality metric

* 分类模型的性能度量：[Python机器学习如何正确评估分类模型的准确性？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/573591611/answer/2825268164)
* 混淆矩阵的画法：[深度学习中如何画一个具有40个类的混淆矩阵？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/569173057/answer/2817684250)

## Neural Network

### General

* 神经网络拟合函数的几何直观示例：[为什么神经网络能拟合出任何函数？ - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/38229942)
* 神经网络为什么可以拟合任意函数：[神经网络为什么可以（理论上）拟合任何函数？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/268384579/answer/484612032)

### CNN

* CNN的特性：[如何解读 CNN 和传统神经网络的区别？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/575461202/answer/2825845986)
* 如何理解CNN中的通道：[如何理解 cnn 中的通道？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/575460913/answer/2824160988)
* 神经网络结构可视化：[神经网络的结构图的绘制有什么合适的软件推荐？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/574891317/answer/2817678890)
* 1*1卷积核的作用：[卷积神经网络中的 1x1 卷积核有什么作用？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/555176370/answer/2710720657)

### Transformer

* ViT

## Reinforcement Learning

* MDP中S，A的相关概念：[强化学习中的S×A什么意思啊？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/555097104/answer/2697797038)

## Feature Engineering

* 如何进行数据归一化：[python 如何实现归一化？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/575576083/answer/2823859483)
* 特征归一化的作用：[特征不归一化有什么危害？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/559345965/answer/2720599228)
* PCA的几何解释：[PCA降维后如何与原来的对应，哪几个特征对应降维后的特征？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/571894023/answer/2820040847)
* 非正态分布数据变换：
  * [非正态分布的数据怎么转换为正态分布？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/372019236/answer/2235639734)
  * 为什么要做正态分布的变换以及具体有哪些方法：[(1 条消息) 如何计算正态分布的众数？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/576588835/answer/2830362657)
* 为什么要对数据进行降维和压缩：[为什么要对数据做降维和压缩？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/557920195/answer/2703781485)

## Clustering Algorithm

* KMeans算法： [如何解读机器学习的聚类分析 Kmeans 算法？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/574234701/answer/2817134561)
* Hierarchical Clustering方法的示例：[1、图1的聚类结果及含义？2、如果将聚类结果分为5类，结果是？3、最终聚类结果设置为多少类合适？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/576568363/answer/2828887729)
* 无监督学习怎么做超参选择： [无监督学习怎么做超参选择？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/573848676/answer/2812123529)
  * 可以再加一个DBSCAN算法的超参选择的说明

## Trees

* Bootstrap采样方法：[统计学中，Bootstrap的意义是什么？从观测样本中重抽样比直接使用观测样本好在哪里？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/576318634/answer/2827057355)
* 决策树有哪些分类：[数据挖掘干货总结（九）-- 决策树分类 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/502595209)

## Optimization Algorithms

* 怎么解决梯度爆炸问题： [如何确定是否出现神经网络梯度爆炸？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/573856383/answer/2828372514)
