import telebot
import wikipedia

bot = telebot.TeleBot('5703144320:AAG6XCmNXpzhWOUAV2csZQgp8YoTWbvQtew')
wikipedia.set_lang('uz')

description = "🇺🇸 Hello, Welcome to our wikipedia bot. Here, you can get any information which you want. You get it just through typing keyword!\n\n🇺🇿 Asslomu alekum bizning Wikipedia botimizga xush kelipsiz.Siz bu bot orqalio'zingizga kerakli bo'lgan ma'lumotni oson va tez topa olishingiz mumkin. Hammasi oddiy shunchaki kalit so'zni kiriting ma'lumotga ega bo'ling!\n\n🇷🇺 Здравствуйте, добро пожаловать в наш бот в Википедии. Здесь вы можете получить любую информацию, которую вы хотите. Вы получаете его, просто набрав ключевое слово!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, description)

@bot.message_handler(content_types=['text'])
def text(message):
    final = message.text.strip()
    try:
        mess = wikipedia.page(final).content
        if len(mess) > 4000:
            for x in range(0, len(mess), 4000):
                bot.send_message(message.chat.id, mess[x:x+4000])
        else:
            bot.send_message(message.chat.id, mess)
    except wikipedia.DisambiguationError:
        bot.send_message(message.chat.id, 'Sorry. Information too long, Please type a shorter keyword!')
    except wikipedia.PageError:
        bot.send_message(message.chat.id, 'Syntax error. Please enter correctly')


bot.polling()