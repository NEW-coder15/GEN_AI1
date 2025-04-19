#Tokens
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
sample_text = 'I love programming!'
tokens = word_tokenize(sample_text)

print('Tokens:', tokens)

#N-Grams
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
sentence="I am learning AI"
token=word_tokenize(sentence)
# Unigram
unigrams = list(ngrams(tokens, 1))
print('Unigrams:', unigrams)

# Bigram
bigrams = list(ngrams(tokens, 2))
print('Bigrams:', bigrams)

# Trigram
trigrams = list(ngrams(tokens, 3))
print('Trigrams:', trigrams)