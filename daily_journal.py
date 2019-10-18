### MISSION STATEMENT ###
# This is a script that the user runs twice daily (morning and evening)
# It's modeled off the 'Five-Minute Journal'
# First, the user says whether they want to answer morning or evening prompts
# The user is then given prompts to answer, such as 'Give 3 things that you are grateful for'
# The questions and answers are then outputted to a .txt file at their home directory 
# I've (Alex) added additional functionality for me: the option to choose 'write for 10 minutes'...
# ... and then the user can write, and a bell sound is played (a .wav file) when 10 minutes has passed!

### KNOWN ISSUES ###
# If user doesn't input M, E, B or W, the script will end. I want it to loop until they enter right thing.

### FEATURES FOR FUTURE VERSIONS ###
# 1) Ability to track how many days in a row the script has been used, and this being printed to the user 
# 2) Replace .txt functionality for .docx, and have some formatting like bold questions? ...
# ... Although the syntax for writing .docx looks horrible, .txt is nice and easy
# 3) Improved "recall" section in evening section. Would be great for it to know what day it is today (i.e. Thur)...
# ... and prompt you individually to recall each previous day. I.e. "Ok so today is Thur, what did you do on Wed?"...
# ... "And what did you do on Tue?" etc. 
# 4) Would be great to have this as a runnable programme, rather than a Python script, so you don't have to...
# ... open your IDE or command line to do this every day. If it could be launched from the desktop, super convenient!

### IMPORTS ###
from datetime import datetime, date, timedelta # for dates
import time # for timer
import os # for operating system check
import sys # for checking if user computer is Mac or PC (I'm on a Mac, I know Dan uses Windows)
import pathlib # lets you save to specific place, and has same syntax for Windows and Mac
from pathlib import Path
import simpleaudio as sa # for sound effect after 10 minutes of writing

print(Path.home())

### OPERATING SYSTEM TEST ###
platform = sys.platform
if platform == 'linux':
	operating_system = 'linux'
elif platform == 'win32':
	operating_system = 'windows'
elif platform == 'cygwin':
	operating_system = 'windows'
elif platform == 'darwin':
	operating_system = 'mac'

### DECLARING VARIABLES ###
today = date.today()
today_date = today.strftime("%B %d, %Y")
yesterday = today - timedelta(days=1)
yesterday_date = yesterday.strftime("%B %d, %Y")

morning_prompt_1 = '\n*What are three things you are grateful for today?*'
morning_prompt_2 = '\n*What are three things that would make today great?*'
morning_prompt_3 = '\n*Time for your daily affirmation! "I am..."*'

evening_prompt_1 = '\n*What are three amazing things that happened today?*'
evening_prompt_2 = '\n*How could you have made today even better?*'

journal_prompt = '\n*Write a brief journal entry for the day!*'

recall_prompt = '\n*Give a quick summary of what you did yesterday (recall is vital for memory consolidation!)*'
recall_prompt_2 = '\n*Give a quick summary of what you did each day for the past 7 days (if you can!)*'

ten_mins_writing_prompt = '\n*Write for 10 minutes. Go!*\n*(When you\'re done, enter a single full stop on a line by itself)*\n'

### DEFINING FUNCTIONS ###
## streak_tracker() looks for yesterday's date in the .txt file, then the day before, etc
## currently only looks for yesterday's date
# Search .txt file for yesterday's date
def streak_tracker():
	if ((pathlib.Path.home() / 'Journal.txt').is_file()) == True:
		with open(pathlib.Path.home() / 'Journal.txt', 'r') as fd:
   			if yesterday_date in fd.read():
   				print('\nYou wrote an entry yesterday, nice one!')
   			else:
   				print('\nThis is day 1 of your streak, keep up the good work!')
	elif ((pathlib.Path.home() / 'Journal.txt').is_file()) == False:
		pass # if the journal.txt file doesn't exist, pass!

# morning_questions() checks existence of journal.txt and then enters questions and answers to this file 
def morning_questions():
	# Check if journal file exists
	if ((pathlib.Path.home() / 'Journal.txt').is_file()) == False:
		journal_file = open(pathlib.Path.home() / 'Journal.txt', 'w') # creates file if it doesn't exist
	elif ((pathlib.Path.home() / 'Journal.txt').is_file()) == True:
		journal_file = open(pathlib.Path.home() / 'Journal.txt', 'a') # reopen file in append mode so you don't overwrite previous answers
	print('Your answers will be saved at {}'.format(Path.home()))
	# Prompts and inputs
	print(morning_prompt_1)
	morning_answer_1 = str(input())
	print(morning_prompt_2)
	morning_answer_2 = str(input())
	print(morning_prompt_3)
	morning_answer_3 = str(input())
	# Saving answers
	journal_file.write('Morning: ' + today_date + '\n')
	journal_file.write(morning_prompt_1 + '\n')
	journal_file.write(morning_answer_1 + '\n \n')
	journal_file.write(morning_prompt_2 + '\n')
	journal_file.write(morning_answer_2 + '\n \n')
	journal_file.write(morning_prompt_3 + '\n')
	journal_file.write(morning_answer_3 + '\n \n')
	journal_file.close()
	print('\nSee you this evening. Have a great day!')

