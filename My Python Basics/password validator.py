
'''
A valid password is the one that conforms to the following rules:

 - Minimum length is 5;

 - Maximum length is 10;

 - Should contain at least one number;

 - Should contain at least one special character (such as &, +, @, $, #, %, etc.);

 - Should not contain spaces.



Examples:

Input: "Sololearn"

Output: false



Input: "John Doe"

Output: false



Input: "$ololearn7"

Output: true

Write a program to checks if the user input is a valid password or not.
'''

from string import digits, punctuation

def validate_password(p):
    if not 5 <= len(p) <= 10:
        return False
    
    if not any(c in digits for c in p):
        return False
    
    if not any(c in punctuation for c in p):
        return False
    
    if ' ' in p:
        return False

    return True

for p in ('Sololearn', 'John Doe'
, '$ololearn7'):
    print(p, ': ', ('invalid', 'valid')[validate_password(p)], sep='')

s = input("INPUT: ")
print("{}\n{}".format(s, 5 <= len(s) <= 10 and any(l in "0123456789" for l in s) and any(l in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" for l in s) and not " " in s))