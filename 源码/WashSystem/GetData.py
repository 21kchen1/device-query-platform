from Claw.GetPlaceList import GetPlaceList
from Claw.GetPlaceDetail import GetPlaceDetail
from Claw.GetFloorDetail import GetFloorDetail
from DB.ConDB import DataBase

# 文件名：GetData
# 功能：获取所有数据并输入数据库
# 输入：调用
# 输出：输入DB

class GetData:

    # 获取对应类型的机器
    @staticmethod
    def __GetDataFromClaw(deviceType: int) -> list:
        data = []

        try:
            # 地点列表 在其 placeDict 存储 键名 值id
            placeList = GetPlaceList.Run(deviceType)
            for placeName in placeList["placeDict"]:
                # 获取值 Placeid
                placeId = placeList["placeDict"][placeName]
                # 获取对应楼层列表 在其 floorList 存储各个 floorId floorName 字典
                # 在其 serviceTime 存储运行时间
                placeDetail = GetPlaceDetail.Run(placeList["deviceType"] ,placeId)
                # 服务时间
                serviceTime = placeDetail["serviceTime"]

                for floorInf in placeDetail["floorList"]:
                    floorId = floorInf["floorId"]
                    floorName = str(floorInf["floorName"]).replace("层" ,"")
                    # 当前楼层的机器列表
                    # 其 deviceList 中存储各个 status location id Rtime
                    floorDetaul = GetFloorDetail.Run(placeDetail["deviceType"] ,floorId)

                    for deviceInf in floorDetaul["deviceList"]:
                        deviceStatus = deviceInf["status"]
                        deviceName = deviceInf["location"]
                        deviceId = deviceInf["id"]
                        deviceTime = deviceInf["remainingTime"]

                        # 当前元组
                        cup = {
                            "deviceType": deviceType,
                            "placeId": placeId,
                            "placeName": placeName,
                            "serviceTime": serviceTime,
                            "floorId": floorId,
                            "floorName": floorName,
                            "deviceStatus": deviceStatus,
                            "deviceName": deviceName,
                            "deviceId": deviceId,
                            "deviceTime": deviceTime
                        }
                        print(cup)
                        data.append(cup)

        except Exception as e:
            print("GetData.GetFromClaw() ERROR:",e)
            return False
        return data

    # 将数据输入DB
    @staticmethod
    def __PutDataToDB(data: list) -> bool:
        try:
            # 与数据库进行连接
            DataBase.ConnectDB("localhost" ,"root" ,"mysqlpassword" ,"clawdata")
            tableName = "washdata"
            cup = """
                deviceType char(20),
                placeId char(20),
                placeName char(20),
                serviceTime char(20),
                floorId char(20),
                floorName char(20),
                deviceStatus char(20),
                deviceName char(20),
                deviceId char(20) primary key,
                deviceTime char(20)
            """

            # 建表
            DataBase.CreateTable(tableName ,cup)

            # 插入数据
            DataBase.InsertTable(tableName ,data)

        except Exception as e:
            print("GetData.PutDataToDB() ERROR:",e)
            return False
        return True

    @staticmethod
    def Run():
        GetData.__PutDataToDB(GetData.__GetDataFromClaw(4) + GetData.__GetDataFromClaw(7))