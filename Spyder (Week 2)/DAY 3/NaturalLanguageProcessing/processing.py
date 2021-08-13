import requests
from bs4 import BeautifulSoup
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

nintendo_wiki = 'https://en.wikipedia.org/wiki/Nintendo'
page = requests.get(nintendo_wiki)
 
soup = BeautifulSoup(page.text, 'html.parser')
text = soup.get_text(separator = ' ', strip = True)

clean_text = text.lower()

table = str.maketrans('', '', string.punctuation)
clean_text = clean_text.translate(table)
 
words = clean_text.split()

'''
clean_words = []

clean_words = list(filter(lambda word: word not in stopwords.words('english'), words))
        
freq = nltk.FreqDist(clean_words)
freq.plot(20, title = 'Frequency Distribution')
'''

sentences = sent_tokenize(text)
 
sentence_words = sentences[6].split()
first_sentence = ' '.join(sentence_words[-18:])

nltk_words = word_tokenize(text)
 
french_text = "Bonjour M. Adam, comment allez-vous? J'espère que tout va bien. Aujourd'hui est un bon jour."
french_sentences = sent_tokenize(french_text,"french")

'''
syn = wordnet.synsets('boy')

print('Name: ', syn[1].name())
print('\nDefinition: ', syn[1].definition())
print('\nExamples: ', syn[1].examples())


antonyms = []
 
for syn in wordnet.synsets('small'):
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())
 
print(antonyms)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
 
print('Stemming: ', stemmer.stem('increases'))
print('Lemmatizing: ', lemmatizer.lemmatize('increases'))
'''

lemmatizer = WordNetLemmatizer()
 
print(lemmatizer.lemmatize('playing', pos='v'))