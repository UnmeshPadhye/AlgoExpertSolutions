from binarytree import tree, bst

def minHeightBst(array):
    # With the sorted array, we can select root as the middle element to maximize the tree balancing
    mid_index = len(array) // 2
    root = BST(array[mid_index])
    if mid_index > 0:
        root.left = minHeightBst(array[0:mid_index])
    if len(array) -1 > mid_index:
        root.right = minHeightBst(array[mid_index:len(array)])
    
    return root
	

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
