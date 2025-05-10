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
    def update(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_size[0] - self.size[0] - 5:
            self.rect.x += self.speed

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


    display.update()
    clock.tick(FPS)