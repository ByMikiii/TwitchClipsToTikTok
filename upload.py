import pyautogui
import webbrowser
import time
import random

def upload():
    # time.sleep(5)
    # print(pyautogui.position())
    # quit()

    browser = webbrowser.get("C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s")

    hashtags = ['fyp', 'foryou', 'funny', 'trending', 'viral', 'foryoupage', 'twitch']

    # Select multiple unique random hashtags from the array
    num_hashtags = 3 
    random_hashtags = random.sample(hashtags, num_hashtags)

    browser.open_new_tab('https://www.tiktok.com/upload?lang=en')
    time.sleep(5)
    pyautogui.leftClick(900, 500)

    pyautogui.leftClick(425, 50)

    pyautogui.typewrite('C:\\Users\\Bymikiii\\Development\\TwitchClipsToTikTok\\clip_edited.mp4')

    pyautogui.hotkey('enter')

    time.sleep(11)

    pyautogui.leftClick(860, 355)

    time.sleep(0.5)

    pyautogui.scroll(-140)

    pyautogui.leftClick(860, 355)

    for i in range(12):
        pyautogui.hotkey('backspace')

    file = open("currentclip.txt", "r")
    channelName = file.read()
    file.close()
    pyautogui.typewrite(f"{channelName} ")

    for hashtag in random_hashtags:
        pyautogui.typewrite(f"#{hashtag}")
        time.sleep(0.8)
        pyautogui.hotkey('enter')

    pyautogui.leftClick(1014, 928)
    print("Uploaded successfully!")
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')
