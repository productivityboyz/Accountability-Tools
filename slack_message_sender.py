# THIS WILL ONLY WORK WITH THE RASPBERRY PI SET TO RESOLUTION OF 1280 BY 720

import pyautogui
import threading
import random
import schedule
import time

pyautogui.PAUSE = 20 # pause of x seconds after each function call
                     # heavy delay because the raspberry pi is slow, especially loading slack
pyautogui.FAILSAFE = True # force mouse to top left corner to stop script running
width, height = pyautogui.size()

# print(pyautogui.position()) # gives mouse position at time of function call


message_list = ['daily public reminder to do ur pledges',
                'do your meditation etc', 'daily reminder',
                'don\'t forget your pledges', 'send ur pledge proof',
                'pledge reminder']

### MAIN CODE ###
def open_slack():
    # get to slack group
    pyautogui.click(66,18) # open web browser
    pyautogui.click(206,116) # click web search bar
    pyautogui.typewrite('www.slack.com') # type slack.com
    pyautogui.typewrite(['enter'])
    pyautogui.click(695,570) # sign into slack
    pyautogui.click(610,689) # click the relevant slack group
    
    # navigate to correct slack channel
    pyautogui.click(98,267) # click "jump to" box
    pyautogui.typewrite('accountability')
    pyautogui.typewrite(['enter'])
    
    # type message
    pyautogui.click(402,670) # click message box
    random_index = random.randint(0,(len(message_list)-1)) # get a random number
    today_message=message_list[random_index]
    print(today_message)
    pyautogui.hotkey('shift','2') # best way to do the '@' symbol
    pyautogui.typewrite('el ') 
    pyautogui.typewrite(today_message) # type random message into slack
    #pyautogui.typewrite('.')
    #click send
    pyautogui.typewrite(['enter'])
    
    # close the web browser
    pyautogui.click(1265,48) # top right corner
    print('done')

### DELAY UNTIL x time ###
schedule.every().day.at("21:00").do(open_slack)

while True:
    schedule.run_pending()
    time.sleep(600) # wait 10 minutes