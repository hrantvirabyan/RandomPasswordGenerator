import random
import string
string.printable
randompassword="";
chars = list(string.printable)
i=0
while i<5:
    del chars[-1] #since in string.printable there are ' \t\n\r\x0b\x0c' we need to remove those and they happen to be the last few in the list
    i+=1
del chars[-10] #had to remove the "\\"

i=0
while i<random.randint(10,20) : #will grab random length for the password
    randompassword=randompassword+(random.choice(chars))
    i+=1



print ('Your random password is:', randompassword)
