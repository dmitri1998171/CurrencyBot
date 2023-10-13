import requests
from bs4 import BeautifulSoup

def getCurrencyRate(pair):
    url = "https://www.google.com/search?q=" + pair
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find("div", class_="BNeawe iBp4i AP7Wnd").get_text()
    result = result.replace(",", ".").split()

    return float(result[0])

if __name__ == "__main__":
    curr_rate = getCurrencyRate("usd rub")
    print(f"curr_rate: {curr_rate}")

