from pygame import *
import random
font.init()
font = font.SysFont('Arial', 65)

win_width = 1200
win_height = 675

racquet_height = 25
racquet_width = 250
racquet_distance = 50 #дистанция от края
racquet_left_x = racquet_distance
racquet_right_x =  win_width - racquet_distance
racquet_speed = 5

ball_side = 50
ball_speed = 2.5

window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('desk.jpg'), (win_width, win_height))
display.set_caption('shooter')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
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

class Rocket_left(GameSprite):
    def update(self, key):
        if key[K_s] and self.rect.y < (win_height - self.width - 10):
            self.rect.y += self.speed
        if key[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed

class Rocket_right(GameSprite):
    def update(self, key):
        if key[K_DOWN] and self.rect.y < (win_height - self.width - 10):
            self.rect.y += self.speed
        if key[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed

right = True 
up = True
left = False
down = False
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height, right, up, left, down):
        super().__init__(player_image, player_x, player_y, player_speed, player_width, player_height)
        self.right = right
        self.up = up
        self.left = left
        self.down = down
    def update(self):
        if self.right:
            self.rect.x += self.speed
        if self.up:
            self.rect.y -= self.speed
        if self.down:
            self.rect.y += self.speed
        if self.left:
            self.rect.x -= self.speed
        if self.rect.y >= (win_height - self.height):
            self.down = False
            self.up = True
        if self.rect.y <= 0:
            self.up = False
            self.down = True
        if self.rect.x >= (win_width - self.width):
            self.right = False
            self.left = True
        if self.rect.x <= 0:
            self.left = False    
            self.right = True

ball = Ball('ball.png', random.randint(400, 600), random.randint(10, (win_height - ball_side - 10)), ball_speed, ball_side, ball_side, right, up, left, down)

rockets = sprite.Group()
rocket1 = Rocket_left('racquet.jpg', racquet_left_x, 250, racquet_speed, racquet_width, racquet_height)      
rocket2 = Rocket_right('racquet.jpg', racquet_right_x, 250, racquet_speed, racquet_width, racquet_height)
rockets.add(rocket1)
rockets.add(rocket2)

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

    ball.show()
    ball.update()

    rockets.draw(window)
    rockets.update(keys_pressed)

    display.update()