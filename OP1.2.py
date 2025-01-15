#Запрашиваем данные

name = input("Введите ваше имя")
age = int(input("Введите ваш возраст"))

months = age * 12
days = age * 365  # Упрощённо считаем, что в году 365 дней
hours = days * 24
minute = hours * 60
secund = minute * 60


# Вывод результата
print(f"Привет, {name}! Тебе {age} лет.")
print(f"Ты прожил(а) примерно {months} месяцев, {days} дней и {hours} часов и {minute} и {secund}")