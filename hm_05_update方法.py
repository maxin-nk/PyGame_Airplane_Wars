import pygame

pygame.init()  # TODO 1.游戏初始化
# ------------------------------------------------------------------------------------------------
screen = pygame.display.set_mode((400, 654))           # 3.创建游戏窗口 400x654

# TODO 绘制背景图片
img_bg = pygame.image.load("./images/background.png")  # 加载背景数据图像
screen.blit(img_bg, (0, 100))

# TODO 绘制英雄的飞机
hero = pygame.image.load("./images/hero0.png")         # 加载英雄飞机图像
screen.blit(hero, (150, 530))

pygame.display.update()

while True:   # TODO 4.简单的游戏循环
    pass
# -------------------------------------------------------------------------------------------------

pygame.quit()  # TODO 2.游戏退出