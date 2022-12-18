import FIRST_PART.DATAS.possions
import pygame


class DOG:
    def __init__(self):
        self.all_data = FIRST_PART.DATAS.possions

    def pos_miki(self):
        return self.all_data.give_pos_miki()

    def entity(self, possible=False, possible_pos=None):
        pos = self.pos_miki() if not possible else possible_pos
        return pygame.Rect(pos[0], pos[1], 20, 20)
