import pygame, sys
from src.game import Game

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Pygamon - Adventure")
screen = pygame.display.set_mode((800, 600))

font = pygame.font.SysFont(None, 20)
game = Game()

pygame.init()
click = False


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    bg = pygame.image.load("../gui/main_menu_bg.png")
    while True:

        screen.fill((0, 0, 0))
        draw_text("main_menu", font, (255, 255, 255), screen, 20, 20)
        screen.blit(bg, (0, 0))
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 450, 200, 50)

        if button_1.collidepoint(mx, my):
            if click:
                game.run()

        pygame.draw.rect(screen, (255, 0, 0), button_1)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def option():
    while True:

        screen.fill((0, 0, 0))
        draw_text('Options', font, (255, 255, 255), screen, 20, 20)

        for event in pygame.event.get():
            if event == KEYDOWN:
                if event.key == K_ESCAPE:
                    pass

        pygame.display.update()
        mainClock.tick(60)
