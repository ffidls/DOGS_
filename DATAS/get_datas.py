def locations(count=None):
    return 'DATAS/location/location1.png'


def inf_for_button():
    file = open('DATAS/INF_BUTTONS', 'r').read().split()
    return bool(file[0]), (int(file[1]), int(file[2]))


class DATAS:
    def __init__(self):
        pass
