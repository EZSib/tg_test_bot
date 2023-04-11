import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '5424991242:AAGwomxQz1p46bRi_2m3V7kvJlt5RjK9xr0'
offset: int = -2
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    time.sleep(3)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')