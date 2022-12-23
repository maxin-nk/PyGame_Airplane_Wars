import pygame

pygame.init()

screen = pygame.display.set_mode((400, 654))
clock = pygame.time.Clock()

img_bg = pygame.image.load("./images/background.png")
screen.blit(img_bg, (0, 100))

hero = pygame.image.load("./images/hero0.png")
screen.blit(hero, (150, 530))

pygame.display.update()

# ------------------------------------------------------------------------------------------------
# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 530, 97, 124)

while True:   # TODO 游戏循环（意味着游戏的正式开始）
    clock.tick(60)
    hero_rect.y -= 1
    screen.blit(img_bg, (0, 0))  # 2.解决重影问题（重新绘制背景图像）
    screen.blit(hero, hero_rect)
    pygame.display.update()
# -------------------------------------------------------------------------------------------------

pygame.quit()  # TODO 游戏退出