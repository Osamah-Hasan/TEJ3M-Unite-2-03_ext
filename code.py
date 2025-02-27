"""
Created by: Osamah
Created on: FEB 2025
Created for: TEJ3M-Unit 2-03 LED python loop
"""

import board
import digitalio
import time

blink_time = 1

# Set up the LED pin (change 'board.GP15' to the correct pin for your board)
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True  # Turn LED on
    time.sleep(blink_time)

    led.value = False  # Turn LED off
    time.sleep(blink_time)
