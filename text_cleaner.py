import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Download required NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

# Common filler words to remove
FILLER_WORDS = ['uh', 'um', 'like', 'you know', 'actually', 'basically', 'so']

def clean_text(text, lemmatize=False):
    """
    Cleans input text by:
        - Lowercasing
        - Removing punctuation
        - Removing filler words
        - Removing stopwords
        - Optional lemmatization
    """
    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove filler words
    for filler in FILLER_WORDS:
        text = re.sub(r'\b' + filler + r'\b', '', text)

    # Tokenize
    words = text.split()

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Optional Lemmatization
    if lemmatize:
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(word) for word in words]

    return ' '.join(words)
