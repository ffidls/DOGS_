import pygame
import DOG.description_dogs


class MOVING_DOG:  # сложность в анимации
    def __init__(self):
        self.datas_Miki = DOG.description_dogs.DOG()

    def miki(self, screen):  # creating animation
        entity_miki = self.datas_Miki.entity()
        pygame.draw.rect(screen, (24, 125, 55), entity_miki)

    def kira(self):
        pass
