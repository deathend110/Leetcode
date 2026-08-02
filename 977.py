# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length :int = len(nums)

        # 在输入数组从左右向中间运动的指针
        left :int = 0
        right :int = length - 1

        # 结果数组
        results = [0 for i in range(length)]
        # 结果数组的指针
        pr :int = length - 1

        while(pr != -1):
            if(pow(nums[left], 2) >= pow(nums[right], 2)):
                results[pr] = pow(nums[left], 2)
                left += 1
                pr -= 1
            else:
                results[pr] = pow(nums[right], 2)
                right -= 1
                pr -= 1

        return results


if __name__ == "__main__":
    nums = [-4,-1,1,3,10]
    target = 3
    S = Solution()
    r = S.sortedSquares(nums)
    pass