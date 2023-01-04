import FIRST_PART.DRAW.ELEMENTS.drawing_fon, FIRST_PART.DRAW.ELEMENTS.drawing_people
import FIRST_PART.DRAW.ELEMENTS.drawing_buttons
import FIRST_PART.DRAW.ELEMENTS.drawing_dogs


class DRAW_MOVING_AND_FON:
    def __init__(self, SCREEN):
        self.fon_screen = FIRST_PART.DRAW.ELEMENTS.drawing_fon.FON()
        self.people = FIRST_PART.DRAW.ELEMENTS.drawing_people.MOVING_PEOPLE()
        self.buttons = FIRST_PART.DRAW.ELEMENTS.drawing_buttons.ASSEMBLING()
        self.dogs = FIRST_PART.DRAW.ELEMENTS.drawing_dogs.MOVING_DOG()

        self.screen = SCREEN

    def processor(self):
        self.fon_screen.draw_fon(self.screen)
        self.dogs.miki(self.screen)
        #self.people.kira(self.screen)
        self.people.anna(self.screen)
        self.buttons.result(self.screen)
