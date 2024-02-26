from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

from utils.database import Database
from config import DB_NAME
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

db = Database(DB_NAME)

def get_category_list() -> InlineKeyboardMarkup:
    categories = db.get_categories()
    rows = []
    for category in categories:
        rows.append([
            InlineKeyboardButton(
                text=str(category[1]),
                callback_data=str(category[0])
            )
        ])
    kb_categories = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb_categories

def get_product_list(cat_id: int) -> InlineKeyboardMarkup:
    products = db.get_products(cat_id)
    rows = []
    for product in products:
        rows.append([
            InlineKeyboardButton(
                text=str(product[1]),
                callback_data=str(product[1])
            )
        ])
    kb_products = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb_products
