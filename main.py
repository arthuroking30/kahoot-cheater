
import math
import ctypes

import time
import tkinter as tk
import pyautogui
import undetected_chromedriver as uc
from undetected_chromedriver.webelement import By

browser=uc.Chrome();


browser.get("https://kahoot.com/")
kahootWindow=browser.current_window_handle
pyautogui.hotkey("win", "left")
browser.switch_to.new_window("window")

chatWindow=browser.current_window_handle
browser.get("https://chat.openai.com/?sso=")
pyautogui.getWindowsWithTitle("chatGPT")[0].activate()
pyautogui.hotkey("win", "right")
browser.switch_to.window(kahootWindow)


time.sleep(2)
cookies=browser.find_element(By.ID,"onetrust-accept-btn-handler")
cookies.click();


def hexToColor(hex):
  converter={
     "#e21b3c":"Red",
     "#1368ce":"Blue",
     "#d89e00":"Orange",
     "#26890c":"Green"
  }
  return converter[hex]


def on_button_click():
    browser.switch_to.window(browser.window_handles[-1])
    questionFormated=""
    try:
      multiSelect=browser.find_element(By.CLASS_NAME,"multi-select-label__Label-sc-z37063-0")
    except:
      questionFormated=questionFormated+"Choose one answer:"
    else:
      questionFormated=questionFormated+multiSelect.text+":"

    question=browser.find_element(By.CLASS_NAME,"question-title__Title-sc-12qj0yr-1") 
    answers=browser.find_elements(By.CLASS_NAME,"card__InteractiveCard-sc-lblpdo-1")
    questionFormated= questionFormated+question.text+"\n"

    print(question)

    for answer in answers:
        hexColor=answer.get_attribute("color")
        color=hexToColor(hexColor)
        questionFormated=questionFormated+color+": "+answer.text+" or "
    print(questionFormated)

    browser.switch_to.window(chatWindow)
    chatArea=browser.find_element(By.ID,"prompt-textarea")

    chatArea.send_keys(questionFormated)

    chatArea.submit()

    browser.switch_to.window(browser.window_handles[-1])
    


user32 = ctypes.windll.user32
displayWidth=user32.GetSystemMetrics(0)

# Create the main window
window = tk.Tk()
window.title("Cheater")
window.attributes("-topmost", True)
window.geometry(f"300x300+{math.trunc(displayWidth/2)}+0")

# Create a button and link it to the on_button_click function
button = tk.Button(window, text="Cheat", command=on_button_click)

# Pack the button into the window
button.pack(pady=20)

# Start the main event loop
window.mainloop()

browser.quit()

