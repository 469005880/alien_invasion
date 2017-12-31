#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Settings():
    """存储游戏设置"""
    def __init__(self):

        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5 #飞船的位置参数

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 12
        self.bullet_color = 80,50,50

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20
        self.fleet_direction = 1 #fleet_direction为1表示向右移，为-1表示向左移
