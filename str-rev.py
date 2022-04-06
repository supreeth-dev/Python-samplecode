'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
#name = "naman"

name = input("Enter name : ")
print("in reverse order ")
reverse_str = name[::-1]
print(reverse_str)

if (name == reverse_str):
    print("its a palindrome")
else:
    print("its not a palindrome")
    
print("Length of string :", len(name))




