
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
