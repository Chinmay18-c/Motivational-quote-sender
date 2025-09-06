import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

now = dt.datetime.now()
week_day = now.weekday()


if week_day in [0,1,2,3]:
    with open("quotes.txt", encoding="utf-8") as quotes:
        quotes_list = quotes.readlines()
        random_quote = random.choice(quotes_list).strip()

    my_email = "jainchinmay2005@gmail.com"
    with open("password.env") as f:
        password=f.read().strip()

    to_email = "jainchinmay18@yahoo.com"

    msg = MIMEMultipart()
    msg["From"] = my_email
    msg["To"] = to_email
    msg["Subject"] = "Motivation Quote of the Day"

    body = f"Here's your motivational quote for today:\n\n{random_quote}"
    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=msg.as_string())
