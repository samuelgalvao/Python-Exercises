import pyautogui as spam
import time

limit = input('Number of msg: ')
msg = input('MSG: ')

i = 0

while i<int(limit):
    spam.typewrite(msg)
    spam.press('Enter')
    i += 1