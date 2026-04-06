from telegram import Update
from telegram.ext import ContextTypes
from bot.database import save_user, get_user, save_message
from bot.config import config

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    save_message(user.id, "/start", "in")
    
    text = f"¡Hola {user.first_name}! 👋\n\nComandos:\n/help - Ayuda\n/about - Info\n/miperfil - Tu perfil"
    await update.message.reply_text(text)
    save_message(user.id, text, "out")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_message(user.id, "/help", "in")
    
    text = "📋 Comandos:\n/start - Inicio\n/help - Ayuda\n/about - Info\n/miperfil - Ver perfil"
    await update.message.reply_text(text)
    save_message(user.id, text, "out")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_message(user.id, "/about", "in")
    
    text = "🤖 Bot simple v1.0\nCreado con python-telegram-bot"
    await update.message.reply_text(text)
    save_message(user.id, text, "out")

async def mi_perfil(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_message(user.id, "/miperfil", "in")
    
    user_data = get_user(user.id)
    if user_data:
        text = f"👤 Perfil:\nID: {user_data['user_id']}\nNombre: {user_data['first_name']}\nUsername: @{user_data['username']}"
    else:
        text = "No encontré tus datos"
    
    await update.message.reply_text(text)
    save_message(user.id, text, "out")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text_in = update.message.text
    
    save_user(user.id, user.username, user.first_name)
    save_message(user.id, text_in, "in")
    
    text_out = f"Dijiste: {text_in}\n\n(Próximamente: respuestas con IA)"
    await update.message.reply_text(text_out)
    save_message(user.id, text_out, "out")