
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
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p = head

        while(p != None):
            # 特殊情况，删除头指针
            if(p.val == val and p == head):
                head = head.next
                p = head
            elif(p.next.val == val):
                p.next = p.next.next
                p = p.next
            else:
                p = p.next

        return head

if __name__ == "__main__":
    nums = [1,2,6,3,4,5,6]
    val = 6
    head = ListNode()
    head = head.asChainList(nums)

    s = Solution()
    head = s.removeElements(head, val)
    pass