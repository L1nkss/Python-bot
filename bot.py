import logging
import os
from tokenize import String
from turtle import st, up

from dotenv import load_dotenv
from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler


icon_dict = {
    "box": "📦",
    "dick": "🍆",
    "empty": "💨",
    "super_dick": "🍌"
}

load_dotenv()
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def dick(update: Update, content: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton(icon_dict["box"], callback_data=icon_dict["dick"]),
            InlineKeyboardButton(icon_dict["box"], callback_data=icon_dict["dick"]),
            InlineKeyboardButton(icon_dict["box"], callback_data=icon_dict["dick"])
        ],
        [
            InlineKeyboardButton(icon_dict["box"], callback_data=icon_dict["dick"]),
            InlineKeyboardButton(icon_dict["box"], callback_data=icon_dict["dick"]),
            InlineKeyboardButton(icon_dict["box"], callback_data=icon_dict["dick"]),
        ],
        [
            InlineKeyboardButton(icon_dict["box"], callback_data=icon_dict["dick"]),
            InlineKeyboardButton(icon_dict["box"], callback_data=icon_dict["dick"]),
            InlineKeyboardButton(icon_dict["box"], callback_data=icon_dict["empty"]),
        ],
        [
            InlineKeyboardButton("Закончить игру", callback_data="finish"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.effective_chat.send_message(text="Угадайте, в какой коробке хуй.\n", reply_markup=reply_markup)


async def button_handler(update: Update, content: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    text: str = f"{query.from_user.first_name}: {query.data} {'нашёл(ла) член' if query.data == icon_dict['dick'] else 'открыл(а) пустую коробку'}"

    updated_text = f"{query.message.text}\n \n{text}"

    await query.edit_message_text(text=updated_text, reply_markup=query.message.reply_markup)


async def message_handler(update: Update, content: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.effective_message)


def main() -> None:
    """Start the bot"""
    # Create the Application
    application = ApplicationBuilder().token(os.environ['bot_token']).build()
    
    application.add_handler(CommandHandler("dick", dick))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.CHAT, message_handler))

    #Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()