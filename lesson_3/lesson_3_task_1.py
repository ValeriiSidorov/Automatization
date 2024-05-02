# lesson_3_task_1.py

# Импортируем класс User из модуля user
from user import User

# Создаем новый экземпляр класса User и сохраняем его в переменную my_user
my_user = User("Иван", "Иванов")

# Вызываем методы объекта my_user
my_user.print_first_name()
my_user.print_last_name()
my_user.print_full_name()
