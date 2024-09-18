import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import ImageGrab, ImageOps
import time

"""An application that opens and runs the google dinosaur game."""

url = "https://elgoog.im/dinosaur-game/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
driver.maximize_window()
time.sleep(3)

pyautogui.press("space")

time.sleep(2)
new_element = driver.find_element(By.XPATH, '//*[@id="main-frame-error"]/div[6]/span')
new_x, new_y = new_element.location["x"], new_element.location["y"]
pyautogui.moveTo(new_x, new_y)

currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(currentMouseX + 280, currentMouseY + 60)
currentMouseX, currentMouseY = pyautogui.position()

a = currentMouseX
b = a + 70
c = currentMouseY
d = c + 30
pyautogui.moveTo(a, d)

game = True
while game:
    image = ImageGrab.grab(bbox=(a, c, b, d))
    gray = ImageOps.grayscale(image)
    palette = gray.getcolors()
    palette = [i[1] for i in palette]
    palette.sort(reverse=True)
    colors = palette[0:3]
    if colors != [255]:
        pyautogui.press("space")
        time.sleep(.01)


