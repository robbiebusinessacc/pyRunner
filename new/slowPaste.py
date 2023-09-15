import pyperclip
import pyautogui
import time
import random
import keyboard

def slow_type(text, delay=0.07):
    """
    Types out the given text slowly, simulating manual keyboard input.
    """
    for char in text:
        if keyboard.is_pressed('esc'):
            print("Typing canceled!")
            return

        # Adjust delay by a random factor within ±20%
        adjusted_delay = delay * random.uniform(0.8, 1.2)

        pyautogui.write(char)
        time.sleep(adjusted_delay)

def main():
    time.sleep(2)
    # Enable pyautogui's fail-safe # 
    pyautogui.FAILSAFE = True

    # Get the current clipboard content
    text = pyperclip.paste()

    try:
        # Type it out slowly
        slow_type(text)
    except pyautogui.FailSafeException:
        print("Script halted due to escape mechanism (cursor in top-left corner).")
main()
