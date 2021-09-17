import pygame
from pygame.locals import *
import player

WIDTH, HEIGHT = 1000, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agar.io bots")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 60


def draw_window(user):
    WIN.fill(WHITE)
    user.draw()
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    user = player.Player(WIN)
    while run:
        clock.tick(FPS)
        for this_event in pygame.event.get():
            if this_event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        speed = 3
        speed_count = 0
        if keys_pressed[pygame.K_w]:
            speed_count += 1
        if keys_pressed[pygame.K_a]:
            speed_count += 1
        if keys_pressed[pygame.K_s]:
            speed_count += 1
        if keys_pressed[pygame.K_d]:
            speed_count += 1

        if speed_count == 0:
            pass
        elif speed_count == 1:
            speed = 3
        elif speed_count > 1:
            speed = 1.5

        if keys_pressed[pygame.K_w]:
            user.change_pos((0, -speed))
        if keys_pressed[pygame.K_a]:
            user.change_pos((-speed, 0))
        if keys_pressed[pygame.K_s]:
            user.change_pos((0, speed))
        if keys_pressed[pygame.K_d]:
            user.change_pos((speed, 0))

        draw_window(user)
    pygame.quit()


if __name__ == "__main__":
    main()
