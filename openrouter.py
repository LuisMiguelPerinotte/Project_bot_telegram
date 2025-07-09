import requests

from telegram import Update
from telegram.ext import ContextTypes

import os
from dotenv import load_dotenv

load_dotenv()
token_openrouter = os.getenv("OPENROUTER_KEY")

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