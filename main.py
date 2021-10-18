import pygame
import game

players = []
WIDTH, HEIGHT = 1000, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agar.io bots")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 60


def sort(things):
    sorted_list = []
    while len(things) > 0:
        biggest = 0
        biggest_pos = 0
        x = 0
        for thing in things:
            if thing.size > biggest:
                biggest = thing.size
                biggest_pos = x
            x += 1
        sorted_list.append(things[biggest_pos])
        things.pop(biggest_pos)

    sorted_list.reverse()
    return sorted_list


def draw_window(draw_me, manager):
    WIN.fill(WHITE)
    manager.draw()
    draw_me = sort(draw_me)
    for thing_to_draw in draw_me:
        thing_to_draw.draw()

    pygame.display.update()


def start():
    global players
    clock = pygame.time.Clock()
    run = True
    user = game.Player(WIN)
    bot = game.RandomBot(WIN)
    bot1 = game.RandomBot(WIN)
    bot2 = game.RandomBot(WIN)
    bot3 = game.RandomBot(WIN)
    bot4 = game.RandomBot(WIN)
    bot5 = game.RandomBot(WIN)
    bot6 = game.RandomBot(WIN)
    bot7 = game.RandomBot(WIN)
    bot8 = game.RandomBot(WIN)
    bot9 = game.RandomBot(WIN)
    bots = [user, bot, bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9]
    GAME = game.Game(WIN)
    GAME.players = bots
    bots = bots[1: len(bots) - 1]
    GAME.start()
    tick = 0
    while run:
        print(format(user.size, ",.2f"))
        tick += 1
        if tick == 60:
            tick = 0
            if user.size > 30:
                user.size -= 0.5
            bot.shrink()
        try:
            clock.tick(FPS)
        except KeyboardInterrupt:
            print("The end")
            break
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
        elif speed_count == 1 or speed_count == 3:
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

        for bot_var in bots:
            if bot_var.dead is False:
                bot_var.turn()

            bot_var.check_for_eat(GAME)
        players_copy = bots
        if user.dead is False:
            user.check_for_eat(GAME)

        GAME.check_for_player_eat()

        draw_window(players_copy, GAME)
    pygame.quit()


if __name__ == "__main__":
    start()
