import sys, random, time, pygame,os
from pygame.locals import *
#全局变量函数
def lucky():
    lucky.one=0
    lucky.two=0

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
pygame.display.set_caption("who is the europeans")
#背景颜色
bg_color = (192,200,192)
#音乐

success = pygame.mixer.Sound("成功.ogg")
start = pygame.mixer.Sound("开始.ogg")
road = pygame.mixer.Sound("道路.ogg")
battle = pygame.mixer.Sound("战斗.ogg")
def loadball(xloc,yloc):
    ball = pygame.image.load('精灵球.png')
    locationxy = [xloc, yloc]
    screen.blit(ball, locationxy)
    pygame.display.flip()
#标题函数
def run_title():
    start.play()
    while True:
        screen.fill(bg_color)
        show_text(screen, (180, 150), u"欧皇鉴定系统", (0, 0, 0), font_size=72)
        show_text(screen, (220, 220), u"Who is the Europeans?", (0, 0, 0), font_size=36)
        show_text(screen, (330, 300), u"开始", (125, 125, 125), font_size=63)
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if  x< 430  and y <380 and x >330 and y >300 :
                    start.stop()
                    run_gameone()
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    start.stop()
                    run_gameone()
        pygame.display.flip()
#游戏场景1函数
def run_gameone():
    #连续响应
    pygame.key.set_repeat(10)
    point=1000
    #处理草丛位图
    grass = pygame.image.load("草丛.png").convert_alpha()
    width, height = grass.get_size()
    grass = pygame.transform.smoothscale(grass,(width * 2,height * 2))
    #处理人物位图
    red = pygame.image.load("赤红.png").convert_alpha()
    width, height = red.get_size()
    red = pygame.transform.smoothscale(red, (width * 2, height * 2))
    #初始随机生成
    num =random.randrange(30,100)
    redranwidth = random.randrange(1, 600)
    redranheight = random.randrange(1, 400)
    grassranwidths=[]
    grassranheights=[]
    for i in range(1, num):
        grassranwidth = random.randrange(1, 750)
        grassranheight = random.randrange(1, 480)
        grassranwidths.append(grassranwidth)
        grassranheights.append(grassranheight)
    road.play()
    # 程序主体
    while True:
        # 事件
        for event in pygame.event.get():
            #关闭事件
            if event.type == pygame.QUIT:
                sys.exit()
            # 移动
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    redranwidth = redranwidth - 5
                    point =point-1
                    if redranwidth <10:
                        redranwidth=10
                    # 碰撞鉴定
                    for i in range(0, num - 1):
                        if grassranwidths[i]<redranwidth<grassranwidths[i]+10   and grassranheights[i]<redranheight<grassranheights[i]+10:
                            step_1 = random.randrange(0, 100)
                            if step_1 < 20:
                                lucky.one=point
                                road.stop()
                                run_pass()
                if event.key == K_RIGHT:
                    redranwidth = redranwidth + 5
                    point = point - 1
                    if redranwidth > 750:
                        redranwidth = 750
                    # 碰撞鉴定
                    for i in range(0, num - 1):
                        if grassranwidths[i]<redranwidth<grassranwidths[i]+10   and grassranheights[i]<redranheight<grassranheights[i]+10:
                            step_1 = random.randrange(0, 100)
                            if step_1 < 20:
                                lucky.one = point
                                road.stop()
                                run_pass()
                if event.key == K_UP:
                    redranheight = redranheight - 5
                    point = point - 1
                    if redranheight <10:
                        redranheight= 10
                    # 碰撞鉴定
                    for i in range(0, num - 1):
                        if grassranwidths[i]<redranwidth<grassranwidths[i]+10   and grassranheights[i]<redranheight<grassranheights[i]+10:
                            step_1 = random.randrange(0, 100)
                            if step_1 < 20:
                                lucky.one = point
                                road.stop()
                                run_pass()
                if event.key == K_DOWN:
                    redranheight = redranheight + 5
                    point = point - 1
                    if redranheight > 480:
                        redranheight= 480
                    #碰撞鉴定
                    for i in range(0, num - 1):
                        if grassranwidths[i]<redranwidth<grassranwidths[i]+10   and grassranheights[i]<redranheight<grassranheights[i]+10:
                            step_1 = random.randrange(0, 100)
                            if step_1 < 20:
                                lucky.one = point
                                road.stop()
                                run_pass()
        # 背景色
        screen.fill(bg_color)
        # 在屏幕的中间绘制人物
        screen.blit(red, (redranwidth, redranheight))
        #随机草丛
        for i in range(0, num - 1):
            screen.blit(grass, (grassranwidths[i], grassranheights[i]))
        pygame.display.flip()
