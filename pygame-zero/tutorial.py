import pgzrun
import time


WIDTH = 300
HEIGHT = 300


alien = Actor("p1_stand")
alien.pos = 200, 200

def draw():
    screen.fill((0,0,128))
    screen.clear()
    alien.draw()
    
    
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
        
        
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Autschie!")
        alien.image = "p1_hurt"
        time.sleep(1)
        # alien.image = "p1_stand"
        # sounds.eep.play()
    else:
        print("hahaaaa")
    
pgzrun.go()