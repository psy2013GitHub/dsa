__author__ = 'flappy'

class Solution(object):
    def isMatch(self, s, p):
        pass

class DPSolution(Solution):
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

class RecursiveSolution(Solution):
     def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.helper(s, p, 0, 0)
        # return self.helper1(s, 0, p, 0)

     def helper(self, s, p, curr_s_pos, curr_p_pos):
         ret = False
         # if curr_s_pos >= len(s): # s 读完, 就看p是不是 a*b*c*得形式
         #     while curr_p_pos < len(p):
         #         if p[curr_p_pos]=='*':
         #             curr_p_pos += 1
         #         elif curr_p_pos + 1 < len(p) and p[curr_p_pos+1] == '*':
         #             curr_p_pos += 2
         #         else:
         #             return False
         #     return True
         if curr_s_pos >= len(s) or curr_p_pos >= len(p):
             print(1, curr_s_pos, curr_p_pos)
             return curr_s_pos >= len(s) and curr_p_pos >= len(p)

         if curr_p_pos+1 < len(p) and p[curr_p_pos+1] == '*':
             if curr_s_pos < len(s) and (s[curr_s_pos]==p[curr_p_pos] or p[curr_p_pos]=='.'): # 匹配多个
                ret = self.helper(s, p, curr_s_pos+1, curr_p_pos)
             ret = ret or self.helper(s, p, curr_s_pos, curr_p_pos+2) # s已经读完, 或者匹配0个
         # !!! below condition, you can't write: `curr_p_pos < len(p) and curr_s_pos < len(s) and s[curr_s_pos]==p[curr_p_pos] or p[curr_p_pos]=='.'`
         # if so, you may get out of index error, because python will calculate `p[curr_p_pos]=='.'` first
         elif curr_p_pos < len(p) and curr_s_pos < len(s) and (s[curr_s_pos]==p[curr_p_pos] or p[curr_p_pos]=='.'):
                ret = self.helper(s, p, curr_s_pos+1, curr_p_pos+1) # 匹配char by char
         else:
             return False
         return ret

     def helper1(self, s, si, p, pi):
         if si == len(s) and p == len(p):
             return True
         if pi+1<len(p) and p[pi+1] == '*':
            return self.helper1(s,si,p,pi+2) or ((s[si]==p[pi] or p[pi]=='.') and si<len(s) and self.helper1(s,si+1,p,pi)); #//match 1 or more occurence case
         else:
            return (si<len(s) and (s[si]==p[pi] or p[pi]=='.')) and self.helper1(s, si+1, p, pi+1) #//match char by char case


def test(solution):
    # print(solution.isMatch('aa', '.*'))
    # print(solution.isMatch('aa', 'a*'))
    # print(solution.isMatch('aa', 'a'))
    # print(solution.isMatch('aaa', 'a*'))
    # print(solution.isMatch('aaa', 'a*'))
    # print(solution.isMatch('ab', 'c*a*b*'))
    # print(solution.isMatch('abcd', 'd*'))
    # print(solution.isMatch('abcd', 'abdc'))
    # print(solution.isMatch('aaa', 'ab*a*c*a'))
    s, p = "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"
    # print(s[13], p[14])
    print(solution.isMatch(s, p))

def testDP():
    solution = DPSolution()
    test(solution)

def testRecursive():
    solution = RecursiveSolution()
    test(solution)


if __name__ == '__main__':
    # testDP()
    testRecursive()


