from utelegram import Bot, ReplyKeyboardMarkup, KeyboardButton , InlineKeyboardMarkup, InlineKeyboardButton
from machine import Pin
import utime
TOKEN = '5118983479:AAFe7UnVnzbaajJ6yVi98LnMvCGVcQh9xLY'

bot = Bot(TOKEN)


#KEYBOARD DEFINED AS ARRAY OF ARRAYS OF KEYBOARDBUTTONS
keyboard = [
        [KeyboardButton('ON'), KeyboardButton('OFF')],
        [KeyboardButton('Toggle')]
        ]

#replyKeyboard = ReplyKeyboardMarkup(keyboard) 
inline_keyboard = [[InlineKeyboardButton("Log",callback_data="Login")], [InlineKeyboardButton("Google","http://google.com")]]
replyKeyboard = InlineKeyboardMarkup(inline_keyboard)

@bot.add_command_handler('help')
def help(update):
    update.reply('Write /start to get a custom keyboard or /value to get the current led status')

@bot.add_callback_handler("Login")
def Login(update):
    print("Editing")
    update.edit("YES",reply_markup = replyKeyboard)

@bot.add_command_handler('start')
def start(update):
    update.reply('Led control keyboard enabled', reply_markup=replyKeyboard)

while True:
    bot._read()
    utime.sleep(1)