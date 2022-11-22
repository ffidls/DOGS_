import pygame, sys, time
from pygame.locals import *
import DATAS.DATAS_LOCATIONS.location2

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
width = 512
height = 512
mainSurface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Keyb moves')
# background = pygame.image.load('DATAS/location2/location2.png')
sprite = pygame.image.load('DATAS/DATAS_LOCATIONS/location1/location1.png')
# Place image to the center of mainSurface
image_pos = (0, 0)
doMove = False
# game loop
while True:
    fpsClock.tick(FPS)  # frame rate
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

    mainSurface.blit(sprite, (0, 0))
    pygame.display.update()
