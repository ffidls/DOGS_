import pygame
import PEOPLE.ANNA
import DATAS.const
import DOG.description_dogs
import DATAS.possions
import DOG.move_dog
import DATAS.possions
import DOG.independent_move


def checking_contact(entity_object, entity_dog):
    return pygame.Rect.colliderect(entity_dog, entity_object)


def get_pos_zona(side):  # !!!
    data_anna = PEOPLE.ANNA.Anna()
    size_zon, pos_user = DATAS.const.SIZE_ZONE, data_anna.pos_anna()
    y, x = pos_user[0], pos_user[1]
    if side == 'left':
        start_pos_zona = (y - size_zon // 2 + 17, x - size_zon + 40)
    elif side == 'right':
        start_pos_zona = (y - size_zon // 2 + 17, x + size_zon // 2 - 75)
    elif side == 'up':
        start_pos_zona = (y - size_zon + 40, x - size_zon // 2 + 17)
    else:
        start_pos_zona = (y - size_zon // 2 + 75, x - size_zon // 2 + 17)

    DATAS.possions.new_pos_zona(start_pos_zona)
    return start_pos_zona


class MOVE:
    def __init__(self, signal):
        self.side = signal
        self.data_user = PEOPLE.ANNA.Anna()
        self.all_const = DATAS.const
        self.miki = DOG.description_dogs.DOG()
        self.recording_new_pos = DATAS.possions

        self.sorting_move()

    def sorting_move(self):
        entity_zona, pos_zona = self.create_entity_zona()
        entity_dog = self.miki.entity()
        if not checking_contact(entity_zona, entity_dog):
            type_move = 'zona'
            need_pos = pos_zona

            move_dog = DOG.move_dog.MECHANIC_MOVE(type_move, need_pos)
            self.write_new_data(move_dog.get_result_pos())

        # DATAS.possions.new_pos_zona(get_pos_zona(self.side))
        # self.get_pos_places(self.data_user.entity_anna())

    def write_new_data(self, pos):
        self.recording_new_pos.new_pos_miki(pos)
        DOG.independent_move.work_with_condition(type_work='new_condition', new_condition='choice_place')

    def create_entity_zona(self):
        size_zona = self.all_const.SIZE_ZONE
        start_pos_zona = get_pos_zona(self.side)
        return pygame.Rect(start_pos_zona[0], start_pos_zona[1], size_zona, size_zona), start_pos_zona

