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

    def figure(point, angle, length, def_vector, width=2):
        last_endpoint = point
        for i in range(1, n + 1):
            vector = draw_vector(last_endpoint, angle, length, width)
            last_endpoint = vector.end_point
            angle += def_vector
    return figure


draw_figure = get_polygon(n=3)
draw_figure(point=sd.get_point(200, 200), angle=13, length=100, def_vector=120)


sd.pause()
