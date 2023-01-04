def give_pos_anna():
    file = open('FIRST_PART/DATAS/POS_ANNA', 'r').read().split()
    return int(file[0]), int(file[1])


def new_pos_anna(new_pos):
    file = open('FIRST_PART/DATAS/POS_ANNA', 'w')
    print(f'{new_pos[0]} {new_pos[1]}', file=file)

    file.close()


def give_pos_miki():
    file = open('FIRST_PART/DATAS/DATAS_DOGS/POS_MIKI', 'r').read().split()
    return int(file[0]), int(file[1])


def give_pos_zona():
    file = open('FIRST_PART/DATAS/DATAS_DOGS/POS_ZONA', 'r').read().split()
    return int(file[0]), int(file[1])


def new_pos_miki(new_pos):
    file = open('FIRST_PART/DATAS/DATAS_DOGS/POS_MIKI', 'w')
    print(f'{new_pos[0]} {new_pos[1]}', file=file)

    file.close()


def new_pos_zona(new_pos):
    file = open('FIRST_PART/DATAS/DATAS_DOGS/POS_ZONA', 'w')
    print(f'{new_pos[0]} {new_pos[1]}', file=file)

    file.close()


def new_pos_kira(pos):
    file = open('FIRST_PART/DATAS/DATA_KIRA/pos_kira')
    print(f'{pos[0]} {pos[1]}', file=file)
    file.close()


def get_pos_kira():
    file = open('FIRST_PART/DATAS/DATA_KIRA/pos_kira', 'r').read().split()
    return int(file[0]), int(file[1])
