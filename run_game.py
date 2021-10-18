import random

import pygame

import game_manager
from game_manager import Game

players = []

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 60


class MyAI:
    def __init__(self, game, weights=False):
        if weights is False:
            weights = []
            for i in range(300):
                weights.append((random.randint(0, 100) - 50) * 0.1)


def start():
    global players
    clock = pygame.time.Clock()
    game = Game()

    run = True

    game.player()
    game.ai()
    game.random_bot()
    game.random_bot()
    game.random_bot()
    game.random_bot()
    game.random_bot()
    game.random_bot()
    game.random_bot()
    game.random_bot()
    game.random_bot()
    game.random_bot()

    game.start()
    while run:
        game.tick()
        try:
            clock.tick(FPS)
        except KeyboardInterrupt:
            print("The end")
            break
        for this_event in pygame.event.get():
            if this_event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()

        # put keys in player class as object self.keys so game can call them to fix error.
        for bot_var in game.players:
            if bot_var.dead is False:
                if type(bot_var) == game_manager.Player:
                    bot_var.turn(keys_pressed)
                elif type(bot_var) == game_manager.AI:
                    bot_var.turn([1, 0, 0, 0])
                else:
                    bot_var.turn()

            bot_var.check_for_eat(game)

        game.check_for_player_eat()

        game.draw()
    pygame.quit()


if __name__ == "__main__":
    start()
