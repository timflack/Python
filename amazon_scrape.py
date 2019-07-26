import requests
from bs4 import BeautifulSoup
import smtplib

"""
script to check the price of an item on amazon and send an email if the price is lower than desired
"""

# Set URL of amazon item to track
URL = 'https://www.amazon.co.uk/RENPHO-Bluetooth-Bathroom-Composition-Smartphone/dp/B01N1UX8RW/ref=sr_1_2_sspa?crid=2Z01T722OV3ZJ&keywords=smart+scales&qid=1564070576&s=gateway&sprefix=smart+scal%2Caps%2C142&sr=8-2-spons&psc=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'}


def price_check():
    webpage = requests.get(URL, headers=headers)
    soup = BeautifulSoup(webpage.content, features='lxml')
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()
    price = float(price[1:6])

    if price < 25:
        send_mail()


def send_mail():
    # create server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # login
    server.login('email@gmail.com', 'password')
    sub = 'READY TO BUY'
    body = 'LINK: https://www.amazon.co.uk/RENPHO-Bluetooth-Bathroom-Composition-Smartphone/dp/B01N1UX8RW/ref=sr_1_2_sspa?crid=2Z01T722OV3ZJ&keywords=smart+scales&qid=1564070576&s=gateway&sprefix=smart+scal%2Caps%2C142&sr=8-2-spons&psc=1'

    msg = f"Subject: {sub}\n\n{body}"

    server.sendmail(
        'email@gmail.com',
        'email@gmail.com',
        msg
    )

    server.quit()


if __name__ == '__main__':
    price_check()
