#Assessment 01 - <caesar.py>
import sys

message = sys.argv[1]
key =  sys.argv[2]  # the letter (key) will represent a number
                    # with which we will shift each letter 
                    # in the message by
#for the numbers representing letters in the alphabet,
#I'm choosing to represent it as A=1, B=2, C=3,... Z=26
ciphertext = '' # cipher text string is currently empty
                # but will be filled and output
alphabet = ['A', 'B', 'C', 'D','E','F', 'G', 'H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
key_num = alphabet.index(key) + 1 # index starts at 0 so I'm adding 1
                                  # to it so the range is 1-26

messagechars = [] # empty list to put the individual characters
                  # of message into
for char in message: # for each character in message, append it to the empty list
    messagechars.append(char)

for i in range(len(messagechars)): # this is to create an index that will go through each character of message
    if messagechars[i] in alphabet:
        newchar_index = ((alphabet.index(messagechars[i])) + (key_num)) % 26
        newchar = alphabet[newchar_index]
        messagechars[i] = newchar #replacing the individual character with the new ecrypted character

for char in messagechars: # adds each new encrypted character into the empty string
    ciphertext += char

print(ciphertext) # prints out final encrypted message

