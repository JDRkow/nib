import telebot

bot = telebot.TeleBot('1116351784:AAEAVfFfr-Hg3V_2E4xO75-Wuc6R8y0CZsE')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()