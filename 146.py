from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from pynput.keyboard import Key, Controller
import time
import pyperclip
import pyautogui
from tkinter import Tk 
import win32clipboard
import keyboard

keyboard = Controller()

driver.get('https://bc.instructure.com')

time.sleep(2)

keyboard.type("[REDACTED]")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(1)
keyboard.type("[REDACTED]")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(0.3)
button_element = driver.find_element_by_id('global_nav_courses_link')
button_element.click()

time.sleep(0.3)
button_element = driver.find_element_by_link_text("4007C013 - ACCT 146 10-Key")
button_element.click()

time.sleep(0.3)
button_element = driver.find_element_by_link_text("Ten Key Mastery Lessons")
button_element.click()

time.sleep(1)
button_element = driver.find_element_by_class_name("btn")
button_element.click()

time.sleep(3)
pyautogui.moveTo(x=251, y=474)
time.sleep(1)
pyautogui.click(button='left')


for x in range(0,12) :
    #1st
    time.sleep(0.35)
    pyautogui.moveTo(x=264, y=349)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=478, y=348)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)
  
    time.sleep(0.35)
    pyautogui.moveTo(x=264, y=379)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=478, y=348)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)


    #2nd
    time.sleep(0.35)
    pyautogui.moveTo(x=266, y=416)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=479, y=416)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    time.sleep(0.35)
    pyautogui.moveTo(x=265, y=446) #4
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=479, y=416)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    #5
    time.sleep(0.35)
    pyautogui.moveTo(x=265, y=481)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=480, y=481)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    time.sleep(0.35)
    pyautogui.moveTo(x=264, y=514)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=480, y=481)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    #7th
    time.sleep(0.35)
    pyautogui.moveTo(x=270, y=549)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=470, y=549)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    time.sleep(0.35)
    pyautogui.moveTo(x=263, y=581)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=470, y=549)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    #9
    time.sleep(0.35)
    pyautogui.moveTo(x=269, y=611)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=470, y=549)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)
    
    time.sleep(0.35)
    pyautogui.moveTo(x=263, y=643)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=470, y=549)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    time.sleep(0.35)
    pyautogui.moveTo(x=263, y=673)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=478, y=348)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    #11
    time.sleep(0.35)
    pyautogui.moveTo(x=362, y=349)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=478, y=348)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)
  
    time.sleep(0.35) #12
    pyautogui.moveTo(x=360, y=379)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=478, y=348)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)


    #2nd
    time.sleep(0.35)
    pyautogui.moveTo(x=362, y=416)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=479, y=416)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    time.sleep(0.35)
    pyautogui.moveTo(x=360, y=449) #4
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=479, y=416)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    #5
    time.sleep(0.35)
    pyautogui.moveTo(x=360, y=481)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=480, y=481)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    time.sleep(0.35)
    pyautogui.moveTo(x=360, y=514)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=480, y=481)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    #7th
    time.sleep(0.35)
    pyautogui.moveTo(x=360, y=549)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=470, y=549)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    time.sleep(0.35)
    pyautogui.moveTo(x=360, y=581)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=470, y=549)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

    #9
    time.sleep(0.35)
    pyautogui.moveTo(x=360, y=611)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=470, y=549)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)
    
    time.sleep(0.35)
    pyautogui.moveTo(x=360, y=643)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=470, y=549)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)
    
    time.sleep(0.35)
    pyautogui.moveTo(x=360, y=673)
    pyautogui.click(button='left')
    pyautogui.click(button='left')
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.moveTo(x=470, y=549)
    pyautogui.click(button= 'left')
    keyboard.type(data)
    keyboard.press(Key.enter)

#keyboard.press(Key.ctrl)
#keyboard.press('w')
#keyboard.release(Key.ctrl)
#keyboard.release('w')
#time.sleep(0.2)
#keyboard.press(Key.ctrl)
#keyboard.press('w')
#keyboard.release(Key.ctrl)
#keyboard.release('w')










