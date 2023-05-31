import logging
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler
from datetime import datetime
import pytz

# Настройка журналирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Функция-обработчик команды /start
def start(update, context):
    button = KeyboardButton('/time')
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Привет! Я телеграм бот.', reply_markup=keyboard)

# Функция-обработчик команды /time
def get_time(update, context):
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Текущее московское время: {current_time}")

# Получаем токен вашего бота
TOKEN = '6208198607:AAEgUzS6QuESJ3PKV8KzZp6zh8FNNGGzNQ4'

# Создаем экземпляр Updater и передаем токен вашего бота
updater = Updater(token=TOKEN, use_context=True)

# Получаем экземпляр Dispatcher для регистрации обработчиков команд
dispatcher = updater.dispatcher

# Регистрируем обработчик команды /start
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Регистрируем обработчик команды /time
time_handler = CommandHandler('time', get_time)
dispatcher.add_handler(time_handler)

# Запускаем бота
updater.start_polling()
