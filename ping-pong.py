from pygame import *
from time import sleep, time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 490:
            self.rect.y += self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("Лабиринт")
background = transform.scale(image.load("galaxy.jpg"),(win_width,win_height))
Finish = False
game = True
hero = Player("images.jpg", 10,250,50,50,6)
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if Finish != True:
        window.blit(background,(0,0))
        hero.update()
        hero.reset()
        display.update()
    clock.tick(FPS)