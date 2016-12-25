#-*- encoding: utf8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0,]
        self.helper(root, 0, res)
        return res[0]

    def helper(self, root, pre_sum, res):
        if not root:
            return
        pre_sum = pre_sum * 10 + root.val
        if not root.left and not root.right:
            res[0] += pre_sum
            return
        self.helper(root.left, pre_sum, res)
        self.helper(root.right, pre_sum, res)