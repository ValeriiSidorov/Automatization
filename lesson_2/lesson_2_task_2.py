def is_year_leap(num):
    result = True
    if (num % 4 == 0):
        result = True
    else:
        result = False
    return result


year = int(input("Введите год: "))

print("Год", year, ":", is_year_leap(year))
