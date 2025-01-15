
exchange_rate = float(input("Введите курс валюты (сколько стоит 1 единица другой валюты): "))

amount = float(input("Введите сумму в вашей валюте: "))

converted_amount = amount / exchange_rate

print(f"Сумма в другой валюте: {converted_amount}")