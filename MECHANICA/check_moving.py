import pygame
import DATAS.location.description_location_1
import DATAS.const
import PEOPLE.ANNA


class CHECKING:
    def __init__(self, pos_user):
        self.borders, self.wall = DATAS.const.BORDERS, DATAS.const.WALL
        self.height, self.width = DATAS.const.HEIGHT, DATAS.const.WIDTH
        self.x, self.y = pos_user[0], pos_user[1]

        self.data_location, self.data_anna = DATAS.location.description_location_1.LOCATION_1(), PEOPLE.ANNA.Anna()

    def result(self):
        return self.border() and self.houses()

    def border(self):
        return self.height - self.x > self.borders and self.width - self.y > self.borders and self.y >= self.wall

    def houses(self):  # for locations
        location, anna = self.data_location.entity(), self.data_anna.entity_anna(True, (self.x, self.y))
        return not pygame.Rect.colliderect(location, anna)

    def buttons(self):
        pass
