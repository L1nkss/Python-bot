import logging
import os

from dotenv import load_dotenv
from telegram import Update, ForceReply
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def dick(update: Update, content: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_chat.send_message(
        f"Угадайте, в какой коробке хуй.",
        parse_mode=ParseMode.HTML,
    )

async def message_handler(update: Update, content: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.effective_message)


def main() -> None:
    """Start the bot"""
    # Create the Application
    application = ApplicationBuilder().token(os.environ['bot_token']).build()
    
    application.add_handler(CommandHandler("dick", dick))
    application.add_handler(MessageHandler(filters.CHAT, message_handler))

    #Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()