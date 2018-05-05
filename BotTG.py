import telebot
from datetime import datetime
from telebot import types

token = '569481488:AAFEuJuynoOvJPB6aznybtW_KCeO9DctWas'

bot = telebot.TeleBot(token)

def getTimeNow():
    return datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')

def writeToLog(who,text):
    file = open('log.txt','a+',encoding = 'utf-8')
    file.write(getTimeNow() + ' ' + str(who) + ' ' + str(text) + '\n')
    file.close()

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')
    writeToLog(message.from_user.id, 'Пользователь начал использовать бота')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    
    wordButton = types.KeyboardButton('Узнать значение слова')
    keyboard.add(wordButton)
    
    translateButton = types.KeyboardButton('Перевести слово')
    keyboard.add(translateButton)
    
    weatherButton = types.KeyboardButton('Узнать погоду')
    keyboard.add(weatherButton)
    
    kursButton = types.KeyboardButton('Курс валют')
    keyboard.add(kursButton)

    bot.send_message(message.chat.id, 'Выбери вариант: ', reply_markup = keyboard)
    bot.register_next_step_handler(message, choiseUser)

def choiseUser(message):
    if message.text == 'Узнать слово':
        writeToLog(message.from_user.id, 'Пользователь выбрал "Узнать слово"')
        bot.send_message(message.from_user.id, 'Введите слово: ')
        bot.register_next_step_handler(message, search_word)
        
try:
    bot.polling(none_stop = True)
except:
    writeToLog('','Ошибка запуска')
