import string
import random
import re
import time
import os

import yaml

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import nltk

import numpy as np

from fuzzywuzzy import fuzz

nltk.download('stopwords')


#==================================================================================
def quitCheck(text):
    quitStrings = ['q', 'quit', 'exit', 'no']
    
    text = text.lower()
    text = re.sub('[ .\s]', '', text)
    
    if text in quitStrings:
        return True
    else:
        return False

def halEnd():
    os.system('cls')
    
    print(
"""There is a flower within my heart, Daisy, Daisy!\n
Planted one day by a glancing dart,\n
Planted by Daisy Bell!\n
Whether she loves me or loves me not,\n
Sometimes it's hard to tell;\n
Yet I am longing to share the lot\n
Of beautiful Daisy Bell!\n
...\n
""")
    time.sleep(5)
    os.system('cls')
    
    
def genExampleQuestion(dataSets):
    # Select random dataset
    randDataset = random.choice(list(dataSets.items()))
    
    # Select random question set
    randQuestionSet = random.choice(list((randDataset[1]['responses']).items()))

    #Select random question
    randQuestion = random.choice(randQuestionSet[1]['options'])
 
    return randQuestion

# IO Functions
def readLib(file):
    with open(file) as f:
        data = yaml.load(f, yaml.Loader)
    return data
  
  
def planSelectionErrorCheck(toCompare, numPolicies):
    try:
        toCompare = [int(x) for x in toCompare]
        fault = False
    except ValueError:
        fault = True
    
    if fault == True:
        print('Not all entered elements are numbers, please retry')
    elif toCompare == '':
        print('no values to compare specified, please retry')
        fault = True
    elif len(toCompare) == 0:
        print('no values to compare specified, please retry')
        fault = True
    elif max(toCompare) > numPolicies - 1:
        print('Non-Valid options selected for plans to compare, please retry')
        fault = True
    else:
        fault = False
        
    return fault

#==================================================================================
# Text processing and cleaning functions

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
# String matching functions

def textMatch_1(query, dataSet):
    """
    Clean Operations
    ----------------
      - Remove punctuation
      - Remove Duplicate spaces
      - Lower text
      - Lemmatize text
    
    MatchMethod
    -----------
      - Fuzz ratio
    """

    query = textPreprocess_1(query)

    #Check all entries in lib
    res = []
    matches = []
    # Iterate though all possible responses
    for response in dataSet:
        responseClean = textPreprocess_1(response)       
        res.append(fuzz.ratio(query, responseClean))
        matches.append(response)
        
    return np.argsort(res)[::-1], res


def textMatch_2(query, dataSet):
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
      - Find best match between all options
    """
    
    query = textPreprocess_2(query)

    #Check all entries in lib
    res = []
    matches = []
    # Iterate though all possible responses
    for idx, response in dataSet.items():
        # Find max value for all questions in the synonym list
        optRes = []
        for opt in response['options']:
            optClean = textPreprocess_2(opt)
            optRes.append(fuzz.partial_ratio(query, optClean))
        matches.append(idx)
        res.append(max(optRes))
    return np.argsort(res)[::-1], res


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
      - Find best match between all options
    """

    query = textPreprocess_3(query)

    #Check all entries in lib
    res = []
    matches = []
    # Iterate though all possible responses
    for idx, response in dataSet.items():
        # Find max value for all questions in the synonym list
        optRes = []
        for opt in response['options']:
            optClean = textPreprocess_3(opt)
            optRes.append(fuzz.partial_ratio(query, optClean))
        matches.append(idx)
        res.append(max(optRes))
    return np.argsort(res)[::-1], res


def textMatch_4(query, dataSet):
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
      - Find best match between all options
    """

    query = textPreprocess_3(query)

    #Check all entries in lib
    res = []
    matches = []
    # Iterate though all possible responses
    for idx, response in dataSet.items():
        # Find max value for all questions in the synonym list
        optRes = []
        for opt in response['options']:
            optClean = textPreprocess_3(opt)    
            optRes.append(fuzz.token_sort_ratio(query, optClean))
        matches.append(idx)
        res.append(max(optRes))
    return np.argsort(res)[::-1], res


def textMatch_5(query, dataSet):
    """
    Preprocess Operations
    ---------------------
      - Remove punctuation
      - Remove Duplicate spaces
      - Lower text
      - Lemmatize text
      - Remove stopwords
    
    Match Method
    ------------
      - Fuzz token_set_ratio
      - Find best match between all options
    """

    query = textPreprocess_3(query)

    #Check all entries in lib
    res = []
    matches = []
    # Iterate though all possible responses
    for idx, response in dataSet.items():
        # Find max value for all questions in the synonym list
        optRes = []
        for opt in response['options']:
            optClean = textPreprocess_3(opt)    
            optRes.append(fuzz.token_set_ratio(query, optClean))
        matches.append(idx)
        res.append(max(optRes))
    return np.argsort(res)[::-1], res



