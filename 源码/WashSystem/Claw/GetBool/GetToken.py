import requests
import json
from faker import Factory
import time

# 文件名：GetToken
# 功能：获取 access Token 与 refresh Token
# 输入：无
# 输出：写入 Token.txt

class GetToken:
    # 登入功能 url
    __url = "https://api.xiaolianhb.com/m/mp/wechat/user/account/public/silent/login"

    # 代理
    proxi = {
        "http": "http://106.15.190.190.3128",
        "https": "https://106.15.190.190.3128",
    }

    # 请求头
    __header = {
        "referer": "https://servicewechat.com/wxabd763cdb5f94ff5/139/page-frame.html",
        # 随机 agent
        "user-agent": str(Factory().create().user_agent()),
    }

    # 传输用 json
    __json = {
        "userInfo": {
            # 虚拟头像链接
            "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/\\"
        },
        # 需要获取用户的 微信 unionId
        "unionId": "oGaH01RLIc6ozb1OEmvtlzWPei7w",
        "system": "2"
    }

    # 存放 token 的路径
    __tokenWay = "Claw\GetBool\Token.txt"

    @staticmethod
    def __Wri(jsons) -> bool:
        try:
            with open(GetToken.__tokenWay ,"w" ,newline= "") as f:
                f.write(str(jsons["data"]["accessToken"]) + "\n")
                f.write(str(jsons["data"]["refreshToken"]))
        except Exception as e:
            print("GetToken Wri() ERROR:",e)
            return False
        return True

    # 静态 获取 url
    @staticmethod
    def Get() -> bool:
        # 限制访问频率
        time.sleep(2)

        try:
            report = requests.post(url= GetToken.__url ,headers= GetToken.__header ,json= GetToken.__json)
        except Exception as e:
            print("GetToken Get() ERROR:" ,e)
            return False

        jsons = json.loads(str(report.text))
        # 当前的 union 可能被封禁
        if jsons.get("result" ,False) == False:
            print(jsons)
            print("UNEXPECTED: The current account is blocked and cannot be used")
            return False

        return GetToken.__Wri(jsons)
