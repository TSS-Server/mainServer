from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import os

TOKEN = "8829230109:AAEIdjqKWM-F25E3hjHZDUgqm0LekVP_01c"


files = os.listdir()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome!\n\nUse /list to see files\nUse /get <name> to download"
    )

async def get(update : Update , context : ContextTypes.DEFAULT_TYPE):
    with open(files[-2] , "rb") as file:
        await update.message.reply_document(
            document=file,
            filename=file.name
            caption="Here is the file"
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("get",get))
    # app.add_handler(CommandHandler("list", list_files))
    # app.add_handler(CommandHandler("get", get_file))

    # channel handler
    # app.add_handler(MessageHandler(filters.ChatType.CHANNEL, channel_post))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
