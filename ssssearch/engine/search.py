import requests
from bs4 import BeautifulSoup


def duck(search):
    links = []
    text = []
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    headers = {'user-agent': userAgent}
    r = requests.get('https://duckduckgo.com/html/?q=' + search, headers=headers)
    s = BeautifulSoup(r.content, "html.parser")
    for i in s.find_all('div', attrs={'class': 'results_links_deep'}):
        a = i.find('a', attrs={'class': 'result__a'})
        links.append(a.get('href'))
        text.append(a.text)
    links.pop(0)
    text.pop(0)
    return links, text