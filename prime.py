
try:
    num = input("Enter number to check prime or not : ")
    num = int(num)
    flag = 0 
    for i in range(2, int(num/2)):
        if (num%i == 0 ):
            #print("Its not a prime number ")
            flag = 1
            break
    
    if(flag == 1):
        print("Its not a prime number ")
    else:
        print("Its a prime number ")
except(ValueError):
    print("its not a number ")
else:
    print("in the else part ")
finally:
    print("Execution is done ")