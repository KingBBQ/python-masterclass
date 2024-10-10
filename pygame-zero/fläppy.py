#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:46:48 2024

@author: kingbbq
"""

import pgzrun
import random

WIDTH = 400
HEIGHT = 708
GAP = 300
SPEED = 3

vogel = Actor("p1_stand",(75,200))
rohr_unten = Actor("pokersad", anchor=("left", "top"))
rohr_oben = Actor("pokermad", anchor=("left","bottom"))



def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    rohr_oben.pos = (WIDTH, pipe_gap_y - GAP // 2)
    rohr_unten.pos = (WIDTH, pipe_gap_y + GAP // 2)

def update_pipes():
    rohr_oben.left -= SPEED
    rohr_unten.left -= SPEED
    if rohr_oben.right < 0:
        reset_pipes()


def draw():
    screen.clear()
    # screen.blit('background', (0, 0))
    rohr_oben.draw()
    rohr_unten.draw()
    vogel.draw()
    
    
    
GRAVITY = 0.3

# Initial state of the bird
vogel.dead = False
vogel.vy = 0

def update_bird():
    uy = vogel.vy
    vogel.vy += GRAVITY
    vogel.y += vogel.vy
    vogel.x = 75
    if not vogel.dead:
        if vogel.vy < -3:
            vogel.image = 'p1_duck'
        else:
            vogel.image = 'p1_jump'
    if vogel.colliderect(rohr_oben) or vogel.colliderect(rohr_unten):
        vogel.dead = True
        vogel.image = 'p1_hurt'
    if not 0 < vogel.y < 720:
        vogel.y = 200
        vogel.dead = False
        vogel.vy = 0
        reset_pipes()


FLAP_VELOCITY = -6.5

def on_key_down():
    if not vogel.dead:
        vogel.vy = FLAP_VELOCITY
        
def update():
    update_pipes()
    update_bird()
   
   
pgzrun.go()