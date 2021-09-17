import pygame


class Player:
    def __init__(self, window):
        self.window = window
        self.color = (255, 0, 0)
        self.pos = (500, 450)
        self.size = 50

    def draw(self):
        pygame.draw.circle(self.window, self.color, self.pos, self.size)

    def change_pos(self, pos):
        self.pos = (self.pos[0] + pos[0], self.pos[1] + pos[1])
