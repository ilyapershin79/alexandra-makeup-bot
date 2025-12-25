import logging
from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)
from aiogram.filters import Command

from app.core.config import BOT_TOKEN, BACKEND_URL

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# ====== КНОПКИ С MINI APP ======

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="✨ Мои курсы",
                web_app=WebAppInfo(url=f"{BACKEND_URL}/")
            ),
            KeyboardButton(
                text="📅 Мои услуги",
                web_app=WebAppInfo(url=f"{BACKEND_URL}/")
            )
        ],
        [
            KeyboardButton(
                text="🎁 Розыгрыши",
                web_app=WebAppInfo(url=f"{BACKEND_URL}/")
            ),
            KeyboardButton(
                text="👩‍🎨 Обо мне",
                web_app=WebAppInfo(url=f"{BACKEND_URL}/")
            )
        ],
        [
            KeyboardButton(
                text="💎 Личный кабинет",
                web_app=WebAppInfo(url=f"{BACKEND_URL}/")
            )
        ]
    ],
    resize_keyboard=True
)


# ====== /start ======

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет! Я бот визажиста Александры 💄\n\n"
        "Выбирай интересующий раздел 👇",
        reply_markup=main_keyboard
    )


if __name__ == "__main__":
    dp.run_polling(bot)
