# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


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


if __name__ == '__main__':
    make = AirTicketMaker(fio='Kulik', from_='Krasnodar', to='Innopolis', date='21/11')
    make.make_ticket()


# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


