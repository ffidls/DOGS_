def locations(count=None):
    return 'DATAS/location/location1.png'


def window_dialog():
    return 'DATAS/DATAS_CONTACT/dialog_window.png'


def img_button():
    return 'DATAS/DATAS_CONTACT/button.png'


def inf_for_button():
    file = open('DATAS/INF_BUTTONS', 'r').read().split()
    str_inf = False if file[0] == 'False' else True
    return str_inf, (int(file[1]), int(file[2])), file[3]


def get_dialog_phrase(name_dialog, count_phrase):
    file = open(f'DATAS/TEXT_DIALOGS/{name_dialog}', 'r').read().split('@')
    all_phrase = file[0]
    a = file[int(count_phrase)]
    phrase, human = a[0], a[1:]
    return all_phrase, phrase, human


def get_data_dialog():
    file = open('DATAS/INF_DIALOG', 'r').read().split()
    return file[0], file[1]


class DATAS:
    def __init__(self):
        pass
