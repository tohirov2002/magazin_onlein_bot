
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from config import DB_NAME,admins
from utils.my_commands import commands_admin,commands_user
from utils.database import Database

from states.admin_states import CategoryStates
from keyboards.admin_inline_keyboards import make_category_list
from states.admin_states import ProductStates

comamands_router = Router()

db = Database(DB_NAME)


@comamands_router.message(CommandStart())
async def start_handlers(message: Message):
    if message.from_user.id in admins:
        await message.bot.set_my_commands(commands_admin)
        await message.answer("Welcome admin, please choose command from commands list")
    else:
        await message.bot.set_my_commands(commands_user)
        await message.answer("let's start registration")


@comamands_router.message(Command('new_category'))
async def new_category_handler(message: Message, state: FSMContext):
    await state.set_state(CategoryStates.newCategory_state)
    await message.answer("Please, send new category name...")


@comamands_router.message(Command('cancel'))
async def cancel_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("All actions canceled , you may continue sending commands")


@comamands_router.message(Command('edit_category'))
async def edit_category_handler(message: Message, state: FSMContext):
    await state.set_state(CategoryStates.updCategory_state_list)
    await message.answer(
        text="Choose category name which you want to change...",
        reply_markup=make_category_list()
    )


@comamands_router.callback_query(CategoryStates.updCategory_state_list)
async def callback_category_edit(callback: CallbackQuery, state: FSMContext):
    await state.update_data(cat_name=callback.data)
    await state.set_state(CategoryStates.updCategory_state_new)
    await callback.message.answer(f"Please, send new name for category {callback.data}")
    await callback.message.delete()


@comamands_router.message(CategoryStates.updCategory_state_new)
async def set_new_category_name(message: Message, state: FSMContext):
    new_cat = message.text
    st_data = await state.get_data()
    old_cat = st_data.get('cat_name')
    res = db.upd_category(message.text,old_cat)
    if res['status']:
        await message.answer("Category name successfully change")
        await state.clear()
    elif res['desc'] == 'exists':
        await message.reply("This category already exists. \n"
                            "Please, send other name or click /cancel")
    else:
        await message.reply(res['desc'])


@comamands_router.message(Command('del_category'))
async def del_category_handler(message: Message, state: FSMContext):
    await state.set_state(CategoryStates.delCategory_state)
    await message.answer(
        text="To delete a category, select a category:",
        reply_markup=make_category_list()
    )



# @comamands_router.callback_query(CategoryStates.delCategory_state)
# async def callback_category_del(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     await callback.message.answer("Categoriyani o'chirishni rostan amalga oshirmoqchimisiz? \n"
#                                   "Agar ha bo'lsa, 'Ha' tugmasini bosing. Aks holda, 'Yo'q' tugmasini bosing.")
#     response = await state.get()
#     if response.text.lower() == 'ha':
#         try:
#             if db.del_category(cat_name=callback.data):
#                 await state.clear()
#                 await callback.message.edit_text(f"Category with name '{callback.data}' successfully deleted")
#             else:
#                 await callback.message.answer(f"Could not delete the category. Please try again!")
#         except Exception as e:
#             await callback.message.answer(f"An error occurred: {str(e)}. Please try again!")
#     elif response.text.lower() == 'yo\'q':
#         await callback.message.answer("Categoriyani o'chirish bekor qilindi.")
#     else:
#         await callback.message.answer("Noto'g'ri javob. Iltimos, 'Ha' yoki 'Yo'q' tanlang.")


@comamands_router.callback_query(CategoryStates.delCategory_state)
async def callback_category_del(callback: CallbackQuery, state: FSMContext):
    if db.del_category(cat_name=callback.data):
        await state.clear()
        await callback.message.edit_text(f"Category with name '{callback.data}' successfully deleted")
    else:
        await callback.message.answer(f"Could not delete the category. Please try again!")


@comamands_router.message(Command('categories'))
async def categories_list_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Categories list",
        reply_markup=make_category_list()
    )


@comamands_router.message(Command('new_product'))
async def new_product_handler(message: Message, state: FSMContext):
    await state.set_state(ProductStates.newProduct_state)
    await message.answer("Pleas, send new Product name....")