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

    def move(self, keys_pressed):
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
    def __init__(self, window):
        self.dots = []
        self.window = window
        self.players = []

    def start(self):
        self.dots = []
        for _ in range(400):
            i = Dot(self.window)
            self.dots.append(i)

    def draw(self):
        for i in self.dots:
            i.draw()

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
            x = -1
            divide_by = 1.1
            for check_if_eaten_player in self.players:
                x += 1
                bool_var = in_circle(eating_player, divide_by, check_if_eaten_player)
                if bool_var is True and eating_player.size > check_if_eaten_player.size * 1.2:
                    check_if_eaten_player.die()
                    eating_player.size += check_if_eaten_player.size * 0.2


class BadBot:
    def __init__(self, window):
        self.window = window
        self.color = (random_color())
        self.pos = (200, 450)
        self.size = 20
        self.dead = False
        self.moving = "right"

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
