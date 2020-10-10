# -*- coding: utf-8 -*-

import simple_draw as sd
import random
sd.resolution = (1200, 1000)

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

# TODO здесь ваш код


class Snowflake:
    def __init__(self):
        self.x = 100
        self.y = 950
        self.length = random.randint(10, 35)
        self.color = sd.COLOR_CYAN

    def move(self):
        self.y -= 50

    def draw(self):
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=self.color)

    def clear_previous_picture(self):
        sd.clear_screen()

    def can_fall(self):
        if self.y == 0:
            self.y = 950


flake = Snowflake()

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     # if not flake.can_fall():
#     #     break
#     sd.sleep(0.1)
#     if flake.can_fall():
#         break
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

# flakes = get_flakes(count=N)  # создать список снежинок


def get_flakes(count):
    db = []
    for i in range(count):
        db.append(flake)
    return db


flakes = get_flakes(10)

#
# def get_fallen_flakes():
#     qua = 0
#     for flake in flakes:
#        qua += 1
#     print(qua)


while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        flake.can_fall()
    # fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    # if fallen_flakes:
    #     append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


