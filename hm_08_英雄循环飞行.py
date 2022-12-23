import pygame

pygame.init()

screen = pygame.display.set_mode((400, 654))
clock = pygame.time.Clock()

img_bg = pygame.image.load("./images/background.png")
screen.blit(img_bg, (0, 100))

hero = pygame.image.load("./images/hero0.png")
screen.blit(hero, (150, 530))

pygame.display.update()

hero_rect = pygame.Rect(150, 530, 97, 124)

while True:
    clock.tick(60)
    hero_rect.y -= 2
# ------------------------------------------------------------------------------------------------
    # 1.判断飞机的位置
    if hero_rect.y <= -124:
        hero_rect.y = 654
# -------------------------------------------------------------------------------------------------
    screen.blit(img_bg, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()


pygame.quit()