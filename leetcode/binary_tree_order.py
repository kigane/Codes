def inorder_traversal_stack(root):
    """
    先将向左走到尽头，将所有中途元素入栈。
    弹出元素，输出，
    如果有右子树：转到右子树，继续向左走到尽头并压栈
    如果没有右子树：继续从栈中弹出元素
    """
    def addAllLeft(node):
        while node:
            stack.append(node)
            node = node.left

    ret = []
    stack = []
    addAllLeft(root)
    while len(stack) != 0:
        curr = stack.pop()
        ret.append(curr.val)
        addAllLeft(curr.right)

    return ret


def inorder_traversal_stack2(root):
    ret = []
    stack = []
    # while stack or root: # 等价条件
    while len(stack) != 0 or root != None:
        if root != None:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            ret.append(root.val)
            root = root.right

    return ret


def inorder_traversal_recursive(root):
    if not root:
        return []

    ret = []
    ret += inorder_traversal_recursive(root.left)
    ret += [root.val]
    ret += inorder_traversal_recursive(root.right)

    return ret


def inorder_traversal_mirros(root):
    """
    在根节点移动之前，先找到其前驱节点(左子树的最右结点)，并将前驱结点的右指针指向根节点。
    当再次来到根节点时(通过前驱结点的右指针)，将前驱结点的右指针复原。即可恢复原树结构。
    """
    ret = []
    while root:
        predessor = root.left
        if predessor:
            while predessor.right and predessor.right != root:
                predessor = predessor.right

            if predessor.right is None:  # 第一次遍历到
                predessor.right = root
                root = root.left
                continue
            elif predessor.right == root:  # 遍历根节点的时候
                predessor.right = None

        ret.append(root.val)
        root = root.right
    return ret
