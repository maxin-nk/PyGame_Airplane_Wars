import pygame

pygame.init()  # 1.游戏初始化

screen = pygame.display.set_mode((400, 654))           # 3.创建游戏窗口 400x654

# ------------------------------------------------------------------------------------------------
# 绘制背景图片
img_bg = pygame.image.load("./images/background.png")  # 5.加载数据图像
screen.blit(img_bg, (0, 100))  # 6.绘制图像（摆放图片位置）
pygame.display.update()        # 7.更新整个屏幕

# 8.绘制英雄的飞机
hero = pygame.image.load("./images/hero0.png")
screen.blit(hero, (150, 530))  # 8.英雄飞机的起始位置
pygame.display.update()


# -------------------------------------------------------------------------------------------------

while True:   # 4.简单的游戏循环
    pass

pygame.quit()  # 2.游戏退出