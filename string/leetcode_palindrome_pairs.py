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
            if w1 in words_idx_dict and words_idx_dict[w1] != i: # in case of `self-palindrome`
                print('1,', i, w, w1, words_idx_dict[w1])
                res.append([words_idx_dict[w1], i])
                # res.append([i, words_idx_dict[w1]])
            # 2, candidate in left, e.g. 'ssl', 'l'
            j = 0
            while j < len(w) + 1:
                if self.is_self_palindrome(w, 0, j):
                    w1 = w[j:][::-1]
                    if w1 in words_idx_dict and words_idx_dict[w1] != i:
                        print('2.1', i, w, w1, words_idx_dict[w1], j)
                        res.append([words_idx_dict[w1], i])
                        # if w1 == '':
                        #     res.append([i, words_idx_dict[w1]])
                        #     print('2.2', i, w, w1, words_idx_dict[w1], j)
                j += 1
            # 3, candidate in right, e.g. 'lss', 'l'
            j = len(w) - 1
            while j > -1:
                if self.is_self_palindrome(w, j, len(w)):
                    w1 = w[:j][::-1]
                    if w1 in words_idx_dict and words_idx_dict[w1] != i:
                        print('3.1', i, w, w1, words_idx_dict[w1], j)
                        res.append([i, words_idx_dict[w1]])
                        # if w1 == '':
                        #     res.append([i, words_idx_dict[w1]])
                        #     print('3.2', i, w, w1, words_idx_dict[w1], j)
                j -= 1

        return res

    def brute_force(self, words):
        res = []
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i==j: continue
                if self.is_palindrome(w1, w2):
                    res.append([i, j])
        # print(res)
        return res

    def is_self_palindrome(self, w, l, r):
        if r < l:
            return False
        if l == r: # ''
            return True
        while l < r:
            if w[l] != w[r-1]:
                return False
            l += 1
            r -= 1
        return True

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
    # print(solution.palindromePairs(["bat", "tab", "cat"]))
    # [[0, 1], [1, 0]]
    # print(solution.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
    # [[0, 1], [1, 0], [3, 2], [2, 4]]
    print(solution.palindromePairs(["a","b","c","ab","ac","aa"]))
    # [[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]]

if __name__ == '__main__':
    # unittest()
    test()
