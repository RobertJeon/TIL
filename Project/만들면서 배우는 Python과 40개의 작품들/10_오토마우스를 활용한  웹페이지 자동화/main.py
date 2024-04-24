
import pyautogui
import time
import pyperclip

# 0.1초마다 마우스의 좌표 출력하는 코드
"""
while True:
    print(pyautogui.position())
    time.sleep(0.1)
"""

# 좌표
# pyautogui.moveTo(x,y,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

# pip install pyautogui
# pip install pyperclip