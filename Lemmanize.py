
import string
import nltk
import spacy

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.util import ngrams


nlp = spacy.load("en_core_web_sm")

text = "I wake up everyday to go to university. My journey is still long and my age increased every year. Relentless and sorrowness gone depth into myself until I find it hard to find  a way to be a person who I want to be. I always tried something new that I never done before but it always ended up failing. I tried to rise up but I have no one to hold my hands but rather I go alone with my journey that I want to reach the pinnacle. Success is not easy but rather it is how you journey lead to success"



print("\n=============")
print("1. Original text")
print("===============")
print(text)

#Tokenisation
tokens = word_tokenize(text)

print("\n==========")
print("2. Original token")
print("==========")
print(tokens)

#Case folding
lowercase_token = [token.lower() for token in tokens]

print("\n=========")
print("3. Case-folded token")
print("==========")
print(lowercase_token)

#Punctuation removal
clean_tokens = [
    token
    for token in lowercase_token
    if token not in string.punctuation
]

print("\n=========")
print("4. Tokens after punctutation removal")
print("==========")
print(clean_tokens) 

#Stop-word removal
english_stopwords = set(stopwords.words("english"))

filtered_tokens = [
    token
    for token in clean_tokens
    if token not in english_stopwords
]

print("\n=========")
print("5. Tokens after stop-word removal")
print("==========")
print(filtered_tokens)

#Stemming
stemmer = PorterStemmer()

stemmed_tokens = [
    stemmer.stem(token)
    for token in filtered_tokens
]

print("\n=========")
print("6. Stemmed tokens")
print("=========")
print(stemmed_tokens)


#Lemmatization
doc = nlp(text)

lemmatized_tokens = [
    token.lemma_.lower()
    for token in doc
    if not token.is_stop
    and not token.is_punct
    and not token.is_space
]

print("\n===========")
print("7. Lemmatized tokens")
print("==========")
print(lemmatized_tokens)

#Vocabulary constructions
vocabulary = sorted(set(lemmatized_tokens))

print("\n=========")
print("8. Vocabulary")
print("=========")
print(vocabulary)

#N-Gram generation
bigrams = list(ngrams(lemmatized_tokens, 2))
print("\n=========")
print("9. Bigrams")
print("=========")

for bigram in bigrams:
    print(bigram)

print("\nText preprocessing completed successfully.")