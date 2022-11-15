import pygame
import PEOPLE.ANNA


class MOVING_PEOPLE:  # сложность в анимации
    def __init__(self):
        self.datas_Anna = PEOPLE.ANNA.Anna()

    def anna(self, screen):  # creating animation
        entity_anna = self.datas_Anna.entity_anna()
        pygame.draw.rect(screen, (24, 25, 255), entity_anna)

    def kira(self):
        pass
