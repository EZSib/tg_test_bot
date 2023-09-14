import requests
import time
from random import choice

list_bibl_math = None
with open('bibl_Math.txt' ) as file:
    list_bibl_math = file.read().split('@')[1:]
# a = ['Готов вкалывать', 'С удовольствием', 'Опять работа!?', 'я не глупая','yes', 'no', 'u are my slave', 'AHAHAHAHAHAHAH']
def random_word() -> str:
    return choice(list_bibl_math)


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = ''
text: str = 'sorry'
MAX_COUNTER: int = 1111
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
offset: int = -2
counter: int = 0
chat_id: int

timeout: int = 60 #for long polling
def do_something() -> None:
    print('Был апдейт')
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')

start_time = time.time()

while True:
    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()  #timeout for long polling
    try:
        if updates['result']:
            cat_response = requests.get('https://api.thecatapi.com/v1/images/search')
            end_time = time.time()
            do_something()
            for result in updates['result']:
                offset = result['update_id']
                chat_id = result['message']['from']['id']
                if cat_response.status_code == 200:
                    cat_link = cat_response.json()[0]['url']
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
                else:
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
                time.sleep(1)
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={random_word()}')

        time.sleep(1)

    except Exception as ex:
        print(f'Ошибка {ex}')
    counter += 1
