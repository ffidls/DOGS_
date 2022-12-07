import pygame
import PEOPLE.ANNA
import DATAS.const
import DOG.description_dogs
import DATAS.possions
import MECHANICA.Change_locations


def checking_contact(entity_object, entity_dog):
    return pygame.Rect.colliderect(entity_dog, entity_object)


def get_pos_zona(side):  # !!!
    data_anna = PEOPLE.ANNA.Anna()
    size_zon, pos_user = DATAS.const.SIZE_ZONE, data_anna.pos_anna()
    y, x = pos_user[0], pos_user[1]
    if side == 'left':
        start_pos_zona = (y - size_zon // 2 - 5, x - size_zon - 10)
    elif side == 'right':
        start_pos_zona = (y - size_zon // 2 - 5, x + size_zon // 2 - 50)
    elif side == 'up':
        start_pos_zona = (y - size_zon - 10, x - size_zon // 2 - 5)
    else:
        start_pos_zona = (y - size_zon // 2 + 50, x - size_zon // 2 - 5)
    return start_pos_zona


def find_contact_place(pos_place, entity_dog, radius):
    find_pos = None
    for place in pos_place:
        y_place, x_place = place[1] - radius, place[0] - radius
        entity_place = pygame.Rect(y_place, x_place, radius, radius)
        entity_dog = pygame.Rect(entity_dog)
        if checking_contact(entity_place, entity_dog):
            find_pos = place
    return find_pos


class II:
    def __init__(self, signal):
        self.side = signal
        self.data_user = PEOPLE.ANNA.Anna()
        self.all_const = DATAS.const
        self.miki = DOG.description_dogs.DOG()

        self.get_signal()

    def get_signal(self):
        DATAS.possions.new_pos_zona(get_pos_zona(self.side))
        # self.get_pos_places(self.data_user.entity_anna())

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

    def get_pos_places(self, entity_dog):
        general_pos, private_pos = MECHANICA.Change_locations.get_special_place()
        radius = self.all_const.RADIUS_PLACE

        find_pos = find_contact_place(general_pos, entity_dog, radius)
        if find_pos is None and private_pos is not None:
            find_pos = find_contact_place(private_pos, entity_dog, radius)
        print(find_pos)
