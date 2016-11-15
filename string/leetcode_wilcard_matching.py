__author__ = 'flappy'

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        state_mat = [[False, ] * (len(s)+1) for _ in range(len(p)+1)]
        state_mat[0][0] = True

        i = 0
        while i < len(p):
            # state_mat[j+1][0] = (state_mat[j][0] or state_mat[j-1][0]) and p[j]=='*'
            state_mat[j+1][0] = (state_mat[j][0]) and p[j]=='*'
            i += 1

        i = 0
        while i < len(s):
            state_mat[0][i+1] = False
            i += 1

        for j in range(len(p)):
            for i in range(len(s)):
                if s[i] == p[j]:
                    # print('1', i, j)
                    state_mat[j+1][i+1] = state_mat[j][i]
                elif p[j] == '?':
                    state_mat[j+1][i+1] = state_mat[j][i]
                    # print('2', i, j)
                elif p[j] == '*':
                    state_mat[j+1][i+1] = state_mat[j+1][i] or state_mat[j][i+1]
                # else:
                #     state_mat[j+1][i+1] = False
                #     print('4', i, j)
        # print(state_mat)
        return state_mat[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    # print(solution.isMatch('aa', 'a'))
    # print(solution.isMatch('aa', 'aa'))
    # print(solution.isMatch('aaa', 'aa'))
    # print(solution.isMatch('aa', '*'))
    # print(solution.isMatch('aa', 'a*'))
    # print(solution.isMatch('ab', '?*'))
    print(solution.isMatch('aab', 'c*a*b'))
    # print(solution.isMatch('aab', 'a*b'))
    # print(solution.isMatch('c', 'a*'))
    # print(solution.isMatch('c', 'a*b'))
