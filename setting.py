import json

import pygame
import os


class Settings:
    def __init__(self):
        pygame.init()
        self.screen_width = 1000
        self.screen_height = 500
        self.screen_color = (255, 255, 255)
        self.mouse_x = 0
        self.mouse_y = 0
        self.mousedown = False
        self.font = "KaiTi"
        self.students_list = []
        self.desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        self.files_done = None
        self.files_path = "D://class manage system"
        self._input_names()
        self.plus_rules = {}
        self.reduce_rules = {}
        # self._reset_score()
        # self._set_rules()
        self._read_rules()

    def _exam_files(self):
        # 如果路径没有文件夹就创建文件夹
        if not os.path.exists(self.files_path):
            os.makedirs(self.files_path)
        # 没有学生名文件就创建
        if not os.path.exists(self.files_path + "//students_name.txt"):
            with open(self.files_path + '//students_name.txt', "w", encoding="utf-8") as files:
                self.files_done = False
                pass
        # 学生名文件为空在桌面创建输入文档
        if os.path.getsize(self.files_path + "//students_name.txt") == 0 and not os.path.exists(
                self.desktop_path + "//students_name_input.txt"):
            with open(self.desktop_path + "//students_name_input.txt", "w", encoding="utf-8") as files:
                self.files_done = False
                pass

    def _input_names(self):
        # 打开桌面文档
        if not os.path.getsize(self.desktop_path + "//students_name_input.txt") == 0:
            with open(self.desktop_path + "//students_name_input.txt", "r", encoding="utf-8") as files:
                with open(self.files_path + '//students_name.txt', "w", encoding="utf-8") as files2:  # 打开学生列表
                    files2.writelines(files.readlines())  # 将桌面文档写入学生列表
        # 再次读取输入后的D盘文件
        with open(self.files_path + '//students_name.txt', "r", encoding="utf-8") as files:
            list = files.readlines()
            if not list == []:
                for i in list:
                    self.students_list.append(i.strip())

    def _reset_score(self):
        students_score = {}
        students_list = []
        if os.path.getsize(self.files_path + '//students_name.txt') != 0:
            with open("students_score_data.json", 'w', encoding='utf-8') as files1:
                with open(self.files_path + '//students_name.txt', 'r', encoding='utf-8') as files2:
                    for name in files2.readlines():
                        students_list.append(name.strip())
                    for student in students_list:
                        students_score[student] = 80
                # print(students_data)
                json.dump(students_score, files1, ensure_ascii=False, indent=4)

    def _read_rules(self):
        with open('rule.json', 'r', encoding='utf-8') as files:
            rule_list = json.load(files)
            self.plus_rules = rule_list[0]
            self.reduce_rules = rule_list[1]

    def _set_rules(self):
        plus_rules = {'在教室里吃东西加一分': 1, 'rule2': 2, 'rule3': 3, 'rule4': 4, 'rule5': 5}
        reduce_rules = {'在教室里吃东西扣两分': -2, 'rule6': -3, 'rule7': -4, 'rule8': -5, 'rule9': -6, 'rule10': -7}
        rule_list = [plus_rules, reduce_rules]
        with open("rule.json", 'w', encoding='utf-8') as files:
            json.dump(rule_list, files, ensure_ascii=False, indent=4)
