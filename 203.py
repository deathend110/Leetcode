
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 输入list， 转为chain并返回头节点
    def asChainList(self, nums):
        length = len(nums)
        head = ListNode()
        p = head
        for i in range(length):
            p.val = nums[i]
            if(i == length - 1):
                break
            temp = ListNode()
            p.next = temp
            p = temp

        return head

    def printChainList(self, head):
        p = head
        while(p != None):
            print(p.val)
            p = p.next
        print("\n")

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head

        if head.next == None:
            if(head.val ==  val):
                head = None
            return head

        slow = head
        fast = head.next

        while(fast != None):
            # 特殊情况，删除头指针
            if(slow.val == val and slow == head):
                head = head.next
                slow = head
                fast = head.next
            elif(fast.val == val):
                slow.next = fast.next
                fast = slow.next
            else:
                fast = fast.next
                slow = slow.next

        while(slow != None):
            if(slow == head and slow.val == val):
                head = None
                slow = head
            else:
                slow = slow.next

        return head

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = head
        prev = dummy
        while cur:
            if cur.val == val:
                prev.next = cur.next
            # prev = prev.next
                cur = cur.next
            else:
                prev = prev.next
                cur = cur.next
        return dummy.next

if __name__ == "__main__":
    nums = [7,7,7,7]
    val = 7
    # nums = [1,2]
    # val = 1
    # nums = [1]
    # val = 2
    # nums = [1]
    # val = 1
    head = ListNode()
    head = head.asChainList(nums)
    head.printChainList(head)

    s = Solution()
    head = s.removeElements(head, val)
    head.printChainList(head)
    pass