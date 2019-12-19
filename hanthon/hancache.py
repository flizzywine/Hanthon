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

