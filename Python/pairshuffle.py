# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:12:06 2024

@author: tomke
"""

import random
import json as js

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def group_pairs(names):
    #shuffle the list to randomize the order
    random.shuffle(names)
    
    #if the number of names is odd, remove one name and print it separately
    if len(names) % 2 != 0:
        odd_name = names.pop()
        print("Unpaired name:", odd_name)
    
    #group the names in pairs and print them
    for i in range(0, len(names), 2):
        pair = names[i:i+2]
        print(f"Pair {i/2}:", pair)
    
def schedule(names):
    #shuffle list
    random.shuffle(names)
    sched = {}
    for k in range(0,len(names)):
        print(f'{k}: {names[k]}\n')
        sched[names[k]] = k
    return sched
        



solo = ['Brycen', 'Juan', 'Luisa', 'Gaby', 'Colin', 'Tanishka', 'Ethan', 'Payton', 'Kevin', 'Zachary', 'Aidan', 'Andreas', 'Greyson']
groups = [['Hayley', 'Ruby'],['Lucas', 'Luis', 'Max'],['Ellis', 'Mia'],['Henry', 'Howard', 'Jeremy'],['Grace', 'Shayna', 'Haven'],['Scott', 'Volkan']]

# group_pairs(solo)
# group_pairs(groups)

#form schedule
groups = flatten_list(groups)
slist = schedule(solo+groups)
with open('FinalSchedule.dat','w') as writefile:
    writefile.write(js.dumps(slist))
