# Download the helper library from https://www.twilio.com/docs/python/install
import twilio.rest
from twilio.rest import Client
import schedule
import time
import os 
### Define pledges
print('What are your pledges for this week?')
user_pledges = str(input())

### Account SID and Auth Token (keeping them secure)
# This doesn't work. Need to go over how to make environment variables again!
account_sid = os.getenv('TWILIO_ACCOUNT_SID') # THIS IS ALWAYS 'NONE', making it fail! :( 
print(account_sid)
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
print(auth_token)
client = Client(account_sid, auth_token)

### schedule module code
# from here https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day
def text_me():
    message = client.messages \
        .create(
            body='Hello! You pledged the following this week: {}'.format(user_pledges),
            from_='+16193562670',
            to='+447397854011'
        )

schedule.every().day.at("19:54").do(text_me)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute