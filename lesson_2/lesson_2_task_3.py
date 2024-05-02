import math


def square(side_length):
    area = side_length ** 2
    rounded_area = math.ceil(area)
    return rounded_area


side = float(input("Введите сторону квадрата: "))
print("Площадь квадрата с длиной стороны", side, "равна", square(side))
