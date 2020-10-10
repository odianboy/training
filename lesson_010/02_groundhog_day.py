# -*- coding: utf-8 -*-
from random import randint
import warnings
from termcolor import cprint

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777
total_day = 0
karma = 0


# TODO здесь ваш код


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    cube = randint(1, 13)
    global karma
    try:
        if cube == 1:
            raise IamGodError('Я Бог!')
        elif cube == 2:
            raise DrunkError('Выпил')
        elif cube == 3:
            raise CarCrashError('Разбился на машине')
        elif cube == 4:
            raise GluttonyError('Я объелся')
        elif cube == 5:
            raise DepressionError('У меня депрессия')
        elif cube == 6:
            raise SuicideError('Покончил с жизнью')
        else:
            karma += randint(1, 7)
            print('Количество кармы полученно:', karma)
        return karma

    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
        cprint(f'Поймано исключение: {exc}', color='red')


try:
    while karma <= ENLIGHTENMENT_CARMA_LEVEL:
        one_day()
        total_day += 1
        # with open('log_error.txt', mode='a') as ff:
        #     for line in str(one_day()):
        #         ff.write(str(one_day()) + '\n')
        print('Количество дней прошло:', total_day)
except TypeError as exc:
    cprint(f'Было поймано исключение {exc}', color='cyan')


# https://goo.gl/JnsDqu
