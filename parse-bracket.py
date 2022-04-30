
def valid_expr(expr):
    print("Inside Expr")
    list1 = []
    stackttop = ""
    for ch in expr:
        #print(ch)
        if(ch == "{" or ch == "(" or ch == "["):
            list1.append(ch)
        elif(ch == "}" and len(list1)>0):
            stackttop = list1[len(list1) - 1]
            print("inside flower close")
            if (stackttop =="{"):
                list1.remove(stackttop)
        elif (ch == ")" and len(list1)>0):
            print("inside small close")
            stackttop = list1[len(list1) - 1]
            print("stackttop=",stackttop)
            if (stackttop == "("):
                list1.remove(stackttop)
        elif (ch == "]" and len(list1)>0):
            print("inside square close")
            stackttop = list1[len(list1) - 1]
            print(stackttop)
            if (stackttop == "["):
                list1.remove(stackttop)
                #list1.pop()
    print(list1)
    if(len(list1)>0):
        return("Invalid")
    else:
        return("Valid")


#expr = "{a+b*(c/d)}"
#expr = "(aa+[b)]"
expr = ")("
print(valid_expr(expr))

