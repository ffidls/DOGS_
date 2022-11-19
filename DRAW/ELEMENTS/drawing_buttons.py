import pygame
import DIALOG_BUTTONS.mechanic_contact
import DATAS.get_datas, DATAS.const


def mechanic_text(phrase, SCREEN, pos):
    my_font = pygame.font.SysFont('DATAS/DATAS_CONTACT/m3x6.ttf', 20)

    if DATAS.const.WINDOW_WIDTH >= (len(phrase) - 2) * DATAS.const.LEN_ONE_WORD:
        text_surface = my_font.render(phrase, False, (0, 0, 0))
        SCREEN.blit(text_surface, pos)
    else:
        index = (DATAS.const.WIDTH_WINDOW_TEXT//DATAS.const.LEN_ONE_WORD - len(phrase))
        new_phrase, phrase = f'{phrase[:index]} -', f'- {phrase[index:]}'
        text_surface = my_font.render(new_phrase, False, (0, 0, 0))
        SCREEN.blit(text_surface, pos)

        mechanic_text(phrase, SCREEN, (pos[0], pos[1] + DATAS.const.INDENT_TEXT))


class ASSEMBLING:
    def __init__(self):
        self.img_button = pygame.image.load(DATAS.get_datas.img_button())
        self.inf_button_dialog = DIALOG_BUTTONS.mechanic_contact.SETTING_CONTACT()

        self.window_dialog = pygame.image.load(DATAS.get_datas.window_dialog())

    def draw_button(self, SCREEN):
        pos = self.inf_button_dialog.setting_for_draw_button()
        SCREEN.blit(self.img_button, (pos[0], pos[1]))

    def draw_dialog(self, SCREEN):
        datas_dialog = self.inf_button_dialog.datas_from_draw_dialog()
        if datas_dialog is not None:
            human, phrase = datas_dialog[1], datas_dialog[2]
            human_png = DATAS.get_datas.img_human(human)
            img = pygame.image.load(human_png)

            SCREEN.blit(img, DATAS.const.POS_IMG_FOR_DIALOG)
            SCREEN.blit(self.window_dialog, DATAS.const.POS_DIALOG_WINDOW)

            mechanic_text(phrase, SCREEN, DATAS.const.START_POS_FOR_TEXT)

    def result(self, SCREEN):
        contact_with_button = DATAS.get_datas.inf_for_button()[0]
        self.draw_button(SCREEN) if contact_with_button else None
        self.draw_dialog(SCREEN)

