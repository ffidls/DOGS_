import pygame
import FIRST_PART.DIALOG_BUTTONS.mechanic_contact
import FIRST_PART.DATAS.get_datas, FIRST_PART.DATAS.const


def mechanic_text(phrase, SCREEN, pos):
    my_font = pygame.font.SysFont('FIRST_PART/DATAS/DATAS_CONTACT/m3x6.ttf', 20)

    if FIRST_PART.DATAS.const.WINDOW_WIDTH >= (len(phrase) - 2) * FIRST_PART.DATAS.const.LEN_ONE_WORD:
        text_surface = my_font.render(phrase, False, (0, 0, 0))
        SCREEN.blit(text_surface, pos)
    else:
        index = (FIRST_PART.DATAS.const.WIDTH_WINDOW_TEXT // FIRST_PART.DATAS.const.LEN_ONE_WORD - len(phrase))
        new_phrase, phrase = f'{phrase[:index]} -', f'- {phrase[index:]}'
        text_surface = my_font.render(new_phrase, False, (0, 0, 0))
        SCREEN.blit(text_surface, pos)

        mechanic_text(phrase, SCREEN, (pos[0], pos[1] + FIRST_PART.DATAS.const.INDENT_TEXT))


class ASSEMBLING:
    def __init__(self):
        #self.img_button = pygame.image.load(FIRST_PART.DATAS.get_datas.img_button())
        self.inf_button_dialog = FIRST_PART.DIALOG_BUTTONS.mechanic_contact.SETTING_CONTACT()

        self.window_dialog = pygame.image.load(FIRST_PART.DATAS.get_datas.window_dialog())

    def draw_button(self, SCREEN):
        pos = self.inf_button_dialog.setting_for_draw_button()
        #SCREEN.blit(self.img_button, (pos[0], pos[1]))

    def draw_dialog(self, SCREEN):
        datas_dialog = self.inf_button_dialog.datas_from_draw_dialog()
        if datas_dialog is not None:
            human, phrase = datas_dialog[1], datas_dialog[2]
            human_png = FIRST_PART.DATAS.get_datas.img_human(human)
            img = pygame.image.load(human_png)

            SCREEN.blit(img, FIRST_PART.DATAS.const.POS_IMG_FOR_DIALOG)
            SCREEN.blit(self.window_dialog, FIRST_PART.DATAS.const.POS_DIALOG_WINDOW)

            mechanic_text(phrase, SCREEN, FIRST_PART.DATAS.const.START_POS_FOR_TEXT)

    def result(self, SCREEN):
        contact_with_button = FIRST_PART.DATAS.get_datas.inf_for_button()[0]
        self.draw_button(SCREEN) if contact_with_button else None
        self.draw_dialog(SCREEN)

