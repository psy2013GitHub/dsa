#-*- encoding: utf8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root: return []
        res = []
        self.helper(root, '', res)
        return res

    def helper(self, node, prev_str, res):
        if not node:
            return
        if not prev_str:
            prev_str = '%d' % node.val
        else:
            prev_str += '->%d' % node.val
        if self.is_leaf(node):
            res.append(prev_str)
            return
        self.helper(node.left, prev_str, res)
        self.helper(node.right, prev_str, res)

    def is_leaf(self, node):
        return not node.left and not node.right