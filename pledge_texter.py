# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import schedule
import time

### Define pledges
print('What are your pledges for this week?')
user_pledges = str(input())

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC9a17dd2a160a15c4b5ad4db719e0f4d1' # good to make these secret
auth_token = '4d645e040cc08e6bf6997a4b0e0a2e54' # use environment variables to make secret!
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

schedule.every().day.at("15:48").do(text_me)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute