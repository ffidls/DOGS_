import pygame
import FIRST_PART.PEOPLE.ANNA


class MOVING_PEOPLE:  # сложность в анимации
    def __init__(self):pass

    def anna(self, screen):  # creating animation
        entity_anna = FIRST_PART.PEOPLE.ANNA.setting_entity()
        screen.blit(entity_anna.image, entity_anna.rect)

    def kira(self):
        pass
