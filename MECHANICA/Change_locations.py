import DATAS.DATAS_LOCATIONS.location1.description_location_1
import DATAS.DATAS_LOCATIONS.location2.description_location_2
import DATAS.get_datas, DATAS.write_new_datas
import PEOPLE.ANNA


def get_count_location():
    return DATAS.get_datas.get_count_location()


class LOCATIONS:
    def __init__(self):
        self.all_datas = None
        self.now_location = 1

        self.datas_location_1 = DATAS.DATAS_LOCATIONS.location1.description_location_1
        self.datas_location_2 = DATAS.DATAS_LOCATIONS.location2.description_location_2

        self.Anna = PEOPLE.ANNA.Anna()

    def check_border(self, pos_user):
        num_location = get_count_location()
        pos_border = self.ger_border_now_location(num_location)

        if pos_border[0] <= pos_user[1] and pos_border[1] <= pos_user[0]:
            DATAS.write_new_datas.new_num_location(num_location + 1)
            self.Anna.new_pos_for_new_location()

    def ger_border_now_location(self, num_location):
        return self.datas_location_1.pos_border_location_2() if num_location == 1 else None

    def inf_location(self):
        num = get_count_location()
        return self.datas_location_1.start_pos_door(), self.datas_location_1.pos_people_house() if num == 1 else None

    def entity_location(self):
        num = get_count_location()
        loc1, loc2 = self.datas_location_1.LOCATION_1(), self.datas_location_2.LOCATION_2()
        return loc1.entity_location if num == 1 else loc2.entity_location
