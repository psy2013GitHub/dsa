#-*- encoding: utf8 -*-
__author__ = 'flappy'

# 思路:
#    什么是回文? 就是镜像和自己相等
#    this problem, 先找到最长子回文串, 然后补完即可

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = s[::-1]
        i = 0
        l = len(s)
        while i < l:
            if s[0:l-i] == v[i:]: # 找到最长自回文字串
                break
            i = i + 1
        s = v[0:i] + s
        return s


def test():
    solution = Solution()
    assert solution.shortestPalindrome("aacecaaa")=="aaacecaaa"
    print(solution.shortestPalindrome("bbcecaaa"))
    assert solution.shortestPalindrome("abcd")=="dcbabcd"

if __name__ == '__main__':
    test()