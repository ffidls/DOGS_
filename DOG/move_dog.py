import DOG.description_dogs
import DATAS.const


class MOVE:
    def __init__(self, type_move, need_pos):
        self.miki = DOG.description_dogs.DOG()
        pos_dog = self.miki.pos_miki()

        self.y_dog, self.x_dog = pos_dog[0], pos_dog[1]
        self.y_need, self.x_need = need_pos[0], need_pos[1]

        missing_pos = self.missing_pos_zona() if type_move == 'zona' else self.missing_pos_place()
        self.missing_pos = missing_pos

    def missing_pos_zona(self):
        size_zona = DATAS.const.SIZE_ZONE

        missing_x = self.x_dog - self.x_need if self.x_dog < self.x_need \
            else missing_x = self.x_dog - (self.x_need + size_zona)
        missing_y = self.y_dog - self.y_need if self.y_dog < self.y_need \
            else missing_y = self. y_dog - (self.y_need + size_zona)

        return missing_y, missing_x

    def missing_pos_place(self):
        missing_x = self.x_dog - self.x_need if self.x_dog >= self.x_need else self.x_need - self.x_dog
        missing_y = self.y_dog - self.y_need if self.y_dog >= self.y_need else self.y_need - self.y_dog
        return missing_y, missing_x

    def get_missing_pos(self):
        return self.missing_pos
