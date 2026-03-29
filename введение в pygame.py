import pygame
pygame.init()

width=900
height=600
screen=pygame.display.set_mode((width,height))

white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)

clock=pygame.time.Clock()
FPS=30

class Player:
    def __init__(self,x,y,height,width,color):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.color=color
        self.speed=10
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.height,self.width))

    def move(self, keys):
        if keys[pygame.K_w]:
            self.y-=self.speed
        if keys[pygame.K_s]:
            self.y+=self.speed

        if player.y < 0:
            player.y = 0
        if player.y > 600-self.width:
            player.y = 600-self.width
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.height,self.width)
class Player2:
    def __init__(self,x,y,height,width,color):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.color=color
        self.speed=10

    def draw(self, screen2):
        pygame.draw.rect(screen2, self.color, (self.x,self.y,self.height,self.width))

    def move(self, keys2):
        if keys2[pygame.K_UP]:
            self.y-=self.speed
        if keys2[pygame.K_DOWN]:
            self.y+=self.speed

        if player2.y<0:
            player2.y=0
        if player2.y>600-self.width:
            player2.y=600-self.width
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.height,self.width)


class Ball:
    def __init__(self, posx, posy, color):
        self.posx = posx
        self.posy = posy
        self.color = color
        self.speed_x = 7
        self.speed_y = 7
        self.radius = 30

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.posx), int(self.posy)), self.radius)

    def move(self):
        self.posx += self.speed_x
        self.posy += self.speed_y
    def check_border_collision(self,screen_height):
        if ball.posy-ball.radius<=0 or ball.posy+ball.radius>=screen_height:
            ball.speed_y*=-1
            self.speed_x+=0.5
            self.speed_y+=0.5
    def get_rect(self):
        return pygame.Rect(self.posx - self.radius, self.posy - self.radius, self.radius * 2, self.radius * 2)
running=True
player=Player(50,50,30,100,blue)

running2=True
player2=Player2(820,450,30,100,red)

running3=True
ball = Ball(450, 300, black)

score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

while running and running2 and running3:
    screen.fill(white)
    player.draw(screen)
    player2.draw(screen)
    ball.draw(screen)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    keys=pygame.key.get_pressed()
    player.move(keys)

    keys2=pygame.key.get_pressed()
    player2.move(keys2)

    ball.move()

    Ball.check_border_collision(ball,height)

    rect1 = player.get_rect()
    rect2 = player2.get_rect()
    rect3 = ball.get_rect()
    if rect1.colliderect(rect3):
        if ball.speed_x < 0:
            ball.speed_x *= -1
            ball.posx = player.x + player.height + ball.radius

    if rect2.colliderect(rect3):
        if ball.speed_x > 0:
            ball.speed_x *= -1
            ball.posx = player2.x - ball.radius



    if ball.posx < 0:
        score2 += 1
        ball.posx, ball.posy =450,300
        ball.speed_x *= -1

    elif ball.posx > width:
        score1 += 1
        ball.posx, ball.posy =450,300
        ball.speed_x *= -1

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Player 1:{score1} Player 2:{score2}", True, green)
    screen.blit(score_text, (width // 2 - 100, 20))

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()