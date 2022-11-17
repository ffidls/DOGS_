import pygame
import DIALOG_BUTTONS.mechanic_contact
import DATAS.get_datas


class ASSEMBLING:
    def __init__(self):
        self.img_button = pygame.image.load('DATAS/DATAS_CONTACT/button.png')
        self.inf_pos_button = DIALOG_BUTTONS.mechanic_contact.SETTING_CONTACT()

    def draw_button(self, SCREEN):
        pos = self.inf_pos_button.setting_for_draw_button()
        SCREEN.blit(self.img_button, (pos[0], pos[1]))

    def draw_dialog(self, text):
        pass

    def result(self, SCREEN):
        contact_with_button = DATAS.get_datas.inf_for_button()[0]
        self.draw_button(SCREEN) if contact_with_button else None
