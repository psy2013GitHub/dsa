#-*- encoding: utf8 -*-
__author__ = 'flappy'

class Solution(object):
        def numDistinct(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: int
            """
            if len(s) < len(t):
                return 0

            state_mat = [[0, ] * (len(s) + 1) for _ in range(len(t) + 1)]
            state_mat[0][0] = 1
            for i in range(len(s)):
                state_mat[0][i + 1] = 1

            for j in range(len(t)):
                for i in range(len(s)):
                    if t[j] == s[i]:
                        state_mat[j + 1][i + 1] = state_mat[j][i] + state_mat[j + 1][i]
                    else:
                        state_mat[j + 1][i + 1] = state_mat[j + 1][i]
            return state_mat[-1][-1]

def test():
    solution = Solution()
    print(solution.numDistinct('', 'a'))
    print(solution.numDistinct('aa', 'aaa'))
    print(solution.numDistinct('aaa', 'aaa'))
    print(solution.numDistinct('rabbbbit', 'rabbit'))
    print(solution.numDistinct('rabbbbittt', 'rabbit'))


if __name__ == '__main__':
    test()