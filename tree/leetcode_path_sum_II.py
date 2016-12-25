#-*- encoding: utf8 -*-

# Definition for a binary tree node.
import copy
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root: return []
        self.helper(root, 0, sum, [], res)
        return res

    def helper(self, root, prev_sum, target, prev_nodes, res):
        prev_nodes = copy.copy(prev_nodes)
        prev_nodes.append(root.val)
        prev_sum += root.val
        if self.is_leaf(root):
            if prev_sum == target:
                res.append(prev_nodes)
            return
        if root.left:
            self.helper(root.left, prev_sum, target, prev_nodes, res)
        if root.right:
            self.helper(root.right, prev_sum, target, prev_nodes, res)

    def is_leaf(self, node):
        return node and not node.left and not node.right
