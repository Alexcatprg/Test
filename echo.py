import telebot
from telebot import types

bot = telebot.TeleBot('5228285733:AAGxFRqodffVosgxhzvL-931iUutnanNt5w')

@bot.message_handler(commands=['start'])
def start(message):
	mess=f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
	bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
	if message.text == "Hello" or message.text == "Привет":
		bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
	elif message.text == "My id" or message.text == "Мой идентификатор":
		bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
	elif message.text == "Фото" or message.text == "Photo":
		photo = open('Iphone.png', 'rb')
		bot.send_photo(message.chat.id, photo)	
	else:
		bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
	bot.send_message(message.chat.id, "Вау, крутое фото!")

@bot.message_handler(commands=['канал Ютубе'])	
def website(message):
	markup=types.ReplyKeyboardMarkup()
	markup.add(types.InLineKeyboardButton("Перейти на Ютуб канал", url="https://www.youtube.com/channel/UCbEXMidfQsJvX3KFkkhyqkw"))
	bot.send_message(message.chat.id, 'Лови ссылку на Ютуб канал', reply_markup=markup)


bot.polling(none_stop=True)
