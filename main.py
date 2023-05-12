import requests
import json

# змінні, що зберігаються з вводу користувача
select_date = input("Введіть дату конвертації (у форматі YYYY-MM-DD): ")
split_date = select_date.split("-")
base_currency = input("Введіть код валюти, яку потрібно конвертувати: ")
target_currency = input("Введіть код валюти, в яку потрібно конвертувати: ")
amount = input("Введіть суму ваших коштів, яку потрібно конвертувати: ")

# змінні до api
api_key = 'ВАШ_АПІ_КЛЮЧ'
url = f"https://v6.exchangerate-api.com/v6/{api_key}/history/{base_currency}/{split_date[0]}/{split_date[1]}/{split_date[2]}"

# # запрос до api
response = requests.get(url)
data = response.json()

# Виведення даних у консоль
try:
    # Конвертація
    conversion_rate = data['conversion_rates'][target_currency]
    currency_name = data['base_code']
    converted_amount = float(amount) * conversion_rate

    print(f"Ваші кошти: {float(amount)} {currency_name}")
    print(f"Дата конвертації: {select_date}")
    print(f"Конвертована сума: {round(converted_amount, 2)} {target_currency}")
except KeyError:
    print(f"Помилка: {data['error-type']}. Немає даних за цією датою, спробуйте іншу дату.")