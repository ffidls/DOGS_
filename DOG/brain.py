import pygame
import PEOPLE.ANNA
import DATAS.const
import DOG.description_dogs
import DATAS.possions


def checking_contact(entity_zona, entity_dog):
    return pygame.Rect.colliderect(entity_dog, entity_zona)


def get_pos_zona(side):
    data_anna = PEOPLE.ANNA.Anna()
    size_zon, pos_user = DATAS.const.SIZE_ZONE, data_anna.pos_anna()
    y, x = pos_user[0], pos_user[1]
    if side == 'left':
        start_pos_zona = (y - size_zon // 2, x - size_zon)
    elif side == 'right':
        #start_pos_zona = (y - size_zon // 2, x - size_zon)
        start_pos_zona = (y - size_zon // 2, x + size_zon )
    elif side == 'up':
        start_pos_zona = (y - 100, x - size_zon // 2)
    else:
        start_pos_zona = (y + size_zon, x - size_zon // 2)
    return start_pos_zona


class II:
    def __init__(self, signal):
        self.side = signal
        self.data_user = PEOPLE.ANNA.Anna()
        self.all_const = DATAS.const
        self.miki = DOG.description_dogs.DOG()

        self.get_signal()

    def get_signal(self):
        DATAS.possions.new_pos_miki(get_pos_zona(self.side))

    def find_special_place(self): pass

    def change_zona(self): pass

    def sort_move_dogs(self):
        # добавить режимы
        entity_dog, entity_zona = self.miki.entity(), self.create_entity_zona()
        if checking_contact(entity_zona, entity_dog):
            pass

    def create_entity_zona(self):
        size_zona = self.all_const.SIZE_ZONE
        start_pos_zona = get_pos_zona(self.side)
        return pygame.Rect(start_pos_zona[0], start_pos_zona[1], size_zona, size_zona)
