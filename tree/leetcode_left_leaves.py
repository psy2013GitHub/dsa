# -*- encoding: utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if self.is_leaf(root): return 0
        return self.helper(root)

    def helper(self, node):

        if not node: return 0

        left = 0
        if node.left:
            if self.is_leaf(node.left):
                left = node.left.val
            else:
                left = self.helper(node.left)

        right = 0
        if node.right:
            if not self.is_leaf(node.right):
                right = self.helper(node.right)

        return left + right

    def is_leaf(self, node):
        return not node.left and not node.right