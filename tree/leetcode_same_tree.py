#-*- encoding: utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.helper(p, q)

    def helper(self, p_root, q_root):
        if not self.same_node(p_root, q_root): return False
        if not p_root: return True
        return self.helper(p_root.left, q_root.left) and self.helper(p_root.right, q_root.right)

    def same_node(self, n1, n2):
        if not n1 and not n2: return True
        if not n1 or not n2: return False
        return n1.val == n2.val