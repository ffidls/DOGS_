import pygame
import MECHANICA.Change_locations
import DATAS.const
import PEOPLE.ANNA


def checking_contact_with_houses(entity_houses, entity_user):
    for house in entity_houses:
        if pygame.Rect.colliderect(house, entity_user):
            return False
    return True


class CHECKING:
    def __init__(self, pos_user):
        self.borders, self.wall = DATAS.const.BORDERS, DATAS.const.WALL
        self.height, self.width = DATAS.const.HEIGHT, DATAS.const.WIDTH
        self.x, self.y = pos_user[0], pos_user[1]
        self.action_locations = MECHANICA.Change_locations.LOCATIONS()

        self.data_anna = PEOPLE.ANNA.Anna()
        # change all_location

    def result(self):
        return self.border() and self.houses()

    def border(self):
        return self.height - self.x > self.borders and self.width - self.y > self.borders and self.y >= self.wall

    def houses(self):  # for locations
        houses, anna = self.action_locations.inf_location(type_inf='entity'), \
                       self.data_anna.entity_anna(True, (self.x, self.y))

        return checking_contact_with_houses(houses, anna)
