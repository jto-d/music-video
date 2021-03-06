from urllib import request
import speech_recognition as sr
import pyttsx3
from os import path
from PIL import Image
from bs4 import BeautifulSoup
import requests
import time
import random
import nltk
# import pillow

# check to see if the image link is a valid picture
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

    # open and display the image
    img = Image.open("image.jpg")
    time.sleep(1)
    img.close()


# audio file to be read
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "gettysburg10.wav")
r = sr.Recognizer()


try:

    with sr.AudioFile(AUDIO_FILE) as source:
        # filter out some background noise for a clearer transcription
        r.adjust_for_ambient_noise(source, duration=0.2)

        # "listen" to the source audio
        audio = r.listen(source)

        #use google api to transcribe audio in lowercase
        text = r.recognize_google(audio)
        text = text.lower()

        # print transcribed audio
        print(text)

except Exception as e:
    print(e)
    pass
# split transcribed audio into a list with each word
lst = text.split(' ')

# filter out small words that won't have a good transcription

# word checker
nltk.download('averaged_perceptron_tagger')
li = []

# taking input text as India
ans = nltk.pos_tag(lst)
  
# ans returns a list of tuple

  
# checking if it is a noun or not
for word in ans:
    val = word[1]
    if(val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP') or val == 'CD' or val == 'JJ':
        li.append(word[0])



for word in li:
    getImage(word)


