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

# Reference

- 1、[线性回归解析解 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/74157986)
- 2、[machine learning 之 多元线性回归 - Echo_fy - 博客园 (cnblogs.com)](https://www.cnblogs.com/echo-coding/p/8690649.html)
