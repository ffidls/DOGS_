import DATAS.DATAS_LOCATIONS.location1.description_location_1
import DATAS.DATAS_LOCATIONS.location2.description_location_2
import DATAS.get_datas, DATAS.write_new_datas


def get_count_location():
    return DATAS.get_datas.get_count_location()


class LOCATIONS:
    def __init__(self):
        self.all_datas = None
        self.now_location = 1

        self.datas_location_1 = DATAS.DATAS_LOCATIONS.location1.description_location_1.LOCATION_1()
        self.datas_location_2 = DATAS.DATAS_LOCATIONS.location2.description_location_2.LOCATION_2()

    def check_border(self, pos_user):
        num_location, new_pos = get_count_location(), None
        if num_location == 1:
            new_num_location, new_pos = self.datas_location_1.checking_border(pos_user)
        elif num_location == 2:
            new_num_location, new_pos = self.datas_location_2.checking_borders(pos_user)
        else:
            new_num_location = None

        if new_num_location is not None:
            DATAS.write_new_datas.new_num_location(new_num_location)
            return new_pos

        return None

    def inf_location(self, type_inf):
        num = get_count_location()
        return self.entity_location(num) if type_inf == 'entity' else self.houses_location(num)

    def entity_location(self, num_location):
        if num_location == 1:
            return self.datas_location_1.entity()
        elif num_location == 2:
            return self.datas_location_2.entity()
        # else for 3 location

    def houses_location(self, num):
        inf_location1 = DATAS.DATAS_LOCATIONS.location1.description_location_1.get_all_inf_location()
        inf_location2 = DATAS.DATAS_LOCATIONS.location2.description_location_2.get_all_inf_location()
        if num == 1:
            return inf_location1[0], inf_location1[1]
        elif num == 2:
            return inf_location2[0], inf_location2[1]
        # else location 3