#过场动画函数
def run_pass():
    x=0
    y=0
    battle.play()
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
            run_gametwo()
        pygame.display.flip()
def run_gametwo():
    pygame.key.set_repeat(100)
    #幸运值统计2
    number = 1000
    #处理精灵位图
    poke = random.randrange(0,100)
    if poke <=100:
        pokemon = pygame.image.load("梦幻.png").convert_alpha()
        bark = pygame.mixer.Sound("梦幻.ogg")
    if 7<poke <=25 :
        pokemon = pygame.image.load("皮卡丘.png").convert_alpha()
        bark = pygame.mixer.Sound("皮卡丘.ogg")
        number = number - 50
    if 25<poke <=50 :
        pokemon = pygame.image.load("妙蛙种子.png").convert_alpha()
        bark = pygame.mixer.Sound("妙蛙种子.ogg")
        number = number - 100
    if 50<poke <=75 :
        pokemon = pygame.image.load("小火龙.png").convert_alpha()
        bark = pygame.mixer.Sound("小火龙.ogg")
        number = number - 100
    if 75<poke <=100 :
        pokemon = pygame.image.load("杰尼龟.png").convert_alpha()
        bark = pygame.mixer.Sound("杰尼龟.ogg")
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
    n=0
    # 程序主体
    while True:
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
            if n ==0:
                bark.play()
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
                    n=n+1
                    if event.key == K_UP:
                        if choose > 305:
                            choose = choose - 50
                    if event.key == K_DOWN:
                        if choose < 405:
                            choose = choose + 50
                #选择
                if event.type==KEYUP:
                    n=n+1
                    if event.key==K_SPACE:
                        if tip == "*捕捉成功,再次点击查看结果":
                            run_end()
                        #捕捉
                        if choose ==305:
                            number=number-40
                            chance = random.randrange(0,100)
                            if chance<catch:
                                pokemon = pygame.image.load("精灵球.png").convert_alpha()
                                width, height = pokemon.get_size()
                                pokemon = pygame.transform.smoothscale(pokemon, (width * 4, height * 4))
                                pokemonwidth = 520
                                pokemonheight = 60
                                tip=u"*捕捉成功,再次点击查看结果"
                                battle.stop()
                                success.play()
                                lucky.two=number
                            else :
                                tip=u"*捕捉失败"
                                catch=catch+1
                        #喂养
                        if choose ==355:
                            number=number-50
                            catch = catch +12
                            tip=u"*亲密度上升"
                        if choose == 405:
                            if tip =="*再次按重新开始游戏":
                                battle.stop()
                                run_title()
                            tip = u"*再次按重新开始游戏"


            screen.blit(pian, (520, choose))
        pygame.display.flip()


def run_end():
    end = lucky.one+lucky.two
    while True:
        screen.fill(bg_color)
        show_text(screen, (260, 100), u"得分为{}".format(end), (0, 0, 0), font_size=54)
        show_text(screen, (310, 350), u"回到标题", (125, 125, 125), font_size=40)
        x, y = pygame.mouse.get_pos()
        # 关闭事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if x <= 500 and y <= 400 and x >= 310 and y >= 350:
                    success.stop()
                    run_gameone()
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    success.stop()
                    run_title()
        if end > 1800:
            show_text(screen, (100, 220), u"欧洲霸主，无冕之王", (0, 0, 0), font_size=68)
        if 1500 < end <= 1800:
            show_text(screen, (120, 220), u"纯正血统的欧洲人", (0, 0, 0), font_size=68)
        if 1200 < end <= 1500:
            show_text(screen, (120, 220), u"你应该是欧非混血", (0, 0, 0), font_size=68)
        if 900 < end <= 1200:
            show_text(screen, (120, 220), u"你还是回非洲去吧", (0, 0, 0), font_size=68)
        if 600<end <= 900:
            show_text(screen, (120, 220), u"酋长好！！！！！", (0, 0, 0), font_size=68)
        if end <= 600:
            show_text(screen, (100, 220), u"这号废了，重新练吧", (0, 0, 0), font_size=68)

        pygame.display.flip()
run_title()
