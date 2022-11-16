import DRAW.ELEMENTS.drawing_fon, DRAW.ELEMENTS.drawing_people
import DRAW.ELEMENTS.drawing_buttons


class DRAW_MOVING_AND_FON:
    def __init__(self, SCREEN):
        self.fon_screen = DRAW.ELEMENTS.drawing_fon.FON()
        self.people = DRAW.ELEMENTS.drawing_people.MOVING_PEOPLE()
        self.buttons = DRAW.ELEMENTS.drawing_buttons.ASSEMBLING()

        self.screen = SCREEN

    def processor(self):
        self.fon_screen.draw_fon(self.screen)
        self.people.anna(self.screen)
        self.buttons.result(self.screen)
