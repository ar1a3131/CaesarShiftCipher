#Assessment 01 - <shift.py>
import sys

message = sys.argv[1]
key =  sys.argv[2] # the key does not have to be just a single
                   # capital letter... variable length, but 
                   # must be shorter than the message

alphabet = ['A', 'B', 'C', 'D','E','F', 'G', 'H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

messagechars =[]
keychars = []
ciphertext = ''

for char in message:
    messagechars.append(char)

repetitions = len(message) // len(key) # find amount of times the full key
                                       # length can allign with the full
                                       # message length

count = 0
while count < repetitions:       # while loop will go for the value of repetitions
    for i in key:
        keychars.append(i)
    count += 1

extra_letters = len(message) % len(key)    # what remaining letters after floor division
                                           # to finally match the length of the message

for i in range(extra_letters):              # add those extra letters to the key list
    keychars.append(keychars[i])


for i in range(len(message)): #similar idea to in caesar.py
    new_index_alph = (alphabet.index(messagechars[i]) + alphabet.index(keychars[i]) + 1) % 26
    messagechars[i] = alphabet[new_index_alph]


for char in messagechars: # adds each new encrypted character into the empty string
    ciphertext += char

print(ciphertext)
