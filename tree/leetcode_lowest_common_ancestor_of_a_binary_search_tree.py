# -*- encoding: utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = []
        self.find_path(root, p, p_path)
        q_path = []
        self.find_path(root, q, q_path)
        i, j = len(p_path) - 1, len(q_path) - 1
        while i > -1 and j > -1:
            if p_path[i].val != q_path[j].val:
                return p_path[i + 1]
            i -= 1
            j -= 1
        return p_path[i + 1]

    def find_path(self, root, target, res):
        '''
            find the top-down path from root to target
        :param root:
        :param target:
        :param res:
        :return:
        '''

        if not root:
            return False
        if root.val == target.val:
            tmp = True
        else:
            tmp = self.find_path(root.left, target, res) or self.find_path(root.right, target, res)
        if tmp:
            res.append(root)
        return tmp