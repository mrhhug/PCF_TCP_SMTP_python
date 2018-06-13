#import smtplib

#sender = 'twhiteley@fiserv.com'
#receivers = ['twhiteley@fiserv.com']

#message = """From: From Person <from@fromdomain.com>
#To: To Person <to@todomain.com>
#Subject: SMTP e-mail test

#This is a test e-mail message.
#"""

#try:
#   smtpObj = smtplib.SMTP(host='tcp.cloudfoundry.onefiserv.net', port=60000)
#   smtpObj.sendmail(sender, receivers, message)         
#   print("Successfully sent email")
#except:
#   print("Error: unable to send email")
   
   
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

michael = "michael.hug@fiserv.com"
#sender = 'twhiteley@fiserv.com'
#receivers = ['twhiteley@fiserv.com']
receivers = michael
sender = michael

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
# with open(textfile, 'rb') as fp:
# Create a text/plain message
msg = MIMEText('some message from me')

msg['Subject'] = 'This is the subject line of my special email'
msg['From'] = sender
msg['To'] = receivers

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP(host='tcp.cloudfoundry.onefiserv.net', port=60008)
s.sendmail(sender, receivers, msg.as_string())
s.quit()
