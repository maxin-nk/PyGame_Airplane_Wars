# *-* coding=utf-8 *-*
import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏类"""
    def __init__(self):
        print("游戏初始化")
        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟（后边设置游戏刷新帧率）
        self.clock = pygame.time.Clock()
        # 3.创建精灵/精灵组（背景/敌机/英雄/子弹精灵）
        self.__create_sprites()
        # 4.设置敌机定时器事件（每隔一段时间出来一次）
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 5.设置子弹定时器事件
        pygame.time.set_timer(HERO_FIRE_EVENT, 150)

    def __create_sprites(self):
        # 1.创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(is_alt=True)
        # 2.创建英雄精灵
        self.hero = Hero()

        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __check_collide(self):                # 3.碰撞检测
        # 1.子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 2.敌机摧毁英雄，返回精灵组中碰撞的精灵列表
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 3.判断列表是否有内容
        if len(enemies) > 0:
            # 英雄牺牲
            self.hero.kill()
            over = pygame.image.load("./images/bomb_1.bmp")
            self.screen.blit(over, (self.hero.rect.x, self.hero.rect.y))
            pygame.display.update()
            # 游戏结束
            PlaneGame.__game_over()

    def __update_sprites(self):               # 4.更新（精灵组）显示
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    def __event_handler(self):                    # 2.事件监听
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()                                  # 创建敌机精灵
                self.enemy_group.add(enemy)                      # 将敌机添加到精灵组
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()  # 监听键盘事件
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def start_game(self):
        print("游戏开始...")

        while True:
            # 1.设置时钟刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新精灵组
            self.__update_sprites()
            # 5.刷新整个屏幕
            pygame.display.update()

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':  # 判断是否是主程序
    game = PlaneGame()
    game.start_game()