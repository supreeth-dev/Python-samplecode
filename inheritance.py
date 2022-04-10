class A():
    def __init__(self,a,b):
        self.a = a
        self.b = b 
        print("In constructor A")
    def feature1(self):
        print("feature 1 in A")
    def feature2(self):
        print("feature 2")

class B(A):
    def __init__(self,a,b):
        self.a = a
        self.b = b 
        print("In constructor B")
    def feature1(self):
        print("feature1 in B ")
        super().feature1()
    def feature3(self):
        print("feature 3")
    def feature4(self):
        print("feature 4")
a = A(3,4)
b = B(5,6)
a.feature1()
b.feature1()