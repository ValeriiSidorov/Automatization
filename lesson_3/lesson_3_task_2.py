# lesson_3_task_2.py

from smartphone import Smartphone

# Объявляем переменную catalog как список для хранения экземпляров Smartphone
catalog = []

# Создаем пять разных экземпляров класса Smartphone и добавляем их в список catalog
catalog.append(Smartphone("Apple", "iPhone 13", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Mi 12", "+79345678901"))
catalog.append(Smartphone("Google", "Pixel 7", "+79456789012"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79567890123"))

# Печатаем каталог (список) в заданном формате
print("Каталог смартфонов:")
for phone in catalog:
    print(phone)
