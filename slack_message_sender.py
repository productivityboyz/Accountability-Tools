import pyautogui
import threading
import random
import schedule

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
    pyautogui.click(64,17) # open web browser
    pyautogui.click(191,119) # click web search bar
    pyautogui.typewrite('www.slack.com') # type slack.com
    pyautogui.typewrite(['enter'])
    pyautogui.click(695,562) # sign into slack
    pyautogui.click(632,728) # click the relevant slack group
    
    # navigate to correct slack channel
    pyautogui.click(75,267) 
    pyautogui.typewrite('accountability')
    pyautogui.typewrite(['enter'])
    
    # type message
    pyautogui.click(444,979) # click message box
    random_index = random.randint(0,(len(message_list)-1)) # get a random number
    today_message=message_list[random_index]
    print(today_message)
    pyautogui.hotkey('shift','2') # best way to do the '@' symbol
    pyautogui.typewrite('el ') 
    pyautogui.typewrite(today_message) # type random message into slack
    
    #click send
    pyautogui.typewrite(['enter'])
    
    # close the web browser
    pyautogui.click(1265,48) # click message box
    print('done')

### DELAY UNTIL x time ###
schedule.every().day.at("21:00").do(open_slack())

while True:
    schedule.run_pending()
    time.sleep(600) # wait 10 minutes