import nltk
from nltk.probability import *
import re
from nltk.util import ngrams
from nltk.lm import MLE
from nltk.lm.preprocessing import padded_everygram_pipeline

# Opens and reads the given file 
file = open("sampledata.vocab.txt", "r")
vocab_file = file.readlines()
vocab_file = [lines.strip() for lines in vocab_file]
file.close()

mapping = nltk.defaultdict(lambda: 'UNK')
for v in vocab_file:
    mapping[v] = v

## Opens the sample data textfile and reads it, finds the <s> and </s> tags and removes them
sampleDataFile = open("sampledata.txt", "r")
sampleData = sampleDataFile.readlines()
sampleDataFile.close()
sampleData = re.findall('(\S+)\s*',' '.join(sampleData)) ##removes /n
sampleData = [lines for lines in sampleData if lines != '<s>' and lines != '</s>'] ## removes <s> tags
sampleData = [mapping[lines] for lines in sampleData]


## Unigram calculations
freq = FreqDist(sampleData)
unsmoothed = MLEProbDist(freq) ## MLE probability distribution 
smoothed = LaplaceProbDist(freq) ## Leplace probability distribution

## Prints the results of the unigram model 
print ("---------------- Toy dataset ----------------")
print ("=== UNIGRAM MODEL ===")
print('- Unsmoothed -')
strToPrint=""
for x in unsmoothed.samples():
    strToPrint += ('{0:5}{1:3}{2:.2}    '.format(str(x), ":", unsmoothed.prob(x)))
print(strToPrint)
strToPrint = ""
print('- Smoothed -')
for x in smoothed.samples():
    strToPrint +=  ('{0:5}{1:3}{2:.2}    '.format(str(x), ":", smoothed.prob(x)))
print(strToPrint)

print ()

## Bigram calculations
mapping = nltk.defaultdict(lambda: 'UNK')
for v in vocab_file:
    mapping[v] = v

vocab_freq = {}
matrix = []
for char in vocab_file:
    vocab_freq[char] = 0
    for char2 in vocab_file:
        matrix.append((char, char2))
vocab_dict = {}
for pair in matrix:
    vocab_dict[pair] = 0
    

sampleDataFile = open("sampledata.txt", "r")
sampleData = sampleDataFile.readlines()
sampleDataFile.close()
sampleData = re.findall('(\S+)\s*',' '.join(sampleData)) ##removes /n
for i in range(0,len(sampleData)):
    sampleData[i]=sampleData[i].strip("\n")
words=[]
for element in sampleData:
    temp=element.split(" ")
    for word in temp:
        words.append(word)
    
#words = sampleData.split(" ")
for word in words:
    if word in vocab_file:
        vocab_freq[word]+=1  
bigrams = [lines for lines in ngrams(words,2)]

print("=== BIGRAM MODEL ===")
print("- Unsmoothed -")

all = []
for x in [e.split() for e in sampleData]:
    words = all.extend(x)
token = set(all)

def top(bi_lst, w1, w2):
	count = 0;
	for m, n in bi_lst:
		if m == w1 and n == w2:
			count += 1;
	return count 
    
def denominator(bi_lst, w):
	count = 0
	for _, n in bi_lst:
		if n == w:
			count += 1
	return count 


def table(wd, bi_lst):
    for w1 in wd:
        print('{0}'.format(w1), end='')
        for w2 in wd:
            p = top(bi_lst, w1, w2)/denominator(bi_lst, w1)
            print('{0:10.2}'.format(p), end='')
        print()
    print()

lst = sorted(list(token))
print('        ', end='')
for e in lst:
    print('{0:11}'.format(e), end='')
print()

table(sorted(list(token)), bigrams)

print("- smoothed -")

all = []
for x in [e.split() for e in sampleData]:
    words = all.extend(x)
token = set(all)

def top(bi_lst, w1, w2):
	count = 0;
	for m, n in bi_lst:
		if m == w1 and n == w2:
			count += 1;
	return count + 1
    
def denominator(bi_lst, w):
	count = 0
	for _, n in bi_lst:
		if n == w:
			count += 1
	return count + len(vocab_file)

def table(wd, bi_lst):
    for w1 in wd:
        print('{0}'.format(w1), end='')
        for w2 in wd:
            p = top(bi_lst, w1, w2)/denominator(bi_lst, w1)
            print('{0:10.2}'.format(p), end='')
        print()
    print()

lst = sorted(list(token))
print('        ', end='')
for e in lst:
    print('{0:11}'.format(e), end='')
print()

table(sorted(list(token)), bigrams)



