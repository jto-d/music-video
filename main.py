from urllib import request
from PIL import Image
from bs4 import BeautifulSoup
import requests
import time
import random
# import pillow


def checkLink(init_link, image_tags):
    index = random.randrange(0,5)
    
    if init_link[0] == '/':
        link = image_tags[index+1]['src']
        return checkLink(link, image_tags)
    return init_link

# pick a random image out of the first 5 images and get the link
def getImage(query):

    # query to be searched
    URL = "https://www.google.com/search?q=" + query + "&rlz=1C1CHBF_enUS983US983&hl=en&tbm=isch&sxsrf=APq-WBuLfSOHmblmLB_DuKpFKoAdUarxvw:1643827311774&source=lnms&sa=X&ved=0ahUKEwiap_X31eH1AhX_kokEHSeDD00Q_AUIvw4oAQ&biw=1920&bih=969&dpr=1"

    # "get" the page from the URL
    page = requests.get(URL)

    # parse the page with bs
    soup = BeautifulSoup(page.content, 'html.parser')

    # find all images
    image_tags = soup.find_all('img')


    link = image_tags[0]['src']

    link = checkLink(link, image_tags)

    request.urlretrieve(link, "image.jpg")

    img = Image.open("image.jpg")
    img.show()
    time.sleep(1)
    img.close()


lst = ['i', 'got', 'black', 'i', 'got', 'white']

for word in lst:
    getImage(word)
