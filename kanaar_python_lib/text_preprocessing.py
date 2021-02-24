import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_punctuation(text):
    """
    returns text without punctiation from text
    """
    for char in string.punctuation:
        text = text.replace(char, '')
    return text

def lemmatize_text(text):
    """
    returns a lemmatized text from un-lemmatized text
    """
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in text.split(' ')]
    return ' '.join(lemmatized)

def remove_stopwords(text):
    """
    returns text without stopwords from text
    """
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    text = [w for w in word_tokens if not w in stop_words]
    return ' '.join(text)

def clean_text(text):
    """
    returns cleaned text, lemmatized and without punctuation or stopwords from text
    """
    text = remove_punctuation(text).lower()
    text = lemmatize_text(remove_stopwords(text))
    text = ''.join(word for word in text if not word.isdigit())
    return text

