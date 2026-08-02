# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        if n == 1:
            return [[1]]
        length = n*n
        nums = [i+1 for i in range(length)]
        res = [[0 for i in range(n)] for i in range(n)]
        y = 0
        x = 0
        # 记录消耗步长，等于n*n-1结束, 也是nums的指针
        np = 0
        # 当前圈的步长是当前圈边长n的n-1， 下一圈边长是n-2
        step = n - 1
        # 右，下，左，上
        # direct = [0,0,0,0]

        while(np < length): 
            # right
            for i in range(step):
                res[y][x] = nums[np]
                np += 1
                x += 1
            # x += 1

            # down
            for i in range(step):
                res[y][x] = nums[np]
                np += 1
                y += 1
            # y += 1

            # left
            for i in range(step):
                res[y][x] = nums[np]
                np += 1
                x -= 1
            # x -= 1

            # up
            for i in range(step):
                res[y][x] = nums[np]
                np += 1
                y -= 1
            # x -= 1

            n = n - 2
            step = n - 1
            x += 1
            y += 1
            if step == 0:
                res[y][x] = nums[np]
                break

        return res

        


if __name__ == "__main__":
    s = Solution()
    n :int = 1
    r = s.generateMatrix(n)

    pass

