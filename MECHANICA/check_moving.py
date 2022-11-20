import pygame
import MECHANICA.Change_locations
import DATAS.const
import PEOPLE.ANNA


class CHECKING:
    def __init__(self, pos_user):
        self.borders, self.wall = DATAS.const.BORDERS, DATAS.const.WALL
        self.height, self.width = DATAS.const.HEIGHT, DATAS.const.WIDTH
        self.x, self.y = pos_user[0], pos_user[1]
        self.action_locations = MECHANICA.Change_locations.LOCATIONS()

        self.data_location, self.data_anna = self.action_locations.entity_location(), PEOPLE.ANNA.Anna()
        # change all_location

    def result(self):
        self.border_another_location()
        return self.border() and self.houses()

    def border(self):
        return self.height - self.x > self.borders and self.width - self.y > self.borders and self.y >= self.wall

    def houses(self):  # for locations
        location, anna = self.data_location, self.data_anna.entity_anna(True, (self.x, self.y))
        return not pygame.Rect.colliderect(location, anna)

    def border_another_location(self):
        self.action_locations.check_border((self.x, self.y))
