__author__ = 'flappy'

class Solution1(object):
    def isMatch(self, s, p):
        if s == p:
            return True
        m = len(s)
        n = len(p)

        T = [[False for j in range(n+1)] for i in range(m+1)]

        T[0][0] = True

        #  Deals with patterns like a* or a*b* or a*b*c*
        for i in range(1, n+1):
            if p[i-1] == '*':
                T[0][i] = T[0][i-2]

        if not s:
            return T[-1][-1]

        s = " "+s
        p = " "+p


        for i in range(1, m+1):
            for j in range(1, n+1):

                if s[i] == p[j] or p[j] == '.':
                    T[i][j] = T[i-1][j-1]

                elif p[j] == '*':
                    if j > 1:
                        T[i][j] = T[i][j-2]

                    if s[i] == p[j-1] or p[j-1] == '.':
                        T[i][j] = T[i][j] or T[i-1][j]
                else:
                    T[i][j]  = False

        return T[i][j]

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        state_mat = [[False, ] * (len(s)+1) for _ in range(len(p)+1)]

        state_mat[0][0] = True
        for j in range(0, len(p)):
            state_mat[j+1][0] = p[j] == '*' and state_mat[j-1][0]

        for j in range(len(p)):
            for i in range(len(s)):
                if p[j]==s[i] or p[j]=='.':
                    state_mat[j+1][i+1] = state_mat[j][i]
                    # print(i, j, 1, s[i], p[j], state_mat[j+1][i+1])
                else:
                    if p[j] == '*':
                        # 很简单, `x*`要么匹配0个, 要么匹配多个
                        tmp1 = False
                        if j > 1: # 匹配0次
                            tmp1 = state_mat[j-1][i+1]

                        tmp2 = False
                        if s[i]==p[j-1] or p[j-1]=='.': # 匹配多次
                            tmp2 = state_mat[j+1][i]

                        state_mat[j+1][i+1] = tmp1 or tmp2
                    else:
                        state_mat[j+1][i+1] = False

        return state_mat[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    # print(solution.isMatch('aa', 'a*'))
    # print(solution.isMatch('aaa', 'a*'))
    # print(solution.isMatch('aaa', 'a*'))
    # print(solution.isMatch('ab', 'c*a*b*'))
    # print(solution.isMatch('abcd', 'd*'))
    # print(solution.isMatch('abcd', 'abdc'))
    print(solution.isMatch('aaa', 'ab*a*c*a'))


