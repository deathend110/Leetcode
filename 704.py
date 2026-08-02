
# 二分查找

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right  = len(nums)
        mid = int(right / 2)

        while(1):
            if(nums[mid] == target):
                return mid
            elif(nums[mid] < target and left != mid):
                left = mid
                mid = int((left + right) / 2)
            elif(nums[mid] > target and left != mid):
                right = mid
                mid = int((left + right) / 2)
            elif(left == right or left == mid or mid == right):
                return - 1


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 3
    S = Solution()
    r = S.search(nums, target)
    pass