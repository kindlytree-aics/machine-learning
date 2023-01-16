## 仿射变换

AffineTransform 类表示 2D [仿射变换](https://baike.baidu.com/item/%E4%BB%BF%E5%B0%84%E5%8F%98%E6%8D%A2/4289056?fromModule=lemma_inlink)，它执行从 2D 坐标到其他 2D 坐标的线性映射，保留了线的“直线性”和“平行性”。可以使用一系列[平移](https://baike.baidu.com/item/%E5%B9%B3%E7%A7%BB/2376933?fromModule=lemma_inlink) (translation)、缩放 (scale)、翻转 (flip)、旋转 (rotation) 和[错切](https://baike.baidu.com/item/%E9%94%99%E5%88%87/7024094?fromModule=lemma_inlink) (shear) 来构造仿射变换。

* shear  空间线性变换之一 [剪切变换_百度百科 (baidu.com)](https://baike.baidu.com/item/%E5%89%AA%E5%88%87%E5%8F%98%E6%8D%A2/4969513?fr=aladdin)
* 平移变换不是一个线性变换： [平移变换_百度百科 (baidu.com)](https://baike.baidu.com/item/%E5%B9%B3%E7%A7%BB%E5%8F%98%E6%8D%A2/18877462?fr=aladdin)
* 线性变换的特点

  * 变换前是直线，变换后依然是直线；
  * 直线比例保持不变
  * 变换前是原点，变换后依然是原点
* 常见的线性变换有

  * 旋转
  * 图像拉伸
  * 缩放
  * 投影
  * 镜像
  * 错切(shear)
