# - *- coding: utf- 8 - *-

import telebot
import config
from telebot import types
from get_info import get_data_airpods, get_data_iphone_12, get_data_iphone_13

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        'Спрашивай или проваливай'
    )


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(
        message.chat.id,
        'Нажми на /button'
    )


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Наушники")
    item2 = types.KeyboardButton("Айфон 12")
    item3 = types.KeyboardButton('Айфон 13')
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id, 'Выбери что надо', reply_markup=markup)


# Кнопки с цветами Айфонов 12
inline_bt_black = types.InlineKeyboardButton('Black', callback_data='btn001')
inline_bt_white = types.InlineKeyboardButton('White', callback_data='btn002')
inline_bt_blue = types.InlineKeyboardButton('Blue', callback_data='btn003')
inline_bt_green = types.InlineKeyboardButton('Green', callback_data='btn004')
inline_bt_red = types.InlineKeyboardButton('(Product) RED', callback_data='btn005')
inline_bt_purple = types.InlineKeyboardButton('Purple', callback_data='btn006')
inline_kb_color_12 = types.InlineKeyboardMarkup(row_width=2)
inline_kb_color_12.add(inline_bt_black, inline_bt_white,
                       inline_bt_blue, inline_bt_green,
                       inline_bt_red, inline_bt_purple)

# Кнопки с цветами Айфонов 13
inline_bt_pink_13 = types.InlineKeyboardButton('Pink', callback_data='btn007')
inline_bt_blue_13 = types.InlineKeyboardButton('Blue', callback_data='btn008')
inline_bt_midnight_13 = types.InlineKeyboardButton('Midnight', callback_data='btn009')
inline_bt_red_13 = types.InlineKeyboardButton('(Product) RED', callback_data='btn010')
inline_bt_starlight_13 = types.InlineKeyboardButton('Starlight', callback_data='btn011')
inline_bt_green_13 = types.InlineKeyboardButton('Green', callback_data='btn012')
inline_kb_color_13 = types.InlineKeyboardMarkup(row_width=2)
inline_kb_color_13.add(inline_bt_midnight_13, inline_bt_starlight_13,
                       inline_bt_green_13, inline_bt_pink_13,
                       inline_bt_blue_13, inline_bt_red_13)


# Диалог
@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Наушники":
        bot.send_message(message.chat.id, get_data_airpods())
    if message.text == 'Пока':
        bot.send_message(message.chat.id, 'Проваливай')
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Спрашивай или проваливай')
    if message.text == 'Айфон 12':
        bot.send_message(message.chat.id, 'Выбери цвет:', reply_markup=inline_kb_color_12)
    if message.text == 'Айфон 13':
        bot.send_message(message.chat.id, 'Выбери цвет:', reply_markup=inline_kb_color_13)


# Возрврашение парсинга с выбранным цветом
@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('btn'))
def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-3:]
    bot.send_message(callback_query.from_user.id, 'Смотри что есть:')
    # Айфоны 12
    if code == '001':
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, get_data_iphone_12('Black'))
    elif code == '002':
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, get_data_iphone_12('White'))
    elif code == '003':
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, get_data_iphone_12('Blue'))
    elif code == '004':
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, get_data_iphone_12('Green'))
    elif code == '005':
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, get_data_iphone_12('(PRODUCT) RED'))
    elif code == '006':
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, get_data_iphone_12('Purple'))
    # Айфоны 13
    elif code == '007':
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, get_data_iphone_13('Pink'))
    elif code == '008':
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, get_data_iphone_13('Blue'))
    elif code == '009':
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, get_data_iphone_13('Midnight'))
    elif code == '010':
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, get_data_iphone_13('(PRODUCT)RED'))
    elif code == '011':
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, get_data_iphone_13('Starlight'))
    elif code == '012':
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, get_data_iphone_13('Green'))
    else:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Упс...')


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
