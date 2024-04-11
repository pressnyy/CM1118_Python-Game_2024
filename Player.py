from time import sleep
import pygame
import Timer as TimerClass

winning = pygame.transform.scale(pygame.image.load('images/winning.png'),(320,80))

class Player():
##### SET VALUES
    def setStartPos(self,x,y):
        self.startX, self.startY = x, y

##### PLAYER CREATION
    def __init__(self, TILE_SIZE, WIDTH, screen, RED, gravity):
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

        for i in range(1,9):
            name = 'images/R' + str(i) + '.png'
            self.walkRight.append(pygame.image.load(name))

        for i in range(1,9):
            name = 'images/L' + str(i) + '.png'
            self.walkLeft.append(pygame.image.load(name))

        self.stand = pygame.image.load('images/standing.png').convert()

        self.image = pygame.image.load('images/guy.png').convert()
        self.rect = self.image.get_rect()

        self.animation = pygame.transform.scale(self.stand, (self.size, self.size))

        self.rect.x, self.rect.y = self.startX, self.startY

        self.jimmy = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.jimmy.fill((0, 0, 0, 0))

        self.dead = False
        self.xDir = 0

        self.gravity = gravity

        self.opacity = 255

        self.rotationAngle = 0
        self.rotationSpeed = 7

        # Length of dash
        self.dashYSpeed = 12
        self.dashXSpeed = 15

        # Frames of dashing
        self.dashFrames = 6
        self.currentDashFrame = 0

        # Can currently dash?
        self.canDash = False
        self.floorDelay = False

        # Dash cooldown
        self.dashCooled = True
        self.lastDashTime = pygame.time.get_ticks()
        self.dashCooldownTimer = 250

        # Hold prevention
        self.hasJumped = False
        self.hasDashed = False

        # More conditions!!
        self.jumpStatus = "allowed"

    def goToStartPos(self):
        self.rect.x, self.rect.y = self.startX, self.startY
            

##### DASHING
# I made further changes from my one.
# I re-added the delay between inputs that Mykyta had made
# and mixed it with the "reset on floor" system I had made.
# This fixes the "infinite dash" issue when you're on the floor!
    def dash(self):
        self.canDash = False
        self.vel_x = 0
        self.vel_y = 0
        self.currentDashFrame += 1

        if self.dir == 1:
            self.vel_x = -self.dashXSpeed * 0.8
            self.vel_y = self.dashYSpeed * 0.8
        if self.dir == 2:
            self.vel_y = self.dashYSpeed
        if self.dir == 3:
            self.vel_x = self.dashXSpeed * 0.8
            self.vel_y = self.dashYSpeed * 0.8
        if self.dir == 4:
            self.vel_x = -self.dashXSpeed
        if self.dir == 6:
            self.vel_x = self.dashXSpeed
        if self.dir == 7:
            self.vel_x = -self.dashXSpeed * 0.8
            self.vel_y = -self.dashYSpeed * 0.8
        if self.dir == 8:
            self.vel_y = -self.dashYSpeed
        if self.dir == 9:
            self.vel_x = self.dashXSpeed * 0.8
            self.vel_y = -self.dashYSpeed * 0.8

        if self.currentDashFrame == self.dashFrames:
            self.state = "moving"
            self.lastDashTime = pygame.time.get_ticks()
            self.currentDashFrame = 0
            self.hasDashed = True

    def dashReset(self):
        currentTime = pygame.time.get_ticks()
        if not self.canDash and currentTime - self.lastDashTime >= self.dashCooldownTimer:
            self.floorDelay = False
        else:
            self.floorDelay = True
        if self.onFloor and not self.floorDelay:
            self.canDash = True
        if self.DASH and self.canDash:
            self.dashing = True
            self.movementNotation()


##### POSITION ADJUSTMENTS
    def getWorld(self, world):
        self.world = world

    def getEnemy(self, zombie):
        self.zombie = zombie

