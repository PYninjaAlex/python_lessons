import requests

URL = 'https://api.telegram.org/bot'

METHOD_getUpdates = '/getUpdates'

METHOD_send_message = '/sendMessage'
TOKEN = '5682038187:AAHvMAJdh2_N3b3u91bFR04IJ00poZwNPAg'

Updates = requests.get(URL+TOKEN+METHOD_getUpdates).json()
chat_id = Updates["result"][0]["message"]["chat"]["id"]

text = input("Введите что хотите отправить через бота пользователю ")

requests.get(URL+TOKEN+METHOD_send_message+f"?chat_id={chat_id}&text={text}")
