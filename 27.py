'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1: 给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。 你不需要考虑数组中超出新长度后面的元素。

示例 2: 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
'''


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 记录是否开始遇到指定val
        length :int = len(nums)

        # 指向一个val值的指针
        pv: int = 0

        #永远在val后，指向非val值的指针
        pnv :int = 0

        # 记录val值出现的次数
        k :int = 0

        while(1):
            if(pv >= length-1 or pnv >= length-1):
                return int(length-k), nums

            if(nums[pv] != val):
                pv += 1
                pnv = pv
            elif(nums[pv] == val):
                # flag = 1
                pnv = self.findPnv(nums, val, pv)
                # exchange
                temp = nums[pv]
                nums[pv] = nums[pnv]
                nums[pnv] = temp
                k += 1

                pv += 1
                pnv += 1


    def findPnv(self, nums, val, pv):
        pnv = pv + 1
        while(1):
            if (nums[pnv] != val):
                return pnv
            else:
                pnv += 1

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    S = Solution()
    r = S.removeElement(nums, val)
    pass