import sys, random, time, pygame
from pygame.locals import *

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
#背景颜色
bg_color = (192,200,192)
#pygame.key.set_repeat(10)
def run_gametwo():
    #幸运值统计2
    number = 1000
    #处理精灵位图
    poke = random.randrange(0,100)
    if poke <=7 :
        pokemon = pygame.image.load("梦幻.png").convert_alpha()
    if 7<poke <=25 :
        pokemon = pygame.image.load("皮卡丘.png").convert_alpha()
        number = number - 50
    if 25<poke <=50 :
        pokemon = pygame.image.load("妙蛙种子.png").convert_alpha()
        number = number - 100
    if 50<poke <=75 :
        pokemon = pygame.image.load("小火龙.png").convert_alpha()
        number = number - 100
    if 75<poke <=100 :
        pokemon = pygame.image.load("杰尼龟.png").convert_alpha()
        number = number - 100
    width, height = pokemon.get_size()
    pokemon = pygame.transform.smoothscale(pokemon,(width * 3,height * 3))
    pokemonwidth=-150
    pokemonheight=20
    #处理人物位图
    red = pygame.image.load("赤红背影.png").convert_alpha()
    width, height = red.get_size()
    red = pygame.transform.smoothscale(red, (width * 4, height * 4))
    redranwidth = 800
    redranheight = 280
    # 处理其他位图
    pian = pygame.image.load("指向.png").convert_alpha()
    width, height = pian.get_size()
    pian = pygame.transform.smoothscale(pian, (width * 3, height * 3))
    #指针位置
    choose = 305
    #指南
    tip = "*"
    #成功率
    catch = 10
    # 程序主体
    while True:
        if tip = "*捕捉成功":
            run_gametwo()
        # 键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 背景色
        screen.fill(bg_color)
        # 在屏幕中绘制人物
        screen.blit(red, (redranwidth, redranheight))
        if redranwidth>100:
            redranwidth =redranwidth -0.5
        #绘制精灵(过程同上)
        screen.blit(pokemon, (pokemonwidth, pokemonheight))
        if pokemonwidth < 550:
            pokemonwidth = pokemonwidth + 0.5
        #动画结束后事件产生
        if pokemonwidth == 550 :
            #绘制选项框外表
            kuang = pygame.draw.rect(screen, [0, 0, 0], [500, 300, 200, 180], 8)
            show_text(screen, (580, 320), u"捕捉", (0, 0, 0), font_size=40)
            show_text(screen, (580, 370), u"丢饵", (0, 0, 0), font_size=40)
            show_text(screen, (580, 420), u"逃跑", (0, 0, 0), font_size=40)
            show_text(screen, (30, 30), tip, (0, 0, 0), font_size=40)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #选择
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        if choose > 305:
                            choose = choose - 50
                    if event.key == K_DOWN:
                        if choose < 405:
                            choose = choose + 50
                #选择
                if event.type==KEYUP:
                    if event.key==K_SPACE:
                        #捕捉
                        if choose ==305:
                            number=number-50
                            chance = random.randrange(0,100)
                            if chance<catch:
                                pokemon = pygame.image.load("精灵球.png").convert_alpha()
                                width, height = pokemon.get_size()
                                pokemon = pygame.transform.smoothscale(pokemon, (width * 4, height * 4))
                                pokemonwidth = 550
                                pokemonheight = 60
                                tip=u"*捕捉成功"
                            else :
                                tip=u"*捕捉失败"
                                catch=catch+5
                        #喂养
                        if choose ==355:
                            number=number-60
                            catch = catch +10
                            tip=u"*亲密度上升"
                        if choose == 405:
                            tip = u"*再次按键重新开始游戏"
            screen.blit(pian, (520, choose))
        pygame.display.flip()
run_gametwo()