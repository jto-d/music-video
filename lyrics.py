from bs4 import BeautifulSoup
import requests


artist = input("Enter artist name (no spaces):")
title = input("Enter song name (no spaces)")
URL = "https://www.azlyrics.com/lyrics/" + artist + "/" + title + ".html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


lyrics = soup.find_all('div', class_="col-xs-12 col-lg-8 text-center")
lyrics = lyrics[0].find_all('div')[5].text

def convert(lst):
    return (lst[0].split())
 
# Driver code
lst =  [lyrics]

lst = convert(lst)
signal = True
final = []
for el in lst:
    if '(' not in el and signal and '[' not in el:
        final.append(el)
    elif '(' in el and signal:
        signal = False
    elif ')' in el:
        signal=True



print(final)


#print(soup.prettify())