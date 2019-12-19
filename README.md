

Hanthon 汉语Python
====================

##  用汉语书写Python.

汉语作为世界主要语言, 历经千年, 传承不息. 我们的祖先用它来抒发情感, 表达思想.

可令人遗憾的是,  由于近代中国在计算机领域的落后, 没有任何一门主流编程语言使用汉语.

本项目通过将中文代码翻译成英文,  给Python套上一层中文的"外衣". 



#  Demo

## 二分搜索

Hanthon:

```
名 二分搜索器:
    有 初(己):
        云云

    有 二分搜索(己, 数组, 目标, 低, 高):
        若 低 > 高:
            得 空

        中 = (低+高)//2
        若 数组[中] == 目标:
            得 中
        若则 数组[中] < 目标:
            得 己.二分搜索(数组, 目标, 中+1, 高)
        若则 数组[中] > 目标:
            得 己.二分搜索(数组, 目标, 低, 中-1)

    

数组1 = [甲 对 甲 于 区间(1, 6)]
搜索器 = 二分搜索器()
对 目标 于 区间(1, 7):    
    位置 = 搜索器.二分搜索(数组1, 目标, 0, 长(数组1)-1)
    见(位置)

```

Python:

```
class 二分搜索器:
    def __init__(self):
        pass

    def 二分搜索(self, 数组, 目标, 低, 高):
        if 低 > 高:
            return None

        中 = (低+高)//2
        if 数组[中] == 目标:
            return 中
        elif 数组[中] < 目标:
            return self.二分搜索(数组, 目标, 中+1, 高)
        elif 数组[中] > 目标:
            return self.二分搜索(数组, 目标, 低, 中-1)

    

数组1 = [甲 for 甲 in range(1, 6)]
搜索器 = 二分搜索器()
for 目标 in range(1, 7):    
    位置 = 搜索器.二分搜索(数组1, 目标, 0, len(数组1)-1)
    print(位置)

```

## 龟兔赛跑

Hanthon:

```
终点: 整 = 100


名 动物:
    有 初(己, 位置=0, 速度=1, 睡觉间隔=5, 睡觉时长=5):
        己.位置 = 位置
        己.速度 = 速度
        己.睡觉时长 = 睡觉时长
        己.睡觉间隔 = 睡觉间隔
        己.困意 = 0 # [-睡觉时长 , 睡觉间隔] 逐渐增大, 若大于最大值则置为最小值 , 小于0表示正在睡觉
        
    有 要睡觉吗(己):
        若 无 己.睡觉间隔:
            得 坏
        己.困意 += 1
        若 己.困意 > 己.睡觉间隔 :
            己.困意 = -己.睡觉时长 
            得 好
        若则 己.困意 < 0:
            得 好
        否则:
            得 坏
            

    有 跑(己):
        若 己.要睡觉吗() == 好:
            己.睡()
        否则:
            己.位置 += 己.速度
            # 见(己.名字, "到达", 己.位置)

    有 睡(己):
        # 见(己.名字, "睡觉中")
        云云
        
    有 吃(己):
        云云
        


名 乌龟(动物):
    有 初(己, 速度, 睡觉间隔):
        祖().初(速度=速度, 睡觉间隔=睡觉间隔)
        己.名字 = "乌龟"

名 兔子(动物):
    有 初(己, 速度, 睡觉间隔):
        祖().初(速度=速度, 睡觉间隔=睡觉间隔)
        己.名字 = "兔子"
    

有 比赛(龟: 乌龟, 兔: 兔子):
    当 龟.位置 < 终点 及 兔.位置 < 终点:
        龟.跑()
        兔.跑()
    否则:
        若 龟.位置 >= 终点:
            见("乌龟获胜!")
            得 "龟"
        若则 兔.位置 >= 终点:
            见("兔子获胜!")
            得 "兔"


夫 开("语录.txt", "w") 为 文:
    对 睡觉间隔 于 区间(1, 3):        
        赢家 = 比赛(乌龟(速度=1, 睡觉间隔=空), 兔子(速度=3, 睡觉间隔=睡觉间隔))    
    若 赢家 == "兔":
        文.写("看来睡一会没什么大不了的 --- 鲁迅")

    若 赢家 == "龟":
        文.写("996是一种福报  --- Jack")

```

Python:

