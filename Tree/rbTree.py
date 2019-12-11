B = 0
R = 1

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.color = R
        self.parent = None
        self.height = 1


def bstInsert(root, val, parent=None):
    '''
    '''
    if not root:
        tmp = Node(val)
        tmp.parent = parent
        return tmp
    
    if root.val > val:
        root.left = bstInsert(root.left, val, root)   
    elif root.val < val:
        root.right = bstInsert(root.right, val, root)
    return root


def delete(root, val):
    pass

def find(root, val):
    pass

def left_rotate(root):
    pass

def right_rotate(root):
    pass

def get_balance(root):
    pass

def get_min(root):
    pass

def inOrder(root):
    if root:
        inOrder(root.left)

        try:
            print(root.val, root.parent.val)
        except AttributeError:
            print(root.val, None)

        inOrder(root.right)


if __name__ == "__main__":
    vals = [50, 30, 20, 10, 40, 70, 60, 80]
    root = None
    for val in vals:
        root = bstInsert(root, val)
    inOrder(root)
    