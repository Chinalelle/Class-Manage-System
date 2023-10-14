import pygame
from pygame import locals
# 导入pygame

import sys
# 导入sys
# import json
import setting
# 导入设置模块

import data_share

# 导入按钮模块
from buttons import Buttons
from button_list import ButtonsList
from mode_button import ModeButton
from scoreboard import ScoreBoard

test_list = ['在教室里吃东西扣一分', 'rule2', 'rule3', 'rule4', 'rule5']
test_list2 = ['在教室里吃东西扣两分', 'rule6', 'rule7', 'rule8', 'rule9', 'rule10']


# 定义主程序类
class CLM:
    # 主程序属性
    def __init__(self):
        # 导入设置类
        self.settings = setting.Settings()
        # 创建窗口
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 设置标题
        pygame.display.set_caption('class manage system')
        # 初始化鼠标的x,y坐标
        self.mouse_x, self.mouse_y = 0, 0
        # 初始化鼠标状态
        self.mousedown = False
        # 字体路径
        self.font = self.settings.font
        # 设置时钟
        self.FPSCLOCK = pygame.time.Clock()
        # 设置帧数
        self.FPSCLOCK.tick(60)
        self.button_lists = []
        # 选中的列表
        self.list_choice = None
        # 加分扣分模式
        self.score_mode = 'plus'

        self.students_option = None

        self.plus_rules = []
        for rule in self.settings.plus_rules.keys():
            self.plus_rules.append(rule)
        self.reduce_rules = []
        for rule in self.settings.reduce_rules.keys():
            self.reduce_rules.append(rule)

    # 定义事件检测
    def _check_event(self):
        # 遍历事件
        for event in pygame.event.get():
            # 设置退出
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()
            # 鼠标移动
            if event.type == locals.MOUSEMOTION:
                self.mouse_x, self.mouse_y = event.pos

                # print(self.mouse_x,self.mouse_y)
                data_share.mouse_x, data_share.mouse_y = event.pos
            # 鼠标按下
            if event.type == locals.MOUSEBUTTONDOWN:
                self.mousedown = True
                # print(self.button_lists)
                data_share.mouse_down = True
                self._click_events()
            # 鼠标抬起
            if event.type == locals.MOUSEBUTTONUP:
                self.mousedown = False
                data_share.mouse_down = False

    def _click_events(self):
        Score_Board._check_button_press()
        if Score_Board.choice != None:
            self.students_option = Score_Board.choice
        if Done_Button._check_click():
            Score_Board._done(self.students_option.split(",")[0], self.score_mode, button_list.option)
            print(self.students_option.split(',')[0], self.score_mode, button_list.option_index)
        state = button_list._check_button_press()
        if Mode_Button._check_click() == 'done':

            button_list.option = None
            if Mode_Button.In_text == '+':
                self.score_mode = 'plus'
                button_list.text_list = self.plus_rules
            elif Mode_Button.In_text == '-':
                self.score_mode = 'reduce'
                button_list.text_list = self.reduce_rules
            button_list._update_list()

    # 定义主程序
    def run(self):
        # 程序主循环
        while True:
            self._update_screen()
            self._check_event()

    def _update_screen(self):
        self.screen.fill(self.settings.screen_color)
        button_list._run_self()
        Mode_Button._run()
        Score_Board._run()
        Done_Button._run()
        pygame.display.flip()


# 程序实例化
CMS = CLM()
button_list = ButtonsList(CMS.plus_rules, "test", (250, 425, 350, 20), CLM)
Mode_Button = ModeButton((75, 425, 25, 25), (230, 230, 230), '+', CLM)
Score_Board = ScoreBoard((20, 20), 'students_score_data.json', CLM)
Done_Button = Buttons((800, 425, 100, 20), (230, 230, 230), '执行', CLM)

# CMS.button_lists.append(button_list)
# 执行
CMS.run()
