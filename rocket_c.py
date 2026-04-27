import pygame
#Initialize pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,600))

#Title and icon
pygame.display.set_caption("Space Invaders")
icon= pygame.image.load(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\ovni.png')
pygame.display.set_icon(icon)
#player
img_player = pygame.image.load(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\rocket.png')
player_x=368
player_y=536

def player():
    screen.blit(img_player,(player_x,player_y))
    
#Game loop
is_running= True
while is_running:
    #RGB Background
    screen.fill((205,144,228))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            is_running=False
            
            
    player()
    
    pygame.display.update()
   