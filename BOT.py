from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time
# login, password = "login", "password"
# vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
# vk_session.auth(token_only=True)

token = "cf1c5235064c9be2c89ed8dfb28f7e1b9092c2aebac26f45d6c8d8d1991ad0c7dd7da71d93bb8c210b60c"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет. Это мой бот, надеюсь тебе понравится!', 'random_id': 0})
                elif response == "хентай":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Хентай для тебя!', 'random_id': 0})
                elif response == "косплей":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Косплей для тебя!', 'random_id': 0})
                elif response == "манга":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Манга для тебя!', 'random_id': 0})
                elif response == "видео":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Видео для тебя!', 'random_id': 0})
                elif response == "гиф":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Гиф для тебя!', 'random_id': 0})
                elif response == "больше видео":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Больше Видео для тебя!', 'random_id': 0})