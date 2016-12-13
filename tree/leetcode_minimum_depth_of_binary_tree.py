# -*- encoding: utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.helper(root)

    def helper(self, node):
        if self.is_leaf(node): return 1
        if not node.left:
            return 1 + self.helper(node.right)
        elif not node.right:
            return 1 + self.helper(node.left)
        else:
            return 1 + min(self.helper(node.left), self.helper(node.right))

    def is_leaf(self, node):
        return node and (not node.left and not node.right)