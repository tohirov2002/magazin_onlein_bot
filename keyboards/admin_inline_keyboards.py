from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

from utils.database import Database
from config import DB_NAME
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

db = Database(DB_NAME)

def make_category_list() -> InlineKeyboardMarkup:
    categories = db.get_categories()
    rows = []
    for category in categories:
        rows.append([
            InlineKeyboardButton(
                text=str(category[1]),
                callback_data=str(category[1])
            )
        ])
    kb_categories = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb_categories


cancel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="cancel")]
],
    resize_keyboard=True,
    input_field_placeholder="if you cancel,touch the 'cancel' button"
)

yes_or_no = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ha', callback_data="yes"), InlineKeyboardButton(text="Yo'q", callback_data="no")]
    ]
)