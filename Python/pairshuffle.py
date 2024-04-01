# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:12:06 2024

@author: tomke
"""

import random

def group_pairs(names):
    # Shuffle the list to randomize the order
    random.shuffle(names)
    
    # If the number of names is odd, remove one name and print it separately
    if len(names) % 2 != 0:
        odd_name = names.pop()
        print("Unpaired name:", odd_name)
    
    # Group the names in pairs and print them
    for i in range(0, len(names), 2):
        pair = names[i:i+2]
        print(f"Pair {i/2}:", pair)
    




solo = ['Brycen', 'Juan', 'Luisa', 'Gabriela', 'Matthew', 'Jacob', 'Zhihui', 'Colin', 'Tanishka', 'Ethan', 'Scott', 'Payton', 'Kevin', 'Zachary', 'Aidan', 'Andreas', 'Volkan', 'Greyson']
groups = [['Hayley', 'Ruby'],['Lucas', 'Luis', 'Max'],['Ellis', 'Mia'],['Henry', 'Howard', 'Jeremy'],['Grace', 'Shayna', 'Haven']]

group_pairs(solo)
group_pairs(groups)