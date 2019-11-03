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

### NEXT FEATURE TO ADD ### 
# Option for script to show you your last week of journal entries, to aid recall!
# Maybe should ask user for 1-sentence summary of each day, and this is what's shown.
# Add the date to the recall. So instead of "Today is Wed. What did you do on Tue?" ...
# ... Have it be "Today is Wed the 2nd. What did you do on Tue the 1st?" ...
# ... As it's easier to remember an exact date than a random day 

### FEATURES FOR FUTURE VERSIONS ###
# 1) Ability to track how many days in a row the script has been used, and this being printed to the user 
# 2) Improved "recall" section in evening section. Would be great for it to know what day it is today (i.e. Thur)...
# 3) Would be great to have this as a runnable programme, rather than a Python script, so you don't have to...
# ... open your IDE or command line to do this every day. If it could be launched from the desktop, super convenient!
# 4) A GUI with TKinter? Time sink though.

### MINOR TWEAKS
# Would be nice to make the terminal/ shell look better, maybe keeping inputs at the top...
# ... or adding a slight delay to each print-out, so things don't all appear at once

### IMPORTS ###
from datetime import datetime, date, timedelta # for dates
import time # for timer
import os # for operating system check
import sys # for checking if user computer is Mac or PC (I'm on a Mac, I know Dan uses Windows)
import pathlib # lets you save to specific place, and has same syntax for Windows and Mac
from pathlib import Path
import simpleaudio as sa # for sound effect after 10 minutes of writing
import threading # apparently using time.sleep() is why my 10 minute thing is dying 
from pyfiglet import Figlet # snazzy command-line title 

### OPERATING SYSTEM TEST ###
print(Path.home())
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
today_date = today.strftime("%A %d %B, %Y") # [weekday] the [num]
#today_date = today.strftime("%B %d, %Y") # November 2, 2019

yesterday = today - timedelta(days=1)
yesterday_date = yesterday.strftime("%B %d, %Y")

morning_prompts = ['\n*What are three things you are grateful for today?*', 
					'\n*What are three things that would make today great?*',
					'\n*Time for your daily affirmation! "I am..."*']

evening_prompts = ['\n*What are three amazing things that happened today?*',
					'\n*How could you have made today even better?*']

journal_prompts = ['\n*Write a brief journal entry for the day!*']

recall_prompts = ['\n*Give a quick summary of what you did yesterday (recall is vital for memory consolidation!)*',
					'\n*Give a quick summary of what you did each day for the past 7 days (if you can!)*']

ten_mins_writing_prompt = "\n*Write for 10 minutes!*\n*A sound effect will play when the time is up.*\n*To save, enter a full stop on a new line.*\n"

morning_answers=[]
evening_answers=[]

### DEFINING FUNCTIONS
# morning_questions() checks existence of journal.txt and then enters questions and answers to this file 

def file_creator(file_name): # used in other functions, like "morning_questions", to reduce redundancy 
	global file_variable # have to make it global so it can be used outside of functions
	if ((pathlib.Path.home() / file_name).is_file()) == False:
		file_variable = open(pathlib.Path.home() / file_name, 'w') # creates file if it doesn't exist
	elif ((pathlib.Path.home() / file_name).is_file()) == True:
		file_variable = open(pathlib.Path.home() / file_name, 'a') # reopen file in append mode so you don't overwrite previous answers

def questions(morn_or_eve):
	# Check if journal file exists
	file_creator('Journal.txt') # checks for file "test.txt"
	print('Your answers will be saved at {}'.format(Path.home()))
	if morn_or_eve == "morning":
		# Prompts and inputs
		for counter, value in enumerate(morning_prompts):
			print(value)
			morning_answers.append(str(input()))
		# Saving answers
		file_variable.write('\nMorning: ' + today_date + '\n')
		counter = 0
		for i in (morning_prompts):
			file_variable.write(morning_prompts[counter] + '\n')
			file_variable.write(morning_answers[counter] + '\n')
			counter += 1
		file_variable.close()
	elif morn_or_eve == 'evening':
		# Print prompts and save user answers
		for counter, value in enumerate(evening_prompts):
			print(value)
			evening_answers.append(str(input()))
		# Saving answers
		file_variable.write('\nEvening: ' + today_date + '\n')
		counter = 0
		for i in (evening_prompts):
			file_variable.write(evening_prompts[counter] + '\n')
			file_variable.write(evening_answers[counter] + '\n')
			counter += 1
		file_variable.close()
	
def week_recall():
	file_creator('Journal.txt') # tests to ensure file exists. 
	today = date.today() # type: datetime.date
	today_string = today.strftime("%A %B %d, %Y") # [Day], [Month] [Day Number], [Year]
	recall_counter = 1
	for i in range(6):
		d = today - timedelta(days=recall_counter) # 'd' is just an arbitrary variable name
		d_string = d.strftime("%A %B %d, %Y") # [Day], [Month] [Day Number], [Year]
		recall_counter += 1
		day_recall_prompt = ('\nToday is {}. What did you do on {}?'.format(today_string,d_string))
		print(day_recall_prompt)
		day_recall_input = str(input())
		# add question + answer to journal.txt
		file_variable.write(day_recall_prompt + '\n')
		file_variable.write(day_recall_input + '\n \n')
	print('\nNice one! See you tomorrow.\n')
	file_variable.close()

# writing_prompt() checks existence of journal.txt and then enters multiline input into this file
# want it to start a 10 minute timer and beep when the timer is done! 	
def writing_prompt():
	# Check if Writing file exists
	file_creator('Writing.txt') # tests to ensure file exists. 
	print('Your answers will be saved at {}'.format(Path.home()))
	# Prompts and inputs
	print(ten_mins_writing_prompt)
	print('Starting the 10 minute timer now!')
	time_delay()
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

# time_delay() runs make_noise() after x amount of seconds (using 600 for 10 minute writing timer)
def time_delay():
	timer = threading.Timer(600.00, make_noise)
	timer.start()

### MAIN CODE ###
# Greeting

f = Figlet(font='slant')
print(f.renderText('Welcome to Daily Journal 2.0'))

print('\n[Press CTRL + C to quit at any time]')
print('\nHello!')
print('\nThe date is {}'.format(today_date))
#streak_tracker()

# Determining which prompts the user wants to answer
print('\nDo you want to answer the morning prompts [M], the evening prompts [E], or do you want to write for 10 minutes [W]?')
user_decision = str(input().upper()) # Ensures uncapitalized inputs are still registered
if user_decision == 'M':
	print('\nMorning prompts, sure!')
	questions('morning')
elif user_decision == 'E':
	print('\nEvening prompts, sure!')
	questions('evening')
	week_recall()
elif user_decision == 'W':
	print('\nWriting for 10 minutes, sure!')
	writing_prompt()
else: 
	print('Sorry, I didn\'t understand that. Type M for morning prompts, E for evening, or B for both!')