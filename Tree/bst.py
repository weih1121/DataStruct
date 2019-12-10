class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_recursion(root, value):
    if not root:
        return Node(value)
    else:
        if root.value > value:
            root.left = insert(root.left, value)
        if root.value < value:
            root.right = insert(root.right, value)
        return root

def insert(root, value):
    if not root:
        root = Node(value)
        return root

    current = root
    parent = None
    while current:
        parent = current
        if current.value > value:
            current = current.left
        elif current.value < value:
            current = current.right

    if parent.value > value:
        parent.left = Node(value)
    else:
        parent.right = Node(value)
    return root

def travel(root):
    if root:
        travel(root.left)
        print(root.value)
        travel(root.right)  

def find_max(root):
    while root:
        if root.right:
            root = root.right
        else:
            return root.value

def find_min(root):
    while root:
        if root.left:
            root = root.left
        else:
            return root.value

def delete(root, value):
    if not root:
        return root
    
    if root.value > value:
        root.left = delete(root.left, value)
    elif root.value < value:
        root.right = delete(root.right, value)
    else:
        if not root.left:
            tmp = root.right
            root = None
            return tmp
        elif not root.right:
            tmp = root.left
            root = None
            return tmp
        else:
            right_min = find_min(root.right)
            root.value = right_min
            root.right = delete(root.right, right_min)
    return root 

def search_recursion(root, value):
    if not root:
        return False
    
    if root.value == value:
        return True
    
    if root.value > value:
        return search_recursion(root.left, value)
    else:
        return search_recursion(root.right, value)

def search(root, value):
    if not root:
        return False
    
    while root:
        if root.value == value:
            return True
        elif root.value > value:
            root = root.left
        else:
            root = root.right
    return False 

def get_parent(root, value):
    if not root:
        return None
    curr = root
    while curr:
        if curr.value < value:
            if curr.right.value == value:
                return curr
            else:
                curr = curr.right
        elif curr.value > value:
            if curr.left.value == value:
                return curr
            else:
                curr = curr.left

def delete_non_recursion(root, value):  # 其实还是用了递归 因为过于好实现
    if not root:
        return root
    
    current = root
    while current:
        if current.value < value:   # current value is less, find right sub tree 
            current = current.right
        elif current.value > value: # current value is larger, find left sub tree
            current = current.left
        else:                       # value equals to node.value
            if not current.right and current.left:
                parent = get_parent(root, value)
                parent.left = current.left
            elif not current.left and current.right:
                parent = get_parent(root, value)
                parent.right = current.left
            elif current.left and current.right:
                min_value = find_min(current.right)
                current.value = min_value
                if not current.right.left and not current.right.right:
                    current.right = None
                else:
                    delete_non_recursion(current.right, min_value)
            else:
                parent = get_parent(root, value)
                if parent.left == current:
                    parent.left = None
                elif parent.right == current:
                    parent.rigth = None
            return root
                    


if __name__ == "__main__":
    l = [50, 30, 20, 10, 40, 70, 60, 80]
    root = None
    for i in l:
        root = insert_recursion(root, i)
    max_value = find_max(root)
    print('max value is: %s' % max_value)
    min_value = find_min(root)
    print('min value is: %s' % min_value)
    is_find = search(root, 70)
    print('70 in the tree? %s' % is_find)
    delete_non_recursion(root, 20)
    print('delete 20 the tree is: (inorder travel)')
    travel(root)
    delete_non_recursion(root, 30)
    print('delete 30 the tree is: (inorder travel)')
    travel(root)
    delete_non_recursion(root, 50)
    print('delete 50 the tree is: (inorder travel)')
    travel(root)