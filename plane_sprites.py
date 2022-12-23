import random
import pygame
SCREEN_RECT = pygame.Rect(0, 0, 400, 654)  # 屏幕大小的常量
FRAME_PER_SEC = 60                         # 刷新帧率常量
CREATE_ENEMY_EVENT = pygame.USEREVENT      # 创建敌机定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1     # 定义英雄发射子弹常量


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        super().__init__()                          # 1.调用父类的初始化方法
        self.image = pygame.image.load(image_name)  # 2.将图片加载到内存
        self.rect = self.image.get_rect()           # 3.获取图像位置
        self.speed = speed

    def update(self):
        self.rect.y += self.speed                   # 4.在屏幕垂直方向上移动


class BackGround(GameSprite):
    """滚动背景精灵"""
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:                                 # 7.判断是否是交替图像
            self.rect.y = -self.rect.height

    def update(self):
        super().update()                            # 5.调用父类向下移动
        if self.rect.y >= SCREEN_RECT.height:       # 6.判断背景是否移出屏幕
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 调用父类方法，创建敌机精灵，同时制定敌机图片
        super().__init__("./images/airplane.png")
        # 指定敌机的初始随机速度 1-3
        self.speed = random.randint(1, 3)
        # 指定敌机的初始随机位置,初始位置在屏幕上方
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):
        # 调用父类方法，保持垂直方向飞行
        super().update()
        # 判断是否飞出屏幕，飞出，从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Bullet(GameSprite):
    """子弹精灵组"""
    def __init__(self):
        super().__init__("./images/bullet.png", -2)

    def __del__(self):
        print("子弹被销毁.....")

    def update(self):
        # 调用父类方法，让子弹延垂直方向飞行
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()


class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        super().__init__("./images/hero1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 10

        self.bullets = pygame.sprite.Group()         # 创建子弹的精灵组

    def update(self):
        # 英雄在水平方向移动,不需要调用父类方法，因为父类方法完全不能满足子类的需要
        self.rect.x += self.speed
        # 控制英雄不能移出屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("英雄发射子弹....")

        # 1.创建子弹精灵
        bullet = Bullet()
        # 2.设置子弹精灵位置
        bullet.rect.bottom = self.rect.y - 20
        bullet.rect.centerx = self.rect.centerx
        # 3.将子弹添加到精灵组
        self.bullets.add(bullet)
