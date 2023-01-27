# MSE的解析解的分析

- $$
  w=(X^TX)^{-1}X^TY
  $$
- 矩阵$X^TX$什么时候可逆，什么时候是奇异矩阵不可逆；
- 矩阵可逆，AB=BA=I，其中A和B为方阵且互为逆矩阵
- $$
  X^TX
  $$

  如果X为design matrix，假设其维度为m*n，则m为样本的个数，n为属性的个数（包含偏置，$X^TX$的结果为$n*n$的方阵*）。
- 如果上述的m>n,则样本的个数大于属性的个数
- 如果有两个样本有相同的属性值，但y不同，且样本数小于属性数字m<n，则$X^TX的$n方阵为奇异矩阵，因为$X^T$和 $X$的矩阵的秩均小于等于m，所以其矩阵的乘积的秩也小于等于m，因此n乘以n方阵的秩<n,为奇异阵
- 回归问题当参数的个数比样本的个数还要多的情况？解析解什么情况下无解
- 样本数量没有参数多时，函数能够完全拟合数据（记住了细节，过拟合），但是如果有冲突的数据（x相同但y不同），则会没有解
- 为什么有时候Ax=b是无解的。因为Ax可以看作A的列向量的线性组合，然后A不是[满秩矩阵](https://www.zhihu.com/search?q=%E6%BB%A1%E7%A7%A9%E7%9F%A9%E9%98%B5&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A118729056%7D)，所以A的列向量的线性组合构成了线性空间的某个子空间，而b这个向量没在这个子空间里面，所以就没有解了。其中A可以是数据属性，即可以为design matrix，x为参数，或者称为w，b为y值。

# Reference

- 1、[线性回归解析解 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/74157986)
- 2、[machine learning 之 多元线性回归 - Echo_fy - 博客园 (cnblogs.com)](https://www.cnblogs.com/echo-coding/p/8690649.html)
