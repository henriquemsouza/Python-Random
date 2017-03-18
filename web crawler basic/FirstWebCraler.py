import requests, shutil
# pip install beautifulsoup4
from bs4 import BeautifulSoup



def trader_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://thenewboston.com/search.php?type=0&sort=reputation&page==' + str(page)
        source_code = requests.get(url, allow_redirects=False)
        plain_text = source_code.text.encode('ascii', 'replace')
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.find_all('a', {'class': 'user-name'}):
            href = link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1


def get_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text #.encode('ascii', 'replace')
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.findAll('img', {'class': 'img-responsive'}):  # all photos of the user
        photo = item_url + item_name.get('src')
        print("photho "+photo)
    else:
        print("nada encontrado")
    for link in soup.findAll('a'):
        href = link.get('href')
        print("Href "+href)
    else:
        print("nada encontrado")

columns = shutil.get_terminal_size().columns
url = input("\nPlease enter url\n".center(columns))
get_data(url)
# trader_spider(1)
#all working
