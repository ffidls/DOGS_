import DOG.description_dogs
import DATAS.const


def sorter_emotion(type_emotion, pos):
    if type_emotion == '0':
        return pos
    elif type_emotion == '+':
        return pos + 4
    return pos - 4


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
        if self.x_dog == self.x_need and self.y_dog == self.y_need:
            return None

        missing_x = self.x_dog - self.x_need if self.x_dog >= self.x_need else self.x_need - self.x_dog
        missing_y = self.y_dog - self.y_need if self.y_dog >= self.y_need else self.y_need - self.y_dog
        return self.final_choice((missing_y, missing_x))

    def move_emotion(self):
        new_y = sorter_emotion(self.y_dog, self.y_need)
        new_x = sorter_emotion(self.x_dog, self.x_need)
        return new_y, new_x

    def final_choice(self, missing_pos):
        if missing_pos == (0, 0):
            return None

        if abs(missing_pos[0]) >= abs(missing_pos[1]):
            result = (self.y_dog - self.speed, self.x_dog) if missing_pos[0] >= 0 \
                else (self.y_dog + self.speed, self.x_dog)
        else:
            result = (self.y_dog, self.x_dog - self.speed) if missing_pos[1] >= 0 \
                else (self.y_dog, self.x_dog + self.speed)
        return result

    def get_result_pos(self):
        return self.result
