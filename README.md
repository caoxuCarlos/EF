# 用一个程序解决健身饮食定量问题

[![GitHub license](https://img.shields.io/github/license/wangshub/wechat_jump_game.svg)](https://github.com/caoxuCarlos/EF/blob/master/LICENSE)


## 介绍

这个程序的名字叫做 EF (EatFolio). 因为解决这个问题灵感来自于  Markowitz 的 porfolio theory, 所以就造了 "eatfolio" 这么个词. 

这个程序能够根据三个因素, 输出一份合适的健身食谱:

2. 你希望碳水化合物所提供的能量是蛋白质提供的能量的多少倍. 
2. 你需要的总能量 (单位千卡). 
3. 你选择的食物. 

假如你今天需要的总能量是 2500 kcal, 你希望碳水化合物提供的能量是蛋白质提供能量的 2.5 倍, 你想吃: 鸡胸肉, 米饭, 红薯, 燕麦和水煮鱼. 那输出的结果差不多是这样的: 

```markdown
我是EF, 很开心能够为你服务!
我帮你找到了这个合适的组合:
鸡胸肉(不吃皮) 387.8g
米饭 850.2g
红薯 941.6g
燕麦 9.9g
水煮鱼 31.0g

你将摄入:
20.5g 脂肪
417.1g 碳水化合物
161.7g 蛋白质

计算所用食物热量信息来源:
https://www.fatsecret.cn/%E7%83%AD%E9%87%8F%E8%90%A5%E5%85%BB/search?q=
```

## 下载

考虑到国内 github 下载网速缓慢, 下载地址以百度网盘的形式给出: 

windows 用户下载地址:

```markdown
链接: https://pan.baidu.com/s/1hRJJ7Nci49vJ6HyZb4kgQQ  密码: cqvn
```

linux 用户下载地址: 

```markdown
链接: https://pan.baidu.com/s/1pungZYVrNNHu0acvf6_Olw  密码: o5bn
```

> linux的可执行文件在 `dist/ef_v1.1`文件夹中

## 教程

软件打开以后差不多是这样: 

![](https://github.com/caoxuCarlos/EF/raw/master/pictures/ef_v1.1_example2.gif)

`碳水-蛋白质供能比`: yangyaqing如果你希望从碳水化合物摄入的热量是从蛋白质摄入的热量的2.8倍, 那就把这个数字设置成 2.8

`总热量(大卡)`: 就是一天需要通过食物摄入多少大卡的热量, 如果需要摄入 2800 kcal, 那就输入 2800

`请选择食物`: 通过`简写`与`编号`均可输入. 如果需要添加鸡胸肉, 则输入`jxr`(拼音的首字母)或者`001`都可以, 输入多种食物的时候中间用逗号隔开. 

如果想输入 "鸡胸肉, 米饭, 红薯, 燕麦和水煮鱼", 则输入:`jxr,mf,ym,hs,szy`或`001,002,003,008,010`.

![](https://github.com/caoxuCarlos/EF/raw/master/pictures/checklist.png)

[点击这里下载上图表格](https://github.com/caoxuCarlos/EF/raw/master/checklist.xlsx)

或者混合输入`jxr,002,ym,003,szy`也是一样的.

![](https://github.com/caoxuCarlos/EF/raw/master/pictures/ef_v1.1_example.gif)

值得说明的是, 不是所有的组合都有符合要求的配比. 比如只选择红薯, 那碳水-蛋白质供能比是 12.8, 是没法满足要求的. 

要承认的是这个程序输出的结果有时候还不够智能, 在它更加完善之前, 希望大家先通过尝试调整食物组合, 来得出可行的方案. 

欢迎朋友们提出建议, 欢迎感兴趣的朋友来帮忙开发GUI !

邮箱:  running_pen@126.com

## 原理

制定食物组合的本质是在给定食物种类的前提下, 给食物分配不同的权重. 

EF使用[蒙特卡洛方法](https://en.wikipedia.org/wiki/Monte_Carlo_method), 随机生成 20000 组权重向量, 每一个向量对应一个组合, 每个组合都在下图中用一个圆点表示(为了清晰起见, 下图只展示300个结果):

![](https://github.com/caoxuCarlos/EF/raw/master/pictures/mc_plot_explain.png)

从这些结果当中, 挑选出`碳水-蛋白质供能比`与所要求的比例相差不到 5% 的所有结果. 就是图中颜色最深的那些点. 

然后把点和原点连线, 斜率就代表了该组合每摄入 1g 脂肪的同时摄入多少克的蛋白质. EF "喜欢蛋白质, 讨厌脂肪", 所以它要选择斜率最大的组合, 也就是在以摄入1g 脂肪为代价, 所能获得最多克蛋白质的组合. 

## 感谢小伙伴对本项目提供的帮助

@ 杨雅清

@ 丁鸿宇
