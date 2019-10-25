### MISSION STATEMENT ###
# This is a script that the user would run daily
# It will be modeled off the 'Five-Minute Journal'
# The user will be given prompts to answer, such as 'Give 3 things that you are grateful for'
# The questions and answers will then be outputted to a file

### POTENTIAL ISSUES
# The 'Five-Minute Journal' is designed to be used both in the morning and at night:
# Potentially user-unfriendly. If only we knew Java/Kotlin/Swift!

### KNOWN ISSUES
# If user doesn't input M, E or B, the script will end. I want it to loop until they enter right thing.

### FEATURES FOR FUTURE VERSIONS
# Ability to track how many days in a row the script has been used, and this being printed to the user 
# Replace .txt functionality for .docx, and have some formatting like bold questions?
# Improved "recall" section in evening section. Would be great for it to know what day it is today (i.e. Thur)...
# ... and prompt you individually to recall each previous day. I.e. "Ok so today is Thur, what did you do on Wed?"...
# ... "And what did you do on Tue?" etc.

### IMPORTS
from datetime import datetime
from datetime import date
import os
import sys # for checking if user computer is Mac or PC (I'm on a Mac, I know Dan uses Windows)
import pathlib # lets you save to specific place, and has same syntax for Windows and Mac
from pathlib import Path


print(Path.home())

### OPERATING SYSTEM TEST
platform = sys.platform
if platform == 'linux':
	operating_system = 'linux'
elif platform == 'win32':
	operating_system = 'windows'
elif platform == 'cygwin':
	operating_system = 'windows'
elif platform == 'darwin':
	operating_system = 'mac'

### DECLARING VARIABLES
today = date.today()
today_time = datetime.now()
a=today_time.hour

today_date = today.strftime("%A, %d %B, %Y")
morning_prompt_1 = '\n*What are three things you are grateful for today?*'
morning_prompt_2 = '\n*What are three things that would make today great?*'
morning_prompt_3 = '\n*Time for your daily affirmation! "I am..."*'
evening_prompt_1 = '\n*What are three amazing things that happened today?*'
evening_prompt_2 = '\n*How could you have made today even better?*'
journal_prompt = '\n*Write a brief journal entry for the day!*'
recall_prompt = '\n*Give a quick summary of what you did yesterday (recall is vital for memory consolidation!)*'
recall_prompt_2 = '\n*Give a quick summary of what you did each day for the past 7 days (if you can!)*'

score_time = 0
score_recall_1 = 0
score_recall_2 = 0


### DEFINING FUNCTIONS

# morning_questions() checks existence of journal.txt and then enters questions and answers to this file 
def morning_questions():
	score_time = 0
	# Check if journal file exists
	if ((pathlib.Path.home() / 'Journal.txt').is_file()) == False:
		journal_file = open(pathlib.Path.home() / 'Journal.txt', 'w') # creates file if it doesn't exist
		journal_data_file =  open(pathlib.Path.home() / 'Journal_Data.txt', 'w') # Storing these answers in a more structured way will be useful if we want to test our memory recall

	elif ((pathlib.Path.home() / 'Journal.txt').is_file()) == True:
		journal_file = open(pathlib.Path.home() / 'Journal.txt', 'a') # reopen file in append mode so you don't overwrite previous answers
		journal_data_file = open(pathlib.Path.home() / 'Journal_Data.txt', 'a')
	print('Your answers will be saved at {}'.format(Path.home()))
	if a > 12:
		score_time = score_time + 1

	# Prompts and inputs
	print(morning_prompt_1)
	morning_answer_1 = str(input())
	# print(morning_prompt_2)
	# morning_answer_2 = str(input())m
	# print(morning_prompt_3)
	# morning_answer_3 = str(input())
	# Saving answers
	journal_file.write('Morning: ' + today_date + '\n')
	journal_file.write(morning_prompt_1 + '\n')
	journal_file.write(morning_answer_1 + '\n \n')
	# journal_file.write(morning_prompt_2 + '\n')
	# journal_file.write(morning_answer_2 + '\n \n')
	# journal_file.write(morning_prompt_3 + '\n')
	# journal_file.write(morning_answer_3 + '\n \n')
	# journal_file.close()

	# Saving answers as lines in a new .txt file
	journal_data_file.write('Morning: ' + today_date + '\n')
	journal_data_file.write(morning_answer_1 + '\n')
	# journal_data_file.write(morning_answer_2 + '\n')
	# journal_data_file.write(morning_answer_3 + '\n')
	journal_data_file.close()
	print('\nSee you this evening. Have a great day!')

	return score_time
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

### MAIN CODE	
# Greeting
print('\n[Press CTRL + C to quit at any time]')
print('\nHello!')
print('\nThe date is {}'.format(today_date))

# Determining which prompts the user wants to answer
print('\nDo you want to answer the morning prompts [M], the evening prompts [E], or both [B]?')
morn_eve_both = str(input().upper()) # Ensures uncapitalized inputs are still registered
if morn_eve_both == 'M':
	print('\nMorning prompts, sure!')
	morning_questions()
elif morn_eve_both == 'E':
	print('\nEvening prompts, sure!')
	evening_questions()
elif morn_eve_both == 'B':
	print('\nBoth, sure!')
	print('\nFirst, the morning prompts')
	morning_questions()
	print('\nNice. Now for the morning prompts')
	evening_questions()
else: 
	print('Sorry, I didn\'t understand that. Type M for morning prompts, E for evening, or B for both!')
		# need to get the loop to repeat here



print(score_time)
print("Congratulations your entry scored ",score_time," points")