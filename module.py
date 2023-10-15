import requests
from bs4 import BeautifulSoup

def strInsert(source_str, insert_str, pos):
    return source_str[:pos] + insert_str + source_str[pos:]

def currencyPairsLoader():
    pairs = []

    with open("currencyPairs.txt", 'r') as f:
        while True:
            line = f.readline()

            if not line:
                break

            line = line[:len(line) - 1]
            pairs.append(line)

    return pairs

pairs = currencyPairsLoader()

def checkFormat(_pair):
    if(_pair[3] != '/'):
       _pair = strInsert(_pair, '/', 3)

    _pair = _pair.replace(' ', '/').replace('\\', '/')
    return _pair.upper()

def currencyPairValidation(_pair):
    global pairs

    if(len(_pair) > 7):
        return False
    
    _pair = checkFormat(_pair)

    for pair in pairs:
        if (pair == _pair):
            return True

    return False

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

