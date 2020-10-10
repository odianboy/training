import simple_draw as sd
import random


def create_snowflakes(quantity):
    all_x = [random.randint(0, 1200) for z in range(quantity)]
    all_y = [random.randint(50, 500) for k in range(quantity)]
    for i in range(quantity):
        sd.snowflake(center=sd.get_point(all_x[i], all_y[i]), length=35, color=sd.COLOR_CYAN)



def snowflakes_color(color):
    return color


def shift_snowflakes():
    pass


def snowflake_numbers():
    pass


def del_numbers_snowflake():
    pass