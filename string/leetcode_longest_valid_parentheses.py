#-*- encoding: utf8 -*-
__author__ = 'flappy'

'''
    基本思路: stack维护分界符
    难点:
        1, 将0, len(s)+1推入stack
        2, 遇到')', 分情况pop, 可能')'本身是分界符
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1, ]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i+1)
            elif c == ')':
                if len(stack) > 0 and stack[-1] > -1:
                    stack.pop()
                else:
                    stack.append(-(i+1))
        stack[0] = 0
        stack.append(len(s)+1)
        max_len, idx = 0, len(stack) - 1
        while idx > 0:
            x1 = stack[idx] if stack[idx] > 0 else -stack[idx]
            x2 = stack[idx-1] if stack[idx-1] > 0 else -stack[idx-1]
            if max_len < x1 - x2 - 1:
                max_len = x1 - x2 - 1
            idx -= 1

        return max_len




def test():
    solution = Solution()
    print(solution.longestValidParentheses("(()"))
    print(solution.longestValidParentheses(")()()("))
    print(solution.longestValidParentheses(")("))
    print(solution.longestValidParentheses("()"))

if __name__ == '__main__':
    test()
