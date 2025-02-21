class ListNode:
    """双向链表"""
    def __init__(self, val: int):
        self.val: int = val                 # 节点值
        self.next: ListNode | None = None   # 下一节点的引用
        self.prev: ListNode | None = None   # 上一节点的引用