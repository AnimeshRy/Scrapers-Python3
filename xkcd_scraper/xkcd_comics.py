import requests
import os
from bs4 import BeautifulSoup
import webbrowser

url = 'https://www.xkcd.com'  # starting url
os.makedirs('xkcd', exist_ok=True)  # making a folder

# while not url.endswith('#'):
for i in range(8):

    # downloading the image
    print(f"Downloading from here... {url}")
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')

    # url elem of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print(f"Couldn't find your image")
    else:
        comicUrl = f"https:{comicElem[0].get('src')}"
        # download the image
        print('Downloading image  %s....' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # saving the image
        imagefile = open(os.path.join('xkcd',
                                      os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(100000):
            imagefile.write(chunk)
        imagefile.close()
        # webbrowser.open(url)

        # get the prev button's url
        prevlink = soup.select('a[rel="prev"]')[0]
        url = f"https://xkcd.com{prevlink.get('href')}"

    print("Done..")
