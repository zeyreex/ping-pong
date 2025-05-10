from random import randint
from time import time as timer

from pygame import *


# Базовый класс для всех спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, size, speed):
        super().__init__()
        # Размер спрайта
        self.size = size
        # Картинка спрайта
        self.image = transform.scale(image.load(img), size)
        # Скорость спрайта
        self.speed = speed
        # "Физическая" модель спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# Класс для спрайта-игрока (стрелочки)
class Player(GameSprite):
    def __init__(self, img, x, y, size, speed, key_up, key_down): 
        super().__init__(img, x, y, size, speed)
        self.key_up = key_up
        self.key_down = key_down
    def update(self):
        keys = key.get_pressed()

        if keys[self.key_up] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[self.key_down] and self.rect.y < win_size[1] - self.size[1] - 5:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, img, x, y, size, speed, speed_x, speed_y):
        super().__init__(img, x, y, size, speed)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce_x(self):
        self.speed_x *= -1

    def bounce_y(self):
        self.speed_y *= -1

# Настройка игровой сцены
win_size = (700, 500)
window = display.set_mode(win_size)
display.set_caption("Пинг-понг")
back_img = image.load("background.jpg")
background = transform.scale(back_img, win_size)

# Параметры игры
game = True
finish = False
clock = time.Clock()
FPS = 60

racket_img = "racket.png"
player_1 = Player(racket_img, 30, 200, (40, 140), 4, K_w, K_s)
player_2 = Player(racket_img, 620, 200, (40, 140), 4, K_UP, K_DOWN)

ball_img = "ball.png"
ball = Ball(ball_img, 300, 300, (40, 40), 0, 3, 3)

# Надписи игры
font.init()
my_font = font.SysFont("verdana", 24)
endgame_font = font.SysFont("verdana", 76)
life_font = font.SysFont("verdana", 60)
win = endgame_font.render("Ты выиграл!", True, (51, 255, 51))
lose = endgame_font.render("Ты проиграл!", True, (255, 51, 51))

# Игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        
        # Отскок от верхней и нижней границ
        if ball.rect.y < 0 or ball.rect.y > win_size[1] - 50:
            ball.bounce_y()

        # Отскок от ракеток
        if sprite.collide_rect(ball, player_1) or sprite.collide_rect(ball, player_2):
            ball.bounce_x()


        player_1.update()
        player_2.update()
        ball.update()

        player_1.reset()
        player_2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)