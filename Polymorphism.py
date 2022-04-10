class Polymorphism():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, obj):
        m1 = self.a+obj.a
        m2 = self.b+obj.b
        #return ((obj1.a+obj2.a),(obj1.b+obj2.b))
        return Polymorphism(m1,m2)
    def __sub__(self,obj):
        m1 = obj.a - self.a
        m2 = obj.b - self.b
        return Polymorphism(m1,m2)



obj1 = Polymorphism(4,5)
obj2 = Polymorphism(8,9)

obj3 = obj1 + obj2
print(obj3.a)
obj3 = obj1 - obj2
print(obj3.a)
print(obj3.b)
#print(obj3.a)