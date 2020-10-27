# -*- coding: utf-8 -*-
import random


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.number = 1
        self.prime_numbers = []
        return self

    def _get_next(self):
        self.number += 1

        if self.number >= self.n:
            raise StopIteration()

        for prime in self.prime_numbers:
            if self.number % prime == 0:
                return
        self.prime_numbers.append(self.number)
        return self.number

    def __next__(self):
        value = None
        while value is None:
            value = self._get_next()

        return value

    def __repr__(self):
        return str(self.prime_numbers)


prime_number_iterator = PrimeNumbers(n=10000)
print('First')
for number in prime_number_iterator:
    print(number)

print('Second')
for number in prime_number_iterator:
    print(number)


    # Часть 2
    # Теперь нужно создать генератор, который выдает последовательность простых чисел до n
    # Распечатать все простые числа до 10000 в столбик

    def prime_numbers_generator(n):
        prime_numbers = []
        for number in range(2, n + 1):
            for prime in prime_numbers:
                if number % prime == 0:
                    break
            else:
                prime_numbers.append(number)
                yield number

for number in prime_numbers_generator(n=10000):
    print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


def lucky_number(number):
    number = str(number)
    sum_1, sum_2 = 0, 0
    for i in range(0,
                   int(len(number) // 2)):
        sum_1 += int(number[i])
        sum_2 += int(number[-i - 1])
    if sum_1 == sum_2:
        yield True, print(f'Самма первых двух чисел - {sum_1}, Последних - {sum_2}')
    else:
        yield False, print(f'Самма первых двух чисел - {sum_1}, Последних - {sum_2}')


# while True:
#     rand = random.randint(1, 99999999999)
#     lucky = good_number(number=(rand))
#
#     for num in lucky:
#         print(num)

def palindromic_numbers(number):
    number = str(number)
    lst = []
    for i in range(0, int(len(number) // 2)):
        if int(number[i]) == int(number[-i - 1]):
            lst.append(True)
        else:
            lst.clear()
            break
    yield True if True in lst else False


palindromic = palindromic_numbers(723327)
for num in palindromic:
    print(num)
