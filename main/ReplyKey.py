from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
baholash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⭐️⭐️⭐️⭐️⭐️ | A'lo")
        ],
        [
            KeyboardButton(text="⭐️⭐️⭐️⭐️ | Yaxshi")
        ],
        [
            KeyboardButton(text="⭐️⭐️⭐️ | O'rtacha")
        ],
        [
            KeyboardButton(text="⭐️⭐️ | Qoniqarli")
        ],
        [
            KeyboardButton(text="⭐️ | Qoniqarsiz")
        ]
    ],
    resize_keyboard=True
)
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menu")
        ]
    ],
    resize_keyboard=True
)
