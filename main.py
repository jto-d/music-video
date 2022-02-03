from urllib import request
from bs4 import BeautifulSoup
import requests
import random

# query to be searched
query = "yellow"
URL = "https://www.google.com/search?q=" + query + "&rlz=1C1CHBF_enUS983US983&hl=en&tbm=isch&sxsrf=APq-WBuLfSOHmblmLB_DuKpFKoAdUarxvw:1643827311774&source=lnms&sa=X&ved=0ahUKEwiap_X31eH1AhX_kokEHSeDD00Q_AUIvw4oAQ&biw=1920&bih=969&dpr=1"

# "get" the page from the URL
page = requests.get(URL)

# parse the page with bs
soup = BeautifulSoup(page.content, 'html.parser')

# find all images
image_tags = soup.find_all('img')

# pick a random image out of the first 5 images and get the link
index = random.randrange(0,5)
link = image_tags[index]['src']
print(link)
