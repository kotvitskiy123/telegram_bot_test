import telebot

bot = telebot.TeleBot('951435140:AAHDranoTsZgmLXVjXc4g_9KKtTf3kzhOf8')


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row("Hi", "Goodbye")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi, you write me /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text.lower() == "hi":
		bot.send_message(message.chat.id, 'Hi, my creator')
	elif message.text.lower() == "goodbye":
		bot.send_message(message.chat.id, 'Goodbye, my creator')
	elif message.text.lower() == "i love you":
		bot.send_sticker(message.chat.id, "CAACAgQAAxkBAAMPXnTEs6dReKhwUYjrr5sGLw0d2CsAAnAAA845CA2TCQABvTArn9sYBA")


@bot.message_handler(content_types=['sticker'])
def print_id_sticker(message):
	print(message)



bot.polling()



