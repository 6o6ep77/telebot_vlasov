import time

import telebot

import config

# мой id: 819125846
client = telebot.TeleBot(config.telegram_token)

client.send_message(819125846, 'Hi! I\'m a Bot!')

@client.message_handler(content_types=['text'])
def get_text(message):
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    if us_name != None:
        us_full_name = str(us_name) + ' ' + str(us_sname)
    else:
        us_full_name = str(us_name)

    if 'start' in message.text.lower():
        client.send_chat_action(us_id, action='typing')
        time.sleep(0.5)
        client.send_message(message.chat.id, 'Привет, <b>' + str(us_full_name) + '</b>', parse_mode='html')
        client.send_chat_action(us_id, action='typing')
        time.sleep(0.5)
        client.send_message(message.chat.id, 'Твой id уз telegram: <b>' + str(us_id) + '</b>', parse_mode='html')
        return

    if 'авария' in message.text.lower():
        user_list = ['819125846', '1681082510', '819125847']
        for user_el in config.user_list:
            try:
                client.send_chat_action(us_id, action='typing')
                time.sleep(0.5)
                client.send_message(user_el,
                                    'Получено сообщение о возможной аварии \n'
                                    'Об аварии сообщил <b>' + str(us_full_name) + '</b>',
                                    parse_mode='html')
            except Exception as er_user:
                client.send_message(message.chat.id, 'Ошибка оповещения пользователя ' + str(user_el))

        client.send_message(message.chat.id, 'Я всех оповестил! 🫥')


    # код, который вызывает ошибку
    if 'test' in message.text.lower():
        client.send_chat_action(us_id, action='typing')
        time.sleep(0.5)
        client.send_message(message.chat.id, str(test))
        return

while True:
    try:
        client.polling(non_stop=True, interval = 0)
    except Exception as e:
        print('Ошибка в работе бота ' + str(e))