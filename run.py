import pygame, sys
from button import Button
import Player as PlayerClass
import Level as LevelClass
import zombie as ZombieClass

pygame.init()

SCREEN = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Menu")

BG = pygame.image.load("images/background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font/font.ttf", size)

def play():


    # Constants
    WIDTH = 700
    HEIGHT = WIDTH
    RED = (255, 0, 0)
    TILE_SIZE = WIDTH / 20

    bkg_img = pygame.image.load('images/background.png')
    background = pygame.transform.scale(bkg_img,(WIDTH,HEIGHT))

    tile_data = [
        [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 3, 3, 1],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 5],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 5],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [4, 0, 0, 0, 0, 0, 0, 9, 8, 0, 0, 0, 0, 0, 13, 2, 2, 2, 2, 1],
        [4, 0, 0, 0, 0, 0, 13, 3, 6, 0, 0, 0, 0, 0, 0, 7, 3, 3, 1, 1],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [1, 2, 8, 0, 0, 0, 0, 0, 0, 18, 0, 0, -2, 0, 18, 0, 0, 0, 0, 5],
        [1, 1, 6, 0, 0, 0, 0, 0, 0, 0, 13, 2, 2, 12, 0, 0, 0, 0, 0, 5],
        [1, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 6, 0, 0, 0, 0, 0, 0, 5],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 2, 1],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 8, 0, 0, 5],
        [4, 0, -1, 0, 9, 8, 0, 0, 0, 9, 8, 0, 0, 0, 0, 5, 4, 0, 0, 5],
        [1, 2, 2, 2, 1, 4, 0, 0, 0, 5, 1, 2, 8, 0, 0, 5, 4, 0, 0, 5]
    ]

    gravity = 9.8

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    player = PlayerClass.Player(TILE_SIZE, WIDTH, screen, RED, gravity)

    zombie = ZombieClass.Zombie(TILE_SIZE, WIDTH, screen, RED)

    world = LevelClass.CreateLevel(tile_data, TILE_SIZE, player, zombie)

    zombie.getWorld(world)

    player.getWorld(world)
    player.getEnemy(zombie)


    pygame.display.set_caption("Run!")

    clock = pygame.time.Clock()

    running = True

    while running:

        SCREEN.fill("black")

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))

        world.draw(screen)

        zombie.update()
        player.update()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
    
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(120).render("RUN!", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 150))

        PLAY_BUTTON = Button(image=pygame.image.load("images/button.png"), pos=(350, 350), 
                            text_input="PLAY", font=get_font(55), base_color="#d7fcd4", hovering_color="Green")
        
        QUIT_BUTTON = Button(image=pygame.image.load("images/button.png"), pos=(350, 550), 
                            text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
