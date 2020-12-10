#########1#########2#########3#########4#########5#########6#########7#########8
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
# 
#########1#########2#########3#########4#########5#########6#########7#########8
#        11111111112222222222333333333344444444445555555555666666666677777777778
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#########1#########2#########3#########4#########5#########6#########7#########8
"""
Use random module with a seed of 2020 to generate 20 integers between 100 and 120 (inclusive). 
Then write code to calculate the median and mode.  The median is the 10th largest number. 
The mode is the number that occurs the most. If two or more number have the same frequency, 
list them all.
"""
#########1#########2#########3#########4#########5#########6#########7#########8
# Imported Modules
import random
import numpy as np

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Constants
SEED_VAL = 2020

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Variables

#########1#########2#########3#########4#########5#########6#########7#########8
# Functions
#--------1---------2---------3---------4---------5---------6---------7---------8#
def get_median(lexicon={}):
    temp_list = []
    # Median = 11th + 10th / 2.  
    # This function only works because the list always has 20 members
    
    # For every unique key in lexicon, and for each count of the unique key, 
    # populate a temporary list
    for keys in lexicon:
        for _ in range(0, lexicon.get(keys)):
            temp_list += [keys]
    
    # Sort the list 
    temp_list.sort()

    # Calculate the median from the two middle values
    median_num = (temp_list[10] + temp_list[9]) / 2.0
     
    return median_num

#--------1---------2---------3---------4---------5---------6---------7---------8#
def get_mode(lexikon={}):
    # Examine lexikon, search for largest values number in the dictionary
    # Sort lexikon by values, then check values
    maximal = 0     # maximal is Swedish for maximum
    result = []

    for varde in sorted(lexikon.values()):  # varde is Swedish for value
        if varde > maximal:
            maximal = varde # If new maximum is found, update maximal
    
    # Search through lexikon for number of times the maximal number was found
    rakna = 0
    for values in sorted(lexikon.values()):
        if values == maximal:
            rakna += 1      # rakna is Swedish for count
    
    # For every instance of maximal in lexikon.values(), print lexikon.keys()
    for keys, values in lexikon.items():
        if values == maximal:
            result += [keys]

    return result
#########1#########2#########3#########4#########5#########6#########7#########8
# Main

# Generate random numbers from seed 2020
# Establish the seed
random.seed(SEED_VAL)
ordbok = {}     # ordbok is Swedish for "dictionary" 

# Populate the dictionary ordbok with the unsorted entries
for _ in range(0, 20):
    entry = random.randint(100, 120)
    if ordbok.get(entry):
        ordbok[entry] += 1
    else:
        ordbok[entry] = 1

# Calculate median, the 10th largest number 
median_val = get_median(ordbok)
print(f'The median of the 20 numbers is {median_val:.2f}')

# Calculate mode
mode_val = [get_mode(ordbok)]
print(f'The mode(s) of the 20 numbers is(are): ',end='')
for index in range(len(mode_val)):
    print(f'{mode_val[index]} ')
# End of Main 