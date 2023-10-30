import string

import yaml

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import nltk

import numpy as np

from fuzzywuzzy import fuzz

nltk.download('wordnet')
nltk.download('stopwords')


#==================================================================================
def readLib(file):
    with open(file) as f:
        data = yaml.load(f, yaml.Loader)
    return data

#==================================================================================

def textPreprocess_1(text):
    
    # Remove punctuation
    for pElem in string.punctuation:
        text = text.replace(pElem, '')    
    
    # Remove duplicate whitespaces
    text = text.split()
    text = ' '.join(text)    
    
    # Convert all text to lowercase
    text = text.lower()
    
    return text


def textPreprocess_2(text):
       
    # Remove punctuation
    for pElem in string.punctuation:
        text = text.replace(pElem, '')    
    
    # Remove duplicate whitespaces
    text = text.split()
    text = ' '.join(text)
     
    # Convert all text to lowercase 
    text = text.lower()
        
    # Lemmatize words
    tokens = word_tokenize(text)
    wnlemmatizer = nltk.stem.WordNetLemmatizer()
    lemmaTokens = [wnlemmatizer.lemmatize(token) for token in tokens]

    return ' '.join(lemmaTokens)


def textPreprocess_3(text):
       
    # Remove punctuation
    for pElem in string.punctuation:
        text = text.replace(pElem, '')    
    
    # Remove duplicate whitespaces
    text = text.split()
    text = ' '.join(text)

    # Convert all text to lowercase 
    text = text.lower()
    
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stopwords = set(nltk.corpus.stopwords.words('english'))
    tokens = [token for token in tokens if not token in stopwords]
    
    # Lemmatize words
    tokens = word_tokenize(text)
    wnlemmatizer = nltk.stem.WordNetLemmatizer()
    lemmaTokens = [wnlemmatizer.lemmatize(token) for token in tokens]

    return ' '.join(lemmaTokens)

#==================================================================================

def textMatch_1(text, lib):
    """
    Clean
    -----
      - Remove punctuation
      - Remove Duplicate spaces
      - Lower text
      - Lemmatize text
    
    Match
    -----
      - Fuzz ratio
    """
    
    # lib = [num, options, answer]
    
    
    text = textPreprocess_2(text)
       
    #Check all entries in lib
    res = []
    matches = []
    for ent in lib:
        entClean = textPreprocess_2(ent)    
        matches.append(ent)
        res.append(fuzz.ratio(text, entClean))
    
    return np.argsort(res), res
      
#-----------------------------------------------------------------------------------

def textMatch_2(text, lib):
    """
    Clean
    -----
      - Remove punctuation
      - Remove Duplicate spaces
      - Lower text
      - Lemmatize text
    
    Match
    -----
      - Fuzz Partial_ratio
    """
    
    text = textPreprocess_2(text)
       
    #Check all entries in lib
    res = []
    matches = []
    for ent in lib:
        entClean = textPreprocess_2(ent)    
        matches.append(ent)
        res.append(fuzz.partial_ratio(text, entClean))

    return np.argsort(res), res

#-----------------------------------------------------------------------------------

def textMatch_3(query, dataSet):
    """
    Clean
    -----
      - Remove punctuation
      - Remove Duplicate spaces
      - Lower text
      - Lemmatize text
      - Remove stopwords
    
    Match
    -----
      - Fuzz ratio
    """
                    
    query = textPreprocess_3(query)
       
    #Check all entries in lib
    res = []
    
    for entry in dataSet.keys():
        
        optRes = []
        for opt in entry['options']:
            optClean = textPreprocess_3(opt)    
            optRes.append(fuzz.partial_ratio(query, optClean))
        
        breakpoint()
        np.argsort(optRes)
        #Find max option match 
        
        matches.append(opt)
    return np.argsort(res), res

#-----------------------------------------------------------------------------------

def textMatch_4(text, lib):
    """
    Clean
    -----
      - Remove punctuation
      - Remove Duplicate spaces
      - Lower text
      - Lemmatize text
      - Remove stopwords
    
    Match
    -----
      - Fuzz token_sort_ratio
    """
                           
    text = textPreprocess_3(text)
       
    #Check all entries in lib
    res = []
    matches = []
    for ent in lib:
        entClean = textPreprocess_3(ent)    
        matches.append(ent)
        res.append(fuzz.token_sort_ratio(text, entClean))

    return np.argsort(res), res

#-----------------------------------------------------------------------------------

def textMatch_5(query, dataSet):
    """
    Clean
    -----
      - Remove punctuation
      - Remove Duplicate spaces
      - Lower text
      - Lemmatize text
      - Remove stopwords
    
    Match
    -----
      - Fuzz token_set_ratio
    """

    query = textPreprocess_3(query)
       
    #Check all entries in lib
    res = []
    matches = []
    # Iterate though all possible responses
    for id, response in dataSet.items():
        # Find max value for all questions in the synonym list
        optRes = []       
        for opt in response['options']:
            optClean = textPreprocess_3(opt)    
            optRes.append(fuzz.token_set_ratio(query, optClean))
        matches.append(id)
        res.append(max(optRes))   
    return np.argsort(res)[::-1], res


#-----------------------------------------------------------------------------------

    