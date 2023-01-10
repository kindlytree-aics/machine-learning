# Taylor\_expansion\_Multi\_Variables\_Functions\_extremum

* [参考资料1](https://blog.csdn.net/u013498583/article/details/79580733)
* [参考资料2](https://blog.csdn.net/baimafujinji/article/details/51167852)

## 多元函数极值

我们是如何处理一元函数求极值问题的。例如， `$\f(x)=x^2$`，我们会先求一阶导数，即f′(x)=2x，根据费马定理极值点处的一阶导数一定等于 0。但这仅是一个必要条件，而非充分条件。对于 `$f(x)=x^2$`来说，函数的确在一阶导数为零的点取得了极值，但是对于 `$f(x)=x^3$`来说，显然只检查一阶导数是不足以下定论的。

这时我们需要再求一次导，如果二阶导数 `${f}''<0$`，那么说明函数在该点取得局部极大值；如果二阶导数 `${f}''>0$`，则说明函数在该点取得局部极小值；如果 `${f}''=0$`，则结果仍然是不确定的，我们就不得不再通过其他方式来确定函数的极值性。

如果要在多元函数中求极值点，方法与此类似。作为一个示例，不妨用一个三元函数 f=f(x,y,z) 来作为示例。首先要对函数中的每个变量分别求偏导数，这会告诉我们该函数的极值点可能出现在哪里。即

```math
\frac{\partial f}{\partial x} = 0

\frac{\partial f}{\partial y} = 0

\frac{\partial f}{\partial z} = 0
```

接下来，要继续求二阶导数，此时包含混合偏导数的情况一共有 9 个，如果用矩阵形式来表示的话就得到

```math
\begin{bmatrix}
    \frac{\partial^2 f}{\partial x \partial x} &\frac{\partial^2 f}{\partial x \partial y}  & \frac{\partial^2 f}{\partial x \partial z}\\ 
     \frac{\partial^2 f}{\partial y \partial x}&\frac{\partial^2 f}{\partial y \partial y}  &\frac{\partial^2 f}{\partial y \partial z} \\ 
    \frac{\partial^2 f}{\partial z \partial x} &\frac{\partial^2 f}{\partial z \partial y}  &\frac{\partial^2 f}{\partial z \partial z} 
    \end{bmatrix}
```

这个矩阵就称为Hessian矩阵。当然上面所给出的仅仅是一个三阶的Hessian矩阵。稍作扩展，我们可以对一个在定义域内二阶连续可导的实值多元函数 f(x1,x2,⋯,xn) 定义其Hessian矩阵HH如下

```math
 \bigtriangledown_x^2f(x) \in\mathbb{R}^{n\times n}=\begin{bmatrix}
    \frac{\partial^2 f}{\partial x_{1}^2} &...  & \frac{\partial^2 f}{\partial x_{1} x_n}\\ 
     ...&...  &... \\ 
    \frac{\partial^2 f}{\partial x_{n}x_1} &...  &\frac{\partial^2 f}{\partial x_{n}^2} 
    \end{bmatrix}
```

当一元函数的二阶导数等于0时，我们并不能确定函数在该点的极值性。类似地，面对Hessian矩阵，仍然存在无法断定多元函数极值性的的情况，即当Hessian矩阵的行列式为0时，我们无法确定函数是否能取得极值。甚至我们可能会得到一个鞍点，也就是一个既非极大值也非极小值的的点。

## 泰勒展开式与Hessian矩阵

设一元函数 f(x) 在包含点x0的开区间 (a,b) 内具有 n+1 阶导数，则当 x∈(a,b) 时，有

```math
f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{{f}''(x_0)}{2!}(x-x_0)^2

+...+\frac{f^n(x_0)}{n!}(x-x_0)^n + R_n(x)
```

其中

```math
R_n(x)=\frac{f^{n+1}(\xi)}{(n+1)!}(x-x_0)^{(n+1)}
```

并且，ξ 在 x和 x0之间，这被称作是拉格朗日余项。上式被称为 f(x)的 n 阶泰勒公式。在不需要余项的精确表达式时，Rn(x) 可以记作 `$o[(x-x_0)^n]$`，这被称为是皮亚诺余项。

现在我们把上面这个结论稍微做一下推广，从而给出二元函数的泰勒公式。设二元函数 z=f(x,y) 在点 (x0,y0) 的某一邻域内连续且有直到 n+1 阶的连续偏导数，则有

```math
f(x,y)= f(x_0,y_0)+[(x-x_0)\frac{\partial}{\partial x}+(y-y_0)\frac{\partial}{\partial y}]f(x_0,y_0)


+\frac{1}{2!}[(x-x_0)\frac{\partial}{\partial x}+(y-y_0)\frac{\partial}{\partial y}]^2f(x_0,y_0)

+\frac{1}{n!}[(x-x_0)\frac{\partial}{\partial x}+(y-y_0)\frac{\partial}{\partial y}]^nf(x_0,y_0)

```

一般地，记号

```math
[(x-x_0)\frac{\partial}{\partial x}+(y-y_0)\frac{\partial}{\partial y}]^mf(x_0,y_0)
```

表示

```math
\sum_{p=0}^mC_m^p(x-x_0)^p(y-y_0)^{(m-p)}\frac{\partial ^m}{\partial x^p \partial  y^{(m-p)}}f(x_0,y_0)
```

特别低，对于一个多维向量 X, 以及在点 X0 的邻域内有连续二阶偏导数的多元函数 f(X) ，可以写出该函数在点 X0 处的（二阶）泰勒展开式

```math
f(X)=f(X_0)+(X-X_0)^T\bigtriangledown f(X_0)

+\frac{1}{2!}(X-X_0)^T\bigtriangledown ^2f(X_0)(X-X0)^2+o(\left \|X-X_0 \right \|^2)
```

其中，`$o \left \| X - X_0 \right \| ^2)$`是高阶无穷小表示的皮亚诺余项。而 `$\bigtriangledown^2f(X_0)$` 显然就是一个Hessian矩阵。

## 个人理解

为什么泰勒展开与多项式有关联，可以理解为一般的函数都是多元多项式函数的逼近。不一定，也有指数形式的表示方法，如e^x
泰勒展开的就是在函数一个特定的点附近用多项式函数去逼近原函数
