#-*- encoding: utf8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, s):
        return self.helper(root, s, [s])

    def helper(self, node, ori, tgts):
        if not node: return 0
        hit = 0
        for t in tgts:
            if not t-node.val: hit += 1
        tgts = [t-node.val for t in tgts]+[ori]         # update the targets
        return hit+self.helper(node.left, ori, tgts)+self.helper(node.right, ori, tgts)
