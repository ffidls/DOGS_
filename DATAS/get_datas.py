def locations(count=None):
    return 'DATAS/location/location1.png'


def inf_for_button():
    file = open('DATAS/INF_BUTTONS', 'r').read().split()
    str_inf = False if file[0] == 'False' else True
    return str_inf, (int(file[1]), int(file[2]))


class DATAS:
    def __init__(self):
        pass
