
import pygame


class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1700
        self.screen_height = 900
        self.bg_color = (0, 124, 167)

        # 飞船设置
        self.ship_img_path = "images/ship.png"
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        # 外星人设置
        self.alien_img_path = "images/alien.png"
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示向右移动，为 -1 表示向左移动
        self.fleet_direction = 1

        # 设置按钮的尺寸和其他属性
        self.button_width, self.button_height = 200, 50
        self.button_button_color = (0, 255, 0)
        self.button_text_color = (255, 255, 255)
        self.button_font = pygame.font.SysFont(None, 48)

        # 设置得分信息时使用的字体
        self.scoreboard_text_color = (255, 255, 255)
        self.scoreboard_font = pygame.font.SysFont(None, 48)

        # 以什么样的速度加快游戏的节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction 为 1 表示向右；为 -1 表示向左
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)



