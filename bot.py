from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, ApplicationBuilder
import requests
import os 
from dotenv import load_dotenv

load_dotenv()
token_openrouter = os.getenv("OPENROUTER_KEY")
token_telegram = os.getenv("TELEGRAM_TOKEN")

def inicio_bot():
    app = ApplicationBuilder().token(token_telegram).build()
    
    app.add_handler(CommandHandler("start", start))  
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_ia))
    
    print("Bot rodando...")
    app.run_polling()
    
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou o Lm Bot😎")
    

async def chat_ia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    headers = {
        "Authorization": f"Bearer {token_openrouter}",
        "Content-Type": "application/json"
    }
    
    user_input = update.message.text
    if user_input.lower() in ["sair", "quit", "exit"]:
        print("você escolheu sair!")
        return
    
    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": user_input}
        ]
        }
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers, 
        json=data
    )
        
    resposta_ia = response.json()["choices"][0]["message"]["content"]
    await update.message.reply_text(resposta_ia)


            