import re
from urllib import request
from nltk import *
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer

## to test it works: https://www.enherts-tr.nhs.uk/our-hospitals/lister/visiting-times/
## Reads the URL of a webpage and extracts unique data  
url = input("Enter the URL for website: ")
response = request.urlopen(url)
webContent = response.read().decode('utf8')
## Web scraping
soup = BeautifulSoup(webContent, 'html5lib')
for s in soup(['script', 'style']):
    s.decompose()
for tag in soup.findAll(True):
    tag.unwrap()
removeTags = soup.get_text().strip().lower()


## Finds the regular expression for telephone numbers
regEx = re.findall('\+?\d{2,5}\s?\d{2,6}?\s?\d{2,8}', removeTags)

if len(regEx)>0:
    print("Found a match!")
    for num in regEx:
        print(num)
else:
    print("There are no numbers on this website.")

