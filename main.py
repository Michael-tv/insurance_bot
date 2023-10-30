import re
from pathlib import Path
import os
import random

from natLang import textMatch_5
from natLang import readLib

#------------------------------------------------

def quitCheck(text):
    quitStrings = ['q', 'quit', 'exit']
    
    text = text.lower()
    text = re.sub('[ .\s]', '', text)
    
    if text in quitStrings:
        return True
    else:
        return False
    
    
def genExampleQuestion(dataSets):
    # Select random dataset
    randDataset = random.choice(list(dataSets.items()))
    
    # Select random question set
    randQuestionSet = random.choice(list((randDataset[1]).items()))

    #Select random question
    randQuestion = random.choice(randQuestionSet[1]['options'])
 
    return randQuestion
    

#-----------------------------------------------

#  Define Parameters

dataDir = Path(__file__).parent / 'data'

# Read data
dataSets = {}
for file in dataDir.rglob('*.yaml'):   
    dataSets[file.stem] = readLib(file)

HAL = """
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⠟⠋⣻⣤⣤⣤⣤⣤⣄⣉⠙⠻⣿⣿⣿⣦⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣇⣤⣾⠿⠛⠉⠉⠉⠉⠛⠿⣷⣶⣿⣿⣿⣿⣷⡀⠀
⠀⣾⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣷⠀
⢠⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇
⠘⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⠃
⠀⢿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡿⠀
⠀⠈⢿⣿⣿⣿⣿⣿⣿⣶⣤⣀⣀⣀⣀⣤⣶⣿⣿⣿⣿⣿⣿⡿⠁⠀
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠿⠿⠿⠿⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀
"""

# sp = spacy.load('en_core_web_sm')

#------------------------------------------------
#Start Program loop

os.system('cls')
print(HAL)
print('Hi my name is HAL, I am a HAL9000 computer\n')
print('I Until my logic circuits are reactivated, am only able to compare Funeral Policies.\n')

print(f'Here is an example of a question you can ask me: {genExampleQuestion(dataSets)}')
print('\n')

cnt = 0
rephReq = False
while True:   
    
    if rephReq:
        query = input('Your question is not clear, please rephrase?\n>') 
        print('\n')         
    
    else:
        if cnt == 0:
            query = input('What would you like to compare?\n>') 
            print('\n') 
        else: 
            query = input('Is there anything else I can compare for you?\n>') 
            print('\n') 
                 
    if quitCheck(query):
        break

    cnt += 1

    answerIds, answerScores = textMatch_5(query, dataSet)
    
    acceptableAnswers = [i for i in answerScores if i > 75]
    # ask for clarity if no answers are above 65
    if max(answerScores) < 70:
        rephReq = True
    
    # ask for clarity if multiple answers are above 75
    elif len(acceptableAnswers) > 1: 
        print('your question is ambiguous, please choose one of the following questions by typing the letter:')
        for answer in acceptableAnswers:
            print(dataSet[id]['options'][0])
    
    else:
        print(f'Answer match certainty: {max(answerScores)}')
        print(dataSet[answerIds[0]]['answer'])
        print('\n')
        rephReq = False

    

    # queryPlans = input('Select plans to compare e.g. for Capitec and Standard Bank type >1 2 \nAvailable Plans:\n  (1) for Capitec \n  (2) for Standard Bank\n>')   
    # if quitCheck(queryPlans):
    #     break
    
    # else:
    #     preprocessText(queryQuestion)        
        
        
        
        # spData = sp(queryQuestion)
        
        # m_tool = spacy.Matcher(nlp.vocab)
        
        # queryQuestionSent = nltk.sent_tokenize(queryQuestion)
        # queryQuestionWords = nltk.word_tokenize(queryQuestion)

        # print(queryQuestion)
        




#TODO: if two scores are close, highlight issue
#TODO: if not score is above 70, highlight issue