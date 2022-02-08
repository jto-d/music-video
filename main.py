from urllib import request
from PIL import Image
from bs4 import BeautifulSoup
import requests
import time
import random
# import pillow


def checkLink(init_link, image_tags):
    index = random.randrange(0,20)
    
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
    time.sleep(1)
    img.close()

getImage('banana')

# def convert(lst):
#     return (lst[0].split())

# def get_lyrics():

#     artist = input("Enter artist name (no spaces):")
#     title = input("Enter song name (no spaces)")
#     URL = "https://www.azlyrics.com/lyrics/" + artist + "/" + title + ".html"
#     page = requests.get(URL)
#     soup = BeautifulSoup(page.content, 'html.parser')

#     lyrics = soup.find_all('div', class_="col-xs-12 col-lg-8 text-center")
#     lyrics = lyrics[0].find_all('div')[5].text
    
#     # Driver code
#     lst =  [lyrics]

#     lst = convert(lst)
#     signal = True
#     final = []
#     for el in lst:
#         if '(' not in el and signal and '[' not in el:
#             final.append(el)
#         elif '(' in el and signal:
#             signal = False
#         elif ')' in el:
#             signal=True
#     return final

# lst = get_lyrics()
# print(lst)

# for word in lst:
#     getImage(word)
