from abc import abstractstaticmethod
class Iperson():
    @abstractstaticmethod
    def get_data():
        """ in Child"""
class PersonSingleton(Iperson):
    __instance=None
    '''@staticmethod
    def get_instance():
        if (PersonSingleton.__instance == None):
            PersonSingleton("Default",0)
        return PersonSingleton.__instance'''
    
    def __init__(self,name,age):
        if(PersonSingleton.__instance != None):
            raise Exception("Single ton cant be created ")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
    @staticmethod
    def get_data():
        print("In child method in staticmethod")


p = PersonSingleton("Mike", 30)        
print(p)
p.get_data()
#p = PersonSingleton("Mike1", 30)        
#print(p)
#p.get_data()

