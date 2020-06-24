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

def run_end():
    end = 200+1400

    while True:
        screen.fill(bg_color)
        show_text(screen, (260, 100), u"得分为{}".format(end), (0, 0, 0), font_size=54)
        show_text(screen, (310, 350), u"重新开始", (125, 125, 125), font_size=40)
        x, y = pygame.mouse.get_pos()
        # 关闭事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if  x< 400  and y <200 and x >260 and y >100 :

        if end >1500:
            show_text(screen, (100, 220), u"欧洲霸主，无冕之王", (0, 0, 0), font_size=68)
        if 1200<end <=1500:
            show_text(screen, (100, 220), u"纯正血统的欧洲人", (0, 0, 0), font_size=68)
        if 900<end <=1200:
            show_text(screen, (100, 220), u"你应该是欧非混血", (0, 0, 0), font_size=68)
        if 600<end <=900:
            show_text(screen, (100, 220), u"你还是回非洲去吧", (0, 0, 0), font_size=68)
        if end <=600:
            show_text(screen, (100, 220), u"酋长好！！！！！", (0, 0, 0), font_size=68)


        pygame.display.flip()
run_end()