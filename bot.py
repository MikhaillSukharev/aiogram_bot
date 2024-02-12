import logging
import aiogram
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from config import DEBUG, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_PORT, WEBAPP_HOST
from loader import dp


async def on_startup(dispatcher: aiogram.Dispatcher):
    import handlers
    logger = logging.getLogger("aiogram")
    logger.info(f"Handlers {handlers} loaded for {dispatcher}")


async def start_webhook(dispatcher: aiogram.Dispatcher):
    dispatcher.middleware.setup(LoggingMiddleware())
    await dispatcher.bot.set_webhook(WEBHOOK_URL)
    await on_startup(dispatcher=dispatcher)


async def stop_webhook(dispatcher: aiogram.Dispatcher):
    await dispatcher.bot.delete_webhook()


if __name__ == "__main__":
    logging.basicConfig(level=DEBUG)
    if DEBUG:
        aiogram.executor.start_polling(
            dispatcher=dp,
            on_startup=on_startup
        )
    else:
        aiogram.executor.set_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            on_startup=start_webhook,
            on_shutdown=stop_webhook,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT
        )
