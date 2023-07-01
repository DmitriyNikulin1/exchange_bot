import asyncio

from aiogram import Bot, Dispatcher

from handlers import cmd_start, cmd_ans

bot = Bot(token='6017023768:AAEsRGqQLE7ppXVTKmHC7AsSkGYt3i-LDik')
dp = Dispatcher()


dp.message.register(cmd_start, commands=['start'])
dp.message.register(cmd_ans)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
