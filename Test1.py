import telebot
from datetime import datetime
import requests
import  json

bot = telebot.TeleBot('1724637364:AAEPqLLPkSfd788vqvneH_dusnBVL5pd2mM')  # коннектимся к нашему боту
users_triggers = dict()
users_triggers[1324220572] = {
    'isAddingDeadline': False,
    'choosingWhatToDelete': False
}


@bot.message_handler(commands=['start', 'help'])  # ответ на определенный тип команд
def send_greeting(message):
    # reply_to отвечает на полученное сообщение (ну типо ссылается)
    bot.send_message(message.from_user.id, "Чо хочешь сделать?\n\n1./add_deadline - добавь дедлайн"
                                           "\n\n2./finish_deadline - закрыть дедлайн\n\n"
                                           "3./show_deadlines - чекни свои дедлайны\n\n")


@bot.message_handler(commands=['add_deadline'])
def send_deadline_request(message):
    bot.send_message(message.from_user.id, "Введи информацию о дедлайне таким образом одним сообщением:"
                                           "\nНазвание дедлайна\nОписание (можно оставить пустым)\n"
                                           "Дата окончания дедлайна (в формате дд.мм.гггг)\n"
                                           "Время в которое тебя тормошить (в формате чч:мм:сс)")
    users_triggers[message.from_user.id]['isAddingDeadline'] = True


@bot.message_handler(content_types=['text'])
def actions(message):
    if users_triggers[message.from_user.id]['isAddingDeadline']:
        bot.send_message(message.from_user.id,
                             "Ты чета не то ввел!\nРовно 4 строки одним сообщением в правильном формате плз!\n"
                             "Давай добавляй заново!")
        users_triggers[message.from_user.id]['isAddingDeadline'] = False
    elif users_triggers[message.from_user.id]['choosingWhatToDelete']:
        bot.send_message(message.from_user.id, "hgfh")
        users_triggers[message.from_user.id]['choosingWhatToDelete'] = False
    else:
        bot.send_message(message.from_user.id, "Скажи команду!\nЕсли забыл напиши /start или /help !")


bot.polling(none_stop=True)  # МУЗЫКА ГРОМЧЕ ГЛАЗА ЗАКРЫТЫ ЭТО НОН СТОП
