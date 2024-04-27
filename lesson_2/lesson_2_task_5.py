def month_to_season(num):
    if num == 12 or num == 1 or num == 2:
        print("Это Зима")
    elif (num == 3 or num == 4 or num == 5):
        print("Это Весна")
    elif (num == 6 or num == 7 or num == 8):
        print("Это Лето")
    elif (num == 9 or num == 10 or num == 11):
        print("Это Осень")
    else:
        print("Введите корректный номер месяца!")


month = int(input("Введите номер месяца: "))

month_to_season(month)
