'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def wrapper_func(inner_function):
    def func():
        print("inside function of wrapper_func func")
        return inner_function()
        
    print("inside wrapper_func func")
    return func

def main_func():
    print("in main function")
    return
main_func = wrapper_func(main_func)
main_func()
    
    


    
