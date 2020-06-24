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
def run_title():
    while True:
        screen.fill(bg_color)
        show_text(screen, (180, 150), u"欧皇鉴定系统", (0, 0, 0), font_size=72)
        show_text(screen, (120, 220), u"Who is the Europeans?", (0, 0, 0), font_size=54)
        show_text(screen, (330, 300), u"开始", (125, 125, 125), font_size=63)
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if  x< 430  and y <380 and x >330 and y >300 :
                    run_gameone()

        pygame.display.flip()



rect_list_leftone = [pos_x, 0, 50, 125]
rect_list_lefttwo = [0, 125, 800, 125]
rect_list_rightone = [0, 250, 800, 125]
rect_list_righttwo = [0, 375, 800, 125]