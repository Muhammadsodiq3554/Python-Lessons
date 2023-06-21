# import requests
# user = str(input("So'z kiriting: "))

# url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
# try:

#     payload = {
# 	    "q": f"{user}",
# 	    "target": "en",
# 	    "source": "uz"
#     }
#     headers = {
#         "content-type": "application/x-www-form-urlencoded",
#         "Accept-Encoding": "application/gzip",
#         "X-RapidAPI-Key": "a2b69e7f24msh2a8eba385bff20ep1d749cjsn4569bc2ed3f5",
#         "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
#     }

#     response = requests.post(url, data=payload, headers=headers)

#     natija = (response.json())['data']['translations'][0]['translatedText']

#     print(natija)
# except:
#     print("Siz so'z kiritishda xato qildingiz.")

#----------------------------------------------------------------------------------------------------------#

import requests
from bs4 import BeautifulSoup

DOLLAR_UZS = "https://www.google.com/search?q=usd+to+uzs&sxsrf=APwXEdeB5hw44fF3m_mqc3Qlf6prYkDoHw%3A1686829347459&ei=I_mKZJfXG4OJrwT-j6GACw&ved=0ahUKEwjX9LSAmcX_AhWDxIsKHf5HCLAQ4dUDCBA&uact=5&oq=usd+to+uzs&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQigUQsAMQQzIKCAAQigUQsAMQQ0oECEEYAFAAWABg9QdoAXABeACAAQCIAQCSAQCYAQDAAQHIAQo&sclient=gws-wiz-serp"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

full_page = requests.get(DOLLAR_UZS, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

natija = soup.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision': "2"})
print(natija[1].text)