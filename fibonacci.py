
def fibonacci(max_num):
    fib_series = []
    n0 = 0 
    n1 = 1
    fib_series.append(n0)
    fib_series.append(n1)
    while(n1 < max_num):
        temp = n1
        n1 = n0 + n1
        n0 = temp
        fib_series.append(n1)
    
    fib_series.pop()
    return fib_series

try:
    max_num = int(input("Enter number till fibonacci series:"))
    print(fibonacci(max_num))
except(ValueError):
    print("provide interger value")

