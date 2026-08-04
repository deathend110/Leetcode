#  环形链表 II

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        # 创建虚拟头节点。
        self.dummy :ListNode = ListNode()
        # 尾节点
        self.tail :ListNode = self.dummy
        # 长度
        self.size = 0

    # 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。index：0开
    def get(self, index: int) -> int:
        p :ListNode = self.dummy.next
        res = -1
        i = 0
        while(p != None):
            if(i == index):
                res = p.val
                break
            i += 1
            p = p.next

        return res

    # 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
    def addAtHead(self, val: int) -> None:
        p :ListNode = ListNode(val=val)
        p.next = self.dummy.next
        self.dummy.next = p
        if self.size == 0:
            self.tail = p
        self.size += 1
        return

    # 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
    def addAtTail(self, val: int) -> None:
        self.tail.next =  ListNode(val=val)
        self.tail = self.tail.next
        self.size += 1
        return

    # 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。
    # 如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。
    # 如果 index 比长度更大，该节点将 不会插入 到链表中。
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        prev.next = ListNode(val, prev.next)
        self.size += 1

    # 如果下标有效，则删除链表中下标为 index 的节点。
    def deleteAtIndex(self, index: int) -> None:
        p :ListNode = self.dummy
        pi = 0
        while (p != None):
            if (pi == index and p.next != None):
                if p.next == self.tail:
                    self.tail = p
                # 此时p->next != Null，p是中间节点
                p.next = p.next.next
                self.size -= 1
                break
            pi += 1
            p = p.next 
        return

    # 输入list， 刷新为这个对象存储的LinkedList
    def list2LinkerList(self, nums):
        # 先清空原链表
        self.dummy.next = None
        self.tail = self.dummy
        self.size = 0

        # 逐个追加，不使用 len() 和下标访问
        for val in nums:
            self.addAtTail(val)

    # 输出链表
    def printLinkedList(self):
        p :ListNode = self.dummy.next
        print("{", end="")
        while(p != None):
            print(p.val, end=", ")
            p = p.next
        print("}")

    # 返回链表长度
    def __len__(self):
        return self.size


# 依据参数创建环形链表.返回单个表头. 没有环形也返回。
def createCircleLinkedList(nums: list, pos: int) -> Optional[ListNode]:
    LinkedList = MyLinkedList()
    LinkedList.list2LinkerList(nums)

    # 直接返回表头，没有环形
    if pos == -1:
        return LinkedList.dummy.next

    # 环形存在，直接让链表的tail.next指向pos指向的链表节点。
    p :ListNode = LinkedList.dummy.next
    for _ in range(pos):
        p = p.next

    LinkedList.tail.next = p

    return LinkedList.dummy.next

class Solution:
    # 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
    # index 0开
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 暴力解答 用一个字典存储，key = id，value = node指针。若发现重复id则返回对应的value
        NodesDict: dict[int, ListNode] = {}

        p: ListNode = head
        while(p != None):
            if( id(p) in NodesDict):
                # p地址已存在，直接返回pid对应的节点
                return NodesDict[id(p)]
            # 不存在，保存这个节点并更新
            NodesDict[id(p)] = p
            p = p.next
        
        return None


if __name__ == "__main__":
    intersectVal = 8
    nums = [3,2,0,-4]
    pos = -1

    # intersectVal = 1
    # listA = [1, 1,2,3]
    # listB = [1,1,2,3]
    # skipA = 1
    # skipB = 1

    head: ListNode = None
    head = createCircleLinkedList(nums, pos)

    s = Solution()
    res = s.detectCycle(head)
    
    pass