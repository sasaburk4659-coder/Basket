import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

TOKEN = '8770831969:AAEkbp-CjBGZk4_6aDZRNwsKzJ4GLWMZrdQ'
APP_URL = 'https://YOUR_GITHUB_USERNAME.github.io/REPO_NAME/'  # замените на ваш URL

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context):
    args = context.args
    code = args[0] if args else ''
    web_app_url = f"{APP_URL}?code={code}"
    keyboard = [[InlineKeyboardButton("🚀 Открыть приложение", web_app={'url': web_app_url})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Нажмите кнопку ниже, чтобы открыть мини-приложение",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()