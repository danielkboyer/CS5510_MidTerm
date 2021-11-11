#  this pygame simulation will drive a skid-steer (4 wheel) vehicle model for a robot 33 inches wide, by 40 inches long for the planner that you chose.
# the robot will have to navigate a maze of obstacles.

## Some resources I used are from the Following web pages
# Pygame sprite Example https://www.pygame.org/news
# Picture was from https://www.kisspng.com/png-robot-robotic-vacuum-cleaner-irobot-smart-sweepin-255219/preview.html
# sample code from https://www.youtube.com/watch?v=fcryHcZE_sM&t=
# picture: https://opengameart.org/content/animals-pack
# picture: https://opengameart.org/content/smiling-husky-dog-portrait


import pygame
import random
from random import choice
import math
import os ,sys

#WIDTH = 800
#HEIGHT = 600
FPS = 30
WIDTH = 640 * 2
HEIGHT = 480 * 2

#             R    G    B
# define colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BLUE = (0, 0, 255)
ROCKGRAY = (116, 137, 170)
BROWN = (101, 67, 33)
GRAY = (133,133,133)
BGCOLOR = BLACK


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")



def random_vec(mag, side ="", side2 = ""):
    isNagetive = 1
    if random.randrange(0, 10) % 2 == 0:
        isNagetive *= -1
    x_unit = random.uniform(0.0,float(mag)) *isNagetive
    y_unit = math.sqrt(math.pow(mag,2)-math.pow(x_unit,2) ) * isNagetive
    # CHANGE THE DIRECTION

    if side != side2 and side2 != "":
        if side2 == "top" and y_unit < 0:
            y_unit *= -1
        if side2 == "bottom" and y_unit > 0:
            y_unit *= -1

        if side2 == "left" and x_unit < 0:
            x_unit *= -1
        if side2 == "right" and x_unit > 0:
            x_unit *= -1
    else:
        if side =="top" and y_unit < 0:
            y_unit *= -1
        if side =="bottom" and y_unit > 0:
            y_unit *= -1

        if side =="left" and x_unit < 0:
            x_unit *= -1
        if side =="right" and x_unit > 0:
            x_unit *= -1


    return x_unit, y_unit


def top_left(selfSprite,sprite1):
    x1 = selfSprite.rect.center[0]
    y1 = selfSprite.rect.center[1]
    h1 = selfSprite.rect.h
    w1 = selfSprite.rect.w
    x2 = sprite1.rect.center[0]
    y2 = sprite1.rect.center[1]
    h2 = sprite1.rect.h
    w2 = sprite1.rect.w
    if (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2):
        #print("1 TOP LEFT")
        selfSprite.x_speed, selfSprite.y_speed = random_vec(selfSprite.magtude, "top", "left")
        return True
    else:
        return False


def top_right(selfSprite,sprite1):
    x1 = selfSprite.rect.center[0]
    y1 = selfSprite.rect.center[1]
    h1 = selfSprite.rect.h
    w1 = selfSprite.rect.w
    x2 = sprite1.rect.center[0]
    y2 = sprite1.rect.center[1]
    h2 = sprite1.rect.h
    w2 = sprite1.rect.w
    if (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2):
        #print("2 TOP RIGHT")
        selfSprite.x_speed, selfSprite.y_speed = random_vec(selfSprite.magtude, "top", "right")
        return True
    else:
        return False


def bottom_left(selfSprite,sprite1):
    x1 = selfSprite.rect.center[0]
    y1 = selfSprite.rect.center[1]
    h1 = selfSprite.rect.h
    w1 = selfSprite.rect.w
    x2 = sprite1.rect.center[0]
    y2 = sprite1.rect.center[1]
    h2 = sprite1.rect.h
    w2 = sprite1.rect.w
    if (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2):
        #print("3 BOTTOM LEFT")
        selfSprite.x_speed, selfSprite.y_speed = random_vec(selfSprite.magtude, "bottom", "left")
        return True
    else:
        return False


