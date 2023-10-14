import pygame
from pygame import locals
from setting import Settings
from buttons import Buttons
import json


class ButtonForBoard(Buttons):
    def __init__(self, rect, color, text, clm):
        super().__init__(rect, color, text, clm)
        self.data_list = text.split(',')
        self.name = self.data_list[0]
        self.score = int(self.data_list[1])
        self.color3 = (173, 216, 230)

    def _blit_self(self):
        # 更新文本的surface对象
        self.text_name = self.font.render(self.name, True, (255, 140, 0))
        self.text_score = self.font.render(str(self.score), True, (0, 255, 0))
        # 获取文本的rect属性
        self.text_name_rect = self.text_name.get_rect()
        self.text_score_rect = self.text_score.get_rect()
        # 绘制实心矩形
        pygame.draw.rect(self.CLM.screen, self.color, self.rect, 0)
        # 绘制空心矩形
        pygame.draw.rect(self.CLM.screen, (0, 0, 0), self.rect, 1)
        # 文本对准中心
        self.text_name_rect.centery = self.rect[1] + self.rect[3] / 2
        self.text_score_rect.centery = self.rect[1] + self.rect[3] / 2
        # 文本相对右移
        self.text_name_rect.x = self.rect[0] + 2
        self.text_score_rect.x = self.rect[0] + self.rect[2] - 25
        # 渲染文本
        self.CLM.screen.blit(self.text_name, self.text_name_rect)
        self.CLM.screen.blit(self.text_score, self.text_score_rect)


class ScoreBoard:
    def __init__(self, pos, file_path, clm):
        self.CLM = clm()
        self.clm = clm
        (self.x, self.y) = pos
        self.students_data = {}

        self.settings = Settings()
        self.width = 100
        self.height = 20
        self.file_path = file_path
        self.button_group = []
        self.choice = None
        self._update_data()
        self.CreatBoard()

    def CreatBoard(self):
        i = 0
        lie = len(self.students_data) // (400 // self.height)  # 计算列数
        name_list = []
        score_list = []

        for k, v in self.students_data.items():
            name_list.append(k)
            score_list.append(str(v))
        for a in range(lie + 1):
            for b in range(400 // self.height):
                try:
                    self.button_group.append(
                        ButtonForBoard((self.x + a * self.width, self.y + b * self.height, self.width, self.height
                                        ), (230, 230, 230), name_list[i] + ',' + score_list[i], self.clm))
                except:
                    break
                i += 1

    def _run(self):
        self._update_data()
        self._update_score()
        for Button in self.button_group:
            Button._run()
            if Button.In_text == self.choice:
                Button.selected = True
            else:
                Button.selected = False

    def _check_button_press(self):
        for Button in self.button_group:
            if Button._check_click():
                self.choice = Button.In_text

            # 按钮判断自己是否被选中
            if Button.In_text == self.choice:
                print(self.choice)
                Button.selected = True
            else:
                Button.selected = False
    def _update_score(self):
        for button in self.button_group:
            for k, v in self.students_data.items():
                if k == button.name:
                    button.score = v

    def _update_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as files:
            self.students_data = json.load(files)

    def _done(self, students_name, mode, rule_index):
        name_list = []
        print(students_name, mode, rule_index)
        for n in self.students_data.keys():
           name_list.append(n)

        for name in name_list:
            if name == students_name:
                print('true')
                if mode == 'plus':
                    self.students_data[name] = self.students_data[name] + self.settings.plus_rules[rule_index]

                elif mode == 'reduce':
                    self.students_data[name] = self.students_data[name] + self.settings.reduce_rules[rule_index]

        with open(self.file_path, 'w', encoding='utf-8') as files:
            json.dump(self.students_data, files, ensure_ascii=False, indent=4)

            # print(self.students_data)
