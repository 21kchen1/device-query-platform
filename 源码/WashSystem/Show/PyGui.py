from PyQt5 import QtCore ,QtWidgets ,QtGui
import sys
import qtawesome
from Show.DataDeal import DataDeal

# 文件名：pygui
# 功能：ui 生成美化
# 输入：无
# 输出：ui

class MainUi(QtWidgets.QMainWindow):
    # 初始化
    def __init__(self):
        super().__init__()
        # 右边页数
        self.right_num = 7
        # 显示机器数
        self.mach_num = 3
        # 公告数量
        self.text_num = 10
        self.init_ui()

    # 重写鼠标事件
    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.ismoving = True
            self.start_point = e.globalPos()
            self.window_point = self.frameGeometry().topLeft()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, e):
        if self.ismoving:
            relpos = e.globalPos() - self.start_point
            self.move(self.window_point + relpos)

    def mouseReleaseEvent(self, _):
        self.ismoving = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    # 按钮实例化
    @staticmethod
    def add_but(name ,layout ,local: list ,*content):
        but = QtWidgets.QPushButton(*content)
        but.setObjectName(name)
        layout.addWidget(but ,local[0] ,local[1] ,local[2] ,local[3])
        return but

    # widget 实例化
    @staticmethod
    def create_widget(name ,layout):
        widget = QtWidgets.QWidget()
        widget.setObjectName(name)
        widget.setLayout(layout)
        return widget ,layout

    # label 实例化
    @staticmethod
    def create_label(name ,layout):
        label = QtWidgets.QLabel()
        label.setObjectName(name)
        label.setLayout(layout)
        return label ,layout

    # 主部件初始化
    def init_ui(self):
        # 强制窗口大小
        self.setFixedSize(2000,1250)

        # 创建主窗口部件 布局
        self.main_widget ,self.main_layout = MainUi.create_widget("main_widget" ,QtWidgets.QGridLayout())

        # 创建左窗口部件 布局
        self.left_widget ,self.left_layout = MainUi.create_widget("left_widget" ,QtWidgets.QGridLayout())
        # 左侧菜单栏
        self.init_left_ui()
        # 左侧美化
        self.init_left_ui_qss()

        # 创建右窗口多个部件 布局
        self.right_widget = []
        self.right_layout = []
        for i in range(0 ,self.right_num):
            widget ,layout = MainUi.create_widget("right_widget_"+ str(i) ,QtWidgets.QGridLayout())
            self.right_widget.append(widget)
            self.right_layout.append(layout)

        # 右 0 ui设置
        self.init_right_ui_0()
        self.init_right_ui_1()
        self.init_right_ui_3()
        # 右 0 ui美化
        # 阴影
        self.init_right_ui_0_qss()
        self.init_right_ui_1_qss()
        self.init_right_ui_3_qss()

        # 设置两个窗口比例
        # 格子数确定，行 12，列 2
        self.main_layout.addWidget(self.left_widget ,0 ,0 ,12 ,2)
        # 格子数确定，行 12，列 10
        for i in range(0 ,self.right_num):
            self.main_layout.addWidget(self.right_widget[i] ,0 ,2 ,12 ,10)
            if not i == 0:
                self.right_widget[i].hide()
        # 设置主部件
        self.setCentralWidget(self.main_widget)

    # 设备按钮实例化 "mdi.dishwasher"
    @staticmethod
    def add_boolButton(pic ,content ,layout ,local: list ,x ,y ,style):
        button = QtWidgets.QToolButton()
        if not pic == "":
            button.setIcon(qtawesome.icon(pic ,color= "black"))
        button.setIconSize(QtCore.QSize(x ,y))
        button.setText(content)
        button.setToolButtonStyle(style)

        layout.addWidget(button ,local[0] ,local[1] ,local[2] ,local[3])
        return button

    # 控制页面切换
    def right_move(self ,n):
        for i in range(0 ,self.right_num):
            if str(i) in n: self.right_widget[i].show()
            else: self.right_widget[i].hide()
        # 获取文档
        if "3" in n: self.right_3_getText()

    # 控制大小
    def slot_max_or_recv(self):
        if self.isMaximized(): self.showNormal()
        else: self.showMaximized()

    # 左侧菜单栏
    def init_left_ui(self):
        # 控制按钮
        # 关闭
        self.left_close = MainUi.add_but("" ,self.left_layout ,[0 ,0 ,1 ,1] ,"")
        self.left_close.clicked.connect(self.close)
        # 最小化
        self.left_min = MainUi.add_but("" ,self.left_layout ,[0 ,1 ,1 ,1] ,"")
        self.left_min.clicked.connect(self.showMinimized)
        # 全屏
        self.left_full = MainUi.add_but("" ,self.left_layout ,[0 ,2 ,1 ,1] ,"")
        self.left_full.clicked.connect(self.slot_max_or_recv)

        # 功能栏
        # 生活服务
        self.left_label_serve = MainUi.add_but("left_label" ,self.left_layout ,[1 ,0 ,1 ,3] ,"公共服务")
        # 便利生活
        self.left_label_easy = MainUi.add_but("left_label" ,self.left_layout ,[5 ,0 ,1 ,3] ,"便利生活")
        # 反馈
        self.left_label_help = MainUi.add_but("left_label" ,self.left_layout ,[9 ,0 ,1 ,3] ,"联系帮助")

        # 功能键
        self.left_button = []
        self.left_button.append(MainUi.add_but("left_button_0" ,self.left_layout ,[2 ,0 ,1 ,3] ,qtawesome.icon("mdi.dishwasher" ,color= "white") ," 洗衣服务"))
        self.left_button.append(MainUi.add_but("left_button_1" ,self.left_layout ,[3 ,0 ,1 ,3] ,qtawesome.icon("mdi.tumble-dryer" ,color= "white") ," 烘干服务"))
        self.left_button.append(MainUi.add_but("left_button_2" ,self.left_layout ,[4 ,0 ,1 ,3] ,qtawesome.icon("ei.print" ,color= "white") ," 打印服务"))
        self.left_button.append(MainUi.add_but("left_button_3" ,self.left_layout ,[6 ,0 ,1 ,3] ,qtawesome.icon("mdi.bulletin-board" ,color= "white") ," 公告汇总"))
        self.left_button.append(MainUi.add_but("left_button_4" ,self.left_layout ,[8 ,0 ,1 ,3] ,qtawesome.icon("fa5s.luggage-cart" ,color= "white") ," 外卖综合"))
        self.left_button.append(MainUi.add_but("left_button_5" ,self.left_layout ,[10 ,0 ,1 ,3] ,qtawesome.icon("msc.feedback" ,color= "white") ," 反馈建议"))
        self.left_button.append(MainUi.add_but("left_button_6" ,self.left_layout ,[11 ,0 ,1 ,3] ,qtawesome.icon("ei.thumbs-up" ,color= "white") ," 关注我们"))

        for i in range(0 ,self.right_num):
            self.left_button[i].clicked.connect(lambda: self.right_move(self.sender().objectName()))

    # 左侧美化
    def init_left_ui_qss(self):
        # 设置大小
        self.left_close.setFixedSize(40 ,40)
        self.left_min.setFixedSize(40 ,40)
        self.left_full.setFixedSize(40 ,40)

        # 设置外观
        self.left_close.setStyleSheet("QPushButton{background:#F76677;border-radius:20px;}QPushButton:hover{background:red;}")
        self.left_min.setStyleSheet("QPushButton{background:#F7D674;border-radius:20px;}QPushButton:hover{background:yellow;}")
        self.left_full.setStyleSheet("QPushButton{background:#6DDF6D;border-radius:20px;}QPushButton:hover{background:green;}")

        # 在左侧框设置 QSS
        self.left_widget.setStyleSheet('''
        QPushButton{border:none;color:white;}
        QPushButton#left_label {
            border:none;
            border-bottom:6px solid white;
            font-size:40px;
            font-weight:800;
            font-family: "Microsoft YaHei";
        }
        QPushButton#left_button_0 {font-weight:700;font-size:30px;} QPushButton#left_button_0:hover {border-left:10px solid white;font-weight:700;font-size:30px;}
        QPushButton#left_button_1 {font-weight:700;font-size:30px;} QPushButton#left_button_1:hover {border-left:10px solid white;font-weight:700;font-size:30px;}
        QPushButton#left_button_2 {font-weight:700;font-size:30px;} QPushButton#left_button_2:hover {border-left:10px solid white;font-weight:700;font-size:30px;}
        QPushButton#left_button_3 {font-weight:700;font-size:30px;} QPushButton#left_button_3:hover {border-left:10px solid white;font-weight:700;font-size:30px;}
        QPushButton#left_button_4 {font-weight:700;font-size:30px;} QPushButton#left_button_4:hover {border-left:10px solid white;font-weight:700;font-size:30px;}
        QPushButton#left_button_5 {font-weight:700;font-size:30px;} QPushButton#left_button_5:hover {border-left:10px solid white;font-weight:700;font-size:30px;}
        QPushButton#left_button_6 {font-weight:700;font-size:30px;} QPushButton#left_button_6:hover {border-left:10px solid white;font-weight:700;font-size:30px;}
        QWidget#left_widget{
            background:gray;
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:50px;
            border-bottom-left-radius:50px;
        }
        ''')

    # 右侧触发函数
    def right_0and1_run(self ,text ,ty ,inputs ,buttonList ,time ,dis ,pri):
        if text == "": return
        mixData ,timeData ,disData ,priData = DataDeal.DataMix(text ,ty)
        if mixData == False:
            inputs.setText("无匹配结果，请重新输入。")
            return
        indx = 0
        content = "书院：{}\n\n楼层：{}层\n\n名称：{}\n\n时间：{}min"
        for button in buttonList:
            # 没有足够的机器
            if indx == len(mixData):
                if ty == "4": button.setIcon(qtawesome.icon("mdi.dishwasher-off"))
                else: button.setIcon(qtawesome.icon("mdi.tumble-dryer-off"))
                button.setText("")
                continue

            # 状态设置
            # 空闲
            if mixData[indx][4] == "0":
                if ty == "4": button.setIcon(qtawesome.icon("mdi.dishwasher"))
                else: button.setIcon(qtawesome.icon("mdi.tumble-dryer"))
            else:
                if ty == "4": button.setIcon(qtawesome.icon("mdi.washing-machine"))
                else: button.setIcon(qtawesome.icon("mdi.hair-dryer-outline"))

            # 填充内容
            button.setText(content.format(mixData[indx][0] ,mixData[indx][1] ,mixData[indx][2] ,mixData[indx][3]))
            indx += 1

        content = "{}     {}层     {}     {}min"
        time.setText(content.format(timeData[0], timeData[1], timeData[2], timeData[3]))
        dis.setText(content.format(disData[0], disData[1], disData[2], disData[3]))
        pri.setText(content.format(priData[0], priData[1], priData[2], priData[3]))

    # 右侧页面 0
    def init_right_ui_0(self):
        # 设置搜索框部件
        self.right_0_bar_widget ,self.right_0_bar_layout = self.create_widget("right_0_bar_widget" ,QtWidgets.QGridLayout())
        # 设置搜索标题
        self.right_0_search_icon = QtWidgets.QLabel(chr(0xf002) + " 搜索")
        self.right_0_search_icon.setObjectName("right_0_ser_lable")
        # 设置搜索标题字体
        self.right_0_search_icon.setFont(qtawesome.font("fa" ,32))
        # 设置输入框
        self.right_0_search_input = QtWidgets.QLineEdit()
        # 设置输入框常驻字体
        self.right_0_search_input.setPlaceholderText("输入如: 敬一c,1 ,回车开始搜索")
        # 设置触发函数
        self.right_0_search_input.returnPressed.connect(lambda: self.right_0and1_run(self.right_0_search_input.text() ,"4" ,self.right_0_search_input ,self.right_0_mix_boolButton ,self.right_0_tim_pushButton ,self.right_0_dis_pushButton ,self.right_0_d_pushButton))

        # 加入搜索框部件
        self.right_0_bar_layout.addWidget(self.right_0_search_icon ,0 ,0 ,1 ,1)
        self.right_0_bar_layout.addWidget(self.right_0_search_input ,0 ,1 ,1 ,8)
        # 加入右部件
        self.right_layout[0].addWidget(self.right_0_bar_widget ,0 ,0 ,2 ,9)

        # 添加综合推荐标签
        self.right_0_mix_recommend_label = QtWidgets.QLabel("综合推荐")
        # 设置标签内容
        self.right_0_mix_recommend_label.setObjectName("right_0_lable")

        # 综合推荐列表部件
        self.right_0_mix_recommend_widget ,self.right_0_mix_recommend_layout = self.create_widget("right_0_mix_recommend_widget" ,QtWidgets.QGridLayout())

        # 按钮图片
        self.right_0_mix_boolButton = []
        for i in range(0 ,self.mach_num):
            content = "书院：待输入\n\n楼层：待输入\n\n名称：待输入\n\n时间：待输入"
            local = [0 ,i*7 ,4 ,4]
            self.right_0_mix_boolButton.append(MainUi.add_boolButton("mdi.dishwasher" ,content ,self.right_0_mix_recommend_layout ,local ,240 ,240 ,QtCore.Qt.ToolButtonTextBesideIcon))
            self.right_0_mix_boolButton[i].setMinimumSize(500,240)

        self.right_layout[0].addWidget(self.right_0_mix_recommend_label ,1 ,0 ,2 ,9)
        self.right_layout[0].addWidget(self.right_0_mix_recommend_widget ,2 ,0 ,2 ,9)

        # 添加多种统计
        self.right_0_kind_widget ,self.right_0_kind_layout = MainUi.create_widget("right_0_kind_widget" ,QtWidgets.QGridLayout())
        self.right_0_tim_lable = QtWidgets.QLabel("时间最少")
        self.right_0_tim_lable.setObjectName("right_0_lable")
        self.right_0_tim_pushButton = QtWidgets.QPushButton("东校区一栋     1层     1号机    55min")
        self.right_0_dis_lable = QtWidgets.QLabel("距离最短")
        self.right_0_dis_lable.setObjectName("right_0_lable")
        self.right_0_dis_pushButton = QtWidgets.QPushButton("东校区一栋     1层     1号机    55min")
        self.right_0_d_lable = QtWidgets.QLabel("价格最低")
        self.right_0_d_lable.setObjectName("right_0_lable")
        self.right_0_d_pushButton = QtWidgets.QPushButton("东校区一栋     1层     1号机    55min")
        # 添加入框架
        right_0_kind_layout_len = 4
        self.right_0_kind_layout.addWidget(self.right_0_tim_lable ,0 ,0 ,1 ,right_0_kind_layout_len)
        self.right_0_kind_layout.addWidget(self.right_0_tim_pushButton ,1 ,0 ,1 ,right_0_kind_layout_len)
        self.right_0_kind_layout.addWidget(self.right_0_dis_lable ,2 ,0 ,1 ,right_0_kind_layout_len)
        self.right_0_kind_layout.addWidget(self.right_0_dis_pushButton ,3 ,0 ,1 ,right_0_kind_layout_len)
        self.right_0_kind_layout.addWidget(self.right_0_d_lable ,4 ,0 ,1 ,right_0_kind_layout_len)
        self.right_0_kind_layout.addWidget(self.right_0_d_pushButton ,5 ,0 ,1 ,right_0_kind_layout_len)

        self.right_layout[0].addWidget(self.right_0_kind_widget ,4 ,0 ,3 ,4)

        # 图标说明部件
        self.right_0_state_widget ,self.right_0_state_layout = MainUi.create_widget("right_0_state_widget" ,QtWidgets.QGridLayout())
        self.right_0_state_block = []
        self.right_0_state_block.append(MainUi.add_boolButton("mdi.dishwasher" ,"空闲\n" ,self.right_0_state_layout ,[0 ,0 ,1 ,1] ,220 ,250 ,QtCore.Qt.ToolButtonTextUnderIcon))
        self.right_0_state_block.append(MainUi.add_boolButton("mdi.washing-machine" ,"运行\n" ,self.right_0_state_layout ,[0 ,1 ,1 ,1] ,220 ,250 ,QtCore.Qt.ToolButtonTextUnderIcon))
        self.right_0_state_block.append(MainUi.add_boolButton("mdi.dishwasher-alert" ,"故障\n" ,self.right_0_state_layout ,[1 ,0 ,1 ,1] ,220 ,250 ,QtCore.Qt.ToolButtonTextUnderIcon))
        self.right_0_state_block.append(MainUi.add_boolButton("mdi.dishwasher-off" ,"关机\n" ,self.right_0_state_layout ,[1 ,1 ,1 ,1] ,220 ,250 ,QtCore.Qt.ToolButtonTextUnderIcon))

        self.right_layout[0].addWidget(self.right_0_state_widget ,4 ,4 ,4 ,6)

    # 右 1 ui
    def init_right_ui_1(self):
        # 设置搜索框部件
        self.right_1_bar_widget ,self.right_1_bar_layout = self.create_widget("right_1_bar_widget" ,QtWidgets.QGridLayout())
        # 设置搜索标题
        self.right_1_search_icon = QtWidgets.QLabel(chr(0xf002) + " 搜索")
        self.right_1_search_icon.setObjectName("right_1_ser_lable")
        # 设置搜索标题字体
        self.right_1_search_icon.setFont(qtawesome.font("fa" ,32))
        # 设置输入框
        self.right_1_search_input = QtWidgets.QLineEdit()
        # 设置输入框常驻字体
        self.right_1_search_input.setPlaceholderText("输入如: 敬一c,1 ,回车开始搜索")
        # 设置触发函数
        self.right_1_search_input.returnPressed.connect(lambda: self.right_0and1_run(self.right_1_search_input.text() ,"7" ,self.right_1_search_input ,self.right_1_mix_boolButton ,self.right_1_tim_pushButton ,self.right_1_dis_pushButton ,self.right_1_d_pushButton))

        # 加入搜索框部件
        self.right_1_bar_layout.addWidget(self.right_1_search_icon ,0 ,0 ,1 ,1)
        self.right_1_bar_layout.addWidget(self.right_1_search_input ,0 ,1 ,1 ,8)
        # 加入右部件
        self.right_layout[1].addWidget(self.right_1_bar_widget ,0 ,0 ,2 ,9)

        # 添加综合推荐标签
        self.right_1_mix_recommend_label = QtWidgets.QLabel("综合推荐")
        # 设置标签内容
        self.right_1_mix_recommend_label.setObjectName("right_1_lable")

        # 综合推荐列表部件
        self.right_1_mix_recommend_widget ,self.right_1_mix_recommend_layout = self.create_widget("right_1_mix_recommend_widget" ,QtWidgets.QGridLayout())

        # 按钮图片
        self.right_1_mix_boolButton = []
        for i in range(0 ,self.mach_num):
            content = "书院：待输入   \n\n楼层：待输入\n\n名称：待输入\n\n时间：待输入"
            local = [0 ,i*7 ,4 ,4]
            self.right_1_mix_boolButton.append(MainUi.add_boolButton("mdi.tumble-dryer" ,content ,self.right_1_mix_recommend_layout ,local ,240 ,240 ,QtCore.Qt.ToolButtonTextBesideIcon))
            self.right_1_mix_boolButton[i].setMinimumSize(500,240)

        self.right_layout[1].addWidget(self.right_1_mix_recommend_label ,1 ,0 ,2 ,9)
        self.right_layout[1].addWidget(self.right_1_mix_recommend_widget ,2 ,0 ,2 ,9)

        # 添加多种统计
        self.right_1_kind_widget ,self.right_1_kind_layout = MainUi.create_widget("right_1_kind_widget" ,QtWidgets.QGridLayout())
        self.right_1_tim_lable = QtWidgets.QLabel("时间最少")
        self.right_1_tim_lable.setObjectName("right_1_lable")
        self.right_1_tim_pushButton = QtWidgets.QPushButton("东校区一栋     1层     1号机    55min")
        self.right_1_dis_lable = QtWidgets.QLabel("距离最短")
        self.right_1_dis_lable.setObjectName("right_1_lable")
        self.right_1_dis_pushButton = QtWidgets.QPushButton("东校区一栋     1层     1号机    55min")
        self.right_1_d_lable = QtWidgets.QLabel("价格最低")
        self.right_1_d_lable.setObjectName("right_1_lable")
        self.right_1_d_pushButton = QtWidgets.QPushButton("东校区一栋     1层     1号机    55min")
        # 添加入框架
        right_0_kind_layout_len = 4
        self.right_1_kind_layout.addWidget(self.right_1_tim_lable ,0 ,0 ,1 ,right_0_kind_layout_len)
        self.right_1_kind_layout.addWidget(self.right_1_tim_pushButton ,1 ,0 ,1 ,right_0_kind_layout_len)
        self.right_1_kind_layout.addWidget(self.right_1_dis_lable ,2 ,0 ,1 ,right_0_kind_layout_len)
        self.right_1_kind_layout.addWidget(self.right_1_dis_pushButton ,3 ,0 ,1 ,right_0_kind_layout_len)
        self.right_1_kind_layout.addWidget(self.right_1_d_lable ,4 ,0 ,1 ,right_0_kind_layout_len)
        self.right_1_kind_layout.addWidget(self.right_1_d_pushButton ,5 ,0 ,1 ,right_0_kind_layout_len)

        self.right_layout[1].addWidget(self.right_1_kind_widget ,4 ,0 ,3 ,4)

        # 图标说明部件
        self.right_1_state_widget ,self.right_1_state_layout = MainUi.create_widget("right_1_state_widget" ,QtWidgets.QGridLayout())
        self.right_1_state_block = []
        self.right_1_state_block.append(MainUi.add_boolButton("mdi.tumble-dryer" ,"空闲\n" ,self.right_1_state_layout ,[0 ,0 ,1 ,1] ,220 ,250 ,QtCore.Qt.ToolButtonTextUnderIcon))
        self.right_1_state_block.append(MainUi.add_boolButton("mdi.hair-dryer-outline" ,"运行\n" ,self.right_1_state_layout ,[0 ,1 ,1 ,1] ,220 ,250 ,QtCore.Qt.ToolButtonTextUnderIcon))
        self.right_1_state_block.append(MainUi.add_boolButton("mdi.tumble-dryer-alert" ,"故障\n" ,self.right_1_state_layout ,[1 ,0 ,1 ,1] ,220 ,250 ,QtCore.Qt.ToolButtonTextUnderIcon))
        self.right_1_state_block.append(MainUi.add_boolButton("mdi.tumble-dryer-off" ,"关机\n" ,self.right_1_state_layout ,[1 ,1 ,1 ,1] ,220 ,250 ,QtCore.Qt.ToolButtonTextUnderIcon))

        self.right_layout[1].addWidget(self.right_1_state_widget ,4 ,4 ,4 ,6)

    # 公共框设置
    def right_3_labBuild(self ,name ,layout ,local: list):
        foce_lab ,foce_lab_layout = MainUi.create_label(name ,QtWidgets.QGridLayout())
        foce_lab.setContentsMargins(30 ,0 ,0 ,0)
        tim_lab = QtWidgets.QLabel("07-01")
        tim_lab.setObjectName("right_3_lab")
        tim_lab.setAlignment(QtCore.Qt.AlignCenter)
        tim_lab.setMaximumSize(120 ,60)
        tim_lab.setMinimumSize(120 ,60)
        url_lab = QtWidgets.QLabel("关于桑浦山校区2022级理、工、化学化工、医科学生修读《形势与政策教育（课内）》课的通知")
        url_lab.setObjectName("right_3_lab")
        url_lab.setAlignment(QtCore.Qt.AlignCenter)
        url_lab.setMaximumSize(1160 ,60)
        url_lab.setMinimumSize(1160 ,60)

        foce_lab_layout.addWidget(tim_lab ,0 ,0 ,1 ,2)
        foce_lab_layout.addWidget(url_lab ,0 ,1 ,1 ,8)

        layout.addWidget(foce_lab ,local[0] ,local[1])
        return tim_lab ,url_lab

    def right_3_getText(self):
        data = DataDeal.DataText()
        for i in range(0 ,self.text_num):
            self.right_3_tim_lab[i].setText(data[i][3])
            self.right_3_url_lab[i].setText('''
            <a style= 'color: black; text-decoration: none;'
                href= '{}' >{}
            </a>'''.format(data[i][0] ,data[i][1]))
            self.right_3_url_lab[i].setOpenExternalLinks(True)

    # 右 3 ui
    def init_right_ui_3(self):
        self.right_3_title_widget ,self.right_3_title_layout = MainUi.create_widget("right_3_title_widget" ,QtWidgets.QGridLayout())
        self.right_3_title_lab = QtWidgets.QLabel("公共告示")
        self.right_3_title_layout.addWidget(self.right_3_title_lab)

        self.right_3_list_widget ,self.right_3_list_layout = MainUi.create_widget("right_3_list_widget" ,QtWidgets.QGridLayout())
        # 主框架 共10个
        self.right_3_tim_lab = []
        self.right_3_url_lab = []
        for i in range(0 ,self.text_num):
            lab ,url = self.right_3_labBuild("right_3_foce_lab" ,self.right_3_list_layout ,[i ,1])
            self.right_3_tim_lab.append(lab)
            self.right_3_url_lab.append(url)
        self.right_3_list_widget.setContentsMargins(50 ,0 ,0 ,0)

        self.right_layout[3].addWidget(self.right_3_list_widget ,2 ,2 ,5 ,5)
        self.right_widget[3].setContentsMargins(10 ,20 ,50 ,20)

    # 右 0 ui 美化
    def init_right_ui_0_qss(self):
        # 设置输入框大小
        self.right_0_search_input.setMinimumHeight(70)
        self.right_0_search_input.setStyleSheet ('''
        QLineEdit {
            border:4px solid gray;
            width:300px;
            border-radius:30px;
            padding-left: 25px;
            font-size: 10pt;
            font-family: "Microsoft YaHei"
        }
        ''')

        # 部件设置
        self.right_widget[0].setStyleSheet('''
        QWidget#right_widget_0 {
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:50px;
            border-bottom-right-radius:50px;
        }
        QLabel#right_0_lable {
            border:none;
            font-size:35px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        ''')

        # 综合推荐与图标说明
        self.right_0_mix_recommend_widget.setStyleSheet('''
            QToolButton{border:none;font-size:25px;font-weight:500}
            QToolButton:hover{border-bottom:4px solid #F76677;}
        ''')
        self.right_0_state_widget.setStyleSheet('''
            QToolButton{border:none;font-size:30px;font-weight:500}
            QToolButton:hover{border-bottom:4px solid #F76677;}
        ''')

        # 各种推荐
        self.right_0_kind_widget.setStyleSheet('''
        QPushButton{
            border:none;
            color:gray;
            font-size:30px;
            font-weight:700;
            height:40px;
            padding-left:5px;
            padding-right:10px;
        }
        QPushButton:hover{
            color:black;
            font-size:30px;
            border:1px solid #F3F3F5;
            border-radius:20px;
            background:LightGray;
        }
        ''')

        # 设置窗口透明度
        self.setWindowOpacity(0.9)
        # 设置窗口背景透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 隐藏边框
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # 设置间隙
        self.main_layout.setSpacing(0)

        # 添加阴影
        main_effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        main_effect_shadow.setOffset(0,0)
        main_effect_shadow.setBlurRadius(20)
        main_effect_shadow.setColor(QtCore.Qt.gray)
        self.main_widget.setGraphicsEffect(main_effect_shadow)

    # 右 1 ui 美化
    def init_right_ui_1_qss(self):
        # 设置输入框大小
        self.right_1_search_input.setMinimumHeight(70)
        self.right_1_search_input.setStyleSheet ('''
        QLineEdit {
            border:4px solid gray;
            width:300px;
            border-radius:30px;
            padding-left: 25px;
            font-size: 10pt;
            font-family: "Microsoft YaHei"
        }
        ''')

        # 部件设置
        self.right_widget[1].setStyleSheet('''
        QWidget#right_widget_1 {
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:50px;
            border-bottom-right-radius:50px;
        }
        QLabel#right_1_lable {
            border:none;
            font-size:35px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        ''')

        # 综合推荐与图标说明
        self.right_1_mix_recommend_widget.setStyleSheet('''
            QToolButton{border:none;font-size:25px;font-weight:500;}
            QToolButton:hover{border-bottom:4px solid #F76677;}
        ''')
        self.right_1_state_widget.setStyleSheet('''
            QToolButton{border:none;font-size:30px;font-weight:500;}
            QToolButton:hover{border-bottom:4px solid #F76677;}
        ''')

        # 各种推荐
        self.right_1_kind_widget.setStyleSheet('''
        QPushButton{
            border:none;
            color:gray;
            font-size:30px;
            font-weight:700;
            height:40px;
            padding-left:5px;
            padding-right:10px;
        }
        QPushButton:hover{
            color:black;
            font-size:30px;
            border:1px solid #F3F3F5;
            border-radius:20px;
            background:LightGray;
        }
        ''')

    # 右 3 ui 美化
    def init_right_ui_3_qss(self):
        # 部件设置
        self.right_widget[3].setStyleSheet('''
        QWidget#right_widget_3 {
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:50px;
            border-bottom-right-radius:50px;
        }
        ''')

        self.right_3_list_widget.setStyleSheet('''
        QWidget#right_3_list_widget {
            color:#232C51;
            background:white;
            border-top-right-radius:30px;
            border-bottom-right-radius:30px;
            border-top-left-radius:30px;
            border-bottom-left-radius:30px;
        }
        QLabel#right_3_foce_lab {
            background:white;

        }
        QLabel#right_3_foce_lab:hover {
            background:white;
            border-left:10px solid red;
        }
        QLabel#right_3_lab {
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            font-size:28px;
            font-weight:500;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            text-decoration: none;
        }
        QLabel#right_3_lab:hover {
            color: red
        }
        ''')

        list_effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        list_effect_shadow.setOffset(0,0)
        list_effect_shadow.setBlurRadius(20)
        list_effect_shadow.setColor(QtCore.Qt.gray)
        self.right_3_list_widget.setGraphicsEffect(list_effect_shadow)

def Run():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())