def bottom_right(selfSprite,sprite1):
    x1 = selfSprite.rect.center[0]
    y1 = selfSprite.rect.center[1]
    h1 = selfSprite.rect.h
    w1 = selfSprite.rect.w
    x2 = sprite1.rect.center[0]
    y2 = sprite1.rect.center[1]
    h2 = sprite1.rect.h
    w2 = sprite1.rect.w
    if (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2):
        #print("4 BOOTOM RIGHT")
        selfSprite.x_speed, selfSprite.y_speed = random_vec(selfSprite.magtude, "bottom", "right")
        return True
    else:
        return False


def detectCollisions(selfSprite,sprite1):
    #https://www.dropbox.com/s/wldf3kdylsfxio1/collision_detect.py

    functionList = ["A","B","C","D"]
    random.shuffle(functionList)

    for fun in functionList:
        if fun=="A":
            return top_right(selfSprite, sprite1)
        if fun=="B":
            return top_left(selfSprite, sprite1)
        if fun=="C":
            return bottom_left(selfSprite, sprite1)
        if fun=="D":
            return bottom_right(selfSprite, sprite1)

    return False


class MovingThing(pygame.sprite.Sprite):
    # sprite for the Player

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        x, y = self.rect.center

        if self.rect.top <= 0:
            y = 25
            self.x_speed, self.y_speed = random_vec(self.magtude, "top")

        if self.rect.bottom >= HEIGHT:
            y=HEIGHT - 25
            self.x_speed, self.y_speed = random_vec(self.magtude, "bottom")

        if self.rect.right >= WIDTH:
            x = WIDTH - 25
            self.x_speed, self.y_speed = random_vec(self.magtude, "right")

        if self.rect.left <= 0:
            x = 25
            self.x_speed, self.y_speed = random_vec(self.magtude, "left")

        self.rect.center = (x,y)

    def collisionCheck(self, listofSprites):
        for sprite1 in listofSprites:
            #horzCollision
            if self !=sprite1:
                detectCollisions(self,sprite1)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image
        #self.image = pygame.Surface((50, 50))
        sides = 50  #int(random.randint(50, 200))
        self.image = pygame.Surface( (sides,sides) ).convert()
        #self.image.fill(GREEN)
        self.image.fill((random.randint(1, 250),
                        random.randint(1, 250),
                        random.randint(1, 250)))
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect() #((0,0),(sides,sides)) #
        # center the sprite on the screen

        self.rect.center =(random.randrange(int(self.rect.w/2), int(WIDTH - self.rect.w/2)), random.randrange(int(self.rect.h/2), int(HEIGHT - self.rect.h/2)))


class Robot(MovingThing):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "bot.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(0, WIDTH - 2), random.randrange(0, HEIGHT - 2))
        self.y_speed, self.x_speed = random_vec(7)
        self.magtude = math.sqrt(math.pow(self.x_speed, 2) + math.pow(self.y_speed, 2))






# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
robotList = pygame.sprite.Group()
dogList = pygame.sprite.Group()
obstaclesList = pygame.sprite.Group() #walls and fernitue
listofSprites = pygame.sprite.Group()

for robot in range(0,10):
    robot = Robot()
    all_sprites.add(robot)
    robotList.add(robot)



for obs in range(60,random.randint(80,100)):
    print(str(obs))
    obs = Obstacle()
    obstaclesList.add(obs)
    all_sprites.add(obs)

#all_sprites.add(rommba1,rommba2,rommba3)

# Game loop
running = True
screen.fill(ROCKGRAY)
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    for robot in robotList:
        robot.collisionCheck(all_sprites)
        pygame.draw.circle(screen, WHITE, robot.rect.center, 40)

    #for robot in carpet

    #Crash in to only other dogs
    for dog in dogList:
        dog.collisionCheck(dogList)
        dog.collisionCheck(obstaclesList)
        pygame.draw.circle(screen, GRAY, dog.rect.center, 40)


    # Draw / render

    #screen.fill(ROCKGRAY)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display

    pygame.display.flip()
    pygame.display.update()

pygame.quit()



