from pathlib import Path
import os

from insuranceBot import textMatch_5
from insuranceBot import readLib
from insuranceBot import quitCheck, genExampleQuestion, halEnd, planSelectionErrorCheck
#-------------------------------------------------------------------------------
#  Define Parameters

dataDir = Path(__file__).parent / 'data' / 'prepared'

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

#------------------------------------------------
#Start Program loop

os.system('cls')
print(HAL)
print('Hi my name is HAL, I am a HAL9000 computer. Until my logic circuits are reactivated, am only able to compare Funeral Policies.\n')

print(f'Here is an example of a question you can ask me: {genExampleQuestion(dataSets)}')
print('\n')

print(f"You can enter 'q' anytime to shut me down")
print('\n')

# Consider adding list of frequent questions, or important keywords to help user

cnt = 0
rephReq = False
while True:   
    
    if rephReq:
        query = input('Your question is not clear, please rephrase?\n> ') 
        print('\n')
    
    else:
        if cnt == 0:
            query = input('What would you like to compare?\n> ') 
            print('\n') 
        else: 
            query = input('Is there anything else I can compare for you?\n> ') 
            print('\n') 
                 
    if quitCheck(query):
        halEnd()
        break

    # Generate toCompare string
    compareStr = ''
    policies = list(dataSets.keys())
    for idx, val in enumerate(policies):
        compareStr = compareStr + f'  ({idx}) ' + val + '\n'

    fault = True
    while fault == True:
        toCompare = input(
            f"""Please select which plans you would you like to compare?\n{compareStr}\n'e.g. for Capitec and Standard bank, enter > 0 1'\n> """)
        print('\n') 

        toCompare = toCompare.split(' ')
        
        # to some error checking on the to compare stuff
        fault = planSelectionErrorCheck(toCompare, len(policies))
    
    toCompare = [int(x) for x in toCompare]
    
    cnt += 1
    for policyNum in toCompare:
        info = dataSets[policies[policyNum]]['document info'] 
        responses = dataSets[policies[policyNum]]['responses']

        answerIds, answerScores = textMatch_5(query, responses)
    
        acceptableAnswers = [i for i in answerScores if i > 75]
        
        if max(answerScores) < 70: # ask for clarity if no answers are above 70
            rephReq = True
        
        # ask for clarity if multiple answers are above 75
        elif len(acceptableAnswers) > 1: 
            print('your question is ambiguous, please choose one of the following questions by retyping the question:')
            for answer in acceptableAnswers:
                idx = answerScores.index(answer)# Find index of proposed answer
                print(responses[idx]['options'][0])
        
        else:
            print(policies[policyNum], f'Answer match certainty: {max(answerScores)}')
            print('--------------------------')
            print(responses[answerIds[0]]['answer'])
            print(f"from {responses[answerIds[0]]['ref']} from document found at {info['Link to document']}")
            print('\n')
            rephReq = False
