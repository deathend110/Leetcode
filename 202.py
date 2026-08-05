
from typing import List

# 编写一个算法来判断一个数 n 是不是快乐数。

# 「快乐数」 定义为：

# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

class Solution:
    def __init__(self):
        # 记录num拆分出的数组
        self.nums = []
        

    def isHappy(self, n: int) -> bool:
        d = set()
        
        while(n not in d):
            d.add(n)
            self.num2nums(n)
            n = self.numsPow()
            if n == 1:
                return True

        return False

    # 把计算数组平方和
    def numsPow(self) -> int:
        res = 0
        for i in self.nums:
            res += i * i
        return res

    # 把num拆分成数组
    def num2nums(self, n: int) -> None:
        self.nums = []
        str_n = str(n)
        for i in str_n:
            self.nums.append(i)
        self.nums = list(map(int, self.nums))
        return


if __name__ == "__main__":
    solution = Solution()
    num = 20

    res = solution.isHappy(num)
    pass