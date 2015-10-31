# reddit-BreedingDittos-giveaway-email-bot
Searches /r/BreedingDIttos for new giveaways and sends an email containing a URL to it so you don't have to keep refreshing the page all the time. Replace your.email@domain.com, "your username", etc. with the appropriate information before running.

SSMTPLib can be found [here](http://www1.cs.columbia.edu/~db2501/ssmtplib.py).
Credit to http://stackoverflow.com/a/64890/3534220 for the email-sending code.

NOTE: Program as it is must be run manually whenever you want to check for new posts. Not exactly a step up from just refreshing the page. Refer [here](http://pythonforengineers.com/build-a-reddit-bot-part-3-automate-your-bot/) for automation. `cd /path/to/script/foo/; ./script.py` can be replaced with simply `python /path/to/script/foo/script.py`. Additionally, as the tutorial states, the script will execute once every minute. If you feel this is too frequent (it likely is, considering how rarely giveaways on the subreddit occur, you can replace `* * * * * python /path/to/script/foo/script.py` with `00 * * * * python /path/to/script/foo/script.py` to run it once every hour, or `00,30 * * * * python /path/to/script/foo/script.py` to run it twice an hour. See [here](http://www.thegeekstuff.com/2009/06/15-practical-crontab-examples/) for more details and examples.
