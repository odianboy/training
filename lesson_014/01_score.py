# -*- coding: utf-8 -*-
import random

# Вас взяли на работу в молодой стартап. Идея стартапа - предоставлять сервис расчета результатов игр.
# Начать решили с боулинга, упрощенной версии.
#
# Правила такие.
#
# Всего 10 кеглей. Игра состоит из 10 фреймов. В одном фрейме до 2х бросков, цель - сбить все кегли.
# Результаты фрейма записываются символами:
#   «Х» – «strike», все 10 кеглей сбиты первым броском
#   «<число>/», например «4/» - «spare», в первый бросок сбиты 4 кегли, во второй – остальные
#   «<число><число>», например, «34» – в первый бросок сбито 3, во второй – 4 кегли.
#   вместо <число> может стоять прочерк «-», например, «-4» - ни одной кегли не было сбито за бросок (первый или второй)
# Результат игры – строка с записью результатов фреймов. Символов-разделителей между фреймами нет.
# Например, для игры из 3 фреймов запись результатов может выглядеть так:
#   «Х4/34»
# Предлагается упрощенный способ подсчета количества очков:
#   «Х» – 20 очков, «4/» - 15 очков, «34» – сумма 3+4=7
# То есть для игры «Х4/34» сумма очков равна 20+15+7=42
#
# Надо написать python-модуль (назвать bowling), предоставляющий API расчета количества очков:
# функцию get_score, принимающую параметр game_result. Функция должна выбрасывать исключения,
# когда game_result содержит некорректные данные. Использовать стандартные исключения по максимуму,
# если не хватает - создать свои.
#
# Обязательно написать тесты на этот модуль. Расположить в папке tests.

# Из текущего файла сделать консольную утилиту для определения количества очков, с помощью пакета argparse
# Скрипт должен принимать параметр --result и печатать на консоль:
#   Количество очков для результатов ХХХ - УУУ.


def bowling():

    result = []
    points = []

    print('Начинаем партию!')
    for frame in range(10):

        throw = 2
        attempt = 0

        while attempt < throw:
            attempt += 1
            shot = random.randint(0, 10)

            if shot == 10:
                result.append('X')
                points.append(20)
                break
            elif shot == 4:
                result.append(shot)
                if attempt == 1:
                    points.append(15)
                else:
                    points.append(4)
                continue
            elif shot == 0:
                result.append('-')
                points.append(0)
                continue
            else:
                result.append(shot)
                points.append(shot)

    print('Партия завершилась со следующим результатом:', '\n', result)
    print('Всего было заработано очков:', '\n', sum(points))


def get_score(game_result=None):
    try:
        if game_result != 'get':
            raise NameError(f'неверный параметр функции, {game_result}')
        elif game_result == 'get':
            return bowling()
    except NameError as exc:
        print(f'Поймана ошибка: {exc}')


get_score('get')

# При написании кода помнить, что заказчик может захотеть доработок и новых возможностей...
# И, возможно, вам пригодится паттерн проектирования "Состояние",
#   см https://clck.ru/Fudd8 и https://refactoring.guru/ru/design-patterns/state

