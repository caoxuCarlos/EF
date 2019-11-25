# "健身到底吃多少"

[![GitHub license](https://img.shields.io/github/license/wangshub/wechat_jump_game.svg)](https://github.com/caoxuCarlos/EF/blob/master/LICENSE)


## 介绍

这个程序的名字叫做 EF (EatFolio). 因为解决这个问题灵感来自于  Markowitz 的 porfolio theory, 所以就造了 "eatfolio" 这么个词. 

在 EFv1.1, 出来以后, 收到了不少反馈, 在EFv1.2中做了很多修正, 可以说是面目全新🤓.

这个程序能根据你给定的`总热量`, `碳水-蛋白质供能比`, `蛋白质范围`以及`所选食物`生成一份精确的食谱. 

## 下载

考虑到国内 github 下载网速缓慢, 下载地址以百度网盘的形式给出: 

windows 用户下载地址:

```markdown
链接: https://pan.baidu.com/s/13Ku-UHy1BzXVkfLHvU2vjw  密码: 6buj
```

linux 用户下载地址: 

```markdown
链接: https://pan.baidu.com/s/1Ya0v_IE1X3anMZk4BFk1oQ  密码: fg6o
```

## 教程

请允许我使用一个自己的例子来说明软件的使用方法: 

打开软件, 界面应该是这样:

![](https://github.com/caoxuCarlos/EF/raw/master/pictures/ef1.2/001.png)

比如我一天需要的热量是 2800 大卡, 那么我在`今天所需总能量`输入2800. 然后点击`显示推荐`.

![](https://github.com/caoxuCarlos/EF/raw/master/pictures/ef1.2/002.png)

先计算早餐, 我把`早餐`后面的 840 复制, 粘贴到下面的`该餐总热量`中. 我希望碳水化合物提供的能量是蛋白质所提供能量的 2.5 倍左右, 于是把 2.5 输入`碳水/蛋白质`中. 我还希望这顿饭提供的蛋白质在 30g~50g 之间, 于是我在`最少蛋白质克数`输入30, 在`最多蛋白质克数`输入50. 

![](https://github.com/caoxuCarlos/EF/raw/master/pictures/ef1.2/003.png)

接着, 我在下面这张表里选择我想要的食物([点击这里](https://github.com/caoxuCarlos/EF/raw/master/foodlist.xlsx)下载图中表格):

![](https://github.com/caoxuCarlos/EF/raw/master/pictures/ef1.2/004.png)

我觉得主食可以是米饭和红薯, 随便哪个都行, 于是我在`主食`中输入:`米饭,红薯`. (中间的符号无所谓输入`米饭&红薯`或者`米饭+红薯`都是一样的)

同样地, 我觉得鸡胸肉和牛排是我喜欢的蛋白质来源, 我就在`肉蛋奶`中输入: `鸡胸肉,牛排,羊肉`

同理, 在`蔬果`中输入:`柚子,橙子`. 

在`脂肪`中输入:`葵花籽油,核桃`

![pass 005](https://github.com/caoxuCarlos/EF/raw/master/pictures/ef1.2/005.png)

然后点击一下旁边的`时间检测`. (因为这个程序的运算量很大, 可能需要算一会儿, 不过如果选择的组合合理, 通常也就是不到 3 秒的事情).

![pass 006](https://github.com/caoxuCarlos/EF/raw/master/pictures/ef1.2/006.png)

我看一下最坏也就十分钟, 哪怕我选择组合实在不合理, 10分钟以后我也就知道 "我的选择不合理" 这个结果了, 所以我直接点击`开始计算`, 如果运算次数太多, 又不确定自己的组合合理, 不妨减少在`主食`, `肉蛋奶`, `蔬果`和`油脂`中输入的食物数量, 比如在每项里只输入一种. 

![](https://github.com/caoxuCarlos/EF/raw/master/pictures/ef1.2/007.png)

事实上, 就算这个组合是我边写教程边随机写的, 我也只用 0.243 秒就做出了答案, 通常情况下还是很快的. 

那我还想一口气把我一天的所有饮食都算出来, 我再算一个午餐为例: 

我直接把午餐后面的 840 选中, 然后粘贴到`该餐总热量`中, 接着把已经选择了的食物进行一些修改, 然后`时间检测`, 结果如图: 

![](https://github.com/caoxuCarlos/EF/raw/master/pictures/ef1.2/008.png)

接着, 不用删除第一次输出的结果, 直接点击`开始计算`, 会发现第一次的结果并没有消失, 第二次结果直接出现在了第一次后面:

![pass 009](https://github.com/caoxuCarlos/EF/raw/master/pictures/ef1.2/009.png)

然后重复晚饭和加餐的操作, 最后直接从输出框里把所有文字复制走就行了. 

但是如果你并不介意每顿饭吃一样的, 这个软件还可以这样用: 

上面的`输入今日所需总能量`不用输入, 也不用点击后面的计算, 你只要像下图这样输入就可以得到一个全天的食谱:

![pass 010](https://github.com/caoxuCarlos/EF/raw/master/pictures/ef1.2/010.png)

这次就是用了 12 秒才算出来的, 所以大家按下`开始计算`之后还是耐心等待一下吧. 

## 期待您宝贵的反馈

<img src="https://github.com/caoxuCarlos/EF/raw/master/pictures/feedback_qrcode.png" width="271">

## 感谢小伙伴们为项目做出的贡献

@ [周涛](https://github.com/ZhouTao)

@ 杨雅清

@ 丁泓宇

