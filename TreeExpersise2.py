class TreeNode2:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parant = None

    def get_level(self):
        level = 0
        p = self.parant
        while p:
            level += 1
            p = p.parant
        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return
        space = " " * self.get_level() * 3
        prefix = space + "|__" if self.parant else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parant = self
        self.children.append(child)

def bulid_tree():
    gujrat = TreeNode2("Gujrat")
    gujrat.add_child(TreeNode2("Ahmedabad"))
    gujrat.add_child(TreeNode2("Baroda"))

    karnataka = TreeNode2("Karnataka")
    karnataka.add_child(TreeNode2("Bangluru"))
    karnataka.add_child(TreeNode2("Mysore"))

    india = TreeNode2("India")
    india.add_child(gujrat)
    india.add_child(karnataka)

    new_jersey = TreeNode2("New Jersey")
    new_jersey.add_child(TreeNode2("Princeton"))
    new_jersey.add_child(TreeNode2("Trenton"))

    calefonia = TreeNode2("California")
    calefonia.add_child(TreeNode2("San Fransisco"))
    calefonia.add_child(TreeNode2("Mountain View"))
    calefonia.add_child(TreeNode2("Palo Alto"))

    usa = TreeNode2("USA")
    usa.add_child(new_jersey)
    usa.add_child(calefonia)

    world = TreeNode2("Global")
    world.add_child(india)
    world.add_child(usa)

    return world

if __name__ == '__main__':
    print("""
    Enter the number which level you want to print data
    1 or 2 or 3
    """)
    level = int(input())
    tree = bulid_tree()
    tree.print_tree(level)
