import pygame
import random
import math

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
img_enemy=[]
enemy_x= []
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
number_of_enemies=8

for e in range(number_of_enemies):
    img_enemy.append(pygame.image.load(r"C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\enemy.png"))
    enemy_x.append(random.randint(0,736))
    enemy_y.append(random.randint(50,200))
    enemy_x_change.append(0.5)
    enemy_y_change.append(50)


#bullet variables
img_bullet=pygame.image.load(r"C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\bullet.png")
bullet_x= player_x
bullet_y=500
bullet_x_change=0
bullet_y_change=1
visible_bullet= False

#score
score=0

#Player function
def player(x,y):
    screen.blit(img_player,(x,y))

#Enemy function
def enemy(x,y):
    screen.blit(img_enemy,(x,y))

#Shoot bullet function
def shoot_bullet(x,y):
    global visible_bullet
    visible_bullet= True
    screen.blit(img_bullet,(x+16,y+10))

#Detect collision
def there_is_a_collision(x_1,y_1,x_2,y_2):
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distance < 27:
        return True
    else:
        return False    
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
        #Press  key event
        if event.type== pygame.KEYDOWN:
        
            if event.key==pygame.K_LEFT:
               player_x_change= -1
            if event.key==pygame.K_RIGHT:
               player_x_change= 1
            if event.key == pygame.K_SPACE:
                if not visible_bullet:
                    bullet_x = player_x
                    bullet_y = 500
                    visible_bullet = True
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
    for enem in range(number_of_enemies):
        enemy_x[enem]+=enemy_x_change[enem]
    #Keep enemy insight screen
    if enemy_x[enem]<=0:
        enemy_x_change[enem]=.5
        enemy_y[enem]+=enemy_y_change[enem]
    elif enemy_x[enem]>=736:
        enemy_x_change[enem]=-.5
        enemy_y[enem]+=enemy_y_change[enem]

    #Bullet movement
    if bullet_y<=-64:
        bullet_y=500
        visible_bullet=False

    if visible_bullet:
        shoot_bullet(bullet_x,bullet_y)
        bullet_y-=bullet_y_change
    #collision
    collision=there_is_a_collision(enemy_x[enem],enemy_y[enem],bullet_x[enem],bullet_y[enem])
    if collision:
        bullet_y = 500
        visible_bullet = False
        score += 1
        print(score)
    

    enemy_x[enem] = random.randint(0,736)
    enemy_y[enem] = random.randint(50,200)

    player(player_x,player_y)
    enemy(enemy_x,enemy_y)

    
    #Update
    pygame.display.update()
   