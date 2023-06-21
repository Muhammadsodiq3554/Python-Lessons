import requests
from bs4 import BeautifulSoup

url = "https://gov.uz/oz/pages/population"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

full_page = requests.get(url, headers=headers)


soup = BeautifulSoup(full_page.content, 'html.parser')


natija = soup.findAll('div', {'class': 'text_justify', 'id': "speechArea"})

print(natija[0].text)