import asyncio
from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Открыть Hamster Wallet', web_app=WebAppInfo(
            url="https://68bc-85-174-200-178.ngrok-free.app"
        )
    )
    return builder.as_markup()

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply('Добро пожаловать в Hamster Wallet!', reply_markup=webapp_builder())

async def main() -> None:
    bot = Bot("6966485199:AAFJTOi4xfR4QwFnjA5Xq-vLKUogddji5Pg")
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())