import requests
from bs4 import BeautifulSoup
import webbrowser
import os
import sys

"""Downloading images from imgur from the terminal"""

# make a folder
os.makedirs('imgurdownloader', exist_ok=True)

query = input('Search imgur here: ')

url = f'https://imgur.com/search?q={query}'
try:
    source = requests.get(url)
    source.raise_for_status()
    # webbrowser.open(url)

    soup = BeautifulSoup(source.text, 'html.parser')
    anchors = soup.select('.image-list-link img')
    # iterate over all the anchor tags on the page and get the src attribute to download the image
    for item in anchors[:10]:
        image = item.get('src')
        imageurl = f'https:{image}'
        print(f'Downloading image from {imageurl}')
        imageobj = requests.get(imageurl)

        imageobj.raise_for_status()

        imagefile = open(os.path.join('imgurdownloader',
                                      os.path.basename(imageurl)), 'wb')

        for chunk in imageobj.iter_content(100000):
            imagefile.write(chunk)
        imagefile.close()

except Exception as e:
    print('Sorry some error occured while downloading')

print('\nDownload is complete', end='')
