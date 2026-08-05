
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i in range(len(nums)):
            if (nums[i] in d and i != d[nums[i]]):
                return [i, d[nums[i]]]            
            diff = target - nums[i]
            d[diff] = i


        return None
if __name__ == "__main__":
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    nums = [3,2,4]
    target = 6
    res = solution.twoSum(nums=nums, target=target)
    pass