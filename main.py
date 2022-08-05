from bs4 import BeautifulSoup
import requests
from decouple import config
import smtplib

URL = "https://www.amazon.com/-/Pantalla-plana-pulgadas-Roku-Smart/dp/B07DCDNHZQ/ref=sr_1_2?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&amp&crid=326VJVHZDLZPQ&amp&keywords=smart+tv&amp&qid=1655957160&amp&sprefix=smart+t,aps,137&amp&sr=8-2&language=en_US&currency=USD"
USER_AGENT = config("USER_AGENT")
ACCEPT_LANGUAGE = config("ACCEPT_LANGUAGE")
EMAIL = config("email")
PASSWORD = config("password")

http_headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

response = requests.get(URL, headers=http_headers).text
soup = BeautifulSoup(response, "html.parser")

price_span = soup.select_one("span .a-offscreen")
price = float(price_span.getText()[1:])

title = soup.title.getText()

if price < 150:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs="axnunezc@gmail.com", msg="Subject:Low Price Alert!\n\n{title} is now {price}!\nBuy at {URL}")
