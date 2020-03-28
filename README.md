# NaturalLanguageProcessing
Probabilties, Regular Expressions and Language Models

Task 1: The program reads the text from the following website "https://www.theguardian.com/music/2018/oct/19/while-my-guitar-gently-weeps-beatles-george-harrison" and identifies all the types and token before and after lowercasing and lemmatising. NLTK functions are used to perform these tasks, from the url reader to the tokenizer and lemmatizer. Part-of-speech tags are assigned to all tokens in the text. 
The errors detected with POS tagging are as follows: 
POS tagging is not always assigned to correct tags to words. The reason behind this inaccuracy is ambiguity. POS tagging algorithms use the probability that the word is a tag type but they also use the surrounding sentence context to predict. However, It is not always easy to understand context. So the more words, the more likely it is to be accurate. 
There have been quite a few tagging errors in the sentences of the given website. 
For instance, the word “spicy” is tagged as NN which refers to noun, singular or mass but in the article it’s an adjective (JJ). An adjective is a word that describes a noun. The word “spicy” is describing the food – “he didn’t want to eat spicy food”.
Also, the word “set” is tagged as a VBN which is a verb, past participle in the POS tagging format. In the article, the word “set” refers to a noun, a group or collection of things that belong together - “… to be included in remastered White Album set”.
Similarly, the word “mic” is given the tag of JJ (adjective) but in the article it is a noun – “…give him his own mic”. 

Task 2: 
A regular expression was written to find all telephone numbers in a text. It is able to deal with different formats, for example +55 51 33083838, 1206 872020, 01206 872020 and 05679401945 as well as +44 5679401945 and 0044 5679401945. It applies to any url specified by the user, reads it and finds the telephone numbers. From that, FSA was derived. 

Task 3: 
Using the Toy dataset, a unigram model was computed. Computing the probabilities in a unigram language model without smoothing. Showing work for P(a), P(c), P(UNK). 
Using the Toy dataset, bigram model was computed. Computed the probabilities in a bigram language model without smoothing. Showing work for P(b|a), P(UNK| <s>), P(UNK|UNK). Smooth the model using Laplace smoothing. Showing work for P(b|a), P(UNK| <s>), P(UNK|UNK).


