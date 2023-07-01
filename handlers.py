from aiogram import types
import requests


async def cmd_start(message: types.Message):
    await message.answer('Введите количество долларов которые хотите конвертировать')


async def cmd_ans(message: types.Message):
    if '1' in message.text or '2' in message.text or '3' in message.text or '4' in message.text or '5' in message.text or '6' in message.text or '7' in message.text or '8' in message.text or '9' in message.text:
        amount = message.text
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"

        payload = {}
        headers = {
            "apikey": "M3JCLoN233UnXzGTafTR6mmn8YpvBCYI"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()

        await message.answer(result["result"])
