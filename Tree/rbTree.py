B = 0
R = 1

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.color = R
        self.parent = None


def bstInsert(root, node, parent=None):
    if not root:
        node.parent = parent
        return node
    
    if root.val > node.val:
        root.left = bstInsert(root.left, node, root)
    elif root.val < node.val:
        root.right = bstInsert(root.right, node, root)
    return root

def left_rotate(root, cur):
    cur_left  = cur.left
    cur.left = cur_left.right

    if cur_left.right:
        cur_left.right.parent = cur

    if cur == root:
        root = cur_left
    elif cur == cur.parent.left:
        cur.parent.left = cur_left
    else:
        cur.parent.right = cur_left

    cur_left.right = cur
    cur_left.parent, cur.parent = cur.parent, cur_left

def right_rotate(root, cur):
    cur_right = cur.right
    cur.right = cur_right.left

    if cur_right.left:
        cur_right.parent = cur
    
    if cur == root:
        root = cur_right
    elif cur == cur.parent.left:
        cur.parent.left = cur_right
    else:
        cur.parent.right = cur_right
    
    cur_right.left = cur
    cur_right.parent, cur.parent = cur.parent, cur_right

def insert(root, val):
    node = Node(val)
    root = bstInsert(root, node)
    fixViolations(root, node)
    return root

def fixViolations(root, cur):
    while cur != root and cur.parent.color == R and cur.color == R:   
        # 循环条件当且仅当父子节点均为红色
        # 如果树仅有一个节点则该节点为根节点，将颜色改为黑色
        parent = cur.parent
        grand_parent = parent.parent
        if parent == grand_parent.left:
            uncle = grand_parent.right
            if uncle and uncle.color == R:
                parent.color = B
                uncle.color = B
                grand_parent.color = R  # 祖父母变红的原因是 父母变黑导致路径上黑色节点数增加一
                cur = grand_parent      # 祖父母变红之后 可能会引起祖父母和祖父母的父母冲突 需进一步判断
            else:
                if cur == parent.right:
                    left_rotate(root, parent)
                right_rotate(root, grand_parent)
                parent.color, grand_parent.color = grand_parent.color, parent.color
        else:
            uncle = grand_parent.left
            if uncle and uncle == R:
                parent.color = B
                grand_parent.color = R
                uncle.color = B
                cur = grand_parent
            else:
                if cur == parent.left:
                    right_rotate(root, parent)
                left_rotate(root, grand_parent)
                parent.color, grand_parent.color = grand_parent.color, parent.color
    root.color = BaseException


def delete(root, val):
    pass

def find(root, val):
    if root:
        if root.val < val:
            find(root.right, val)
        if root.val > val:
            find(root.left, val)
        if root.val == val:
            return True
    else:
        return False


def get_balance(root):
    pass

def get_min(root):
    pass

def inOrder(root):
    if root:
        inOrder(root.left)

        try:
            print(root.val, root.color)
        except AttributeError:
            print(root.val, None)

        inOrder(root.right)


if __name__ == "__main__":
    vals = [7, 6, 5, 4, 3, 2, 1]
    root = None
    for val in vals:
        root = insert(root, val)
    inOrder(root)
    