import requests
from fake_headers import Headers
from bs4 import BeautifulSoup as bs4
from random import randint


import prettytable as pt

import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified
from aiogram.utils.callback_data import CallbackData
from os import getenv
from sys import exit
from random import randint
from contextlib import suppress
from telegram import ParseMode


# Токен берётся из переменной окружения
token = "1751490595:AAFmANWqMy6o21HOtmrFVweSPzpE8fxtKew"
if not token:
    exit("Error: no token provided")

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)





user_data = {}

# ----------

def get_data_from_cgs_api():
	numr =  randint(randint(0,11),11)
	r = requests.get('https://www.customgamestats.com/custom-games/GetGameStats').json()[:20]
	return r
def get_all_types(Bdict):
	temp_list = []
	for i in Bdict[0]:
		temp_list.append(i)
	return temp_list
def data_convert_to_normal(Bdict,type_i):
	print(type_i)
	table = pt.PrettyTable(['номер','название', type_i.replace("_"," ")])
	table.align['номер'] = 'r'
	table.align['название'] = 'l'
	table.align[type_i.replace("_"," ")] = 'r'

	for num,i in enumerate(Bdict,start=1):
		type_i_num = i[type_i]
		title = i["title"]
		table.add_row([f'{num}',title, type_i_num])
	return table

def edit_data_from_cgs_json(data,type_s=None):
	player_count = sorted(data, key=lambda dataL: dataL[type_s],reverse=True)
	return player_count

# ----------
# Это вариант с фабрикой колбэков

# fabnum - префикс, action - название аргумента, которым будем передавать значение
callback_numbers = CallbackData("fabnum", "action")


def get_keyboard_fab():
	data = get_all_types(get_data_from_cgs_api())
	buttons = []
	for i in data:
		buttons.append(types.InlineKeyboardButton(text="sort "+i.replace("_"," "), callback_data=callback_numbers.new(action=i)))
	keyboard = types.InlineKeyboardMarkup(row_width=2)
	keyboard.add(*buttons)
	return keyboard


async def update_num_text_fab(message: types.Message, new_value: int):
    with suppress(MessageNotModified):
        await message.edit_text(f"{new_value}", reply_markup=get_keyboard_fab(), parse_mode=ParseMode.HTML)


@dp.message_handler(commands="numbers_fab")
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard_fab())


@dp.callback_query_handler(callback_numbers.filter())
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    user_value = user_data.get(call.from_user.id, 0)
    action = callback_data["action"]
    data = get_all_types(get_data_from_cgs_api())
    if action in  data:
    	edata = edit_data_from_cgs_json(get_data_from_cgs_api(),type_s=action)
    	await update_num_text_fab(call.message, f"<pre>{data_convert_to_normal(edata,action)}</pre>")
    await call.answer()



# --------------------

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)