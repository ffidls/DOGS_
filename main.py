import pygame, sys, time
from pygame.locals import *
import DATAS.location

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
width = 500
height = 500
mainSurface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Keyb moves')
background = pygame.image.load('DATAS/location/location1.png')
sprite = pygame.image.load('DATAS/location/location1.png')
# Place image to the center of mainSurface
image_pos = ((mainSurface.get_width() - sprite.get_width()) / 2, (mainSurface.get_height() - sprite.get_height()) / 2)
doMove = False
# game loop
while True:
    fpsClock.tick(FPS)  # frame rate
    mainSurface.blit(background, (0, 0))

    # get all events from the queue
    for event in pygame.event.get():
        # loop events queue
        if event.type == QUIT:
            # window close X pressed
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            # ESC key pressed
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    mainSurface.blit(sprite, image_pos)
    pygame.display.update()
