from aiogram.types import BotCommand

commands_admin = [
    BotCommand(
        command='start',
        description='Start/restart bot'
    ),
    BotCommand(
        command='new_category',
        description='add new category to store'
    ),
    BotCommand(
        command='new_product',
        description='add new product to store'
    ),
    BotCommand(
        command='edit_category',
        description='edit category infarmations'
    ),
    BotCommand(
        command='edit_product',
        description='edit product infarmations'
    ),
    BotCommand(
        command='del_category',
        description='delete category'
    ),
    BotCommand(
        command='del_product',
        description='delete product'
    ),
    BotCommand(
        command='categories',
        description='categories list (with pagination)'
    ),
    BotCommand(
        command='products',
        description='products list (with pagination)'
    ),
    BotCommand(
        command='ads',
        description='ads list (with pagination)'
    ),
    BotCommand(
        command='new_ad',
        description='add new ad to store'
    ),
    BotCommand(
        command='edit_ad',
        description='edit ad infarmations'
    ),
    BotCommand(
        command='del_ad',
        description='delete ad'
    ),
    BotCommand(
        command='users',
        description='all bot users list'
    ),
]

commands_user = [
    BotCommand(
        command='start',
        description='Start/restart bot'
    ),
    BotCommand(
        command='help',
        description='????'
    ),
    BotCommand(
        command='ads',
        description='ads list (with pagination)'
    ),
    BotCommand(
        command='new_ad',
        description='add new ad to store'
    ),
    BotCommand(
        command='edit_ad',
        description='edit ad infarmations'
    ),
    BotCommand(
        command='del_ad',
        description='delete ad'
    )
]