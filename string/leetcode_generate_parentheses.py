__author__ = 'flappy'

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        n_left, n_right = n, n
        self.helper(res, '(', n_left-1, n_right)
        return res

    def helper(self, res, curr_str, n_left, n_right):
        if n_left == 0 and n_right == 0:
            res.append(curr_str)
        if n_left > 0:
            self.helper(res, curr_str+'(', n_left-1, n_right)
        if n_right > 0 and n_left < n_right:
            self.helper(res, curr_str+')', n_left, n_right-1)
