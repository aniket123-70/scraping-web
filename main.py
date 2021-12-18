import smtplib
import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"

    }

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

BUY_PRICE = 200
price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
if price_as_float < BUY_PRICE:
    message = f"{below} is now {99}"

    with smtplib.SMTP("smtp.appbrewary19@gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("appbrewary19@gmail.com", "123456")
        connection.sendmail(
            from_addr="appbrewary19@gmail.com",
            to_addrs="appbrewary19@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{below}\n{https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463}"
        )

