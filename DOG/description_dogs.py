import DATAS.possions
import pygame


class DOG:
    def __init__(self):
        self.all_data = DATAS.possions

    def pos_miki(self):
        return self.all_data.give_pos_miki()

    def entity(self):
        pos = self.pos_miki()
        return pygame.Rect(pos[0], pos[1], 20, 20)
