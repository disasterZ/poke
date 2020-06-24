import sys, random, time, pygame,os
from pygame.locals import *

#文本显示
def show_text(surface_handle, pos, text, color, font_bold=False, font_size=13, font_italic=False):
    # 获取系统字体，并设置文字大小
    cur_font = pygame.font.SysFont("SimHei", font_size)
    # 设置是否加粗属性
    cur_font.set_bold(font_bold)
    # 设置是否斜体属性
    cur_font.set_italic(font_italic)
    # 设置文字内容
    text_fmt = cur_font.render(text, 1, color)
    # 绘制文字
    surface_handle.blit(text_fmt, pos)
 #初始化窗口
pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("who is the king")
pygame.key.set_repeat(10)
#背景颜色
bg_color = (192,200,192)

def run_pass():
    x=0
    y=0
    while True:
        screen.fill(bg_color)
        # 关闭事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        rect_list_leftone = [x, 0, 800, 125]
        rect_list_lefttwo = [y, 125, 800, 125]
        rect_list_rightone = [x, 250, 800, 125]
        rect_list_righttwo = [y, 375, 800, 125]
        x=x+0.5
        y=y-0.5
        rect1 = pygame.draw.rect(screen, [0, 0, 0], rect_list_leftone, 0)
        rect2 = pygame.draw.rect(screen, [0, 0, 0], rect_list_rightone, 0)
        rect3 = pygame.draw.rect(screen, [0, 0, 0], rect_list_lefttwo, 0)
        rect4 = pygame.draw.rect(screen, [0, 0, 0], rect_list_righttwo, 0)
        if x>800:
            run_pass()
        pygame.display.flip()
run_pass()