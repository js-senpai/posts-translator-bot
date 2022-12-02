from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
# Get ENV
from config import BaseConfig
from services import post_service

get_config = BaseConfig()

# Initialize bot
bot = Bot(token=get_config.TELEGRAM_API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.channel_post_handler()
async def post_handler(msg: types.Message):
    try:
        await post_service(bot,msg)
    except Exception as e:
        print(f'Error in post handler method. {e}')

@dp.message_handler()
async def message_handler(msg: types.Message):
    try:
        await post_service(bot, msg)
    except Exception as e:
        print(f'Error in message handler method. {e}')


# Start bot
if __name__ == '__main__':
    executor.start_polling(dp)