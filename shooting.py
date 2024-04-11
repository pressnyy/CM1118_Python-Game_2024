#Import and Initialize Libraries
import pygame
pygame.init()

#Set the Game Window
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

#*************************************************************
#Download Images
walkRightSprites = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
walkLeftSprites = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
alexBackgroundSprite = pygame.image.load('images/bg.png')
#*************************************************************

#Player Class
class player(object):
#Initializer
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
#************************************************************* 
        self.left = False
        self.right = False
        self.walkCount = 0
#************************************************************* 

        self.jumpCount = 10

#************************************************************* 
        self.standing = True
#************************************************************* 


#Moving Animation Method
#************************************************************* 
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeftSprites[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRightSprites[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRightSprites[0], (self.x, self.y))
            else:
                win.blit(walkLeftSprites[0], (self.x, self.y))
#************************************************************* 
                

#Projectile Class
#************************************************************* 
class projectile(object):
#Initializer
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
#Bullet Animation Method
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
#************************************************************* 

#Window Update Function
def redrawGameWindow():
#************************************************************* 
    win.blit(alexBackgroundSprite, (0,0))
    player.draw(win)
    for bullet in bullets:
        bullet.draw(win)
#*************************************************************    
    pygame.display.update()


#Creating Objects
player = player(200, 410, 64, 64)
bullets = []


#Start of the Main Loop
run = True
while run:
    #FPS
    clock = pygame.time.Clock()
    clock.tick(27)

    #Closing the Game Window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Keys Input Function
    keys = pygame.key.get_pressed()

#*************************************************************
    #Disappearing of Bullets  
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
  
    #Shooting Part
    if keys[pygame.K_SPACE]:
        if player.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 10:
            bullets.append(projectile(round(player.x + player.width //2), round(player.y + player.height//2), 6, (255,255,255), facing))
#*************************************************************   
    #Moving Part
    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.vel:
        player.x += player.vel
        player.right = True
        player.left = False
        player.standing = False
    else:
        player.standing = True
        player.walkCount = 0
    
    #Jumping Part    
    if not(player.isJump):
        if keys[pygame.K_UP]:
            player.isJump = True
            player.right = False
            player.left = False
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10
    
    #Updating the Game Window        
    redrawGameWindow()

#End of the Main Loop
pygame.quit()