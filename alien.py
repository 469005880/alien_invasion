#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settengs, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settengs = ai_settengs

        #加载外星人图像，并设置其rect属性  
        self.image = pygame.image.load("images/alien.png")
        self.rect =  self.image.get_rect()

        #每个外星人最初都在屏幕的左上角 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的准确位置 
        self.x = float(self.rect.x)

    def blite_alien(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settengs.alien_speed_factor * self.ai_settengs.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人处于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
