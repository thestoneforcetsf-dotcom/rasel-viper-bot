import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "আসসালামু আলাইকুম!\n"
        "আমি Rasel Viper 🤖\n"
        "একটি বাংলা AI সহকারী।"
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("আমি উত্তর দেওয়ার চেষ্টা করছি 😊")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
