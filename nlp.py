from distutils.command.clean import clean
import nltk
import numpy as np
nltk.download('punkt') # one time execution
nltk.download('stopwords')

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def clean_text(english_txt):
    try:
       word_tokens = nltk.word_tokenize(english_txt)
       filtered_word = [w for w in word_tokens if not w in stop_words]
       filtered_word = [w + " " for w in filtered_word]
       return "".join(filtered_word)
    except:
       return np.nan