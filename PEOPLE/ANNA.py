import DATAS.possions
import MECHANICA.moving
import DATAS.const


class Anna:
    def __init__(self):
        self.speed = 8
        self.datas_for_pos = DATAS.possions
        self.get_new_pos = MECHANICA.moving.MOVING()

    def setting_movement(self, signal):
        old_pos = self.pos_anna()
        possible_pos = self.get_new_pos.new_possions_user(signal, old_pos)

        new_pos = possible_pos if possible_pos is not None else old_pos
        self.datas_for_pos.new_pos_anna(new_pos)

    def pos_anna(self):
        return self.datas_for_pos.give_pos_anna()

    def entity_anna(self, possible=False, possible_pos=None):
        pos = self.pos_anna() if not possible else possible_pos
        return pos[1], pos[0], 40, 40

    def new_pos_for_new_location(self):
        old_pos = self.pos_anna()
        new_pos = DATAS.const.NEW_Y_LOCATION_2, old_pos[0] * (-1)
        self.datas_for_pos.new_pos_anna(new_pos)
