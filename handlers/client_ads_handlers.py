
from aiogram.fsm.context import FSMContext
from aiogram import F,Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart,Command

from states.admin_states import CategoryStates
from aiogram.types import CallbackQuery
from states.admin_states import ProductStates
from utils.database import Database
from config import DB_NAME
from states.client_states import ClientAdsStates
from keyboards.client_inline_keyboards import get_category_list,get_product_list

ads_router = Router()
db = Database(DB_NAME)

@ads_router.message(Command('new_ad'))
async def new_ad_handler(message: Message, state: FSMContext):
    await state.set_state(ClientAdsStates.selectAdCategory)
    await message.answer(
        text="Please, choose a category for your ad:",
        reply_markup=get_category_list()
    )


@ads_router.callback_query(ClientAdsStates.selectAdCategory)
async def get_category_product(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Please, choose a product type for your ad",
        reply_markup=get_product_list(int(callback.data))
    )





