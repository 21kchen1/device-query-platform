import sys
from thefuzz.fuzz import token_set_ratio as tsr
sys.path.append("..")
from DB.ConDB import DataBase
from Claw.GetText import GetText

# 文件名：DataDeal
# 功能：数据处理 获取
# 输入：输入框字符串
# 输出：对应数据库查询结果

class Node:
    def __init__(self ,code ,point) -> None:
        self.code = code
        self.point = point

class DataDeal:
    # 洗衣机综合评价，返回数组
    @staticmethod
    def DataMix(text: str ,ty: str):
        DataBase.ConnectDB("localhost" ,"root" ,"mysqlpassword" ,"clawdata")
        try:
            if "," in text:
                text = text.split(",")
            else: text = text.split("，")
            # 处理楼层
            f = 0
            if(len(text) > 1):
                for i in text[1]:
                    if i in "0123456789":
                        f *= 10
                        f += int(i)
        except :
            return False ,False ,False ,False

        # 获取地址信息
        pl ,_ = DataBase.SelectFromTable("washdata" ,"DISTINCT placeName" ,{"deviceType": "= '{}'".format(ty)})
        placeList = []
        for i in pl:
            placeList.append(i[0])

        # 通过字符串模糊匹配获取地址
        textPlace = ""
        maxPoint = 0
        for i in placeList:
            thisPoint = tsr(i ,text[0])
            if maxPoint > thisPoint: continue
            maxPoint = thisPoint
            textPlace = i

        if maxPoint < 10: return False ,False ,False ,False
        washList ,_ = DataBase.SelectFromTable("washdata" ,"placeName ,floorName ,deviceName ,deviceTime ,deviceStatus" ,{"placeName": "= '{}'".format(textPlace), "deviceType": "= '{}'".format(ty)})

        # 排序用数组
        order = []
        # 评分
        for i in range(0 ,len(washList)):
            point = int(washList[i][3])
            if not f == 0:
                point += abs(f - int(washList[i][1]))
            order.append(Node(i ,point))

        order = sorted(order ,key= lambda x: x.point)

        mixData = []
        for i in range(0 ,len(washList)):
            mixData.append(washList[order[i].code])

        order = []
        # 评分时间
        for i in range(0 ,len(washList)):
            point = int(washList[i][3])
            order.append(Node(i ,point))

        order = sorted(order ,key= lambda x: x.point)
        timCode = order[0].code

        order = []
        # 评分距离
        for i in range(0 ,len(washList)):
            if not f == 0:
                point = abs(f - int(washList[i][1]))
            order.append(Node(i ,point))

        order = sorted(order ,key= lambda x: x.point)
        disCode = order[0].code

        return mixData ,washList[timCode] ,washList[disCode] ,mixData[0]

    @staticmethod
    def DataText():
        return GetText.Run()