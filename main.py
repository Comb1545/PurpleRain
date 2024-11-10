# no Googling challenge
# pygame docs used
# random docs used
# rgb colour picker used

import random
import pygame
import pygame.locals
from pygame import mixer
from func import *

class rainDrop():
    depth = 10

    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(-HEIGHT, -HEIGHT * 3)
        self.z = logRandom(self.depth, 2)
        self.image = rainPNG

        self.length = scale(1, self.depth, self.z, 3, 20)
        self.thickness = scale(1, self.depth, self.z, 1, 3)
        self.fallSpeed = scale(1, self.depth, self.z, 3, 10)

    def draw(self):
        pygame.draw.line(display, RAINCOLOUR, (self.x, self.y), (self.x, self.y - self.length), self.thickness)

    def drawSprite(self):
        display.blit(self.image, (self.x, self.y))

    def fall(self):
        self.y += self.fallSpeed
        if self.y >= HEIGHT:
            self.y = random.uniform(-HEIGHT, -HEIGHT * 1.5)
            #rainDropAudio.play()

RAINCOLOUR = (20, 60, 110)
BACKGROUND = (0, 20, 50)
WIDTH = 1280
HEIGHT = 680
rainPNG = pygame.image.load("Raindrop.png")

mixer.init()
rainDropAudio = pygame.mixer.Sound("waterdrip.mp3")
rainAudio = pygame.mixer.Sound("RainSounds.mp3")

rainAudio.play(-1)

pygame.init
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))

drops = [rainDrop() for _ in range(1, 1000)]
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill(BACKGROUND)

    # game logic
    for drop in drops:
        drop.draw()
        drop.fall()

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()