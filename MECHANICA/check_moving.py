import pygame
import MECHANICA.Change_locations
import DATAS.const
import PEOPLE.ANNA
import DOG.description_dogs


def checking_contact_with_houses(entity_houses, entity_user):
    for house in entity_houses[0]:
        if pygame.Rect.colliderect(house, entity_user):
            return False
    return True


class CHECKING:
    def __init__(self, pos_user, type_checking):
        self.borders, self.wall = DATAS.const.BORDERS, DATAS.const.WALL
        self.height, self.width = DATAS.const.HEIGHT, DATAS.const.WIDTH
        self.x, self.y = pos_user[0], pos_user[1]
        self.action_locations = MECHANICA.Change_locations.LOCATIONS()
        self.type_object = type_checking

        self.data_anna = PEOPLE.ANNA.Anna()
        self.data_dog = DOG.description_dogs.DOG()
        # change all_location

    def result(self):
        return self.border() and self.houses()

    def border(self):
        return self.height - self.x > self.borders and self.width - self.y > self.borders and self.y >= self.wall

    def houses(self):  # for locations
        if self.type_object == 'people':
            object = self.data_anna.entity_anna(True, (self.x, self.y))
        else:
            object = self.data_dog.entity(True, (self.x, self.y))
        houses = self.action_locations.inf_location(type_inf='entity'),

        return checking_contact_with_houses(houses, object)
