import pymysql

# 文件名：ConDB
# 功能：数据库操作
# 输入：sql
# 输出：数据

class DataBase:
    # 游标
    __Cursor = 0

    # 链接数据库
    @staticmethod
    def ConnectDB(host ,user ,password ,dbName) ->bool:
        # 用户归属(一般localhost) 用户名称 密码 数据库名称 端口 编码方式
        try:
            # 获取数据库权限 并获得游标
            DataBase.__Cursor = pymysql.connect(host= host ,user= user ,password= password ,db= dbName ,port= 3306 ,charset= "utf8" ,autocommit= True).cursor()
        except Exception as e:
            print("DataBase ConnectDB() ERROR:", e)
            return False
        return True

    # 删表
    @staticmethod
    def DropTable(tableName) -> bool:
        if not DataBase.__Cursor:
            print("databases is not connect")
            return False

        try:
            dropTable = "DROP TABLE IF EXISTS {};"
            DataBase.__Cursor.execute(dropTable.format(tableName))
        except Exception as e:
            print("DataBase DropTable() ERROR:" ,e)
            return False
        return True

    # 建表 以机器id为键
    @staticmethod
    def CreateTable(tableName ,content) -> bool:
        if not DataBase.__Cursor:
            print("databases is not connect")
            return False

        try:
            # 清理原有数据
            DataBase.DropTable(tableName)
            # 建表
            creatTable = "CREATE TABLE {} ({});"
            DataBase.__Cursor.execute(creatTable.format(tableName ,content))
        except Exception as e:
            print("DataBase CreateTable() ERROR:" ,e)
            return False
        return True

    # 向表中插入元组
    @staticmethod
    def InsertTable(tableName ,content: list) -> bool:
        if not DataBase.__Cursor:
            print("databases is not connect")
            return False

        try:
            prop = ""
            contents = ""
            # 获取属性列
            for name in content[0]:
                prop += str(name) + ","
            prop = prop[0 :-1]

            # 获取每一列的元素
            for line in content:
                contents += "("
                for name in line:
                    contents += "'" + str(line[name]) + "'" + ","
                contents = contents[0 :-1]
                contents += "),"
            contents = contents[0 :-1]

            insertTable = "INSERT into {}({}) values {};"
            DataBase.__Cursor.execute(insertTable.format(tableName ,prop ,contents))
        except Exception as e:
            print("DataBase InsertTable() ERROR:" ,e)
            return False
        return True

    # 在表中搜索元组 利用地址进行搜索
    @staticmethod
    def SelectFromTable(tableName ,demand ,condition: dict) -> dict:
        if not DataBase.__Cursor:
            print("databases is not connect")
            return False
        try:
            condi = ""
            for name in condition:
                condi += str(name) + str(condition[name]) + " and "
            condi = condi[0 :-4]

            selectFromTable = "Select {} From ({})"
            if not condition == {}:
                selectFromTable += " Where ({})"
                selectFromTable = selectFromTable.format(demand ,tableName ,condi)
            else:
                selectFromTable = selectFromTable.format(demand ,tableName)

            DataBase.__Cursor.execute(selectFromTable + ";")
            # 从游标获取搜索到的数据
            data = DataBase.__Cursor.fetchall()
        except Exception as e:
            print("DataBase SelectFromTable() ERROR:" ,e)
            return  {}, False
        return data ,True


# print(DataBase.ConnectDB("localhost" ,"root" ,"" ,"clawdata"))
# print(DataBase.CreateTable("washdata" ,"name char(20) primary key ,time char(20)"))
# print(DataBase.DropTable("washsdata"))
# print(DataBase.InsertTable("washdata" ,[{"name": "a" ,"time": "b"}, {"name": "b" ,"time": "b"}]))
# print(DataBase.InsertTable("washdata" ,{"name": "b" ,"time": "b"}))
# print(DataBase.SelectFromTable("washdata" ,"*" ,{"time": "b"}))
