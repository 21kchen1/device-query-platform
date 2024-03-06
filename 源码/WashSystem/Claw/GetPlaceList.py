from Claw.GetBool.GetJson import GetJson

# 文件名：GetPlaceList
# 功能：获取对应服务的地点字典
# 输入：服务类型
# 输出：地址为键，id为值的字典

class GetPlaceList:
    url = "https://api.xiaolianhb.com/w/stu/residence/listBySchool"
    jsons = {
        "deviceType": 0,
    }

    @staticmethod
    def Run(deviceType: int) -> dict:
        GetPlaceList.jsons["deviceType"] = deviceType
        Data = GetJson.Run(GetPlaceList.url ,GetPlaceList.jsons).get("data" ,False)

        # 获取错误
        if Data == False:
            print("UNEXPECTED: From GetPlaceList. Run()")
            return False

        placeDict = Data["residences"]
        # 返回内容
        placeList = {
            "deviceType": deviceType,
            "placeDict": {}
        }

        try:
            for place in placeDict:
                placeList["placeDict"][place["fullName"]] = place["id"]
        except Exception as e:
            print("GetPlaceList Run() ERROR:",e)
            return False

        return placeList