# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import argparse


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

#
class AirTicketMaker:

    def __init__(self, fio, from_, to, date):
        self.fio = fio
        self.from_ = from_
        self.to = to
        self.date = date

    def make_ticket(self):
        image = Image.open("Images/ticket_template.png")

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("fonts/ofont_ru_Cyntho Next Slab.ttf", size=20)

        draw.text((45, 125), self.fio, font=font, fill='black')
        draw.text((45, 194), self.from_, font=font, fill='black')
        draw.text((45, 260), self.to, font=font, fill='black')
        draw.text((286, 260), self.date, font=font, fill='black')

        image.show()


# if __name__ == '__main__':
#     make = AirTicketMaker(fio='Kulik', from_='Krasnodar', to='Innopolis', date='21/11')
#     make.make_ticket()


# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


parser = argparse.ArgumentParser()

parser.add_argument("-f", "--fio", action="store_const", const="KULIK", help="client's surname")
parser.add_argument("-fm", "--from_", action="store_const", const="KRASNODAR", help="where are we flying from")
parser.add_argument("-t", "--to", action="store_const", const="INNOPOLIS", help="where are we flying")
parser.add_argument("-d", "--date", action="store_const", const="23/11", help="flight date")
parser.add_argument("save_to", help="save ticket", default="yes")

args = parser.parse_args()


def make_ticket(fio, from_, to, date, save_to):
    image = Image.open("lesson_013/Images/ticket_template.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("lesson_013/fonts/ofont_ru_Cyntho Next Slab.ttf", size=20)

    draw.text((45, 125), fio, font=font, fill='black')
    draw.text((45, 194), from_, font=font, fill='black')
    draw.text((45, 260), to, font=font, fill='black')
    draw.text((286, 260), date, font=font, fill='black')

    if args.save_to == 'yes':
        image.save("lesson_013/ready_ticket.png")
    else:
        image.show()


make_ticket(args.fio, args.from_, args.to, args.date, args.save_to)
