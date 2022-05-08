import pygame
import pytmx, pyscroll
from player import Player
from map import MapManager
from src.dialog import DialogBox


class Game:

    def __init__(self):
        # créer la fenêtre du jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon - Adventure")

        # générer le joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()

    def handle_input(self):

        pressed = pygame.key.get_pressed()
        if not self.dialog_box.reading:
            if pressed[pygame.K_UP] or pressed[pygame.K_z]:
                self.player.move_up()
            elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
                self.player.move_down()
            elif pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
                self.player.move_left()
            elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                self.player.move_right()

    def update(self):
        self.map_manager.update()

    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu
        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            pygame.display.flip()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collision(self.dialog_box)

            clock.tick(60)

        pygame.quit()
