class One():
    def __init__(self, arg):
        print("inside One constructor")
        # TODO: write code...
    def method(self):
        print("One class method")

class Two():
    def __init__(self, arg):
        print("inside Two constructor")
        # TODO: write code...
    def method(self):
        print("Two class method")


ob1 = One(10)
ob2 = Two(20)
ob1.method()
ob1 = Two(20)
ob1.method()