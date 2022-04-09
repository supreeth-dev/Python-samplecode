'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import math
to_word = " "
def lastdigit_to_word(number):
    to_word = ""
    for digit in number:
        if(digit == '0'):
            pass
        elif(digit == '1'):
            to_word = to_word + "one"
        elif(digit == '2'):
            to_word = to_word + "two"
        elif(digit == '3'):
            to_word = to_word + "three"
        elif(digit == '4'):
            to_word = to_word + "four"
        elif(digit == '5'):
            to_word = to_word + "five"
        if(digit == '6'):
            to_word = to_word + "six"
        elif(digit == '7'):
            to_word = to_word + "seven"
        elif(digit == '8'):
            to_word = to_word + "eight"
        elif(digit == '9'):
            to_word = to_word + "nine"
    return to_word
def tenthdigit_to_word(number):
    to_word = ""
    
    for digit in number:
        if(digit == '0'):
            break
        elif(digit == '1'):
            to_word = to_word + "Ten"
            break
        elif(digit == '2'):
            to_word = to_word + "twenty"
            break
        elif(digit == '3'):
            print("here I am prev")
            to_word = to_word + "thirty"
            break
        elif(digit == '4'):
            print("here I am ")
            to_word = to_word + "fourty"
            break
        elif(digit == '5'):
            print("here I am next")
            to_word = to_word + "fifty"
            break
        if(digit == '6'):
            to_word = to_word + "sixty"
            break
        elif(digit == '7'):
            to_word = to_word + "seventy"
            break
        elif(digit == '8'):
            to_word = to_word + "eighty"
            break
        elif(digit == '9'):
            to_word = to_word + "ninty"
    return to_word    

def in_itr(number):
    to_word = ""
    sub_word = ""
    number_of_digit = 1 
    digit = ''
    while len(number)< 3:
        number = '0' + number
    for digit in number:
    
#        print("number_of_digit =",number_of_digit )
#        print("digit =",digit)
        if(number_of_digit == 1 ):
            
            if(digit == '0'):
                number_of_digit = number_of_digit + 1
                continue
            else:
                to_word = lastdigit_to_word(digit)
                to_word = to_word + " hundred"    
            print("in hundred",to_word)
        if(number_of_digit == 2 ):
            
            if(digit == '0'):
                number_of_digit = number_of_digit + 1
                continue
            else:
                to_word = tenthdigit_to_word(digit)
                print(">>>>>",type(digit),digit)
                print("in tenth",to_word)
        elif(number_of_digit == 3 ):
            to_word = lastdigit_to_word(digit)
            print("in once",to_word)
        
        number_of_digit = number_of_digit + 1
        to_word = to_word + " "
        sub_word = sub_word + to_word
    return sub_word    


number = str(input("Enter number: "))
i = 0 
number_of_comma = int(math.ceil(len(number)/3))

commas = 0 

while(i<len(number)):


    #sub_number = number[i:(i+3)]
    sub_number = number[len(number)-i-3:len(number)-i]
    print("sub_number =",sub_number)
    j = 2
    while(sub_number == ""):
        
        print("////////////")
        sub_number = number[len(number)-i-j:len(number)-i]
        j = j - 1
    sub_str = in_itr(sub_number) 
    
    i= i+3
    if(commas == 0):
        print("----->",sub_str )
        to_word1 = sub_str
    elif (commas == 1):
        print("----->",sub_str )
    #    to_word1 = to_word1 + " Thousand **"
        to_word1 = sub_str +"* Thousand * " + to_word1
    elif (commas == 2):
        print("----->",sub_str )
    #    to_word1 = to_word1 + " Thousand **"
        to_word1 = sub_str +"* Million * " + to_word1
    elif (commas == 3):
        print("----->",sub_str )
    #    to_word1 = to_word1 + " Thousand **"
        to_word1 = sub_str +"* Billion * " + to_word1
    elif (commas == 4):
        print("----->",sub_str )
    #    to_word1 = to_word1 + " Thousand **"
        to_word1 = sub_str +"* Trillion * " + to_word1
    
    commas = commas + 1
    sub_str = ""
    #b[len(b)-i-3:len(b)-i]
    
print(to_word1)    
        
    
    





