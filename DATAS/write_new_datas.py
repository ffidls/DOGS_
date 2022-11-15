def new_inf_for_button(pos):
    file = open('DATAS/INF_BUTTONS', 'w')
    print(f'True {pos[0]} {pos[1]}', file=file)

    file.close()

