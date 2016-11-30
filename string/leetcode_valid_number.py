#-*- encoding: utf8 -*-
__author__ = 'flappy'


class Solution(object):
    def isNumber(self, s):
        """
            这种问题一般dfa，值得注意得是：
                1，dfa状态合并问题，
                2，只画有用得路径，
        :type s: str
        :rtype: bool
        """
        # row as current-state, key as step, value as next-state
        dfa_mat = [
            {'space':0, '+':1, '-':1, 'digit':2, '.':3},
            {'.':3, 'digit':2},
            {'digit':2, 'space':8, '.':9, 'e':5},
            {'digit':4},
            {'digit':4, 'e':5, 'space':8},
            {'digit':6, '+':7, '-':7},
            {'digit':6, 'space':8},
            {'digit':6},
            {'space':8},
            {'e':5, 'digit':4, 'blank':8}
        ]

        valid_states = {2, 4, 6, 8, 9}

        current_state = 0
        for c in s:
            key = c
            if unicode.isspace(c):
                key = 'space'
            elif c == '+' or c == '-' or c == '.' or c == 'e':
                key = c
            elif unicode.isdigit(c):
                key = 'digit'
            else:
                return False
            current_state = dfa_mat[current_state].get(key, -1)
            if current_state == -1:
                return False

        if current_state in valid_states:
            return True
        return False

def test():
    solution = Solution()
    def Print(s):
        print(s, solution.isNumber(s))
    Print(u".")
    Print(u"3.")
    Print(u"-0.1")
    Print(u"0e")
    Print(u"10e")
    Print(u"26.")
    Print(u"46.e3")
    Print(u".e3")
    Print(u"6e6.5")
    Print(u"6e+6.5")
    # print(solution.isNumber(u"0"))
    # print(solution.isNumber(u"11"))
    # print(solution.isNumber(u"0 "))
    # print(solution.isNumber(u" 0.1 "))
    # print(solution.isNumber(u"abc"))
    # print(solution.isNumber(u"1 a"))
    # print(solution.isNumber(u"2e10"))


if __name__ == '__main__':
    test()