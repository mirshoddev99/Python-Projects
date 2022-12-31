import smtplib
from email.mime.text import MIMEText
from my_api import print_data
import datetime

SENDER = 'mirshodpnu22@gmail.com'
PASSWORD = 'obypzyiavxjkkddp'
RECEIVER = 'oripovmirshod9@gmail.com'
today = datetime.datetime.now()
now = f"{today.hour}:{today.minute}"


def sending_email(receiver, country):
    # Create the email message
    data = print_data(country)
    msg = MIMEText(f"\tIt is time {now} in South Korea~ \n{data[0]}")
    msg["Subject"] = f"The Weather forecast in {data[2]}, {data[1]}"
    msg["From"] = f"{SENDER}"
    msg["To"] = f"{RECEIVER}"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER, PASSWORD)
        print("Logged in...")
        server.sendmail(SENDER, receiver, msg.as_string())
        print("Email has been sent successfully!")

    except AttributeError:
        print("Failed")
