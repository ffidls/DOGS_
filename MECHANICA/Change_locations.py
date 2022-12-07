import DATAS.DATAS_LOCATIONS.location1.description_location
import DATAS.DATAS_LOCATIONS.location2.description_location
import DATAS.DATAS_LOCATIONS.location3.description_location
import DATAS.get_datas, DATAS.write_new_datas
import DATAS.const


def get_count_location():
    return DATAS.get_datas.get_count_location()


def get_datas_location(type_depth):
    num = get_count_location()
    if num == 1:
        user_location = DATAS.DATAS_LOCATIONS.location1.description_location
    elif num == 2:
        user_location = DATAS.DATAS_LOCATIONS.location2.description_location
    else:
        user_location = DATAS.DATAS_LOCATIONS.location3.description_location
    # else user_location = location3

    if type_depth == 'class':
        return user_location.LOCATION()
    elif type_depth == 'fail':
        return user_location


def get_special_place():
    general_pos = DATAS.const.GENERAL_PLACE
    private_place = get_datas_location('fail').private_place()
    return general_pos, private_place


class LOCATIONS:
    def __init__(self):
        self.all_datas = None
        self.now_location = 1
        self.all_const = DATAS.const

    def check_border(self, pos_user):
        user_location = get_datas_location(type_depth='class')
        num_location, new_pos = user_location.checking_border(pos_user)

        if num_location is not None:
            DATAS.write_new_datas.new_num_location(num_location)
            return new_pos

        return None

    def inf_location(self, type_inf):
        return self.entity_location() if type_inf == 'entity' else self.houses_location()

    def entity_location(self):
        user_location = get_datas_location(type_depth='class')
        return user_location.entity()

    def houses_location(self):
        user_location = get_datas_location(type_depth='fail')
        all_inf = user_location.get_all_inf()
        return all_inf[0], all_inf[1]
