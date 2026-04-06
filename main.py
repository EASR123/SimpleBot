import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot.config import config
from bot.database import init_db
from bot.handlers import start, help_command, about, mi_perfil, echo

# Configurar logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Verificar configuración
    if not config.BOT_TOKEN:
        logger.error("Falta BOT_TOKEN en .env")
        return
    
    # Inicializar base de datos
    init_db()
    logger.info("Base de datos lista")
    
    # Crear bot
    app = Application.builder().token(config.BOT_TOKEN).build()
    
    # Agregar comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("miperfil", mi_perfil))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Iniciar bot
    logger.info("Bot iniciado!")
    app.run_polling()

if __name__ == "__main__":
    main()