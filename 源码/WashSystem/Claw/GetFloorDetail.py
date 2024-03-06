from Claw.GetBool.GetJson import GetJson

# 文件名：GetFloorDetail
# 功能：获取对应楼层机器数据
# 输入：服务类型 楼层编号
# 输出：机器数据

class GetFloorDetail:
    url = "https://api.xiaolianhb.com/w/stu/device/getDevices"
    jsons = {
        "id": str(0),
        "deviceType": 0,
    }

    @staticmethod
    def __DealData(Data: dict ,deviceType: int) -> dict:
        try:
            deviceList = Data["devices"]
            floorDetail = {
                "deviceType": deviceType,
                "deviceList": []
            }

            for device in deviceList:
                deviceInf = {}
                # 状态 0 空闲 状态 1 使用中 状态 -1 离线
                deviceInf["status"] = device["status"]
                # 机器名称
                deviceInf["location"] = device["location"]
                # 机器 id 显示排序用
                deviceInf["id"] = str(device["id"])
                # 剩余时间
                deviceInf["remainingTime"] = device["remainingTime"]
                floorDetail["deviceList"].append(deviceInf)
        except Exception as e:
            print("GetFloorDetail. __DealData() ERROR:",e)
            return False
        return floorDetail


    @staticmethod
    def Run(deviceType: int ,floorId: str) -> dict:
        GetFloorDetail.jsons["id"] = floorId
        GetFloorDetail.jsons["deviceType"] = deviceType
        Data = GetJson.Run(GetFloorDetail.url ,GetFloorDetail.jsons).get("data" ,False)

        # 获取错误
        if Data == False:
            print("UNEXPECTED: From GetFloorDetail. Run()")
            return False

        return GetFloorDetail.__DealData(Data ,deviceType)