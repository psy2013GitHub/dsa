#-*- encoding: utf8 -*-
__author__ = 'flappy'

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []

        words_idx_dict = {w:i for i, w in enumerate(words)}

        for i, w in enumerate(words):
            # 1, 'abc', 'bca'
            w1 = w[::-1]
            if w1 in words_idx_dict:
                res.append([words_idx_dict[w1], i])
                res.append([i, words_idx_dict[w1]])
            # 2, 'l', 'ssl'


    def brute_force(self, words):
        res = []
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i==j: continue
                if self.is_palindrome(w1, w2):
                    res.append([i, j])
        # print(res)
        return res

    def is_palindrome(self, w1, w2):
        idx1, idx2 = 0, len(w2) + len(w1) - 1
        while idx2 > idx1:
            c1 = w1[idx1] if idx1 < len(w1) else w2[idx1 - len(w1)]
            c2 = w2[idx2 - len(w1)] if idx2 >= len(w1) else w1[idx2]
            if c1 != c2:
                return False
            idx1 += 1
            idx2 -= 1
        return True


def unittest():
    solution = Solution()
    solution.is_palindrome('l', 'ssl')
    solution.is_palindrome('tab', 'bat')


def test():
    solution = Solution()
    assert solution.palindromePairs(["bat", "tab", "cat"])==[[0, 1], [1, 0]]

if __name__ == '__main__':
    unittest()
    test()
