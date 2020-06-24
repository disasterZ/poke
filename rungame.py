import sys, random, time, pygame
from pygame.locals import *



 #初始化窗口
pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("who is the king")
pygame.key.set_repeat(10)
#背景颜色
bg_color = (192,200,192)
def run_gameone():
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

    # 程序主体
    while True:
        # 键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 移动
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    redranwidth = redranwidth - 5
                    if redranwidth <10:
                        redranwidth=10
                if event.key == K_RIGHT:
                    redranwidth = redranwidth + 5
                    if redranwidth > 750:
                        redranwidth = 750
                if event.key == K_UP:
                    redranheight = redranheight - 5
                    if redranheight <10:
                        redranheight= 10
                if event.key == K_DOWN:
                    redranheight = redranheight + 5
                    if redranheight > 480:
                        redranheight= 480
        # 背景色
        screen.fill(bg_color)
        # 在屏幕的中间绘制人物
        screen.blit(red, (redranwidth, redranheight))
        for i in range(0, num - 1):
            screen.blit(grass, (grassranwidths[i], grassranheights[i]))

        # visualiaze the window
        pygame.display.flip()