from time import sleep
import pygame
import Timer as TimerClass

class Zombie():
##### SET VALUES
    def setStartPos(self,x,y):
        self.startX, self.startY = x, y

##### PLAYER CREATION
    def __init__(self, TILE_SIZE, WIDTH, screen, RED):
        self.i = 0
        self.timer = TimerClass.Timer()

        self.startX, self.startY = 0, 0

        self.state = "moving"
        
        self.decel:float = 1.1
        self.accel:float = 3
        
        self.maxVel:float = 8

        self.vel_x:float = 0
        self.vel_y:float = 0

        self.jumpPower = 16
        self.onFloor = True

        self.WIDTH = WIDTH
        self.screen = screen
        self.RED = RED
        self.TILE_SIZE = TILE_SIZE
        self.size = TILE_SIZE
        self.walkRight = []
        self.walkLeft = []

        self.walkRightFrame = 0
        self.walkLeftFrame = 0

        for i in range(1,5):
            name = 'zombie/R' + str(i) + '.png'
            self.walkRight.append(pygame.image.load(name))

        for i in range(1,5):
            name = 'zombie/L' + str(i) + '.png'
            self.walkLeft.append(pygame.image.load(name))

        self.stand = pygame.image.load('zombie/L1.png')

        self.image = pygame.image.load('zombie/R1.png').convert()
        self.rect = self.image.get_rect()
        self.animation = pygame.transform.scale(self.stand, (self.size, self.size))

        self.rect.x, self.rect.y = self.startX, self.startY

        self.jimmy = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.jimmy.fill((0, 0, 0, 0))

        self.dead = False
        self.xDir = 1

    def goToStartPos(self):
        self.rect.x, self.rect.y = self.startX, self.startY


##### POSITION ADJUSTMENTS
    def getWorld(self, world):
        self.world = world

    # I based the "dash notation" on fighting game notation
    # Based on a keyboard's numpad
    def movementNotation(self):
        if self.xDir == 1:
            self.walkLeftFrame = 0
            self.walkRightFrame += 1
            if (self.walkRightFrame // 16) >= 4:
                self.walkRightFrame = 0
            self.animation = pygame.transform.scale(self.walkRight[self.walkRightFrame//16], (self.size, self.size))
        elif self.xDir == -1:
            self.walkRightFrame = 0
            self.walkLeftFrame += 1
            if (self.walkLeftFrame // 16) >= 4:
                self.walkLeftFrame = 0
            self.animation = pygame.transform.scale(self.walkLeft[self.walkLeftFrame//16], (self.size, self.size))

    def move(self):
        self.movementNotation()
        self.vel_x = 3 * self.xDir

##### UPDATE & DRAW
    def collision(self):
        # Completely breaks if you try to mix the two into a single for loop
        ## HORIZONTAL COLLISION
        for tile in self.world.tile_list:
            if tile[1].colliderect(self.rect.x + self.vel_x, self.rect.y, self.size, self.size):
                if self.rect.right >= (tile[1].left - self.TILE_SIZE) and self.rect.x <= (tile[1].left):
                    self.xDir = -1
                    self.rect.x = tile[1].left - self.TILE_SIZE
                if self.rect.left <= (tile[1].right + self.TILE_SIZE) and self.rect.x >= (tile[1].right):
                    self.xDir = 1
                    self.rect.x = tile[1].right
        for tile in self.world.enemy_list:
            if tile[1].colliderect(self.rect.x + self.vel_x, self.rect.y, self.size, self.size):
                if self.rect.right >= (tile[1].left - self.TILE_SIZE) and self.rect.x <= (tile[1].left):
                    self.xDir = -1
                    self.rect.x = tile[1].left - self.TILE_SIZE
                if self.rect.left <= (tile[1].right + self.TILE_SIZE) and self.rect.x >= (tile[1].right):
                    self.xDir = 1
                    self.rect.x = tile[1].right
                    

    def draw(self):
        self.deathX, self.deathY = self.rect.x, self.rect.y
        
        self.screen.blit(self.animation, self.rect)
        

    def updatePosition(self):
        self.rect.x += self.vel_x * (self.WIDTH/1000)
        self.rect.y += self.vel_y * (self.WIDTH/1000)

    def update(self):
        self.move()
        self.collision()
        self.updatePosition()
        self.draw()