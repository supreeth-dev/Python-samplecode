'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import re
class Maxchar(Exception):
    pass
try:
    word = input("Enter the string :")
    if(len(word) > 20 ):
        raise Maxchar
except Maxchar:
    print("Maxchar value")

    
flag = 0
count = 0 
for ch in word:
    if(ch == 'o' and prev == 'z'):
        flag =1 
        count = count + 1
    prev = ch 

if (flag == 1 and count == 1):
    ch_z = word.count('z')
    ch_o = word.count('o')

    if (ch_o == (2*ch_z)):
        print("Yes")
    else:
        print("No")
else:
    print("No")
