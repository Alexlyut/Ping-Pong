from pygame import *
from time import sleep, time as timer

font.init()
font2 = font.Font(None, 36)

score1 = 0
score2 = 0

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
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("Лабиринт")
background = transform.scale(image.load("galaxy.jpg"),(win_width,win_height))
Finish = False
game = True
speed_x = 3
speed_y = 3
hero1 = Player("images.jpg", 20,250,50,100,7)
hero2 = Player("images.jpg", 630,250,50,100,7)
ball =GameSprite("Ball.png", 350,250,40,40,5)
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if Finish != True:
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        hero1.update1()
        hero1.reset()
        hero2.update2()
        hero2.reset()
        text1 = font2.render("Счёт: " + str(score1), 1, (255, 255, 255))
        window.blit(text1, (10,10))
        text2 = font2.render("Счёт: " + str(score2), 1, (255, 255, 255))
        window.blit(text2, (10,40))
        display.update()
    if ball.rect.y < 0 or ball.rect.y > win_height - 50:
        speed_y *= -1
    if sprite.collide_rect(hero1,ball) or sprite.collide_rect(hero2,ball):
        speed_x *= -1
    if ball.rect.x > 700:
        score1 += 1
        ball.kill()
        ball.reset()
    if ball.rect.x < 0:
        score2 += 1
        ball.kill()
        ball.reset()
    clock.tick(FPS)
