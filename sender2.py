# Add your Python code here. E.g.
from microbit import *
import radio
radio.on()
radio.config(group=200)
while True:

    if button_a.is_pressed():
        radio.send("hi")
    sleep(2000)
