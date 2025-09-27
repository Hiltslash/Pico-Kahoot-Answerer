import serial
import pyautogui
import time

# Replace this with your Pico's actual serial device
ser = serial.Serial('/dev/tty.usbmodem1101', 115200, timeout=0.1)
time.sleep(2)  # wait for Pico to initialize

def moveTo(place):
    if place == "yellow":
        pyautogui.moveTo(300, 800)
    elif place == "red":
        pyautogui.moveTo(300, 750)
    elif place == "green":
        pyautogui.moveTo(800, 800)
    elif place == "blue":
        pyautogui.moveTo(800, 750)
    pyautogui.click()

while True:
    if ser.in_waiting:
        line = ser.readline().decode().strip()
        if line in ["red", "blue", "green", "yellow"]:
            moveTo(line)
