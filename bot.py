import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configurar logs
logging.basicConfig(level=logging.INFO)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu primer bot 🎉")

def main():
    import os
    token = os.getenv("8213842847:AAEmzSiUQxO9OdwwfEPJNr2VfOjICTlqKPI")  # Tomar el token de variables de entorno
    app = Application.builder().token(token).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
