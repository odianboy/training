# -*- coding: utf-8 -*-
import threading
from collections import defaultdict
import os
import csv
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


class Ticker(threading.Thread):

    def __init__(self, dir_name, name_ticker, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dir_name = dir_name
        self.lock_ticker = lock
        self.name_ticker = name_ticker

    def run(self):
        self.result = {}
        with open(f"{self.dir_name}/{self.name_ticker}") as ff:
            total_list = []
            spam_reader = list(csv.reader(ff))

            for read in spam_reader[1:]:
                self.price = float(read[2])
                total_list.append(self.price)

                average_price = sum(total_list) / len(total_list)
                volatility = ((max(total_list)) - (min(total_list)) / average_price) * 100

                self.result[self.name_ticker[7:11]] = round(volatility, 4)

                total_list.clear()
        print(self.result)


if __name__ == '__main__':

    dir_name = os.listdir('trades')
    lock = threading.Lock
    count = [Ticker(dir_name='trades', name_ticker=line_ticker, lock=lock) for line_ticker in dir_name]

    for ticker in count:
        ticker.start()

    for ticker in count:
       ticker.join()
       print(ticker)