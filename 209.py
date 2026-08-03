# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
# 子数组是：连续！！ 非空！！的序列


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int: 
        if (target == sum(nums)):
            return len(nums)
        if target in nums:
            return 1

        res = 0xffffffff
        lenght = len(nums)
        left = 0
        right = 0
        cur_sum = nums[left]

        while(right < lenght):
            if(cur_sum < target):
                right += 1
                if right >= lenght:
                    break
                cur_sum += nums[right]
            elif(cur_sum >= target):
                if right - left + 1 < res:
                    res = right - left + 1
                cur_sum -= nums[left]
                left += 1

        if res == 0xffffffff:
            res = 0
        return res

    
if __name__ == "__main__":
    nums = [2,3,1,2,4,3]
    target = 7
    S = Solution()
    r = S.minSubArrayLen(target, nums)
    pass