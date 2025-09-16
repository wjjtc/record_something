class pair:
    """键值对"""

    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class ArrayHashTable:
    """基于数组实现的哈希表"""

    def __init__(self):
        """初始化100个桶"""
        self.buckets: list[pair | None] = [None] * 100

    def hash_func(self, key: int) -> int:
        return key % 100

    def get(self, key: int) -> str | None:
        """通过键获取值"""
        index: int = self.hash_func(key)
        res: pair | None = self.buckets[index]
        if res is None:
            return None
        return res.value

    def put(self, key: int, val: str) -> None:
        temp: pair = pair(key, val)
        index: int = self.hash_func(key)
        self.buckets[index] = temp

    def remove(self, key: int):
        """删除操作"""
        index: int = self.hash_func(key)
        # 置为 None ，代表删除
        self.buckets[index] = None


class Node(object):
    def __init__(self, key: int, val: str) -> None:
        self.key = key
        self.val = val
        self.next: Node | None = None


class HashMapChaining(object):
    """链式地址哈希表"""

    def __init__(self) -> None:
        self.size = 0  # 键值对数量
        self.capacity = 4  # 哈希表容量
        self.load_thres = 2.0 / 3.0  # 触发扩容的负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets: list[Node | None] = [None] * self.capacity  # 桶数组

    def hash_func(self, key: int) -> int:
        return key % self.capacity

    def get(self, key: int) -> str | None:
        index: int = self.hash_func(key)
        cur: Node | None = self.buckets[index]
        while cur is not None and cur.key != key:
            cur = cur.next
        if cur is None:
            return None
        return cur.val

    def load_factor(self) -> float:
        """负载因子"""
        return self.size / self.capacity

    def extend(self):
        """扩容哈希表"""
        # 暂存原哈希表
        buckets = self.buckets
        # 初始化扩容后的新哈希表
        self.capacity *= self.extend_ratio
        self.buckets = [None] * self.capacity
        self.size = 0
        # 将键值对从原哈希表搬运至新哈希表
        for i in buckets:
            while i is not None:
                self.put(i.key, i.val)
                i = i.next

    def put(self, key: int, val: str):
        if self.load_factor() >self.load_thres:
            self.extend()
        index: int = self.hash_func(key)
        tmp = self.buckets[index]
        cur = Node(key,val)
        cur.next = tmp
        self.buckets[index] = cur

