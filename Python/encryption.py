# Encryption Pseudocode
# 
# Function ( string ), will eventually take a text file that can be read
#         this is plaintext!
# Loop through the string
#      Take a character from the string
#      Put the character in the encryption dict to find encrypt value
#      Add encrypt value for character to new string
#                             this is ciphertext!
# return new string
#
# Could also enable function to take a dict for encryption, so it works on
# any given alphanumeric conversions, as long as every possible key has a value

# Can be made into encrypt and decrypt
# Function ( file )
#     opens file, reads, stores string, closes

# Function ( array )
#    converts to string, stores string, writes to new results file, closes


import numpy as np

# Purpose: takes a string and encrypts it to numeric
def  cipher(plaintext):
    
    lowercase_plaintext = plaintext.lower()
    
    # the lowercase alphabet
    alphabet = ['a', 'b', 'c', 'd', 
                'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p',
                'q', 'r', 's', 't',
                'u', 'v', 'w', 'x',
                'y', 'z', ' ', '.', 
                '!', '?', '<', '>',
                ',', '=', '"', '-', 
                '\n', '1', '2', '3',
                '4', '5', '6', '7', 
                '8', '9', '0', '(',
                ')', '%','\'', ':', 
                ';', '&', '$', '#'
                '_', '+', '*', '@',
                '^']
    
    # creates a numeric list
    i = 1
    numbers = []
    while i < 61:
        numbers.append(i)
        i = i + 1
    
    # combines alphabet and numeric lists into a dictionary
    encryption = dict(zip(alphabet, numbers))
    
    # initialized the value for the conversion working list to be empty
    ciphertext = np.array([])
    for char in lowercase_plaintext:
        new_value = encryption[char]  # finds the conversion
        ciphertext = np.append(ciphertext, new_value)     # adds new value to the list

    return ciphertext

# reads the message from the given file
def readcipher(plaintextfilename):
    folder = 'testfiles//'
    location = folder + plaintextfilename
    txthandler = open(location, 'r')
    plaintext = (txthandler.read())
    txthandler.close()
    
    return plaintext


# takes the ciphered message and writes it to a results file
def writecipher(encryptedmessage):
    encryptedmessage = np.array2string(encryptedmessage)
    f = open('results.txt', 'w+')    # will be overwritten on each test
    f.write(encryptedmessage)
    # f.write('\n')
    f.close()


# encryption process

file = input('Input file name:')

writecipher(cipher(readcipher(file)))



def ciphertester():
    testcounter = 0
    passedcounter = 0
    
    if (np.array_equal(cipher('abc'), np.array([1., 2., 3.]))):          # test case 1 in condition
        testcounter = testcounter + 1
        passedcounter = passedcounter + 1
    else:
        testcounter = testcounter + 1
        
    if (np.array_equal(cipher('helloworld'), 
                              np.array([8., 5., 12., 12., 15., 23., 15., 18., 12., 4.,]))):  # test 2
        testcounter = testcounter + 1
        passedcounter = passedcounter + 1
    else:
        testcounter = testcounter + 1
        
    if (np.array_equal(cipher('AABB'), np.array([1., 1., 2., 2.]))):  # test 2
       testcounter = testcounter + 1
       passedcounter = passedcounter + 1
    else:
       testcounter = testcounter + 1
    
    
    if (testcounter == passedcounter):
        print('All tests passed!')
    elif (passedcounter > 0):
        print(f'Only {passedcounter} out of {testcounter} tests passed.')
    else:
        print('No tests passed.')
        
    return passedcounter
            
    