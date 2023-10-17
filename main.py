import pygame
from sys import exit
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_sprite_1 = pygame.image.load('graphics/player/player_0.png').convert_alpha()
        player_sprite_2 = pygame.image.load('graphics/player/player_1.png').convert_alpha()
        player_sprite_3 = pygame.image.load('graphics/player/player_2.png').convert_alpha()
        self.player_sprites = [player_sprite_1, player_sprite_2, player_sprite_3]
        self.player_sprites_index = 0

        self.y_pos = screen_height / 2

        self.image = self.player_sprites[self.player_sprites_index]
        self.rect = self.image.get_rect(midbottom = (50, self.y_pos))

    def player_animation(self):
        self.player_sprites_index += 0.1
        if self.player_sprites_index >= len(self.player_sprites):
            self.player_sprites_index = 0
        self.image = self.player_sprites[int(self.player_sprites_index)]

    def player_movement(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.y_pos = self.mouse_pos[1]
        self.rect.y = self.y_pos - 40

    def update(self):
        self.player_animation()
        self.player_movement()

    def create_bullet(self):
        return Bullet()

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bullet_1 = pygame.image.load('graphics/bullet/bullet_0.png')
        bullet_2 = pygame.image.load('graphics/bullet/bullet_1.png')
        bullet_3 = pygame.image.load('graphics/bullet/bullet_2.png')
        bullet_4 = pygame.image.load('graphics/bullet/bullet_3.png')
        bullet_5 = pygame.image.load('graphics/bullet/bullet_4.png')
        bullet_6 = pygame.image.load('graphics/bullet/bullet_5.png')
        bullet_7 = pygame.image.load('graphics/bullet/bullet_6.png')
        bullet_8 = pygame.image.load('graphics/bullet/bullet_7.png')

        self.bullet_sprites = [bullet_1, bullet_2, bullet_3, bullet_4, bullet_5,  bullet_6, bullet_7, bullet_8]
        self.bullet_sprites_index = 0

        self.pos_y = pygame.mouse.get_pos()[1]

        self.image  = self.bullet_sprites[self.bullet_sprites_index]
        self.rect =  self.image.get_rect(center = (50, (self.pos_y + 5)))
    
    def bullet_animation(self):
        self.bullet_sprites_index += 0.2
        if self.bullet_sprites_index >= len(self.bullet_sprites):
            self.bullet_sprites_index = 0
        self.image = self.bullet_sprites[int(self.bullet_sprites_index)]
    
    def update(self):
        self.bullet_animation()
        self.rect.x += 5

        if self.rect.x >= (screen_width + 200):
            self.kill()


class Ballon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        red_ballon_sprite_1 = pygame.image.load('graphics/ballon/red_ballon_0.png')
        red_ballon_sprite_2 = pygame.image.load('graphics/ballon/red_ballon_1.png')
        red_ballon_sprite_3 = pygame.image.load('graphics/ballon/red_ballon_2.png')
        red_ballon_sprite_4 = pygame.image.load('graphics/ballon/red_ballon_3.png')
        self.red_ballon_sprites = [red_ballon_sprite_1, red_ballon_sprite_2, red_ballon_sprite_3, red_ballon_sprite_4]
        self.red_ballon_sprite_index = 0
        self.position = [randint(200, 850), screen_height + 50]

        self.image = self.red_ballon_sprites[self.red_ballon_sprite_index]
        self.rect = self.image.get_rect(center = (self.position[0], self.position[1]))

    def ballon_animation(self):
        self.red_ballon_sprite_index += 0.1
        if self.red_ballon_sprite_index >= len(self.red_ballon_sprites):
            self.red_ballon_sprite_index = 0
        self.image = self.red_ballon_sprites[int(self.red_ballon_sprite_index)]

    def update(self):
        self.rect.y -= 2
        if self.rect.y <= - 100:
            self.rect.y = screen_height + 100
        self.ballon_animation()

def bullet_collision():
    pygame.sprite.groupcollide(bullet_group, ballon_group, False, True)

def ballon_setup(ballons):
    for ballon in range(ballons):
        ballon = Ballon()
        ballon_group.add(ballon)

pygame.init()   

screen_width, screen_height = 854, 480

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Penguin Shooter")
clock = pygame.time.Clock()

# Cursor invisivel
pygame.mouse.set_visible(False)

# Groups
player = Player()
player_list = pygame.sprite.GroupSingle()
player_list.add(player)

bullet_group = pygame.sprite.Group()

ballon = Ballon()
ballon_group = pygame.sprite.Group()

score = 0

ballon_setup(10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())
    
    screen.fill('aquamarine')

    bullet_collision()

    # Player
    bullet_group.draw(screen)
    bullet_group.update()
    player_list.draw(screen)
    player_list.update()

    # Ballon
    ballon_group.draw(screen)
    ballon_group.update()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()