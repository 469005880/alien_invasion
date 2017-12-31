#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame

class Ship():

    def __init__(self, screen, ai_settings):

        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将飞船放在屏幕的底部中央位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #飞船移移动的center属性
        self.center = float(self.rect.centerx)

        #飞船移动标志
        self.moving_right = False
        self.moving_left = False


    def blite_ship(self):
        """显示飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志移动飞船"""
        if self.moving_right :
            if self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left :
            if self.rect.left > self.screen_rect.left :
                self.center -= self.ai_settings.ship_speed_factor

        #根据self.center更新rect对象
        self.rect.centerx = self.center
