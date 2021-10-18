import pygame
import random


def random_color():
    return random.randint(50, 215), random.randint(50, 215), random.randint(50, 215)


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


class Player:
    def __init__(self, window):
        self.window = window
        self.color = (255, 0, 0)
        self.pos = (500, 450)
        self.size = 20
        self.dead = False

    def draw(self):
        pygame.draw.circle(self.window, self.color, self.pos, self.size)

    def change_pos(self, pos):
        self.pos = (self.pos[0] + pos[0], self.pos[1] + pos[1])

    def get_coords(self):
        return self.pos

    def die(self):
        self.dead = True

    def shrink(self):
        if self.size > 30:
            self.size -= 0.5

    def turn(self, keys_pressed):
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
            self.change_pos((0, -speed))
        if keys_pressed[pygame.K_a]:
            self.change_pos((-speed, 0))
        if keys_pressed[pygame.K_s]:
            self.change_pos((0, speed))
        if keys_pressed[pygame.K_d]:
            self.change_pos((speed, 0))

    def check_for_eat(self, game_info):
        x = -1
        divide_by = 1.1
        for dot in game_info.get_dots():
            x += 1
            if in_circle(self, divide_by, dot):
                game_info.delete_dot(x, self)


class AI:
    def __init__(self, window):
        self.window = window
        self.color = (0, 0, 0)
        self.pos = (500, 450)
        self.size = 20
        self.dead = False

    def draw(self):
        pygame.draw.circle(self.window, self.color, self.pos, self.size)

    def change_pos(self, pos):
        self.pos = (self.pos[0] + pos[0], self.pos[1] + pos[1])

    def get_coords(self):
        return self.pos

    def die(self):
        self.dead = True

    def shrink(self):
        if self.size > 30:
            self.size -= 0.5

    def turn(self, keys_pressed):
        speed = 3
        speed_count = 0
        if keys_pressed[0]:
            speed_count += 1
        if keys_pressed[1]:
            speed_count += 1
        if keys_pressed[2]:
            speed_count += 1
        if keys_pressed[3]:
            speed_count += 1

        if speed_count == 0:
            pass
        elif speed_count == 1 or speed_count == 3:
            speed = 3
        elif speed_count > 1:
            speed = 1.5

        if keys_pressed[0]:
            self.change_pos((0, -speed))
        if keys_pressed[1]:
            self.change_pos((-speed, 0))
        if keys_pressed[2]:
            self.change_pos((0, speed))
        if keys_pressed[3]:
            self.change_pos((speed, 0))

    def check_for_eat(self, game_info):
        x = -1
        divide_by = 1.1
        for dot in game_info.get_dots():
            x += 1
            if in_circle(self, divide_by, dot):
                game_info.delete_dot(x, self)


class RandomBot:
    def __init__(self, window):
        self.window = window
        self.color = (random_color())
        self.pos = (random.randint(200, 800), random.randint(200, 800))
        self.size = 20
        self.dead = False

    def draw(self):
        pygame.draw.circle(self.window, self.color, self.pos, self.size)

    def turn(self):
        keys_pressed = {"w": random.choice([True, False]), "a": random.choice([True, False]), "s": random.choice([True,
                        False]), "d": random.choice([True, False])}
        speed = 3
        speed_count = 0
        if keys_pressed["w"]:
            speed_count += 1
        if keys_pressed["a"]:
            speed_count += 1
        if keys_pressed["s"]:
            speed_count += 1
        if keys_pressed["d"]:
            speed_count += 1

        if speed_count == 0:
            pass
        elif speed_count == 1 or speed_count == 3:
            speed = 3
        elif speed_count > 1:
            speed = 1.5

        if keys_pressed["w"]:
            self.change_pos((0, -speed))
        if keys_pressed["a"]:
            self.change_pos((-speed, 0))
        if keys_pressed["s"]:
            self.change_pos((0, speed))
        if keys_pressed["d"]:
            self.change_pos((speed, 0))

    def change_pos(self, pos):
        self.pos = (self.pos[0] + pos[0], self.pos[1] + pos[1])

    def get_coords(self):
        return self.pos

    def die(self):
        self.dead = True

    def shrink(self):
        if self.size > 30:
            self.size -= 0.5

    def check_for_eat(self, game_info):
        x = -1
        divide_by = 1.1
        for dot in game_info.get_dots():
            x += 1
            if in_circle(self, divide_by, dot):
                game_info.delete_dot(x, self)


class Dot:
    def __init__(self, window):
        self.window = window
        self.color = (random_color())
        self.pos = (random.randint(10, 990), random.randint(10, 890))  # x then y
        self.size = 5

    def draw(self):
        pygame.draw.circle(self.window, self.color, self.pos, self.size)


class Game:
    def __init__(self, width=1000, height=900, respawn=True):
        self.ticks = 0
        self.dots = []
        self.players = []

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Agar.io bots")

    def start(self):
        self.dots = []
        for _ in range(400):
            i = Dot(self.window)
            self.dots.append(i)

    def random_bot(self):
        bot = RandomBot(self.window)
        self.players.append(bot)
        return bot

    def player(self):
        player = Player(self.window)
        self.players.append(player)
        return player

    def ai(self):
        ai = AI(self.window)
        self.players.append(ai)
        return ai

    def draw(self):
        self.window.fill((255, 255, 255))
        for i in self.dots:
            i.draw()
        self.sort()
        for player in self.players:
            if not player.dead:
                player.draw()
        pygame.display.update()

    def get_dots(self):
        return self.dots

    def delete_dot(self, spot, player):
        self.dots.pop(spot)
        dot = Dot(self.window)
        self.dots.append(dot)
        player.size += 0.2

    def check_for_player_eat(self):
        if len(self.players) < 2:
            return self.players
        for eating_player in self.players:
            if eating_player.dead is False:
                x = -1
                divide_by = 1.1
                for check_if_eaten_player in self.players:
                    if check_if_eaten_player.dead is False:
                        x += 1
                        bool_var = in_circle(eating_player, divide_by, check_if_eaten_player)
                        if bool_var is True and eating_player.size > check_if_eaten_player.size * 1.2:
                            check_if_eaten_player.die()
                            eating_player.size += check_if_eaten_player.size * 0.2

    def sort(self):
        sorted_list = []
        players_copy = self.players
        while len(players_copy) > 0:
            biggest = 0
            biggest_pos = 0
            x = 0
            for player in players_copy:
                if player.size > biggest:
                    biggest = player.size
                    biggest_pos = x
                x += 1
            sorted_list.append(players_copy[biggest_pos])
            players_copy.pop(biggest_pos)

        sorted_list.reverse()
        self.players = sorted_list

    def tick(self):
        self.ticks += 1
        if self.ticks == 60:
            self.ticks = 0
            for bot in self.players:
                if bot.dead:
                    bot.color = (random_color())
                    bot.pos = (random.randint(200, 800), random.randint(200, 800))
                    bot.size = 20
                    bot.dead = False
                bot.shrink()
