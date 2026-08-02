'''
题目描述
给定一个整数数组 Array，请计算该数组在每个指定区间内元素的总和。

输入描述
第一行输入为整数数组 Array 的长度 n，接下来 n 行，每行一个整数，表示数组的元素。随后的输入为需要计算总和的区间，直至文件结束。

输出描述
输出每个指定区间内元素的总和。

输入示例
5
1
2
3
4
5
0 1
1 3



输出示例
3
9
'''

import sys

if __name__ == "__main__":
    n = int(input())

    # 获取数组
    nums = []
    for _ in range(n):
        nums.append(int(input()))

    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]

    # 获取下标并计算
    for line in sys.stdin:
        index = tuple(map(int, line.split()))

        print(prefix[index[1]+1] - prefix[index[0]])
    
    pass
