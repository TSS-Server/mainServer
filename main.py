import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = "8829230109:AAHfAzHLMl1dNYAlajNIOdncnw7eZ7s1Uyg"

# It is safer to list files inside the function so it reads the folder in real-time
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome!\n\nUse /get to download the file."
    )

async def get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    files = os.listdir()
    
    if not context.args:
        await update.message.reply_text("Provide an attribute such as '/get 2026-x-x'")
    print(context.args)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("get", get))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
