# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:31:35 2024

@author: tomke
"""

def main():
    numbers_list=[1,1,2,3,5,8]
    total=0
    for num in numbers_list:
        total += num
        print("Current total:",total)
    return total
 
    
#The code below runs whatever is in main()
if __name__ == '__main__':
    main()