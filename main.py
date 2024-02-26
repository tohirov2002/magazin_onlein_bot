
import logging
import asyncio
from handlers.admin_msg_handlers import admin_message_router
from aiogram import Bot,Dispatcher
from aiogram.enums import ParseMode
from handlers.commands_handlers import comamands_router
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN
from handlers.client_ads_handlers import ads_router

async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode='HTML',
            link_preview_is_disabled=True
        )
    )
    db = Dispatcher()
    db.include_routers(comamands_router,admin_message_router,ads_router)
    await db.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")