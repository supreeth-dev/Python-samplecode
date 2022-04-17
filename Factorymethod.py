from abc import abstractclassmethod,ABCMeta
class IPerson(ABCMeta):
    @abstractclassmethod
    def print_method():
        """Interface method"""

class Student():
    def __init__(self):
        self.name="Basic Student method"
    def print_method(self):
        print("I am a Student !!!")

class Teacher():
    def __init__(self):
        self.name = "Basic Teacher method"

    def print_method(self):
        print("I am a Teacher !!!")

class Factoryclass():
    @staticmethod
    def type_person(type):
        if(type == "Student"):
            return Student()
        if(type == "Teacher"):
            return Teacher()
        else:
            raise Exception("Neither Student not Teacher ")
            return -1



choice = str(input("Enter your type :"))
person_type = Factoryclass.type_person(choice)
person_type.print_method()
