
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
