# lesson_3_task_3.py
from address import Address
from mailing import Mailing

# Создаем адреса (экземпляры класса Address)
to_address = Address("123456", "Москва", "Ленина ул.", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина ул.", "5", "10")

# Создаем почтовое отправление (экземпляр класса Mailing)
mailing = Mailing(to_address, from_address, 250, "ABC123")

# Получаем данные из экземпляра Mailing для печати
to_address_info = f"{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}"
from_address_info = f"{mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment}"

# Выводим информацию о почтовом отправлении в консоль
print(
    f"Отправление {mailing.track} из {to_address_info} в {from_address_info}. Стоимость {mailing.cost} рублей.")
