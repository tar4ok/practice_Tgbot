from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('бибизян')
    button_2 = KeyboardButton('следующая клава')
    button_5 = KeyboardButton('дотка видик')
    button_6 = KeyboardButton('газилион долларов')
    keyboard.add(button_1, button_2, button_5, button_6)
    return keyboard


def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_3 = KeyboardButton('мотивация')
    button_4 = KeyboardButton('прошлая клава')
    button_7 = KeyboardButton('сигма')
    button_8 = KeyboardButton('xd')
    keyboard_2.add(button_3, button_4, button_7, button_8)
    return keyboard_2
