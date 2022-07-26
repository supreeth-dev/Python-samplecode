class BinarySearchTree:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if( self.data == data):
            return None
        if(data < self.data):
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        if (data > self.data):
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def inorder(self):
        element = []
        if(self.left):
            element += self.left.inorder()
        element.append(self.data)
        if(self.right):
            element += self.right.inorder()
        return element

    def preorder(self):
        pass

    def postorder(self):
        pass

    def find_min(self):
        if self.left is None :
            return self.data
        return self.left.find_min()


    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self,val):
        #1 delete leaf node
        if(self.data > val):
            if self.left:
                self.left.delete(val)
        elif(self.data < val):
            if self.right:
                self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.find_min()
            self.data = min_val
            self.left = self.left.delete(min_val)
            return self


        #2 delete one child
        #3 delete 2 chile node
def build_tree(numbers):
    root = BinarySearchTree(numbers[0])
    for i in range(1,len(numbers)):
        root.add_child(numbers[i])
    return root



if __name__ == '__main__':
    print("in main function ")
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = build_tree(numbers)
    print ("inorder =",root.inorder())

    print("min",root.find_min())
    print("max", root.find_max())
    root.delete(20)
    print ("inorder =",root.inorder())
