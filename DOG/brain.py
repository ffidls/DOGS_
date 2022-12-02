import pygame
import PEOPLE.ANNA
import DATAS.const
import DOG.description_dogs


def checking_contact(entity_zona, entity_dog):
    return pygame.Rect.colliderect(entity_dog, entity_zona)


class II:
    def __init__(self, signal):
        self.side = signal
        self.data_user = PEOPLE.ANNA.Anna()
        self.all_const = DATAS.const
        self.miki = DOG.description_dogs.DOG()

    def get_signal(self, side):
        pass

    def create_entity_zona(self):
        pos_user = self.data_user.pos_anna()
        size_zon = self.all_const.SIZE_ZONE
        y, x = pos_user[0], pos_user[1]
        if self.side == 'left':
            start_pos_zona = (y - size_zon // 2, x)
        elif self.side == 'right':
            start_pos_zona = (y - size_zon // 2, x - size_zon)
        elif self.side == 'up':
            start_pos_zona = (y - size_zon, x - size_zon // 2)
        else:
            start_pos_zona = (y, x - size_zon // 2)

        return pygame.Rect(start_pos_zona[0], start_pos_zona[1], size_zon, size_zon)
