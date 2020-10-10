# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 1000)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код

# sd.snowflake(center=point, length=100)
# y = 1000
# x = 100
#
# y2 = 950
# x2 = 150
#
# while True:
#     sd.clear_screen()
#     point = sd.get_point(x, y)
#     sd.snowflake(center=point, length=50)
#     y -= 10
#     if y < 50:
#         break
#     x += 5
#
#     point_2 = sd.get_point(x2, y2)
#     sd.snowflake(center=point_2, length=40)
#     y2 -= 10
#     if y2 < 50:
#         break
#     x2 += 10
#
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
# all_x = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
# all_y = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 0]

#
# def draw_snowflake(x, y):
#     point = sd.get_point(x, y)
#     sd.snowflake(center=point, length=sd.random_number(10, 25), color=sd.COLOR_CYAN)
#
#
# while True:
#     for i, _ in enumerate(all_x):
#         for z in range(21):
#             draw_snowflake(sd.randint(0, 1000), all_y[i] + sd.randint(100, 1000))
#             if all_y[i] <= 35:
#                 all_y[i] = 550
#
#         sd.sleep(0.1)
#         sd.clear_screen()
#     if sd.user_want_exit():
#         break
# #
# #

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугроб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


x = 0
y = 950
q = 5

all_x = [sd.randint(0, 1200) for z in range(q)]
all_y = [sd.randint(50, 500) for k in range(q)]
all_length = [sd.randint(10, 35) for n in range(q)]

y2 = 950


def snow_make(x1, y1, color):
    for i in range(q):
        sd.snowflake(center=sd.get_point(x1 + all_x[i], y1 + all_y[i]), length=all_length[i], color=color)


while True:
    sd.clear_screen()
    snow_make(x, y, color=sd.COLOR_CYAN)
    y -= 50
    if y + all_y[-1] <= 50:
        y = 100

    # snow_make(x, y2, color=sd.COLOR_CYAN)
    # y2 -= 50
    # if y2 <= 75:
    #     y2 = 950

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
