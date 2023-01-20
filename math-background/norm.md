# 范数

## 定义

一个向量的 norm 就是将该向量 **投影到 [0, ) 范围内的值** ，其中 0 值只有零向量的 norm 取到。看到这样的一个范围，相信大家就能想到其与现实中距离的类比，于是在机器学习中 norm 也就总被拿来表示 **距离关系** ：根据怎样怎样的范数，这两个向量有多远。上面这个怎样怎样也就是范数种类，通常我们称为p-norm，严格定义是：

$$
||x||_p=(\sum_{i=1}^n|x_i|^p)^{1/p}
$$

其中，当p 取 1 时被称为 1-norm，也就是提到的 L1-norm，同理 L2-norm 可得

## FAQ

- L1范数和L2范数有什么区别：[(1 封私信) L1范数和L2范数有什么区别？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/574589430/answer/2815476448)

  - L1的等高线为棱形（以原点为坐标的水平正方形旋转45度）
  - L2的等高线为以圆点为中心的圆
  - [L1范数和L2范数有什么区别？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/574589430/answer/2849557497)
- L0 norm

  - 严格说，L0不是严格的范数，0的根的定义不好理解
- - 元素中非零元素的个数：is a total number of non-zero elements in a vector [（转）几种范数的解释 l0-Norm, l1-Norm, l2-Norm, … , l-infinity Norm - AHU-WangXiao - 博客园 (cnblogs.com)](https://www.cnblogs.com/wangxiaocvpr/p/5933512.html)
  - 

# Reference

- https://www.jianshu.com/p/6c31e8c27e8e
