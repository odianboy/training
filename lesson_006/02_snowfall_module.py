# -*- coding: utf-8 -*-

import simple_draw as sd
import random


# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
def rand(N):
    global length, x
    # length = [random.randint(5, 50) for d in range(N)]
    x = [random.randint(30, 1200) for s in range(N)]


def creat_show(N, Y, color):
    for i in range(N):
        point = sd.get_point(x[i], Y)
        show = sd.snowflake(point, length=35, color=color)


N = random.randint(4, 7)
rand(N)

y = 550

while True:
    creat_show(N, Y=y, color=sd.background_color)
    y -= 15
    creat_show(N, Y=y, color=sd.COLOR_CYAN)
    sd.sleep(0.1)
    if y <= 35:
        y = 550
        N = random.randint(4, 8)
        rand(N)
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
