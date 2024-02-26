
from aiogram.fsm.context import FSMContext
from aiogram import F,Router
from aiogram.types import Message, ReplyKeyboardRemove

from states.admin_states import CategoryStates
from aiogram.types import CallbackQuery
from states.admin_states import ProductStates
from utils.database import Database
from config import DB_NAME
from keyboards.admin_inline_keyboards import cancel, yes_or_no

admin_message_router = Router()

db = Database(DB_NAME)


@admin_message_router.message(CategoryStates.newCategory_state)
async def new_category_handlers(message: Message, state: FSMContext):
    res = db.add_category(message.text)
    if res['status']:
        await message.answer("New category successfully added")
        await state.clear()
    elif res['desc'] == 'exists':
        await message.reply("This category already exists. \n"
                            "Please, send other name or click /cancel")
    else:
        await message.reply(res['desc'])



@admin_message_router.message(ProductStates.newProduct_state)
async def product_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text="Please send product photo", reply_markup=cancel)
    await state.set_state(ProductStates.add_product_img)

@admin_message_router.message(ProductStates.add_product_img)
async def add_img(message: Message, state: FSMContext):
    if message.text != "cancel":
        try:
            await state.update_data(img_url=message.photo[-1].file_id)
            await message.answer(text="Please send product category",reply_markup=cancel)
            await state.set_state(ProductStates.add_product_category)
        except:
            await message.answer(text="send me only photo")
    else:
        await state.clear()
        await message.answer(text="Canceled",reply_markup=ReplyKeyboardRemove())


@admin_message_router.message(ProductStates.add_product_category)
async def add_category(message: Message,state: FSMContext):
    if message.text != "cancel":
        if db.get_categorie(message.text):
            await state.update_data(category=message.text)
            data = await state.get_data()
            info = f"Product information:\n\n\tProduct name: {data.get('name')}\nProduct category: {data.get('category')}"
            await message.answer_photo(photo=data.get("img_url"),caption=info,reply_markup=yes_or_no)
            await state.set_state(ProductStates.newProduct_state)
        else:
            await message.answer(text="This category did not found")
    else:
        await state.clear()
        await message.answer(text="Canceled",reply_markup=ReplyKeyboardRemove())


@admin_message_router.callback_query(ProductStates.newProduct_state)
async def add_product(query: CallbackQuery,state: FSMContext):
    if query.data == "yes":
        data = await state.get_data()
        if db.add_product(name=data.get("name"),image=data.get("img_url"),category_name=data.get("category")):
            await query.message.delete()
            await query.answer(text="Product saved")
            await query.message.answer(text="Product saved")
            await query.message.answer("Menu")
            await state.clear()
        else:
            await query.message.delete()
            await query.answer(text="Unknown error")
            await query.message.answer("Menu")
    else:
        await query.message.delete()
        await query.answer(text="canceled")
        await query.message.answer("Menu")

