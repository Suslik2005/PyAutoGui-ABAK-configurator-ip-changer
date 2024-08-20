import pyautogui
import time


print("Введите ip адрес")
a = input()
#открываем
pyautogui.hotkey('win', 'r')  # открываем "Выполнить"
pyautogui.typewrite('C:\Program Files (x86)\ABAK PLC Configurator\AbakConfigurator.exe')
pyautogui.press('enter')
time.sleep(2)

pyautogui.click(28, 85)
time.sleep(3)
pyautogui.click(811, 565)
time.sleep(1)
pyautogui.click(801, 499)
pyautogui.keyDown('ctrl')  # hold down the shift key
pyautogui.click(801, 499)
pyautogui.click(801, 499)
pyautogui.keyUp('ctrl')
pyautogui.click(912, 609)
time.sleep(3)
pyautogui.click(316, 43)
time.sleep(1)
pyautogui.moveTo(384,78)
time.sleep(1)
pyautogui.moveTo(880, 78)
pyautogui.click(880,78)
time.sleep(1)
pyautogui.click(795, 198)
time.sleep(2)
pyautogui.click(1075, 277)
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('backspace')
for i in a:
    pyautogui.press(i)

pyautogui.click(720, 155)
pyautogui.click(1096, 667)
time.sleep(15)
pyautogui.click(1120, 674)
pyautogui.click(1287, 113)


