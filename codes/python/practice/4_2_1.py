class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val                 # 节点值
        self.next: ListNode | None = None   # 指向下一节点的引用


if __name__ == "__main__":

    # 初始化链表 1 -> 3 -> 2 -> 5 -> 4
    # 初始化各个节点
    n0 = ListNode(1)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(5)
    n4 = ListNode(4)

    # 构建节点之间的引用
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    # 将尾节点指向首节点构成环形链表
    n4.next = n0

    head = n0
    count = 0
    while count < 10:
        print(head.val)
        head = head.next
        count +=1