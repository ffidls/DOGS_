def locations(count):
    return f'FIRST_PART/DATAS/DATAS_LOCATIONS/location{count}/location{count}.png'


def get_count_location():
    datas = open('FIRST_PART/DATAS/DATAS_LOCATIONS/count_now_location', 'r').read()
    return int(datas)


def get_side_user():
    datas = open('FIRST_PART/DATAS/DATA_ANNA/side_move', 'r').read()
    return datas


def get_img_anna(count_sprite, type_move):
    return f"FIRST_PART/DATAS/DATA_ANNA/{type_move[:len(type_move) - 1]}_anna/{count_sprite}.png"


def window_dialog():
    return 'FIRST_PART/DATAS/DATAS_CONTACT/dialog_window.png'


def img_button():
    return 'FIRST_PART/DATAS/DATAS_CONTACT/button.png'


def img_human(name):
    name_fail = "Anna" if name == 'A' else 'Kira'
    return f'FIRST_PART/DATAS/DATAS_CONTACT/{name_fail}.png'


def inf_for_button():
    file = open('FIRST_PART/DATAS/INF_BUTTONS', 'r').read().split()
    str_inf = False if file[0] == 'False' else True
    return str_inf, (int(file[1]), int(file[2])), file[3]


def get_dialog_phrase(name_dialog, count_phrase):
    file = open(f'FIRST_PART/DATAS/TEXT_DIALOGS/{name_dialog}', 'r').read().split('@')
    all_phrase = file[0]
    a = file[int(count_phrase)]
    phrase, human = a[0], a[1:]
    return all_phrase, phrase, human


def get_condition_dog():
    file = open(f'FIRST_PART/DATAS/DATAS_DOGS/INF_CONDITION', 'r').read().split('@')
    return file[0], file[1]


def get_data_dialog():
    file = open('FIRST_PART/DATAS/INF_DIALOG', 'r').read().split()
    return file[0], file[1]


def get_count_sprite_anna():
    datas = open('FIRST_PART/DATAS/DATA_ANNA/count_sprite', 'r').read()
    return int(datas)


def get_condition_anna():
    datas = open('FIRST_PART/DATAS/DATA_ANNA/condition_anna', 'r').read()
    return datas


class DATAS:
    def __init__(self):
        pass