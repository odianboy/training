# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = 1200, 1000


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код


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


# def draw_vector(point, angle, length, width):
#     vector = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     vector.draw()
#     return vector


# triangle()
COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE = "0", "1", "2", "3", "4", \
                                                                                           "5", "6"
print("Возможные цвета:", "0 : red", "1 : orange", "2 : yellow", "3 : green", "4 : cyan", "5 : blue", "6 : purple",
      sep="\n")
# while True:
colors = input("Введите желаемый цвет: ")
    # if colors == "x":
    #     break
if colors == "0":
    colors = sd.COLOR_RED
elif colors == "1":
    colors = sd.COLOR_ORANGE
elif colors == "2":
    colors = sd.COLOR_YELLOW
elif colors == "3":
    colors = sd.COLOR_GREEN
elif colors == "4":
    colors = sd.COLOR_CYAN
elif colors == "5":
    colors = sd.COLOR_BLUE
elif colors == "6":
    colors = sd.COLOR_PURPLE
else:
    print("Вы ввели некоректный номер!")


def draw_vector(point, angle, length, width):
    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    vector.draw(color=colors)
    return vector


triangle_0, square_1, pentagon_2, hexagon_3 = "0", "1", "2", "3"

print("Возможные фигуры:", "0 : треугольник", "1 : квадрат", "2 : пятиугольник", "3 : шестиугольник", sep="\n")

figura = input("Введите желаемую фигуру: ")

if figura == "0":
    triangle()
elif figura == "1":
    square()
elif figura == "2":
    pentagon()
elif figura == "3":
    hexagon()
else:
    print("Вы ввели некоректный номер!")


sd.pause()
