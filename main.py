from aiogram.utils import executor
from config import dp, bot, ADMINS
import logging

from handlers import client
from handlers import callback
from handlers import admin
from handlers import fsmadmin
from handlers import schedule

# from handlers import extra
fsmadmin.register_handlers_fsm(dp)
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
callback.register_handler_callback(dp)


async def on_startup(dp):
    await bot.send_message(ADMINS[0], "Я родился!")


async def on_shutdown(dp):
    await bot.send_message(ADMINS[0], "Пока пока!")


# extra.register_handler_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
