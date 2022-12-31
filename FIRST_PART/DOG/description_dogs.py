import FIRST_PART.DATAS.possions
import pygame
import FIRST_PART.DATAS.get_datas


class DOG:
    def __init__(self):
        self.all_data = FIRST_PART.DATAS.possions
        self.data = FIRST_PART.DATAS.get_datas

    def pos_miki(self):
        return self.all_data.give_pos_miki()

    def entity(self, possible=False, possible_pos=None):
        pos = self.pos_miki() if not possible else possible_pos
        return pygame.Rect(pos[0], pos[1], 20, 20)

    def check_location(self):
        location_user, location_dog = self.data.get_count_location(), self.data.get_dog_location()
        return True if location_dog == location_user else False
