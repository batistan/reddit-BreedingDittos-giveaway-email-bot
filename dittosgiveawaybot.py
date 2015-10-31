import ssmtplib
import praw

user_agent = ("Breeding Dittos Giveaway Alerter, by soroun")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("BreedingDittos")

insts = []

for submission in subreddit.get_new():
    if ("[Giveaway]" in submission.title) or ("[GIVEAWAY]" in submission.title) or ("[giveaway]" in submission.title):
        insts.append(submission.title + ": " + submission.url) 

if not insts: # empty lists are false. `not insts` will return true if it insts contains at least one entry
    SMTPserver = 'Your SMTP server'
    sender = 'your.email@yourdomain.com'
    destination = ['recipient.email@recipientdomain.com']

    USERNAME = "your username to log on to server"
    PASSWORD = "your password"

    text_subtype = 'plain'

    content = '\n'.join(insts).encode('utf-8').strip()

    subject = "New giveaway on /r/BreedingDittos!"

    import sys
    import os
    import re

    from smtplib import SMTP_SSL as SMTP
    from email.MIMEText import MIMEText

    try:
        msg = MIMEText(content, text_subtype)
        msg['Subject'] = subject
        msg['From'] = sender

        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(USERNAME, PASSWORD)

        try:
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.close()

    except Exception, exc:
        sys.exit("Sending failed. %s" % str(exc))
