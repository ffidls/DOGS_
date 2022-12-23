import pygame

import FIRST_PART.DATAS.possions
import FIRST_PART.MECHANICA.moving, FIRST_PART.MECHANICA.Change_locations
import FIRST_PART.DATAS.const
import FIRST_PART.DATAS.get_datas
import FIRST_PART.DATAS.write_new_datas
import FIRST_PART.MECHANICA.control_all_condition


class Anna:
    def __init__(self):
        self.speed = 8
        self.datas_for_pos = FIRST_PART.DATAS.possions
        self.get_new_pos = FIRST_PART.MECHANICA.moving.MOVING()
        self.check_for_another_location = FIRST_PART.MECHANICA.Change_locations.LOCATIONS()

    def setting_movement(self, signal):
        old_pos = self.pos_anna()
        possible_pos = self.get_new_pos.new_possions_user(signal, old_pos)
        check_location = self.new_pos_for_new_location(old_pos)

        if check_location is not None:
            pos = check_location
        elif possible_pos is not None:
            pos = possible_pos
        else:
            pos = old_pos

        self.datas_for_pos.new_pos_anna(pos)

    def pos_anna(self):
        return self.datas_for_pos.give_pos_anna()

    def entity_anna(self, possible=False, possible_pos=None):
        pos = self.pos_anna() if not possible else possible_pos
        return pos[1], pos[0], 40, 40

    def new_pos_for_new_location(self, old_pos):
        return self.check_for_another_location.check_border(old_pos)


class setting_entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.data = FIRST_PART.DATAS.get_datas
        self.new_data = FIRST_PART.DATAS.write_new_datas
        pos, sprite = self.get_pos(), self.get_image()

        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(center=(pos[1], pos[0]))

    def get_image(self):
        last_count_sprite = self.data.get_count_sprite_anna()
        type_condition = FIRST_PART.MECHANICA.control_all_condition.get_condition()

        limit_sprite = 17 if type_condition == 'move\n' else 23
        count_sprite = last_count_sprite + 1 if last_count_sprite <= limit_sprite else 1

        self.new_data.new_count_sprite_anna(count_sprite)
        return self.data.get_img_anna(count_sprite, type_condition)

    def get_pos(self):
        return FIRST_PART.DATAS.possions.give_pos_anna()

