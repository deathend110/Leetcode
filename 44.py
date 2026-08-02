'''
【题目描述】
在一个城市区域内，被划分成了n * m个连续的区块，每个区块都拥有不同的权值，代表着其土地价值。目前，有两家开发公司，A 公司和 B 公司，希望购买这个城市区域的土地。
现在，需要将这个城市区域的所有区块分配给 A 公司和 B 公司。
然而，由于城市规划的限制，只允许将区域按横向或纵向划分成两个子区域，而且每个子区域都必须包含一个或多个区块。
为了确保公平竞争，你需要找到一种分配方式，使得 A 公司和 B 公司各自的子区域内的土地总价值之差最小。
注意：区块不可再分。

【输入描述】
第一行输入两个正整数，代表 n 和 m。
接下来的 n 行，每行输出 m 个正整数。

输出描述
请输出一个整数，代表两个子区域内土地总价值之间的最小差距。

【输入示例】
3 3
1 2 3
2 1 3
1 2 3


4 5
1 7 0 4 6
10 2 2 1 3
1 1 1 2 3
3 3 3 3 3


【输出示例】
0

【提示信息】
如果将区域按照如下方式划分：
1 2 | 3
2 1 | 3
1 2 | 3

两个子区域内土地总价值之间的最小差距可以达到 0。
'''

import sys

if __name__ == "__main__":
    n, m = (map(int, input().split(" ")))
    zone = []

    # 先算行列的和
    row_sum = []
    col_sum = []

    for line in sys.stdin:
        if not line.strip():
            break
        line_list = list(map(int, line.split()))
        zone.append(line_list)
        row_sum.append(sum(line_list))

    # n*m的区块，有n-1 * m-1 种划法
    # 列和
    for i in range(m):
        t = [row[i] for row in zone]
        col_sum.append(sum(t))

    # 有了rowsum和colsum，在这里区分即可。
    res :int = 0xefffffff

    for i in range(1, n):
        left = sum(row_sum[0:i])
        right = sum(row_sum[i:n])
        t = abs(left - right)
        if t < res:
            res = t

    for i in range(1, m):
            left = sum(col_sum[0:i])
            right = sum(col_sum[i:m])
            t = abs(left - right)
            if t < res:
                res = t

    print(res)
    pass
