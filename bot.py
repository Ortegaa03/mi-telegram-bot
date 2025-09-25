import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configurar logs
logging.basicConfig(level=logging.INFO)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu primer bot 🎉")

def main():
    # Tomar el token de la variable de entorno llamada BOT_TOKEN
    token = os.getenv("BOT_TOKEN")

    if token is None:
        print("❌ Error: No se encontró BOT_TOKEN. Pon tu token en la variable de entorno BOT_TOKEN.")
        return
    else:
        print("✅ Token cargado correctamente.")

    app = Application.builder().token(token).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))

    # Iniciar el bot
    app.run_polling()

if __name__ == "__main__":
    main()
