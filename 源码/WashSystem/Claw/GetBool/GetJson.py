import requests
import json
from Claw.GetBool.GetToken import GetToken as G
from faker import Factory
import time
from os import path

# 文件名：GetJson
# 功能：通用获取 json
# 输入：从 token.txt 获取 token 从调用文件获取 url 与传输 json
# 输出：以字典的形式返回获取的 json

class GetJson:
    __tokenWay = "Claw\GetBool\Token.txt"
    __url = ""
    # 发送的json
    __json = {}
    __token = []
    # 接收的json
    __reJsons = {}


    # 获取 token
    @staticmethod
    def __GetToken() -> None:
        # 判断是否存在
        if not path.exists(GetJson.__tokenWay) or not path.getsize(GetJson.__tokenWay):
            G.Get()
        # token
        GetJson.__token = []
        with open(GetJson.__tokenWay ,"r" ,encoding= "utf-8") as f:
            # 获取 token
            for token in f:
                a = str(token).replace("\n" ,"")
                GetJson.__token.append(a)

    # 通过 url 获取数据
    @staticmethod
    def __Get() -> bool:
        time.sleep(1)

        header = {
            "referer": "https://servicewechat.com/wxabd763cdb5f94ff5/139/page-frame.html",
            # 随机 agent
            "user-agent": str(Factory().create().user_agent()),
            "accessToken": GetJson.__token[0],
            "refreshToken": GetJson.__token[1]
        }

        try:
            report = requests.post(url= GetJson.__url ,headers= header ,json= GetJson.__json)
        except Exception as e:
            print("GetJson __Get() ERROR:", e)
            return False

        GetJson.__reJsons = json.loads(str(report.text))

        # 当前 token 是否无效
        return GetJson.__reJsons.get("result" ,False)

    # 输入 url 与 json 综合运行 返回 json
    @staticmethod
    def Run(url: str ,json: dict) -> dict:
        GetJson.__url = url
        GetJson.__json = json

        GetJson.__GetToken()
        while not GetJson.__Get():
            G.Get()
            GetJson.__GetToken()

        return GetJson.__reJsons
