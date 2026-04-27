import pygame
import random

#Initialize pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,600))

#Title and icon
pygame.display.set_caption("Space Invaders")
icon= pygame.image.load(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\ovni.png')
pygame.display.set_icon(icon)
background=pygame.image.load(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\Background.jpg')

#player variables
img_player = pygame.image.load(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\rocket.png')
player_x=368
player_y=500
player_x_change= 0


#Enemy variables
img_enemy=pygame.image.load(r"C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\enemy.png")
enemy_x= random.randint(0,736)
enemy_y=random.randint(50,200)
enemy_x_change=0.5
enemy_y_change=50


#Player function
def player(x,y):
    screen.blit(img_player,(x,y))

#Enemy function
def enemy(x,y):
    screen.blit(img_enemy,(x,y))
    
#Game loop
is_running= True
while is_running:
    #Background
    screen.blit(background,(0,0))
    
    #Event iteration
    for event in pygame.event.get():
        #Event closing
        if event.type== pygame.QUIT:
            is_running=False
        #Press arrow key event
        if event.type== pygame.KEYDOWN:
        
            if event.key==pygame.K_LEFT:
               player_x_change= -1
            if event.key==pygame.K_RIGHT:
               player_x_change= 1
            
        #Realese key event
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                player_x_change= 0
            if event.key == pygame.K_UP or event.key==pygame.K_DOWN:
                player_y_change= 0
    
    #Modify player location               
    player_x+=player_x_change
    
    
    #Keep player insight screen
    if player_x<=0:
        player_x=0
    elif player_x>=736:
        player_x=736

    #Modify enemy location               
    enemy_x+=enemy_x_change
    
    #Keep enemy insight screen
    if enemy_x<=0:
        enemy_x_change=.5
        enemy_y+=enemy_y_change
    elif enemy_x>=736:
        enemy_x_change=-.5
        enemy_y+=enemy_y_change

    player(player_x,player_y)
    enemy(enemy_x,enemy_y)

    
    #Update
    pygame.display.update()
   