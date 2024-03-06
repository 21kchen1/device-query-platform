import requests
from bs4 import BeautifulSoup

# 文件名：GetText
# 功能：获取 OA 信息
# 输入：无
# 输出：返回链接与标题

class GetText:
    @staticmethod
    def Run():
        soupTree = BeautifulSoup(requests.get(url= "http://oa.stu.edu.cn/csweb/list.jsp").text ,"html.parser")
        trList = soupTree.find_all("tr" ,class_ = "datalight")
        urlList = soupTree.find_all("a" ,target = "_blank")

        data = []
        for i in range(0 ,len(trList) - 1):
            time = trList[i].find_all("td")
            data.append(["http://oa.stu.edu.cn" + urlList[i].get("href") ,urlList[i].get("title") ,time[1].string ,time[2].string[5:]])

        return data

