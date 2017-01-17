#-*- encoding: utf8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        self.res_dict = dict()
        self.helper(root, 0)
        res = []
        for i in range(len(self.res_dict)):
            res.append(self.res_dict[i].val)
        return res

    def helper(self, root, bfs_level):
        if not root: return
        self.res_dict[bfs_level] = root
        self.helper(root.left, bfs_level + 1)
        self.helper(root.right, bfs_level + 1)