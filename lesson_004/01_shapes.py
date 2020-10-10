# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 1000)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код


# point = sd.get_point(300, 300)

# def triangle(start_point, angle, length):
#
#     v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=width)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=width)
#     v3.draw()
#

# triangle(point=sd.get_point(300, 300), angle=0)

# def square(point, angle, length=200):
#
#     v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=2)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=2)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=210, length=200, width=2)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=300, length=200, width=2)
#     v4.draw()
#
# # square(point=sd.get_point(300,300), angle=30)


# def pentagon(point, angle, length=200):
#
#     v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=2)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=108, length=200, width=2)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=180, length=200, width=2)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=252, length=200, width=2)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=324, length=200, width=2)
#     v5.draw()


# pentagon(point=sd.get_point(300, 300), angle=36)

# def hexagon(point, angle, length=200):
#
#     v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=2)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=2)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=180, length=200, width=2)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=240, length=200, width=2)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=300, length=200, width=2)
#     v5.draw()
#
#     v6 = sd.get_vector(start_point=v5.end_point, angle=360, length=200, width=2)
#     v6.draw()

# hexagon(point=sd.get_point(300,300), angle=60)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

def draw_vector(point, angle, length, width):
    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    vector.draw()
    return vector


def hexagon(point=sd.get_point(300, 300), angle=0, length=200, width=2, def_vector=60):
    last_endpoint = point
    for i in range(1, 7):
        vector = draw_vector(last_endpoint, angle, length, width)
        last_endpoint = vector.end_point
        angle += def_vector


# hexagon()

def pentagon(point=sd.get_point(300, 300), angle=0, length=200, width=2, def_vector=72):
    last_endpoint = point
    for i in range(1, 6):
        vector = draw_vector(last_endpoint, angle, length, width)
        last_endpoint = vector.end_point
        angle += def_vector


# pentagon()


def square(point=sd.get_point(300, 300), angle=0, length=200, width=2, def_vector=90):
    last_endpoint = point
    for i in range(1, 5):
        vector = draw_vector(last_endpoint, angle, length, width)
        last_endpoint = vector.end_point
        angle += def_vector


# square()

def triangle(point=sd.get_point(300, 300), angle=0, length=200, width=2, def_vector=120):
    last_endpoint = point
    for i in range(1, 4):
        vector = draw_vector(last_endpoint, angle, length, width)
        last_endpoint = vector.end_point
        angle += def_vector

# triangle()


# triangle()
# square()
# pentagon()
# hexagon()



# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
