import pygame
import sys

pygame.init()



black = (0, 0, 0)
white = (255, 255, 255)
screen_hight = 600
screen_width = 600
center_x = screen_width / 2

screen = pygame.display.set_mode((screen_width, screen_hight))

class Line:
    def __init__(self):
        self.offset_x = 35
        self.offset_y = 10
        self.x1 = center_x - self.offset_x
        self.x2 = center_x + self.offset_x
        self.y = screen_hight - self.offset_y
        self.width = 5
        self.line_color = 190, 190, 255
        self.speed = 6


    def draw(self, screen):
        pygame.draw.line(screen, self.line_color, (self.x1, self.y), (self.x2, self.y), self.width)


    def move_left(self):
        self.x1 -= self.speed
        self.x2 -= self.speed

    def move_right(self):
        self.x1 += self.speed
        self.x2 += self.speed   

line = Line()

class Key:

    def __init__(self):
        self.left = pygame.K_LEFT
        self.right = pygame.K_RIGHT
        self.down = pygame.KEYDOWN
        self.esc = pygame.K_ESCAPE
        self.space = pygame.K_SPACE

key = Key() 

class Brick:
    WIDTH = 50
    HIGHT = 20

    def __init__(self, top_x=0, top_y=0):
        self.yellow = 255, 255, 0
        self.blue = 150, 190, 255
        self.top_x = top_x
        self.top_y = top_y

            

    def draw(self, screen):
        pygame.draw.rect(screen, self.yellow, ((self.top_x, self.top_y), (Brick.WIDTH, Brick.HIGHT)))
    
class BrickManager:

    def __init__(self):
        self.number_of_bricks = int(screen_width / Brick.WIDTH)

        self.bricks = []


        for n in range(self.number_of_bricks):
            brick_top_x = n * (Brick.WIDTH + 1)
            self.bricks.append(Brick(brick_top_x, 0))

    def draw(self, screen):
        for b in self.bricks:
            b.draw(screen)

bm = BrickManager()

class BigBall:

    def __init__(self):
        self.color = white
        self.x = center_x
        self.offset_y = screen_hight - 15
        self.radius = 3

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.offset_y), self.radius)

    def move(self):
        self.offset_y -= 1

ball = BigBall()


class BigBallManager:

    def move_with_line(self, line, ball):
        if line.move_left():
            ball.x -= line.speed
            print(ball.x)
        if line.move_right():
            ball.x += line.speed
            print(ball.x)

  

#import ipdb; ipdb.set_trace()

bbm = BigBallManager()

all_instances = [line, key, bm, ball, bbm]
always_moving_instances = []

while True:
    
    screen.fill(black)
    line.draw(screen)
    bm.draw(screen)
    ball.draw(screen)

    for b in always_moving_instances:
        b.move()      

    pygame.time.Clock().tick(500)
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[key.left]:
        line.move_left()
    if keys[key.right]:
        line.move_right()
    if keys[key.space]:
        always_moving_instances.append(ball)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == key.down:
            if event.key == key.esc:
                pygame.quit()
                sys.exit()
            