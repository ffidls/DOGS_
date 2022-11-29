import pygame
import DATAS.const


def start_pos_door():
    return None


def pos_people_house():
    return None


def get_all_inf():
    return start_pos_door(), pos_people_house()


class LOCATION:
    def __init__(self):
        self.width, self.height = DATAS.const.WIDTH_LOCATION_2, DATAS.const.HEIGHT_LOCATION_2
        self.pos_border_next = DATAS.const.BORDER_NEXT
        self.pos_border_ago = DATAS.const.BORDER_AGO

        self.entity_location = pygame.Rect((0, 0, self.width, self.height))

    def entity(self):
        return [self.entity_location]

    def checking_border(self, entity_Anna):
        entity_border_next = pygame.Rect((self.pos_border_next[0], self.pos_border_next[1],
                                          DATAS.const.BORDER_HEIGHT, DATAS.const.BORDER_WIDTH))
        entity_border_ago = pygame.Rect((self.pos_border_ago[0], self.pos_border_ago[1],
                                          DATAS.const.BORDER_HEIGHT, DATAS.const.BORDER_WIDTH))
        entity_user = pygame.Rect(entity_Anna)

        if pygame.Rect.colliderect(entity_border_next, entity_user):
            next_num_location, new_pos_user = 2, DATAS.const.NEW_POC_NEXT_LOCATION
            return next_num_location, new_pos_user
        elif pygame.Rect.colliderect(entity_border_ago, entity_user):
            next_num_location, new_pos_user = 1, DATAS.const.NEW_POC_AGO_LOCATION
            return next_num_location, new_pos_user

        return None, None
