#-*- encoding: utf8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        height = 0
        curr_node = root
        while curr_node:
            height += 1  # h(root) = 1
            curr_node = curr_node.left

        return 2 ** (height - 1) - 1 + self.helper(root, height)

    def helper(self, root, height):
        '''
            count nodes in last level
            binary-search
        '''
        if not root: return 0
        if height == 1: return 1

        mid_node = root.left
        curr_height = 2
        while curr_height < height:
            mid_node = mid_node.right
            curr_height += 1

        if mid_node:
            return 2 ** (height - 2) + self.helper(root.right, height - 1)
        else:
            return self.helper(root.left, height - 1)