#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif  event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """响应按键与鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets, aliens):
    """更新屏幕上的图像"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blite_ship()
    aliens.draw(screen)
    #刷新绘制的屏幕
    pygame.display.flip()

def update_bullets(bullets, aliens):
    """"更新子弹位置，并删除已消失的子弹"""
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    #检查是否有子弹击中了外星人，若击中，则删除相应的子弹与外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def get_number_alien_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / ( 2 * alien_width ))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number = 1):
    """创建外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width +  2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_alien_row(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - 3*alien_height - ship_height)
    number_row = int(available_space_y / (2 * alien_height))
    return number_row

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_aliens_x  = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_alien_row(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
    """检查外星人是否在边缘"""
    for alien in aliens.sprites():
        if alien.check_edges():

            change_fleet_direction(ai_settings, aliens)
            break

def update_alien(ai_settings, aliens):
    """更新外星人群的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


