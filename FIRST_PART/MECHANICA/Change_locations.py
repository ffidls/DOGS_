import FIRST_PART.DATAS.DATAS_LOCATIONS.location1.description_location
import FIRST_PART.DATAS.DATAS_LOCATIONS.location2.description_location
import FIRST_PART.DATAS.DATAS_LOCATIONS.location3.description_location
import FIRST_PART.DATAS.DATAS_LOCATIONS.location4.description_location
import FIRST_PART.DATAS.get_datas, FIRST_PART.DATAS.write_new_datas
import FIRST_PART.DATAS.const


def get_count_location(entity):
    if entity == 'user':
        count = FIRST_PART.DATAS.get_datas.get_count_location()
    else:
        count = FIRST_PART.DATAS.get_datas.get_dog_location()
    return count


def get_datas_location(type_depth, object='user'):
    num = get_count_location('user') if object == 'user' else get_count_location('dog')
    if num == 1:
        user_location = FIRST_PART.DATAS.DATAS_LOCATIONS.location1.description_location
    elif num == 2:
        user_location = FIRST_PART.DATAS.DATAS_LOCATIONS.location2.description_location
    elif num == 3:
        user_location = FIRST_PART.DATAS.DATAS_LOCATIONS.location3.description_location
    else:
        user_location = FIRST_PART.DATAS.DATAS_LOCATIONS.location4.description_location
    # else user_location = location3

    if type_depth == 'class':
        return user_location.LOCATION()
    elif type_depth == 'fail':
        return user_location


def get_special_place():
    private_place = get_datas_location('fail').private_place()
    return private_place


class LOCATIONS:
    def __init__(self):
        self.all_datas = None
        self.now_location = 1
        self.all_const = FIRST_PART.DATAS.const

    def check_border(self, pos_user, entity_object='user'):
        user_location = get_datas_location(type_depth='class') if entity_object == 'user' \
            else get_datas_location(type_depth='class', object='dog')
        num_location, new_pos = user_location.checking_border(pos_user)

        if entity_object =='dog':
            pass

        if num_location is not None:
            FIRST_PART.DATAS.write_new_datas.new_num_location(num_location) if entity_object == 'user' \
                else FIRST_PART.DATAS.write_new_datas.new_count_location_dog(num_location)
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
