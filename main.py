from aiogram import Bot, Dispatcher, executor, types

import Coins
import Keyboards as kb

bot = Bot('2007889284:AAHEyF5naTazhwdkTW-PiX7LAevQ8rBiLks')
dp = Dispatcher(bot)

CoinSending = {}

@dp.callback_query_handler(lambda c: c.data.startswith('alert'))
async def Menu(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    data = callback_query.data
    code = data.split()[-1]
    if code == 'value':
        await bot.send_message(callback_query.from_user.id, f'Текущая стоимость {await Coins.GetPrice()} \nУкажите ниже какой стоимости нужно присылать уведомление \nПример: /alert [стоимость]')
    elif code == 'min':
            if CoinSending.get(callback_query.from_user.id) == None:
                send = Coins.Sending(bot, callback_query.from_user.id, 5)
                CoinSending[callback_query.from_user.id] = send
                await send.Start()
                await bot.send_message(callback_query.from_user.id, f'Вы успешно подписались на рассылку \nТекущая стоимость {await Coins.GetPrice()}')
            else:
                await bot.send_message(callback_query.from_user.id, f'Вы уже подписаны на рассылку')

@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} \nВыберите условие уведомления: ', parse_mode='Markdown', reply_markup=kb.MainMenu)

@dp.message_handler(commands=['stop'])
async def stop(message):
    send = CoinSending[message.chat.id]
    await send.Stop()
    CoinSending[message.chat.id] = None
    await bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}\n'
                                            'Вы отписались от рассылки',)

@dp.message_handler(commands=['alert'])
async def send_welcome(message):
    if CoinSending.get(message.chat.id) == None:
        value = float(message.text.split()[-1])
        if value > 0:
            send = Coins.Sending(bot, message.chat.id, 5, value)
        else:
            await bot.send_message(message.chat.id, f'Стоимость не может быть ниже 0')
            return
        CoinSending[message.chat.id] = send
        await send.Start()
        await bot.send_message(message.chat.id,
                           f'Вы успешно подписались на рассылку \nТекущая стоимость {await Coins.GetPrice()} \nВы указали стоимость {value}')
    else:
        await bot.send_message(message.chat.id, f'Вы уже подписаны на рассылку')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)