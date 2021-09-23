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


def in_circle(player, divide_by, dot):
    dot_x = dot.pos[0]
    dot_y = dot.pos[1]
    player_x = player.pos[0]
    player_y = player.pos[1]
    if player.pos[0] + (player.size / divide_by) > dot.pos[0] > player.pos[0] - (player.size / divide_by) and \
            player.pos[1] + (player.size / divide_by) > dot.pos[1] > player.pos[1] - (player.size / divide_by):
        if dot_x + dot_y < player_x + player_y:
            return True
        elif dot_x - dot_y < player_x - player_y:
            return True
        else:
            return False
    return False


def check_for_eat(players1, game_info):
    for player in players1:
        x = -1
        divide_by = 1.1
        for dot in game_info.get_dots():
            x += 1
            if in_circle(player, divide_by, dot):
                game_info.delete_dot(x, player)


def check_for_player_eat(players1):
    players2 = players1
    if len(players2) < 2:
        return players2
    for eating_player in players2:
        x = -1
        divide_by = 1.1
        for check_if_eaten_player in players2:
            x += 1
            bool_var = in_circle(eating_player, divide_by, check_if_eaten_player)
            if bool_var is True and eating_player.size > check_if_eaten_player.size * 1.2:
                check_if_eaten_player.die()
                eating_player.size += check_if_eaten_player.size * 0.2


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
    players = [user, bot, bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9]
    GAME = game.Game(WIN)
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

        if bot.dead is False:
            bot.turn()
        players = []
        if user.dead is False:
            players.append(user)
        if bot.dead is False:
            players.append(bot)
        players_copy = players
        check_for_eat(players_copy, GAME)

        check_for_player_eat(players)

        draw_window(players_copy, GAME)
    pygame.quit()


if __name__ == "__main__":
    start()
