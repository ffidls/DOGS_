import DOG.description_dogs
import DATAS.const


class MECHANIC_MOVE:
    def __init__(self, type_move, need_pos):
        self.miki = DOG.description_dogs.DOG()
        pos_dog = self.miki.pos_miki()
        self.speed = DATAS.const.SPEED_DOG

        self.y_dog, self.x_dog = pos_dog[0], pos_dog[1]
        self.y_need, self.x_need = need_pos[0], need_pos[1]

        missing_pos = self.missing_pos_zona() if type_move == 'zona' else self.missing_pos_place()
        self.missing_pos = missing_pos

        self.result = self.final_choice()

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

        return missing_y, missing_x

    def missing_pos_place(self):
        if self.x_dog == self.x_need and self.y_dog == self.y_need:
            return 0, 0

        missing_x = self.x_dog - self.x_need if self.x_dog >= self.x_need else self.x_need - self.x_dog
        missing_y = self.y_dog - self.y_need if self.y_dog >= self.y_need else self.y_need - self.y_dog
        return missing_y, missing_x

    def final_choice(self):
        if self.missing_pos == (0, 0):
            return None

        if abs(self.missing_pos[0]) >= abs(self.missing_pos[1]):
            result = (self.y_dog - self.speed, self.x_dog) if self.missing_pos[0] >= 0 \
                else (self.y_dog + self.speed, self.x_dog)
        else:
            result = (self.y_dog, self.x_dog - self.speed) if self.missing_pos[1] >= 0 \
                else (self.y_dog, self.x_dog + self.speed)
        return result

    def get_result_pos(self):
        return self.result
