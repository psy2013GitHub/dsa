#-*- encoding: utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.iter_preorderTraversal(root)

    def iter_preorderTraversal(self, root):
        if not root: return []
        res, stack = [], []
        stack.append(root)
        while len(stack) > 0:
            curr_node = stack.pop()
            res.append(curr_node.val)
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
        return res