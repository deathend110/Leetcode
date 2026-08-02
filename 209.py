# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
# 子数组是：连续！！ 非空！！的序列


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int: 
        if (target == sum(nums)):
            return len(nums)
        if target in nums:
            return 1

        res = 0
        lenght = len(nums)
        left = 0
        right = 1

        while(left != right and right <= lenght):
            if(sum(nums[left:right]) < target):
                right += 1
            elif(sum(nums[left:right]) >= target):
                res = len(nums[left:right])
                left += 1

        return res
