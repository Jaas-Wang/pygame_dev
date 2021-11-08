import pygame


class Ship:

    def __init__(self, screen, ai_settings):
        """初始化飞船并设置初始公位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.img_path = self.ai_settings.ship_img_path
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(self.img_path)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将每搜飞船放在屏幕底部中央
        self.center_ship()
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕底部居中"""
        self.centerx = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom


