import requests
from bs4 import BeautifulSoup


HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://sullygnome.com/channel/lirik',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Content-Type': 'application/json; charset=utf-8'
}

print('\nВыполнение задания\n')

payload = {'q': 'pool', 'start': '0', 'num': '10'}
request = requests.get('https://google.com/search', headers=HEADERS, params=payload)
soup = BeautifulSoup(request.text, 'html.parser')

hints = soup.find("div", id="bres").find_all("a")

print('Подсказки:')
for item in hints:
    print(item.find_all("div")[1].contents)

links = soup.find_all("div", class_="g")

print('Ссылки:')
for item in links:
    print(item.find("a")['href'])

exit(0)
