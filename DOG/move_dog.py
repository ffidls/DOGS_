import DOG.description_dogs
import DATAS.const
import pygame
import MECHANICA.check_moving


def sorter_emotion(type_emotion, pos):
    if type_emotion == '0':
        return pos
    elif type_emotion == '+':
        return pos + 8
    return pos - 8


def checking_contact(entity_object, entity_dog):
    return pygame.Rect.colliderect(entity_dog, entity_object)


def check_new_pos(possible_pos):
    mechanica_check = MECHANICA.check_moving.CHECKING((possible_pos[1], possible_pos[0]), 'dog')
    return mechanica_check.result()


class MECHANIC_MOVE:
    def __init__(self, type_move, need_pos):
        self.miki = DOG.description_dogs.DOG()
        pos_dog = self.miki.pos_miki()
        self.speed = DATAS.const.SPEED_DOG

        self.y_dog, self.x_dog = pos_dog[0], pos_dog[1]
        self.y_need, self.x_need = need_pos[0], need_pos[1]

        if type_move == 'zona':
            self.result = self.missing_pos_zona()
        elif type_move == 'place':
            self.result = self.missing_pos_place()
        else:
            self.result = self.move_emotion()

    def missing_pos_zona(self):
        size_zona = DATAS.const.SIZE_ZONE

        if self.x_dog < self.x_need:
            missing_x = self.x_dog - self.x_need
        else:
            missing_x = self.x_dog - (self.x_need + size_zona)

        if self.y_dog < self.y_need:
            missing_y = self.y_dog - self.y_need
        else:
            missing_y = self.y_dog - (self.y_need + size_zona)

        return self.final_choice((missing_y, missing_x))

    def missing_pos_place(self):
        radius = DATAS.const.RADIUS_FIND_PLACE
        entity_place = pygame.Rect((self.y_need, self.x_need, radius, radius))
        entity_dog = self.miki.entity()
        speed = DATAS.const.SPEED_DOG

        if checking_contact(entity_place, entity_dog):
            return None

        missing_y = self.y_need - self.y_dog if self.y_need > self.y_dog else self.y_dog - self.y_need
        missing_x = self.x_need - self.x_dog if self.x_need > self.x_dog else self.x_dog - self.x_need

        first_var = self.y_dog, self.x_dog - speed if self.x_dog > self.x_need else self.x_dog + speed
        second_var = self.y_dog - speed if self.y_dog > self.y_need else self.y_dog + speed, self.x_dog

        if abs(missing_x) - abs(missing_y) == 3 or abs(missing_y) - abs(missing_x) == 3:
            pos = self.y_dog - speed if self.y_dog > self.y_need else self.y_dog + speed, \
                  self.x_dog - speed if self.x_dog > self.x_need else self.x_dog + speed

        elif abs(missing_x) > abs(missing_y):
            pos = first_var if check_new_pos(first_var) else second_var
        else:
            pos = second_var if check_new_pos(second_var) else first_var

        return pos

    def move_emotion(self):
        new_y = sorter_emotion(self.y_need, self.y_dog)
        new_x = sorter_emotion(self.x_need, self.x_dog)
        return new_y, new_x

    def final_choice(self, missing_pos):
        speed = DATAS.const.SPEED_DOG
        if abs(missing_pos[0]) >= abs(missing_pos[1]):
            result = (self.y_dog - speed, self.x_dog) if missing_pos[0] >= 0 \
                else (self.y_dog + speed, self.x_dog)
        else:
            result = (self.y_dog, self.x_dog - speed) if missing_pos[1] >= 0 \
                else (self.y_dog, self.x_dog + speed)
        return result

    def get_result_pos(self):
        return self.result
