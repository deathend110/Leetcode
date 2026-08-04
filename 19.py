# Definition for singly-linked list.

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


# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建虚拟头节点并让fast指针和slow指针都指向头节点开始
        dummy :ListNode = ListNode()
        dummy.next = head
        fast :ListNode = dummy
        slow :ListNode = dummy

        
        # 先让fast走n+1步
        for _ in range(n+1):
            fast = fast.next

        # 然后让fast和slow一起走直到fast到达Null
        while(fast != None):
            fast = fast.next
            slow = slow.next

        # 删除slow.next,这里的slow.next就是我们的删除节点
        slow.next = slow.next.next
    
        return dummy.next
    

if __name__ == "__main__":
    LinkedList_1 = MyLinkedList()
    nums = [1]
    nums = [1,2,3,4,5]
    LinkedList_1.list2LinkerList(nums)
    n = 1
    n = 5
    # 头节点
    head :ListNode = LinkedList_1.dummy.next
    s = Solution()
    res = s.removeNthFromEnd(head=head, n=n)
    
    pass


