"""
hello.py
    Writes "Hello!" in random colors at random locations on the display.
"""

import utime
import st7789
from machine import SPI,Pin
import vga1_bold_16x32 as font




def config(rotation=1, buffer_size=0, options=0):
    return st7789.ST7789(
        SPI(1, baudrate=30000000, sck=Pin(18), mosi=Pin(19)),
        135,
        240,
        reset=Pin(23, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(16, Pin.OUT),
        backlight=Pin(4, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size= buffer_size)


tft = config()
tft.init()

def center(text : str) -> None:
    '''
    Put Text in center with red background
    '''
    length = len(text)
    tft.fill(st7789.WHITE)
    tft.text(
        font,
        text,
        tft.width() // 2 - length // 2 * font.WIDTH,
        tft.height() // 2 - font.HEIGHT,
        st7789.BLACK,
        st7789.WHITE)
