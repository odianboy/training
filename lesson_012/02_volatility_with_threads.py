# -*- coding: utf-8 -*-
import threading
import os
import csv
from threading import Thread
from lesson_012.python_snippets.utils import time_track

# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#


class Ticker(Thread):

    def __init__(self, dir_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dir_name = dir_name

    def run(self):
        result = {}
        null_result = {}
        files = os.listdir(self.dir_name)
        for file_name in files:
            with open(f"{self.dir_name}/{file_name}") as ff:
                total_list = []
                spam_reader = list(csv.reader(ff))
                ticker_name = file_name[7:11]

                for read in spam_reader[1:]:
                    self.price = float(read[2])
                    total_list.append(self.price)

                maximum = max(total_list)
                minimum = min(total_list)
                average = sum(total_list) / len(total_list)
                volatility = round((maximum - minimum) / average * 100, 4)

                if not volatility:
                    null_result[ticker_name] = volatility
                else:
                    result[ticker_name] = volatility

        result = sorted(result.items(), key=lambda row: row[1], reverse=True)

        def _print_result(data):
            for _ticker_name, _volatility in data:
                print(f'\t{_ticker_name} - {_volatility}', '%')

        print('\nМаксимальная волатильность:')
        _print_result(result[:3])

        print('\nМинимальная волатильность:')
        _print_result(result[len(result)-3:])

        print('\nНулевая волатильность:')
        _print_result(null_result.items())


if __name__ == '__main__':
    thread = Ticker('trades')
    thread2 = Ticker('trades')
    thread.start()
    thread.join()
    thread2.start()
    thread2.join()

