'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import os
print("Hello World")

try:
    num = "abs"
    os.system('ls')
    num = int(num)# TODO: write code...
except ValueError:
    print("ValueError")
    
else:
    print("Value Error in  in else")
finally:
    print("Value Error in finally ")
    
    
unsorted = [10 ,20 ,6 ,15]
#unsorted = unsorted.sort()
unsorted.sort()
print(unsorted)


prime_numbers = [11, 3, 7, 5, 2]

# sort the list
prime_numbers.sort()
print(prime_numbers)