import pygame
from gui import draw_text


class Inventory:

    def __init__(self):
        self.name = "inventory"
        self.xpos = 20
        self.ypos = 30
        self.width = 500
        self.height = 500
        self.font = pygame.font.Font("../dialogs/dialog_font.ttf", 18)

    def init(self):
        pass
