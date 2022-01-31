"""Go to : http://myhttpheader.com/
and Accept-Language: ____
User-Agent:"""
import socket

from bs4 import BeautifulSoup
import requests
import smtplib

# MY_EMAIL = "YOUR EMAIL"
# MY_PASSWORD = "YOUR PASSWORD"

url = input("Enter the url of the product: ")
accept_language = "en-US,en;q=0.9"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)" \
			 " Chrome/92.0.4515.131 Safari/537.36"

response = requests.get(url + accept_language + user_agent)
product_url = response.text

soup = BeautifulSoup(product_url, "html.parser")

product_current_price = soup.find(name="div", class_="_30jeq3 _16Jk6d").getText()
product_original_price = soup.find(name="div", class_="_3I9_wc _2p6lqe").getText()

list_price = product_current_price.split("₹")
str_price = ''.join(str(str_price).replace(",", "") for str_price in list_price)
current_price = int(str_price)

print(f"\nOriginal price: {product_original_price}\navailable at: ₹{current_price}\n")

your_price = int(input("Enter the price when you want to buy it: ₹"))
if current_price <= your_price:
	print("Hurryyy Uppp ..! your item is available at your price")

	with smtplib.SMTP(host='smpt.gmail.com', port=587) as connection:
		connection.starttls()
		result = connection.login("YOUR_GMAIL", "YOUR_GMAIL_PASSWORD")
		connection.sendmail(
			from_addr="thakerniramay@gmai.com",
			to_addrs="thakerniramay@gmai.com",
			msg=f"Hurryyy Uppp ..! your item is available at your price\n₹{your_price}"
		)
