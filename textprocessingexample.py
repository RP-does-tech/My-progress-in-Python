"""

This script demonstrates a basic text-processing pipeline:

1. Raw text
2. Tokenisation
3. Case folding
4. Punctuation removal
5. Stop-word removal
6. Stemming
7. Lemmatization
8. Vocabulary construction
9. N-gram generation

Required packages:
    pip install nltk spacy
    python -m spacy download en_core_web_sm

Note:
The first time you use NLTK stop words or tokenization,
the script may download the required resources.
"""

# ============================================================
# STAGE 0: IMPORT REQUIRED LIBRARIES
# ============================================================

import string
import nltk
import spacy

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.util import ngrams


# ============================================================
# STAGE 1: DOWNLOAD REQUIRED NLTK RESOURCES
# ============================================================

# These downloads are needed only the first time.
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


# ============================================================
# STAGE 2: LOAD THE spaCy ENGLISH MODEL
# ============================================================

# The spaCy model is used later for lemmatization.
nlp = spacy.load("en_core_web_sm")


# ============================================================
# STAGE 3: DEFINE THE RAW TEXT
# ============================================================

# This is the original document before preprocessing.
text = """
Consistency is the foundation of strong habits because small actions repeated regularly can 
gradually shape a person’s character and way of life. In Islam, 
believers are encouraged to remain consistent in good deeds, even when those deeds are simple. 
Regular prayer, daily Qur’an reading, helping others, speaking kindly, giving charity, and 
remembering Allah can become natural habits when practised continuously. 
A person may begin with a small effort, but repeating it every day builds discipline and 
makes the action easier over time. This teaches us that meaningful change does not always come 
from doing something large once; it often comes from doing something good consistently.
"""

print("\n==============================")
print("1. ORIGINAL TEXT")
print("==============================")
print(text)


# ============================================================
# STAGE 4: TOKENISATION
# ============================================================

# Tokenisation splits the text into smaller units called tokens.
# Tokens may include words and punctuation marks.

tokens = word_tokenize(text)

print("\n==============================")
print("2. ORIGINAL TOKENS")
print("==============================")
print(tokens)


# ============================================================
# STAGE 5: CASE FOLDING
# ============================================================

# Case folding converts all words to lowercase.
# This helps treat words such as:
# "Information", "information", and "INFORMATION"
# as the same term.

lowercase_tokens = [token.lower() for token in tokens]

print("\n==============================")
print("3. CASE-FOLDED TOKENS")
print("==============================")
print(lowercase_tokens)


# ============================================================
# STAGE 6: PUNCTUATION REMOVAL
# ============================================================

# Punctuation marks such as commas and full stops
# are usually not useful as searchable terms.

clean_tokens = [
    token
    for token in lowercase_tokens
    if token not in string.punctuation
]

print("\n==============================")
print("4. TOKENS AFTER PUNCTUATION REMOVAL")
print("==============================")
print(clean_tokens)


# ============================================================
# STAGE 7: STOP-WORD REMOVAL
# ============================================================

# Stop words are very common words such as:
# "the", "is", "are", "and", "for".
# In many IR tasks, they may be removed because
# they carry less retrieval value.

english_stopwords = set(stopwords.words("english"))

filtered_tokens = [
    token
    for token in clean_tokens
    if token not in english_stopwords
]

print("\n==============================")
print("5. TOKENS AFTER STOP-WORD REMOVAL")
print("==============================")
print(filtered_tokens)


# ============================================================
# STAGE 8: STEMMING
# ============================================================

# Stemming reduces words to a shortened root-like form.
# The result is not always a correct dictionary word.
#
# Examples:
# searching -> search
# retrieval -> retriev
# different -> differ

stemmer = PorterStemmer()

stemmed_tokens = [
    stemmer.stem(token)
    for token in filtered_tokens
]

print("\n==============================")
print("6. STEMMED TOKENS")
print("==============================")
print(stemmed_tokens)


# ============================================================
# STAGE 9: LEMMATIZATION
# ============================================================

# Lemmatization reduces a word to its meaningful base form.
# Unlike stemming, it tries to return a valid dictionary form.
#
# Examples:
# students -> student
# searching -> search
# systems -> system

doc = nlp(text)

lemmatized_tokens = [
    token.lemma_.lower()
    for token in doc
    if not token.is_stop
    and not token.is_punct
    and not token.is_space
]

print("\n==============================")
print("7. LEMMATIZED TOKENS")
print("==============================")
print(lemmatized_tokens)


# ============================================================
# STAGE 10: VOCABULARY CONSTRUCTION
# ============================================================

# A vocabulary is the set of unique terms
# found in the processed document collection.

vocabulary = sorted(set(lemmatized_tokens))

print("\n==============================")
print("8. VOCABULARY")
print("==============================")
print(vocabulary)

print("\nVocabulary size:", len(vocabulary))


# ============================================================
# STAGE 11: N-GRAM GENERATION
# ============================================================

# An n-gram is a sequence of n consecutive terms.
#
# Unigram = one term
# Bigram  = two consecutive terms
# Trigram = three consecutive terms
#
# Here we generate bigrams.

bigrams = list(ngrams(lemmatized_tokens, 2))

print("\n==============================")
print("9. BIGRAMS")
print("==============================")

for bigram in bigrams:
    print(bigram)


print("\nText preprocessing completed successfully.")
