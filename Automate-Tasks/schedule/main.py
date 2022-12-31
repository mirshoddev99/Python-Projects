import schedule
import time
from sending_email import *


schedule.every().day.at("21:00").do(sending_email, receiver=RECEIVER, country="bukhara/uzbekistan")
schedule.every().day.at("06:00").do(sending_email, receiver=RECEIVER, country="bukhara/uzbekistan")

while True:
    schedule.run_pending()
    time.sleep(1)
