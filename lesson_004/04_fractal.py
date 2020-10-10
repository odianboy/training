# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 1000)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

root_point = sd.get_point(600, 30)
# delta = 30
# #
# #
# def draw_bunches(start_point, angle, length):
#     if length < 10:
#         return
#     vector = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
#     vector.draw()
#     next_point = vector.end_point
#     next_angle = angle
#     next_length = length * 0.75
#     draw_bunches(start_point=next_point, angle=next_angle - delta, length=next_length)
#     draw_bunches(start_point=next_point, angle=next_angle + delta, length=next_length)
#
#
# draw_bunches(start_point=root_point, angle=90, length=250)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

# delta = sd.random_number(10, 40)
# delta = (30 + (30/100 * sd.random_number(1, 40)))
# delta_length = sd.random_number(1, 20)


def draw_bunches(start_point, angle, length):
    if length < 10:
        return
    vector = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
    vector.draw(color=sd.COLOR_RED)
    next_point = vector.end_point
    next_angle = angle
    next_length = length * (0.75 + (0.75 / 100 * sd.random_number(1, 20)))
    draw_bunches(start_point=next_point, angle=next_angle - sd.random_number(10, 40), length=next_length)
    draw_bunches(start_point=next_point, angle=next_angle + sd.random_number(10, 40), length=next_length)


draw_bunches(start_point=root_point, angle=90, length=100)


sd.pause()


