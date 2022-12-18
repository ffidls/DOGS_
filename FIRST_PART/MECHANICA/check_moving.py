import pygame
import FIRST_PART.MECHANICA.Change_locations
import FIRST_PART.DATAS.const
import FIRST_PART.PEOPLE.ANNA
import FIRST_PART.DOG.description_dogs


def checking_contact_with_houses(entity_houses, entity_user):
    for house in entity_houses[0]:
        if pygame.Rect.colliderect(house, entity_user):
            return False
    return True


class CHECKING:
    def __init__(self, pos_user, type_checking):
        self.borders, self.wall = FIRST_PART.DATAS.const.BORDERS, FIRST_PART.DATAS.const.WALL
        self.height, self.width = FIRST_PART.DATAS.const.HEIGHT, FIRST_PART.DATAS.const.WIDTH
        self.x, self.y = pos_user[0], pos_user[1]
        self.action_locations = FIRST_PART.MECHANICA.Change_locations.LOCATIONS()
        self.type_object = type_checking

        self.data_anna = FIRST_PART.PEOPLE.ANNA.Anna()
        self.data_dog = FIRST_PART.DOG.description_dogs.DOG()
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
