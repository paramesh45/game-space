import  pygame
import random
import math

# initalize pygame
pygame.init()


# creating screen

screen=pygame.display.set_mode((800,600))
# background
background=pygame.image.load("moon.png")

# if we use our system will hang
# while True:
#     pass

# title icon
pygame.display.set_caption("space invaders")
icon=pygame.image.load("interface.png")
pygame.display.set_icon(icon)

# player image
playerimg=pygame.image.load("gaming.png")
playerx=370
playery=480
playerx_change=0

# enemy image
enemyimg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("sign.png"))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,150))
    enemyx_change.append(4)
    enemyy_change.append(40)

# bullet
bulletimg=pygame.image.load("bullet.png")
bulletx=0
bullety=480
bulletx_change=0
bullety_change=10

score_value=0


font=pygame.font.Font("freesansbold.ttf",32)

textx=10
texty=10
over_font=pygame.font.Font("freesansbold.ttf",32)
def show_score(playerx,playery):
    score=font.render("score"+str(score_value),True,(255,255,255))
    screen.blit(score, (playerx, playery))
def game_over_text():
    over_text = over_font.render("game over", True, (255, 255, 255))
    screen.blit(over_text, (200,250))
#ready-- you can't see the bullet it fires wh
# en it is moving
bullet_state="ready"
def player(playerx,playery):
    screen.blit(playerimg,(playerx,playery))

def enemy(enemyx,enemyy,i):
    screen.blit(enemyimg[i],(enemyx,enemyy))
def fire_bullet(bulletx,bullety):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(bulletx+16,bullety+10))

def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((math.pow(enemyx-bulletx,2)+math.pow(enemyy-bullety,2)))
    if distance<27:
        return True
    else:
        return False
# to avoid hanging use below
running=True
while running:
    # background
    screen.fill((255,255,0))
    #screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        # if keystroke is pressed right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change -= 0.3
            if event.key == pygame.K_RIGHT:
                playerx_change += 0.3
            if event.key==pygame.K_SPACE:
                bulletx=playerx
                fire_bullet(playerx,bulletx)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerx_change = 0
            if event.key == pygame.K_RIGHT:
                playerx_change = 0
    playerx+=playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    for i in range(num_of_enemies):
        if enemyy[i] > 440:
            for j in range(num_of_enemies):
                enemyy[j]=2000
            game_over_text()
            break

        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 3
            enemyy[i]+=enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -3
            enemyy[i] += enemyy_change[i]

        collision = iscollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bullety = 480
            bullet_state = "ready"
            score_value += 1

            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)
        enemy(enemyx[i], enemyy[i],i)


    #bullet movement
    if bullety<=0:
        bullety=480
        bullet_state="ready"

    if bullet_state is "fire" :
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
    player(playerx,playery)
    show_score(textx,texty)


    pygame.display.update()