class TreeNode(object):
    """二叉树节点"""

    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinarySearchTree(object):
    """二叉搜索树"""

    def __init__(self) -> None:
        self.__root: TreeNode | None = None

    def search(self, num: int) -> TreeNode | None:
        """查找节点"""
        cur = self.__root
        # 循环查找，越过叶节点后跳出
        while cur is not None:
            # 目标节点在 cur 的右子树中
            if cur.val < num:
                cur = cur.right
            # 目标节点在 cur 的左子树中
            elif cur.val > num:
                cur = cur.left
            # 找到目标节点，跳出循环
            else:
                break
        return cur

    def insert(self, num: int) -> None:
        """插入节点"""
        if self.__root is None:
            self.__root = TreeNode(num)
            return
        cur: TreeNode | None = self.__root
        pre: TreeNode | None = None  # type: ignore
        while cur is not None:
            if cur.val == num:
                return
            pre = cur
            if cur.val > num:
                cur = cur.left
            else:
                cur = cur.right
        node = TreeNode(num)
        if num > pre.val:
            pre.right = node
        else:
            pre.left = node

    def remove(self, num: int) -> None:
        """删除节点"""
        # 若树为空，直接提前返回
        if self.__root is None:
            return
        # 循环查找，越过叶节点后跳出
        cur, pre = self._root, None
        while cur is not None:
            # 找到待删除节点，跳出循环
            if cur.val == num:
                break
            pre = cur
            # 待删除节点在 cur 的右子树中
            if cur.val < num:
                cur = cur.right
            # 待删除节点在 cur 的左子树中
            else:
                cur = cur.left
        # 若无待删除节点，则直接返回
        if cur is None:
            return
        # 子节点数量 = 0 or 1
        if cur.left is None or cur.right is None:
        # 当子节点数量 = 0 / 1 时， child = null / 该子节点
            child = cur.left or cur.right
            if cur == self.__root:
                self.__root = child
            else:
                if pre.left == cur:
                    pre.left = child
                else:
                    pre.right = child
        else:
            temp = cur.right
            while temp.left is not None:
                temp = temp.letf
            self.remove(temp.val)
            cur.val = temp.val