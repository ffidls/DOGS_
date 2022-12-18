import pygame
import random
import FIRST_PART.DATAS.write_new_datas, FIRST_PART.DATAS.get_datas
import FIRST_PART.MECHANICA.Change_locations
import FIRST_PART.DOG.move_dog
import FIRST_PART.DATAS.possions
import FIRST_PART.DATAS.const


def work_with_condition(type_work, new_condition=None, new_datas=None):
    if type_work == 'get_condition':
        return FIRST_PART.DATAS.get_datas.get_condition_dog()
    else:
        FIRST_PART.DATAS.write_new_datas.new_condition(new_condition, new_datas)

 
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
        self.recording_new_pos = FIRST_PART.DATAS.possions
        self.all_const = FIRST_PART.DATAS.const

        self.sorting_condition()

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
            all_place = FIRST_PART.MECHANICA.Change_locations.get_special_place()
            next_place_dog = choice_place(all_place)
            work_with_condition(type_work='new_condition', new_condition='search_place', new_datas=next_place_dog)

        elif now_condition == 'search_place':
            find_place_pos = all_data_condition[1].split()
            mechanic_move = FIRST_PART.DOG.move_dog.MECHANIC_MOVE(type_move='place',
                                                       need_pos=(int(find_place_pos[1]), int(find_place_pos[0])))
            new_pos = mechanic_move.result

            if new_pos is not None:
                self.write_new_data(mechanic_move.result)
            else:
                work_with_condition(type_work='new_condition', new_condition='emotions_from place', new_datas=0)

        else:  # add random emotions
            num_move = all_data_condition[1]
            result_pos = self.work_emotion(int(num_move))
            if result_pos is not None:
                work_with_condition(type_work='new_condition', new_condition='emotions_from place',
                                    new_datas=int(num_move) + 1)
                self.write_new_data(result_pos)
            else:
                work_with_condition(type_work='new_condition', new_condition='choice_place', new_datas=None)

    def write_new_data(self, new_pos):
        self.recording_new_pos.new_pos_miki(new_pos)

    def work_emotion(self, num_move):
        emotion_move = self.all_const.DSK_EMOTIONS[1]
        if num_move > len(emotion_move) - 1:
            return None
        mechanic_move = FIRST_PART.DOG.move_dog.MECHANIC_MOVE(type_move='emotion', need_pos=emotion_move[num_move])
        return mechanic_move.get_result_pos()
