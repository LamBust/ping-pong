from pygame import *

font.init()
font = font.SysFont('Arial', 65)

win_width = 1200
win_height = 675

window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('desk.jpg'), (win_width, win_height))
display.set_caption('shooter')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_height, player_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_height, player_width))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
        self.height = player_height
        self.width = player_width
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Rocket1(GameSprite):
    def update(self, key):
        if key[K_s] and self.rect.y < (win_height - self.height - 10):
            self.rect.y + self.speed
        



clock = time.Clock()
FPS = 60

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    clock.tick(FPS)
    window.blit(background, (0,0))

    display.update()