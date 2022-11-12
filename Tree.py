class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children  = []
        self.parant = None

    def get_level(self):
        level = 0
        p = self.parant
        while p:
            level += 1
            p = p.parant
        return level

    def print_tree(self):
        space = " " * self.get_level() * 3
        prefix = space + "|__" if self.parant else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parant = self
        self.children.append(child)

def built_product_tree():
    root = TreeNode("Electronic")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("i-Phone"))
    cellphone.add_child(TreeNode("Google-pixel"))
    cellphone.add_child(TreeNode("Oppo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    built_product_tree()
