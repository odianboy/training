# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):

    def draw_vector(point, angle, length, width):
        vector = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        vector.draw()
        return vector

    if n == 3:
        def triangle(point, angle, length, width=2, def_vector=120):
            last_endpoint = point
            for i in range(1, 4):
                vector = draw_vector(last_endpoint, angle, length, width)
                last_endpoint = vector.end_point
                angle += def_vector
        return triangle
    elif n == 4:
        def square(point=sd.get_point(300, 300), angle=0, length=200, width=2, def_vector=90):
            last_endpoint = point
            for i in range(1, 5):
                vector = draw_vector(last_endpoint, angle, length, width)
                last_endpoint = vector.end_point
                angle += def_vector
        return square
    elif n == 5:
        def pentagon(point=sd.get_point(300, 300), angle=0, length=200, width=2, def_vector=72):
            last_endpoint = point
            for i in range(1, 6):
                vector = draw_vector(last_endpoint, angle, length, width)
                last_endpoint = vector.end_point
                angle += def_vector
        return pentagon
    elif n == 6:
        def hexagon(point=sd.get_point(300, 300), angle=0, length=200, width=2, def_vector=60):
            last_endpoint = point
            for i in range(1, 7):
                vector = draw_vector(last_endpoint, angle, length, width)
                last_endpoint = vector.end_point
                angle += def_vector
        return hexagon
    raise Exception('Могу принимать только эти параметры 3, 4, 5, 6')


draw_figure = get_polygon(n=3)
draw_figure(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()
