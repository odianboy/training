# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

def iter_log():
    sum_nok = 0
    pprint = ''

    for i in range(0, 6):
        with open('events.txt') as file:
            for text in file:
                if 'NOK' in text:
                    if int(text[15]) == i:
                        pprint = text[:17] + ']'
                        sum_nok += 1

        yield pprint, sum_nok

        sum_nok = 0
        pprint = ''


grouped_events = iter_log()
for group_time, event_count in grouped_events:
    print(group_time, event_count)