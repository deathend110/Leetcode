

class Solution:
    # 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。
    def isAnagram(self, s: str, t: str) -> bool:
        # 刨除不等长的情况
        length = len(s)
        if length != len(t):
            return False
        
        # 用一个数组来记录字符出现次数。记录s时+1，t时-1.若最后数组是全0，则True
        # 数组下标从0-25对应a-z。
        record = [0 for _ in range(26)]

        for i in range(length):
            record[ord(s[i]) - ord('a')] += 1

        for i in range(length):
            record[ord(t[i]) - ord('a')] -= 1

        if any(record):
            # 数组有非零元素。
            return False
        return True

if __name__ == "__main__":
    solution = Solution()
    s = "rat"
    t = "car"

    print(ord('a'))
    print(ord('z'))

    res = solution.isAnagram(s, t)
    pass