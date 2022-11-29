import DATAS.possions
import MECHANICA.moving, MECHANICA.Change_locations
import DATAS.const


class Anna:
    def __init__(self):
        self.speed = 8
        self.datas_for_pos = DATAS.possions
        self.get_new_pos = MECHANICA.moving.MOVING()
        self.check_for_another_location = MECHANICA.Change_locations.LOCATIONS()

    def setting_movement(self, signal):
        old_pos = self.pos_anna()
        possible_pos = self.get_new_pos.new_possions_user(signal, old_pos)
        check_location = self.new_pos_for_new_location()

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

    def new_pos_for_new_location(self):
        entity_user = self.entity_anna()
        return self.check_for_another_location.check_border(entity_user)

