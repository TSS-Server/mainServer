import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = "8829230109:AAEIdjqKWM-F25E3hjHZDUgqm0LekVP_01c"

# It is safer to list files inside the function so it reads the folder in real-time
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome!\n\nUse /get to download the file."
    )

async def get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    files = os.listdir()
    
    # Filter out script files so you don't accidentally send your code/token
    valid_files = [f for f in files if os.path.isfile(f) and not f.endswith('.py')]
    
    if not valid_files:
        await update.message.reply_text("No files available for download.")
        return

    # Using the first valid file found safely
    target_file = valid_files[0] 

    with open(target_file, "rb") as file:
        await update.message.reply_document(
            document=file,
            filename=os.path.basename(file.name),
            caption="Here is the file!"  # Added the missing comma right above this line
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("get", get))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
