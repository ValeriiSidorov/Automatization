def bank(X, Y):
    curr_amount = X
    for year in range(Y):
        curr_amount *= 1.1
    return curr_amount


init_amount = int(input("Введите начальную сумму: "))
years = int(input("Введите количество лет: "))

final_amount = bank(init_amount, years)
print("Сумма на счету после", years, "лет:", round(final_amount, 2))
