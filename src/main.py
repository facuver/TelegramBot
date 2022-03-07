from utelegram import (
    Bot,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from machine import Pin
import utime
import logging
import gc
import uasyncio as asyncio

log = logging.getLogger(__name__)
logging.basicConfig(level=0)


def timed_function(f, *args, **kwargs):
    myname = str(f).split(" ")[1]

    def new_func(*args, **kwargs):
        t = utime.ticks_us()
        result = f(*args, **kwargs)
        delta = utime.ticks_diff(utime.ticks_us(), t)
        print("Function {} time = {:6.3f}ms".format(myname, delta / 1000))
        return result

    return new_func


TOKEN = "5118983479:AAFe7UnVnzbaajJ6yVi98LnMvCGVcQh9xLY"

bot = Bot(TOKEN)


# KEYBOARD DEFINED AS ARRAY OF ARRAYS OF KEYBOARDBUTTONS
keyboard = [[KeyboardButton("ON"), KeyboardButton("OFF")], [KeyboardButton("Toggle")]]

# replyKeyboard = ReplyKeyboardMarkup(keyboard)
inline_keyboard = [
    [InlineKeyboardButton("Log", callback_data="Login")],
    [InlineKeyboardButton("Google", "http://google.com")],
]
replyKeyboard = InlineKeyboardMarkup(inline_keyboard)


@bot.add_command_handler("que hora es?")
def help(update):
    update.reply(utime.localtime())


@bot.add_message_handler("[A-Z]*123$")
def default(update):
    update.reply("Hello")


@bot.add_callback_handler("Login")
def Login(update):
    log.debug("Callback")
    update.edit("YES", reply_markup=replyKeyboard)


@bot.add_command_handler("start")
def start(update):
    update.reply("Led control keyboard enabled", reply_markup=replyKeyboard)


@timed_function
def read():
    while True:
        bot._read()


while True:
    read()
