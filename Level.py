import pygame

class CreateLevel():
    def __init__(self, data, TILE_SIZE, player,zombie):
        self.tile_list = []
        self.collectable_list = []
        self.enemy_list = []
        
        square = pygame.image.load('images/square.png')
        square_bot = pygame.image.load('images/square_bot.png')
        square_top = pygame.image.load('images/square_top.png')
        square_left = pygame.image.load('images/square_left.png')
        square_right = pygame.image.load('images/square_right.png')
        square_bot2 = pygame.image.load('images/square_bot2.png')
        square_top2 = pygame.image.load('images/square_top2.png')
        square_left2 = pygame.image.load('images/square_left2.png')
        square_right2 = pygame.image.load('images/square_right2.png')
        square_botleft = pygame.image.load('images/square_botleft.png')
        square_botright = pygame.image.load('images/square_botright.png')
        square_topleft = pygame.image.load('images/square_topleft.png')
        square_topright = pygame.image.load('images/square_topright.png')
        square_topbot = pygame.image.load('images/square_topbot.png')
        square_leftright = pygame.image.load('images/square_leftright.png')
        square_all = pygame.image.load('images/square_all.png')
        goal = pygame.image.load('images/goalsprite.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == -2:
                    zombie.setStartPos(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    zombie.goToStartPos()
                if tile == -1:
                    player.setStartPos(col_count * TILE_SIZE, row_count * TILE_SIZE)
                    player.goToStartPos()
                if tile == 1:
                    img = pygame.transform.scale(square, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(square_top, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(square_bot, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 4:
                    img = pygame.transform.scale(square_right, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 5:
                    img = pygame.transform.scale(square_left, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 6:
                    img = pygame.transform.scale(square_botright, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 7:
                    img = pygame.transform.scale(square_botleft, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 8:
                    img = pygame.transform.scale(square_topright, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 9:
                    img = pygame.transform.scale(square_topleft, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 10:
                    img = pygame.transform.scale(square_top2, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 11:
                    img = pygame.transform.scale(square_bot2, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 12:
                    img = pygame.transform.scale(square_right2, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 13:
                    img = pygame.transform.scale(square_left2, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 14:
                    img = pygame.transform.scale(square_topbot, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 15:
                    img = pygame.transform.scale(square_leftright, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 16:
                    img = pygame.transform.scale(square_all, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 17:
                    img = pygame.transform.smoothscale(goal, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.collectable_list.append(tile)

                if tile == 18:
                    img = pygame.transform.scale(square_all, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.enemy_list.append(tile)
                
                col_count += 1
            row_count += 1
    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
        for tile in self.collectable_list:
            screen.blit(tile[0], tile[1])