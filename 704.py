
# 二分查找

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = left + int((right-left) / 2)

        while(left <= right):
            mid = left + int((right-left) / 2)
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                right = mid - 1
            elif(nums[mid] < target):
                left = mid + 1

        return -1


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 3
    S = Solution()
    r = S.search(nums, target)
    pass