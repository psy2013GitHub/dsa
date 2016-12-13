#-*- encoding: utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = [[root.val,],]
        self.helper([root,], res)
        return res[::-1]

    def helper(self, prev_level_nodes, res):
        next_level_nodes, tmp = [], []
        for node in prev_level_nodes:
            if node:
                if node.left:
                    tmp.append(node.left.val)
                    next_level_nodes.append(node.left)
                if node.right:
                    tmp.append(node.right.val)
                    next_level_nodes.append(node.right)
        if len(tmp) > 0:
            res.append(tmp)
            self.helper(next_level_nodes, res)
