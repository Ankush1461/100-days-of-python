# Amazon Price Tracker

import smtplib

import requests
from bs4 import BeautifulSoup

MY_EMAIL = "my_mail@gmail.com"
MY_PASSWORD = "my_password"
SMTP_ADDRESS = "smtp.gmail.com"
BUY_PRICE = 800

url = "https://www.amazon.com/Acer-AN515-55-53E5-i5-10300H-GeForce-Keyboard/dp/B092YHJGMN/ref=sr_1_6?crid=BW7CQKZ6YKGF&keywords=acer+nitro+5+12&qid=1649775857&sprefix=acer+nitro+5+12%2Caps%2C540&sr=8-6"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())
title = soup.find(id="productTitle").get_text().strip()
print(title)

price = soup.find("span", class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
