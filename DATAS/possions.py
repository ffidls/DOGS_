def give_pos_anna():
    file = open('DATAS/POS_ANNA', 'r').read().split()
    return int(file[0]), int(file[1])


def new_pos_anna(new_pos):
    file = open('DATAS/POS_ANNA', 'w')
    print(f'{new_pos[0]} {new_pos[1]}', file=file)

    file.close()


def give_pos_miki():
    file = open('DATAS/DATAS_DOGS/POS_MIKI', 'r').read().split()
    return int(file[0]), int(file[1])


def give_pos_zona():
    file = open('DATAS/DATAS_DOGS/POS_ZONA', 'r').read().split()
    return int(file[0]), int(file[1])


def new_pos_miki(new_pos):
    file = open('DATAS/DATAS_DOGS/POS_MIKI', 'w')
    print(f'{new_pos[0]} {new_pos[1]}', file=file)

    file.close()


def new_pos_zona(new_pos):
    file = open('DATAS/DATAS_DOGS/POS_ZONA', 'w')
    print(f'{new_pos[0]} {new_pos[1]}', file=file)

    file.close()
