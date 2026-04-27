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
player_x_change= 0
player_y_change= 0
def player(x,y):
    screen.blit(img_player,(x,y))
    
#Game loop
is_running= True
while is_running:
    #RGB Background
    screen.fill((205,144,228))
    
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            is_running=False
        if event.type== pygame.KEYDOWN:
        
            if event.key==pygame.K_LEFT:
               player_x_change= -.3
            if event.key==pygame.K_RIGHT:
               player_x_change= .3
            if event.key==pygame.K_UP:
               player_y_change= -.3
            if event.key==pygame.K_DOWN:
               player_y_change= .3
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                player_x_change= 0
            if event.key == pygame.K_UP or event.key==pygame.K_DOWN:
                player_y_change= 0
                   
    player_x+=player_x_change
    player_y+=player_y_change
    player(player_x,player_y)
    
    pygame.display.update()
   