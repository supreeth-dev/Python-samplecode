


class A:
    def __init__(self, a ,b):
        self.a = a 
        self.b = b 
    def display(self):
        print("in display menthod ", self.a, self.b)
        
class B(A):
    def __init__(self,a,b,c ,d):
        super().__init__(a,b)
        self.c = c
        self.d = d
    
    def display(self):
        print("inside the child method")
        super().display()
        print("in display menthod ", self.c, self.d)
    
    @classmethod
    def ind_of_obj(cls):
        print("inside the class menthod")
    
    @staticmethod
    def ind_of_cls():
        print("inside the static method")
        
    def __add__(self,other):
        print("inside add func")
        print(self.a+other.b)


a = "5" 
b = "6"
print(a+b)
print(str.__add__(a,b))



obj_a = A(4,5)
obj_a.display()

obj_b = B(4,5,8,9)
obj_c = B(10,20,30,40)

obj_b.display()
B.ind_of_obj()
B.ind_of_cls()

obj_b + obj_c
