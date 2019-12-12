class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1     # 树的最小高度为叶子节点层 1
    

def get_height(node):
    '''
        获取avl树节点的高度
    '''
    if not node:
        return 0
    return node.height

def get_balance_factor(node):
    '''
        根据avl树的子树高度差计算平衡因子
    '''
    if not node: 
        return 0 
    return get_height(node.left) - get_height(node.right)

def left_rotate(node):
    '''
        x: new root
        y: x.left
    '''
    x = node.right
    y = x.left
    x.left = node
    node.right = y
    node.height = max(get_height(node.left), get_height(node.right)) + 1 # 左子树 先更新
    x.height = max(get_height(x.left), get_height(x.right)) + 1          # root 后更新
    return x

def right_rotate(node):
    '''
        x: new root
        y: x.right
    '''
    x = node.left
    y = x.right
    x.right = node
    node.left = y
    node.height = max(get_height(node.left), get_height(node.right)) + 1 # 同上
    x.height = max(get_height(x.left), get_height(x.right)) + 1          # 同上
    return x

def insert(root, val):
    '''
        1. 执行bst树插入操作
        2. 更新插入节点祖先节点的高度
        3. 计算祖先节点的平衡因子
        4. 根据平衡因子以及左旋右旋情况进行树调整
    '''
    if not root:
        root = Node(val)
        return root
    
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    root.height = max(get_height(root.left), get_height(root.right)) + 1

    balance_factor = get_balance_factor(root)

    if balance_factor > 1 and val < root.left.val:
        return right_rotate(root)

    if balance_factor > 1 and val > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if balance_factor < -1 and val > root.right.val:
        return left_rotate(root)

    if balance_factor < -1 and val < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def preorder_travel(root):
    '''
        先序遍历
    '''
    if root:
        print(root.val, end=' ')
        preorder_travel(root.left)
        preorder_travel(root.right)

def get_min(root):
    '''
        获取avl树中的最小值
    '''
    while root:
        if root.left:
            root = root.left
        else:
            return root.val

def delete(root, val):
    '''
        删除avl树中值为val的节点
        第一步: 执行正常的bst树节点删除操作
        第二步: 如果树只有一个节点则删除后直接返回
        第三步: 更新删除后祖先节点的高度
        第四步: 计算平衡因子并根据平衡因子进行avl树的旋转
    '''
    if not root:
        return root
    
    if root.val > val:                      # 根节点值大于val 递归删除左子树
        root.left = delete(root.left, val)
    elif root.val < val:
        root.right = delete(root.right, val) # 根节点值小于val, 递归删除右子树
    else:
        if not root.left:                    # 根节点值为val 第一种情况没有左子树， 返回右子树的根节点
            tmp = root.right
            root = None
            return tmp
        elif not root.right:                 # 根节点的值为val, 第二种情况没有右子树, 返回左子树的根节点
            tmp = root.left
            root = None
            return tmp
        else:                                # 第三种情况既有左子树又有右子树， 将节点的值改为右子树最小节点的值(root节点的后继), 递归删除右子树中节点值为tmp的节点
            tmp = get_min(root.right)
            root.val = tmp
            root.right = delete(root.right, tmp)

    # 只有一个节点 删除之后树为空
    if root is None: 
        return root 

    # 更新节点以及祖先节点的高度
    root.height = 1 + max(get_height(root.left), 
                        get_height(root.right)) 

    # 计算当前节点的平衡因子 
    balance = get_balance_factor(root) 

    # 平衡银子大于1 判断根的左子树平衡因子
    # 左子树平衡因子大于等于0 说明根节点左子树的左孩子高度大于等于根节点左子树有孩子 属于左左情况
    # 相反属于右右情况
    #  平衡因子小于-1 则判断根节点右子树平衡因子情况 并以此划分两种情况代码如下 

    if balance > 1 and get_balance_factor(root.left) >= 0: 
        return right_rotate(root) 

    if balance > 1 and get_balance_factor(root.left) < 0: 
        root.left = left_rotate(root.left) 
        return right_rotate(root) 

    if balance < -1 and get_balance_factor(root.right) <= 0: 
        return left_rotate(root) 
 
    if balance < -1 and get_balance_factor(root.right) > 0: 
        root.right = right_rotate(root.right) 
        return left_rotate(root) 

    return root




if __name__ == "__main__":
    import random
    vals = [random.randint(1, 99) for x in range(9)]
    root = None
    for val in vals:
        root = insert(root, val)
    print('My tree is: ')
    preorder_travel(root)
    print()

    key = random.choice(vals)
    root = delete(root, key) 

    print('After delete {} my tree is: '.format(key))
    preorder_travel(root)


