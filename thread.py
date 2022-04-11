import threading

def square(num,num1):
    print("Square :", num*num1)

def cube(num,num1):
    print("Cube :", num*num*num1)
    
if __name__ == "__main__":
    t1 = threading.Thread(target=square, args=(10,20))
    t2 = threading.Thread(target=cube, args=(10,20))
    t1.start()
    t2.start()
    #t1.join()
    t2.join()
    print("Done")