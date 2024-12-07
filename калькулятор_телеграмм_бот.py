import telebot
import numexpr

TOKEN = '7326919610:AAE5YD1jIiiYRoiEIVS5sFwJcGEqeLBRIGk'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я калькулятор! Введите выражение, и я его вычислю.')


@bot.message_handler(func=lambda message: True)
def calculate(message):
    text = message.text
    chat_id = message.chat.id
    try:
        result = numexpr.evaluate(text)
        bot.send_message(chat_id, str(result))
    except (SyntaxError, NameError, TypeError, ValueError) as e:
        bot.send_message(chat_id, f"Ошибка: {e}. Пожалуйста, проверьте выражение.")
    except Exception as e:
        bot.send_message(chat_id, f"Произошла неизвестная ошибка: {type(e).__name__}")

