import pyautogui
import time

# update the co-ordinates to fit your screen
long_button_x, long_button_y = 100, 150
close_button_x, close_button_y = 100, 550

def gui_open_long():
    pyautogui.moveTo(long_button_x, long_button_y)
    time.sleep(0.25)
    pyautogui.click()
    
def gui_close_long():
    pyautogui.moveTo(close_button_x, close_button_y)
    time.sleep(0.25)
    pyautogui.click()

def main():
    gui_open_long()
    time.sleep(1)
    gui_close_long()
    
if __name__ == '__main__':
    main()
