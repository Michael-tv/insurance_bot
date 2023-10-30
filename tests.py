import os
from pathlib import Path

from insuranceBot import textMatch_1, textMatch_2, textMatch_3, textMatch_4, textMatch_5
from insuranceBot import readLib

os.system('cls')


# Data Reading Tests
#-------------------
dataDir = Path(__file__).parent / 'data'

# file = dataDir / 'Capitec Funeral Plan.yaml'
file = dataDir / 'Standard Bank Funeral Plan.yaml'

data = readLib(file)


# Testing Todo
# ------------
# - Calculate measure of success that includes high values for correct match as well as low values for incorrect matches
# - Write tests to evaluate false positives
# - write tests to test all if branches

# setup Test Strings
#-------------------

tests = [
    'What lives are Assured?',
    'What lives can be Insured?',
    "Whose lives can be insured?",
    "Whose lives can be Covered?",
    'what lives are covered?'
]

# Only Single question matching test set
lib = [
    'Whose Lives can be assured?',
    'What is the cover amount?',
    # 'what is the Waiting period?',
    # 'When is the termination Date?',
    # 'when is the start date?',
    # 'when does the policy start?',
    # 'what are the maximum lives covered?',
    # 'what are the policy benefits?',
    # 'what are the exclusions?',
    # 'what is excluded?'
]

# Multiple question test set
libOpt = {
    0: {'options': ["Whose Lives can be assured?", "Whose Lives can be Insured?"], 'answer': ["Whose Lives can be assured?"]},
    1: {'options': ['What is the cover amount?'], 'answer': ['What is the cover amount?']}
    # 'what is the Waiting period?',
    # 'When is the termination Date?',
    # 'when is the start date?',
    # 'when does the policy start?',
    # 'what are the maximum lives covered?',
    # 'what are the policy benefits?',
    # 'what are the exclusions?',
    # 'what is excluded?'
}


print("""
------
Test 1
------
""")
for test in tests:
    res = textMatch_1(test, lib)
    print('Question:', test, '|', 'Answer:',  lib[res[0][0]], '|', 'Certainty:', res[1][res[0][0]])
    print('All Certainties:', res[1])
    print('\n')
print('\n')

print("""
------
Test 2
------
""")
for test in tests:
    res = textMatch_2(test, libOpt)
    print('Question:', test, '|', 'Answer:',  lib[res[0][0]], '|', 'Certainty:', res[1][res[0][0]])
    print('All Certainties:', res[1])
    print('\n')
print('\n')

print("""
------
Test 3
------
""")
for test in tests:
    res = textMatch_3(test, libOpt)
    print('Question:', test, '|', 'Answer:',  lib[res[0][0]], '|', 'Certainty:', res[1][res[0][0]])
    print('All Certainties:', res[1])
    print('\n')
print('\n')

print("""
------
Test 4
------
""")
for test in tests:
    res = textMatch_4(test, libOpt)
    print('Question:', test, '|', 'Answer:',  lib[res[0][0]], '|', 'Certainty:', res[1][res[0][0]]) 
    print('All Certainties:', res[1])
    print('\n')  
print('\n')

print("""
------
Test 5
------
""")
for test in tests:
    res = textMatch_5(test, libOpt)
    print('Question:', test, '|', 'Answer:',  lib[res[0][0]], '|', 'Certainty:', res[1][res[0][0]]) 
    print('All Certainties:', res[1])
    print('\n')