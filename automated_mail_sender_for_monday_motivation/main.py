import datetime as dt
import random
import smtplib

MY_EMAIL = "xyz@gmail.com"  # Enter your gmail account
MY_PASSWORD = "$*#8"   # Enter your password
SEND_TO = "abc@gmail.com"   # Enter Account of person you want to send

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:  # Will set up the connection
        connection.starttls()   # tls is for  encrypting, TLS = Transport Layer Security
        connection.login(MY_EMAIL, MY_PASSWORD)  
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=SEND_TO,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
