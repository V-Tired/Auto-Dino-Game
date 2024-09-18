import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import ImageGrab, ImageOps
from tkinter import Tk
import time

"""An application that opens and runs the google dinosaur game."""


class Webdriver:
    """Initiates selenium webdriver on the Google dinosaur site"""
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        url = "https://elgoog.im/dinosaur-game/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(3)
        pyautogui.press("space")
        time.sleep(2)
        self.find_space()

    def find_space(self):
        """Locates the element in the game to help position the check window"""
        new_element = self.driver.find_element(By.XPATH, '//*[@id="main-frame-error"]/div[6]/span')
        new_x, new_y = new_element.location["x"], new_element.location["y"]
        pyautogui.moveTo(new_x, new_y)
        self.move_mouse()

    def move_mouse(self):
        """Moves mouse to bottom left corner of check window"""
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.moveTo(currentMouseX + 475, currentMouseY + 60)
        currentMouseX, currentMouseY = pyautogui.position()
        self.a = currentMouseX
        self.b = self.a + 40
        self.c = currentMouseY
        self.d = self.c + 40
        pyautogui.moveTo(self.a, self.d)
        pyautogui.keyDown("down")

    def image_grab(self):
        """Creates a 40x20 pixel box image and checks if it is white. If not, controls the dino to stand and jump."""
        image = ImageGrab.grab(bbox=(self.a, self.c, self.b, self.d))
        gray = ImageOps.grayscale(image)
        palette = gray.getcolors()
        palette = [i[1] for i in palette]
        palette.sort(reverse=True)
        colors = palette[0:3]
        if colors != [255]:
            pyautogui.keyUp("down")
            time.sleep(.01)
            pyautogui.press("space")
            time.sleep(.2)
            pyautogui.keyDown("down")

    def check_end(self):
        """Checks if the game over image has appeared or the cursor is nearing the top of the screen
         and shuts the window down."""
        currentMouseX, currentMouseY = pyautogui.position()
        size = driver.driver.get_window_size()
        if currentMouseX >= size['width'] - 60:
            return True
        image = ImageGrab.grab(bbox=(817, 501, 819, 503))
        gray = ImageOps.grayscale(image)
        palette = gray.getcolors()
        palette = [i[1] for i in palette]
        palette.sort(reverse=True)
        colors = palette[0:3]
        if colors != [255]:
            pyautogui.press("space")

# Window and webdriver initialization
window = Tk()
driver = Webdriver()
screen_height = window.winfo_screenheight()
game = True

while game:
    driver.image_grab()
    end = driver.check_end()
    if end:
        driver.driver.close()
        break
