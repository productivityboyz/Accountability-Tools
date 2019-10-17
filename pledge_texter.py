# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

print('What are your pledges for this week?')
user_pledges = str(input())

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC9a17dd2a160a15c4b5ad4db719e0f4d1' # good to make these secret
auth_token = '4d645e040cc08e6bf6997a4b0e0a2e54' # use environment variables to make secret!
client = Client(account_sid, auth_token)

# Want to get it to send me a text every day at 8am

message = client.messages \
    .create(
         body='Hello! You pledged the following this week: {}'.format(user_pledges),
         from_='+16193562670',
         to='+447397854011'
     )

print(message.sid)