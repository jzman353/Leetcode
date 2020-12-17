#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
import requests, os, bs4
url = 'http://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src').strip("http://")
        comicUrl = "http://" + comicUrl
        if 'xkcd' not in comicUrl:
            comicUrl = comicUrl[:7] + 'xkcd.com/' + comicUrl[7:]

        print("comic url", comicUrl)
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    # Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')

"""
Multi-threaded
#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.
import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd
def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' % (urlNumber)) 
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)
        # Find the URL of the comic image. 
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl)) 
            res = requests.get(comicUrl)
            res.raise_for_status()
            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') 
            for chunk in res.iter_content(100000):
                imageFile.write(chunk) imageFile.close()
# Create and start the Thread objects.
downloadThreads = [] # a list of all the Thread objects for i in range(0, 1400, 100): # loops 14 times, creates 14 threads
downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99)) 
downloadThreads.append(downloadThread)
downloadThread.start()
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
"""