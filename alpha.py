#EDX PYTHON COURSE EXERCICE
#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc



s = 'sdfvpaiond'

# initialise tracker variables
comp=0
char=s[0]
long=s[0]

# step through s indices
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        char += s[i + 1]
        # if current length is bigger update
        if len(char) > comp:
            comp = len(char)
            long = char
    else:
        char=s[i + 1]
print ('Longest substring in alphabetical order is: ' + long)