# evening_questions() checks existence of journal.txt and then enters questions and answers to this file 
def evening_questions():
	# Check is journal file exists
	if ((pathlib.Path.home() / 'Journal.txt').is_file()) == False:
		journal_file = open(pathlib.Path.home() / 'Journal.txt', 'w') # creates file if it doesn't exist
	elif ((pathlib.Path.home() / 'Journal.txt').is_file()) == True:
		journal_file = open(pathlib.Path.home() / 'Journal.txt', 'a') # reopen file in append mode so you don't overwrite previous answers
	print('Your answers will be saved at {}'.format(Path.home()))
	# Print prompts and save user answers
	print(evening_prompt_1)
	evening_answer_1 = str(input())
	print(evening_prompt_2)
	evening_answer_2 = str(input())
	# Write a brief journal entry for the day
	print(journal_prompt)
	journal_answer = str(input())
	# Summary of yesterday 
	print(recall_prompt)
	recall_answer = str(input())
	# Summary of last week 
	print(recall_prompt_2)
	recall_answer_2 = str(input())
	# Saving answers
	journal_file.write('Evening: ' + today_date + '\n')
	journal_file.write(evening_prompt_1 + '\n')
	journal_file.write(evening_answer_1 + '\n \n')
	journal_file.write(evening_prompt_2 + '\n')
	journal_file.write(evening_answer_2 + '\n \n')
	journal_file.write(journal_prompt + '\n')
	journal_file.write(journal_answer + '\n \n')
	journal_file.write(recall_prompt + '\n')
	journal_file.write(recall_answer + '\n \n')
	journal_file.write(recall_prompt_2 + '\n')
	journal_file.write(recall_answer_2 + '\n \n')
	journal_file.close()
	print('\nSee you tomorrow!')

# writing_prompt() checks existence of journal.txt and then enters multiline input into this file
# want it to start a 10 minute timer and beep when the timer is done! 	
def writing_prompt():
	# Check if Writing file exists
	if ((pathlib.Path.home() / 'Writing.txt').is_file()) == False:
		writing_file = open(pathlib.Path.home() / 'Writing.txt', 'w') # creates file if it doesn't exist
	elif ((pathlib.Path.home() / 'Writing.txt').is_file()) == True:
		writing_file = open(pathlib.Path.home() / 'Writing.txt', 'a') # reopen file in append mode so you don't overwrite previous answers
	print('Your answers will be saved at {}'.format(Path.home()))
	# Prompts and inputs
	print(ten_mins_writing_prompt)
	print('Starting the 10 minute timer now!')
	timer()
	# INPUT MULTIPLE LINES
	buffer = []
	while True:
    		print("> ", end="") # this indentation seems wrong, but it wouldn't run until I made it like this!
    		line = input()
    		if line == ".":
        		break
    		buffer.append(line)
	user_input_1 = "\n".join(buffer)
	# Saving answers
	writing_file.write(today_date + '\n')
	writing_file.write(user_input_1 + '\n')
	print('\nNice one! See you tomorrow.')

# make_noise() plays a sound effect
def make_noise():
	wave_obj = sa.WaveObject.from_wave_file("churchbell.wav")
	play_obj = wave_obj.play()
	play_obj.wait_done()

# timer() runs make_noise() after x amount of seconds (using 600 for 10 minute writing timer)
def timer():
	delay = 600 # 10 minutes of writing
	time.sleep(delay)
	make_noise()

### MAIN CODE ###
# Greeting
print('\n[Press CTRL + C to quit at any time]')
print('\nHello!')
print('\nThe date is {}'.format(today_date))
streak_tracker()

# Determining which prompts the user wants to answer
print('\nDo you want to answer the morning prompts [M], the evening prompts [E], both [B], or do you want to write for 10 minutes [W]?')
user_decision = str(input().upper()) # Ensures uncapitalized inputs are still registered
if user_decision == 'M':
	print('\nMorning prompts, sure!')
	morning_questions()
elif user_decision == 'E':
	print('\nEvening prompts, sure!')
	evening_questions()
elif user_decision == 'B':
	print('\nBoth, sure!')
	print('\nFirst, the morning prompts')
	morning_questions()
	print('\nNice. Now for the morning prompts')
	evening_questions()
elif user_decision == 'W':
	print('\nWriting for 10 minutes, sure!')
	writing_prompt()
else: 
	print('Sorry, I didn\'t understand that. Type M for morning prompts, E for evening, or B for both!')
		# need to get the loop to repeat here