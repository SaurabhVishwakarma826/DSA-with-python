class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, val):
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

    def in_order_travser(self):
        element = []
        if self.left:
            element += self.left.in_order_travser()
        element.append(self.data)
        if self.right:
            element += self.right.in_order_travser()
        return element

    def post_order_travser(self):
        element = []
        if self.left:
            element += self.left.post_order_travser()
        if self.right:
            element += self.right.post_order_travser()
        element.append(self.data)
        return element

    def pre_order_travser(self):
        element = []
        element.append(self.data)
        if self.left:
            element += self.left.pre_order_travser()
        if self.right:
            element += self.right.pre_order_travser()
        return element

    def min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.min()

    def max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.max()

    def sum(self):
        left_sum = self.left.sum() if self.left else 0
        right_sum = self.right.sum() if self.right else 0
        return left_sum + self.data + right_sum

    def delet(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delet(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delet(val)
        else:
            if self.right is None and self.left is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            max_val = self.left.max()
            self.data = max_val
            self.left = self.left.delet(max_val)
        return self

def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    element = [15,12,7,14,27,20,23,88]
    print("Elements are : ",element)
    binary_tree = build_tree(element)
    print("After deleting 23",binary_tree.delet(23))
    print("In order traverser : ",binary_tree.in_order_travser())
    print("Pre order traverser : ",binary_tree.pre_order_travser())
    print("Post order traverser : ",binary_tree.post_order_travser())
    print("Is 14 present in tree : ",binary_tree.search(14))
    print("Is 5 present in  tree : ",binary_tree.search(5))
    print("Sum of binary tree : ",binary_tree.sum())
    print("Minimum number in binary tree : ",binary_tree.min())
    print("Maximum number in binary tree : ",binary_tree.max())
    name = ['Saurabh','Vishal','Reema','Vikash','Komal']
    binary_tree1 = build_tree(name)
    print("In order traverser name : ",binary_tree1.in_order_travser())

