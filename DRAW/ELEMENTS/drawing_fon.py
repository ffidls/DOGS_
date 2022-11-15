import pygame
import DATAS.get_datas, DATAS.const


class FON:
    def __init__(self):
        self.get_locations = DATAS.get_datas.locations()

        self.width, self.height = DATAS.const.WIDTH, DATAS.const.HEIGHT
        self.location = self.get_locations

        self.setting_screen()

    def setting_screen(self):
        self.background = pygame.image.load(self.location)  # Фон

    def draw_fon(self, SCREEN):
        SCREEN.blit(self.background, (0, 0))
