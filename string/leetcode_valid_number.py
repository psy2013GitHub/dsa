#-*- encoding: utf8 -*-
__author__ = 'flappy'


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 数字:0, .e:1
        dfa_mat = {0:{0,1}, 1:{0}}
        i = -1
        while i < len(s) - 1:
            i += 1
            if unicode.isspace(s[i]):
                continue
            else:
                break

        if s[i] == '-' or s[i] == '+':
            i += 1

        if not (unicode.isdigit(s[i]) or s[i]=='.'):
            return False

        digit_occurance, dot_occurance, e_occurance = False, False, False

        while i < len(s):
            if unicode.isdigit(s[i]):
                digit_occurance = True
                print('digit', s, s[i])
                if i + 1 < len(s):
                    if unicode.isdigit(s[i+1]):
                        print('1.1', s, s[i], s[i+1])
                        i += 2
                    elif (not e_occurance and s[i+1]=='e'):
                        if i + 2 < len(s):
                            if not unicode.isdigit(s[i+2]):
                                return False
                            else:
                                e_occurance = True
                                i += 3
                        else:
                            return False
                    elif (not e_occurance and not dot_occurance and s[i+1]=='.'):
                        dot_occurance = True
                        i += 2
                    elif unicode.isspace(s[i+1]):
                        i += 1
                        break
                    else:
                        return False
                else:
                    return True
            elif (not e_occurance and s[i] == 'e'):
                 print('e', s, s[i])
                 e_occurance = True
                 if i + 1 < len(s):
                    if unicode.isdigit(s[i+1]):
                        digit_occurance = True
                        print('.|e digit', s, s[i+1])
                        i += 2
                    elif s[i+1] == '+' or s[i+1] == '-':
                        i += 2
                    else:
                        return False
                 else:
                     return False
            elif (not e_occurance and not dot_occurance and s[i] == '.'):
                print('.', s, s[i])
                dot_occurance = True
                if i + 1 < len(s):
                    if unicode.isdigit(s[i+1]):
                        digit_occurance = True
                        print('.|e digit', s, s[i+1])
                        i += 2
                    elif digit_occurance and s[i+1] == 'e': # 46.e3
                        i += 1
                    else:
                        return False
                else:
                    if not digit_occurance:
                        return False
                    else:
                        return True
            else:
                # print('break', s, s[i])
                break

        while i < len(s):
            if not unicode.isspace(s[i]):
                print('no space', i ,s[i])
                return False
            i += 1

        return True

def test():
    solution = Solution()
    print(solution.isNumber(u"."))
    print(solution.isNumber(u"3."))
    print(solution.isNumber(u"-0.1"))
    print(solution.isNumber(u"3."))
    print(solution.isNumber(u"0e"))
    print(solution.isNumber(u"10e"))
    print(solution.isNumber(u"26."))
    print(solution.isNumber(u"46.e3"))
    print(solution.isNumber(u".e3"))
    print(solution.isNumber(u"6e6.5"))
    print(solution.isNumber(u"6e+6.5"))
    # print(solution.isNumber(u"0"))
    # print(solution.isNumber(u"11"))
    # print(solution.isNumber(u"0 "))
    # print(solution.isNumber(u" 0.1 "))
    # print(solution.isNumber(u"abc"))
    # print(solution.isNumber(u"1 a"))
    # print(solution.isNumber(u"2e10"))


if __name__ == '__main__':
    test()