```
终点: int = 100


class 动物:
    def __init__(self, 位置=0, 速度=1, 睡觉间隔=5, 睡觉时长=5):
        self.位置 = 位置
        self.速度 = 速度
        self.睡觉时长 = 睡觉时长
        self.睡觉间隔 = 睡觉间隔
        self.困意 = 0 # [-睡觉时长 , 睡觉间隔] 逐渐增大, 若大于最大值则置为最小值 , 小于0表示正在睡觉
        
    def 要睡觉吗(self):
        if not self.睡觉间隔:
            return False
        self.困意 += 1
        if self.困意 > self.睡觉间隔 :
            self.困意 = -self.睡觉时长 
            return True
        elif self.困意 < 0:
            return True
        else:
            return False
            

    def 跑(self):
        if self.要睡觉吗() == True:
            self.睡()
        else:
            self.位置 += self.速度
            # print(self.名字, "到达", self.位置)

    def 睡(self):
        # print(self.名字, "睡觉中")
        pass
        
    def 吃(self):
        pass
        


class 乌龟(动物):
    def __init__(self, 速度, 睡觉间隔):
        super().__init__(速度=速度, 睡觉间隔=睡觉间隔)
        self.名字 = "乌龟"

class 兔子(动物):
    def __init__(self, 速度, 睡觉间隔):
        super().__init__(速度=速度, 睡觉间隔=睡觉间隔)
        self.名字 = "兔子"
    

def 比赛(龟: 乌龟, 兔: 兔子):
    while 龟.位置 < 终点 and 兔.位置 < 终点:
        龟.跑()
        兔.跑()
    else:
        if 龟.位置 >= 终点:
            print("乌龟获胜!")
            return "龟"
        elif 兔.位置 >= 终点:
            print("兔子获胜!")
            return "兔"


with open("语录.txt", "w") as str:
    for 睡觉间隔 in range(1, 3):        
        赢家 = 比赛(乌龟(速度=1, 睡觉间隔=None), 兔子(速度=3, 睡觉间隔=睡觉间隔))    
    if 赢家 == "兔":
        str.write("看来睡一会没什么大不了的 --- 鲁迅")

    if 赢家 == "龟":
        str.write("996是一种福报  --- Jack")

```



#  安装

` pip install hanthon`

``python -m hanthon <source-file>``


# Hanthon语言快速入门

Hanthon本质上只是Python的一张皮, 所做的仅仅是将特定中文关键词转化成英文.
因此.Hanthon语言可以用一张中英对照表来描述.
你可以在源文件`table.org`中进行自定义.

## 变量
支持变量类型申明

| Python | Hanthon |
| ------ | ------- |
| int    | 整      |
| float  | 浮      |
|str|文|
|list|表|
|dict|典|
|None|空|
|True|好|
|False|坏|



## 逻辑判断

| Python | Hanthon        |
| ------ | -------------- |
| and    | 及             |
| or     | 或             |
| not    | 不             |
| not    | 无(两者都可以) |



## 循环

| Python   | Hanthon |
| -------- | ------- |
| for      | 对      |
| while    | 当      |
| continue | 续      |
| break    | 弃      |



## 控制流

| Python | Hanthon |
| ------ | ------- |
| if     | 若      |
| else   | 否则    |
| elif   | 若则    |

## 块
| Python | Hanthon |
| ------ | ------- |
|def|有|
|return|得|
|pass|云云|
|global|外|
|try|试|
|except|误|


## 面向对象 

| Python     | Hanthon |
| ---------- | ------- |
| class      | 名      |
| `__init__` | 初      |
| self       | 己      |
|super| 祖|

# 其他

| Python     | Hanthon |
| ---------- | ------- |
|in|于|
|as|即|
|from|自|
|import|引|
|yield|求|
|del|删|


# 常用函数
| Python     | Hanthon |
| ---------- | ------- |
|print|见|
|range|区间|
|append|补|
|len|长|
|sort|排序|
|open|开|
|read|读|
|write|写|








设计思路 
====

## 模仿文言, 求其神似

### 为什么用文言文

文言文诞生于纸张稀缺的历史时期, 因此落笔必须惜字如金. 这个历史条件的限制, 反而使得文言文具有简练高效的表达特点.

比如`if`, 翻译为`如果`,  编写起来就过于麻烦, 翻译为`若`,  同样的意思, 却节约了一个字, 对于`if`这样的关键词来说, 可以节约不少时间. 

Python在所有编程语言中, 最重视程序的可读性, 甚至为此牺牲了大量运行的效率, 为了能少写一行`file.close()` , 不惜引入一个新的关键词`with` .  就是为了让代码阅读更加顺畅.

两者结合, 可以写出非常接近自然语言的效果. 

### 为什么只求神似

大多数技术文献, 在翻译名词时, 会尽量贴近原意. 这样做, 虽然精确, 但是过于死板. 由于中英文之间思考方式, 语法习惯的差异, 造成的结果就是可读性不强.

为了更好的可读性, Hanthon语言的中文关键字不会刻意贴近其英文版,  而是考虑其使用场景,  选取更加贴近应用场景的翻译方法. 使其读起来接近一篇自然语言的文章.

### 翻译中的一些决策

以`for` 关键词为例, 按字面意思应该翻译成 `遍历`,  或者`循环`
首先`for`作为一个常用关键字, 其中文对照应该被压缩到一个字. 

其次, 考虑到`for`经常性的用法是 ` for i in range()`. 这句话翻译成中文,  应该是 `对每一个i在区间xx里` , 进一步文言化, 即为`对i于区间xx里`, 所以将`for`翻译为`对`, 将`in`翻译为`于` , 状语后置, 颇有古风.

再谈谈`def`, 字面义`定义`, 但是汉语的习惯是动宾搭配, `def`之后, 马上会接上函数的名称, 因此考虑将其翻译成动词, 而不是名词,  `存在`是一个不错的候选项, 而 `有`  显然更好一些.

`lamda`更难直译,  翻译成`拉姆达算子`, 未免太掉胃口, 考虑到`lamda` 代表一种运算过程, 

我将其翻译为`道`,  道有道路的意思, 引申为从此处到彼处的一种过程, 又因为lambda可以创造高阶函数, 非常玄妙,
也比较适合用玄妙的`道`来描述.

类似的还有`pass`翻译成`云云`, 表示要说什么, 但又不知道说些什么. `with`翻译成`夫` ,常在文言文中做发表感叹的起手词.

