import pygame
#Initialize pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,600))

#Title and icon
pygame.display.set_caption("Space Invaders")
icon= pygame.image.load(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\ovni.png')
pygame.display.set_icon(icon)

#Game loop
is_running= True
while is_running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            is_running=False
    screen.fill((205,144,228))
    pygame.display.update()
    