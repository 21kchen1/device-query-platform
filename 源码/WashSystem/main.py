# from Claw.GetPlaceList import GetPlaceList
# from Claw.GetPlaceDetail import GetPlaceDetail
# from Claw.GetFloorDetail import GetFloorDetail

# # deviceType 4 洗衣机 7 干衣机

# placeList = GetPlaceList.Run(7)

# for placeName in placeList["placeDict"]:
#     placeId = placeList["placeDict"][placeName]
#     print(placeName)
#     placeDetail = GetPlaceDetail.Run(placeList["deviceType"] ,placeId)

#     for floorInf in placeDetail["floorList"]:
#         print(floorInf["floorName"])
#         print(GetFloorDetail.Run(placeDetail["deviceType"] ,floorInf["floorId"]))
#     print()

from GetData import GetData
from Show.PyGui import Run as UIRun
import multiprocessing
import time


def claw_():
    while True:
        GetData.Run()
        print("爬取完成")
        time.sleep(200000)


if __name__ == "__main__":
    show_thread = multiprocessing.Process(target=UIRun)
    claw_thread = multiprocessing.Process(target=claw_)

    show_thread.start()
    claw_thread.start()

    show_thread.join()
    claw_thread.join()