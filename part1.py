from urllib import request
from nltk import *
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer

## reads context of the website
url = 'https://www.theguardian.com/music/2018/oct/19/while-my-guitar-gently-weeps-beatles-george-harrison'
response = request.urlopen(url)
webContent = response.read().decode('utf8')

## Pulls out the unique data from the website using beautiful soup
soup = BeautifulSoup(webContent, 'html5lib')
removeTags = soup.find('article').getText()
tokenised_content = sorted([word for word in word_tokenize(removeTags) if re.search("\w", word)])
uniqueWords = unique_list(tokenised_content)

## Number of types and tokens before lemmatization
print('This text contains {} types before lemmatization:'.format(len(uniqueWords)))
print('\n\n')
print('This text contains {} tokens before lemmatization:'.format(len(tokenised_content)))
print('\n\n')

## Lemmatization 
lemmatizer = stem.WordNetLemmatizer()
lemmatized_tokens = sorted([lemmatizer.lemmatize(w.lower()) for w in tokenised_content])
lemmatized_types = unique_list(lemmatized_tokens)

## Number of types and token after lemmatization
print('This text contains {} types after lemmatization:'.format(len(lemmatized_types)))
print('\n\n')
print('This text contains {} tokens after lemmatization:'.format(len(lemmatized_tokens)))
print('\n\n')


## POS tagging method for tokens 
posTagging = pos_tag(tokenised_content)
for pos in posTagging:
    print("POS for tokens: ", pos)

## POS tagging method for types 
posTagging = pos_tag(uniqueWords)
for pos in posTagging:
    print("POS for types: ", pos)

