#-*- encoding: utf8 -*-
__author__ = 'flappy'

class Solution(object):

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        self.count, self.s, self.t = 1, s, t
        self.brute_force(0, 0, 0)
        return self.count

    def brute_force(self, i, j, curr_count):
        '''
            从左到右匹配, 直到匹配到j为止, 遇到重复得计算组合数。
            time complexity: O(n^2)
        :param i:
        :param j:
        :param curr_count:
        :return:
        '''
        if i >= len(self.t):
            if self.count == 0:
                self.count = 1
            return

        if j >= len(self.t):
            candidate = 1
            while i < len(self.s) and i > 0 and self.s[i] == self.s[i-1]:
                print('---***', i, j, self.s[:i+1], self.t[:j+1], candidate)
                candidate += 1
                i += 1
            if candidate > 1:
                self.count *= self.C(candidate, 1)
            self.brute_force(i, 0, curr_count)

        # print(1)
        while i < len(self.s):
            if self.s[i] != self.t[j]:
                i += 1
            else:
                break

        # print(2)
        if i >= len(self.s) and not j >= len(self.t):
            self.count = 0
            return

        # print(3)
        # print(i, j, self.s[:i+1], self.t[:j+1])
        raw_i, raw_j, necessary_repeat, candidate, cum_prod = i, j, 0, 0, 0
        while i < len(self.s) and j < len(self.t):
            if self.s[i] == self.t[j]:
                if j > 0 and self.t[j] == self.t[j-1]:
                    necessary_repeat += 1
                i += 1
                j += 1
            else:
                necessary_repeat += 1
                candidate = necessary_repeat
                while i > 0 and self.s[i] == self.s[i-1]:
                    # print('***', i, j, self.s[:i+1], self.t[:j+1], candidate)
                    candidate += 1
                    i += 1

                print('***', i, j, self.s[:i+1], self.t[:j+1], candidate, necessary_repeat)


                if candidate > 1:
                    self.count *= self.C(candidate, necessary_repeat)


                # print('...', i, j, self.s[:i+1], self.t[:j+1])
                break

        # print(4)
        self.brute_force(i, j, curr_count)

    def C(self, m, n):
        '''
            calc `latex: C_{m}^n`
        :param m:
        :param n:
        :return:
        '''
        res = 1
        while m > n:
            res *= m
            m -= 1
        return res

def test():
    solution = Solution()
    print(solution.numDistinct('', 'a'))
    print(solution.numDistinct('aa', 'aaa'))
    print(solution.numDistinct('aaa', 'aaa'))
    print(solution.numDistinct('rabbbbit', 'rabbit'))
    print(solution.numDistinct('rabbbbittt', 'rabbit'))


if __name__ == '__main__':
    test()