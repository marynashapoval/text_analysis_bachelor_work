from bs4 import BeautifulSoup
from selenium import webdriver



words = input().splitlines()

for word in words:
    url = 'https://slovnyk.ua/index.php?swrd=' + str(word.encode('utf-8'))
    browser = webdriver.PhantomJS()
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')

    print(soup)
    for paragraph in soup.find_all('td'):
        result += paragraph.text + ' '
   