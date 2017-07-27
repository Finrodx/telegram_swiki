


"""
import urllib
from bs4 import BeautifulSoup


if tr-en or en-tr
    get searched words
        r = urllib.urlopen('http://tureng.com/en/turkish-english/"searched words" ').read()
        soup = BeautifulSoup(r)
        if selection== en-tr

                  letters = soup.find_all("div", class_="tr ts")

        elif selection ==tr-en

                letters = soup.find_all("div", class="en tm"


"""