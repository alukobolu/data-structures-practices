class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    
    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inorder_traversal(self):
        elements =[]

        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()


    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

    def search(self,val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        

        

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    numbers_tree.delete(20)
    print("After deleting 20 ---",numbers_tree.inorder_traversal())
    # print(numbers_tree.search(20))

    # countries =['Nigeria','Ghana','UK','America','Turkey']
    # countries_tree = build_tree(countries)
    # print("is America There ?",countries_tree.search('America'))
    # print("is Singapore There ?",countries_tree.search('Singapore'))
    # print(countries_tree.inorder_traversal())