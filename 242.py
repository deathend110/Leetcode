

class Solution:
    # 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        set_s = list()
        set_t = list()
        for i in range(len(s)):
            set_s.append(s[i])
            set_t.append(t[i])

        set_s = sorted(set_s)
        set_t = sorted(set_t)

        if set_s == set_t:
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"

    res = solution.isAnagram(s, t)
    pass