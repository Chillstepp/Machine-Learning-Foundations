---
title: 机器学习基石Ch5：Training VS Testing
date: 2021-01-12 10:54:46
tags: 机器学习
---



# Ch5：Training VS Testing

## Recap and preview 回顾

![image-20210111230212927](https://i.loli.net/2021/01/11/TRGceul2MPAOfa8.png)

上图是我们所希望做到的。



![image-20210111230757095](https://i.loli.net/2021/01/11/824psLJKdMtUC1R.png)

回到第四章问题：如果$M$变为无限大，怎么办呢？



我们所想做到的：

![image-20210111231128141](https://i.loli.net/2021/01/11/JvQOEP9WMVFmac5.png)

- 建立一种有限的量替代M
- 证明M为无限时学习的可行性
- 这个$m_H$的选择会帮助我们更好的学习hypothesis的选择



## Effective Number Of Lines

![image-20210111232329199](https://i.loli.net/2021/01/11/t8ViHIj42wYGxWs.png)

我们在以上不等式 用了union bound，但是M无穷大时出了问题。



------

![image-20210111232659335](https://i.loli.net/2021/01/11/Tx3bD7jgk8hlLzV.png)

我们看上图可知，一般相近的两个hypothesis的结果是没有什么太大区别的，因此多个h之间很大一部分都是重叠的（如上图：三个圆圈有重叠），而我们的union bound是把他们直接相加的，造成了over-estimating（过度估计）。

------

![image-20210111233228291](https://i.loli.net/2021/01/11/zqcioRpItn8mHuM.png)

我们来考虑一下上图有几个h，即有几种线可以划分出不同的结果。

不难看出是四种分类结果。

![image-20210111233324728](https://i.loli.net/2021/01/11/7WiUI2ey6bLAYEH.png)

同理，若有三个点，则有8种。那么规律是$2^n$吗？



我们观察下图:

![image-20210111233427807](https://i.loli.net/2021/01/12/WkPceVDdanXIgjO.png)

上图我们可以发现，粉色花圈的两个不可能用一条线做到，因此只有6种.



------



![image-20210111233811256](https://i.loli.net/2021/01/11/suFIYN6xyldzO4Z.png)

对于四个点，其实最多只有14种方式。



![image-20210111233858816](https://i.loli.net/2021/01/11/UgYGB3VDnef7tjp.png)

我们猜测：无限多的线可以划分为有限的种类。同种类的线就不需要union bound加在一起了。

希望做到上图所提到的公式，找到一个$effective(N)$



如果$effective(N)$可以做到下的两点，那么我们说学习是可能的。

![image-20210111234037199](https://i.loli.net/2021/01/11/baHm1zYTfX9tLKg.png)

------



## Effective Number of Hypothesis

![image-20210111234559377](https://i.loli.net/2021/01/11/7x1paYGMiwzPejB.png)

这里我们引入了新的Dichotomies，他和hypothesis的区别是dichotomies代表种类的多少，是有限的。

------

![image-20210111234919017](https://i.loli.net/2021/01/11/EajtHQ2fYG9uZpT.png)

这里对于不同的样本，线的种类数量可能不是确定的，如三个点，可能是6，也可能是8种。

那么不妨考虑最坏情况，我们取这些不同种类种最大的一个：

即![image-20210111235110535](https://i.loli.net/2021/01/11/HNzqWvw9TsKcBX7.png)。

我们称之为$growth \ function$成长函数。

------



![image-20210111235746549](https://i.loli.net/2021/01/11/4Ai6gvVWrCQ8tDP.png)

对于这种模型，我们有几种切法呢？

不难发现左边0个，右边N个，左边1个，右边N-1个..... 这样递推，因此：

![image-20210111235810729](https://i.loli.net/2021/01/11/ivYzqwDEJp3TR42.png)

$m_H=N+1$



如果对下图这种h来说：

![image-20210112000215920](https://i.loli.net/2021/01/12/v9TFQ6PC4OsdIBb.png)

就有：

![image-20210112000112025](https://i.loli.net/2021/01/12/DTiIJkg5wmXRpPh.png)

这么多种。



![image-20210112000450979](https://i.loli.net/2021/01/12/AoC9EraYu2Pn3ws.png)

那么如果对于一个 二维的分类，并别h也是区域覆盖，那么$m_H=2^N$,即成长函数growth function为$2^N$。



## Break point

![image-20210112001312073](https://i.loli.net/2021/01/12/49lDr1GYjcENxSA.png)

我们回顾一下不同模型的growth function的不同。



![image-20210112001459983](https://i.loli.net/2021/01/12/x6UDzIgYvyBEKdk.png)

​	因此如果M的替代量是一个多项式(polynomial)，那么这是一个很好的替代，它的变化远不及后面e的指数的变化，因此这是可以学习的。但是也有可能是指数型(exponential)的，这就不一定会是可以学习了，因为后面的也是e的指数，在一起可能是不收敛的。

​	那么对于一个2维感知机问题，增长函数是多项式形式的吗？



------

![image-20210112001952796](https://i.loli.net/2021/01/12/eROUz6SGPDmXCsL.png)

这里我们引入$break\  point$，在二维感知机分类中，从4个点开始我们发现无法做到$2^N$种情况，即16种，最多只能找到14种，无论这四个点怎么排列。我们称4为break point。



![image-20210112002301731](https://i.loli.net/2021/01/12/3TBh9clC4XJHvUt.png)

我们观察到，这个break point好像和增长函数有如上的关系，那么真的有吗？下一节会从数学角度解决这个问题。