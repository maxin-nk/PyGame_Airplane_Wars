import pygame
from plane_sprites import *

pygame.init()

screen = pygame.display.set_mode((400, 654))
clock = pygame.time.Clock()

img_bg = pygame.image.load("./images/background.png")
screen.blit(img_bg, (0, 0))

hero = pygame.image.load("./images/hero0.png")
screen.blit(hero, (150, 530))

pygame.display.update()

hero_rect = pygame.Rect(150, 530, 97, 124)



# ------------------------------------------------------------------------------------------------
# 1.创建敌机精灵
enemy = GameSprite("./images/airplane.png")
enemy1 = GameSprite("./images/airplane.png", 2)
# 2.创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# ------------------------------------------------------------------------------------------------
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出...")
            pygame.quit()

            exit()

    hero_rect.y -= 2

    if hero_rect.y <= -124:
        hero_rect.y = 654

    screen.blit(img_bg, (0, 0))
    screen.blit(hero, hero_rect)

# ------------------------------------------------------------------------------------------------
    # 3.让精灵组调用两个方法
    enemy_group.update()
    enemy_group.draw(screen)

# ------------------------------------------------------------------------------------------------
    pygame.display.update()


pygame.quit()