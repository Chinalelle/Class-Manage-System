
import pygame
from buttons import Buttons

class ModeButton(Buttons):
    def __init__(self,rect, color, text, clm):
        super().__init__(rect, color, text, clm)
    def _check_click(self):
        # 如果鼠标在范围内且鼠标按下就返回值
        if self.color == self.color2:  # 变色表示鼠标在按钮上方
            if self.In_text == '+':
                self.In_text = '-'

            elif self.In_text == '-':
                self.In_text = '+'
            return 'done'
    def _blit_self(self):
        # 更新文本的surface对象
        self.text = self.font.render(self.In_text, True, (0, 0, 0))
        # 获取文本的rect属性
        self.text_rect = self.text.get_rect()
        # 绘制实心矩形
        pygame.draw.rect(self.CLM.screen, self.color, self.rect, 0)
        # 绘制空心矩形
        pygame.draw.rect(self.CLM.screen, (0, 0, 0), self.rect, 1)
        # 文本对准中心
        self.text_rect.centery = self.rect[1] + self.rect[3] / 2
        self.text_rect.centerx = self.rect[0] + self.rect[2] / 2
        # 渲染文本
        self.CLM.screen.blit(self.text, self.text_rect)
