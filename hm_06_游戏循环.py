import pygame

pygame.init()  # TODO 游戏初始化
# ------------------------------------------------------------------------------------------------
screen = pygame.display.set_mode((400, 654))           # 创建游戏窗口 400x654
clock = pygame.time.Clock()                            # 创建游戏时钟

# TODO 绘制背景图片
img_bg = pygame.image.load("./images/background.png")
screen.blit(img_bg, (0, 100))

# TODO 绘制英雄的飞机
hero = pygame.image.load("./images/hero0.png")
screen.blit(hero, (150, 530))

pygame.display.update()

i = 0
while True:   # TODO 游戏循环（意味着游戏的正式开始）
    clock.tick(2)  # 设置屏幕的刷新率
    i += 1
    print(i)
# -------------------------------------------------------------------------------------------------

pygame.quit()  # TODO 游戏退出