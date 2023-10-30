import os
from pathlib import Path

from natLang import textMatch_1, textMatch_2, textMatch_3, textMatch_4, textMatch_5
from natLang import readLib

os.system('cls')


# Data Reading Tests
#-------------------
dataDir = Path(__file__).parent / 'data'

# file = dataDir / 'Capitec Funeral Plan.yaml'
file = dataDir / 'Standard Bank Funeral Plan.yaml'

data = readLib(file)



# setup Test Strings
#-------------------

tests = [
    'What lives are Assured?',
    'What lives can be Insured?',
    "Whose lives can be insured?",
    "Whose lives can be Covered?",
    'what lives are covered?',
]

lib = {
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


# print("""
# ------
# Test 1
# ------
# """)
# for test in tests:
#     res = textMatch_1(test, lib)
#     print('Question:', test, '|', 'Answer:',  lib[res[0][-1]], '|', 'Certainty:', res[1][res[0][-1]])
#     print('All Certainties:', res[1])
#     print('\n')
# print('\n')

# print("""
# ------
# Test 2
# ------
# """)
# for test in tests:
#     res = textMatch_2(test, lib)
#     print('Question:', test, '|', 'Answer:',  lib[res[0][-1]], '|', 'Certainty:', res[1][res[0][-1]])
#     print('All Certainties:', res[1])
#     print('\n')
# print('\n')

# print("""
# ------
# Test 3
# ------
# """)
# for test in tests:
#     res = textMatch_3(test, lib)
#     print('Question:', test, '|', 'Answer:',  lib[res[0][-1]], '|', 'Certainty:', res[1][res[0][-1]])
#     print('All Certainties:', res[1])
#     print('\n')
# print('\n')

# print("""
# ------
# Test 4
# ------
# """)
# for test in tests:
#     res = textMatch_4(test, lib)
#     print('Question:', test, '|', 'Answer:',  lib[res[0][-1]], '|', 'Certainty:', res[1][res[0][-1]]) 
#     print('All Certainties:', res[1])
#     print('\n')  
# print('\n')

print("""
------
Test 5
------
""")
for test in tests:
    res = textMatch_5(test, lib)
    print('Question:', test, '|', 'Answer:',  lib[res[0][-1]], '|', 'Certainty:', res[1][res[0][-1]]) 
    print('All Certainties:', res[1])
    print('\n')