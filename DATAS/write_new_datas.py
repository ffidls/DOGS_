def new_inf_for_button(pos):
    file = open('DATAS/INF_BUTTONS', 'w')
    str_inf = f'True {pos[0]} {pos[1]}' if pos is not None else 'False -1 -1'
    print(str_inf, file=file)

    file.close()

