class TreeNode:
    def __init__(self , data):
        self.data = data
        self.children  = []
        self. parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level()*3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    
def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Windows"))
    laptop.add_child(TreeNode("Linux"))

    cellphone = TreeNode('cell phone')
    cellphone.add_child(TreeNode("samsung"))
    cellphone.add_child(TreeNode("iphone"))
    cellphone.add_child(TreeNode("redmi"))

    tv = TreeNode('tv')
    tv.add_child(TreeNode("lg"))
    tv.add_child(TreeNode("philips"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()