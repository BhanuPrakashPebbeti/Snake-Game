
import pygame
import random
pygame.init()

red = (255,0,0)
red1 = (255,51,51)
orange = (255,128,0)
orange1 = (255,153,51)
yellow = (255,255,0)
green = (128,255,0)
green1 = (0,255,0)
green2=(0,255,128)
blue=(0,255,255)
dblue=(0,128,255)
dblue1=(0,0,255)
violet=(127,0,255)
pink=(255,0,255)
dpink=(255,0,127)
white=(255,255,255)
black=(0,0,0)

screen=pygame.display.set_mode((800,650))
running=True
clock=pygame.time.Clock()

pygame.display.set_caption("SNAKE")
icon=pygame.image.load("cobra.png")
pygame.display.set_icon(icon)

#logo
logo=pygame.image.load('scared.png')

#paused logo
paused_logo=pygame.image.load('snakes.png')

#snake
snakeX_change=0
snakeY_change=0
snakeX=400
snakeY=325
snake_list=[]
length_snake=0

#food
foodX=round((random.randint(0,775))/25.0)*25
foodY=round((random.randint(50,625))/25.0)*25

# Score
global score_value
score_value = 0

def message_to_screen(q,size,colour,x,y):
    message= pygame.font.Font('freesansbold.ttf',size)
    messages=message.render(q,True,colour)
    screen.blit(messages,(x,y))

def pause():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit
                if event.key==pygame.K_SPACE:
                    paused=False
        pygame.draw.rect(screen,black,(0,50,800,600))
        message_to_screen("PAUSED",64,white,255,200)
        screen.blit(paused_logo,(336,60))
        message_to_screen("press spacebar to continue / press q to quit",32,white,50,500)
        clock.tick(15)
        pygame.display.update()

def logos():
    screen.blit(logo,(225,12))

def game_over(q,size,colour,x,y):
    colour=(red,red1,orange,orange1,yellow,green,green1,green2,blue,dblue,dblue1,violet,pink,dpink,white)
    gameover= pygame.font.Font('freesansbold.ttf',size)
    for i in range(15):
        game_overs=gameover.render(q,True,colour[i])
        screen.blit(game_overs,(x,y))
        screen.blit(paused_logo,(336,100))
        clock.tick(10)
        pygame.display.update()
        
def snake(snake_list,len_snake):
    for x,y in snake_list:
        pygame.draw.rect(screen,green,(x+3,y+3,20,20))

def food(x,y):
    pygame.draw.rect(screen,red,(x+3,y+3,20,20))

def eating(snakeX,snakeY,foodX,foodY):
    if (foodX==snakeX and foodY==snakeY):
        return True
    else:
        return False


while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                snakeX_change=0
                snakeY_change=0
                snakeX_change=25
            elif event.key==pygame.K_LEFT:
                snakeX_change=0
                snakeY_change=0
                snakeX_change=-25
            elif event.key==pygame.K_UP:
                snakeX_change=0
                snakeY_change=0
                snakeY_change=-25
            elif event.key==pygame.K_DOWN:
                snakeX_change=0
                snakeY_change=0
                snakeY_change=25
            if event.key==pygame.K_SPACE:
                pause()


    for i in range(0,825,25):
        for j in range(0,675,25):
            if j>=50:
                pygame.draw.line(screen,(255,255,255),(0,j),(800,j),1)
            pygame.draw.line(screen,(255,255,255),(i,50),(i,650),1)

    snakeX+=snakeX_change
    snakeY+=snakeY_change
    if eating(snakeX,snakeY,foodX,foodY):
        score_value+=1
        length_snake+=1
        foodX=round((random.randint(0,775))/25.0)*25
        foodY=round((random.randint(50,625))/25.0)*25

    head=[]
    head.append(snakeX)
    head.append(snakeY)
    snake_list.append(head)
    snake(snake_list,length_snake)
    if len(snake_list)>length_snake:
        del(snake_list[0])

    food(foodX,foodY)
    pygame.draw.rect(screen,dblue,(0,0,800,50))
    pygame.draw.line(screen,yellow,(0,0),(800,0),10)
    pygame.draw.line(screen,yellow,(0,47),(800,47),5)
    
    message_to_screen("Score : " + str(score_value),25,(255,255,255),15,15)
    message_to_screen("SNAKE  XENZIA",40,white,270,10)
    logos()

    if (snakeX<0 or snakeX>775or snakeY<50 or snakeY>625):
        snakeX=2000
        snakeY=2000
        foodX=6000
        foodY=6000
        pygame.draw.rect(screen,black,(0,50,800,600))
        game_over("GAME OVER",100,white,90,295)


    for x,y in snake_list[:-1]:
        if [x,y]==head:
            snakeX=2000
            snakeY=2000
            foodX=6000
            foodY=6000
            pygame.draw.rect(screen,black,(0,50,800,600))
            game_over("GAME OVER",100,white,90,295)

    clock.tick(8)
    pygame.display.update()


