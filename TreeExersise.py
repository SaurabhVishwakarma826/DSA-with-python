class TreeNode1:
    def __init__(self, name, degination):
        self.data = name
        self.degination = degination
        self.children = []
        self.parant = None

    def get_level(self):
        level = 0
        p = self.parant
        while p:
            level += 1
            p = p.parant
        return level

    def print_tree(self, property):
        if property == "both":
            value = self.data + " (" + self.degination + " )"
        elif property == "name":
            value = self.data
        else:
            value = self.degination
        space = " " * self.get_level() * 3
        prefix = space+"|__" if self.parant else ""
        print(prefix+value)
        if self.children:
            for child in self.children:
                child.print_tree(property)

    def add_child(self, child):
        child.parant = self
        self.children.append(child)

def bult_management(choise):
    vishw = TreeNode1("Vishwa","Infrastructure Head")
    vishw.add_child(TreeNode1("Dhaval","Cloud Manager"))
    vishw.add_child(TreeNode1("Abhijit","App Manager"))

    chinmay = TreeNode1("Chinmay","CTO")
    chinmay.add_child(vishw)
    chinmay.add_child(TreeNode1("Amir","Application Manager"))

    gels = TreeNode1("Gels","HR Head")
    gels.add_child(TreeNode1("Peter","Recruitment Manager"))
    gels.add_child(TreeNode1("Waqas","Policy Manager"))

    root = TreeNode1("Nipul","CEO")
    root.add_child(chinmay)
    root.add_child(gels)
    root.print_tree(choise)

if __name__ == '__main__':
    print("What would you like to print\nname\ndeginaion\nboth")
    choise = input()
    root_node = bult_management(choise)



