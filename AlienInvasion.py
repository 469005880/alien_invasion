#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens  = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, aliens)
        gf.update_alien(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()
