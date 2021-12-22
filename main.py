import telebot
from telebot import types
import random

bot = telebot.TeleBot('5050440661:AAGsAgrS4MQOMWpnDcWJeXEDe_FWGdGLq-g')
stikers = ['🤨','🤑','🥶','😎','🦛','🐿','🐊','🕷']
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row( "/help",'/stiker','/timetable','youtube',"МТУСИ",'почта','инста')
    bot.send_message(message.chat.id, 'Здравствуй, {0.first_name}\n Хочешь узнать свежую информацию о МТУСИ? '
                                      'Если нет, то нажми Help и увидишь, что я еще могу.'.format(message.from_user),parse_mode='html', reply_markup=keyboard)

@bot.message_handler(commands=['stiker'])
def stiker(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("/start", '/help','/timetable','youtube','МТУСИ','почта','инста')
    rand = random.randint(0,8)
    bot.send_message(message.chat.id,stikers[rand], reply_markup=keyboard)

@bot.message_handler(commands = ['timetable'])
def timetable(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("/start", '/help','/stiker', 'youtube', 'МТУСИ', 'почта', 'инста')
    doc = open('tmp/timetable.xls','rb')
    bot.send_document(message.chat.id, doc)

@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("/start", '/stiker','/timetable','youtube','МТУСИ','почта','инста')
    bot.send_message(message.chat.id, 'Я умею выдавать свежую информацию о МТУСИ (МТУСИ); '
                                      'Выводить рандомный стикер(/stiker); Прислать расписание занятий по команде /timetable; Открывать Youtube (youtube), Mail(почта), Instagram(инста); ', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def youtube(message):
    if message.text.lower() == "youtube":
        bot.send_message(message.chat.id, 'Переходи по ссылке – https://www.youtube.com/')
    elif message.text.lower() == "МТУСИ":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "почта":
        bot.send_message(message.chat.id, 'Переходи – https://mail.ru/')
    elif message.text.lower() == "инста":
        bot.send_message(message.chat.id, 'Нажимай – https://www.instagram.com/')




if __name__ == '__main__':
    while True:
        try:
            bot.polling(non_stop=True)
        except Exception as e:
            print(e)