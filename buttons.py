# 导入pygame
import pygame
# 导入数据共享
import data_share
# 定义按钮类
class Buttons:
    # 按钮的rect，颜色，文本，字体及从main中使用的类
    def __init__(self, rect, color, text, clm):
        # pygame初始化
        pygame.init()
        # 将各变量赋值给相应的类属性
        self.CLM = clm()
        # 按钮内的内容
        self.In_text = text
        # 初始的颜色
        self.color1 = (255, 255, 255)
        # 改变后颜色
        self.color2 = color
        # 选中变色
        self.color3 = (180, 180, 180)
        # 初始化颜色
        self.color = self.color1
        # 按钮的矩阵属性（用于绘制矩形）
        self.rect = rect
        # 导入字体
        self.font = pygame.font.SysFont(self.CLM.font, self.rect[3] - 2)  # 字体大小为按钮的高-2

        # 导入共享文件
        self.data_share = data_share
        # 同步鼠标的x,y坐标
        self.mouse_x, self.mouse_y = self.data_share.mouse_x, self.data_share.mouse_y
        # 自己的被选中状态
        self.selected = False

    # 渲染按钮
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
        # 文本相对右移
        self.text_rect.x = self.rect[0] + 2
        # 渲染文本
        self.CLM.screen.blit(self.text, self.text_rect)

    # 鼠标选中变色
    def _change(self):

        # 侦测鼠标范围
        # 没有被选中且鼠标位于范围内变色
        if self.rect[0] < self.data_share.mouse_x < self.rect[0] + self.rect[2] and self.rect[
            1] < self.data_share.mouse_y < self.rect[1] + self.rect[3] and not self.selected:
            # 将颜色改为被选中时的颜色
            self.color = self.color2
        # 选中变色
        elif self.selected:
            self.color = self.color3
        # 原色
        else:
            self.color = self.color1

    # 侦测鼠标按下状态
    def _check_click(self):
        # 如果鼠标在范围内且鼠标按下就返回值
        if self.color == self.color2:  # 变色表示鼠标在按钮上方
            return True

    # 主运行
    def _run(self):
        # 变色
        self._change()
        # 渲染
        self._blit_self()
