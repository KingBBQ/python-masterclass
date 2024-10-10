import pygame
from pygame.locals import *

pygame.init()

screen_width = 500
screen_hight = 500

#hier wird die map definiert
map = [
[ 0, 0, 4, 0, 0],
[ 0, 0, 0, 0, 0],
[ 0, 0, 1, 0, 0],
[ 0, 0, 0, 0, 0],
[ 2, 2, 2, 2, 2]
]


#hier wird die tile size automatisch angepasst
tile_size = screen_width / len(map)


screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Platformer")


#load images
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')



dirt_tile = pygame.transform.scale(pygame.image.load('img/dirt.png'), (tile_size, tile_size))
lava_tile = pygame.transform.scale(pygame.image.load('img/lava.png'), (tile_size, tile_size))
grass_tile = pygame.transform.scale(pygame.image.load('img/grass.png'), (tile_size, tile_size))
platform_tile = pygame.transform.scale(pygame.image.load('img/platform.png'), (tile_size, tile_size))

def zeichneKarte():
    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (600, 600))
   

   
    zeilen_Nummer = 0
    for zeile in map:
        spalte_Nummer = 0
        for spalte in zeile:
        
            print(spalte_Nummer)
            print(zeilen_Nummer)
            if spalte == 1:
                screen.blit(dirt_tile, (spalte_Nummer * tile_size, zeilen_Nummer * tile_size))
            
            if spalte == 2:
                screen.blit(lava_tile, (spalte_Nummer * tile_size, zeilen_Nummer * tile_size))
            

            if spalte == 3:
                screen.blit(grass_tile, (spalte_Nummer * tile_size, zeilen_Nummer* tile_size))

            if spalte == 4:
                screen.blit(platform_tile, (spalte_Nummer * tile_size, zeilen_Nummer * tile_size))
            spalte_Nummer = spalte_Nummer + 1
        zeilen_Nummer = zeilen_Nummer + 1
    pygame.display.update()

    

zeichneKarte()

run = True
while run == True:

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()