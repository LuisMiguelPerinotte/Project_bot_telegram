import threading

from bot import inicio_bot
from interface import inicio_interface

thread_interface = threading.Thread(target=inicio_interface)
thread_interface.start()

inicio_bot()