##### DEATH
    def die(self):
        if self.opacity > 0:
            self.opacity -= 5
        self.rotationAngle = (self.rotationAngle + self.rotationSpeed) % 360
        self.animation.set_alpha(self.opacity)
        self.animation = pygame.transform.scale(self.stand, (self.size, self.size))
        self.animation = pygame.transform.rotate(self.animation, self.rotationAngle)
        self.rect = self.animation.get_rect(center=(self.deathX + self.size // 2, self.deathY + self.size // 2))
        self.screen.blit(self.animation, self.rect)
    
        if self.opacity == 0:
            self.opacity = 255
            self.rotationAngle = 0
            rotated_image = pygame.transform.rotate(self.jimmy, self.rotationAngle)
            self.rect = rotated_image.get_rect(center=(self.deathX + self.size // 2, self.deathY + self.size // 2))

            self.vel_x = 0
            self.vel_y = 0

            self.goToStartPos()

            self.state = "moving"
            self.zombie.goToStartPos()
            self.zombie.xDir = 1

            self.timer.startTimer()
        

##### MOVING & INPUTS
    # Please remember to remove the DIE key when finishing up
    def getInput(self):
        keys = pygame.key.get_pressed()
        self.RIGHT = keys[pygame.K_RIGHT]
        self.LEFT = keys[pygame.K_LEFT]
        self.UP = keys[pygame.K_UP]
        self.DOWN = keys[pygame.K_DOWN]

        self.DASH = keys[pygame.K_SPACE]
        self.DIE = keys[pygame.K_k]

        if self.DIE:
            self.state = "dead"

        if not self.DASH:
            self.hasDashed = False

        if not self.UP:
            self.hasJumped = False

    # I based the "dash notation" on fighting game notation
    # Based on a keyboard's numpad
    def movementNotation(self):
        if self.RIGHT:
            self.walkLeftFrame = 0
            self.walkRightFrame += 1
            if (self.walkRightFrame // 16) >= 8:
                self.walkRightFrame = 0
            self.animation = pygame.transform.scale(self.walkRight[self.walkRightFrame//16], (self.size, self.size))
            self.xDir = 1
            if self.UP:
                self.dir = 9
            elif self.DOWN:
                self.dir = 3
            else:
                self.dir = 6
        elif self.LEFT:
            self.walkRightFrame = 0
            self.walkLeftFrame += 1
            if (self.walkLeftFrame // 16) >= 8:
                self.walkLeftFrame = 0
            self.animation = pygame.transform.scale(self.walkLeft[self.walkLeftFrame//16], (self.size, self.size))
            self.xDir = -1
            if self.UP:
                self.dir = 7
            elif self.DOWN:
                self.dir = 1
            else:
                self.dir = 4
        elif self.UP:
            self.dir = 8
            self.xDir = 0
        elif self.DOWN: 
            self.dir = 2
            self.xDir = 0
        else:
            self.xDir = 0
            self.dir = 5

    def move(self):
        if self.xDir != 0:
            self.vel_x = self.vel_x * self.xDir
            if self.vel_x > -(self.maxVel * 0.8) and self.vel_x < 0:
                self.vel_x = 0
            self.vel_x += 1 ** self.accel
            if self.vel_x > self.maxVel:
                self.vel_x = self.maxVel
            self.vel_x = self.vel_x * self.xDir

        else:
            self.walkLeftFrame = 0
            self.walkRightFrame = 0
            self.animation = pygame.transform.scale(self.stand, (self.size, self.size))
            if self.vel_x > 0:
                self.vel_x -= self.decel ** self.accel
            if self.vel_x < 0:
                self.vel_x += self.decel ** self.accel
            if (self.vel_x > -2) and (self.vel_x < 2):
                self.vel_x = 0

        self.vel_y += 1
        if self.vel_y > self.gravity * 2:
            self.vel_y = self.gravity * 2

        if self.rect.y > self.WIDTH - (self.TILE_SIZE * 2):
            self.state = "dead"
        
        self.jump()

        if self.DASH and self.canDash and not self.hasDashed:
            self.state = "dashing"

    def jump(self):
        if self.UP and self.onFloor and not self.hasJumped:
                    self.vel_y = -self.jumpPower
                    self.jumpStatus = "blocked"
                    self.onFloor = False
                    self.hasJumped = True

##### UPDATE & DRAW
    def collision(self):
        # Completely breaks if you try to mix the two into a single for loop
        ## HORIZONTAL COLLISION
        for tile in self.world.tile_list:
                if tile[1].colliderect(self.rect.x + self.vel_x, self.rect.y, self.size, self.size):
                    if self.rect.right >= (tile[1].left - self.TILE_SIZE) and self.rect.x <= (tile[1].left):
                        self.vel_x = 0
                        self.rect.x = tile[1].left - self.TILE_SIZE
                    if self.rect.left <= (tile[1].right + self.TILE_SIZE) and self.rect.x >= (tile[1].right):
                        self.vel_x = 0
                        self.rect.x = tile[1].right
        ## VERTICAL COLLISION
        for tile in self.world.tile_list:
            if tile[1].colliderect(self.rect.x, self.rect.y + self.vel_y, self.size, self.size):
                # Bigger number goes down on screen
                if self.rect.top <= (tile[1].bottom + self.TILE_SIZE) and self.rect.top >= (tile[1].bottom):
                    self.rect.y = tile[1].bottom
                    self.vel_y = 0

                if self.rect.bottom >= (tile[1].top - self.TILE_SIZE) and self.rect.bottom <= (tile[1].top):
                    self.rect.y = tile[1].top - self.TILE_SIZE
                    self.vel_y = 0
                    self.onFloor = True
                else:
                    self.onFloor = False

        for tile in self.world.collectable_list:
            if tile[1].colliderect(self.rect.x, self.rect.y + self.vel_y, self.size, self.size):
                self.state = "win"

        if self.zombie.rect.colliderect(self.rect.x, self.rect.y, self.size, self.size):
            self.state = "dead"
                    

    def draw(self):
        self.deathX, self.deathY = self.rect.x, self.rect.y
        
        self.screen.blit(self.animation, self.rect)
        

    def updatePosition(self):
        self.rect.x += self.vel_x * (self.WIDTH/1000)
        self.rect.y += self.vel_y * (self.WIDTH/1000)

    def update(self):
        self.getInput()

        self.dashReset()

        match self.state:
            case "moving":
                self.timer.countUp(self.screen)
                self.movementNotation()
                self.move()
                self.collision()
                self.updatePosition()
                self.draw()

            case "dashing":
                self.timer.countUp(self.screen)
                self.dash()
                self.collision()
                self.updatePosition()
                self.draw()
        
            case "dead":
                self.timer.countUp(self.screen)
                self.die()

            case "win":
                self.victoryScreen()
            
            case _:
                self.state = "moving"

    def victoryScreen(self):
        self.i += 1
        
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)

        # Font settings
        font = pygame.font.Font(None, 36)
        timer_text = font.render("", True, RED)
        timer_rect = timer_text.get_rect(center=((self.WIDTH - 300) // 2, self.WIDTH // 2))

        winTime = round(self.timer.getTime(),2)

        timer_text = font.render(f"Beat the level in: {winTime:.2f} seconds", True, BLACK)

        
        base_points = 10000
        reduction_factor = 0.02
        reduction_multiplier = (winTime - 5) * reduction_factor
        
        final_points = base_points - (base_points * reduction_multiplier)
        if final_points < 0:
            final_points = 0
        finalPointsss = font.render(f"score: {final_points:.0f}", True, BLACK)
        

        self.screen.blit(timer_text, timer_rect)
        self.screen.blit(finalPointsss, (250, 450))

        self.screen.blit(winning, (250, 250))

        if self.i == 120:
            self.state = "dead"
            self.i = 0