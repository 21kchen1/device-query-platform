from Claw.GetBool.GetJson import GetJson

# 文件名：GetPlaceDetail
# 功能：获取对应服务对应地点的详细信息
# 输入：服务类型 地址id
# 输出：包含楼层id 的字典

class GetPlaceDetail:
    url = "https://api.xiaolianhb.com/w/stu/device/washerRoomList"
    jsons = {
        "type": str(0),
        "buildingId": 0
    }

    @staticmethod
    def __DealData(Data: dict ,deviceType: int) -> dict:
        try:
            detailList = Data["list"]
            # 返回内容
            placeDetail = {
                "deviceType": deviceType,
                "serviceTime": str(Data["serviceTime"]),
                "floorList": []
            }

            for floor in detailList:
                floorInf = {}
                # 楼层 id
                floorInf["floorId"] = str(floor["id"])
                # 楼层名称
                floorInf["floorName"] = floor["floorName"]
                # 剩余可用机器数
                floorInf["floorNum"] = floor["freeNum"]
                placeDetail["floorList"].append(floorInf)
        except Exception as e:
            print("GetPlaceList. __DealData ERROR:",e)
            return False
        return placeDetail

    @staticmethod
    def Run(deviceType: int ,buildingId: str) -> dict:
        GetPlaceDetail.jsons["type"] = deviceType
        GetPlaceDetail.jsons["buildingId"] = buildingId
        Data = GetJson.Run(GetPlaceDetail.url ,GetPlaceDetail.jsons).get("data" ,False)

        # 获取失败
        if Data == False:
            print("UNEXPECTED: From GetPlaceDetail. Run()")
            return False

        return GetPlaceDetail.__DealData(Data ,deviceType)