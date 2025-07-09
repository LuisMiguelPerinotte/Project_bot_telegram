import threading

from bot import inicio_bot
from interface import inicio_interface

thread_bot = threading.Thread(target=inicio_interface)
thread_bot.start()

inicio_bot()