from PyLyrics import *

albums = PyLyrics.getAlbums(singer='Eminem')
myalbum = albums[4] #Select your album based on Index

tracks = myalbum.tracks() #or PyLyrics.getTracks(myalbum)