from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboard import get_keyboard_1, get_keyboard_2
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Команда для запуска бота'),
        types.BotCommand(command='/help', description='Команда для вывода помощи')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('ку!', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'бибизян')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://krots.top/uploads/posts/2022-03/1646237256_26-krot-info-p-obezyana-mem-smeshnie-foto-29.jpg', caption='ну раз бибизян так бибизян')

@dp.message_handler(lambda message: message.text ==  'дотка видик')
async def button_5_click(message: types.Message):
    await message.answer('https://www.youtube.com/watch?v=DJCbYEr9wZ4')

@dp.message_handler(lambda message: message.text == 'газилион долларов')
async def button_6_click(message: types.Message):
    await message.answer('https://www.youtube.com/watch?v=Ptb9F2KHcWo&list=PL2RiRLApO2-baS2UZQcuqY4n-fEImCg3Q')


@dp.message_handler(lambda message: message.text == 'сигма')
async def button_8_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://i.ytimg.com/vi/oTKCnr7-HDg/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgVyhIMA8=&rs=AOn4CLBfJs-qd8IkDUJFgWrasuqW-OkobQ', caption='сигма ультра скибиди туалет 1000lvl super bo$$')


@dp.message_handler(lambda message: message.text == 'xd')
async def button_8_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://avatanplus.com/files/resources/original/5da3477dca1e316dc5cf4384.png', caption='XDDDDDDDDDDDD')


@dp.message_handler(lambda message: message.text == 'мотивация')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://i.kym-cdn.com/entries/icons/original/000/043/251/cover6.jpg', caption='никогда не сдавайся!')

@dp.message_handler(lambda message: message.text == 'следующая клава')
async def button_2_click(message: types.Message):
    await message.answer("вперед!",reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'прошлая клава')
async def button_1_click(message: types.Message):
    await message.answer("обратно!", reply_markup=get_keyboard_1())

@dp.message_handler(commands= 'help')
async def start(message: types.Message):
    await message.reply('го в доту?!')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup= on_startup)

