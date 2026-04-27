import pygame
import random
import math

#Initialize pygame
pygame.init()
pygame.mixer.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\ovni.png')
pygame.display.set_icon(icon)
background = pygame.image.load(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\Background.jpg')

#Music and sounds
pygame.mixer.music.load(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\background_music.mp3')
pygame.mixer.music.play(-1)

shot_sound = pygame.mixer.Sound(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\shot.mp3')
explosion_sound = pygame.mixer.Sound(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\punch.mp3')

#player variables
img_player = pygame.image.load(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\rocket.png')
player_x = 368
player_y = 500
player_x_change = 0

#Enemy variables
number_of_enemies = 8

img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

for e in range(number_of_enemies):
    img_enemy.append(
        pygame.image.load(
            r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\enemy.png'
        )
    )

    enemy_x.append(random.randint(0,736))
    enemy_y.append(random.randint(50,200))
    enemy_x_change.append(0.5)
    enemy_y_change.append(40)

#bullet variables
img_bullet = pygame.image.load(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 10\bullet.png')
bullet_x = 0
bullet_y = 500
bullet_y_change = 3
visible_bullet = False

#score variables
score = 0
font = pygame.font.Font(None,40)

#game over variables
big_font = pygame.font.Font(None,80)

#Player function
def player(x,y):
    screen.blit(img_player,(x,y))

#Enemy function
def enemy(x,y,e):
    screen.blit(img_enemy[e],(x,y))

#Shoot bullet function
def shoot_bullet(x,y):
    global visible_bullet
    visible_bullet = True
    screen.blit(img_bullet,(x+16,y+10))

#Show score function
def show_score():
    text = font.render("Score: " + str(score),True,(255,255,255))
    screen.blit(text,(10,10))

#Game over function
def game_over():
    text = big_font.render("GAME OVER",True,(255,0,0))
    screen.blit(text,(220,250))

#Detect collision
def there_is_a_collision(x_1,y_1,x_2,y_2):
    distance = math.sqrt((x_1-x_2)**2 + (y_1-y_2)**2)

    if distance < 27:
        return True
    else:
        return False

#Game loop
is_running = True

while is_running:

    #Background
    screen.blit(background,(0,0))

    #Event iteration
    for event in pygame.event.get():

        #Event closing
        if event.type == pygame.QUIT:
            is_running = False

        #Press key event
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_x_change = -1.5

            if event.key == pygame.K_RIGHT:
                player_x_change = 1.5

            if event.key == pygame.K_SPACE:

                if not visible_bullet:
                    shot_sound.play()
                    bullet_x = player_x
                    bullet_y = player_y
                    visible_bullet = True

        #Release key event
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    #Modify player location
    player_x += player_x_change

    #Keep player insight screen
    if player_x <= 0:
        player_x = 0

    elif player_x >= 736:
        player_x = 736

    #Modify enemy location
    for e in range(number_of_enemies):

        enemy_x[e] += enemy_x_change[e]

        #Keep enemy insight screen
        if enemy_x[e] <= 0:
            enemy_x_change[e] = 0.5
            enemy_y[e] += enemy_y_change[e]

        elif enemy_x[e] >= 736:
            enemy_x_change[e] = -0.5
            enemy_y[e] += enemy_y_change[e]

        #Game over
        if enemy_y[e] > 440:

            for j in range(number_of_enemies):
                enemy_y[j] = 2000

            game_over()
            break

        #Collision
        collision = there_is_a_collision(
            enemy_x[e],enemy_y[e],
            bullet_x,bullet_y
        )

        if collision:

            explosion_sound.play()

            bullet_y = 500
            visible_bullet = False

            score += 1

            enemy_x[e] = random.randint(0,736)
            enemy_y[e] = random.randint(50,200)

        enemy(enemy_x[e],enemy_y[e],e)

    #Bullet movement
    if bullet_y <= -64:
        bullet_y = 500
        visible_bullet = False

    if visible_bullet:
        shoot_bullet(bullet_x,bullet_y)
        bullet_y -= bullet_y_change

    player(player_x,player_y)
    show_score()

    #Update
    pygame.display.update()