# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
quantity_month = 0   # Количество прожитых месяцев
grants = 0  # Сумма ежемеечных стипендний
costs = 0  # Сумма ежемеечных расходов


while quantity_month != 10:  # До тех пор пока количество месяцев не равно 10
    grants += educational_grant
    if quantity_month == 0:
        month = expenses
        costs += month      # Накопительный счет для расходов с повышением цен на 3%
    elif quantity_month == 1:
        month_2 = month + (month * 0.03)
        costs += month_2
    elif quantity_month == 2:
        month_3 = month_2 + (month_2 * 0.03)
        costs += month_3
    elif quantity_month == 3:
        month_4 = month_3 + (month_3 * 0.03)
        costs += month_4
    elif quantity_month == 4:
        month_5 = month_4 + (month_4 * 0.03)
        costs += month_5
    elif quantity_month == 5:
        month_6 = month_5 + (month_5 * 0.03)
        costs += month_6
    elif quantity_month == 6:
        month_7 = month_6 + (month_6 * 0.03)
        costs += month_7
    elif quantity_month == 7:
        month_8 = month_7 + (month_7 * 0.03)
        costs += month_8
    elif quantity_month == 8:
        month_9 = month_8 + (month_8 * 0.03)
        costs += month_9
    elif quantity_month == 9:
        month_10 = month_9 + (month_9 * 0.03)
        costs += month_10

    quantity_month += 1

print('Студенту надо попросить', round(costs - grants, 2), "рублей")











