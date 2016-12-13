# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        tag = [True, ] # tag, pass by reference in python
        self.helper(root, tag)
        return tag[-1]

    def helper(self, root, tag):
        if not root:
            return 0
        h1, h2 = self.helper(root.left, tag), self.helper(root.right, tag)
        if h1 - h2 < -1 or h1 - h2 > 1:
            tag[-1] = False
        return 1 + max(h1, h2)