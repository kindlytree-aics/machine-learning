## Machine Learning experiments code

### 开发环境准备：

- IDE：https://code.visualstudio.com/
  - vscode相关插件安装：`jupyter`,`python`
- python环境安装
  - 下载镜像链接： https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
  - 选择最近时间的版本即可
  - 安装完成后一般当前的 `base` env已经够用,可以根据需要去conda install相关的机器学习库

### 数据集

* IRIS  [[download from kaggle]()]([Iris-Dataset - KNN /KNR Model | Kaggle](https://www.kaggle.com/code/sundarikonar/iris-dataset-knn-knr-model/data?select=IRIS.csv))

### 算法集汇总

| Topic| Key notes| code or comments |
| ------- |------------| -------------- |
| [Linear_Regression](http://note.youdao.com/noteshare?id=e3d052b17e33e6a1d9c45b7f8a90d86c/) | 1. The errors between labels and predictions follow normal distribution `<br>`2. The samples joint probability also follows normal distribution | [code](https://github.com/kindlytree/ai/blob/master/samples/ml/linear_regression.ipynb)|
|[Logistic_Regression](http://note.youdao.com/noteshare?id=a62bb63c6a049ce5e0cdc8abfe8ba3fd)| 1. The sample probability follows Bernoulli distribution `<br>`2. The logistic function and its derivative's property `<br>`3. Maximize the log likelihood equals maximization of liklihood | [code](https://github.com/kindlytree/ai/blob/master/samples/ml/logistic_regression.ipynb)|
| [Newton's Method](http://note.youdao.com/noteshare?id=57e9b323d4ae19c215c421fcac32b638) | 1. The second order of derivative  Hessian matrix's property.`<br>`2. Multi variable Taylor expansion| [code](https://github.com/kindlytree/ai/blob/master/samples/ml/newton_method.ipynb)|
| [Generalized Linear Models](http://note.youdao.com/noteshare?id=b814a849cf4752746518d4f63ef0d79c)| 1. exponential family distributions.`<br>` 2. Construct GLM according to exponential family distributions|| [softmax regression code](https://github.com/kindlytree/ai/blob/master/samples/ml/softmax_regression.ipynb)|||
| [Generative Learning algorithms](http://note.youdao.com/noteshare?id=179205e43731362a960bf52236599fa9)| 1.Different from discriminative learning algorithms|||
| [Gaussian discriminant analysis](http://note.youdao.com/noteshare?id=7a34e72665581d2d379ac9a9cdebd0ce)| 1. The multivariate normal distribution.`<br>` 2.  GDA makes stronger modeling assumptions than logistic regression.||
| [Naive Bayes](http://note.youdao.com/noteshare?id=0ca8c256d4dcb349dd32b155594426ea)  | 1. features are discrete-valued.`<br>` 2. Features are conditionally independent given y||
| [Kernel Methods](http://note.youdao.com/noteshare?id=5de8fb8eaa20e53517671b7d706bd6c6)| 1. Feature mapping.||
| [SVM](http://note.youdao.com/noteshare?id=04eb156cc9eb0137844a2a381f3f1668)| 1. Functional and geometric margins.`<br>` 2. The optimal margin classifier. `<br>`3. Lagrange duality|
| [Learning Theory](https://note.youdao.com/ynoteshare1/index.html?id=85c244e8f122dc38842208d7c6f0bfe4&type=note) ||
|Adaboost| 1. Weak models `<br>` 2. Additive models. `<br>` 3. exponential loss function.| [算法原理及推导](https://www.cnblogs.com/liuwu265/p/4692347.html)|
| [Decision Tree](https://blog.csdn.net/jiaoyangwm/article/details/79525237)| 1. Information Entropy.<br> 2. Information gain ||
| [Random Forest](https://blog.csdn.net/weixin_41940752/article/details/98717868)| 1. Bagging method.`<br>` 2. out of bag error |
| Tree Boosting| 1. Additive models.`<br>` 2. forward step method||
| [CART回归树](http://note.youdao.com/noteshare?id=922bd61daea279fed55ac3359c4f9cd3)  `<br>` GBDT `<br>` [XGBoost](https://blog.csdn.net/u014411730/article/details/78796890) `<br>` LightGBM ||
PGM| [HMM 的通俗解释](https://zhuanlan.zhihu.com/p/25963621) `<br>` MRF||
| Neural Networks| 1.Multi layer perception machine.`<br>` 2. [Back Propagation](http://ufldl.stanford.edu/tutorial/supervised/MultiLayerNeuralNetworks/)||
| The k-means clustering algorithm| ||
| Mixtures of Gaussians and the EM algorithm| 1. Jensen’s inequality.`<br>` 2. latent random variables|||
| [GMM](http://note.youdao.com/noteshare?id=611be89d2eeb9c40c79bc5f5e86bc022) `<br>` [The EM algorithm](https://www.cnblogs.com/bigmoyan/p/4550375.html)|||
| Factor analysis|| |
| Principal components analysis| covariance| [PCA](https://blog.csdn.net/program_developer/article/details/80632779)||
| Independent Components Analysis|||
| Reinforcement Learning and Control| [MDP](https://blog.csdn.net/unixtch/article/details/78922936)||

### TODO

- 基于Numpy实现机器学习算法
- 算法视频内容优化

### 更多内容：

- 视频内容分享： https://space.bilibili.com/505620745/channel/seriesdetail?sid=2595000
- 抖音账号：kindlytree_aics

### Reference

- https://zhuanlan.zhihu.com/p/345444342
- https://github.com/ddbourgin/numpy-ml
- https://machinelearningmastery.com/start-here/
