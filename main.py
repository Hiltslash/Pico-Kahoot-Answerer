from machine import Pin
import time
import sys

# Setup buttons
redButton = Pin(16, Pin.IN, Pin.PULL_UP)
blueButton = Pin(28, Pin.IN, Pin.PULL_UP)
greenButton = Pin(0, Pin.IN, Pin.PULL_UP)
yellowButton = Pin(15, Pin.IN, Pin.PULL_UP)

# Last states
lastRedState = 1
lastBlueState = 1
lastGreenState = 1
lastYellowState = 1

while True:
    # Red button
    redState = redButton.value()
    if redState == 0 and lastRedState == 1:
        print("red")  # send over USB serial
    lastRedState = redState

    # Blue button
    blueState = blueButton.value()
    if blueState == 0 and lastBlueState == 1:
        print("blue")
    lastBlueState = blueState

    # Green button
    greenState = greenButton.value()
    if greenState == 0 and lastGreenState == 1:
        print("green")
    lastGreenState = greenState

    # Yellow button
    yellowState = yellowButton.value()
    if yellowState == 0 and lastYellowState == 1:
        print("yellow")
    lastYellowState = yellowState

    time.sleep(0.01)

