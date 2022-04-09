'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
from functools import reduce

class Error(Exception):
    pass

def exception_method():
    raise Error
number = int(input())
try:
                
    if(number > 100):
        exception_method()
    else:
        print("No Exception")
except(Error):
    print("greater than 100 exception ")
number = [10,20,40,50]
new_number = reduce(lambda op1,op2 : op1 * op2 ,list(filter(lambda sel: sel >30,list(map(lambda item : item+10, number)))))
print(new_number)