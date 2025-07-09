from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, ApplicationBuilder

import os 
from dotenv import load_dotenv

from openrouter import chat_ia 

load_dotenv()
token_telegram = os.getenv("TELEGRAM_TOKEN")

def inicio_bot():
    app = ApplicationBuilder().token(token_telegram).build()
    
    app.add_handler(CommandHandler("start", start))  
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_ia))

    app.run_polling()
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou o Lm Bot😎") 