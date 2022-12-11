import pygame
import random
import DATAS.write_new_datas, DATAS.get_datas
import MECHANICA.Change_locations
import DOG.move_dog
import DATAS.possions


def work_with_condition(type_work, new_condition=None, new_datas=None):
    if type_work == 'get_condition':
        return DATAS.get_datas.get_condition_dog()
    else:
        DATAS.write_new_datas.new_condition(new_condition, new_datas)

 
def checking_contact(entity_object, entity_dog):
    return pygame.Rect.colliderect(entity_dog, entity_object)


def find_contact_place(pos_place, entity_dog, radius):
    find_pos = None
    for place in pos_place:
        y_place, x_place = place[1] - radius, place[0] - radius
        entity_place = pygame.Rect(y_place, x_place, radius, radius)
        entity_dog = pygame.Rect(entity_dog)
        if checking_contact(entity_place, entity_dog):
            find_pos = place
    return find_pos


def choice_place(pos_place):
    random_area = len(pos_place) - 1
    ind_place = random.randint(0, random_area)
    return pos_place[ind_place]


class INDEPENDENCE_MOVE:
    def __init__(self):
        self.all_condition = ['choice_place', 'search_place', 'emotions_from place']
        self.recording_new_pos = DATAS.possions

    def get_pos_places(self, entity_dog):
        """general_pos, private_pos = MECHANICA.Change_locations.get_special_place()
        radius = self.all_const.RADIUS_PLACE

        find_pos = find_contact_place(general_pos, entity_dog, radius)
        if find_pos is None and private_pos is not None:
            find_pos = find_contact_place(private_pos, entity_dog, radius)

        return find_pos"""
        pass

    def sorting_condition(self):
        all_data_condition = work_with_condition('get_condition')
        now_condition = all_data_condition[0]

        if now_condition == 'choice_place':
            all_place = MECHANICA.Change_locations.get_special_place()
            next_place_dog = choice_place(all_place)
            work_with_condition(type_work='new_condition', new_condition='search_place', new_datas=next_place_dog)

        elif now_condition == 'search_place':
            find_place_pos = now_condition[1]
            mechanic_move = DOG.move_dog.MECHANIC_MOVE(type_move='place', need_pos=find_place_pos)
            new_pos = mechanic_move.result
            if new_pos is not None:
                self.write_new_data(mechanic_move.result)
            else:
                work_with_condition(type_work='new_condition', new_condition='emotions_from place', new_datas=0)

        else:
            pass

    def write_new_data(self, new_pos):
        self.recording_new_pos.new_pos_miki(new_pos)
