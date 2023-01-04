import pygame
import FIRST_PART.DATAS.get_datas, FIRST_PART.DATAS.write_new_datas
import FIRST_PART.DATAS.possions
import FIRST_PART.DATAS.const
import FIRST_PART.DOG.move_dog


def get_pos():
    return FIRST_PART.DATAS.possions.get_pos_kira()


def write_new_condition(condition):
    FIRST_PART.DATAS.write_new_datas.new_condition_kira(condition)


class CONTROL_MOVE:
    def __init__(self):
        self.new_data = FIRST_PART.DATAS.write_new_datas
        self.get_data = FIRST_PART.DATAS.get_datas
        self.all_const = FIRST_PART.DATAS.const

        self.condition = ['wait', 'talk', 'go']

    def sorter_dialog(self, name_dialog):
        now_condition = self.get_data.get_condition_kira()

        if now_condition == self.condition[0] and name_dialog == 'kira_house':
            write_new_condition(self.condition[1])
            FIRST_PART.DATAS.possions.new_pos_kira(self.all_const.POS_HOUSE_KIRA)

        if now_condition == self.condition[1] and name_dialog is None:
            write_new_condition(self.condition[2])

    def get_type_move(self):
        return self.get_data.get_condition_kira()


class KIRA:
    def __init__(self):
        self.setting_condition = CONTROL_MOVE()
        self.all_const = FIRST_PART.DATAS.const

    def setting_move(self):
        now_condition = self.setting_condition.get_type_move()
        pos = None
        if now_condition == 'talk':
            pos = self.all_const.POS_HOUSE_KIRA
        elif now_condition == 'go':
            make_new_pos = FIRST_PART.DOG.move_dog.MECHANIC_MOVE(
                type_move='place', need_pos=self.all_const.POS_HOUSE_ALINA, entity_object='people')
            pos = make_new_pos.get_result_pos()
        return pos


class setting_entity(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.data = FIRST_PART.DATAS.get_datas
        self.new_data = FIRST_PART.DATAS.write_new_datas
        sprite = self.get_image()

        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(center=(pos[1], pos[0]))

    def get_image(self):
        last_count_sprite = self.data.get_count_sprite(name_people='KIRA')
        type_condition = 'move\n'

        limit_sprite = 17 if type_condition == 'move\n' else 23
        count_sprite = last_count_sprite + 1 if last_count_sprite <= limit_sprite else 1

        self.new_data.new_count_sprite(count=count_sprite, name_people='KIRA')
        return self.data.get_img(count_sprite=count_sprite, type_move=type_condition, name_people='KIRA')
