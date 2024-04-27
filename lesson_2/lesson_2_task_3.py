def square(num):
    result = num * num
    return result


storona = float(input("Введите сторону квадрата: "))

print("Площадь квадрата со стороной =", storona,
      ", равна", round(square(storona)))
