LibSym
======

A python program to simulate locker occupation in PKU library

http://blog.sciencenet.cn/blog-270448-850759.html

近年来，北京大学图书馆的存包柜被长期占用的情况十分严重。尽管图书馆在《北京大学图书馆存包柜使用须知》中明确规定了闭馆前不带走物品和挂锁的行为为占柜，并应该被清理，而因为种种原因这一规定并没有得到彻底的执行。

近来，随着图书馆方面加强了对存包柜的清理，一些利益相关者在北大未名BBS的PKULibrary版面上产生了很多的争执。有一些网友认为，清理存书柜的行为不具有正当性，而违规占柜是正当的。他们的理由包括清理存包柜会导致实际的利用效率下降。

针对这些争论，我对北京大学图书馆的存包过程进行了简化假设，并构建了模拟模型，利用python语言对其进行了实现和求解，并研究了不同参数下的模型结果。

该模型的假设简要概括如下：

北京大学图书馆（PKULib）每天开放10小时。

PKULib有1000位读者，其中100位为不遵守规定的读者（badreader），900位为遵守规定的读者（goodreader）。

北京大学图书馆提供150个存包柜（locker）供读者使用。

每天，所有读者都会一个个的进馆，并都会使用存包柜。其进入图书馆的时间基本满足均匀分布，即每小时进入的人数相差不大。每人进馆后都会寻找空的储物柜，如果找到，该读者会感到开心（happiness）；如果存包柜都被沾满，该读者会感到郁闷（madness）。

goodreader每天会在图书馆呆到下一个整点，且这一天就不再来图书馆。他们走的时候会带走存包柜里自己的东西。

badreader走的时间谁也不知道，而且他们不会带走自己在存包柜里的东西。

每隔一段时间（emptyperiod），图书馆会在闭馆后清理存包柜，此时badreader占用的存包柜会被清空。直到下一次badreader来到图书馆，他们才会重新占据一个存包柜。

我编写并求解了这一模型。在参数emptyperiod不同的情况下，获得了不同的结果。经过多次尝试，发现参数不变的情况下结果的差异不大（可以算方差表征）。典型的值如下：

当每天清一次柜时，happiness为90209，madness为9791；

当每30天清一次柜时，happiness为1314，madness为98686。

这样的模拟结果说明，在模型假设条件下，每天清柜相比每30天清柜，会显著的增加happiness，降低madness。

<hr>

History:
1.0.0 Released 20141213

