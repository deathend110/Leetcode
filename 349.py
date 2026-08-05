# 给定两个数组 nums1 和 nums2 ，返回 它们的 交集 。
# 输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序

from typing import List

class Solution:
    # 给定两个数组 nums1 和 nums2 ，返回 它们的 交集 。
    # 输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = set(nums1)
        d2 = set(nums2)

        d = d1 & d2
        return list(d)

if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    res = solution.intersection(nums1, nums2)
    pass