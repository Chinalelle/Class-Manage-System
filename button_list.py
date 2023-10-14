
from buttons import Buttons
import math
import pygame
from setting import Settings
import data_share
#定义按钮列表
class ButtonsList():
    def __init__(self, text_list, list_name, rect, clm):
        #设置共享变量
        self.data_share = data_share
        # 为button提供类名
        self.clm = clm
        # 导入设置
        self.settings = Settings()
        # 实例化主程序类
        self.CLM = clm()
        # 初始化储存按钮的列表
        self.buttons_group = []
        # 导入按钮列表
        self.text_list = text_list
        # 设置按钮列表名
        self.list_name = list_name
        # 设置按钮的rect参数
        self.button_rect = rect
        # 设置按钮中的字体
        self.font = self.CLM.font
        # 设置展开后的rect参数
        self.list_rect = (
         self.button_rect[0], self.button_rect[1] - len(self.text_list) * self.button_rect[3], self.button_rect[2],
         (len(self.text_list)+1) * self.button_rect[3])
        # 创建控制按钮列表的主按钮
        self.main_button = Buttons(self.button_rect, (230, 230, 230), self.list_name, self.clm)
        # 初始化按钮列表中选中的按钮名
        self.option = None
        # 创建按钮列表
        self._update_list()
        # 初始化运行状态为False
        self.running = False

        self.option_index = 0

    # 定义创建按钮列表
    def _update_list(self):
        # 便利提供的按钮名列表
        self.buttons_group.clear()
        for i in range(len(self.text_list)):
            # 创建文本为按钮名的按钮对象
            button = Buttons((self.button_rect[0], self.button_rect[1] - (i + 1) * self.button_rect[3],
                              self.button_rect[2], self.button_rect[3]), (230, 230, 230)
                             , self.text_list[i], self.clm)
            # 将按钮对象加入到按钮列表中
            self.buttons_group.append(button)



    # 在鼠标按下时检测鼠标位置并执行相应指令

    def _check_button_press(self):
        for button in self.buttons_group:
            if button._check_click():
                self.option = button.In_text  # button._check_click会检测鼠标按下并返回对应的按钮名
                for i in range(len(self.text_list)):
                    if self.text_list[i] == self.option:
                        self.option_index = i

            # 按钮判断自己是否被选中
            if button.In_text == self.option:
                button.selected = True
            else:
                button.selected = False
        # 鼠标在范围内的判定
        if self.button_rect[0] < self.main_button.data_share.mouse_x < self.button_rect[0] + self.main_button.rect[2] and self.button_rect[
            1] < self.main_button.data_share.mouse_y < self.button_rect[1] + self.button_rect[3]:
            # 若鼠标在主按钮上
            # 若没有运行，则开始
            if not self.running:
                # 将运行状态设为True
                self.running = True
                return True

            # 若正在运行，则停止
        if self.running:
                # 将运行状态设为False
            self.running = False
                # 表示没有选中的按钮
            #self.option = None
            return False
        # # 鼠标不在大范围中的判定
        # if not (self.list_rect[0] < self.main_button.data_share.mouse_x < self.list_rect[0] + self.list_rect[2] and self.list_rect[1] < self.main_button.data_share.mouse_y < self.list_rect[1] + self.list_rect[3]) and self.running == True:
        #     self.running = False
        #     self.option = None

    # 按钮列表的主运行
    def _run_self(self):
        # 运行主按钮
        if self.option == None:
            self.main_button.In_text = self.list_name
        else:
            self.main_button.In_text = self.option
        self.main_button._run()
        # 画出表示状态的三角形
        self._state()

    def _run_list(self):
        # 运行所有按钮
        # 便利按钮列表中的所有按钮并运行
        for button in self.buttons_group:
            # 运行按钮
            button._run()

    # 画出表示状态的三角形
    def _state(self):
        if self.running == True:
            pos_list = [(self.button_rect[0] + self.button_rect[2] - 20, self.button_rect[1] + self.button_rect[3] - self.button_rect[3] / 4),
                        # 顶点坐标算法
                        (self.button_rect[0] + self.button_rect[2] - 20 + math.tan(math.radians(35)) * self.button_rect[
                            3] / 2, self.button_rect[1] + self.button_rect[3] - self.button_rect[3] / 4 * 3),  # 右上点坐标
                        (self.button_rect[0] + self.button_rect[2] - 20 - math.tan(math.radians(35)) * self.button_rect[
                            3] / 2, self.button_rect[1] + self.button_rect[3] - self.button_rect[3] / 4 * 3)]  # 左上点坐标
            pygame.draw.polygon(self.CLM.screen, (0, 0, 0), pos_list)
            self._run_list()
        else:
            pos_list = [(self.button_rect[0] + self.button_rect[2] - 20, self.button_rect[1] + self.button_rect[3] / 4),
                        # 顶点坐标算法
                        (self.button_rect[0] + self.button_rect[2] - 20 + math.tan(math.radians(35)) * self.button_rect[
                            3] / 2, self.button_rect[1] + self.button_rect[3] / 4 * 3),  # 右下点坐标
                        (self.button_rect[0] + self.button_rect[2] - 20 - math.tan(math.radians(35)) * self.button_rect[
                            3] / 2, self.button_rect[1] + self.button_rect[3] / 4 * 3)]  # 左下点坐标
            pygame.draw.polygon(self.CLM.screen, (0, 0, 0), pos_list)